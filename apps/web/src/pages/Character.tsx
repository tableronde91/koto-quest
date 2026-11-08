import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { AVATAR_OPTIONS } from '@koto/learning-engine';
import type { AvatarConfig, CosmeticSlot, ShopDto, ShopItemDto } from '@koto/shared';
import { api, post, put } from '../api/client';
import { qk } from '../api/hooks';
import { Avatar, EYES_LABELS, HAIR_COLORS, HAIR_COLOR_LABELS, HAIR_LABELS, SKIN_TONES } from '../components/Avatar';
import { ErrorBox, PageTitle, Spinner } from '../components/ui';
import { T } from '../i18n';

const useShop = () => useQuery({ queryKey: ['shop'], queryFn: () => api<ShopDto>('/shop') });

export function Coins({ value, className = '' }: { value: number; className?: string }) {
  return (
    <span className={`inline-flex items-center gap-1.5 font-bold tabular-nums ${className}`} aria-label={T("{0} pièces", [value])}>
      <svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="10" fill="var(--gold)" />
        <rect x="9.5" y="9.5" width="5" height="5" fill="var(--surface)" />
      </svg>
      {value}
    </span>
  );
}

/** Personnage : apparence (gratuite) et boutique de cosmétiques (pièces ou trophées). */
export function CharacterPage() {
  const { data: shop, isLoading, error, refetch } = useShop();
  const [params, setParams] = useSearchParams();
  const tab = params.get('t') === 'boutique' ? 'shop' : 'look';
  const [draft, setDraft] = useState<AvatarConfig | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const qc = useQueryClient();

  useEffect(() => {
    if (shop && !draft) setDraft(shop.avatar);
  }, [shop, draft]);

  const save = useMutation({
    mutationFn: (avatar: AvatarConfig) => put<AvatarConfig>('/me/avatar', { avatar }),
    onSuccess: (avatar) => {
      setDraft(avatar);
      qc.invalidateQueries();
      setMessage(T("Apparence enregistrée."));
    },
  });
  const acquire = useMutation({
    mutationFn: (sku: string) => post<ShopDto>('/shop/acquire', { sku }),
    onSuccess: (data, sku) => {
      qc.setQueryData(['shop'], data);
      qc.invalidateQueries({ queryKey: qk.me });
      qc.invalidateQueries({ queryKey: qk.dashboard });
      const item = data.items.find((i) => i.sku === sku)!;
      setMessage(item.price > 0 ? T("{0} acheté.", [item.name]) : T("{0} ajouté à ta garde-robe.", [item.name]));
    },
  });

  if (isLoading || (shop && !draft)) return <Spinner />;
  if (error || !shop || !draft) return <ErrorBox error={error} onRetry={refetch} />;

  const dirty = JSON.stringify(draft) !== JSON.stringify(shop.avatar);
  const equip = (slot: CosmeticSlot, sku: string | null) => {
    const next = { ...draft, [slot]: sku };
    setDraft(next);
    save.mutate(next);
  };

  return (
    <div>
      <PageTitle sub={T("Ton personnage t’accompagne dans l’aventure. Les objets s’achètent avec les pièces gagnées en étudiant, ou se gagnent en battant les gardiens.")}>{T("Mon personnage")}</PageTitle>
      <div className="grid gap-8 md:grid-cols-[minmax(220px,280px)_1fr]">
        <aside className="flex flex-col items-center gap-3 md:sticky md:top-6 md:self-start">
          <div className="rounded-[2rem] border border-line bg-surface p-2">
            <Avatar config={draft} size={240} title={T("Aperçu de ton personnage")} />
          </div>
          <Coins value={shop.coins} className="text-xl text-gold-ink" />
          {dirty && (
            <div className="flex gap-2">
              <button className="btn btn-gold" onClick={() => save.mutate(draft)} disabled={save.isPending}>{T("Enregistrer")}</button>
              <button className="btn btn-quiet" onClick={() => setDraft(shop.avatar)}>{T("Annuler")}</button>
            </div>
          )}
          {message && !dirty && <p role="status" className="text-sm text-ink-soft">{message}</p>}
          {(save.error || acquire.error) && <ErrorBox error={save.error ?? acquire.error} />}
        </aside>

        <section>
          <div role="tablist" aria-label={T("Personnage")} className="mb-6 grid grid-cols-2 rounded-2xl bg-surface-2 p-1">
            {(['look', 'shop'] as const).map((t) => (
              <button
                key={t}
                role="tab"
                aria-selected={tab === t}
                onClick={() => setParams(t === 'shop' ? { t: 'boutique' } : {}, { replace: true })}
                className={`min-h-12 rounded-xl font-bold ${tab === t ? 'bg-surface shadow-sm' : 'text-ink-soft'}`}
              >
                {t === 'look' ? T("Apparence") : T("Boutique")}
              </button>
            ))}
          </div>
          {tab === 'look' ? (
            <Look draft={draft} setDraft={setDraft} shop={shop} onEquip={equip} />
          ) : (
            <Shop shop={shop} draft={draft} onAcquire={(sku) => acquire.mutate(sku)} onEquip={equip} busy={acquire.isPending} />
          )}
        </section>
      </div>
    </div>
  );
}

function OptionGroup({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <fieldset className="mb-6">
      <legend className="mb-2 font-bold">{label}</legend>
      <div className="flex flex-wrap gap-2">{children}</div>
    </fieldset>
  );
}

function Swatch({ color, label, selected, onClick }: { color: string; label: string; selected: boolean; onClick: () => void }) {
  return (
    <button type="button" aria-pressed={selected} aria-label={label} title={label} onClick={onClick} className="h-12 w-12 rounded-full border-4" style={{ background: color, borderColor: selected ? 'var(--ink)' : 'var(--surface)', boxShadow: '0 0 0 1px var(--line)' }} />
  );
}

