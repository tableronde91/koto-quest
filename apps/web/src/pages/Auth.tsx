import { FormEvent, useState } from 'react';
import { Link, useLocation, useNavigate, useSearchParams } from 'react-router';
import { useQueryClient } from '@tanstack/react-query';
import { post } from '../api/client';
import { qk } from '../api/hooks';
import { DEFAULT_AVATAR } from '@koto/learning-engine';
import { HeroScene } from '../components/Illustrations';
import { LanguageSwitch } from '../components/LanguageSwitch';
import { T } from '../i18n';
import { SiteFooter } from './Legal';

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

  const startNow = () => {
    setMode('register');
    setError(null);
    document.getElementById('inscription')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    window.setTimeout(() => document.getElementById('displayName')?.focus({ preventScroll: true }), 400);
  };

  return (
    <>
    <div className="mx-auto flex max-w-5xl flex-col gap-16 px-5 pb-10 pt-6">
      <header className="flex flex-wrap items-center gap-3">
        <img src="/icons/icon.svg" alt="" className="h-12 w-12" />
        <p className="font-display text-xl">{T("Koto Quest")}</p>
        <span className="ml-auto flex items-center gap-2">
          <button
            type="button"
            className="btn btn-quiet min-h-10 px-3 text-sm md:hidden"
            onClick={() => {
              setMode('login');
              setError(null);
              document.getElementById('inscription')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }}
          >
            {T("Se connecter")}
          </button>
          <LanguageSwitch compact />
        </span>
      </header>

      {/* Héros : la mission, en clair */}
      <div className="grid items-center gap-10 md:grid-cols-[1.1fr_1fr]">
        <section aria-labelledby="hero-title">
          <p className="inline-flex items-center gap-2 rounded-full bg-surface-2 px-3 py-1 text-sm font-bold">
            <span lang="ja" className="jp">日本語</span> · {T("Préparation au JLPT, du N5 au N1")}
          </p>
          <h1 id="hero-title" className="mt-4 max-w-[20ch] text-4xl sm:text-5xl">{T("Apprends le japonais et réussis ton JLPT.")}</h1>
          <p className="mt-4 max-w-[54ch] text-lg text-ink-soft">
            {T("Koto Quest a une seule mission : aider chacun à apprendre le japonais et à se présenter serein aux examens du JLPT. Du premier hiragana jusqu’à l’examen blanc, tu progresses par leçons de 5 à 10 minutes, avec des révisions qui reviennent au moment où tu allais oublier.")}
          </p>
          <ul className="mt-5 flex flex-col gap-2">
            {[T("Un parcours aligné sur les niveaux officiels du JLPT"), T("Des examens blancs au format exact de l’épreuve"), T("Gratuit, sans publicité, en français ou en anglais")].map((x) => (
              <li key={x} className="flex items-start gap-2"><span aria-hidden="true" className="mt-0.5 font-bold text-ok">✓</span>{x}</li>
            ))}
          </ul>
          <div className="mt-6 hidden md:block"><HeroScene avatar={{ ...DEFAULT_AVATAR, outfit: 'outfit-yukata-ai', hat: 'hat-hachimaki' }} /></div>
        </section>

      <section id="inscription" aria-label={T("Créer un compte ou se connecter")} className="panel scroll-mt-6 p-6 sm:p-8">
        <div role="tablist" aria-label={T("Accès au compte")} className="mb-6 grid grid-cols-2 rounded-xl bg-surface-2 p-1">
          {(['register', 'login'] as const).map((m) => (
            <button key={m} role="tab" aria-selected={mode === m} onClick={() => { setMode(m); setError(null); }} className={`min-h-11 rounded-lg font-bold ${mode === m ? 'bg-surface shadow-sm' : 'text-ink-soft'}`}>
              {m === 'register' ? T("Créer un compte") : T("Se connecter")}
            </button>
          ))}
        </div>
        <form onSubmit={onSubmit} className="flex flex-col gap-4" noValidate={false}>
          {mode === 'register' && (
            <label className="flex flex-col gap-1 font-bold">{T("Pseudo")}<input id="displayName" name="displayName" required maxLength={40} autoComplete="nickname" className="field font-normal" />
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
          {mode === 'register' && (
            <p className="text-sm text-ink-soft">
              {T("En créant un compte, tu acceptes les")} <Link to="/conditions" className="underline">{T("conditions d’utilisation")}</Link>. {T("Tes données restent exportables et supprimables à tout moment depuis les réglages")} (<Link to="/confidentialite" className="underline">{T("confidentialité")}</Link>).
            </p>
          )}
        </form>
      </section>
      </div>

      {/* Le JLPT, niveau par niveau */}
      <section aria-labelledby="jlpt-title" className="flex flex-col gap-5">
        <div>
          <h2 id="jlpt-title" className="text-3xl">{T("Le JLPT, c’est quoi ?")}</h2>
          <p className="mt-2 max-w-[70ch] text-ink-soft">
            {T("Le JLPT (Japanese-Language Proficiency Test) est la certification de japonais la plus reconnue pour les non-japonophones. Il compte cinq niveaux, du N5 (débutant) au N1 (avancé), et a lieu une à deux fois par an selon les pays, en juillet et en décembre. Il évalue le vocabulaire, les kanji, la grammaire, la lecture et la compréhension orale.")}
          </p>
        </div>
        <ol className="grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
          {JLPT_LEVELS.map((l) => (
            <li key={l.id} className={`flex flex-col gap-2 rounded-3xl border-2 p-4 ${l.ready ? 'border-ink bg-surface' : 'border-dashed border-line'}`}>
              <div className="flex items-center justify-between gap-2">
                <span className="font-display text-3xl">{l.id}</span>
                <span className={`rounded-full px-2.5 py-0.5 text-xs font-bold ${l.ready ? 'bg-ok-bg' : 'bg-surface-2 text-ink-soft'}`}>{l.ready ? T("Disponible") : T("En préparation")}</span>
              </div>
              <p className="font-bold">{l.name()}</p>
              <p className="text-sm text-ink-soft">{l.text()}</p>
              <p className="mt-auto text-sm"><span className="font-bold">{T("≈ {0} kanji", [l.kanji])}</span> · {T("≈ {0} mots", [l.words])}</p>
            </li>
          ))}
        </ol>
        <p className="text-sm text-ink-soft">{T("Nombres de kanji et de mots : repères indicatifs couramment utilisés, non publiés par les organisateurs du JLPT.")}</p>
      </section>

      {/* Comment Koto Quest prépare */}
      <section aria-labelledby="how-title" className="flex flex-col gap-5">
        <h2 id="how-title" className="text-3xl">{T("Comment Koto Quest te prépare")}</h2>
        <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {FEATURES.map((f) => (
            <li key={f.glyph} className="flex gap-4 rounded-3xl border border-line bg-surface p-5">
              <span aria-hidden="true" lang="ja" className="jp flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl text-2xl font-black text-white" style={{ background: f.color }}>{f.glyph}</span>
              <div>
                <h3 className="text-lg">{f.title()}</h3>
                <p className="text-ink-soft">{f.text()}</p>
              </div>
            </li>
          ))}
        </ul>
      </section>

      {/* Appel final */}
      <section aria-labelledby="cta-title" className="relative overflow-hidden rounded-3xl bg-ink p-6 text-paper sm:p-10">
        <span aria-hidden="true" lang="ja" className="jp pointer-events-none absolute -right-6 -top-10 select-none text-[12rem] font-black leading-none opacity-[0.07]">合格</span>
        <h2 id="cta-title" className="relative max-w-[24ch] text-3xl sm:text-4xl">{T("Ton objectif JLPT commence aujourd’hui.")}</h2>
        <p className="relative mt-3 max-w-[56ch] text-lg opacity-85">{T("Débutant complet, étudiant, voyageur ou candidat à l’examen : fixe ton niveau visé et ta date d’examen, Koto Quest construit ton programme jour après jour.")}</p>
        <button className="btn btn-gold relative mt-6 min-h-14 px-6 text-lg" onClick={startNow}>{T("Commencer gratuitement")}</button>
      </section>

      <p className="text-sm text-ink-soft">{T("Koto Quest n’est pas affilié à la Japan Foundation ni à JEES, organisateurs du JLPT. Les examens blancs sont non officiels et ne garantissent pas la réussite.")}</p>
    </div>
    <div className="mx-auto max-w-5xl px-5"><SiteFooter className="mt-0" /></div>
    </>
  );
}

const JLPT_LEVELS = [
  { id: 'N5', ready: true, kanji: '100', words: '800', name: () => T("Les bases"), text: () => T("Lire hiragana, katakana et des kanji simples ; comprendre des phrases lentes du quotidien.") },
  { id: 'N4', ready: true, kanji: '300', words: '1 500', name: () => T("Japonais élémentaire"), text: () => T("Suivre des conversations courantes et lire des textes simples sur des sujets familiers.") },
  { id: 'N3', ready: true, kanji: '650', words: '3 750', name: () => T("Niveau intermédiaire"), text: () => T("Comprendre le japonais de la vie quotidienne à une vitesse presque naturelle.") },
  { id: 'N2', ready: true, kanji: '1 000', words: '6 000', name: () => T("Niveau avancé"), text: () => T("Lire articles et actualités, suivre des échanges de la vie courante et du travail.") },
  { id: 'N1', ready: true, kanji: '2 000', words: '10 000', name: () => T("Maîtrise"), text: () => T("Comprendre des textes complexes et abstraits et des discours dans des situations variées.") },
];

const FEATURES = [
  { glyph: '道', color: '#C8323F', title: () => T("Un mode histoire par niveau"), text: () => T("Samouraï au N5, ninja au N4, esprit au N3, onmyōji au N2, shōgun au N1 : chaque niveau est une aventure, avec des leçons de 5 à 10 minutes qui suivent le programme du JLPT.") },
  { glyph: '復', color: '#3FA7A0', title: () => T("Des révisions au bon moment"), text: () => T("La répétition espacée fait revenir chaque mot, kanji ou point de grammaire juste avant que tu l’oublies.") },
  { glyph: '試', color: '#D4A537', title: () => T("Des examens blancs JLPT"), text: () => T("Chaque épreuve au format exact de l’examen, corrigée immédiatement, pour arriver le jour J sans surprise.") },
  { glyph: '読', color: '#6E63B5', title: () => T("Des contes à lire"), text: () => T("Des contes japonais en japonais simple, tous ouverts dès le départ, pour s’habituer à lire vraiment.") },
  { glyph: '話', color: '#2E8B9A', title: () => T("Des expressions utiles"), text: () => T("Les phrases dont on a besoin au Japon, classées par situation, avec l’audio.") },
  { glyph: '闘', color: '#9C6B3E', title: () => T("Des duels entre amis"), text: () => T("Affronte d’autres apprenants en quiz rapides pour réviser en t’amusant et grimper au classement.") },
];

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
      <SiteFooter />
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
