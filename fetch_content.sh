#!/bin/bash
# Fetch HVR 6 capabilities pages using curl and extract content
OUTPUT_DIR="/root/hvr-docs"
mkdir -p "$OUTPUT_DIR"

RELEASES=("635" "630" "625" "620" "615" "610")
DATABASES=(
  "apache-kafka"
  "aurora-mysql"
  "aurora-postgresql"
  "azure-sql-database"
  "azure-sql-managed-instance"
  "azure-synapse-analytics"
  "bigquery"
  "databricks"
  "db2-for-i"
  "db2-for-linux-unix-and-windows"
  "db2-for-z-os"
  "greenplum"
  "ingres"
  "mariadb"
  "mysql"
  "oracle"
  "postgresql"
  "redshift"
  "sap-hana"
  "sap-netweaver-on-hana"
  "sap-netweaver-on-oracle"
  "singlestore"
  "snowflake"
  "sql-database-in-microsoft-fabric"
  "sql-server"
  "sybase-ase"
  "teradata"
  "vector"
  "yugabytedb"
)

echo "Fetching capabilities pages..."

for ver in "${RELEASES[@]}"; do
  echo "Fetching main page for $ver..."
  curl -s "https://fivetran.com/docs/hvr6/capabilities/$ver" -o "$OUTPUT_DIR/raw_${ver}_main.html"
  
  for db in "${DATABASES[@]}"; do
    echo "  Fetching $ver/$db..."
    curl -s "https://fivetran.com/docs/hvr6/capabilities/$ver/capabilities-for-$db" -o "$OUTPUT_DIR/raw_${ver}_${db}.html"
    sleep 0.5
  done
done

echo "Done fetching."
