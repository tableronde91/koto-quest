import { useState } from 'react';
import { Link, useNavigate } from 'react-router';
import { AnimatePresence, motion } from 'motion/react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { normalizeAvatar } from '@koto/learning-engine';
import type { DuelLobbyDto, DuelPlayerSearchDto, FriendActionDto, FriendDto, FriendPlayerDto, FriendsDto } from '@koto/shared';
import { LOCAL, api, del, post } from '../api/client';
import { Avatar } from './Avatar';
import { RankBadge } from './DuelBits';
import { ErrorBox } from './ui';
import { T, locale } from '../i18n';

export const useFriends = (enabled = true) =>
  useQuery({ queryKey: ['friends'], queryFn: () => api<FriendsDto>('/friends'), enabled: enabled && !LOCAL, refetchInterval: 15_000 });

const CODE_RE = /^(KQ-?)?[A-Z0-9]{6}$/i;

/** « en ligne », « vu il y a 5 min »… */
function seen(f: FriendDto): string {
  if (f.online) return T('En ligne');
  if (!f.lastSeenAt) return T('Hors ligne');
  const min = Math.max(1, Math.round((Date.now() - Date.parse(f.lastSeenAt)) / 60_000));
  const rtf = new Intl.RelativeTimeFormat(locale === 'en' ? 'en' : 'fr', { numeric: 'auto' });
  const rel = min < 60 ? rtf.format(-min, 'minute') : min < 60 * 24 ? rtf.format(-Math.round(min / 60), 'hour') : rtf.format(-Math.round(min / 1440), 'day');
  return T('Vu {0}', [rel]);
}

function PlayerFace({ p, online }: { p: FriendPlayerDto; online?: boolean }) {
  return (
    <span className="relative shrink-0">
      <span className="block overflow-hidden rounded-2xl border border-line bg-surface-2">
        <Avatar config={normalizeAvatar(p.avatar)} size={48} />
      </span>
      {online !== undefined && (
        <span aria-hidden="true" className={`absolute -bottom-0.5 -right-0.5 h-4 w-4 rounded-full border-2 border-surface ${online ? 'bg-[#2EAD5B]' : 'bg-line'}`} />
      )}
    </span>
  );
}

