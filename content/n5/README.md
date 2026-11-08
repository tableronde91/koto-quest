# Contenu pédagogique

Le contenu est **séparé du code** : chaque niveau est un fichier JSON importé par `npm run db:seed`.

- Import idempotent : chaque monde, chapitre, leçon et notion est identifié par son `slug` (upsert).
  Corriger une traduction = modifier le JSON puis relancer le seed ; la progression des utilisateurs est conservée.
- `contentVersion` est enregistré en base : incrémentez-le à chaque publication.
- Le seed **valide** le contenu (réponse présente parmi les choix, pas de doublons, explication obligatoire)
  et refuse l'import en cas d'erreur.
- Les notions partagent un `slug` global : un même mot introduit dans deux leçons n'a qu'une seule carte de révision.

Types de notions : `kana`, `vocabulary`, `kanji` (avec `kanji.onyomi`, `kanji.kunyomi`, `kanji.strokes`), `grammar`.
Types d'exercices rédigés : `particle_choice`, `fill_blank`, `sentence_order`, `dialogue_choice`, `true_false`.
Les QCM sens/lecture/écoute/association sont générés automatiquement par `@koto/learning-engine`.

Tout le contenu est original. Les listes ne sont pas les listes officielles du JLPT (qui n'en publie plus depuis 2010).
