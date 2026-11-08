# Koto Quest — Architecture

> Document de référence du lead dev. Il décrit l'architecture cible (phases 1 à 5) et ce
> qui est effectivement livré en phase 1 (MVP web).

## 1. Vue d'ensemble

```
koto-quest/
├── apps/
│   ├── api/                 NestJS + Prisma + PostgreSQL (REST, OpenAPI sur /api/docs)
│   ├── web/                 React + Vite + Tailwind + TanStack Query + Motion (PWA)
│   └── mobile/              Expo / React Native (expo-router), réutilise shared + learning-engine
├── packages/
│   ├── shared/              Types et contrats d'API partagés web/api/mobile
│   └── learning-engine/     Moteur pédagogique PUR (aucune dépendance UI / BDD)
├── content/
│   └── n5/                  Contenu pédagogique versionné (JSON) importé par le seed
├── e2e/                     Tests Playwright des parcours essentiels
├── docs/
└── docker-compose.yml       PostgreSQL (+ Redis réservé aux phases suivantes)
```

Principe directeur : **toute règle pédagogique vit dans `learning-engine`**
(planification FSRS, états de maîtrise, génération d'exercices, plan de session,
fenêtres de rappel, séries, quêtes, estimation de préparation). L'API l'orchestre
et persiste ; le web et le futur mobile ne font qu'afficher. Le moteur est donc
réutilisable tel quel par Expo (phase 4) et testable unitairement.

```
 ┌──────────── Web (PWA) ─────────────┐         ┌───────────── API NestJS ──────────────┐
 │ React pages ─ TanStack Query ──────┼─ /api ─▶│ Controllers ─▶ Services ─▶ Prisma ─▶ PG │
 │ Service Worker (push, cache shell) │◀─ push ─│ ReminderScheduler (cron 1 min)        │
 │ Popup quiz in-app (poll inbox)     │         │        │ uses                          │
 └────────────────────────────────────┘         │  @koto/learning-engine                │
                                                └───────────────────────────────────────┘
```

## 2. Choix structurants

| Sujet | Choix | Pourquoi |
|---|---|---|
| Validation des réponses | Le serveur **émet** chaque question (`IssuedQuestion`) et garde la bonne réponse | Le client ne reçoit jamais la réponse ; XP, progression et récompenses sont calculés côté serveur |
| Répétition espacée | FSRS‑4.5 (paramètres par défaut publiés) + étapes d'apprentissage courtes | Intervalles individuels pilotés par la difficulté/stabilité de chaque carte |
| Sessions | Cookie `httpOnly` + `SameSite=Lax`, jeton aléatoire stocké **haché** en base | Révocable (déconnexion, suppression de compte), pas de JWT en localStorage |
| Rappels | Table `Notification` = boîte de réception ; Web Push en plus si consentement + abonnement | Fonctionne même si le navigateur refuse les notifications (popup in-app) |
| Planification | Cron NestJS en process (phase 1). BullMQ/Redis prévu quand plusieurs instances API | Moins de pièces mobiles pour le MVP |
| Contenu | JSON versionné dans `content/`, importé par un seed idempotent (upsert par `slug`) | Corrigeable par PR, versionné par git + champ `contentVersion` |
| Audio | Web Speech API `ja-JP` côté client (gratuit, sans licence de fichiers) | Ralentir/répéter via `rate` |

## 3. Écrans et parcours (phase 1)

1. **Accueil public** → Inscription / Connexion / Mot de passe oublié.
2. **Onboarding** (6 questions du cahier des charges) → génère le profil d'étude.
3. **Tableau de bord** : niveau visé, progression globale, XP, série, temps du jour,
   mots/kanji maîtrisés, révisions en attente, leçon recommandée, quêtes du jour,
   estimation prudente de préparation.
4. **Parcours N5** : mondes → chapitres → leçons (verrouillage progressif).
5. **Leçon** : objectif → explication + exemples (furigana commutables, audio) →
   exercices → mini‑révision → bilan (XP).
