# Oracle Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/index.md)

# Oracle Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Oracle for replication.

#### Supported Platforms


- Learn about the Oracle versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Oracle on our **Capabilities for Oracle** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-oracle), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-oracle), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of supported Oracle data types and their mapping, see [Data Type Mapping for Oracle](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-oracle).

- 
Understand the character encodings HVR supports for Oracle on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#oracle) page.



> **Note:** 
Fivetran provides additional solutions for replicating data from Oracle. For more information, see section [Oracle](https://fivetran.com/docs/connectors/databases/oracle) in Databases.


> **Important:** 
Oracle client library version 21 is supported since version 6.1.0/19.


## Connecting to Oracle Database or ASM Instance


This section describes how HVR connects to an Oracle Database or ASM instance. HVR uses Oracle’s native TNS connection libraries to establish the connection and supports two connection types: **Local connections** and **TNS connections**.

### Local connections


A local connection uses the bequeath protocol to establish a direct connection, which bypasses the listener and provides higher performance. It uses an Oracle SID to identify the Oracle Database or ASM instance. To use this connection type, HVR must run on the same machine as the Oracle Database or ASM instance, and you must set **ORACLE_HOME** to the Oracle home for that instance.

In the HVR UI, to use this method, select the [**Local connect to database**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-oracle) option and enter the SID in the **SID** field. For CLI and REST API configurations, use the [**Oracle_SID**](https://fivetran.com/docs/hvr6/property-reference/location-properties#oraclesid) location property.

### TNS connections


A TNS connection uses the Oracle listener to establish the connection. You can use this connection type regardless of whether HVR runs on the same machine as the Oracle instance or on a remote machine. This connection type supports all TNS features, including mTLS. HVR supports the following methods for establishing a TNS connection:

- 
**Connection string**
Connect using a simple host-based connection string in the form HOST[:PORT]/SERVICE_NAME.

- 
**TNS alias**
Connect using a TNS alias that resolves to the Oracle Database or ASM instance. To use this method, you must include TNSNAMES in NAMES.DIRECTORY_PATH in the sqlnet.ora file used for the connection.

- 
**EZCONNECT**
Connect using the EZCONNECT naming method, with a connection identifier in the form ``HOST[:PORT]/SERVICE_NAME_or_SID. To use this method, you must include EZCONNECTinNAMES.DIRECTORY_PATHin thesqlnet.ora` file used for the connection. For more information about EZCONNECT, see Oracle’s [Configuring the Easy Connect Naming Method documentation](https://docs.oracle.com/en/database/oracle/oracle-database/26/netag/configuring-easy-connect-naming-method.html).



In the HVR UI, to use this method, select the [**Oracle TNS**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-oracle) option and enter either a TNS alias or a connect string in the **Oracle TNS** field. For CLI and REST API configurations, use the [**Oracle_TNS**](https://fivetran.com/docs/hvr6/property-reference/location-properties#oracletns) location property.

## Oracle Database Client


HVR requires the **full** Oracle Database Client to be installed on the machine from which it connects to the Oracle database, except when HVR is installed on the Oracle database server machine. For detailed instructions on downloading and installing the Oracle Database Client, refer to Oracle’s documentation for [Linux](https://docs.oracle.com/en/database/oracle/oracle-database/23/lacli/installing-oracle-database-client.html) (also see [OS Requirements](https://docs.oracle.com/en/database/oracle/oracle-database/23/lacli/operating-system-requirements-for-x86-64-linux-platforms.html)) and [Windows](https://docs.oracle.com/en/database/oracle/oracle-database/23/ntcli/install-oracle-db-client.html).

The requirement to install the Oracle Database Client depends on how the HVR Hub connects to the Oracle database.

- 
**Connects directly without HVR Agent**:

- When the HVR Hub installed on the Oracle database server connects directly to the Oracle database, you **don’t need** to install the Oracle Database Client, assuming the full Oracle Database Client was pre-installed with Oracle.
- When the HVR Hub installed on a separate machine (not the Oracle database server) connects directly to the Oracle database, you **must** install the full Oracle Database Client on the machine hosting the HVR Hub.


- 
**Connects via HVR Agent**:

- When the HVR Hub connects to the Oracle database through an HVR Agent installed on the Oracle database server, you **don’t need** to install the Oracle Database Client, assuming the full Oracle Database Client was pre-installed with Oracle.
- When the HVR Hub connects to the Oracle database through an HVR Agent installed on a separate machine (not the Oracle database server), you **must** install the full Oracle Database Client on the machine hosting the HVR Agent.




> **Important:** 
When installing the client, ensure that you install only the **full** Oracle Database Client, as the Instant Client is insufficient for HVR operations. The [full Oracle Database Client](https://docs.oracle.com/en/database/oracle/oracle-database/23/lacli/installing-oracle-database-client.html#GUID-07890CF0-35FE-42F8-A27B-53E2EC3ED039) includes all necessary libraries and tools for advanced features such as replication and monitoring, whereas the [Oracle Instant Client](https://docs.oracle.com/en/database/oracle/oracle-database/23/lacli/about-instant-client.html#GUID-A4EEF626-09E3-4116-ABAD-885D60E9CFF0) is lightweight and may lack the critical libraries required for these features.


## Supported Editions


HVR supports the following Oracle editions:

- Enterprise edition
- Standard edition


> **Important:** 
HVR log-based capture is not supported on Oracle 18c Express Edition because the supplemental logging settings cannot be modified in this edition.


## Related Articles


- [Oracle as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source)
- [Capture from Oracle using Direct Redo Access](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-direct-redo-access)
- [Capture from Oracle ASM](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-direct-redo-access/capture-from-oracle-asm)
- [Capture from Oracle Data Guard](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-direct-redo-access/capture-from-oracle-data-guard)


- [Capture from Oracle using Archive Only](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-archive-only)
- [Capture from Oracle using LogMiner](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-logminer)
- [Capture from Amazon RDS for Oracle](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-logminer/capture-from-amazon-rds-for-oracle)


- [Capture from Oracle using BFile](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-bfile)
- [Capture from Oracle TDE](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-tde)
- [Capture from Oracle Pluggable Database](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-pluggable-database)
- [Capture from Oracle RAC](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-rac)


- [Oracle as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-target)
- [Location Connection for Oracle](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-oracle)

