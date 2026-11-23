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
            <span lang="ja" className="jp">日本語</span> · <span lang="ko" className="jp">한국어</span> · <span lang="en">English</span> · <span lang="zh" className="jp">中文</span> · {T("Préparation au JLPT, au TOPIK, au TOEIC et au HSK")}
          </p>
          <h1 id="hero-title" className="mt-4 max-w-[22ch] text-4xl sm:text-5xl">{T("Apprends le japonais, le coréen, l’anglais ou le chinois, et réussis ton examen.")}</h1>
          <p className="mt-4 max-w-[54ch] text-lg text-ink-soft">
            {T("Koto Quest a une seule mission : aider chacun à apprendre une langue et à se présenter serein à son examen, le JLPT pour le japonais, le TOPIK pour le coréen, le TOEIC pour l’anglais, le HSK pour le chinois. Du premier mot jusqu’à l’examen blanc, tu progresses par leçons de 5 à 10 minutes, avec des révisions qui reviennent au moment où tu allais oublier.")}
          </p>
          <ul className="mt-5 flex flex-col gap-2">
            {[T("Un parcours aligné sur les niveaux officiels du JLPT, du TOPIK, du CECRL et du HSK"), T("Des examens blancs au format exact de l’épreuve"), T("Gratuit, sans publicité, en français ou en anglais")].map((x) => (
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

      {/* Le TOPIK, pour le coréen */}
      <section aria-labelledby="topik-title" className="flex flex-col gap-5">
        <div>
          <h2 id="topik-title" className="text-3xl">{T("Et le coréen ? Le TOPIK")}</h2>
          <p className="mt-2 max-w-[70ch] text-ink-soft">
            {T("Le TOPIK (Test of Proficiency in Korean) est l’examen officiel de coréen pour les non-coréanophones. Le TOPIK I couvre les niveaux 1 et 2, le TOPIK II les niveaux 3 à 6 ; le niveau dépend du score obtenu. Il évalue l’écoute et la lecture, et l’écriture au TOPIK II. Koto Quest commence par le hangeul, l’alphabet coréen, que l’on apprend en quelques jours.")}
          </p>
        </div>
        <ol className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {TOPIK_LEVELS.map((l) => (
            <li key={l.id} className={`flex flex-col gap-2 rounded-3xl border-2 p-4 ${l.ready ? 'border-ink bg-surface' : 'border-dashed border-line'}`}>
              <div className="flex items-center justify-between gap-2">
                <span className="font-display text-2xl">{l.id}</span>
                <span className={`rounded-full px-2.5 py-0.5 text-xs font-bold ${l.ready ? 'bg-ok-bg' : 'bg-surface-2 text-ink-soft'}`}>{l.ready ? T("Disponible") : T("En préparation")}</span>
              </div>
              <p className="font-bold">{l.name()}</p>
              <p className="text-sm text-ink-soft">{l.text()}</p>
            </li>
          ))}
        </ol>
      </section>

      {/* Le TOEIC, pour l'anglais */}
      <section aria-labelledby="toeic-title" className="flex flex-col gap-5">
        <div>
          <h2 id="toeic-title" className="text-3xl">{T("Et l’anglais ? Le TOEIC")}</h2>
          <p className="mt-2 max-w-[70ch] text-ink-soft">
            {T("Le TOEIC Listening & Reading est le test d’anglais professionnel le plus demandé par les entreprises. Il est noté sur 990 points (495 en écoute, 495 en lecture). Koto Quest suit les niveaux du CECRL, de A1 à C1, avec pour chacun le score TOEIC correspondant, et mêle l’anglais du bureau aux légendes britanniques.")}
          </p>
        </div>
        <ol className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {TOEIC_LEVELS.map((l) => (
            <li key={l.id} className="flex flex-col gap-2 rounded-3xl border-2 border-ink bg-surface p-4">
              <div className="flex items-center justify-between gap-2">
                <span className="font-display text-2xl">{l.id}</span>
                <span className="rounded-full bg-ok-bg px-2.5 py-0.5 text-xs font-bold">{T("Disponible")}</span>
              </div>
              <p className="font-bold">{l.name()}</p>
              <p className="text-sm text-ink-soft">{l.text()}</p>
            </li>
          ))}
        </ol>
      </section>

      {/* Le HSK, pour le chinois */}
      <section aria-labelledby="hsk-title" className="flex flex-col gap-5">
        <div>
          <h2 id="hsk-title" className="text-3xl">{T("Et le chinois ? Le HSK")}</h2>
          <p className="mt-2 max-w-[70ch] text-ink-soft">
            {T("Le HSK (Hanyu Shuiping Kaoshi) est l’examen officiel de chinois pour les non-sinophones. Il compte six niveaux, de 150 mots au HSK 1 à plus de 5 000 au HSK 6. Koto Quest suit le format des sessions de 2026, avec le pinyin au-dessus des caractères qui s’efface au fil des niveaux, et t’emmène à travers les Royaumes combattants.")}
          </p>
        </div>
        <ol className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {HSK_LEVELS.map((l) => (
            <li key={l.id} className={`flex flex-col gap-2 rounded-3xl border-2 p-4 ${l.ready ? 'border-ink bg-surface' : 'border-dashed border-line bg-surface-2'}`}>
              <div className="flex items-center justify-between gap-2">
                <span className="font-display text-2xl">{l.id}</span>
                <span className={`rounded-full px-2.5 py-0.5 text-xs font-bold ${l.ready ? 'bg-ok-bg' : 'bg-surface text-ink-soft'}`}>{l.ready ? T("Disponible") : T("Bientôt")}</span>
              </div>
              <p className="font-bold">{l.name()}</p>
              <p className="text-sm text-ink-soft">{l.text()}</p>
            </li>
          ))}
        </ol>
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
        <h2 id="cta-title" className="relative max-w-[24ch] text-3xl sm:text-4xl">{T("Ton objectif JLPT, TOPIK, TOEIC ou HSK commence aujourd’hui.")}</h2>
        <p className="relative mt-3 max-w-[56ch] text-lg opacity-85">{T("Débutant complet, étudiant, voyageur ou candidat à l’examen : fixe ton niveau visé et ta date d’examen, Koto Quest construit ton programme jour après jour.")}</p>
        <button className="btn btn-gold relative mt-6 min-h-14 px-6 text-lg" onClick={startNow}>{T("Commencer gratuitement")}</button>
      </section>

      <p className="text-sm text-ink-soft">{T("Koto Quest n’est pas affilié à la Japan Foundation ni à JEES, organisateurs du JLPT, ni au NIIED, organisateur du TOPIK, ni à ETS, organisateur du TOEIC, ni au CLEC (Centre for Language Education and Cooperation), organisateur du HSK. Les examens blancs sont non officiels et ne garantissent pas la réussite.")}</p>
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

const TOPIK_LEVELS = [
  { id: 'TOPIK 1', ready: true, name: () => T("Débutant (TOPIK I)"), text: () => T("Lire le hangeul, se présenter, compter, faire ses courses et parler de son quotidien au présent, au passé et au futur.") },
  { id: 'TOPIK 2', ready: true, name: () => T("Élémentaire (TOPIK I)"), text: () => T("Expliquer pourquoi, demander la permission, raconter ses expériences, décrire, situer dans le temps et parler poliment des aînés.") },
  { id: 'TOPIK 3', ready: true, name: () => T("Intermédiaire (TOPIK II)"), text: () => T("Rapporter des paroles, expliquer un contexte, raconter un changement, exprimer un but, le passif et le causatif, regrets et souhaits.") },
  { id: 'TOPIK 4', ready: true, name: () => T("Intermédiaire avancé (TOPIK II)"), text: () => T("Distinguer le vu de l’entendu, deviner, faire des hypothèses, la concession, causes et conséquences, l’actualité et la société.") },
  { id: 'TOPIK 5', ready: true, name: () => T("Avancé (TOPIK II)"), text: () => T("Nuancer, comparer, argumenter, exprimer l’inévitable et le paradoxe : mythes, chamanisme et grands débats de société.") },
  { id: 'TOPIK 6', ready: true, name: () => T("Maîtrise (TOPIK II)"), text: () => T("Style écrit soutenu, proverbes et expressions en quatre caractères, textes académiques et mythes fondateurs de la Corée.") },
];

const TOEIC_LEVELS = [
  { id: 'A1', name: () => T("Découverte · TOEIC 120+"), text: () => T("Saluer, se présenter, compter, l’heure, commander, demander son chemin, le présent et le prétérit.") },
  { id: 'A2', name: () => T("Survie · TOEIC 225+"), text: () => T("Raconter au passé, comparer, parler de ses projets, le present perfect, les règles et les conditions simples.") },
  { id: 'B1', name: () => T("Seuil · TOEIC 550+"), text: () => T("E-mails professionnels, téléphone, entretien, passif, discours rapporté, hypothèses et négociation.") },
  { id: 'B2', name: () => T("Avancé · TOEIC 785+"), text: () => T("Présentations, finance, ressources humaines, rapports, conditionnels mixtes et langage diplomatique.") },
  { id: 'C1', name: () => T("Autonome · TOEIC 945+"), text: () => T("Registre soutenu, idiomes, nuances, stratégie, contrats et négociation de haut niveau.") },
];

const HSK_LEVELS = [
  { id: 'HSK 1', ready: true, name: () => T("Découverte · 150 mots"), text: () => T("Le pinyin et les tons, les nombres, se présenter, la famille, les achats, l’heure, les transports et le temps qu’il fait.") },
  { id: 'HSK 2', ready: true, name: () => T("Élémentaire · 300 mots"), text: () => T("Comparer, raconter une expérience, les compléments de résultat et de durée, les petits échanges du quotidien.") },
  { id: 'HSK 3', ready: true, name: () => T("Intermédiaire · 600 mots"), text: () => T("Se débrouiller en voyage, au travail et à l’école ; 把, 被, les compléments de direction ; premiers textes sans pinyin.") },
  { id: 'HSK 4', ready: false, name: () => T("Intermédiaire avancé · 1 200 mots"), text: () => T("Discuter de sujets variés avec des natifs, lire des textes courants et rédiger de courtes phrases.") },
  { id: 'HSK 5', ready: false, name: () => T("Avancé · 2 500 mots"), text: () => T("Lire journaux et magazines, suivre films et émissions, faire un exposé structuré.") },
  { id: 'HSK 6', ready: false, name: () => T("Maîtrise · 5 000 mots"), text: () => T("Comprendre sans effort ce qu’on lit et entend, chengyu et langue écrite soutenue.") },
];

const FEATURES = [
  { glyph: '道', color: '#C8323F', title: () => T("Un mode histoire par niveau"), text: () => T("Samouraï au N5, ninja au N4, esprit au N3, onmyōji au N2, shōgun au N1 ; en coréen, apprenti hwarang au TOPIK 1, conteur au TOPIK 2, inspecteur royal au TOPIK 3, historien au TOPIK 4, chanteur de mythes au TOPIK 5, gardien des mythes au TOPIK 6 ; en anglais, apprenti de Merlin en A1 jusqu’à héritier d’Arthur en C1 ; en chinois, messager des Royaumes au HSK 1 : chaque niveau est une aventure, avec des leçons de 5 à 10 minutes qui suivent le programme de l’examen.") },
  { glyph: '復', color: '#3FA7A0', title: () => T("Des révisions au bon moment"), text: () => T("La répétition espacée fait revenir chaque mot, kanji ou point de grammaire juste avant que tu l’oublies.") },
  { glyph: '試', color: '#D4A537', title: () => T("Des examens blancs JLPT, TOPIK, TOEIC et HSK"), text: () => T("Au format exact du JLPT, du TOPIK et du HSK, au format abrégé du TOEIC, corrigés immédiatement, pour arriver le jour J sans surprise.") },
  { glyph: '読', color: '#6E63B5', title: () => T("Des contes à lire"), text: () => T("Des contes japonais, coréens et britanniques et des fables chinoises en langue simple, tous ouverts dès le départ, pour s’habituer à lire vraiment.") },
  { glyph: '話', color: '#2E8B9A', title: () => T("Des expressions utiles"), text: () => T("Les phrases dont on a besoin au Japon, en Corée, en Chine ou en anglais, classées par situation, avec l’audio.") },
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