function Chip({ label, selected, onClick }: { label: string; selected: boolean; onClick: () => void }) {
  return (
    <button type="button" aria-pressed={selected} onClick={onClick} className={`btn min-h-11 ${selected ? 'btn-primary' : 'btn-quiet'}`}>
      {label}
    </button>
  );
}

function Look({ draft, setDraft, shop, onEquip }: { draft: AvatarConfig; setDraft: (a: AvatarConfig) => void; shop: ShopDto; onEquip: (slot: CosmeticSlot, sku: string | null) => void }) {
  const set = (patch: Partial<AvatarConfig>) => setDraft({ ...draft, ...patch });
  return (
    <div>
      <OptionGroup label={T("Teint")}>
        {SKIN_TONES.slice(0, AVATAR_OPTIONS.skin).map((c, i) => <Swatch key={c} color={c} label={T("Teint {0}", [i + 1])} selected={draft.skin === i} onClick={() => set({ skin: i })} />)}
      </OptionGroup>
      <OptionGroup label={T("Coiffure")}>
        {AVATAR_OPTIONS.hair.map((h) => <Chip key={h} label={HAIR_LABELS[h]} selected={draft.hair === h} onClick={() => set({ hair: h })} />)}
      </OptionGroup>
      <OptionGroup label={T("Couleur des cheveux")}>
        {HAIR_COLORS.slice(0, AVATAR_OPTIONS.hairColor).map((c, i) => <Swatch key={c} color={c} label={HAIR_COLOR_LABELS[i]} selected={draft.hairColor === i} onClick={() => set({ hairColor: i })} />)}
      </OptionGroup>
      <OptionGroup label={T("Yeux")}>
        {AVATAR_OPTIONS.eyes.map((e) => <Chip key={e} label={EYES_LABELS[e]} selected={draft.eyes === e} onClick={() => set({ eyes: e })} />)}
      </OptionGroup>
      <h2 className="mb-1 mt-2 text-xl">{T("Ma garde-robe")}</h2>
      <p className="mb-4 text-sm text-ink-soft">{T("Les objets que tu possèdes. Touche un objet pour l’équiper ou le retirer.")}</p>
      {shop.slots.map(({ slot, label }) => {
        const owned = shop.items.filter((i) => i.slot === slot && i.owned);
        return (
          <OptionGroup key={slot} label={label}>
            {slot !== 'outfit' && slot !== 'background' && <Chip label={T("Aucun")} selected={!draft[slot]} onClick={() => onEquip(slot, null)} />}
            {owned.map((i) => <Chip key={i.sku} label={i.name} selected={draft[slot] === i.sku} onClick={() => onEquip(slot, draft[slot] === i.sku && slot !== 'outfit' && slot !== 'background' ? null : i.sku)} />)}
          </OptionGroup>
        );
      })}
    </div>
  );
}

function Shop({ shop, draft, onAcquire, onEquip, busy }: { shop: ShopDto; draft: AvatarConfig; onAcquire: (sku: string) => void; onEquip: (slot: CosmeticSlot, sku: string | null) => void; busy: boolean }) {
  const [slot, setSlot] = useState<CosmeticSlot>('hat');
  const items = shop.items.filter((i) => i.slot === slot);
  return (
    <div>
      <div className="mb-4 flex flex-wrap gap-2" role="group" aria-label={T("Catégorie")}>
        {shop.slots.map((s) => <Chip key={s.slot} label={s.label} selected={slot === s.slot} onClick={() => setSlot(s.slot)} />)}
      </div>
      <ul className="grid grid-cols-2 gap-3 lg:grid-cols-3">
        {items.map((i) => (
          <li key={i.sku}>
            <ShopCard item={i} draft={draft} coins={shop.coins} busy={busy} onAcquire={() => onAcquire(i.sku)} onEquip={() => onEquip(i.slot, i.sku)} />
          </li>
        ))}
      </ul>
    </div>
  );
}

function ShopCard({ item, draft, coins, busy, onAcquire, onEquip }: { item: ShopItemDto; draft: AvatarConfig; coins: number; busy: boolean; onAcquire: () => void; onEquip: () => void }) {
  const preview = { ...draft, [item.slot]: item.sku };
  const trophy = !!item.unlockBoss;
  let action: React.ReactNode;
  if (item.equipped) action = <span className="text-sm font-bold text-ok">{T("Équipé")}</span>;
  else if (item.owned) action = <button className="btn btn-quiet min-h-10 w-full" onClick={onEquip}>{T("Équiper")}</button>;
  else if (item.lockedBy) action = <span className="text-sm text-ink-soft">{T("Bats {0}", [ item.lockedBy])}</span>;
  else if (trophy) action = <button className="btn btn-gold min-h-10 w-full" disabled={busy} onClick={onAcquire}>{T("Récupérer")}</button>;
  else
    action = (
      <button className="btn btn-gold min-h-10 w-full" disabled={busy || coins < item.price} onClick={onAcquire} aria-label={T("Acheter {0} pour {1} pièces", [item.name, item.price])}>
        <Coins value={item.price} />
      </button>
    );
  return (
    <div className={`flex h-full flex-col gap-2 rounded-2xl border-2 bg-surface p-3 ${item.equipped ? 'border-ok' : 'border-line'}`}>
      <div className={`mx-auto ${item.lockedBy ? 'opacity-50 grayscale' : ''}`}>
        <Avatar config={preview} size={110} title={T("Aperçu : {0}", [item.name])} />
      </div>
      <p className="font-bold leading-tight">{item.name}</p>
      <p className="flex-1 text-sm text-ink-soft">{item.description}</p>
      <div className="flex min-h-10 items-center justify-center">{action}</div>
    </div>
  );
}
