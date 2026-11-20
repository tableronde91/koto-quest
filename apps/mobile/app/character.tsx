import { ReactNode, useEffect, useState } from 'react';
import { Pressable, Text, View } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { AVATAR_OPTIONS } from '@koto/learning-engine';
import type { AvatarConfig, CosmeticSlot, ShopDto, ShopItemDto } from '@koto/shared';
import { api, post, put } from '../src/api';
import { Avatar, EYES_LABELS, HAIR_COLORS, HAIR_COLOR_LABELS, HAIR_LABELS, SKIN_TONES } from '../src/Avatar';
import { C } from '../src/theme';
import { Button, ErrorBox, H1, H2, Loading, P, Screen } from '../src/ui';
import { T } from '../src/i18n';

/** Personnage : apparence (gratuite), garde-robe et boutique de cosmétiques (pièces ou trophées). */
export default function Character() {
  const router = useRouter();
  const params = useLocalSearchParams<{ t?: string }>();
  const qc = useQueryClient();
  const { data: shop, isLoading, error, refetch } = useQuery({ queryKey: ['shop'], queryFn: () => api<ShopDto>('/shop') });
  const [tab, setTab] = useState<'look' | 'shop'>(params.t === 'boutique' ? 'shop' : 'look');
  const [draft, setDraft] = useState<AvatarConfig | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  useEffect(() => {
    if (shop && !draft) setDraft(shop.avatar);
  }, [shop, draft]);

  const save = useMutation({
    mutationFn: (avatar: AvatarConfig) => put<AvatarConfig>('/me/avatar', { avatar }),
    onSuccess: (avatar) => {
      setDraft(avatar);
      void qc.invalidateQueries();
      setMessage(T('Apparence enregistrée.'));
    },
  });
  const acquire = useMutation({
    mutationFn: (sku: string) => post<ShopDto>('/shop/acquire', { sku }),
    onSuccess: (data, sku) => {
      qc.setQueryData(['shop'], data);
      void qc.invalidateQueries({ queryKey: ['me'] });
      void qc.invalidateQueries({ queryKey: ['dashboard'] });
      const item = data.items.find((i) => i.sku === sku)!;
      setMessage(item.price > 0 ? T('{0} acheté.', [item.name]) : T('{0} ajouté à ta garde-robe.', [item.name]));
    },
  });

  if (isLoading || (shop && !draft)) return <Loading />;
  if (error || !shop || !draft) return <Screen><ErrorBox error={error} onRetry={refetch} /></Screen>;

  const dirty = JSON.stringify(draft) !== JSON.stringify(shop.avatar);
  const equip = (slot: CosmeticSlot, sku: string | null) => {
    const next = { ...draft, [slot]: sku };
    setDraft(next);
    save.mutate(next);
  };

  return (
    <Screen>
      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
        <Pressable accessibilityRole="button" accessibilityLabel={T('Retour')} onPress={() => (router.canGoBack() ? router.back() : router.replace('/profile'))} hitSlop={12}>
          <Text style={{ fontSize: 26, color: C.ink, fontWeight: '800' }}>‹</Text>
        </Pressable>
        <H1 style={{ flex: 1 }}>{T('Mon personnage')}</H1>
        <View style={{ backgroundColor: C.surface, borderRadius: 99, paddingHorizontal: 12, paddingVertical: 6, borderWidth: 1, borderColor: C.line }}>
          <Text testID="coins" style={{ fontWeight: '800', color: C.goldInk }}>🪙 {shop.coins}</Text>
        </View>
      </View>

      <View style={{ alignItems: 'center', gap: 10 }}>
        <View style={{ borderRadius: 32, borderWidth: 1, borderColor: C.line, backgroundColor: C.surface, padding: 6 }}>
          <Avatar config={draft} size={190} title={T('Aperçu de ton personnage')} />
        </View>
        {dirty && (
          <View style={{ flexDirection: 'row', gap: 10 }}>
            <Button tone="gold" label={T('Enregistrer')} disabled={save.isPending} onPress={() => save.mutate(draft)} />
            <Button tone="quiet" label={T('Annuler')} onPress={() => setDraft(shop.avatar)} />
          </View>
        )}
        {message && !dirty && <P soft style={{ fontSize: 14 }}>{message}</P>}
        {(save.error || acquire.error) && <ErrorBox error={save.error ?? acquire.error} />}
      </View>

      <View accessibilityRole="tablist" style={{ flexDirection: 'row', backgroundColor: C.surface2, borderRadius: 16, padding: 4 }}>
        {(['look', 'shop'] as const).map((t) => (
          <Pressable key={t} accessibilityRole="tab" accessibilityState={{ selected: tab === t }} onPress={() => setTab(t)} style={{ flex: 1, alignItems: 'center', paddingVertical: 10, borderRadius: 12, backgroundColor: tab === t ? C.surface : 'transparent' }}>
            <Text style={{ fontWeight: '800', color: tab === t ? C.ink : C.inkSoft }}>{t === 'look' ? T('Apparence') : T('Boutique')}</Text>
          </Pressable>
        ))}
      </View>

      {tab === 'look' ? (
        <Look draft={draft} setDraft={setDraft} shop={shop} onEquip={equip} />
      ) : (
        <Shop shop={shop} draft={draft} busy={acquire.isPending} onAcquire={(sku) => acquire.mutate(sku)} onEquip={equip} />
      )}
    </Screen>
  );
}

