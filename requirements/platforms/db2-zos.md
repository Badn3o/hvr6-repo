# Db2 for z/OS Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/index.md)

# Db2 for z/OS Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using 'Db2 for z/OS' for replication.

#### Supported Platforms


- Learn about the Db2 for z/OS versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Db2 for z/OS on our **Capabilities for Db2 for z/OS** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-db2-for-z-os), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-db2-for-z-os), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-db2-for-z-os), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-db2-for-z-os), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-db2-for-z-os), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-db2-for-z-os)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Db2 for z/OS data types and their mapping, see [Data Type Mapping for Db2 for z/OS](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-db2-for-z-os).

- 
Understand the character encodings HVR supports for Db2 for z/OS on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#db2forzos) page.



## Introduction


To capture from Db2 for z/OS, HVR needs to be installed on a separate machine(either 64-bit Linux on Intel or 64-bit Windows on Intel or 64-bit AIX on PowerPC) from which HVR will access Db2 on z/OS machine. Additionally, the HVR stored procedures need to be installed on Db2 for z/OS machine for accessing Db2 log files. For steps to install the stored procedures on Db2 for z/OS machine, see section [Installing Capture Stored Procedures](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/installing-capture-stored-procedures).

HVR requires 'Db2 Connect' for connecting to Db2 for z/OS.



## Prerequisites for Fivetran HVR Machine


HVR requires the IBM Data Server Driver for ODBC and CLI or Db2 client or Db2 server or Db2 Connect to be installed on the machine from which HVR connects to Db2 on z/OS. The Db2 client should have an instance to store the data required for the remote connection.

To install the IBM Data Server Driver for ODBC and CLI, refer to the [IBM documentation](https://www.ibm.com/docs/en/db2/11.5?topic=clients-data-server-drivers).

To set up the Db2 client or Db2 server or Db2 Connect, use the following commands to catalog the TCP/IP node and the remote database:
db2 catalog tcpip node <em>nodename</em> remote <em>hostname</em> server <em>portnumber</em>
db2 catalog database <em>databasename</em> at node <em>nodename</em>

- *nodename* is the local nickname for the remote machine that contains the database you want to catalog.
- *hostname* is the name of the host/node where the target database resides.
- *databasename* is the name of the database you want to catalog.


For more information about configuring Db2 client or Db2 server or Db2 Connect, refer to [IBM documentation](https://www.ibm.com/support/knowledgecenter/en).

### Verifying Connection to the Db2 Server


To test the connection to the Db2 server on the z/OS machine, use the following command:

- 
When using IBM Data Server Driver for ODBC and CLI
db2cli validate -database <em>databasename</em>:<em>servername</em>:<em>portnumber</em> -connect -user <em>username</em> -passwd <em>password</em>

or
db2cli validate -dsn <em>dsnname</em> -connect -user <em>username</em> -passwd <em>password</em>



- When using Db2 client or Db2 server or Db2 Connectdb2 connect to<em> databasenam</em>e user<em> userid</em>



## Related Articles


- [Installing Capture Stored Procedures](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/installing-capture-stored-procedures)
- [Db2 for z/OS as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source)
- [Db2 for z/OS as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-target)
- [Location Connection for Db2 for z/OS](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-db2-for-z-os)

