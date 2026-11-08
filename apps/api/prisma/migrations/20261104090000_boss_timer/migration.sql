-- Chrono des combats de gardiens : instant où la question est affichée
ALTER TABLE "IssuedQuestion" ADD COLUMN "shownAt" TIMESTAMP(3);