function Group({ label, children }: { label: string; children: ReactNode }) {
  return (
    <View style={{ gap: 8 }}>
      <Text style={{ fontWeight: '800', color: C.ink }}>{label}</Text>
      <View accessibilityLabel={label} style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>{children}</View>
    </View>
  );
}

function Swatch({ color, label, selected, onPress }: { color: string; label: string; selected: boolean; onPress: () => void }) {
  return (
    <Pressable accessibilityRole="radio" accessibilityState={{ checked: selected }} accessibilityLabel={label} onPress={onPress} style={{ width: 46, height: 46, borderRadius: 23, backgroundColor: color, borderWidth: 4, borderColor: selected ? C.ink : C.surface }} />
  );
}

function Chip({ label, selected, onPress }: { label: string; selected: boolean; onPress: () => void }) {
  return (
    <Pressable accessibilityRole="radio" accessibilityState={{ checked: selected }} accessibilityLabel={label} onPress={onPress} style={{ paddingHorizontal: 14, paddingVertical: 9, borderRadius: 99, borderWidth: 2, borderColor: selected ? C.ink : C.line, backgroundColor: selected ? C.ink : C.surface }}>
      <Text style={{ fontWeight: '800', color: selected ? C.paper : C.ink }}>{label}</Text>
    </Pressable>
  );
}

function Look({ draft, setDraft, shop, onEquip }: { draft: AvatarConfig; setDraft: (a: AvatarConfig) => void; shop: ShopDto; onEquip: (slot: CosmeticSlot, sku: string | null) => void }) {
  const set = (patch: Partial<AvatarConfig>) => setDraft({ ...draft, ...patch });
  const free = (slot: CosmeticSlot) => slot !== 'outfit' && slot !== 'background';
  return (
    <View style={{ gap: 18 }}>
      <Group label={T('Teint')}>
        {SKIN_TONES.slice(0, AVATAR_OPTIONS.skin).map((c, i) => <Swatch key={c} color={c} label={T('Teint {0}', [i + 1])} selected={draft.skin === i} onPress={() => set({ skin: i })} />)}
      </Group>
      <Group label={T('Coiffure')}>
        {AVATAR_OPTIONS.hair.map((h) => <Chip key={h} label={T(HAIR_LABELS[h])} selected={draft.hair === h} onPress={() => set({ hair: h })} />)}
      </Group>
      <Group label={T('Couleur des cheveux')}>
        {HAIR_COLORS.slice(0, AVATAR_OPTIONS.hairColor).map((c, i) => <Swatch key={c} color={c} label={T(HAIR_COLOR_LABELS[i])} selected={draft.hairColor === i} onPress={() => set({ hairColor: i })} />)}
      </Group>
      <Group label={T('Yeux')}>
        {AVATAR_OPTIONS.eyes.map((e) => <Chip key={e} label={T(EYES_LABELS[e])} selected={draft.eyes === e} onPress={() => set({ eyes: e })} />)}
      </Group>
      <View style={{ gap: 4 }}>
        <H2>{T('Ma garde-robe')}</H2>
        <P soft style={{ fontSize: 14 }}>{T('Les objets que tu possèdes. Touche un objet pour l’équiper ou le retirer.')}</P>
      </View>
      {shop.slots.map(({ slot, label }) => {
        const owned = shop.items.filter((i) => i.slot === slot && i.owned);
        return (
          <Group key={slot} label={label}>
            {free(slot) && <Chip label={T('Aucun')} selected={!draft[slot]} onPress={() => onEquip(slot, null)} />}
            {owned.map((i) => <Chip key={i.sku} label={i.name} selected={draft[slot] === i.sku} onPress={() => onEquip(slot, draft[slot] === i.sku && free(slot) ? null : i.sku)} />)}
          </Group>
        );
      })}
    </View>
  );
}

