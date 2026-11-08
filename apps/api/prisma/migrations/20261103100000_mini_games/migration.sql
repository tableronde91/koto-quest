-- Mini-jeux chronométrés
ALTER TABLE "DailyActivity" ADD COLUMN "gameCoins" INTEGER NOT NULL DEFAULT 0;

-- CreateTable
CREATE TABLE "GameResult" (
    "userId" TEXT NOT NULL,
    "gameId" TEXT NOT NULL,
    "plays" INTEGER NOT NULL DEFAULT 0,
    "bestScore" INTEGER NOT NULL DEFAULT 0,
    "lastScore" INTEGER NOT NULL DEFAULT 0,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    CONSTRAINT "GameResult_pkey" PRIMARY KEY ("userId","gameId")
);

-- AddForeignKey
ALTER TABLE "GameResult" ADD CONSTRAINT "GameResult_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
