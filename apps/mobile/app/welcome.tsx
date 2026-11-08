import { useState } from 'react';
import { KeyboardAvoidingView, Platform, Pressable, Text, TextInput, View } from 'react-native';
import { useAuth } from '../src/auth';
import { API_URL } from '../src/config';
import { C } from '../src/theme';
import { Button, Card, H1, P, Screen } from '../src/ui';

export default function Welcome() {
  const { login, register } = useAuth();
  const [mode, setMode] = useState<'register' | 'login'>('login');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit() {
    setBusy(true);
    setError(null);
    try {
      if (mode === 'register') await register(name.trim(), email.trim(), password);
      else await login(email.trim(), password);
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Erreur');
    } finally {
      setBusy(false);
    }
  }

  const field = { borderWidth: 2, borderColor: C.line, borderRadius: 14, padding: 14, fontSize: 16, backgroundColor: C.surface, color: C.ink } as const;
  return (
    <KeyboardAvoidingView style={{ flex: 1 }} behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
      <Screen>
        <View style={{ alignItems: 'center', gap: 6, marginTop: 24 }}>
          <Text style={{ fontSize: 88, fontWeight: '900', color: C.ink }}>言<Text style={{ color: C.ko }}>。</Text></Text>
          <H1>Koto Quest</H1>
          <P soft style={{ textAlign: 'center' }}>Un mot le matin, un défi l’après-midi. Le japonais du N5 au N1, au rythme de ta mémoire.</P>
        </View>
        <Card style={{ gap: 12 }}>
          <View style={{ flexDirection: 'row', backgroundColor: C.surface2, borderRadius: 12, padding: 4 }}>
            {(['login', 'register'] as const).map((m) => (
              <Pressable key={m} accessibilityRole="tab" accessibilityState={{ selected: mode === m }} onPress={() => setMode(m)} style={{ flex: 1, padding: 10, borderRadius: 10, backgroundColor: mode === m ? C.surface : 'transparent', alignItems: 'center' }}>
                <Text style={{ fontWeight: '800', color: mode === m ? C.ink : C.inkSoft }}>{m === 'login' ? 'Se connecter' : 'Créer un compte'}</Text>
              </Pressable>
            ))}
          </View>
          {mode === 'register' && <TextInput placeholder="Pseudo" accessibilityLabel="Pseudo" value={name} onChangeText={setName} style={field} />}
          <TextInput placeholder="Adresse e-mail" accessibilityLabel="Adresse e-mail" autoCapitalize="none" keyboardType="email-address" autoComplete="email" value={email} onChangeText={setEmail} style={field} />
          <TextInput placeholder="Mot de passe (8 caractères minimum)" accessibilityLabel="Mot de passe" secureTextEntry value={password} onChangeText={setPassword} style={field} />
          {error && <Text style={{ color: C.ko, fontWeight: '700' }}>{error}</Text>}
          <Button label={busy ? '…' : mode === 'login' ? 'Se connecter' : 'Créer mon compte'} disabled={busy || !email || password.length < 8 || (mode === 'register' && !name.trim())} onPress={submit} />
        </Card>
        <P soft style={{ textAlign: 'center', fontSize: 12 }}>Serveur : {API_URL}</P>
      </Screen>
    </KeyboardAvoidingView>
  );
}
