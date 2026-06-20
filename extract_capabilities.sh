#!/bin/bash
# Script to extract all HVR 6 Capabilities content using the browser tool
# We'll output the URLs to visit in order

OUTPUT_DIR="/root/hvr-docs"
mkdir -p "$OUTPUT_DIR"

# Define the releases and their sub-pages
RELEASES=("635:6.3.5" "630:6.3.0" "625:6.2.5" "620:6.2.0" "615:6.1.5" "610:6.1.0")

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

echo "# URLs to visit for HVR 6 Capabilities"
echo ""

for release in "${RELEASES[@]}"; do
  IFS=':' read -r ver label <<< "$release"
  echo "## Release $label"
  echo "MAIN: https://fivetran.com/docs/hvr6/capabilities/$ver"
  
  for db in "${DATABASES[@]}"; do
    echo "SUB: https://fivetran.com/docs/hvr6/capabilities/$ver/capabilities-for-$db"
  done
  echo ""
done
