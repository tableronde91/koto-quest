import { FormEvent, useState } from 'react';
import { Link, useLocation, useNavigate, useSearchParams } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import { post } from '../api/client';
import { qk } from '../api/hooks';
import { DEFAULT_AVATAR } from '@koto/learning-engine';
import { HeroScene } from '../components/Illustrations';
import { LanguageSwitch } from '../components/LanguageSwitch';
import { T } from '../i18n';

/** Accueil public : présentation courte + connexion / inscription. */
export function WelcomePage() {
  const [mode, setMode] = useState<'register' | 'login'>('register');
  const [error, setError] = useState<string | null>(null);
  const [pending, setPending] = useState(false);
  const qc = useQueryClient();
  const navigate = useNavigate();
  const location = useLocation();
  const from = (location.state as { from?: string } | null)?.from;

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const f = new FormData(e.currentTarget);
    setPending(true);
    setError(null);
    try {
      const body = { email: f.get('email'), password: f.get('password'), ...(mode === 'register' ? { displayName: f.get('displayName') } : {}) };
      await post(`/auth/${mode}`, body);
      await qc.invalidateQueries({ queryKey: qk.me });
      navigate(from && from !== '/welcome' ? from : '/', { replace: true });
    } catch (err) {
      setError(err instanceof Error ? err.message : T("Erreur"));
    } finally {
      setPending(false);
    }
  }

  return (
    <div className="mx-auto grid min-h-dvh max-w-5xl items-center gap-10 px-5 py-10 md:grid-cols-[1.1fr_1fr]">
      <section>
        <div className="flex flex-wrap items-center gap-3">
          <img src="/icons/icon.svg" alt="" className="h-12 w-12" />
          <p className="font-display text-xl">{T("Koto Quest")}</p>
          <span className="ml-auto"><LanguageSwitch compact /></span>
        </div>
        <div className="mt-8"><HeroScene avatar={{ ...DEFAULT_AVATAR, outfit: 'outfit-yukata-ai', hat: 'hat-hachimaki' }} /></div>
        <h1 className="mt-4 max-w-[18ch] text-4xl sm:text-5xl">{T("Un mot le matin, un défi l’après-midi.")}</h1>
        <p className="mt-4 max-w-[52ch] text-lg text-ink-soft">{T("Apprends le japonais du N5 au N1 par leçons de cinq à dix minutes. Chaque notion revient au moment où tu allais l’oublier, sous forme de petit défi.")}</p>
      </section>

      <section className="panel p-6 sm:p-8">
        <div role="tablist" aria-label={T("Accès au compte")} className="mb-6 grid grid-cols-2 rounded-xl bg-surface-2 p-1">
          {(['register', 'login'] as const).map((m) => (
            <button key={m} role="tab" aria-selected={mode === m} onClick={() => { setMode(m); setError(null); }} className={`min-h-11 rounded-lg font-bold ${mode === m ? 'bg-surface shadow-sm' : 'text-ink-soft'}`}>
              {m === 'register' ? T("Créer un compte") : T("Se connecter")}
            </button>
          ))}
        </div>
        <form onSubmit={onSubmit} className="flex flex-col gap-4" noValidate={false}>
          {mode === 'register' && (
            <label className="flex flex-col gap-1 font-bold">{T("Pseudo")}<input name="displayName" required maxLength={40} autoComplete="nickname" className="field font-normal" />
            </label>
          )}
          <label className="flex flex-col gap-1 font-bold">{T("Adresse e-mail")}<input name="email" type="email" required autoComplete="email" className="field font-normal" />
          </label>
          <label className="flex flex-col gap-1 font-bold">{T("Mot de passe")}<input name="password" type="password" required minLength={mode === 'register' ? 8 : 1} autoComplete={mode === 'register' ? 'new-password' : 'current-password'} className="field font-normal" />
            {mode === 'register' && <span className="text-sm font-normal text-ink-soft">{T("8 caractères minimum.")}</span>}
          </label>
          {error && <p role="alert" className="rounded-xl bg-ko-bg p-3 font-bold">{error}</p>}
          <button className="btn btn-primary mt-2" disabled={pending}>
            {pending ? T("Un instant…") : mode === 'register' ? T("Créer mon compte") : T("Me connecter")}
          </button>
          {mode === 'login' && <Link to="/forgot-password" className="text-center text-ink-soft underline">{T("Mot de passe oublié ?")}</Link>}
          {mode === 'register' && <p className="text-sm text-ink-soft">{T("Tes données restent exportables et supprimables à tout moment depuis les réglages.")}</p>}
        </form>
      </section>
    </div>
  );
}

export function ForgotPasswordPage() {
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    try {
      const r = await post<{ message: string }>('/auth/forgot-password', { email: new FormData(e.currentTarget).get('email') });
      setMessage(r.message);
    } catch (err) {
      setError(err instanceof Error ? err.message : T("Erreur"));
    }
  }
  return (
    <div className="mx-auto max-w-md px-5 py-16">
      <h1 className="text-3xl">{T("Mot de passe oublié")}</h1>
      {message ? (
        <p role="status" className="mt-6 rounded-xl bg-ok-bg p-4">{message}</p>
      ) : (
        <form onSubmit={onSubmit} className="mt-6 flex flex-col gap-4">
          <label className="flex flex-col gap-1 font-bold">{T("Adresse e-mail du compte")}<input name="email" type="email" required className="field font-normal" />
          </label>
          {error && <p role="alert" className="text-ko">{error}</p>}
          <button className="btn btn-primary">{T("Recevoir un lien")}</button>
        </form>
      )}
      <Link to="/welcome" className="mt-6 inline-block underline">{T("Retour à la connexion")}</Link>
    </div>
  );
}

export function ResetPasswordPage() {
  const [params] = useSearchParams();
  const [done, setDone] = useState(false);
  const [error, setError] = useState<string | null>(null);
  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    try {
      await post('/auth/reset-password', { token: params.get('token'), password: new FormData(e.currentTarget).get('password') });
      setDone(true);
    } catch (err) {
      setError(err instanceof Error ? err.message : T("Erreur"));
    }
  }
  return (
    <div className="mx-auto max-w-md px-5 py-16">
      <h1 className="text-3xl">{T("Nouveau mot de passe")}</h1>
      {done ? (
        <p role="status" className="mt-6 rounded-xl bg-ok-bg p-4">{T("Mot de passe modifié.")}{' '}<Link to="/welcome" className="underline">{T("Se connecter")}</Link></p>
      ) : (
        <form onSubmit={onSubmit} className="mt-6 flex flex-col gap-4">
          <label className="flex flex-col gap-1 font-bold">{T("Nouveau mot de passe (8 caractères minimum)")}<input name="password" type="password" minLength={8} required autoComplete="new-password" className="field font-normal" />
          </label>
          {error && <p role="alert" className="text-ko">{error}</p>}
          <button className="btn btn-primary">{T("Enregistrer le mot de passe")}</button>
        </form>
      )}
    </div>
  );
}
