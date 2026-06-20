# HVR 6 Documentation - Complete Reference

**Source:** https://fivetran.com/docs/hvr6
**Generated:** 2026-06-20
**Version coverage:** 6.1.0, 6.2.0, 6.2.5, 6.3.0, 6.3.5

HVR (High-Volume Replicator) is a self-hosted enterprise-level replication solution
for databases and file systems, now part of Fivetran.

---

## Table of Contents

### 1. Getting Started
- [Getting Started](getting-started/index.md)
- [Quick Start Guide](getting-started/quick-start.md)
- [Document Conventions](getting-started/document-conventions.md)
- [Pricing](getting-started/pricing.md)
- [Licensing](getting-started/licensing.md)
- [Release Life Cycle](getting-started/release-life-cycle.md)

#### Concepts
- [Architecture](getting-started/concepts/architecture.md)
- [Channel](getting-started/concepts/channel.md)
- [Location](getting-started/concepts/location.md)
- [Agent](getting-started/concepts/agent.md)
- [Refresh](getting-started/concepts/refresh.md)
- [Compare](getting-started/concepts/compare.md)
- [Jobs](getting-started/concepts/jobs.md)
- [Events](getting-started/concepts/events.md)
- [Scheduler](getting-started/concepts/scheduler.md)
- [Replication Topologies](getting-started/concepts/replication-topologies.md)

### 2. Supported Platforms
- [Supported Platforms](supported-platforms/index.md)

### 3. Capabilities
- [Capabilities 6.2.0](capabilities/620.md)
- [Capabilities 6.2.5](capabilities/625.md)
- [Capabilities 6.3.0](capabilities/630.md)
- [Capabilities 6.3.5](capabilities/635.md)

### 4. Requirements
- [Source and Target Requirements](requirements/source-and-target.md)
- [Hub Repository Requirements](requirements/hub-repository.md)

#### Platform-Specific Requirements
- [Oracle](requirements/platforms/oracle.md)
- [Oracle as Source](requirements/platforms/oracle-as-source.md)
- [Snowflake](requirements/platforms/snowflake.md)
- [Snowflake as Target](requirements/platforms/snowflake-as-target.md)
- [Snowflake Staging](requirements/platforms/snowflake-staging.md)
- [SQL Server](requirements/platforms/sql-server.md)
- [PostgreSQL](requirements/platforms/postgresql.md)
- [MySQL](requirements/platforms/mysql.md)
- [MariaDB](requirements/platforms/mariadb.md)
- [DB2 for LUW](requirements/platforms/db2-luw.md)
- [DB2 for z/OS](requirements/platforms/db2-zos.md)
- [DB2 for i](requirements/platforms/db2-i.md)
- [Teradata](requirements/platforms/teradata.md)
- [Sybase ASE](requirements/platforms/sybase-ase.md)
- [SAP HANA](requirements/platforms/sap-hana.md)
- [SAP NetWeaver](requirements/platforms/sap-netweaver.md)
- [Greenplum](requirements/platforms/greenplum.md)
- [SingleStore](requirements/platforms/singlestore.md)
- [Ingres](requirements/platforms/ingres.md)
- [Actian Vector](requirements/platforms/actian-vector.md)
- [Redshift](requirements/platforms/redshift.md)
- [Google BigQuery](requirements/platforms/bigquery.md)
- [Databricks](requirements/platforms/databricks.md)
- [Azure Synapse](requirements/platforms/azure-synapse.md)
- [Azure SQL Database](requirements/platforms/azure-sql-db.md)
- [Azure SQL Managed Instance](requirements/platforms/azure-sql-mi.md)
- [Azure Blob Storage](requirements/platforms/azure-blob.md)
- [Azure Data Lake](requirements/platforms/azure-data-lake.md)
- [Amazon S3](requirements/platforms/amazon-s3.md)
- [Google Cloud Storage](requirements/platforms/google-cloud-storage.md)
- [Apache Kafka](requirements/platforms/apache-kafka.md)
- [Apache HDFS](requirements/platforms/apache-hdfs.md)
- [File (FTP/SFTP)](requirements/platforms/file-ftp-sftp.md)
- [Aurora MySQL](requirements/platforms/aurora-mysql.md)
- [Aurora PostgreSQL](requirements/platforms/aurora-postgresql.md)
- [SQL DB in Microsoft Fabric](requirements/platforms/sql-db-fabric.md)

