import { Text, View } from 'react-native';
import { rubySegments } from '@koto/learning-engine';
import { C } from './theme';

/**
 * Japonais avec furigana ({漢字|かな}) : React Native n'a pas de <ruby>, on place la lecture
 * au-dessus de chaque groupe de kanji. Sans furigana, le texte reste d'un seul tenant.
 */
export function Ruby({ text, furigana, size = 22, color = C.ink }: { text: string; furigana: boolean; size?: number; color?: string }) {
  const segs = rubySegments(text);
  if (!furigana) return <Text style={{ fontSize: size, color, lineHeight: size * 1.5 }}>{segs.map((s) => s.text).join('')}</Text>;
  // Les morceaux sans furigana sont découpés en caractères pour que la ligne puisse se replier n'importe où.
  const pieces: { text: string; ruby?: string }[] = [];
  for (const sg of segs) {
    if (sg.ruby) pieces.push(sg);
    else
      for (const ch of sg.text) {
        // La ponctuation reste collée au caractère qui la précède (jamais seule en début de ligne).
        const last = pieces[pieces.length - 1];
        if (last && !last.ruby && /[、。，．！？」』）]/.test(ch)) last.text += ch;
        else pieces.push({ text: ch });
      }
  }
  return (
    <View style={{ flexDirection: 'row', flexWrap: 'wrap', alignItems: 'flex-end' }}>
      {pieces.map((p, i) => (
        <View key={i} style={{ alignItems: 'center' }}>
          <Text style={{ fontSize: size * 0.45, color: C.inkSoft, lineHeight: size * 0.6 }}>{p.ruby ?? ' '}</Text>
          <Text style={{ fontSize: size, color, lineHeight: size * 1.3 }}>{p.text}</Text>
        </View>
      ))}
    </View>
  );
}
