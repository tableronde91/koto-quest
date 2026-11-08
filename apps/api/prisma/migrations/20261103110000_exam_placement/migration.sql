-- Examen blanc et test de positionnement
ALTER TABLE "UserPreferences" ADD COLUMN "placementAt" TIMESTAMP(3), ADD COLUMN "placedWorlds" INTEGER NOT NULL DEFAULT 0;
ALTER TABLE "World" ADD COLUMN "examSlug" TEXT;
ALTER TABLE "LearningSession" ADD COLUMN "state" JSONB;
ALTER TABLE "ExamAttempt" ADD COLUMN "sessionId" TEXT, ADD COLUMN "percent" INTEGER, ADD COLUMN "passed" BOOLEAN;

-- CreateIndex
CREATE UNIQUE INDEX "ExamAttempt_sessionId_key" ON "ExamAttempt"("sessionId");
CREATE INDEX "ExamAttempt_userId_finishedAt_idx" ON "ExamAttempt"("userId", "finishedAt");