#### Hub Repository by Platform
- [Oracle](requirements/hub-repo/oracle.md)
- [SQL Server](requirements/hub-repo/sql-server.md)
- [PostgreSQL](requirements/hub-repo/postgresql.md)
- [MySQL](requirements/hub-repo/mysql.md)
- [MariaDB](requirements/hub-repo/mariadb.md)
- [DB2 LUW](requirements/hub-repo/db2-luw.md)
- [Sybase ASE](requirements/hub-repo/sybase-ase.md)
- [Azure SQL Database](requirements/hub-repo/azure-sql-db.md)
- [Azure SQL MI](requirements/hub-repo/azure-sql-mi.md)
- [Aurora PostgreSQL](requirements/hub-repo/aurora-postgresql.md)
- [Aurora MySQL](requirements/hub-repo/aurora-mysql.md)
- [SQL DB Fabric](requirements/hub-repo/sql-db-fabric.md)

### 5. Install and Upgrade
- [Install and Upgrade](install-upgrade/index.md)
- [Download](install-upgrade/download.md)
- [Install Hub](install-upgrade/install/hub.md)
- [Install Agent](install-upgrade/install/agent.md)
- [Configure](install-upgrade/configure.md)
- [Configure Hub](install-upgrade/configure/hub.md)
- [Configure Agent](install-upgrade/configure/agent.md)
- [Upgrade](install-upgrade/upgrade.md)
- [Upgrading from HVR 5](install-upgrade/upgrade/from-hvr5.md)
- [Uninstall](install-upgrade/uninstall.md)

### 6. User Interface
- [User Interface](user-interface/index.md)
- [Channels](user-interface/channels.md)
- [Channel Details](user-interface/channels/channel-details.md)
- [Refreshing Data](user-interface/channels/refreshing-data.md)
- [Comparing Data](user-interface/channels/comparing-data.md)
- [Activating Replication](user-interface/channels/activating-replication.md)
- [Adding Tables](user-interface/channels/adding-tables.md)
- [Locations](user-interface/locations.md)
- [Location Details](user-interface/locations/location-details.md)
- [Tables](user-interface/tables.md)
- [Table Details](user-interface/tables/table-details.md)
- [Topology](user-interface/topology.md)
- [Statistics](user-interface/statistics.md)
- [Jobs](user-interface/jobs.md)
- [Events](user-interface/events.md)
- [Event Details](user-interface/events/event-details.md)
- [System Alerts](user-interface/system/alerts.md)

### 7. Command Line Interface
- [CLI Overview](cli/index.md)
- [hvrrefresh](cli/command-reference/hvrrefresh.md)
- [hvrcompare](cli/command-reference/hvrcompare.md)
- [hvradapt](cli/command-reference/hvradapt.md)
- [hvrhubconfig](cli/command-reference/hvrhubconfig.md)
- [hvragentlistener](cli/command-reference/hvragentlistener.md)
- [hvruserconfig](cli/command-reference/hvruserconfig.md)
- [hvrlicense](cli/command-reference/hvrlicense.md)
- [hvralertconfig](cli/command-reference/hvralertconfig.md)
- [hvrlogin](cli/command-reference/hvrlogin.md)
- [hvrreposconfig](cli/command-reference/hvrreposconfig.md)

### 8. Action Reference
- [Capture](action-reference/capture.md)
- [Integrate](action-reference/integrate.md)
- [Restrict](action-reference/restrict.md)
- [AdaptDDL](action-reference/adaptddl.md)
- [Transform](action-reference/transform.md)
- [FileFormat](action-reference/fileformat.md)
- [CollisionDetect](action-reference/collisiondetect.md)
- [Scheduling](action-reference/scheduling.md)
- [TableProperties](action-reference/tableproperties.md)
- [ColumnProperties](action-reference/columnproperties.md)
- [DBObjectGeneration](action-reference/dbobjectgeneration.md)
- [Environment](action-reference/environment.md)
- [AgentPlugin](action-reference/agentplugin.md)
- [DBSequence](action-reference/dbsequence.md)

### 9. Property Reference
- [Location Properties](property-reference/location-properties.md)
- [Hub Properties](property-reference/hub-properties.md)
- [Hub Server Properties](property-reference/hub-server-properties.md)
- [Agent Properties](property-reference/agent-properties.md)
- [Alert Properties](property-reference/alert-properties.md)
- [User Properties](property-reference/user-properties.md)
- [Repository Properties](property-reference/repository-properties.md)

