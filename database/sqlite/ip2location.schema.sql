-- SQLite schema extracted without original records.
CREATE TABLE "asn" (
  "ip_from" integer NOT NULL,
  "ip_to" integer NOT NULL,
  "cidr" TEXT NOT NULL,
  "asn" TEXT NOT NULL,
  "as" TEXT NOT NULL
);
CREATE INDEX "idx_ip_from"
ON "asn" (
  "ip_from" ASC
);
CREATE INDEX "idx_ip_to"
ON "asn" (
  "ip_to" ASC
);
