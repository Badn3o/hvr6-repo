# SQL Server Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/index.md)

# SQL Server Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using SQL Server for replication.

#### Supported Platforms


- Learn about the SQL Server versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for SQL Server on our **Capabilities for SQL Server** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-sql-server), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-sql-server), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-sql-server), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-sql-server), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-sql-server), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-sql-server)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported SQL Server data types and their mapping, see [Data Type Mapping for SQL Server](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sql-server).

- 
Understand the character encodings HVR supports for SQL Server on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#sqlserver) page.



> **Note:** 
Fivetran provides additional solutions for replicating data from SQL Server. For more information, see section [SQL Server](https://fivetran.com/docs/connectors/databases/sql-server) in Databases.


## Supported Editions


HVR supports the following SQL Server editions:

- SQL Server Developer Edition
- SQL Server Enterprise Edition
- SQL Server Standard Edition


## Connecting Hub to a Remote SQL Server Database


For connecting HVR Hub machine to a remote SQL Server database, the following three methods are available:

> **Note:** 
All of the following connection methods are applicable when SQL Server is used as source and as target. Specifically, HVR's log-based capture can get changes from a database without HVR's executables being physically installed on the source machine.


- 
**Method 1:** Connect the HVR Hub directly to the SQL Server database (available on a remote machine) using the SQL Server protocol - Tabular Data Stream (TDS).

> **Important:** 
To use this connection method, the [Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16) must be installed on the machine from which the HVR Hub will connect to the SQL Server database. For information about the supported ODBC driver versions, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the [download page](https://fivetran.com/dashboard/account/downloads).


- 
**Method 2:** Connect the HVR Hub to an HVR Agent installed on the remote machine containing the SQL Server database using HVR's protocol on a special TCP/IP port number. Then connect the HVR Agent directly to the SQL Server database using the SQL Server protocol - TDS.

> **Note:** 
On Windows, the special TCP/IP port is serviced by a Windows service called [HVR Agent Listener](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener).


This connection method gives the best performance, but is the most intrusive.

- 
**Method 3:** Connect the HVR Hub to an HVR Agent installed on a separate machine using HVR's protocol on a special TCP/IP port number. Then connect the HVR Agent directly to the SQL Server database (available on a different machine) using the SQL Server protocol - TDS. This connection method involves three separate machines - one with the HVR Hub, another with the HVR Agent, and finally the machine containing the SQL Server database.

> **Note:** 
On Windows, the special TCP/IP port is serviced by a Windows service called [HVR Agent Listener](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener).


> **Important:** 
To use this connection method, the [Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16) must be installed on the machine from which the HVR Agent will connect to the SQL Server database. For information about the supported ODBC driver versions, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the [download page](https://fivetran.com/dashboard/account/downloads).


This connection method is useful when connecting from a Linux hub to avoid an (intrusive) installation of HVR on the machine containing the SQL Server database.



## Connecting to Amazon RDS for SQL Server


HVR supports using Amazon RDS for SQL Server as a target, a hub, or for refresh-only workflows. HVR does not support log-based capture from Amazon RDS for SQL Server.

To enable the HVR process to connect to Amazon RDS for SQL Server, you must allow inbound traffic on the database listener port to the system running the HVR process.

- If an HVR Agent is in place, communication must be enabled for the system where the HVR Agent is running.
- When directly connected from an HVR Hub Server, the connection must be allowed for the HVR Hub Server.


If the HVR system connecting to Amazon RDS for SQL Server runs in the same VPC as Amazon RDS for SQL Server, you can use the internal rather than public IP address for the service to allow access. It is recommended to restrict access to only the HVR system that requires access, rather than allowing broader or public access.

The default database listener port that must be opened for a TCP/IP connection is **1433**.

> **Note:** 
The port may have been changed from the default by an administrator.


## SQL Server on Linux


HVR supports SQL Server on Linux as source and as target. The following are required for using HVR with SQL Server running on Linux:

- 
[Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16). For information about the supported ODBC driver versions, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the [download page](https://fivetran.com/dashboard/account/downloads).
ODBC Driver Configuration
> **Important:** 
Since v6.1.5/8, skip step 2 (create symbolic link) and step 3 (verify dynamic dependencies).


- 
Download and install the latest Microsoft ODBC Driver for SQL Server on Linux. For more information, refer to the Microsoft documentation - [Install the Microsoft ODBC driver for SQL Server (Linux)](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server).

- 
Create a symbolic link (symlink) for the ODBC driver. Following is an example for Microsoft ODBC Driver for SQL Server **libmsodbcsql-17.5.so.1.1**:
ln -s  /opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.1.1  $HVR_HOME/lib/libmsodbcsql-17.so

- 
After installing the Microsoft ODBC Driver for SQL Server, it is recommended to verify the dynamic dependencies. For example:
ldd $HVR_HOME/lib/hvr_ms17.so



- 
The HVR database **User** (username for connecting HVR to SQL Server) should have read access to the **.mdf** and **.ldf** files. For this, the **User** should typically be added to the operating system user group **mssql**.



## Character Data and Collation Handling


<b>Since</b> v6.3.5/3

During capture, HVR detects the collation of each CHAR, VARCHAR, and TEXT column individually for SQL Server tables containing mixed collations or character encodings. HVR also retrieves character data in binary format.

During integrate, HVR detects the collation of each character column and inserts character data in binary format to prevent unwanted character conversion or translation by the ODBC driver. This behavior preserves the original character data during replication and helps prevent data corruption between source and target tables.

For versions before 6.3.5/3, HVR considered only the database collation and ignored column-level collations. In environments with mixed column collations, this could result in corrupted character data during replication. For example, if a column used a UTF-8 collation while the database used a WIN-1252 collation, replicating emoji characters could produce corrupted data.

## Related Articles


- [SQL Server as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/sql-server-as-source)
- [Capture from SQL Server using Direct Transaction Log Access](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/sql-server-as-source/capture-from-sql-server-using-direct-transaction-log-access)
- [Capture from SQL Server using Archive Only](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/sql-server-as-source/capture-from-sql-server-using-archive-only)
- [Capture from SQL Server using SQL Access](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/sql-server-as-source/capture-from-sql-server-using-sql-access)
- [Capture from SQL Server using Database Triggers](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/sql-server-as-source/capture-from-sql-server-using-database-triggers)


- [SQL Server as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/sql-server-as-target)
- [Location Connection for SQL Server](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-sql-server)

