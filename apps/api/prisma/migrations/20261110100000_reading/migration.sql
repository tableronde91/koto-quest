-- CreateTable
CREATE TABLE "ReadingLog" (
    "userId" TEXT NOT NULL,
    "chapter" TEXT NOT NULL,
    "dateKey" TEXT NOT NULL,
    "correct" INTEGER NOT NULL,
    "total" INTEGER NOT NULL,
    "seconds" INTEGER NOT NULL DEFAULT 0,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "ReadingLog_pkey" PRIMARY KEY ("userId","chapter")
);

-- CreateIndex
CREATE INDEX "ReadingLog_userId_dateKey_idx" ON "ReadingLog"("userId", "dateKey");

-- AddForeignKey
ALTER TABLE "ReadingLog" ADD CONSTRAINT "ReadingLog_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
