-- Reprise des exercices ratés en fin de séance
ALTER TABLE "IssuedQuestion" ADD COLUMN "retryOf" TEXT;

-- CreateIndex
CREATE INDEX "IssuedQuestion_retryOf_idx" ON "IssuedQuestion"("retryOf");
