-- Personnage, boutique et quêtes récompensées
ALTER TABLE "User" ADD COLUMN "avatar" JSONB;
ALTER TABLE "DailyActivity" ADD COLUMN "questsClaimed" TEXT[] DEFAULT ARRAY[]::TEXT[];

-- CreateIndex
CREATE UNIQUE INDEX "InventoryItem_userId_sku_key" ON "InventoryItem"("userId", "sku");
