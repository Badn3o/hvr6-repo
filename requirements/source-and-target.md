# Source and Target Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/index.md)

# Source and Target Requirements


Fivetran HVR can replicate between databases, directories (file locations), as well as between databases and directories that HVR calls 'locations'. HVR connects to these locations directly (from hub machine) or indirectly (via its HVR Agent connections). If HVR must access a source or target database directly, then the database connectivity (e.g. ODBC drivers) must be installed on the hub machine.

Additionally, the account that HVR uses must have sufficient access to capture changes from a source database or integrate changes into a target database.

## Topics


The following sections describe the pre-requisites, access privileges, and other configuration required for using HVR to capture or integrate changes into sources and targets locations (also called as the location types), listed below.

- [Actian Vector Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/actian-vector-requirements)
- [Amazon S3 Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/amazon-s3-requirements)
- [Apache HDFS Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-hdfs-requirements)
- [Apache Kafka Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements)
- [Aurora MySQL Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/aurora-mysql-requirements)
- [Azure Blob Storage Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-blob-storage-requirements)
- [Azure Data Lake Storage Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-data-lake-storage-requirements)
- [Azure SQL Database Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-sql-database-requirements)
- [Azure SQL Managed Instance Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-sql-managed-instance-requirements)
- [Azure Synapse Analytics Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-synapse-analytics-requirements)
- [Databricks Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/databricks-requirements)
- [Db2 for i Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-i-requirements)
- [Db2 for Linux, Unix and Windows Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-linux-unix-and-windows-requirements)
- [Db2 for z/OS Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements)
- [File, FTP, SFTP Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/file-ftp-sftp-requirements)
- [Google BigQuery Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-bigquery-requirements)
- [Google Cloud Storage Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-cloud-storage-requirements)
- [Greenplum Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/greenplum-requirements)
- [Ingres Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/ingres-requirements)
- [MariaDB Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/mariadb-requirements)
- [MySQL Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/mysql-requirements)
- [Oracle Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements)
- [PostgreSQL Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements)
- [Redshift Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/redshift-requirements)
- [SAP HANA Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements)
- [SAP NetWeaver Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements)
- [SingleStore Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/singlestore-requirements)
- [Snowflake Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements)
- [SQL Server Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements)
- [Sybase ASE Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements)
- [Teradata Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/teradata-requirements)