### 10. Advanced Operations
- [Advanced Operations](advanced-operations/index.md)
- [Data Type Mapping](advanced-operations/data-type-mapping.md)
- [Replication with File Locations](advanced-operations/replication-with-file-locations.md)
- [Multidirectional Replication](advanced-operations/configuring-multidirectional-replication.md)
- [Extended Data Type Support](advanced-operations/extended-data-type-support.md)
- [Character Encodings](advanced-operations/supported-character-encodings.md)
- [Managing Recapturing](advanced-operations/managing-recapturing.md)
- [Performance Metrics](advanced-operations/performance-metrics.md)
- [Time Profiler](advanced-operations/time-profiler.md)
- [Tuning Capture Checkpoints](advanced-operations/tuning-capture-checkpoints.md)
- [Managed Secrets](advanced-operations/managed-secrets.md)
- [Migrating from HVR 5](advanced-operations/migrating-channel-from-hvr5.md)
- [Migrating Pre-prod to Prod](advanced-operations/migrating-channel-preprod-to-prod.md)
- [Upgrading Database on Source](advanced-operations/upgrading-database-source.md)
- [Analyzing Diff File](advanced-operations/analyzing-diff-file.md)
- [Replication Transformations](advanced-operations/replication-transformations.md)
- [Manual DDL Adaptation](advanced-operations/manual-ddl-adaptation.md)
- [Context Variables for DateTime](advanced-operations/contexts-variables-datetime.md)

#### Data Type Mappings by Platform
- [Oracle](advanced-operations/data-type-mapping/oracle.md)
- [SQL Server](advanced-operations/data-type-mapping/sql-server.md)
- [PostgreSQL](advanced-operations/data-type-mapping/postgresql.md)
- [MySQL](advanced-operations/data-type-mapping/mysql.md)
- [MariaDB](advanced-operations/data-type-mapping/mariadb.md)
- [DB2 LUW](advanced-operations/data-type-mapping/db2-luw.md)
- [DB2 z/OS](advanced-operations/data-type-mapping/db2-zos.md)
- [DB2 i](advanced-operations/data-type-mapping/db2-i.md)
- [Teradata](advanced-operations/data-type-mapping/teradata.md)
- [Sybase ASE](advanced-operations/data-type-mapping/sybase-ase.md)
- [SAP HANA](advanced-operations/data-type-mapping/sap-hana.md)
- [SAP](advanced-operations/data-type-mapping/sap.md)
- [Greenplum](advanced-operations/data-type-mapping/greenplum.md)
- [SingleStore](advanced-operations/data-type-mapping/singlestore.md)
- [Ingres](advanced-operations/data-type-mapping/ingres.md)
- [Actian Vector](advanced-operations/data-type-mapping/actian-vector.md)
- [Redshift](advanced-operations/data-type-mapping/redshift.md)
- [BigQuery](advanced-operations/data-type-mapping/bigquery.md)
- [Databricks](advanced-operations/data-type-mapping/databricks.md)
- [Azure Synapse](advanced-operations/data-type-mapping/azure-synapse.md)
- [Azure SQL DB](advanced-operations/data-type-mapping/azure-sql-db.md)
- [Snowflake](advanced-operations/data-type-mapping/snowflake.md)
- [Kafka](advanced-operations/data-type-mapping/kafka.md)
- [Avro/JSON/Parquet](advanced-operations/data-type-mapping/avro-json-parquet.md)
- [Aurora PostgreSQL](advanced-operations/data-type-mapping/aurora-postgresql.md)
- [Aurora MySQL](advanced-operations/data-type-mapping/aurora-mysql.md)
- [SQL DB Fabric](advanced-operations/data-type-mapping/sql-db-fabric.md)

### 11. Internal Objects
- [Internal Objects](internal-objects/index.md)
- [Repository Tables](internal-objects/repository-tables.md)

### 12. REST API
- [REST API](rest-api/index.md)
- [REST API Reference](rest-api/rest-api-reference.md)

### 13. FAQ
- [FAQ](faq/index.md)
- [Troubleshooting](faq/troubleshooting.md)

### 14. Release Notes
- [Release Notes](release-notes/index.md)

---

## Statistics
- **Total markdown files:** 196
- **Total content size:** 2,602,200 bytes (2.5 MB)
- **Source:** Fivetran HVR 6 Documentation (fivetran.com/docs/hvr6)
