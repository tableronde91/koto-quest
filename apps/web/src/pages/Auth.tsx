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
  const [lang, setLang] = useState<(typeof LANGS)[number]['id']>('ja');
  const current = LANGS.find((l) => l.id === lang)!;

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

      {/* Héros : la promesse en une phrase */}
      <div className="grid items-center gap-10 md:grid-cols-[1.1fr_1fr]">
        <section aria-labelledby="hero-title">
          <p className="inline-flex flex-wrap items-center gap-x-2 rounded-full bg-surface-2 px-3 py-1 text-sm font-bold">
            <span lang="ja" className="jp">日本語</span> · <span lang="ko" className="jp">한국어</span> · <span lang="en">English</span> · <span lang="zh" className="jp">中文</span> · <span lang="es">Español</span>
          </p>
          <h1 id="hero-title" className="mt-4 max-w-[16ch] text-4xl sm:text-5xl">{T("Apprends une langue. Réussis ton examen.")}</h1>
          <p className="mt-4 max-w-[46ch] text-lg text-ink-soft">{T("Des leçons de 5 à 10 minutes, des révisions au bon moment et des examens blancs, du premier mot jusqu’au jour J.")}</p>
          <ul className="mt-5 flex flex-col gap-2">
            {[T("JLPT, TOPIK, TOEIC, HSK ou DELE : un parcours par niveau officiel"), T("Gratuit, sans publicité, en français ou en anglais")].map((x) => (
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

      {/* Cinq langues : une seule visible à la fois, le détail de l'examen sur demande */}
      <section aria-labelledby="langs-title" className="flex flex-col gap-5">
        <h2 id="langs-title" className="text-3xl">{T("Cinq langues, cinq examens")}</h2>
        <div role="tablist" aria-label={T("Langue à découvrir")} className="-mx-5 flex gap-2 overflow-x-auto px-5 pb-1 sm:mx-0 sm:flex-wrap sm:overflow-visible sm:px-0">
          {LANGS.map((l) => (
            <button key={l.id} role="tab" id={`lang-${l.id}`} aria-selected={lang === l.id} aria-controls="lang-panel" onClick={() => setLang(l.id)} className={`flex min-h-14 shrink-0 items-center gap-3 rounded-2xl border-2 px-4 text-left ${lang === l.id ? 'border-ink bg-ink text-paper' : 'border-line bg-surface hover:border-ink-soft'}`}>
              <span aria-hidden="true" className="jp text-2xl font-black">{l.glyph}</span>
              <span className="leading-tight"><span className="block font-bold">{l.name()}</span><span className={`text-sm ${lang === l.id ? 'opacity-80' : 'text-ink-soft'}`}>{l.exam}</span></span>
            </button>
          ))}
        </div>
        <div id="lang-panel" role="tabpanel" aria-labelledby={`lang-${current.id}`} className="panel flex flex-col gap-4 p-5 sm:p-6">
          <p className="max-w-[60ch] text-lg">{current.pitch()}</p>
          <ol className="flex flex-wrap gap-2">
            {current.levels.map((l) => (
              <li key={l.id} className="rounded-2xl border border-line bg-surface-2 px-3 py-2 leading-tight">
                <span className="block font-display text-lg">{l.id}</span>
                <span className="text-sm text-ink-soft">{l.name()}</span>
              </li>
            ))}
          </ol>
          <details className="text-ink-soft">
            <summary className="cursor-pointer font-bold text-ink underline">{T("En savoir plus sur l’examen ({0})", [current.exam])}</summary>
            <p className="mt-2 max-w-[70ch]">{current.about()}</p>
          </details>
        </div>
      </section>

      {/* Comment Koto Quest prépare */}
      <section aria-labelledby="how-title" className="flex flex-col gap-5">
        <h2 id="how-title" className="text-3xl">{T("Comment Koto Quest te prépare")}</h2>
        <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {FEATURES.map((f) => (
            <li key={f.glyph} className="flex items-center gap-4 rounded-3xl border border-line bg-surface p-4">
              <span aria-hidden="true" lang="ja" className="jp flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl text-2xl font-black text-white" style={{ background: f.color }}>{f.glyph}</span>
              <div>
                <h3 className="text-lg leading-tight">{f.title()}</h3>
                <p className="text-sm text-ink-soft">{f.text()}</p>
              </div>
            </li>
          ))}
        </ul>
      </section>

      {/* Appel final */}
      <section aria-labelledby="cta-title" className="relative overflow-hidden rounded-3xl bg-ink p-6 text-paper sm:p-10">
        <span aria-hidden="true" lang="ja" className="jp pointer-events-none absolute -right-6 -top-10 select-none text-[12rem] font-black leading-none opacity-[0.07]">合格</span>
        <h2 id="cta-title" className="relative max-w-[24ch] text-3xl sm:text-4xl">{T("Ton examen commence aujourd’hui.")}</h2>
        <p className="relative mt-3 max-w-[50ch] text-lg opacity-85">{T("Fixe ton niveau visé et ta date d’examen : Koto Quest construit ton programme jour après jour.")}</p>
        <button className="btn btn-gold relative mt-6 min-h-14 px-6 text-lg" onClick={startNow}>{T("Commencer gratuitement")}</button>
      </section>

      <p className="text-xs text-ink-soft">{T("Koto Quest n’est affilié à aucun organisateur d’examen (Japan Foundation et JEES pour le JLPT, NIIED pour le TOPIK, ETS pour le TOEIC, CLEC pour le HSK, Instituto Cervantes pour le DELE). Les examens blancs sont non officiels et ne garantissent pas la réussite.")}</p>
    </div>
    <div className="mx-auto max-w-5xl px-5"><SiteFooter className="mt-0" /></div>
    </>
  );
}

/** Les cinq langues de la page d'accueil : une phrase, les niveaux, et le détail de l'examen replié. */
const LANGS = [
  {
    id: 'ja', glyph: '言', exam: 'JLPT', name: () => T("Japonais"),
    pitch: () => T("Du N5 au N1, des hiragana aux textes complexes, sur les pas d’un apprenti samouraï."),
    about: () => T("Le JLPT (Japanese-Language Proficiency Test) est la certification de japonais la plus reconnue pour les non-japonophones. Il compte cinq niveaux, du N5 (débutant) au N1 (avancé), et a lieu une à deux fois par an selon les pays, en juillet et en décembre. Il évalue le vocabulaire, les kanji, la grammaire, la lecture et la compréhension orale."),
    levels: [
      { id: 'N5', name: () => T("Les bases") },
      { id: 'N4', name: () => T("Japonais élémentaire") },
      { id: 'N3', name: () => T("Niveau intermédiaire") },
      { id: 'N2', name: () => T("Niveau avancé") },
      { id: 'N1', name: () => T("Maîtrise") },
    ],
  },
  {
    id: 'ko', glyph: '한', exam: 'TOPIK', name: () => T("Coréen"),
    pitch: () => T("Du TOPIK 1 au TOPIK 6, en commençant par le hangeul, l’alphabet coréen."),
    about: () => T("Le TOPIK (Test of Proficiency in Korean) est l’examen officiel de coréen pour les non-coréanophones. Le TOPIK I couvre les niveaux 1 et 2, le TOPIK II les niveaux 3 à 6 ; le niveau dépend du score obtenu. Il évalue l’écoute et la lecture, et l’écriture au TOPIK II. Koto Quest commence par le hangeul, l’alphabet coréen, que l’on apprend en quelques jours."),
    levels: [
      { id: 'TOPIK 1', name: () => T("Débutant (TOPIK I)") },
      { id: 'TOPIK 2', name: () => T("Élémentaire (TOPIK I)") },
      { id: 'TOPIK 3', name: () => T("Intermédiaire (TOPIK II)") },
      { id: 'TOPIK 4', name: () => T("Intermédiaire avancé (TOPIK II)") },
      { id: 'TOPIK 5', name: () => T("Avancé (TOPIK II)") },
      { id: 'TOPIK 6', name: () => T("Maîtrise (TOPIK II)") },
    ],
  },
  {
    id: 'en', glyph: 'E', exam: 'TOEIC', name: () => T("Anglais"),
    pitch: () => T("Du A1 au C1, avec le score TOEIC visé à chaque niveau."),
    about: () => T("Le TOEIC Listening & Reading est le test d’anglais professionnel le plus demandé par les entreprises. Il est noté sur 990 points (495 en écoute, 495 en lecture). Koto Quest suit les niveaux du CECRL, de A1 à C1, avec pour chacun le score TOEIC correspondant, et mêle l’anglais du bureau aux légendes britanniques."),
    levels: [
      { id: 'A1', name: () => T("Découverte · TOEIC 120+") },
      { id: 'A2', name: () => T("Survie · TOEIC 225+") },
      { id: 'B1', name: () => T("Seuil · TOEIC 550+") },
      { id: 'B2', name: () => T("Avancé · TOEIC 785+") },
      { id: 'C1', name: () => T("Autonome · TOEIC 945+") },
    ],
  },
  {
    id: 'zh', glyph: '中', exam: 'HSK', name: () => T("Chinois"),
    pitch: () => T("Du HSK 1 au HSK 6, avec le pinyin qui s’efface au fil des niveaux."),
    about: () => T("Le HSK (Hanyu Shuiping Kaoshi) est l’examen officiel de chinois pour les non-sinophones. Il compte six niveaux, de 150 mots au HSK 1 à plus de 5 000 au HSK 6. Koto Quest suit le format des sessions de 2026, avec le pinyin au-dessus des caractères qui s’efface au fil des niveaux, et t’emmène à travers les Royaumes combattants."),
    levels: [
      { id: 'HSK 1', name: () => T("Découverte · 150 mots") },
      { id: 'HSK 2', name: () => T("Élémentaire · 300 mots") },
      { id: 'HSK 3', name: () => T("Intermédiaire · 600 mots") },
      { id: 'HSK 4', name: () => T("Intermédiaire avancé · 1 200 mots") },
      { id: 'HSK 5', name: () => T("Avancé · 2 500 mots") },
      { id: 'HSK 6', name: () => T("Maîtrise · 5 000 mots") },
    ],
  },
  {
    id: 'es', glyph: 'Ñ', exam: 'DELE', name: () => T("Espagnol"),
    pitch: () => T("Du A1 au C2, de la Manche de Don Quichotte aux classiques d’Amérique latine."),
    about: () => T("Le DELE (Diplomas de Español como Lengua Extranjera) est le diplôme officiel d’espagnol délivré au nom du ministère espagnol de l’Éducation par l’Instituto Cervantes. Il suit les six niveaux du CECRL, de A1 à C2. Koto Quest t’y prépare en six étapes : la Manche de Don Quichotte, la route de Barcelone, le chemin de Saint-Jacques, la traversée des Amériques, la Bibliothèque enchantée et son Rayon secret."),
    levels: [
      { id: 'DELE A1', name: () => T("Découverte") },
      { id: 'DELE A2', name: () => T("Survie") },
      { id: 'DELE B1', name: () => T("Seuil") },
      { id: 'DELE B2', name: () => T("Avancé") },
      { id: 'DELE C1', name: () => T("Autonome") },
      { id: 'DELE C2', name: () => T("Maîtrise") },
    ],
  },
] as const;

const FEATURES = [
  { glyph: '道', color: '#C8323F', title: () => T("Une histoire par niveau"), text: () => T("Chaque niveau est une aventure, avec ses îles et ses gardiens à vaincre.") },
  { glyph: '復', color: '#3FA7A0', title: () => T("Des révisions au bon moment"), text: () => T("Chaque notion revient juste avant que tu l’oublies.") },
  { glyph: '試', color: '#D4A537', title: () => T("Des examens blancs"), text: () => T("Au format de l’épreuve, chronométrés et corrigés aussitôt.") },
  { glyph: '読', color: '#6E63B5', title: () => T("Des contes à lire"), text: () => T("Des contes et légendes en langue simple, ouverts dès le départ.") },
  { glyph: '話', color: '#2E8B9A', title: () => T("Des expressions utiles"), text: () => T("Les phrases du quotidien, classées par situation, avec l’audio.") },
  { glyph: '闘', color: '#9C6B3E', title: () => T("Des duels entre amis"), text: () => T("Des quiz rapides contre d’autres apprenants, pour réviser en t’amusant.") },
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
