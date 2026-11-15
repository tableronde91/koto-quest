-- Dernière visite : durée de conservation des comptes (suppression après 3 ans d'inactivité)
ALTER TABLE "User" ADD COLUMN "lastSeenAt" TIMESTAMP(3);
