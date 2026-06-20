# MariaDB Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/mariadb-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/mariadb-requirements/index.md)

# MariaDB Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using MariaDB for replication.

#### Supported Platforms


- Learn about the MariaDB versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for MariaDB on our **Capabilities for MariaDB** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-mariadb), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-mariadb), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-mariadb), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-mariadb), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-mariadb), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-mariadb)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of supported MariaDB data types and their mapping, see [Data Type Mapping for MariaDB](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-mariadb).


> **Tip:** 
Fivetran provides additional solutions for replicating data from MySQL. For more information, see section [MySQL](https://fivetran.com/docs/connectors/databases/mariadb) in Databases.


## Connecting to Amazon RDS for MariaDB


To enable the HVR capture or integrate process to connect to Amazon RDS for MariaDB, you must allow inbound traffic on the database listener port to the system running the HVR process. If an HVR Agent is in place, then communication must be enabled for the system where the HVR Agent is running. When directly connected from an HVR Hub Server, the connection must be allowed for the HVR Hub Server. If the HVR system connecting to Amazon RDS for MariaDB runs in the same VPC as Amazon RDS for MariaDB, you can use the internal rather than public IP address for the service to allow access. It is recommended to restrict access to only the HVR system that requires access, rather than allowing broader or public access.

The default database listener port that must be opened for TCP/IP connection is **3306**.

> **Note:** 
The port may have been changed from the default by an administrator.


## Using Authentication Plugins


HVR supports using MariaDB authentication plugins for user authentication. For more information about authentication plugins, refer to the [Authentication Plugins](https://mariadb.com/kb/en/authentication-plugins/) section in the MariaDB documentation. To use authentication plugins installed in a custom directory, you must define the environment variable **MARIADB_PLUGIN_DIR**. You can define this environment variable using the action [Environment](https://fivetran.com/docs/hvr6/action-reference#environment) with parameters [Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)=MARIADB_PLUGIN_DIR and [Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)=*path_to_directory*.

## Related Articles


- [MariaDB as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/mariadb-requirements/mariadb-as-source)
- [MariaDB as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/mariadb-requirements/mariadb-as-target)
- [Staging for MariaDB](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/mariadb-requirements/mariadb-as-target/staging-for-mariadb)


- [Location Connection for MariaDB](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-mariadb)

