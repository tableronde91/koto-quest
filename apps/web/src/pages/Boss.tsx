import { useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router';
import { AnimatePresence, motion, useAnimationControls } from 'motion/react';
import { useQueryClient } from '@tanstack/react-query';
import { bossTimeLimitSec, simulateBoss } from '@koto/learning-engine';
import type { AvatarConfig, BossFightDto, BossOutcomeDto, MeDto, WorldBossDto } from '@koto/shared';
import { post } from '../api/client';
import { usePath } from '../api/hooks';
import { Question } from '../components/Question';
import { ErrorBox, Spinner } from '../components/ui';
import { Confetti, Stamp, useCalm } from '../components/Celebrate';
import { BossCreature, BossMood } from '../components/BossCreature';
import { Avatar } from '../components/Avatar';
import { T } from '../i18n';

/** Sceau du gardien : un grand caractère dans un cercle d'encre, comme un tampon. */
export function BossSeal({ glyph, size = 'lg', dim = false }: { glyph: string; size?: 'sm' | 'md' | 'lg'; dim?: boolean }) {
  const box = size === 'lg' ? 'h-40 w-40 text-8xl border-[6px]' : size === 'md' ? 'h-24 w-24 text-5xl border-4' : 'h-14 w-14 text-2xl border-[3px]';
  return (
    <span
      aria-hidden="true"
      className={`jp inline-flex shrink-0 items-center justify-center rounded-full font-black ${box}`}
      style={{ borderColor: dim ? 'var(--line)' : 'var(--ko)', color: dim ? 'var(--ink-soft)' : 'var(--ko)', background: 'var(--surface)' }}
    >
      {glyph}
    </span>
  );
}

function Hearts({ left, total }: { left: number; total: number }) {
  return (
    <span className="flex gap-1" role="img" aria-label={T("{0} cœur{1} sur {2}", [left, left > 1 ? 's' : '', total])}>
      {Array.from({ length: total }, (_, i) => (
        <svg key={i} width="26" height="26" viewBox="0 0 24 24" aria-hidden="true">
          <path
            d="M12 21s-7.5-4.6-9.6-9.2C.9 8.4 3 4.5 6.7 4.5c2.1 0 3.6 1.2 5.3 3 1.7-1.8 3.2-3 5.3-3 3.7 0 5.8 3.9 4.3 7.3C19.5 16.4 12 21 12 21z"
            fill={i < left ? 'var(--ko)' : 'none'}
            stroke={i < left ? 'var(--ko)' : 'var(--line)'}
            strokeWidth="2"
          />
        </svg>
      ))}
    </span>
  );
}

type Stage = { kind: 'intro' } | { kind: 'fight'; fight: BossFightDto } | { kind: 'finishing' } | { kind: 'done'; outcome: BossOutcomeDto; fight: BossFightDto };

export function BossPage({ me }: { me: MeDto }) {
  const { world = '' } = useParams();
  // Le niveau se lit dans le slug du monde (n5-w3, n4-w1…).
  const { data: path, isLoading } = usePath(world.split('-')[0].toUpperCase() || 'N5');
  const [stage, setStage] = useState<Stage>({ kind: 'intro' });
  const [error, setError] = useState<unknown>(null);
  const qc = useQueryClient();

  if (isLoading) return <Spinner />;
  const w = path?.worlds.find((x) => x.slug === world);
  if (!w?.boss) return <ErrorBox error={new Error(T("Ce monde n’a pas de gardien."))} />;
  const boss = w.boss;

  async function start() {
    setError(null);
    try {
      setStage({ kind: 'fight', fight: await post<BossFightDto>(`/worlds/${world}/boss/start`) });
    } catch (e) {
      setError(e);
    }
  }

  async function finish(fight: BossFightDto) {
    setStage({ kind: 'finishing' });
    try {
      const outcome = await post<BossOutcomeDto>(`/worlds/${world}/boss/finish`, { sessionId: fight.sessionId });
      setStage({ kind: 'done', outcome, fight });
      qc.invalidateQueries();
    } catch (e) {
      setError(e);
    }
  }

  if (error) return <div className="flex flex-col gap-4"><ErrorBox error={error} /><Link to="/path" className="underline">{T("Retour au parcours")}</Link></div>;
  if (stage.kind === 'fight') return <Fight fight={stage.fight} furigana={me.preferences.showFurigana} avatar={me.avatar} onEnd={() => finish(stage.fight)} />;
  if (stage.kind === 'finishing') return <Spinner label={T("Le combat s’achève…")} />;
  if (stage.kind === 'done') return <Outcome boss={boss} outcome={stage.outcome} onRetry={start} />;
  return <Intro boss={boss} worldTitle={w.title} onStart={start} />;
}

/** Nuage de fumée (apparition ou disparition du gardien). */
function Smoke({ calm }: { calm: boolean }) {
  if (calm) return null;
  return (
    <span aria-hidden="true" className="pointer-events-none absolute inset-0 flex items-center justify-center">
      {Array.from({ length: 8 }, (_, i) => {
        const a = (i / 8) * Math.PI * 2;
        return (
          <motion.span
            key={i}
            className="absolute h-16 w-16 rounded-full bg-[#E9E4DA]"
            initial={{ x: 0, y: 20, scale: 0.4, opacity: 0.95 }}
            animate={{ x: Math.cos(a) * 90, y: 20 + Math.sin(a) * 50, scale: 1.4, opacity: 0 }}
            transition={{ duration: 0.9, ease: 'easeOut' }}
          />
        );
      })}
    </span>
  );
}

function Intro({ boss, worldTitle, onStart }: { boss: WorldBossDto; worldTitle: string; onStart: () => void }) {
  const calm = useCalm();
  return (
    <div className="flex flex-col items-center gap-6 py-6 text-center">
      <Link to="/path" className="self-start text-ink-soft underline">← {worldTitle}</Link>
      <div className="relative flex flex-col items-center">
        <Smoke calm={calm} />
        <motion.div initial={{ scale: 0.2, opacity: 0, y: 30 }} animate={{ scale: 1, opacity: boss.available ? 1 : 0.55, y: 0 }} transition={{ type: 'spring', stiffness: 180, damping: 13, delay: 0.15 }}>
          <motion.div animate={calm ? undefined : { y: [0, -8, 0] }} transition={{ duration: 2.2, repeat: Infinity, ease: 'easeInOut' }} style={{ filter: boss.available ? undefined : 'grayscale(0.7)' }}>
            <BossCreature glyph={boss.glyph} mood={boss.defeated ? 'laugh' : 'angry'} size={200} title={boss.name} />
          </motion.div>
        </motion.div>
        <span className="-mt-3 h-4 w-40 rounded-[50%] bg-[rgb(0_0_0/0.12)]" aria-hidden="true" />
        <span className="absolute -right-6 top-0"><BossSeal glyph={boss.glyph} size="sm" dim={!boss.available} /></span>
      </div>
      <div>
        <p className="text-ink-soft">{T("Gardien de l’île")}</p>
        <h1 className="text-4xl">{boss.name}</h1>
      </div>
      <motion.p className="relative max-w-[46ch] rounded-2xl border border-line bg-surface px-5 py-3 text-lg" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.6 }}>
        <span aria-hidden="true" className="absolute -top-2 left-1/2 h-4 w-4 -translate-x-1/2 rotate-45 border-l border-t border-line bg-surface" />
        <span className="relative">« {boss.intro} »</span>
      </motion.p>
      {boss.available ? (
        <>
          <ul className="grid w-full max-w-xl grid-cols-1 gap-3 text-left sm:grid-cols-3">
            <li className="rounded-2xl border border-line bg-surface p-4"><strong className="block text-xl">{T("9 coups")}</strong><span className="text-sm text-ink-soft">{T("Chaque bonne réponse le frappe.")}</span></li>
            <li className="rounded-2xl border border-line bg-surface p-4"><strong className="block text-xl">{T("3 cœurs")}</strong><span className="text-sm text-ink-soft">{T("Chaque erreur t’en coûte un.")}</span></li>
            <li className="rounded-2xl border border-line bg-surface p-4"><strong className="block text-xl">⏱ 10 à 30 s</strong><span className="text-sm text-ink-soft">{T("Trop lent ? Le gardien riposte.")}</span></li>
          </ul>
          <button className="btn btn-gold min-h-14 px-10 text-lg" onClick={onStart}>{boss.defeated ? T("Rejouer le combat") : T("Affronter le gardien")}</button>
          {boss.defeated && <p className="text-sm text-ink-soft">{T("Déjà vaincu : rejouer rapporte peu d’XP, mais entretient ta mémoire.")}</p>}
        </>
      ) : (
        <p className="rounded-2xl bg-surface-2 p-4">{T("Termine toutes les leçons de cette île pour affronter son gardien.")}</p>
      )}
    </div>
  );
}

