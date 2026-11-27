import { studyWords, useDecor, useRankLabel } from '../components/StudyLanguage';
import { useEffect } from 'react';
import { Link, useLocation } from 'react-router';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { levelFromXp } from '@koto/learning-engine';
import { examLevelLabel, levelsOfLanguage, type DuelLobbyDto, type MeDto } from '@koto/shared';

/** Niveaux dont le parcours est publié (les autres sont affichés « bientôt »). */
const READY_LEVELS = new Set(['N5', 'N4', 'N3', 'N2', 'N1', 'TOPIK1', 'TOPIK2', 'TOPIK3', 'TOPIK4', 'TOPIK5', 'TOPIK6', 'A1', 'A2', 'B1', 'B2', 'C1', 'HSK1', 'HSK2', 'HSK3', 'HSK4', 'HSK5', 'HSK6', 'DELEA1', 'DELEA2', 'DELEB1', 'DELEB2', 'DELEC1', 'DELEC2', 'GOETHEA1', 'GOETHEA2', 'GOETHEB1', 'GOETHEB2']);
import { api } from '../api/client';
import { useUpdatePrefs } from '../api/hooks';
import { Avatar } from '../components/Avatar';
import { RankBadge } from '../components/DuelBits';
import { FriendsPanel } from '../components/Friends';
import { ErrorBox, PageTitle, Spinner } from '../components/ui';
import { Coins } from './Character';
import { T } from '../i18n';

/** Profil : qui je suis (personnage, pseudo, objectifs) et mes amis. Les Réglages gardent l'application. */
export function ProfilePage({ me }: { me: MeDto }) {
  const { hash } = useLocation();
  const qc = useQueryClient();
  const lobby = useQuery({ queryKey: ['duels'], queryFn: () => api<DuelLobbyDto>('/duels'), refetchInterval: 15_000 });
  useEffect(() => {
    if (lobby.data && /^#[\w-]+$/.test(hash)) document.querySelector(hash)?.scrollIntoView();
  }, [hash, lobby.data]);

  return (
    <div className="flex flex-col gap-10">
      <div className="flex flex-wrap items-center gap-3">
        <div className="flex-1"><PageTitle>{T("Profil")}</PageTitle></div>
        <Link to="/settings" className="btn btn-quiet">{T("Réglages")}</Link>
      </div>
      <IdentityCard me={me} lobby={lobby.data} />
      <GoalsSection me={me} />
      {lobby.isLoading ? <Spinner /> : lobby.error || !lobby.data ? <ErrorBox error={lobby.error} /> : (
        <FriendsPanel lobby={lobby.data} onChange={() => qc.invalidateQueries({ queryKey: ['duels'] })} />
      )}
    </div>
  );
}

function IdentityCard({ me, lobby }: { me: MeDto; lobby?: DuelLobbyDto }) {
  const RL = useRankLabel();
  const D = useDecor();
  const lv = levelFromXp(me.xp);
  const pct = Math.round((lv.intoLevel / Math.max(1, lv.forNext)) * 100);
  return (
    <section aria-label={T("Carte d’identité")} className="relative overflow-hidden rounded-3xl bg-ink p-6 text-paper">
      <span aria-hidden="true" className="jp pointer-events-none absolute -right-2 -top-8 select-none text-[9rem] font-black leading-none opacity-10">{D('me')}</span>
      <div className="flex flex-wrap items-center gap-5">
        <span className="overflow-hidden rounded-3xl border-2 border-[rgb(255_255_255/0.3)] bg-surface"><Avatar config={me.avatar} size={96} /></span>
        <div className="min-w-[11rem] flex-1">
          <p className="break-words font-display text-3xl leading-tight">{me.displayName}</p>
          <p className="mt-1 opacity-85">{T("Niveau {0} · objectif {1}", [lv.level, examLevelLabel(me.preferences.targetLevel)])}</p>
          <div className="mt-3 h-2.5 max-w-xs overflow-hidden rounded-full bg-[rgb(255_255_255/0.2)]" role="progressbar" aria-label={T("XP du niveau")} aria-valuenow={pct} aria-valuemin={0} aria-valuemax={100}>
            <div className="h-full rounded-full bg-gold" style={{ width: `${pct}%` }} />
          </div>
          <p className="mt-1 text-sm opacity-75">{T("{0} / {1} XP", [lv.intoLevel, lv.forNext])} · <Coins value={me.coins} /></p>
        </div>
        {lobby && (
          <div className="flex items-center gap-3 text-left sm:flex-col sm:gap-1 sm:text-center">
            <RankBadge rank={lobby.profile.rank} size={56} />
            <span className="text-sm font-bold">{RL(lobby.profile.rank)}</span>
            <span className="text-xs opacity-75">{T("{0} pts", [lobby.profile.rating])}</span>
          </div>
        )}
      </div>
      <div className="mt-5 flex flex-wrap gap-3">
        <Link to="/avatar" className="btn btn-gold">{T("Personnaliser")}</Link>
        {/* Fond clair explicite : .btn-quiet est transparent, et le texte foncé disparaissait sur la carte sombre. */}
        <Link to="/achievements" className="btn btn-quiet" style={{ background: 'var(--surface)' }}>{T("Mes succès")}</Link>
      </div>
    </section>
  );
}

function GoalsSection({ me }: { me: MeDto }) {
  const update = useUpdatePrefs();
  const p = me.preferences;
  return (
    <section aria-labelledby="goals-title" className="flex flex-col gap-5">
      <h2 id="goals-title" className="text-2xl">{T("Identité et objectifs")}</h2>
      <p className="-mt-3 text-sm text-ink-soft">{T("Tu étudies {0}. Pour changer de langue, va dans les ", [studyWords(me.preferences.studyLanguage ?? 'ja').theLanguage])}<Link to="/settings" className="font-bold underline">{T("Réglages")}</Link>.</p>
      <div className="flex flex-wrap gap-6">
        <label className="flex flex-col gap-1 font-bold">{T("Pseudo")}<input className="field w-60 font-normal" defaultValue={me.displayName} maxLength={40} onBlur={(e) => e.target.value.trim() && e.target.value !== me.displayName && update.mutate({ displayName: e.target.value })} />
        </label>
        <label className="flex flex-col gap-1 font-bold">{T("Niveau visé")}<select className="field w-44 font-normal" value={p.targetLevel} onChange={(e) => update.mutate({ targetLevel: e.target.value })}>
            {levelsOfLanguage(p.studyLanguage ?? 'ja').map((l) => <option key={l} value={l} disabled={!READY_LEVELS.has(l)}>{READY_LEVELS.has(l) ? examLevelLabel(l) : T("{0} (bientôt)", [examLevelLabel(l)])}</option>)}
          </select>
        </label>
        <label className="flex flex-col gap-1 font-bold">{T("Temps d’étude par jour")}<select className="field w-44 font-normal" value={p.minutesPerDay} onChange={(e) => update.mutate({ minutesPerDay: Number(e.target.value) })}>
            {[10, 15, 20, 30, 45, 60, 90].map((m) => <option key={m} value={m}>{T("{0} min", [m])}</option>)}
          </select>
        </label>
        <label className="flex flex-col gap-1 font-bold">{T("Date d’examen")}<input type="date" className="field w-48 font-normal" defaultValue={p.examDate ?? ''} onBlur={(e) => update.mutate({ examDate: e.target.value || null })} />
        </label>
      </div>
      {update.error && <ErrorBox error={update.error} />}
    </section>
  );
}
