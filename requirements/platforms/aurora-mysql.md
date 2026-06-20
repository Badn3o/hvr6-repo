# Aurora MySQL Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/aurora-mysql-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/aurora-mysql-requirements/index.md)

# Aurora MySQL Requirements


#### Supported Platforms


- Learn about the Aurora MySQL versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Aurora MySQL on our **Capabilities for Aurora MySQL** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-aurora-mysql), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-aurora-mysql), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-aurora-mysql), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-aurora-mysql), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-aurora-mysql), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-aurora-mysql)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of supported Aurora MySQL data types and their mapping, see [Data Type Mapping for Aurora MySQL](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-aurora-mysql).


> **Tip:** 
Fivetran provides additional solutions for replicating data from MySQL. For more information, see section [MySQL](https://fivetran.com/docs/connectors/databases/mysql) in Databases.


## Connecting to Aurora MySQL


To enable the HVR capture or integrate process to connect to Aurora MySQL, you must allow inbound traffic on the database listener port to the system running the HVR process. If an HVR Agent is in place, then communication must be enabled for the system where the HVR Agent is running. When directly connected from an HVR Hub Server, the connection must be allowed for the HVR Hub Server. If the HVR system connecting to Aurora MySQL runs in the same VPC as Aurora MySQL, you can use the internal rather than public IP address for the service to allow access. It is recommended to restrict access to only the HVR system that requires access, rather than allowing broader or public access.

The default database listener port that must be opened for TCP/IP connection is **3306**.

> **Note:** 
The port may have been changed from the default by an administrator.


## Related Articles


- [Aurora MySQL as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/aurora-mysql-requirements/aurora-mysql-as-source)
- [Aurora MySQL as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/aurora-mysql-requirements/aurora-mysql-as-target)
- [Staging for Aurora MySQL](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/aurora-mysql-requirements/aurora-mysql-as-target/staging-for-aurora-mysql)


- [Location Connection for Aurora MySQL](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-aurora-mysql)