6. **Révisions** : file des cartes dues, ordonnée par urgence.
7. **Mini‑quiz** (`/quiz/:id`) : ouvert depuis une notification push ou une popup in‑app.
8. **Statistiques** : activité, taux de réussite, maîtrise, temps d'étude.
9. **Réglages** : rappels (mode, créneaux, silence, pause, consentement),
   thème, furigana, export / suppression des données.

## 4. Modèle de données (résumé)

Voir `apps/api/prisma/schema.prisma` (source de vérité).

- **Comptes** : `User`, `Session`, `PasswordResetToken`, `UserPreferences`, `NotificationPreferences`, `PushSubscription`.
- **Contenu** : `JlptLevel` → `World` → `Chapter` → `Lesson` ; `LearningItem`
  (type `kana | vocabulary | kanji | grammar`) avec détails `Vocabulary`, `Kanji`,
  `GrammarPoint` ; `Example` ; `Exercise` (exercices rédigés : particule, phrase
  à trous, remise en ordre, vrai/faux, dialogue) ; `LessonItem` (items introduits par une leçon).
- **Apprentissage** : `ReviewCard` (état FSRS par utilisateur × item),
  `ReviewHistory` (journal immuable), `UserLessonProgress`, `LearningSession`,
  `IssuedQuestion`, `ExerciseAnswer`.
- **Engagement** : `Notification`, `DailyActivity` (agrégat pour série/stats), `XpEvent`.
- **Phases suivantes (déjà modélisées a minima)** : `Quest`, `Achievement`,
  `UserAchievement`, `InventoryItem`, `Exam`, `ExamAttempt`.

## 5. API essentielle (préfixe `/api`, doc OpenAPI `/api/docs`)

| Méthode | Route | Rôle |
|---|---|---|
| POST | `/auth/register`, `/auth/login`, `/auth/logout` | Comptes (limités en débit) |
| POST | `/auth/forgot-password`, `/auth/reset-password` | Réinitialisation |
| GET | `/me` | Profil + préférences |
| PUT | `/me/onboarding`, `/me/preferences` | Objectifs, temps/jour, difficultés |
| GET | `/me/export` · DELETE `/me` | RGPD |
| GET | `/path/:level` | Mondes/chapitres/leçons + état de déblocage |
| GET | `/lessons/:slug` | Contenu de la leçon |
| POST | `/lessons/:slug/start` | Démarre une session, émet les exercices |
| POST | `/lessons/:slug/complete` | Valide la leçon (serveur) + mini‑révision |
| POST | `/questions/:id/answer` | Corrige une question émise, met à jour FSRS, XP |
| GET | `/reviews/summary` · POST `/reviews/session` | File de révisions |
| GET | `/dashboard` | Données de l'accueil |
| GET | `/stats` | Statistiques détaillées |
| GET/PUT | `/notifications/preferences` | Réglages des rappels |
| POST/DELETE | `/notifications/push-subscription` | Abonnement Web Push |
| GET | `/notifications/inbox` · POST `/notifications/:id/open` | Popups in‑app |
| POST | `/notifications/test` | Envoie un défi immédiat (pour tester) |

## 6. Plan de développement

- **Phase 1 (livrée ici)** : socle monorepo, moteur pédagogique testé, auth, onboarding,
  dashboard, parcours N5 (premiers mondes), 8 types d'exercices, révisions FSRS,
  rappels push + popups, stats, RGPD, PWA, tests unitaires/intégration/E2E.
- **Phase 2 (livrée)** : avatar, carte animée, inventaire, quêtes, boss, mini‑jeux, succès.
- **Phase 3 (en cours)** : N5 complet, test de positionnement et examen blanc N5 livrés ; N4 : 7 îles et examen blanc N4 ; N3 → N1 à venir.
- **Phase 4 (en cours)** : application Expo livrée (parcours, leçons, révisions, rappels natifs, session par jeton Bearer) ; à venir : combats, mini-jeux, hors ligne.
- **Phase 5** : assistant IA, prononciation, tracé de kanji, social.
