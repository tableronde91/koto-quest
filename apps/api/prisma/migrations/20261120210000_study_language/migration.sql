-- Plusieurs langues : japonais (JLPT) et coréen (TOPIK)
ALTER TABLE "UserPreferences" ADD COLUMN "studyLanguage" TEXT NOT NULL DEFAULT 'ja';
ALTER TABLE "UserPreferences" ADD COLUMN "levelByLanguage" JSONB NOT NULL DEFAULT '{}';
