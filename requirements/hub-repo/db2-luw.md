# Repository Database in Db2 for Linux, Unix and Windows - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-db2-for-linux-unix-and-windows

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-db2-for-linux-unix-and-windows/index.md)

# Repository Database in Db2 for Linux, Unix and Windows


Fivetran HVR allows you to create a repository database in Db2 for Linux, Unix and Windows (LUW). The **Repository Database** section in **Capabilities** ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635#repositorydatabase), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630#repositorydatabase), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#repositorydatabase), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#repositorydatabase), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#repositorydatabase), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#repositorydatabase)) lists the supported Db2 for Linux, Unix and Windows (LUW) versions that can be used as a repository database.

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

## Grants for Repository Database


The following grant is required for the repository database in Db2 for LUW:

- The HVR repository user should have permission to create and drop HVR [repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables).GRANT CREATETAB ON DATABASE TO USER <em>username</em> 



## Repository Database Connection


This section describes the details required for connecting to the repository database in Db2 for LUW:

 Field | Description | Equivalent Location Property |
 **INSTHOME** | 
When using "Db2 client or Db2 server or Db2 Connect" the directory path of the Db2 installation must be specified.

When using "IBM Data Server Driver for ODBC and CLI" the directory path of the IBM Data Server Driver for ODBC and CLI installation on HVR machine (e.g. **/distr/db2/driver/odbc_cli/clidriver**) must be specified.

Example: **/db2/9.7** | [**Db2_INSTHOME**](https://fivetran.com/docs/hvr6/property-reference/location-properties#db2insthome) |
 **DB2INSTANCE** | 
When using "Db2 client or Db2 server or Db2 Connect", the name of the Db2 instance must be specified.

When using "IBM Data Server Driver for ODBC and CLI" this field must be left blank/empty.

Example: **db2instl** | [**Db2_DB2INSTANCE**](https://fivetran.com/docs/hvr6/property-reference/location-properties#db2db2instance) |
 **DATABASE** | 
Name of the DB2 database.

Example: **mytestdb** | [**Database_Name**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasename) |
 **USER** | 
Username for connecting HVR to the Db2 database.

Example: **hvruser** | [**Database_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseuser) |
 **PASSWORD** | Password for the **USER**. | **[Database_Password](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasepassword)** |

