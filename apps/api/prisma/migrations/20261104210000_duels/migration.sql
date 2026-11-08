-- Duels en ligne : profils classés, duels, réponses
CREATE TABLE "DuelProfile" (
    "userId" TEXT NOT NULL,
    "code" TEXT NOT NULL,
    "rating" INTEGER NOT NULL DEFAULT 1000,
    "peakRating" INTEGER NOT NULL DEFAULT 1000,
    "wins" INTEGER NOT NULL DEFAULT 0,
    "losses" INTEGER NOT NULL DEFAULT 0,
    "draws" INTEGER NOT NULL DEFAULT 0,
    "streak" INTEGER NOT NULL DEFAULT 0,
    "bestStreak" INTEGER NOT NULL DEFAULT 0,
    "damageDealt" INTEGER NOT NULL DEFAULT 0,
    "lastDuelAt" TIMESTAMP(3),
    "queuedAt" TIMESTAMP(3),
    "queueSeenAt" TIMESTAMP(3),
    "updatedAt" TIMESTAMP(3) NOT NULL,
    CONSTRAINT "DuelProfile_pkey" PRIMARY KEY ("userId")
);
CREATE UNIQUE INDEX "DuelProfile_code_key" ON "DuelProfile"("code");
CREATE INDEX "DuelProfile_rating_idx" ON "DuelProfile"("rating");
CREATE INDEX "DuelProfile_wins_idx" ON "DuelProfile"("wins");
CREATE INDEX "DuelProfile_queuedAt_idx" ON "DuelProfile"("queuedAt");
ALTER TABLE "DuelProfile" ADD CONSTRAINT "DuelProfile_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE "Duel" (
    "id" TEXT NOT NULL,
    "kind" TEXT NOT NULL,
    "status" TEXT NOT NULL,
    "p1Id" TEXT NOT NULL,
    "p2Id" TEXT,
    "botName" TEXT,
    "botRating" INTEGER,
    "hp1" INTEGER NOT NULL DEFAULT 100,
    "hp2" INTEGER NOT NULL DEFAULT 100,
    "streak1" INTEGER NOT NULL DEFAULT 0,
    "streak2" INTEGER NOT NULL DEFAULT 0,
    "round" INTEGER NOT NULL DEFAULT 0,
    "roundStartsAt" TIMESTAMP(3),
    "questions" JSONB NOT NULL,
    "seen1" TIMESTAMP(3),
    "seen2" TIMESTAMP(3),
    "outcome" TEXT,
    "endReason" TEXT,
    "rating1" INTEGER,
    "rating2" INTEGER,
    "delta1" INTEGER,
    "delta2" INTEGER,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "startedAt" TIMESTAMP(3),
    "endedAt" TIMESTAMP(3),
    CONSTRAINT "Duel_pkey" PRIMARY KEY ("id")
);
CREATE INDEX "Duel_p1Id_status_idx" ON "Duel"("p1Id", "status");
CREATE INDEX "Duel_p2Id_status_idx" ON "Duel"("p2Id", "status");
ALTER TABLE "Duel" ADD CONSTRAINT "Duel_p1Id_fkey" FOREIGN KEY ("p1Id") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "Duel" ADD CONSTRAINT "Duel_p2Id_fkey" FOREIGN KEY ("p2Id") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE "DuelAnswer" (
    "duelId" TEXT NOT NULL,
    "round" INTEGER NOT NULL,
    "side" INTEGER NOT NULL,
    "answer" TEXT NOT NULL,
    "correct" BOOLEAN NOT NULL,
    "ms" INTEGER NOT NULL,
    "damage" INTEGER NOT NULL DEFAULT 0,
    "critical" BOOLEAN NOT NULL DEFAULT false,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "DuelAnswer_pkey" PRIMARY KEY ("duelId", "round", "side")
);
ALTER TABLE "DuelAnswer" ADD CONSTRAINT "DuelAnswer_duelId_fkey" FOREIGN KEY ("duelId") REFERENCES "Duel"("id") ON DELETE CASCADE ON UPDATE CASCADE;