type Clash = { id: number; kind: 'hit' | 'counter' };

/** Arène : le gardien en haut à droite, ton personnage en bas à gauche, comme dans un RPG. */
function Arena({ fight, avatar, hpLeft, heartsLeft, clash, onFlee }: { fight: BossFightDto; avatar: AvatarConfig; hpLeft: number; heartsLeft: number; clash: Clash | null; onFlee: () => void }) {
  const calm = useCalm();
  const boss = useAnimationControls();
  const hero = useAnimationControls();
  const [mood, setMood] = useState<BossMood>('idle');
  const restMood: BossMood = hpLeft <= 3 ? 'angry' : 'idle';

  useEffect(() => {
    if (!clash) return;
    if (clash.kind === 'hit') {
      setMood('hurt');
      hero.start({ x: [0, 46, 0], y: [0, -16, 0], transition: { duration: 0.45 } });
      boss.start({ x: [0, 22, -8, 0], rotate: [0, 9, -4, 0], filter: ['brightness(1)', 'brightness(2.2)', 'brightness(1)'], transition: { duration: 0.5, delay: 0.15 } });
    } else {
      setMood('laugh');
      boss.start({ x: [0, -54, 0], y: [0, 18, 0], scale: [1, 1.18, 1], transition: { duration: 0.5 } });
      hero.start({ x: [0, -10, 9, -6, 4, 0], transition: { duration: 0.45, delay: 0.2 } });
    }
    const t = window.setTimeout(() => setMood(restMood), 900);
    return () => window.clearTimeout(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [clash?.id]);

  const shown: BossMood = clash && mood !== 'idle' && mood !== 'angry' ? mood : restMood;
  return (
    <section aria-label={T("Combat")} className="relative h-64 overflow-hidden rounded-3xl sm:h-72" style={{ background: 'linear-gradient(180deg,#2B3A67 0%,#7A5C8E 45%,#E79B6B 72%,#3F7D5A 72%,#2F6448 100%)' }}>
      {/* Décor : lune, montagnes, sol */}
      <span aria-hidden="true" className="absolute right-[38%] top-4 h-10 w-10 rounded-full bg-[#FFE7B3] opacity-80" />
      <svg aria-hidden="true" viewBox="0 0 400 120" preserveAspectRatio="none" className="absolute inset-x-0 top-[38%] h-[34%] w-full opacity-60">
        <path d="M0 120 L60 50 L110 100 L170 30 L240 110 L300 60 L360 100 L400 70 L400 120Z" fill="#3B2F52" />
      </svg>
      <span aria-hidden="true" className="absolute bottom-[28%] right-[5%] h-6 w-40 rounded-[50%] bg-[rgb(0_0_0/0.25)]" />
      <span aria-hidden="true" className="absolute bottom-5 left-[7%] h-5 w-32 rounded-[50%] bg-[rgb(0_0_0/0.25)]" />

      {/* Plaque du gardien */}
      <div className="absolute left-3 top-3 w-[58%] max-w-64 rounded-2xl bg-[rgb(255_255_255/0.92)] p-2.5 text-ink shadow">
        <div className="flex items-baseline justify-between gap-2">
          <p className="truncate text-sm font-bold">{fight.boss.name}</p>
          <p className="shrink-0 text-xs tabular-nums">{T("PV {0}/{1}", [ hpLeft , fight.rules.hp])}</p>
        </div>
        <div className="mt-1.5 h-2.5 overflow-hidden rounded-full bg-[#E3DED4]" role="progressbar" aria-label={T("Vie du gardien")} aria-valuenow={hpLeft} aria-valuemin={0} aria-valuemax={fight.rules.hp}>
          <motion.div className="h-full rounded-full" style={{ background: hpLeft <= 3 ? 'var(--ko)' : 'var(--ok)' }} animate={{ width: `${(hpLeft / fight.rules.hp) * 100}%` }} transition={{ duration: 0.4 }} />
        </div>
      </div>
      <button className="absolute right-2 top-2 rounded-full bg-[rgb(0_0_0/0.25)] p-2 text-white hover:bg-[rgb(0_0_0/0.4)]" aria-label={T("Fuir le combat")} onClick={onFlee}>
        <svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" /></svg>
      </button>

      {/* Gardien */}
      <motion.div className="absolute bottom-[30%] right-[4%] origin-bottom-right scale-[0.78] sm:scale-100" animate={boss}>
        <motion.div animate={calm ? undefined : shown === 'angry' ? { y: [0, -4, 0], rotate: [-2, 2, -2] } : { y: [0, -7, 0] }} transition={{ duration: shown === 'angry' ? 0.8 : 2, repeat: Infinity, ease: 'easeInOut' }}>
          <BossCreature glyph={fight.boss.glyph} mood={shown} size={160} title={fight.boss.name} />
        </motion.div>
      </motion.div>

      {/* Ton personnage */}
      <motion.div className="absolute bottom-6 left-[6%]" animate={hero}>
        <div className="overflow-hidden rounded-2xl border-[3px] border-white shadow-lg">
          <Avatar config={avatar} size={78} title={T("Toi")} />
        </div>
      </motion.div>
      <div className="absolute bottom-3 right-3 rounded-full bg-[rgb(255_255_255/0.92)] px-2 py-1">
        <Hearts left={heartsLeft} total={fight.rules.hearts} />
      </div>

      {/* Effets du coup */}
      <AnimatePresence>
        {clash?.kind === 'hit' && !calm && (
          <motion.div key={clash.id} aria-hidden="true" className="pointer-events-none absolute bottom-[32%] right-[6%] h-40 w-40 origin-bottom-right scale-[0.78] sm:scale-100" initial={{ opacity: 1 }} animate={{ opacity: 0 }} transition={{ duration: 0.4, delay: 0.55 }}>
            <svg viewBox="0 0 100 100" className="absolute inset-0">
              <motion.path d="M10 85 Q50 50 92 12" stroke="#FFFFFF" strokeWidth="7" fill="none" strokeLinecap="round" initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.18, delay: 0.15 }} />
              <motion.path d="M20 95 Q60 60 98 30" stroke="#FFE08A" strokeWidth="3" fill="none" strokeLinecap="round" initial={{ pathLength: 0 }} animate={{ pathLength: 1 }} transition={{ duration: 0.18, delay: 0.2 }} />
            </svg>
            {[0, 1, 2, 3].map((i) => (
              <motion.span key={i} className="absolute left-1/2 top-1/2 text-xl text-[#FFE08A]" initial={{ x: 0, y: 0, scale: 0.4 }} animate={{ x: Math.cos(i * 1.6) * 60, y: Math.sin(i * 1.6) * 50, scale: 1.2, opacity: 0 }} transition={{ duration: 0.6, delay: 0.2 }}>✦</motion.span>
            ))}
            <motion.span className="absolute left-1/3 top-6 font-display text-3xl font-black text-[#FFE08A] [text-shadow:0_2px_0_#7A2A1F]" initial={{ y: 10, opacity: 0 }} animate={{ y: -20, opacity: [0, 1, 1] }} transition={{ duration: 0.7, delay: 0.2 }}>−1</motion.span>
          </motion.div>
        )}
        {clash?.kind === 'counter' && !calm && (
          <motion.div key={clash.id} aria-hidden="true" className="pointer-events-none absolute inset-0">
            <motion.div className="absolute inset-0 bg-[#C8323F]" initial={{ opacity: 0 }} animate={{ opacity: [0, 0.35, 0] }} transition={{ duration: 0.5, delay: 0.2 }} />
            <motion.span className="absolute bottom-28 left-[9%] font-display text-2xl font-black text-white [text-shadow:0_2px_0_#7A2A1F]" initial={{ y: 0, opacity: 0 }} animate={{ y: -30, opacity: [0, 1, 0] }} transition={{ duration: 0.9, delay: 0.25 }}>−♥</motion.span>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}

function Fight({ fight, furigana, avatar, onEnd }: { fight: BossFightDto; furigana: boolean; avatar: AvatarConfig; onEnd: () => void }) {
  const [results, setResults] = useState<boolean[]>([]);
  const [index, setIndex] = useState(0);
  const [clash, setClash] = useState<Clash | null>(null);
  const navigate = useNavigate();
  const progress = simulateBoss(results, fight.rules);
  const hpLeft = fight.rules.hp - progress.hits;
  const q = fight.questions[index];

  function onResult(correct: boolean) {
    setResults((r) => [...r, correct]);
    // Bonne réponse : ton personnage frappe ; erreur : le gardien riposte.
    setClash((c) => ({ id: (c?.id ?? 0) + 1, kind: correct ? 'hit' : 'counter' }));
  }

  function next() {
    if (progress.state !== 'ongoing' || index + 1 >= fight.questions.length) onEnd();
    else setIndex(index + 1);
  }

  return (
    <div className="flex flex-col gap-5">
      <Arena fight={fight} avatar={avatar} hpLeft={hpLeft} heartsLeft={progress.heartsLeft} clash={clash} onFlee={() => navigate('/path')} />
      <p className="-mt-2 text-right text-sm text-ink-soft">{T("Question {0}", [ index + 1])}</p>
      <Question
        key={q.id}
        question={q}
        furigana={furigana}
        onResult={(r) => onResult(r.correct)}
        onDone={next}
        timeLimitSec={bossTimeLimitSec(q.type)}
        onShown={() => {
          post(`/questions/${q.id}/shown`).catch(() => undefined);
        }}
        continueLabel={(r) => {
          const after = simulateBoss([...results.slice(0, index), r.correct], fight.rules);
          return after.state === 'won' ? T("Coup final !") : after.state === 'lost' ? T("Voir le résultat") : T("Continuer");
        }}
      />
    </div>
  );
}

function Outcome({ boss, outcome, onRetry }: { boss: WorldBossDto; outcome: BossOutcomeDto; onRetry: () => void }) {
  const won = outcome.state === 'won';
  const calm = useCalm();
  return (
    <div className="flex flex-col items-center gap-5 py-8 text-center">
      {won && <Confetti count={60} />}
      <div className="relative flex flex-col items-center">
        {won && <Smoke calm={calm} />}
        {won ? (
          // Le gardien vacille, tourne sur lui-même et se rend (il reste visible, sonné).
          <motion.div initial={{ rotate: 0, scale: 1 }} animate={calm ? undefined : { rotate: [0, -12, 12, -8, 360], scale: [1, 1, 1, 1, 0.8], y: [0, 0, 0, 0, 12] }} transition={{ duration: 1.4 }}>
            <BossCreature glyph={boss.glyph} mood="ko" size={170} title={`${boss.name}, vaincu`} />
          </motion.div>
        ) : (
          <motion.div animate={calm ? undefined : { y: [0, -14, 0, -10, 0] }} transition={{ duration: 1.2, repeat: Infinity, repeatDelay: 0.6 }}>
            <BossCreature glyph={boss.glyph} mood="laugh" size={170} title={`${boss.name}, victorieux`} />
          </motion.div>
        )}
        <span className="-mt-2 h-4 w-36 rounded-[50%] bg-[rgb(0_0_0/0.12)]" aria-hidden="true" />
        {won && !calm && (
          <motion.span aria-hidden="true" className="absolute right-0 top-2 text-3xl" animate={{ rotate: 360 }} transition={{ duration: 2, repeat: Infinity, ease: 'linear' }}>💫</motion.span>
        )}
      </div>
      <Stamp className="jp text-6xl font-black text-ko">{won ? '勝利' : '敗北'}</Stamp>
      <h1 className="text-4xl">{won ? `${boss.name} est vaincu !` : T("Le gardien résiste…")}</h1>
      <p className="text-lg">{T("{0} coup{1} porté{2}, {3} cœur{4} restant{5}.", [ outcome.hits , outcome.hits > 1 ? 's' : '' , outcome.hits > 1 ? 's' : '' , outcome.heartsLeft , outcome.heartsLeft > 1 ? 's' : '' , outcome.heartsLeft > 1 ? 's' : '' ])}</p>
      <p className="font-bold text-gold-ink">{T("+{0} XP{1}", [ outcome.xpGained , outcome.coinsGained > 0 ? T(", +{0} pièces", [outcome.coinsGained]) : '' ])}</p>
      {!won && <p className="max-w-[46ch] text-ink-soft">{T("Les notions ratées reviendront dans tes révisions. Retente ta chance quand tu veux.")}</p>}
      <div className="flex flex-wrap justify-center gap-3">
        {!won && <button className="btn btn-gold" onClick={onRetry}>{T("Réessayer")}</button>}
        <Link to="/path" className={`btn ${won ? 'btn-gold' : 'btn-quiet'}`}>{T("Retour au parcours")}</Link>
      </div>
    </div>
  );
}
