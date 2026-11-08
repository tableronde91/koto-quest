import { motion } from 'motion/react';
import type { AchievementDto } from '@koto/shared';
import { useAchievements } from '../api/hooks';
import { Medal, RARITY_LABEL } from '../components/Achievements';
import { ErrorBox, PageTitle, ProgressBar, Spinner } from '../components/ui';
import { T, DATE_LOCALE } from '../i18n';

const CATEGORIES: { id: AchievementDto['category']; title: string }[] = [
  { id: 'study', title: T("Étude") },
  { id: 'streak', title: T("Régularité") },
  { id: 'mastery', title: T("Maîtrise") },
  { id: 'adventure', title: T("Aventure") },
  { id: 'play', title: T("Jeux et collection") },
];

export function AchievementsPage() {
  const { data, isLoading, error, refetch } = useAchievements();
  if (isLoading) return <Spinner />;
  if (error || !data) return <ErrorBox error={error} onRetry={refetch} />;
  return (
    <div className="flex flex-col gap-8">
      <PageTitle sub={T("Chaque succès rapporte des pièces et de l’expérience, une seule fois.")}>{T("Succès")}</PageTitle>
      <div className="max-w-md">
        <ProgressBar value={data.unlocked} max={data.total} label={T("Succès débloqués")} tone="gold" />
        <p className="mt-1 text-sm text-ink-soft">{T("{0} sur {1} débloqués", [data.unlocked , data.total ])}</p>
      </div>
      {CATEGORIES.map((cat) => {
        const list = data.achievements.filter((a) => a.category === cat.id);
        return (
          <section key={cat.id} aria-labelledby={`cat-${cat.id}`}>
            <h2 id={`cat-${cat.id}`} className="text-xl">{cat.title} <span className="text-base font-normal text-ink-soft">{list.filter((a) => a.unlocked).length}/{list.length}</span></h2>
            <ul className="mt-3 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {list.map((a, i) => (
                <motion.li
                  key={a.slug}
                  data-testid="achievement"
                  data-unlocked={a.unlocked ? '1' : '0'}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: i * 0.04 }}
                  className={`flex items-center gap-3 rounded-2xl border p-3 ${a.unlocked ? 'border-line bg-surface' : 'border-dashed border-line'}`}
                >
                  <Medal a={a} size={60} />
                  <div className="min-w-0">
                    <p className={`font-bold ${a.unlocked ? '' : 'text-ink-soft'}`}>{a.title}</p>
                    <p className="text-sm text-ink-soft">{a.description}</p>
                    <p className="mt-0.5 text-xs text-ink-soft">
                      {RARITY_LABEL[a.rarity]} · {a.unlocked
                        ? `obtenu${a.unlockedAt ? T(" le {0}", [new Date(a.unlockedAt).toLocaleDateString(DATE_LOCALE, { day: 'numeric', month: 'short' })]) : ''}`
                        : T("{0}/{1} · +{2} pièces", [a.value, a.target, a.coins])}
                    </p>
                  </div>
                </motion.li>
              ))}
            </ul>
          </section>
        );
      })}
    </div>
  );
}
