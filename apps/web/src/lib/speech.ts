/**
 * Synthèse vocale (japonais, coréen, anglais, chinois) via le navigateur (gratuite, sans fichier audio à licencier).
 *
 * Toute la lecture passe par `say()`, qui contourne les défauts connus des navigateurs :
 * - les voix se chargent en différé : au premier appel, la liste est vide et le navigateur lit le
 *   japonais avec une voix étrangère (souvent muette) → on attend la liste avant de parler ;
 * - les voix « en ligne » (Google 日本語…) mettent parfois plusieurs secondes à démarrer, ou ne
 *   démarrent pas → on préfère une voix japonaise installée sur l'appareil ;
 * - `cancel()` suivi immédiatement de `speak()` fait sauter ou retarder la phrase suivante (Chrome)
 *   → si une lecture était en cours, on laisse un court instant au moteur pour s'arrêter ;
 * - un moteur resté « en pause » ne lit plus rien → `resume()` avant chaque lecture ;
 * - Chrome peut libérer une phrase en cours de lecture (plus d'événement de fin) → on garde une
 *   référence sur les phrases jusqu'à la fin ;
 * - deux lectures demandées coup sur coup se chevauchaient → seule la dernière demande est jouée.
 */
import { scriptAccents, textLanguage } from '@koto/shared';

export const speechSupported = () => typeof window !== 'undefined' && 'speechSynthesis' in window;

export interface SpeechPart {
  text: string;
  rate?: number;
  pitch?: number;
  /** Variante régionale (ex. en-US) : écoutes TOEIC aux accents variés */
  locale?: string;
  onStart?: () => void;
}

type VoiceLang = 'ja' | 'ko' | 'en' | 'zh' | 'es';
const LOCALE: Record<VoiceLang, string> = { ja: 'ja-JP', ko: 'ko-KR', en: 'en-GB', zh: 'zh-CN', es: 'es-ES' };
const voices = new Map<VoiceLang, SpeechSynthesisVoice | null>();
let voicesReady: Promise<void> | null = null;

/** Langue d'un texte : coréen (hangeul), japonais (kana), chinois (caractères seuls quand on étudie le chinois) ou anglais (alphabet latin). */
export const voiceLangOf = (text: string): VoiceLang => textLanguage(text);

/** Meilleure voix pour la langue : installée sur l'appareil d'abord (démarrage immédiat), puis en ligne. */
function chooseVoice(lang: VoiceLang): SpeechSynthesisVoice | null {
  const list = speechSynthesis.getVoices().filter((v) => v.lang.toLowerCase().replace('_', '-').startsWith(lang));
  if (!list.length) return null;
  // Chinois : mandarin de Chine continentale d'abord, jamais le cantonais (zh-HK) si une autre voix existe.
  const score = (v: SpeechSynthesisVoice) => (v.localService ? 4 : 0) + (v.lang.toLowerCase().replace('_', '-') === LOCALE[lang].toLowerCase() ? 2 : 0) + (v.default ? 1 : 0) - (/zh-hk|yue/.test(v.lang.toLowerCase().replace('_', '-')) ? 10 : 0);
  return [...list].sort((a, b) => score(b) - score(a))[0];
}

/** Voix d'une variante régionale (en-US, en-AU…) ; à défaut, américaine pour le Canada, puis toute voix de la langue. */
const localeVoices = new Map<string, SpeechSynthesisVoice | null>();
function pickLocaleVoice(locale: string, lang: VoiceLang): SpeechSynthesisVoice | null {
  if (!speechSupported()) return null;
  if (!localeVoices.get(locale)) {
    const norm = (v: SpeechSynthesisVoice) => v.lang.toLowerCase().replace('_', '-');
    const all = speechSynthesis.getVoices();
    const find = (l: string) => all.filter((v) => norm(v) === l.toLowerCase()).sort((a, b) => Number(b.localService) - Number(a.localService))[0];
    localeVoices.set(locale, find(locale) ?? (locale === 'en-CA' ? find('en-US') : undefined) ?? null);
  }
  return localeVoices.get(locale) ?? pickVoice(lang);
}

function pickVoice(lang: VoiceLang = 'ja') {
  if (!speechSupported()) return null;
  if (!voices.has(lang) || !voices.get(lang)) voices.set(lang, chooseVoice(lang));
  return voices.get(lang) ?? null;
}