function Shop({ shop, draft, busy, onAcquire, onEquip }: { shop: ShopDto; draft: AvatarConfig; busy: boolean; onAcquire: (sku: string) => void; onEquip: (slot: CosmeticSlot, sku: string) => void }) {
  const [slot, setSlot] = useState<CosmeticSlot>('hat');
  return (
    <View style={{ gap: 14 }}>
      <View accessibilityLabel={T('Catégorie')} style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 8 }}>
        {shop.slots.map((s) => <Chip key={s.slot} label={s.label} selected={slot === s.slot} onPress={() => setSlot(s.slot)} />)}
      </View>
      <View style={{ flexDirection: 'row', flexWrap: 'wrap', marginHorizontal: -5 }}>
        {shop.items.filter((i) => i.slot === slot).map((i) => (
          <View key={i.sku} style={{ width: '50%', padding: 5 }}>
            <ShopCard item={i} draft={draft} coins={shop.coins} busy={busy} onAcquire={() => onAcquire(i.sku)} onEquip={() => onEquip(i.slot, i.sku)} />
          </View>
        ))}
      </View>
    </View>
  );
}

function ShopCard({ item, draft, coins, busy, onAcquire, onEquip }: { item: ShopItemDto; draft: AvatarConfig; coins: number; busy: boolean; onAcquire: () => void; onEquip: () => void }) {
  const preview = { ...draft, [item.slot]: item.sku };
  let action: ReactNode;
  if (item.equipped) action = <Text style={{ fontWeight: '800', color: C.ok, textAlign: 'center' }}>{T('Équipé')}</Text>;
  else if (item.owned) action = <Button tone="quiet" label={T('Équiper')} onPress={onEquip} />;
  else if (item.lockedBy) action = <Text style={{ fontSize: 13, color: C.inkSoft, textAlign: 'center' }}>{T('Bats {0}', [item.lockedBy])}</Text>;
  else if (item.unlockBoss) action = <Button tone="gold" label={T('Récupérer')} disabled={busy} onPress={onAcquire} />;
  else action = <Button tone="gold" label={`🪙 ${item.price}`} disabled={busy || coins < item.price} onPress={onAcquire} testID="buy" />;
  return (
    <View testID="shop-item" accessibilityLabel={item.name} style={{ flex: 1, gap: 6, borderWidth: 2, borderColor: item.equipped ? C.ok : C.line, borderRadius: 18, backgroundColor: C.surface, padding: 10 }}>
      <View style={{ alignItems: 'center', opacity: item.lockedBy ? 0.45 : 1 }}>
        <Avatar config={preview} size={104} title={T('Aperçu : {0}', [item.name])} />
      </View>
      <Text style={{ fontWeight: '800', color: C.ink }}>{item.name}</Text>
      <Text style={{ flex: 1, fontSize: 12, color: C.inkSoft }}>{item.description}</Text>
      {action}
    </View>
  );
}
