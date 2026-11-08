import { useEffect, useMemo, useRef, useState } from 'react';
import { Link, useNavigate, useParams, useSearchParams } from 'react-router';
import { AnimatePresence, motion, useAnimationControls } from 'motion/react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { normalizeAvatar } from '@koto/learning-engine';
import type { DuelLeaderboardDto, DuelLobbyDto, DuelPlayerSearchDto, DuelQueueDto, DuelSideResultDto, DuelStateDto } from '@koto/shared';
import { LOCAL, api, del, post } from '../api/client';
import { ErrorBox, PageTitle, Spinner } from '../components/ui';
import { Avatar } from '../components/Avatar';
import { BossCreature, type BossMood } from '../components/BossCreature';
import { Confetti, CountUp, Stamp, useCalm } from '../components/Celebrate';
import { CrossedSwords, HpPlate, RankBadge } from '../components/DuelBits';
import { T } from '../i18n';

const JP_RE = /[぀-ヿ一-龯]/;
const KIND_LABEL = { ranked: T("Classé"), friendly: T("Amical"), practice: T("Entraînement") } as const;

// ═══════════════════════════ Dojo (hall des duels) ═══════════════════════════

export function DuelLobbyPage() {
  const nav = useNavigate();
  const qc = useQueryClient();
  const [params, setParams] = useSearchParams();
  const { data, error, isLoading, refetch } = useQuery({ queryKey: ['duels'], queryFn: () => api<DuelLobbyDto>('/duels'), refetchInterval: 5000 });
  const [searching, setSearching] = useState<string | null>(null);
  const [actionError, setActionError] = useState<unknown>(null);
  const [tab, setTab] = useState<'board' | 'history'>('board');
  const searchingRef = useRef<string | null>(null);
  searchingRef.current = searching;

  async function startSearch() {
    setActionError(null);
    try {
      const r = await post<DuelQueueDto>('/duels/queue');
      if (r.status === 'matched' && r.duelId) nav(`/duel/${r.duelId}`);
      else setSearching(r.since ?? new Date().toISOString());
    } catch (e) {
      setActionError(e);
    }
  }
  async function practice() {
    setActionError(null);
    try {
      if (searchingRef.current) await del('/duels/queue').catch(() => undefined);
      setSearching(null);
      const r = await post<{ duelId: string }>('/duels/practice');
      nav(`/duel/${r.duelId}`);
    } catch (e) {
      setActionError(e);
    }
  }
  async function cancelSearch() {
    setSearching(null);
    await del('/duels/queue').catch(() => undefined);
    qc.invalidateQueries({ queryKey: ['duels'] });
  }

  // Reprise d'une recherche en cours, ou lancement direct (« Nouveau duel classé »)
  useEffect(() => {
    if (data?.searching && !searching) setSearching(data.searching.since);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [data?.searching?.since]);
  useEffect(() => {
    if (params.get('search') === '1') {
      setParams({}, { replace: true });
      void startSearch();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Sondage de la file d'attente
  useEffect(() => {
    if (!searching) return;
    let stop = false;
    const tick = async () => {
      try {
        const r = await api<DuelQueueDto>('/duels/queue');
        if (stop) return;
        if (r.status === 'matched' && r.duelId) {
          searchingRef.current = null;
          nav(`/duel/${r.duelId}`);
        } else if (r.status === 'idle') setSearching(null);
      } catch {
        /* nouvelle tentative au prochain tour */
      }
    };
    const t = window.setInterval(tick, LOCAL ? 700 : 1200);
    void tick();
    return () => {
      stop = true;
      window.clearInterval(t);
    };
  }, [searching, nav]);
  // En quittant la page, on quitte la file
  useEffect(() => () => void (searchingRef.current && del('/duels/queue').catch(() => undefined)), []);

  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  const p = data.profile;
  const played = p.wins + p.losses + p.draws;

  return (
    <div className="flex flex-col gap-6">
      <PageTitle sub={T("Affronte d’autres apprentis en temps réel : même question, même chrono. Plus tu réponds vite, plus tu frappes fort.")}>{T("Duels")}</PageTitle>
      {!data.online && (
        <p className="rounded-2xl border-2 border-dashed border-line p-3 text-sm text-ink-soft">{T("Mode hors ligne : tes adversaires sont simulés et le classement est fictif. Les duels contre de vrais joueurs et les défis entre amis demandent la version en ligne.")}</p>
      )}

      {/* Écusson et palmarès */}
      <section className="relative overflow-hidden rounded-3xl p-5 text-white sm:p-6" style={{ background: `radial-gradient(circle at 15% 20%, ${p.rank.color}55, transparent 55%), linear-gradient(135deg,#1B2550,#3B2F62 60%,#5A2A45)` }}>
        <div className="flex flex-col items-center gap-5 sm:flex-row sm:items-center">
          <RankBadge rank={p.rank} size={110} glow />
          <div className="flex w-full flex-1 flex-col gap-2 text-center sm:text-left">
            <p className="text-sm font-bold uppercase tracking-wider opacity-80">{T("Ton rang")}</p>
            <h2 className="text-3xl leading-tight">{p.rank.label}</h2>
            <p className="text-lg">
              <span className="font-display text-2xl tabular-nums">{p.rating}</span>{' '}{T("points")}{played > 0 && <span className="opacity-80">{T("· {0}ᵉ sur {1}", [ p.position , p.players])}</span>}
            </p>
            {p.rank.next !== null && (
              <div className="flex flex-col gap-1">
                <div className="h-2.5 overflow-hidden rounded-full bg-[rgb(255_255_255/0.2)]" role="progressbar" aria-label={T("Progression vers la division suivante")} aria-valuenow={Math.round(p.rank.progress * 100)} aria-valuemin={0} aria-valuemax={100}>
                  <motion.div className="h-full rounded-full" style={{ background: p.rank.color }} initial={{ width: 0 }} animate={{ width: `${p.rank.progress * 100}%` }} transition={{ duration: 0.8 }} />
                </div>
                <p className="text-sm opacity-80">{T("Encore {0} points pour la division suivante", [ Math.max(1, p.rank.next - p.rating) ])}</p>
              </div>
            )}
          </div>
        </div>
        <dl className="mt-5 grid grid-cols-2 gap-2 sm:grid-cols-4">
          {[
            [T("Victoires"), p.wins],
            [T("Défaites"), p.losses],
            [T("Série"), p.streak > 0 ? `🔥 ${p.streak}` : '0'],
            [T("Record"), T("{0} pts", [p.peakRating])],
          ].map(([k, v]) => (
            <div key={k} className="rounded-2xl bg-[rgb(255_255_255/0.1)] px-3 py-2 text-center">
              <dt className="text-xs opacity-80">{k}</dt>
              <dd className="font-display text-xl tabular-nums">{v}</dd>
            </div>
          ))}
        </dl>
      </section>

      {actionError != null && <ErrorBox error={actionError} />}

      {data.activeDuelId && (
        <Link to={`/duel/${data.activeDuelId}`} className="flex items-center gap-3 rounded-3xl border-2 border-ko bg-ko-bg p-4 font-bold">
          <span aria-hidden="true" className="jp text-3xl text-ko">戦</span>
          <span className="flex-1">{T("Un duel est en cours : reviens vite, sinon il sera perdu par abandon.")}</span>
          <span className="btn btn-primary">{T("Reprendre")}</span>
        </Link>
      )}

      {data.invites.map((inv) => (
        <InviteCard key={inv.id} invite={inv} onDone={() => qc.invalidateQueries({ queryKey: ['duels'] })} />
      ))}

      {/* Modes de jeu */}
      <section className="grid gap-4 md:grid-cols-3">
        <ModeCard glyph="闘" color="#C8323F" title={T("Duel classé")} text={T("Un adversaire de ton niveau, au hasard. Gagne des points pour monter de rang.")} action={T("Trouver un adversaire")} onClick={startSearch} primary />
        <ModeCard glyph="友" color="#3FA7A0" title={T("Défier un ami")} text={T("Envoie un défi avec son code de duelliste. Duel amical, sans effet sur le classement.")} action={T("Voir ci-dessous")} onClick={() => document.getElementById('defi')?.scrollIntoView({ behavior: 'smooth' })} />
        <ModeCard glyph="浪" color="#7B5BD6" title={T("Entraînement")} text={T("Contre un rōnin (IA) de ton niveau. Idéal pour apprendre le rythme.")} action={T("S’entraîner")} onClick={practice} />
      </section>

      <ChallengePanel lobby={data} onChange={() => qc.invalidateQueries({ queryKey: ['duels'] })} />

      {/* Classement et historique */}
      <section className="flex flex-col gap-4">
        <div role="tablist" aria-label={T("Classement et historique")} className="flex gap-2">
          {(['board', 'history'] as const).map((t) => (
            <button key={t} role="tab" aria-selected={tab === t} className={`rounded-full px-4 py-2 font-bold ${tab === t ? 'bg-ink text-paper' : 'bg-surface-2 text-ink-soft'}`} onClick={() => setTab(t)}>
              {t === 'board' ? T("Classement") : T("Mes duels")}
            </button>
          ))}
        </div>
        {tab === 'board' ? <Leaderboard /> : <History lobby={data} />}
      </section>

      <Rules lobby={data} />

      <AnimatePresence>{searching && <SearchingOverlay since={searching} onCancel={cancelSearch} onPractice={practice} />}</AnimatePresence>
    </div>
  );
}

function ModeCard({ glyph, color, title, text, action, onClick, primary }: { glyph: string; color: string; title: string; text: string; action: string; onClick: () => void; primary?: boolean }) {
  return (
    <motion.div whileHover={{ y: -3 }} className="flex flex-col gap-3 rounded-3xl border border-line bg-surface p-5">
      <span aria-hidden="true" className="jp flex h-14 w-14 items-center justify-center rounded-2xl text-3xl font-black text-white" style={{ background: color }}>{glyph}</span>
      <h2 className="text-xl">{title}</h2>
      <p className="flex-1 text-ink-soft">{text}</p>
      <button className={`btn ${primary ? 'btn-gold' : 'btn-quiet'}`} onClick={onClick}>{action}</button>
    </motion.div>
  );
}

function SearchingOverlay({ since, onCancel, onPractice }: { since: string; onCancel: () => void; onPractice: () => void }) {
  const [, force] = useState(0);
  useEffect(() => {
    const t = window.setInterval(() => force((x) => x + 1), 500);
    return () => window.clearInterval(t);
  }, []);
  const elapsed = Math.max(0, Math.floor((Date.now() - Date.parse(since)) / 1000));
  return (
    <motion.div className="fixed inset-0 z-50 flex items-center justify-center bg-[rgb(10_14_40/0.7)] p-4" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
      <motion.div role="dialog" aria-modal="true" aria-labelledby="search-title" className="flex w-full max-w-sm flex-col items-center gap-4 rounded-3xl bg-surface p-6 text-center" initial={{ scale: 0.9 }} animate={{ scale: 1 }}>
        <CrossedSwords size={110} spin />
        <h2 id="search-title" className="text-2xl">{T("Recherche d’un adversaire…")}</h2>
        <p className="font-display text-3xl tabular-nums" aria-live="off">{Math.floor(elapsed / 60)}:{String(elapsed % 60).padStart(2, '0')}</p>
        <p className="text-ink-soft">{T("Garde cette page ouverte : le duel commence dès qu’un joueur est trouvé.")}</p>
        {elapsed >= 20 && (
          <motion.div initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} className="flex flex-col gap-2 rounded-2xl bg-surface-2 p-3">
            <p className="text-sm">{T("Peu de monde en ligne en ce moment. Tu peux t’entraîner contre un rōnin en attendant.")}</p>
            <button className="btn btn-quiet" onClick={onPractice}>{T("Affronter un rōnin")}</button>
          </motion.div>
        )}
        <button className="btn btn-primary w-full" onClick={onCancel}>{T("Annuler")}</button>
      </motion.div>
    </motion.div>
  );
}

function InviteCard({ invite, onDone }: { invite: DuelLobbyDto['invites'][number]; onDone: () => void }) {
  const nav = useNavigate();
  const [err, setErr] = useState<unknown>(null);
  return (
    <motion.div layout initial={{ opacity: 0, y: -8 }} animate={{ opacity: 1, y: 0 }} className="flex flex-col gap-3 rounded-3xl border-2 border-gold bg-surface p-4 sm:flex-row sm:items-center">
      <div className="flex flex-1 items-center gap-3">
        <RankBadge rank={invite.player.rank} size={40} />
        <p>
          <strong>{invite.player.name}</strong> ({invite.player.rank.label}{T(") te défie en duel !")}</p>
      </div>
      {err != null && <ErrorBox error={err} />}
      <div className="flex gap-2">
        <button className="btn btn-gold" onClick={async () => { try { const r = await post<{ duelId: string }>(`/duels/${invite.id}/accept`); nav(`/duel/${r.duelId}`); } catch (e) { setErr(e); onDone(); } }}>{T("Accepter")}</button>
        <button className="btn btn-quiet" onClick={async () => { await post(`/duels/${invite.id}/decline`).catch(() => undefined); onDone(); }}>{T("Refuser")}</button>
      </div>
    </motion.div>
  );
}

function ChallengePanel({ lobby, onChange }: { lobby: DuelLobbyDto; onChange: () => void }) {
  const nav = useNavigate();
  const [q, setQ] = useState('');
  const [copied, setCopied] = useState(false);
  const [err, setErr] = useState<unknown>(null);
  const term = q.trim();
  const { data } = useQuery({ queryKey: ['duel-players', term], queryFn: () => api<DuelPlayerSearchDto>(`/duels/players?q=${encodeURIComponent(term)}`), enabled: lobby.online && term.length >= 2 });

  async function challenge(target: { code?: string; userId?: string }) {
    setErr(null);
    try {
      const r = await post<{ duelId: string }>('/duels/challenges', target);
      onChange();
      nav(`/duel/${r.duelId}`);
    } catch (e) {
      setErr(e);
    }
  }
  const looksLikeCode = /^(KQ-?)?[A-Z0-9]{6}$/i.test(term);

  return (
    <section id="defi" className="flex flex-col gap-4 rounded-3xl border border-line bg-surface p-5">
      <h2 className="text-xl">{T("Défier un ami")}</h2>
      <div className="flex flex-wrap items-center gap-3 rounded-2xl bg-surface-2 p-3">
        <span className="text-ink-soft">{T("Ton code de duelliste :")}</span>
        <code className="font-display text-xl tracking-wider">{lobby.profile.code}</code>
        <button
          className="btn btn-quiet min-h-10 px-3 text-sm"
          onClick={async () => {
            try {
              await navigator.clipboard.writeText(lobby.profile.code);
              setCopied(true);
              window.setTimeout(() => setCopied(false), 1500);
            } catch {
              /* presse-papiers indisponible */
            }
          }}
        >
          {copied ? T("Copié ✓") : T("Copier")}
        </button>
      </div>
      {lobby.online ? (
        <>
          <form
            className="flex flex-col gap-2 sm:flex-row"
            onSubmit={(e) => {
              e.preventDefault();
              if (looksLikeCode) void challenge({ code: term });
            }}
          >
            <label className="sr-only" htmlFor="duel-search">{T("Code ou nom du joueur")}</label>
            <input id="duel-search" value={q} onChange={(e) => setQ(e.target.value)} placeholder={T("Code (KQ-…) ou nom du joueur")} className="min-h-12 flex-1 rounded-xl border-2 border-line bg-surface px-3" autoComplete="off" />
            <button type="submit" className="btn btn-primary" disabled={!looksLikeCode}>{T("Défier ce code")}</button>
          </form>
          {err != null && <ErrorBox error={err} />}
          {data && data.players.length > 0 && (
            <ul className="flex flex-col gap-2">
              {data.players.map((pl) => (
                <li key={pl.userId} className="flex items-center gap-3 rounded-2xl border border-line p-2">
                  <RankBadge rank={pl.rank} size={32} />
                  <span className="flex-1"><strong>{pl.name}</strong> <span className="text-sm text-ink-soft">· {pl.rank.label} · {pl.code}</span></span>
                  <button className="btn btn-gold min-h-10 px-3" onClick={() => challenge({ userId: pl.userId! })}>{T("Défier")}</button>
                </li>
              ))}
            </ul>
          )}
          {data && term.length >= 2 && data.players.length === 0 && <p className="text-ink-soft">{T("Aucun duelliste trouvé.")}</p>}
          {lobby.sent.length > 0 && (
            <div className="flex flex-col gap-2">
              <h3 className="font-bold">{T("Défis envoyés")}</h3>
              {lobby.sent.map((s) => (
                <div key={s.id} className="flex items-center gap-3 rounded-2xl bg-surface-2 p-2">
                  <span className="flex-1">{T("En attente de")}{' '}<strong>{s.player.name}</strong>…</span>
                  <Link className="btn btn-quiet min-h-10 px-3" to={`/duel/${s.id}`}>{T("Voir")}</Link>
                  <button className="btn btn-quiet min-h-10 px-3" onClick={async () => { await post(`/duels/${s.id}/decline`).catch(() => undefined); onChange(); }}>{T("Annuler")}</button>
                </div>
              ))}
            </div>
          )}
        </>
      ) : (
        <p className="text-ink-soft">{T("Disponible dans la version en ligne : partage ton code, ton ami le saisit, et le duel commence dès qu’il accepte.")}</p>
      )}
    </section>
  );
}

function Leaderboard() {
  const [sort, setSort] = useState<'rating' | 'wins'>('rating');
  const { data, isLoading, error, refetch } = useQuery({ queryKey: ['duel-board', sort], queryFn: () => api<DuelLeaderboardDto>(`/duels/leaderboard?sort=${sort}`) });
  return (
    <div className="flex flex-col gap-3">
      <div className="flex items-center gap-2 text-sm">
        <span className="text-ink-soft">{T("Trier par")}</span>
        {(['rating', 'wins'] as const).map((s) => (
          <button key={s} aria-pressed={sort === s} className={`rounded-full border-2 px-3 py-1 font-bold ${sort === s ? 'border-ink' : 'border-line text-ink-soft'}`} onClick={() => setSort(s)}>
            {s === 'rating' ? T("Points") : T("Victoires")}
          </button>
        ))}
      </div>
      {isLoading ? (
        <Spinner />
      ) : error || !data ? (
        <ErrorBox error={error} onRetry={refetch} />
      ) : data.entries.length === 0 ? (
        <p className="rounded-2xl bg-surface-2 p-4 text-ink-soft">{T("Personne n’est encore classé. Gagne un duel classé pour ouvrir le tableau !")}</p>
      ) : (
        <ol className="flex flex-col gap-1.5" aria-label={T("Classement des duellistes")}>
          {data.entries.map((e) => (
            <motion.li key={e.userId} initial={{ opacity: 0, x: -8 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: Math.min(0.4, e.position * 0.03) }} className={`flex items-center gap-3 rounded-2xl px-3 py-2 ${e.me ? 'bg-gold text-[#2a1a00]' : 'bg-surface'}`}>
              <span className="w-8 text-center font-display text-lg tabular-nums">{e.position <= 3 ? ['🥇', '🥈', '🥉'][e.position - 1] : e.position}</span>
              <RankBadge rank={e.rank} size={30} />
              <span className="min-w-0 flex-1">
                <span className="block truncate font-bold">{e.name}{e.me ? ' (toi)' : ''}</span>
                <span className={`block text-xs ${e.me ? '' : 'text-ink-soft'}`}>{e.rank.label}</span>
              </span>
              <span className="text-right text-sm tabular-nums">
                <strong className="block">{sort === 'wins' ? `${e.wins} V` : T("{0} pts", [e.rating])}</strong>
                <span className={e.me ? '' : 'text-ink-soft'}>{sort === 'wins' ? T("{0} pts", [e.rating]) : `${e.wins} V · ${e.losses} D`}</span>
              </span>
            </motion.li>
          ))}
        </ol>
      )}
      {data?.me && !data.entries.some((e) => e.me) && <p className="text-sm text-ink-soft">{T("Ta place : {0}ᵉ ({1} pts, {2} victoires)", [ data.me.position , data.me.rating , data.me.wins ])}</p>}
    </div>
  );
}

function History({ lobby }: { lobby: DuelLobbyDto }) {
  if (lobby.history.length === 0) return <p className="rounded-2xl bg-surface-2 p-4 text-ink-soft">{T("Aucun duel pour l’instant. Ton premier combat t’attend !")}</p>;
  return (
    <ul className="flex flex-col gap-2">
      {lobby.history.map((h) => (
        <li key={h.id} className="flex items-center gap-3 rounded-2xl border border-line bg-surface p-3">
          <span aria-hidden="true" className={`jp flex h-10 w-10 items-center justify-center rounded-xl text-xl font-black text-white ${h.result === 'win' ? 'bg-ok' : h.result === 'loss' ? 'bg-ko' : 'bg-ink-soft'}`}>{h.result === 'win' ? '勝' : h.result === 'loss' ? '負' : '分'}</span>
          <span className="flex-1">
            <strong>{h.result === 'win' ? T("Victoire") : h.result === 'loss' ? T("Défaite") : T("Égalité")}</strong>{' '}{T("contre")}{' '}{h.opponent}
            <span className="block text-sm text-ink-soft">{T("{0} · {1} · PV {2} – {3}", [KIND_LABEL[h.kind] , h.endReason === 'ko' ? 'K.-O.' : h.endReason === 'forfeit' ? 'abandon' : 'aux points' , h.myHp , h.oppHp])}</span>
          </span>
          {h.delta !== null && <span className={`font-display text-lg tabular-nums ${h.delta >= 0 ? 'text-ok' : 'text-ko'}`}>{h.delta >= 0 ? '+' : ''}{h.delta}</span>}
        </li>
      ))}
    </ul>
  );
}

function Rules({ lobby }: { lobby: DuelLobbyDto }) {
  return (
    <details className="rounded-3xl bg-surface-2 p-5">
      <summary className="cursor-pointer text-lg font-bold">{T("Comment se déroule un duel ?")}</summary>
      <ul className="mt-3 flex list-disc flex-col gap-1.5 pl-5 text-ink-soft">
        <li>{T("Chacun commence avec {0} PV. {1} questions au maximum, {2} secondes chacune, la même pour les deux.", [ lobby.rules.hp , lobby.rules.rounds , lobby.rules.roundMs / 1000 ])}</li>
        <li>{T("Une bonne réponse frappe l’adversaire : de 8 à 26 dégâts selon ta vitesse. Sous 2 secondes, c’est un coup critique (+6).")}</li>
        <li>{T("Les bonnes réponses enchaînées ajoutent un combo (jusqu’à +6). Une erreur ne fait rien… mais casse ton combo.")}</li>
        <li>{T("Celui qui tombe à 0 PV perd. Sinon, après la dernière question, le plus de PV l’emporte.")}</li>
        <li>{T("Les duels classés font gagner ou perdre des points : battre plus fort que soi rapporte davantage. Rangs : Ashigaru, Samouraï, Kengō, Daimyō, Shōgun, Tenkabito.")}</li>
        <li>{T("Quitter un duel en cours compte comme un abandon.")}</li>
      </ul>
    </details>
  );
}

// ═══════════════════════════ Arène ═══════════════════════════

interface Clash {
  id: number;
  mine: { damage: number; critical: boolean; combo: number };
  theirs: { damage: number; critical: boolean; combo: number };
}

export function DuelArenaPage() {
  const { id = '' } = useParams();
  const nav = useNavigate();
  const qc = useQueryClient();
  const offset = useRef(0);
  const { data: s, error, refetch } = useQuery({
    queryKey: ['duel', id],
    queryFn: async () => {
      const r = await api<DuelStateDto>(`/duels/${id}`);
      offset.current = Date.parse(r.serverNow) - Date.now();
      return r;
    },
    refetchInterval: (q) => {
      const st = q.state.data?.status;
      return st === 'active' ? 600 : st === 'pending' ? 2000 : false;
    },
  });
  const [, setTick] = useState(0);
  useEffect(() => {
    const t = window.setInterval(() => setTick((x) => x + 1), 100);
    return () => window.clearInterval(t);
  }, []);
  const now = Date.now() + offset.current;

  // Relance exactement au début de chaque question
  useEffect(() => {
    if (!s?.roundStartsAt || s.status !== 'active') return;
    const wait = Date.parse(s.roundStartsAt) - (Date.now() + offset.current);
    if (wait <= 0) return;
    const t = window.setTimeout(() => void refetch(), wait + 40);
    return () => window.clearTimeout(t);
  }, [s?.roundStartsAt, s?.status, refetch]);

  // Échanges de coups à chaque correction
  const [clash, setClash] = useState<Clash | null>(null);
  const lastIndex = useRef<number | null>(null);
  useEffect(() => {
    const idx = s?.last?.question.index ?? null;
    if (idx === null || !s?.last) return;
    if (lastIndex.current === null) {
      lastIndex.current = idx;
      return;
    }
    if (idx !== lastIndex.current) {
      lastIndex.current = idx;
      setClash({ id: idx, mine: s.last.me, theirs: s.last.opponent });
    }
  }, [s?.last]);

  // Le résultat s'affiche après le dernier échange
  const [showResult, setShowResult] = useState(false);
  useEffect(() => {
    if (s?.status !== 'finished') return;
    const t = window.setTimeout(() => setShowResult(true), s.result?.endReason === 'forfeit' ? 0 : 1800);
    return () => window.clearTimeout(t);
  }, [s?.status, s?.result?.endReason]);

  const [picked, setPicked] = useState<{ round: number; answer: string } | null>(null);
  const [confirmQuit, setConfirmQuit] = useState(false);

  // Une erreur passagère pendant le duel ne doit pas masquer l'arène : le sondage suivant reprend la main.
  if (error && !s) return <ErrorBox error={error} onRetry={refetch} />;
  if (!s) return <Spinner label={T("Entrée dans l’arène…")} />;

  if (s.status === 'pending') return <PendingView s={s} now={now} onChange={() => qc.invalidateQueries({ queryKey: ['duel', id] })} />;
  if (s.status === 'declined' || s.status === 'cancelled' || s.status === 'expired')
    return (
      <div className="flex flex-col items-center gap-4 py-10 text-center">
        <CrossedSwords size={90} />
        <h1 className="text-3xl">{s.status === 'declined' ? T("Défi refusé") : s.status === 'expired' ? T("Défi expiré") : T("Défi annulé")}</h1>
        <p className="text-ink-soft">{s.status === 'declined' ? T("{0} a décliné le duel.", [s.opponent.name]) : s.status === 'expired' ? T("Personne n’a répondu à temps.") : T("Ce défi a été annulé.")}</p>
        <Link to="/duel" className="btn btn-primary">{T("Retour au dojo")}</Link>
      </div>
    );
  if (s.status === 'finished' && showResult && s.result) return <ResultView s={s} />;

  const start = s.roundStartsAt ? Date.parse(s.roundStartsAt) : now;
  const countdown = s.status === 'active' && s.round === 0 && now < start;
  const q = s.question;
  const myPick = picked && q && picked.round === q.index ? picked.answer : null;
  const remaining = q ? Math.max(0, s.rules.roundMs - (now - start)) : 0;
  const answered = !!s.mine || !!myPick;

  async function choose(answer: string) {
    if (!q || answered) return;
    setPicked({ round: q.index, answer });
    try {
      const r = await post<DuelStateDto>(`/duels/${id}/answer`, { round: q.index, answer });
      qc.setQueryData(['duel', id], r);
    } catch {
      void refetch();
    }
  }

  return (
    <div className="mx-auto flex w-full max-w-3xl flex-col gap-4">
      <DuelStage s={s} clash={clash} countdown={countdown ? Math.ceil((start - now) / 1000) : null} onQuit={() => setConfirmQuit(true)} />

      {/* Chrono de la question */}
      {q && (
        <div className="h-2.5 overflow-hidden rounded-full bg-surface-2" role="progressbar" aria-label={T("Temps restant")} aria-valuenow={Math.ceil(remaining / 1000)} aria-valuemin={0} aria-valuemax={s.rules.roundMs / 1000}>
          <div className="h-full rounded-full transition-[width] duration-100 ease-linear" style={{ width: `${(remaining / s.rules.roundMs) * 100}%`, background: remaining < 3000 ? 'var(--ko)' : 'var(--gold)' }} />
        </div>
      )}

      <AnimatePresence mode="wait">
        {q ? (
          <motion.section key={`q${q.index}`} initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }} className="flex flex-col gap-4" aria-label={T("Question {0}", [q.index + 1])}>
            <div className="flex items-baseline justify-between gap-3">
              <p className="text-lg font-bold">{q.prompt}</p>
              <p className="shrink-0 text-sm text-ink-soft tabular-nums">{T("Question {0}/{1} · {2} s", [ q.index + 1 , s.rules.rounds , Math.ceil(remaining / 1000) ])}</p>
            </div>
            {(q.display?.jp || q.display?.text) && (
              <div className="flex min-h-24 flex-col items-center justify-center rounded-3xl bg-surface-2 p-4 text-center">
                {q.display?.jp && <p lang="ja" className={`jp font-bold ${[...q.display.jp].length <= 3 ? 'text-6xl' : 'text-4xl'}`}>{q.display.jp}</p>}
                {q.display?.text && <p className={q.display.jp ? 'text-ink-soft' : 'text-2xl font-bold'}>{q.display.text}</p>}
              </div>
            )}
            <div className="grid grid-cols-2 gap-3">
              {q.choices.map((c) => {
                const mine = (s.mine?.answer ?? myPick) === c;
                const verdict = mine && s.mine ? (s.mine.correct ? 'ok' : 'ko') : null;
                return (
                  <motion.button
                    key={c}
                    whileTap={answered ? undefined : { scale: 0.96 }}
                    disabled={answered}
                    onClick={() => choose(c)}
                    className={`min-h-16 rounded-2xl border-2 px-3 py-2 text-lg font-bold transition-colors ${JP_RE.test(c) ? 'jp text-2xl' : ''}`}
                    style={{
                      borderColor: verdict === 'ok' ? 'var(--ok)' : verdict === 'ko' ? 'var(--ko)' : mine ? 'var(--ink)' : 'var(--line)',
                      background: verdict === 'ok' ? 'var(--ok-bg)' : verdict === 'ko' ? 'var(--ko-bg)' : 'var(--surface)',
                      opacity: answered && !mine ? 0.55 : 1,
                    }}
                  >
                    <span lang={JP_RE.test(c) ? 'ja' : 'fr'}>{c}</span>
                  </motion.button>
                );
              })}
            </div>
            <div aria-live="polite" className="min-h-8 text-center font-bold">
              {s.mine ? (
                s.mine.correct ? (
                  <motion.p initial={{ scale: 0.8, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} className="text-ok">{T("Juste ! Tu prépares un coup de")}{' '}{s.mine.damage} {s.mine.critical && <span className="text-ko">{T("· CRITIQUE")}</span>}
                    {s.mine.combo >= 2 && <span className="text-gold-ink">{T("· combo ×{0}", [ s.mine.combo])}</span>}
                  </motion.p>
                ) : (
                  <motion.p initial={{ x: -6 }} animate={{ x: [6, -4, 0] }} className="text-ko">{T("Raté… pas de coup cette fois.")}</motion.p>
                )
              ) : myPick ? (
                <p className="text-ink-soft">…</p>
              ) : null}
            </div>
          </motion.section>
        ) : s.last ? (
          <RevealView key={`r${s.last.question.index}`} s={s} />
        ) : (
          <motion.p key="wait" className="py-6 text-center text-lg text-ink-soft" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>{T("Prépare-toi : la première question arrive…")}</motion.p>
        )}
      </AnimatePresence>

      <AnimatePresence>
        {confirmQuit && (
          <motion.div className="fixed inset-0 z-50 flex items-center justify-center bg-[rgb(10_14_40/0.6)] p-4" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
            <div role="dialog" aria-modal="true" aria-labelledby="quit-title" className="flex w-full max-w-sm flex-col gap-4 rounded-3xl bg-surface p-6 text-center">
              <h2 id="quit-title" className="text-2xl">{T("Abandonner le duel ?")}</h2>
              <p className="text-ink-soft">{s.kind === 'ranked' ? T("Tu perdras le duel et des points de classement.") : T("Tu perdras ce duel.")}</p>
              <div className="flex flex-col gap-2">
                <button className="btn btn-primary" onClick={() => setConfirmQuit(false)}>{T("Continuer le combat")}</button>
                <button
                  className="btn btn-quiet text-ko"
                  onClick={async () => {
                    setConfirmQuit(false);
                    if (s.status !== 'active') return nav('/duel');
                    const r = await post<DuelStateDto>(`/duels/${id}/forfeit`).catch(() => null);
                    if (r) qc.setQueryData(['duel', id], r);
                  }}
                >{T("Abandonner")}</button>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

/** Scène du duel : les deux combattants face à face, leurs PV et les coups échangés. */
function DuelStage({ s, clash, countdown, onQuit }: { s: DuelStateDto; clash: Clash | null; countdown: number | null; onQuit: () => void }) {
  const calm = useCalm();
  const me = useAnimationControls();
  const opp = useAnimationControls();
  const [oppMood, setOppMood] = useState<BossMood>('idle');
  const [fx, setFx] = useState<Clash | null>(null);
  const myAvatar = useMemo(() => normalizeAvatar(s.me.avatar), [s.me.avatar]);
  const oppAvatar = useMemo(() => normalizeAvatar(s.opponent.avatar), [s.opponent.avatar]);

  useEffect(() => {
    if (!clash) return;
    setFx(clash);
    const hitOpp = clash.mine.damage > 0;
    const hitMe = clash.theirs.damage > 0;
    if (!calm) {
      if (hitOpp) {
        void me.start({ x: [0, 60, 0], y: [0, -14, 0], transition: { duration: 0.45 } });
        void opp.start({ x: [0, 18, -6, 0], filter: ['brightness(1)', 'brightness(2)', 'brightness(1)'], transition: { duration: 0.45, delay: 0.2 } });
      }
      if (hitMe) {
        void opp.start({ x: [0, -60, 0], y: [0, -14, 0], transition: { duration: 0.45, delay: hitOpp ? 0.7 : 0 } });
        void me.start({ x: [0, -16, 6, 0], filter: ['brightness(1)', 'brightness(2)', 'brightness(1)'], transition: { duration: 0.45, delay: hitOpp ? 0.9 : 0.2 } });
      }
    }
    setOppMood(hitOpp ? 'hurt' : hitMe ? 'laugh' : 'idle');
    const t = window.setTimeout(() => {
      setOppMood('idle');
      setFx(null);
    }, 1900);
    return () => window.clearTimeout(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [clash?.id]);

  const koMe = s.status === 'finished' && s.me.hp <= 0;
  const koOpp = s.status === 'finished' && s.opponent.hp <= 0;
  return (
    <section aria-label={T("Arène du duel")} className="relative h-72 overflow-hidden rounded-3xl sm:h-80" style={{ background: 'linear-gradient(180deg,#1E2A55 0%,#5B3F78 46%,#C9785C 70%,#6B4A33 70%,#4E3524 100%)' }}>
      {/* Décor : lune, torii lointain, tatamis */}
      <span aria-hidden="true" className="absolute right-[26%] top-[36%] h-10 w-10 rounded-full bg-[#FFE7B3] opacity-70" />
      <svg aria-hidden="true" viewBox="0 0 400 120" preserveAspectRatio="none" className="absolute inset-x-0 top-[40%] h-[30%] w-full opacity-50">
        <path d="M0 120 L70 60 L120 100 L190 40 L250 110 L320 55 L400 95 L400 120Z" fill="#2E2147" />
        <g fill="#8E1B26"><rect x="186" y="62" width="4" height="30" /><rect x="208" y="62" width="4" height="30" /><rect x="178" y="58" width="42" height="5" /><rect x="182" y="68" width="34" height="3" /></g>
      </svg>
      <span aria-hidden="true" className="absolute bottom-4 left-[8%] h-5 w-32 rounded-[50%] bg-[rgb(0_0_0/0.3)]" />
      <span aria-hidden="true" className="absolute bottom-4 right-[8%] h-5 w-32 rounded-[50%] bg-[rgb(0_0_0/0.3)]" />

      {/* Plaques de vie */}
      <div className="absolute inset-x-2 top-2 flex items-start gap-2 sm:inset-x-3 sm:top-3">
        <div className="w-[44%]"><HpPlate name={`${s.me.name} (toi)`} rank={s.me.rank} hp={s.me.hp} max={s.rules.hp} combo={s.me.combo} answered={!!s.mine} /></div>
        <div className="flex flex-1 flex-col items-center gap-1 pt-2">
          <span className="font-display text-xl text-white [text-shadow:0_2px_0_#000]">{T("VS")}</span>
          <span className="rounded-full bg-[rgb(0_0_0/0.35)] px-2 text-[10px] font-bold text-white">{KIND_LABEL[s.kind]}</span>
        </div>
        <div className="w-[44%]"><HpPlate name={s.opponent.name} rank={s.opponent.rank} hp={s.opponent.hp} max={s.rules.hp} combo={s.opponent.combo} align="right" answered={s.opponentAnswered && !!s.question} /></div>
      </div>
      {s.status === 'active' && (
        <button className="absolute bottom-2 left-1/2 -translate-x-1/2 rounded-full bg-[rgb(0_0_0/0.3)] px-3 py-1 text-xs font-bold text-white hover:bg-[rgb(0_0_0/0.5)]" onClick={onQuit}>{T("Abandonner")}</button>
      )}
      {!s.opponent.online && s.status === 'active' && <p className="absolute bottom-10 right-3 rounded-full bg-[rgb(0_0_0/0.45)] px-2 py-0.5 text-xs text-white">{T("connexion de l’adversaire…")}</p>}

      {/* Combattants */}
      <motion.div className="absolute bottom-6 left-[9%]" animate={me}>
        <motion.div animate={koMe ? { rotate: -80, y: 20, opacity: 0.6 } : calm ? undefined : { y: [0, -4, 0] }} transition={koMe ? { duration: 0.6 } : { duration: 1.8, repeat: Infinity }}>
          <div className="overflow-hidden rounded-2xl border-[3px] border-white shadow-lg">
            <Avatar config={myAvatar} size={88} title={T("Toi")} />
          </div>
        </motion.div>
      </motion.div>
      <motion.div className="absolute bottom-6 right-[7%]" animate={opp}>
        <motion.div animate={koOpp ? { rotate: 80, y: 20, opacity: 0.6 } : calm ? undefined : { y: [0, -5, 0] }} transition={koOpp ? { duration: 0.6 } : { duration: 2.1, repeat: Infinity }}>
          {s.opponent.isBot ? (
            <BossCreature glyph="浪" mood={koOpp ? 'ko' : oppMood} size={118} title={s.opponent.name} />
          ) : (
            <div className="overflow-hidden rounded-2xl border-[3px] border-white shadow-lg [transform:scaleX(-1)]">
              <Avatar config={oppAvatar} size={88} title={s.opponent.name} />
            </div>
          )}
        </motion.div>
      </motion.div>

      {/* Dégâts */}
      <AnimatePresence>
        {fx && fx.mine.damage > 0 && (
          <DamagePop key={`m${fx.id}`} side="right" hit={fx.mine} delay={0.25} />
        )}
        {fx && fx.theirs.damage > 0 && (
          <DamagePop key={`t${fx.id}`} side="left" hit={fx.theirs} delay={fx.mine.damage > 0 ? 0.95 : 0.25} />
        )}
      </AnimatePresence>

      {/* Compte à rebours */}
      <AnimatePresence>
        {countdown !== null && (
          <motion.div key={countdown} className="absolute inset-0 flex items-center justify-center bg-[rgb(0_0_0/0.25)]" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
            <motion.span initial={{ scale: 2.2, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={{ type: 'spring', stiffness: 260, damping: 18 }} className="font-display text-8xl text-white [text-shadow:0_4px_0_#8E1B26]" aria-live="assertive">
              {countdown > 0 ? countdown : '始め!'}
            </motion.span>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}

function DamagePop({ side, hit, delay }: { side: 'left' | 'right'; hit: { damage: number; critical: boolean; combo: number }; delay: number }) {
  return (
    <motion.div aria-hidden="true" className={`pointer-events-none absolute bottom-[42%] flex flex-col items-center ${side === 'right' ? 'right-[12%]' : 'left-[12%]'}`} initial={{ opacity: 0, y: 10, scale: 0.6 }} animate={{ opacity: [0, 1, 1, 0], y: [10, -10, -24, -36], scale: [0.6, 1.25, 1, 1] }} transition={{ duration: 1.5, delay, times: [0, 0.2, 0.7, 1] }}>
      {hit.critical && <span className="rounded-md bg-[#C8323F] px-1.5 text-xs font-black tracking-wider text-white">{T("CRITIQUE")}</span>}
      <span className={`font-display font-black text-[#FFE08A] [text-shadow:0_3px_0_#7A2A1F] ${hit.critical ? 'text-5xl' : 'text-4xl'}`}>−{hit.damage}</span>
      {hit.combo >= 2 && <span className="text-sm font-bold text-white [text-shadow:0_1px_0_#000]">{T("combo ×{0}", [ hit.combo])}</span>}
    </motion.div>
  );
}

function RevealView({ s }: { s: DuelStateDto }) {
  const last = s.last!;
  const line = (who: string, r: DuelSideResultDto) => (
    <div className="flex items-center justify-between gap-2 rounded-2xl bg-surface p-3">
      <span className="font-bold">{who}</span>
      <span className={`text-right ${r.correct ? 'text-ok' : 'text-ko'}`}>
        {r.answer === null ? T("pas de réponse") : r.correct ? T("juste en {0} s", [((r.ms ?? 0) / 1000).toFixed(1)]) : 'faux'}
        {r.damage > 0 && <strong>{T("· {0} dégâts{1}", [ r.damage , r.critical ? ' (critique)' : ''])}</strong>}
      </span>
    </div>
  );
  return (
    <motion.section initial={{ opacity: 0, scale: 0.97 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0 }} className="flex flex-col gap-3" aria-live="polite">
      <div className="rounded-3xl bg-surface-2 p-4 text-center">
        <p className="text-sm text-ink-soft">{last.question.prompt} {last.question.display?.jp && <span lang="ja" className="jp font-bold text-ink">{last.question.display.jp}</span>}</p>
        <p className="mt-1 text-lg">{T("Réponse :")}{' '}<strong lang={JP_RE.test(last.answer) ? 'ja' : 'fr'} className={JP_RE.test(last.answer) ? 'jp text-2xl' : ''}>{last.answer}</strong>
        </p>
      </div>
      {line(T("Toi"), last.me)}
      {line(s.opponent.name, last.opponent)}
      {s.status === 'active' && <p className="text-center text-sm text-ink-soft">{T("Question suivante…")}</p>}
    </motion.section>
  );
}

function PendingView({ s, now, onChange }: { s: DuelStateDto; now: number; onChange: () => void }) {
  const nav = useNavigate();
  const [err, setErr] = useState<unknown>(null);
  const left = s.expiresAt ? Math.max(0, Math.ceil((Date.parse(s.expiresAt) - now) / 1000)) : 0;
  const challenger = s.me.side === 1;
  return (
    <div className="flex flex-col items-center gap-5 py-8 text-center">
      <CrossedSwords size={110} spin={challenger} />
      <div className="flex items-center gap-4">
        <RankBadge rank={s.me.rank} size={54} />
        <span className="font-display text-2xl">{T("VS")}</span>
        <RankBadge rank={s.opponent.rank} size={54} />
      </div>
      {challenger ? (
        <>
          <h1 className="text-3xl">{T("Défi envoyé à {0}", [ s.opponent.name])}</h1>
          <p className="text-ink-soft">{T("Le duel commence dès qu’il accepte. Expire dans {0}:{1}.", [ Math.floor(left / 60) , String(left % 60).padStart(2, '0') ])}</p>
          <button className="btn btn-quiet" onClick={async () => { await post(`/duels/${s.id}/decline`).catch(() => undefined); onChange(); }}>{T("Annuler le défi")}</button>
        </>
      ) : (
        <>
          <h1 className="text-3xl">{T("{0} te défie !", [s.opponent.name ])}</h1>
          <p className="text-ink-soft">{T("{0} · {1} points · duel amical", [s.opponent.rank.label , s.opponent.rating ])}</p>
          {err != null && <ErrorBox error={err} />}
          <div className="flex gap-3">
            <button className="btn btn-gold" onClick={async () => { try { await post(`/duels/${s.id}/accept`); onChange(); } catch (e) { setErr(e); } }}>{T("Accepter")}</button>
            <button className="btn btn-quiet" onClick={async () => { await post(`/duels/${s.id}/decline`).catch(() => undefined); nav('/duel'); }}>{T("Refuser")}</button>
          </div>
        </>
      )}
    </div>
  );
}

function ResultView({ s }: { s: DuelStateDto }) {
  const nav = useNavigate();
  const qc = useQueryClient();
  const [err, setErr] = useState<unknown>(null);
  const r = s.result!;
  const win = r.outcome === 'win';
  const promoted = r.delta > 0 && r.rankAfter.label !== r.rankBefore.label;
  const newTier = promoted && r.rankAfter.tierId !== r.rankBefore.tierId;
  const demoted = r.delta < 0 && r.rankAfter.label !== r.rankBefore.label;
  useEffect(() => {
    void qc.invalidateQueries({ queryKey: ['duels'] });
    void qc.invalidateQueries({ queryKey: ['me'] });
  }, [qc]);

  async function again() {
    setErr(null);
    try {
      if (s.kind === 'practice') nav(`/duel/${(await post<{ duelId: string }>('/duels/practice')).duelId}`);
      else if (s.kind === 'friendly' && s.opponent.userId) nav(`/duel/${(await post<{ duelId: string }>('/duels/challenges', { userId: s.opponent.userId })).duelId}`);
      else nav('/duel?search=1');
    } catch (e) {
      setErr(e);
    }
  }

  return (
    <div className="flex flex-col items-center gap-5 py-6 text-center">
      {win && <Confetti />}
      <Stamp className={`jp text-7xl font-black ${win ? 'text-gold' : r.outcome === 'loss' ? 'text-ko' : 'text-ink-soft'}`}>{win ? '勝' : r.outcome === 'loss' ? '負' : '分'}</Stamp>
      <h1 className="text-4xl">{win ? T("Victoire !") : r.outcome === 'loss' ? T("Défaite") : T("Égalité")}</h1>
      <p className="text-lg text-ink-soft">
        {r.endReason === 'ko' ? (win ? `${s.opponent.name} est K.-O.` : T("Tu es K.-O.")) : r.endReason === 'forfeit' ? (win ? T("{0} a abandonné.", [s.opponent.name]) : T("Tu as abandonné.")) : T("Aux points : {0} PV contre {1}.", [s.me.hp, s.opponent.hp])}
      </p>

      {s.kind === 'ranked' ? (
        <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.4 }} className="flex w-full max-w-md flex-col items-center gap-3 rounded-3xl border border-line bg-surface p-5">
          <RankBadge rank={r.rankAfter} size={88} glow={promoted} />
          {promoted && <p className="text-xl font-bold text-gold-ink">{newTier ? T("Promotion ! Te voilà {0}", [r.rankAfter.label]) : T("Nouvelle division : {0}", [r.rankAfter.label])}</p>}
          {demoted && <p className="font-bold text-ko">{T("Retour en {0}", [ r.rankAfter.label])}</p>}
          {!promoted && !demoted && <p className="font-bold">{r.rankAfter.label}</p>}
          <p className="text-lg">
            <span className="font-display text-3xl tabular-nums"><CountUp value={r.ratingAfter} /></span>{' '}{T("points")}{' '}
            <span className={`font-bold ${r.delta >= 0 ? 'text-ok' : 'text-ko'}`}>({r.delta >= 0 ? '+' : ''}{r.delta})</span>
          </p>
        </motion.div>
      ) : (
        <p className="rounded-2xl bg-surface-2 px-4 py-2 text-ink-soft">{T("{0} : sans effet sur le classement.", [s.kind === 'practice' ? T("Entraînement") : T("Duel amical") ])}</p>
      )}

      {(r.xp > 0 || r.coins > 0) && (
        <p className="text-lg font-bold">{T("+{0} XP · +{1} 🪙", [ r.xp , r.coins ])}</p>
      )}
      {err != null && <ErrorBox error={err} />}
      <div className="flex flex-wrap justify-center gap-3">
        <button className="btn btn-gold" onClick={again}>{s.kind === 'ranked' ? T("Nouveau duel classé") : s.kind === 'practice' ? T("Rejouer") : T("Revanche")}</button>
        <Link to="/duel" className="btn btn-quiet">{T("Retour au dojo")}</Link>
      </div>
    </div>
  );
}

// ═══════════════════════════ Alerte de défi (partout dans l'application) ═══════════════════════════

/** Signale un défi reçu, où que l'on soit dans l'application (version en ligne). */
export function DuelInviteWatcher({ path }: { path: string }) {
  const nav = useNavigate();
  const [dismissed, setDismissed] = useState<string[]>([]);
  const { data, refetch } = useQuery({
    queryKey: ['duel-invites'],
    queryFn: () => api<DuelLobbyDto['invites']>('/duels/invites'),
    enabled: !LOCAL,
    refetchInterval: 10_000,
    retry: false,
  });
  const invite = data?.find((i) => !dismissed.includes(i.id));
  if (LOCAL || !invite || path.startsWith('/duel')) return null;
  return (
    <motion.div role="alert" initial={{ y: 40, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="fixed inset-x-3 bottom-20 z-40 mx-auto flex max-w-md items-center gap-3 rounded-3xl border-2 border-gold bg-surface p-3 shadow-xl md:bottom-6">
      <CrossedSwords size={44} />
      <p className="flex-1 text-sm">
        <strong>{invite.player.name}</strong>{' '}{T("te défie en duel !")}</p>
      <button
        className="btn btn-gold min-h-10 px-3"
        onClick={async () => {
          try {
            const r = await post<{ duelId: string }>(`/duels/${invite.id}/accept`);
            nav(`/duel/${r.duelId}`);
          } catch {
            void refetch();
          }
        }}
      >{T("Accepter")}</button>
      <button
        className="rounded-full p-2 text-ink-soft"
        aria-label={T("Refuser le défi")}
        onClick={async () => {
          setDismissed((d) => [...d, invite.id]);
          await post(`/duels/${invite.id}/decline`).catch(() => undefined);
        }}
      >
        ✕
      </button>
    </motion.div>
  );
}
