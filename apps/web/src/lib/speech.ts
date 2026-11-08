/** Synthèse vocale japonaise via le navigateur (gratuite, sans fichier audio à licencier). */
export const speechSupported = () => typeof window !== 'undefined' && 'speechSynthesis' in window;

let voice: SpeechSynthesisVoice | null = null;
function pickVoice() {
  if (!speechSupported()) return null;
  voice ??= speechSynthesis.getVoices().find((v) => v.lang.toLowerCase().startsWith('ja')) ?? null;
  return voice;
}
if (speechSupported()) speechSynthesis.onvoiceschanged = () => { voice = null; pickVoice(); };

export function speak(text: string, slow = false) {
  if (!speechSupported() || !text) return false;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP';
  u.rate = slow ? 0.55 : 0.9;
  const v = pickVoice();
  if (v) u.voice = v;
  speechSynthesis.speak(u);
  return true;
}

export const hasJapaneseVoice = () => !!pickVoice();

/**
 * Document d'écoute d'examen : lignes « N|… » (narrateur), « M|… » (homme), « F|… » (femme).
 * Une seule voix japonaise est souvent disponible : on distingue les rôles par la hauteur de voix.
 */
export function speakScript(script: string, onEnd?: () => void) {
  if (!speechSupported() || !script) return false;
  speechSynthesis.cancel();
  const lines = script.split('\n').map((l) => (l[1] === '|' ? { who: l[0], text: l.slice(2) } : { who: 'N', text: l })).filter((l) => l.text.trim());
  const v = pickVoice();
  lines.forEach((l, i) => {
    const u = new SpeechSynthesisUtterance(l.text);
    u.lang = 'ja-JP';
    u.rate = 0.9;
    u.pitch = l.who === 'M' ? 0.7 : l.who === 'F' ? 1.4 : 1;
    if (v) u.voice = v;
    if (i === lines.length - 1 && onEnd) u.onend = () => onEnd();
    speechSynthesis.speak(u);
  });
  return true;
}

/** Texte lisible d'un document d'écoute (sans les marques de rôle). */
export const scriptText = (script: string) => script.split('\n').map((l) => (l[1] === '|' ? l.slice(2) : l)).join('\n');