/** Attend que la liste des voix soit disponible (au plus 1,5 s : certains navigateurs n'envoient jamais l'événement). */
function loadVoices(): Promise<void> {
  if (!speechSupported()) return Promise.resolve();
  if (speechSynthesis.getVoices().length) return Promise.resolve();
  voicesReady ??= new Promise<void>((resolve) => {
    const done = () => {
      speechSynthesis.removeEventListener?.('voiceschanged', done);
      voices.clear();
      resolve();
    };
    speechSynthesis.addEventListener?.('voiceschanged', done);
    window.setTimeout(done, 1500);
  });
  return voicesReady;
}

if (speechSupported()) {
  speechSynthesis.addEventListener?.('voiceschanged', () => {
    voices.clear();
    localeVoices.clear();
  });
  // Charge la liste des voix dès le démarrage, pour que la première lecture parte tout de suite.
  speechSynthesis.getVoices();
}

let request = 0;
const live = new Set<SpeechSynthesisUtterance>();

/** Lit une suite de phrases ; remplace toute lecture en cours. Renvoie false si le navigateur ne sait pas parler. */
export function say(parts: SpeechPart[], onEnd?: () => void): boolean {
  if (!speechSupported()) return false;
  const list = parts.filter((p) => p.text.trim());
  if (!list.length) return false;
  const my = ++request;
  const wasBusy = speechSynthesis.speaking || speechSynthesis.pending;
  speechSynthesis.cancel();
  live.clear();

  const go = () => {
    if (my !== request) return; // une lecture plus récente a été demandée entre-temps
    speechSynthesis.resume();
    list.forEach((p, i) => {
      // Chaque phrase est lue par une voix de sa langue (japonais ou coréen).
      const lang = voiceLangOf(p.text);
      const v = p.locale && lang === 'en' ? pickLocaleVoice(p.locale, lang) : pickVoice(lang);
      const u = new SpeechSynthesisUtterance(p.text);
      u.lang = v?.lang ?? (p.locale && lang === 'en' ? p.locale : LOCALE[lang]);
      try {
        if (v) u.voice = v;
      } catch {
        // voix refusée par le navigateur : la langue suffit
      }
      u.rate = p.rate ?? 0.9;
      u.pitch = p.pitch ?? 1;
      u.volume = 1;
      live.add(u);
      if (p.onStart) u.onstart = () => my === request && p.onStart?.();
      const finish = () => {
        live.delete(u);
        if (i === list.length - 1 && my === request) onEnd?.();
      };
      u.onend = finish;
      u.onerror = finish;
      speechSynthesis.speak(u);
    });
  };

  const ready = speechSynthesis.getVoices().length > 0;
  if (ready && !wasBusy) go();
  else loadVoices().then(() => (wasBusy ? window.setTimeout(go, 120) : go()));
  return true;
}

export function speak(text: string, slow = false) {
  if (!text) return false;
  return say([{ text, rate: slow ? 0.55 : 0.9 }]);
}

/** Arrête toute lecture (et annule une lecture en attente de démarrage). */
export function stopSpeech() {
  if (!speechSupported()) return;
  request++;
  live.clear();
  speechSynthesis.cancel();
}

export const hasJapaneseVoice = () => !!pickVoice('ja');
export const hasVoiceFor = (lang: VoiceLang) => !!pickVoice(lang);

/**
 * Document d'écoute d'examen : lignes « N|… » (narrateur), « M|… » (homme), « F|… » (femme).
 * Une seule voix japonaise est souvent disponible : on distingue les rôles par la hauteur de voix.
 * En anglais, comme au TOEIC, chaque rôle a son accent (américain, britannique, australien, canadien),
 * qui change d'un document à l'autre ; faute de voix pour un accent, la voix anglaise habituelle le remplace.
 */
export function speakScript(script: string, onEnd?: () => void) {
  if (!script) return false;
  const lines = script.split('\n').map((l) => (l[1] === '|' ? { who: l[0], text: l.slice(2) } : { who: 'N', text: l }));
  const accents = voiceLangOf(scriptText(script)) === 'en' ? scriptAccents(script) : null;
  return say(lines.map((l) => ({ text: l.text, rate: 0.9, pitch: l.who === 'M' ? 0.7 : l.who === 'F' ? 1.4 : 1, locale: accents?.[l.who] })), onEnd);
}

/** Texte lisible d'un document d'écoute (sans les marques de rôle). */
export const scriptText = (script: string) => script.split('\n').map((l) => (l[1] === '|' ? l.slice(2) : l)).join('\n');
