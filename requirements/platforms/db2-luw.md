# Db2 for Linux, Unix and Windows Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-linux-unix-and-windows-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/db2-for-linux-unix-and-windows-requirements/index.md)

# Db2 for Linux, Unix and Windows Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Db2 for Linux, Unix and Windows (LUW) for replication.

#### Supported Platforms


- Learn about the Db2 for LUW versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Db2 for LUW on our **Capabilities for Db2 for LUW** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-db2-for-linux-unix-and-windows), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-db2-for-linux-unix-and-windows), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-db2-for-linux-unix-and-windows), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-db2-for-linux-unix-and-windows), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-db2-for-linux-unix-and-windows), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-db2-for-linux-unix-and-windows)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Db2 for LUW data types and their mapping, see [Data Type Mapping for Db2 for LUW](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-db2-for-linux-unix-and-windows).

- 
Understand the character encodings HVR supports for Db2 for LUW on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#db2forlinuxunixandwindows) page.



## Supported Editions


HVR supports the following editions of Db2 for LUW:

- Server Edition
- Advanced Enterprise Server Edition
- Express-C Edition


For information about compatibility and supported versions of Db2 for LUW with HVR platforms, see [Supported Platforms](https://fivetran.com/docs/hvr6/supported-platforms).

## Prerequisites


HVR requires Db2 client to be installed on the machine from which HVR connects to Db2. The Db2 client should have an instance to store the data required for the remote connection.

> **Important:** 
The Db2 client must be installed on a machine with the same ["endianness"](https://en.wikipedia.org/wiki/Endianness) as the machine running the Db2 server. For instance, AIX and Solaris SPARC are big-endian operating systems, while Linux and Windows are little-endian. Therefore, if the Db2 server is running on AIX, the Db2 client should be installed on either AIX or Solaris SPARC.


- 
To set up the Db2 client, use the following commands to [catalog the TCP/IP node](https://www.ibm.com/docs/en/db2/latest?topic=commands-catalog-tcpip-node) and the remote database:
db2 CATALOG TCPIP NODE <em>nodename</em> REMOTE <em>remotehost</em> SERVER <em>portnumber</em>

db2 CATALOG DATABASE <em>databasename</em> AT NODE <em>nodename</em>

- 
To test the connection with Db2 server, use the following command:
db2 CONNECT TO <em>databasename</em> USER <em>username</em>



For more information about configuring Db2 client, refer to [Db2 documentation](https://www.ibm.com/docs/en/db2/latest).

## Related Articles


- [Db2 for LUW as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-linux-unix-and-windows-requirements/db2-for-luw-as-source)
- [Db2 for LUW as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-linux-unix-and-windows-requirements/db2-for-luw-as-target)
- [Location Connection for Db2 for LUW](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-db2-for-luw)

