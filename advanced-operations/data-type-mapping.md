# Data Type Mapping - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/index.md)

# Data Type Mapping


Fivetran HVR's mapping/conversion of data types is complex because each DBMS's data types have a specific range which seldom corresponds to the range of another DBMS. For example, data type **varchar(10)** in SQL Server corresponds to **varchar2(10 bytes)** in Oracle, but **varchar(8000)** corresponds to **clob**. Note that the mapping here does not just depend on the 'name' of the data type, but also its 'attributes' like byte length, encoding, scale, and precision, etc. If HVR is not accurate in mapping data types, then target tables could be created which are unable to contain the data delivered from the source DBMS.

Data types are not directly mapped/converted from the source DBMS to the target DBMS, instead they are first mapped to the HVR 'repository data types' and then these repository data types are mapped to corresponding data types in target DBMS or file format. Data type mapping/conversion happens in the following manner:

- When a channel is built using the [**Table Selection**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel) dialog (or [**hvradapt**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvradapt)), the source DBMS data types are mapped to the HVR 'repository data types'.
After the tables are added to a channel the mapping of data types in source DBMS (capture location) to the HVR repository data types can be viewed in the [**Tables**](https://fivetran.com/docs/hvr6/user-interface/tables) and [**Table Details**](https://fivetran.com/docs/hvr6/user-interface/tables/table-details) page.
- Then during [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) and [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate), the HVR repository data types are mapped to corresponding data types in the target DBMS (integrate location). This mapping happens at the moment the [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) is used to create target tables.
After performing [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)/[**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) the mapping of the HVR repository data types to the target DBMS data types can be viewed in the [**Tables**](https://fivetran.com/docs/hvr6/user-interface/tables) and [**Table Details**](https://fivetran.com/docs/hvr6/user-interface/tables/table-details) page.


HVR repository data types do not have independent numeric or length limits. The precision, scale, and length stored in the repository data type are derived from the source data type's definition, and practical limits are governed by the source and target DBMS capabilities.

## Customizing Data Type Mapping


If the automatic/default mapping of data type is not appropriate for a specific channel, it can be modified using parameter [**Datatype**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatype) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties).

For example, by default HVR maps a **number** (without scale or precision) in Oracle to **numeric(38,4)** in SQL Server. By defining the following action, **number** (without scale or precision) in Oracle is mapped to **float** instead:

 Group | Table | Action | Parameter(s) |
 SRCGRP | * | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** | **[DatatypeMatch](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch)**=**"number[prec=0 && scale=0]"**, **[Datatype](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatype)**=**"float"** |


In the above example, parameter [**DatatypeMatch**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch) is used for mapping all columns with **number**(without scale or precision) data type into **float** data type.

Alternatively, parameter [**Name**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#name) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) can be used for mapping the data type of a specific column (e.g. **MYCOLUMN**) into **float** data type.

 Group | Table | Action | Parameter(s) |
 SRCGRP | * | ****[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**** | **[Name](https://fivetran.com/docs/hvr6/action-reference/columnproperties#name)**=**"MYCOLUMN"**, **[Datatype](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatype)**=**"float"** |


### Extended Data Type Support


'Extended data types' are the DBMS data types (e.g. **sql_variant** in SQL Server or **xmltype** in Oracle) which are not mapped to native HVR data types. Instead, HVR's [**Extended Data Type Support**](https://fivetran.com/docs/hvr6/advanced-operations/extended-data-type-support) feature should be used for such data types. For this, you need to use parameter [**CaptureExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) for converting an extended data type to a supported data type during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture), [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) or [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) (read from source) and parameter [**IntegrateExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#integrateexpression) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) for converting it back to extended data type during [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate), [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) or [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) (write into target) respectively.

## Data Type Mapping for Location Types


- [Data Type Mapping for Aurora MySQL](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-aurora-mysql)
- [Data Type Mapping for Aurora PostgreSQL](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-aurora-postgresql)
- [Data Type Mapping for Avro, Json, and Parquet](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-avro-json-parquet)
- [Data Type Mapping for Azure SQL Database](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-azure-sql-database)
- [Data Type Mapping for Azure Synapse Analytics](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-azure-synapse-analytics)
- [Data Type Mapping for Databricks](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-databricks)
- [Data Type Mapping for Db2 for i](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-db2-for-i)
- [Data Type Mapping for Db2 for Linux, Unix and windows](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-db2-for-linux-unix-and-windows)
- [Data Type Mapping for Db2 for z/OS](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-db2-for-z-os)
- [Data Type Mapping for Google BigQuery](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-google-bigquery)
- [Data Type Mapping for Greenplum](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-greenplum)
- [Data Type Mapping for Ingres](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-ingres)
- [Data Type Mapping for Kafka](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-kafka)
- [Data Type Mapping for Mariadb](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-mariadb)
- [Data Type Mapping for Mysql](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-mysql)
- [Data Type Mapping for Oracle](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-oracle)
- [Data Type Mapping for Postgresql](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-postgresql)
- [Data Type Mapping for Redshift](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-redshift)
- [Data Type Mapping for SAP HANA](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sap-hana)
- [Data Type Mapping for SAP](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sap)
- [Data Type Mapping for SingleStore](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-singlestore)
- [Data Type Mapping for Snowflake](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-snowflake)
- [Data Type Mapping for SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sql-database-in-microsoft-fabric)
- [Data Type Mapping for SQL Server](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sql-server)
- [Data Type Mapping for Sybase ASE](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sybase-ase)
- [Data Type Mapping for Teradata](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-teradata)
- [Data Type Mapping for Vector](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-vector)

