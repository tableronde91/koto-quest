-- Combats de boss de fin de monde
ALTER TABLE "World" ADD COLUMN "bossName" TEXT, ADD COLUMN "bossGlyph" TEXT, ADD COLUMN "bossIntro" TEXT;
ALTER TABLE "LearningSession" ADD COLUMN "scope" TEXT;

-- CreateTable
CREATE TABLE "BossResult" (
    "userId" TEXT NOT NULL,
    "worldSlug" TEXT NOT NULL,
    "attempts" INTEGER NOT NULL DEFAULT 0,
    "victories" INTEGER NOT NULL DEFAULT 0,
    "bestHits" INTEGER NOT NULL DEFAULT 0,
    "firstVictoryAt" TIMESTAMP(3),
    "updatedAt" TIMESTAMP(3) NOT NULL,
    CONSTRAINT "BossResult_pkey" PRIMARY KEY ("userId","worldSlug")
);

-- AddForeignKey
ALTER TABLE "BossResult" ADD CONSTRAINT "BossResult_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
