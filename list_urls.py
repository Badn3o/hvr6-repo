#!/usr/bin/env python3
"""
Extract HVR 6 Capabilities content from Fivetran documentation.
This script generates a shell script that uses curl to fetch pages,
then we use the browser tool to extract content via JavaScript.
"""

RELEASES = [
    ("635", "6.3.5"),
    ("630", "6.3.0"),
    ("625", "6.2.5"),
    ("620", "6.2.0"),
    ("615", "6.1.5"),
    ("610", "6.1.0"),
]

DATABASES = [
    "apache-kafka",
    "aurora-mysql",
    "aurora-postgresql",
    "azure-sql-database",
    "azure-sql-managed-instance",
    "azure-synapse-analytics",
    "bigquery",
    "databricks",
    "db2-for-i",
    "db2-for-linux-unix-and-windows",
    "db2-for-z-os",
    "greenplum",
    "ingres",
    "mariadb",
    "mysql",
    "oracle",
    "postgresql",
    "redshift",
    "sap-hana",
    "sap-netweaver-on-hana",
    "sap-netweaver-on-oracle",
    "singlestore",
    "snowflake",
    "sql-database-in-microsoft-fabric",
    "sql-server",
    "sybase-ase",
    "teradata",
    "vector",
    "yugabytedb",
]

# Output the list of all URLs to visit
for ver, label in RELEASES:
    print(f"RELEASE:{ver}:{label}")
    print(f"  MAIN:https://fivetran.com/docs/hvr6/capabilities/{ver}")
    for db in DATABASES:
        print(f"  SUB:{db}:https://fivetran.com/docs/hvr6/capabilities/{ver}/capabilities-for-{db}")
