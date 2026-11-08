import { FormEvent, useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import type { MeDto, ReminderMode } from '@koto/shared';
import { ApiError, LOCAL, del, post } from '../api/client';
import { qk, useNotifPrefs, useUpdateNotifPrefs, useUpdatePrefs } from '../api/hooks';
import { ErrorBox, PageTitle, Spinner } from '../components/ui';
import { hhmmToMinutes, minutesToHHMM } from '../lib/format';
import { permission, pushSupported, subscribePush, unsubscribePush } from '../lib/push';
import { LanguageSwitch } from '../components/LanguageSwitch';
import { T, DATE_LOCALE } from '../i18n';

export function SettingsPage({ me }: { me: MeDto }) {
  const { hash } = useLocation();
  useEffect(() => {
    if (/^#[\w-]+$/.test(hash)) document.querySelector(hash)?.scrollIntoView();
  }, [hash]);
  return (
    <div className="flex flex-col gap-12">
      <PageTitle>{T("Réglages")}</PageTitle>
      <RemindersSection />
      <StudySection me={me} />
      {LOCAL ? <LocalDataSection /> : <DataSection />}
    </div>
  );
}

const MODES: { value: ReminderMode; label: string; hint: string }[] = [
  { value: 'calm', label: T("Tranquille"), hint: T("2 défis par jour") },
  { value: 'normal', label: T("Normal"), hint: T("4 défis par jour") },
  { value: 'intense', label: T("Intensif"), hint: T("8 défis par jour") },
  { value: 'custom', label: T("Personnalisé"), hint: T("Tes propres horaires") },
];

function RemindersSection() {
  const { data: p, isLoading, error } = useNotifPrefs();
  const update = useUpdateNotifPrefs();
  const [pushState, setPushState] = useState<string | null>(null);
  const [testMsg, setTestMsg] = useState<string | null>(null);
  const [customDraft, setCustomDraft] = useState('');
  const qc = useQueryClient();

  if (isLoading) return <Spinner />;
  if (error || !p) return <ErrorBox error={error} />;
  const paused = p.pausedUntil && new Date(p.pausedUntil) > new Date();
  const perm = permission();

  async function enablePush() {
    if (!p!.vapidPublicKey) return setPushState(T("Le serveur n’a pas de clé Web Push configurée : les défis s’afficheront dans l’application uniquement."));
    const r = await subscribePush(p!.vapidPublicKey);
    setPushState(
      r === 'subscribed' ? T("Notifications activées sur cet appareil.")
        : r === 'denied' ? T("Ton navigateur bloque les notifications. Les défis s’afficheront quand l’application est ouverte ; tu peux autoriser les notifications dans les paramètres du site.")
        : r === 'unsupported' ? T("Ce navigateur ne gère pas les notifications push. Sur iPhone, installe d’abord Koto Quest sur l’écran d’accueil.")
        : T("L’activation a échoué. Réessaie dans un instant."),
    );
    update.reset();
    await update.mutateAsync({});
  }

  async function test() {
    setTestMsg(null);
    try {
      const r = await post<{ pushed: boolean }>('/notifications/test');
      setTestMsg(r.pushed ? T("Défi envoyé : regarde tes notifications.") : T("Défi créé : il s’affiche ici."));
      qc.invalidateQueries({ queryKey: qk.inbox });
    } catch (e) {
      setTestMsg(e instanceof ApiError ? e.message : T("Erreur"));
    }
  }

  return (
    <section id="rappels" aria-labelledby="rappels-title" className="flex flex-col gap-5 scroll-mt-6">
      <div>
        <h2 id="rappels-title" className="text-2xl">{T("Défis dans la journée")}</h2>
        <p className="mt-1 max-w-[62ch] text-ink-soft">{T("Quelques heures après une leçon, Koto Quest te pose une question courte sur une notion que tu es en train d’apprendre. Aucun défi n’est envoyé s’il n’y a rien d’utile à réviser.")}</p>
      </div>

      <label className="flex items-start gap-3 rounded-2xl border-2 border-line bg-surface p-4">
        <input type="checkbox" className="mt-1 h-5 w-5 accent-[var(--ink)]" checked={p.consent} onChange={(e) => update.mutate({ consent: e.target.checked, enabled: e.target.checked })} />
        <span>
          <span className="font-bold">{T("J’accepte de recevoir des défis de révision")}</span>
          <span className="block text-sm text-ink-soft">{T("Tu peux retirer ton accord à tout moment : tous les envois s’arrêtent et les abonnements de cet appareil sont supprimés.")}</span>
        </span>
      </label>

      {p.consent && (
        <>
          <label className="flex items-center gap-3">
            <input type="checkbox" className="h-5 w-5 accent-[var(--ink)]" checked={p.enabled} onChange={(e) => update.mutate({ enabled: e.target.checked })} />
            <span className="font-bold">{T("Défis activés")}</span>
          </label>

          <fieldset>
            <legend className="font-bold">{T("Fréquence")}</legend>
            <div className="mt-2 grid gap-2 sm:grid-cols-4">
              {MODES.map((m) => (
                <button key={m.value} type="button" aria-pressed={p.mode === m.value} onClick={() => update.mutate({ mode: m.value })} className="rounded-2xl border-2 bg-surface px-4 py-3 text-left" style={{ borderColor: p.mode === m.value ? 'var(--ink)' : 'var(--line)' }}>
                  <span className="block font-bold">{m.label}</span>
                  <span className="text-sm text-ink-soft">{m.hint}</span>
                </button>
              ))}
            </div>
          </fieldset>

          {p.mode === 'custom' ? (
            <div>
              <p className="font-bold">{T("Mes horaires")}</p>
              <div className="mt-2 flex flex-wrap items-center gap-2">
                {p.customTimes.map((t) => (
                  <button key={t} className="rounded-full bg-surface-2 px-3 py-1" onClick={() => update.mutate({ customTimes: p.customTimes.filter((x) => x !== t) })} aria-label={T("Retirer {0}", [minutesToHHMM(t)])}>
                    {minutesToHHMM(t)} ✕
                  </button>
                ))}
                <input type="time" className="field w-36" value={customDraft} onChange={(e) => setCustomDraft(e.target.value)} aria-label={T("Nouvel horaire")} />
                <button className="btn btn-quiet" disabled={!customDraft || p.customTimes.length >= 10} onClick={() => { update.mutate({ customTimes: [...p.customTimes, hhmmToMinutes(customDraft)] }); setCustomDraft(''); }}>{T("Ajouter")}</button>
              </div>
            </div>
          ) : (
            <div className="flex flex-wrap gap-4">
              <TimeField label={T("Pas avant")} value={p.windowStart} onChange={(v) => update.mutate({ windowStart: v })} />
              <TimeField label={T("Pas après")} value={p.windowEnd} onChange={(v) => update.mutate({ windowEnd: v })} />
            </div>
          )}
          <div className="flex flex-wrap gap-4">
            <TimeField label={T("Heures silencieuses de")} value={p.quietStart ?? 1320} onChange={(v) => update.mutate({ quietStart: v })} />
            <TimeField label="à" value={p.quietEnd ?? 480} onChange={(v) => update.mutate({ quietEnd: v })} />
          </div>
          <p className="text-sm text-ink-soft">{T("Créneaux prévus : {0}.", [ p.slots.length ? p.slots.map(minutesToHHMM).join(', ') : T("aucun (vérifie tes horaires)") ])}</p>

          <div className="flex flex-wrap gap-3">
            {paused ? (
              <button className="btn btn-quiet" onClick={() => update.mutate({ pausedUntil: null })}>{T("Reprendre (en pause jusqu’au {0})", [ new Date(p.pausedUntil!).toLocaleString(DATE_LOCALE, { weekday: 'long', hour: '2-digit', minute: '2-digit' }) ])}</button>
            ) : (
              <>
                <button className="btn btn-quiet" onClick={() => update.mutate({ pausedUntil: new Date(Date.now() + 86_400_000).toISOString() })}>{T("Pause 24 h")}</button>
                <button className="btn btn-quiet" onClick={() => update.mutate({ pausedUntil: new Date(Date.now() + 7 * 86_400_000).toISOString() })}>{T("Pause 1 semaine")}</button>
              </>
            )}
          </div>

          <div className="rounded-2xl bg-surface-2 p-4">
            {LOCAL ? (
              <LocalNotifications />
            ) : (
              <>
            <p className="font-bold">{T("Notifications sur cet appareil")}</p>
            <p className="text-sm text-ink-soft">
              {p.pushSubscribed && perm === 'granted'
                ? T("Activées : tu recevras les défis même quand Koto Quest est fermé.")
                : T("Sans notifications, les défis apparaissent en fenêtre quand l’application est ouverte.")}
            </p>
            <div className="mt-3 flex flex-wrap gap-3">
              {pushSupported() && !(p.pushSubscribed && perm === 'granted') && <button className="btn btn-primary" onClick={enablePush}>{T("Autoriser les notifications")}</button>}
              {p.pushSubscribed && <button className="btn btn-quiet" onClick={async () => { await unsubscribePush(); update.mutate({}); }}>{T("Désactiver sur cet appareil")}</button>}
            </div>
            {pushState && <p role="status" className="mt-3">{pushState}</p>}
              </>
            )}
            <button className="btn btn-quiet mt-3 mr-3" onClick={test}>{T("Recevoir un défi maintenant")}</button>
            {testMsg && <p role="status" className="mt-3">{testMsg}</p>}
          </div>
        </>
      )}
      {update.error && <ErrorBox error={update.error} />}
    </section>
  );
}

function TimeField({ label, value, onChange }: { label: string; value: number; onChange: (v: number) => void }) {
  return (
    <label className="flex flex-col gap-1 font-bold">
      {label}
      <input type="time" className="field w-36 font-normal" defaultValue={minutesToHHMM(value)} onBlur={(e) => e.target.value && hhmmToMinutes(e.target.value) !== value && onChange(hhmmToMinutes(e.target.value))} />
    </label>
  );
}

function StudySection({ me }: { me: MeDto }) {
  const update = useUpdatePrefs();
  const p = me.preferences;
  return (
    <section aria-labelledby="study-title" className="flex flex-col gap-5">
      <h2 id="study-title" className="text-2xl">{T("Apprentissage et affichage")}</h2>
      <div className="flex flex-wrap gap-6">
        <label className="flex flex-col gap-1 font-bold">{T("Pseudo")}<input className="field w-60 font-normal" defaultValue={me.displayName} maxLength={40} onBlur={(e) => e.target.value.trim() && e.target.value !== me.displayName && update.mutate({ displayName: e.target.value })} />
        </label>
        <label className="flex flex-col gap-1 font-bold">{T("Temps d’étude par jour")}<select className="field w-44 font-normal" value={p.minutesPerDay} onChange={(e) => update.mutate({ minutesPerDay: Number(e.target.value) })}>
            {[10, 15, 20, 30, 45, 60, 90].map((m) => <option key={m} value={m}>{T("{0} min", [m ])}</option>)}
          </select>
        </label>
        <label className="flex flex-col gap-1 font-bold">{T("Date d’examen")}<input type="date" className="field w-48 font-normal" defaultValue={p.examDate ?? ''} onBlur={(e) => update.mutate({ examDate: e.target.value || null })} />
        </label>
        <div className="flex flex-col gap-1 font-bold">
          <span id="lang-label">{T("Langue de l’application")}</span>
          <LanguageSwitch saveToAccount />
          <span className="text-sm font-normal text-ink-soft">{T("Les cours, exercices et messages s’affichent dans cette langue. Le japonais reste en japonais !")}</span>
        </div>
        <label className="flex flex-col gap-1 font-bold">{T("Thème")}<select className="field w-44 font-normal" value={p.theme} onChange={(e) => update.mutate({ theme: e.target.value })}>
            <option value="system">{T("Comme l’appareil")}</option>
            <option value="light">{T("Clair")}</option>
            <option value="dark">{T("Sombre")}</option>
          </select>
        </label>
      </div>
      <label className="flex items-center gap-3">
        <input type="checkbox" className="h-5 w-5 accent-[var(--ink)]" checked={p.showFurigana} onChange={(e) => update.mutate({ showFurigana: e.target.checked })} />{T("Afficher les furigana (lecture au-dessus des kanji)")}</label>
      <label className="flex items-center gap-3">
        <input type="checkbox" className="h-5 w-5 accent-[var(--ink)]" checked={p.reducedMotion} onChange={(e) => update.mutate({ reducedMotion: e.target.checked })} />{T("Réduire les animations")}</label>
      <p className="text-sm text-ink-soft">{T("Fuseau horaire : {0}. Objectif : JLPT {1}.", [ p.timezone , p.targetLevel ])}</p>
    </section>
  );
}

function DataSection() {
  const [confirming, setConfirming] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const qc = useQueryClient();
  const navigate = useNavigate();

  async function logout() {
    await post('/auth/logout').catch(() => undefined);
    qc.clear();
    navigate('/welcome');
  }

  async function remove(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    try {
      await del('/me', { password: new FormData(e.currentTarget).get('password') });
      await unsubscribePush().catch(() => undefined);
      qc.clear();
      navigate('/welcome');
    } catch (err) {
      setError(err instanceof Error ? err.message : T("Erreur"));
    }
  }

  return (
    <section aria-labelledby="data-title" className="flex flex-col gap-4">
      <h2 id="data-title" className="text-2xl">{T("Compte et données")}</h2>
      <div className="flex flex-wrap gap-3">
        <a className="btn btn-quiet" href="/api/me/export" download>{T("Télécharger mes données")}</a>
        <button className="btn btn-quiet" onClick={logout}>{T("Se déconnecter")}</button>
        <button className="btn btn-quiet text-ko" onClick={() => setConfirming(true)}>{T("Supprimer mon compte")}</button>
      </div>
      {confirming && (
        <form onSubmit={remove} className="flex flex-col gap-3 rounded-2xl border-2 border-ko p-4">
          <p className="font-bold">{T("La suppression est définitive : progression, révisions et statistiques seront effacées.")}</p>
          <label className="flex flex-col gap-1">{T("Confirme avec ton mot de passe")}<input name="password" type="password" required className="field max-w-xs" autoComplete="current-password" />
          </label>
          {error && <p role="alert" className="text-ko">{error}</p>}
          <div className="flex gap-3">
            <button className="btn btn-primary" style={{ background: 'var(--ko)' }}>{T("Supprimer définitivement")}</button>
            <button type="button" className="btn btn-quiet" onClick={() => setConfirming(false)}>{T("Annuler")}</button>
          </div>
        </form>
      )}
    </section>
  );
}

/** Version hors ligne : défis planifiés par l'onglet ouvert, notification système facultative. */
function LocalNotifications() {
  const supported = typeof window !== 'undefined' && 'Notification' in window;
  const [perm, setPerm] = useState(supported ? Notification.permission : 'denied');
  return (
    <>
      <p className="font-bold">{T("Version hors ligne")}</p>
      <p className="text-sm text-ink-soft">{T("Les défis arrivent tant que Koto Quest est ouvert dans un onglet, même en arrière-plan. Garde l’onglet ouvert pendant ta journée.")}</p>
      {supported && perm !== 'granted' && (
        <button className="btn btn-primary mt-3 mr-3" onClick={async () => setPerm(await Notification.requestPermission())}>{T("Afficher aussi une notification du système")}</button>
      )}
      {perm === 'granted' && <p className="mt-2 text-sm">{T("Notifications système autorisées quand l’onglet est en arrière-plan.")}</p>}
    </>
  );
}

function LocalDataSection() {
  const [msg, setMsg] = useState<string | null>(null);
  const [confirming, setConfirming] = useState(false);
  const qc = useQueryClient();

  async function download() {
    const { exportBackup } = await import('../local/backend');
    const url = URL.createObjectURL(new Blob([exportBackup()], { type: 'application/json' }));
    const a = document.createElement('a');
    a.href = url;
    a.download = `koto-quest-sauvegarde-${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  }

  async function restore(file: File | undefined) {
    if (!file) return;
    try {
      const { importBackup } = await import('../local/backend');
      importBackup(await file.text());
      setMsg(T("Sauvegarde restaurée."));
      qc.invalidateQueries();
    } catch (e) {
      setMsg(e instanceof Error ? e.message : T("Fichier illisible."));
    }
  }

  async function reset() {
    const { resetAll } = await import('../local/backend');
    resetAll();
    qc.invalidateQueries();
    setConfirming(false);
  }

  return (
    <section aria-labelledby="data-title" className="flex flex-col gap-4">
      <h2 id="data-title" className="text-2xl">{T("Ma progression")}</h2>
      <p className="max-w-[62ch] text-ink-soft">{T("Ta progression est enregistrée dans ce navigateur, sur ton ordinateur. Elle disparaît si tu effaces les données du navigateur : télécharge une sauvegarde de temps en temps, ou pour continuer sur un autre ordinateur.")}</p>
      <div className="flex flex-wrap gap-3">
        <button className="btn btn-quiet" onClick={download}>{T("Télécharger une sauvegarde")}</button>
        <label className="btn btn-quiet cursor-pointer">{T("Restaurer une sauvegarde")}<input type="file" accept="application/json,.json" className="sr-only" onChange={(e) => restore(e.target.files?.[0])} />
        </label>
        <button className="btn btn-quiet text-ko" onClick={() => setConfirming(true)}>{T("Tout recommencer")}</button>
      </div>
      {msg && <p role="status">{msg}</p>}
      {confirming && (
        <div className="flex flex-col gap-3 rounded-2xl border-2 border-ko p-4">
          <p className="font-bold">{T("Effacer toute la progression de ce navigateur ? Cette action est définitive.")}</p>
          <div className="flex gap-3">
            <button className="btn btn-primary" style={{ background: 'var(--ko)' }} onClick={reset}>{T("Effacer ma progression")}</button>
            <button className="btn btn-quiet" onClick={() => setConfirming(false)}>{T("Annuler")}</button>
          </div>
        </div>
      )}
    </section>
  );
}