/** Amis : code à partager, demandes, liste avec présence et défi en un clic. */
export function FriendsPanel({ lobby, onChange }: { lobby: DuelLobbyDto; onChange: () => void }) {
  const nav = useNavigate();
  const qc = useQueryClient();
  const { data } = useFriends(lobby.online);
  const [q, setQ] = useState('');
  const [copied, setCopied] = useState(false);
  const [err, setErr] = useState<unknown>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [confirmRemove, setConfirmRemove] = useState<string | null>(null);
  const term = q.trim();
  const search = useQuery({
    queryKey: ['duel-players', term],
    queryFn: () => api<DuelPlayerSearchDto>(`/duels/players?q=${encodeURIComponent(term)}`),
    enabled: lobby.online && term.length >= 2,
  });
  const refresh = () => {
    void qc.invalidateQueries({ queryKey: ['friends'] });
    void qc.invalidateQueries({ queryKey: ['duel-players'] });
    void qc.invalidateQueries({ queryKey: ['friend-requests'] });
  };

  async function act<R>(fn: () => Promise<R>, after?: (r: R) => void) {
    setErr(null);
    setNotice(null);
    try {
      const r = await fn();
      refresh();
      after?.(r);
    } catch (e) {
      setErr(e);
    }
  }
  const addFriend = (target: { code?: string; userId?: string }) =>
    act(
      () => post<FriendActionDto>('/friends', target),
      (r) => {
        setNotice(r.status === 'accepted' ? T('{0} et toi êtes maintenant amis !', [r.player.name]) : T('Demande envoyée à {0}.', [r.player.name]));
        setQ('');
      },
    );
  const challenge = (userId: string) =>
    act(
      () => post<{ duelId: string }>('/duels/challenges', { userId }),
      (r) => {
        onChange();
        nav(`/duel/${r.duelId}`);
      },
    );
  const accept = (id: string) => act(() => post<FriendActionDto>(`/friends/${id}/accept`), (r) => setNotice(T('{0} et toi êtes maintenant amis !', [r.player.name])));
  const remove = (id: string) => act(() => del(`/friends/${id}`), () => setConfirmRemove(null));

  async function share() {
    const text = T('Ajoute-moi sur Koto Quest pour qu’on s’affronte en duel ! Mon code : {0}', [lobby.profile.code]);
    try {
      if (navigator.share) await navigator.share({ text, url: location.origin });
      else {
        await navigator.clipboard.writeText(lobby.profile.code);
        setCopied(true);
        window.setTimeout(() => setCopied(false), 1500);
      }
    } catch {
      /* partage annulé ou presse-papiers indisponible */
    }
  }

  const friends = data?.friends ?? [];
  const onlineCount = friends.filter((f) => f.online).length;

  return (
    <section id="amis" aria-labelledby="friends-title" className="flex flex-col gap-4 rounded-3xl border border-line bg-surface p-5">
      <div className="flex flex-wrap items-center gap-2">
        <h2 id="friends-title" className="flex-1 text-xl">
          {T('Mes amis')} {friends.length > 0 && <span className="text-base font-normal text-ink-soft">· {T('{0} en ligne sur {1}', [onlineCount, friends.length])}</span>}
        </h2>
      </div>

      <div className="flex flex-wrap items-center gap-3 rounded-2xl bg-surface-2 p-3">
        <span className="text-ink-soft">{T('Ton code de duelliste :')}</span>
        <code className="font-display text-xl tracking-wider" data-testid="my-code">{lobby.profile.code}</code>
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
          {copied ? T('Copié ✓') : T('Copier')}
        </button>
        {lobby.online && typeof navigator !== 'undefined' && 'share' in navigator && (
          <button className="btn btn-quiet min-h-10 px-3 text-sm" onClick={share}>{T('Partager')}</button>
        )}
      </div>

      {!lobby.online ? (
        <p className="text-ink-soft">{T('Disponible dans la version en ligne : ajoute tes amis avec leur code, vois qui est en ligne et défie-les en un clic.')}</p>
      ) : (
        <>
          {/* Demandes reçues */}
          <AnimatePresence initial={false}>
            {data?.incoming.map((r) => (
              <motion.div key={r.id} layout initial={{ opacity: 0, y: -6 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }} className="flex flex-wrap items-center gap-3 rounded-2xl border-2 border-gold p-3" data-testid="friend-request">
                <PlayerFace p={r.player} />
                <p className="min-w-0 flex-1">
                  <strong>{r.player.name}</strong> <span className="text-ink-soft">({r.player.rank.label})</span> {T('veut devenir ton ami.')}
                </p>
                <button className="btn btn-gold min-h-10 px-4" onClick={() => accept(r.id)}>{T('Accepter')}</button>
                <button className="btn btn-quiet min-h-10 px-3" onClick={() => remove(r.id)}>{T('Refuser')}</button>
              </motion.div>
            ))}
          </AnimatePresence>

          {/* Liste d'amis */}
          {friends.length > 0 ? (
            <ul className="flex flex-col gap-2" aria-label={T('Liste d’amis')}>
              {friends.map((f) => (
                <li key={f.id} className="flex flex-wrap items-center gap-3 rounded-2xl border border-line p-2.5 sm:flex-nowrap" data-testid="friend">
                  <PlayerFace p={f.player} online={f.online} />
                  <div className="min-w-0 flex-1">
                    <p className="truncate font-bold">{f.player.name}</p>
                    <p className="flex flex-wrap items-center gap-x-2 text-sm text-ink-soft">
                      <span className={f.online ? 'font-bold text-[#1F7A40]' : ''}>{seen(f)}</span>
                      <span>· {f.player.rank.label}</span>
                      {f.record.wins + f.record.losses + f.record.draws > 0 && (
                        <span title={T('Vos duels terminés')}>· {T('{0} V – {1} D', [f.record.wins, f.record.losses])}{f.record.draws ? ` – ${T('{0} N', [f.record.draws])}` : ''}</span>
                      )}
                    </p>
                  </div>
                  <div className="flex items-center gap-2">
                    {f.pendingDuelId ? (
                      <Link to={`/duel/${f.pendingDuelId}`} className="btn btn-quiet min-h-10 px-3">{T('Défi en attente')}</Link>
                    ) : (
                      <button className={`btn min-h-10 px-4 ${f.online ? 'btn-gold' : 'btn-quiet'}`} onClick={() => challenge(f.player.userId)} aria-label={T('Défier {0}', [f.player.name])}>
                        {T('Défier')}
                      </button>
                    )}
                    {confirmRemove === f.id ? (
                      <>
                        <button className="btn btn-quiet min-h-10 px-3 text-ko" onClick={() => remove(f.id)}>{T('Retirer ?')}</button>
                        <button className="rounded-full p-2 text-ink-soft" onClick={() => setConfirmRemove(null)} aria-label={T('Annuler')}>✕</button>
                      </>
                    ) : (
                      <button className="rounded-full p-2 text-ink-soft hover:bg-surface-2" onClick={() => setConfirmRemove(f.id)} aria-label={T('Retirer {0} de mes amis', [f.player.name])} title={T('Retirer de mes amis')}>
                        ⋯
                      </button>
                    )}
                  </div>
                </li>
              ))}
            </ul>
          ) : (
            data && <p className="rounded-2xl bg-surface-2 p-4 text-ink-soft">{T('Ajoute tes amis avec leur code de duelliste (ou leur nom) : tu verras quand ils sont en ligne et tu pourras les défier en un clic.')}</p>
          )}

          {/* Ajouter un ami */}
          <form
            className="flex flex-col gap-2 sm:flex-row"
            onSubmit={(e) => {
              e.preventDefault();
              if (CODE_RE.test(term)) void addFriend({ code: term });
            }}
          >
            <label className="sr-only" htmlFor="friend-search">{T('Code ou nom du joueur')}</label>
            <input id="friend-search" value={q} onChange={(e) => setQ(e.target.value)} placeholder={T('Code (KQ-…) ou nom du joueur')} className="min-h-12 flex-1 rounded-xl border-2 border-line bg-surface px-3" autoComplete="off" />
            <button type="submit" className="btn btn-primary" disabled={!CODE_RE.test(term)}>{T('Ajouter en ami')}</button>
          </form>
          {notice && <p role="status" className="rounded-2xl bg-ok-bg p-3 font-bold">{notice}</p>}
          {err != null && <ErrorBox error={err} />}
          {search.data && term.length >= 2 && (
            search.data.players.length > 0 ? (
              <ul className="flex flex-col gap-2" aria-label={T('Résultats de recherche')}>
                {search.data.players.map((pl) => (
                  <li key={pl.userId} className="flex flex-wrap items-center gap-3 rounded-2xl border border-line p-2">
                    <RankBadge rank={pl.rank} size={32} />
                    <span className="min-w-0 flex-1"><strong>{pl.name}</strong> <span className="text-sm text-ink-soft">· {pl.rank.label} · {pl.code}</span></span>
                    {pl.relation === 'friend' ? (
                      <span className="text-sm font-bold text-ink-soft">{T('Ami ✓')}</span>
                    ) : pl.relation === 'outgoing' ? (
                      <span className="text-sm text-ink-soft">{T('Demande envoyée')}</span>
                    ) : pl.relation === 'incoming' ? (
                      <button className="btn btn-gold min-h-10 px-3" onClick={() => accept(pl.friendshipId!)}>{T('Accepter')}</button>
                    ) : (
                      <button className="btn btn-gold min-h-10 px-3" onClick={() => addFriend({ userId: pl.userId! })}>{T('Ajouter')}</button>
                    )}
                    <button className="btn btn-quiet min-h-10 px-3" onClick={() => challenge(pl.userId!)}>{T('Défier')}</button>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-ink-soft">{T('Aucun duelliste trouvé.')}</p>
            )
          )}

          {/* Demandes envoyées et défis en attente */}
          {(data?.outgoing.length ?? 0) > 0 && (
            <div className="flex flex-col gap-2">
              <h3 className="font-bold">{T('Demandes d’ami envoyées')}</h3>
              {data!.outgoing.map((r) => (
                <div key={r.id} className="flex items-center gap-3 rounded-2xl bg-surface-2 p-2">
                  <span className="flex-1">{T('En attente de')} <strong>{r.player.name}</strong>…</span>
                  <button className="btn btn-quiet min-h-10 px-3" onClick={() => remove(r.id)}>{T('Annuler')}</button>
                </div>
              ))}
            </div>
          )}
          {lobby.sent.length > 0 && (
            <div className="flex flex-col gap-2">
              <h3 className="font-bold">{T('Défis envoyés')}</h3>
              {lobby.sent.map((s) => (
                <div key={s.id} className="flex items-center gap-3 rounded-2xl bg-surface-2 p-2">
                  <span className="flex-1">{T('En attente de')} <strong>{s.player.name}</strong>…</span>
                  <Link className="btn btn-quiet min-h-10 px-3" to={`/duel/${s.id}`}>{T('Voir')}</Link>
                  <button className="btn btn-quiet min-h-10 px-3" onClick={async () => { await post(`/duels/${s.id}/decline`).catch(() => undefined); onChange(); }}>{T('Annuler')}</button>
                </div>
              ))}
            </div>
          )}
        </>
      )}
    </section>
  );
}

/** Après un duel contre un vrai joueur : l'ajouter en ami. */
export function AddFriendButton({ userId, name }: { userId: string; name: string }) {
  const { data } = useFriends();
  const qc = useQueryClient();
  const [state, setState] = useState<'idle' | 'sent' | 'friends' | 'error'>('idle');
  if (LOCAL || !data) return null;
  const isFriend = data.friends.some((f) => f.player.userId === userId);
  const outgoing = data.outgoing.some((r) => r.player.userId === userId);
  if (isFriend || state === 'friends') return <p className="text-sm text-ink-soft">{T('{0} fait partie de tes amis.', [name])}</p>;
  if (outgoing || state === 'sent') return <p className="text-sm text-ink-soft">{T('Demande d’ami envoyée à {0}.', [name])}</p>;
  return (
    <button
      className="btn btn-quiet"
      onClick={async () => {
        try {
          const r = await post<FriendActionDto>('/friends', { userId });
          setState(r.status === 'accepted' ? 'friends' : 'sent');
          void qc.invalidateQueries({ queryKey: ['friends'] });
        } catch {
          setState('error');
        }
      }}
    >
      {T('Ajouter {0} en ami', [name])}
    </button>
  );
}

/** Alerte de demande d'ami, partout dans l'application. */
export function FriendRequestWatcher({ path }: { path: string }) {
  const qc = useQueryClient();
  const [dismissed, setDismissed] = useState<string[]>([]);
  const { data } = useQuery({
    queryKey: ['friend-requests'],
    queryFn: () => api<FriendsDto['incoming']>('/friends/requests'),
    enabled: !LOCAL,
    refetchInterval: 30_000,
    retry: false,
  });
  const req = data?.find((r) => !dismissed.includes(r.id));
  if (LOCAL || !req || path.startsWith('/duel')) return null;
  return (
    <motion.div role="status" initial={{ y: 40, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="fixed inset-x-3 bottom-20 z-30 mx-auto flex max-w-md items-center gap-3 rounded-3xl border-2 border-[#3FA7A0] bg-surface p-3 shadow-xl md:bottom-6" data-testid="friend-toast">
      <span aria-hidden="true" className="jp flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-[#3FA7A0] text-2xl font-black text-white">友</span>
      <p className="flex-1 text-sm">
        <strong>{req.player.name}</strong> {T('veut devenir ton ami.')}
      </p>
      <button
        className="btn btn-gold min-h-10 px-3"
        onClick={async () => {
          setDismissed((d) => [...d, req.id]);
          await post(`/friends/${req.id}/accept`).catch(() => undefined);
          void qc.invalidateQueries({ queryKey: ['friends'] });
          void qc.invalidateQueries({ queryKey: ['friend-requests'] });
        }}
      >
        {T('Accepter')}
      </button>
      <button className="rounded-full p-2 text-ink-soft" aria-label={T('Plus tard')} onClick={() => setDismissed((d) => [...d, req.id])}>
        ✕
      </button>
    </motion.div>
  );
}
