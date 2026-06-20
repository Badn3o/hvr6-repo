#!/bin/bash
# Script to extract content from all HVR 6 capabilities pages
# Uses a headless approach with the browser tool via a control file

OUTPUT_DIR="/root/hvr-docs"
mkdir -p "$OUTPUT_DIR"

# All releases
RELEASES=("635" "630" "625" "620" "615" "610")

# All databases (sub-pages)
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

# Generate a JSON file with all URLs to visit
echo '{"urls":[' > "$OUTPUT_DIR/urls.json"

first=true
for ver in "${RELEASES[@]}"; do
  if [ "$first" = true ]; then first=false; else echo "," >> "$OUTPUT_DIR/urls.json"; fi
  echo "{\"release\":\"$ver\",\"url\":\"https://fivetran.com/docs/hvr6/capabilities/$ver\",\"type\":\"main\"}" >> "$OUTPUT_DIR/urls.json"
  
  for db in "${DATABASES[@]}"; do
    echo ",{\"release\":\"$ver\",\"db\":\"$db\",\"url\":\"https://fivetran.com/docs/hvr6/capabilities/$ver/capabilities-for-$db\",\"type\":\"sub\"}" >> "$OUTPUT_DIR/urls.json"
  done
done

echo ']}' >> "$OUTPUT_DIR/urls.json"

echo "Generated URLs file with all pages to visit"
