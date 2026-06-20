# SQL database in Microsoft Fabric Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements/index.md)

# SQL database in Microsoft Fabric Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using SQL database in Microsoft Fabric for replication.

#### Supported Platforms


- Learn about the SQL database in Microsoft Fabric versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635) and [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630)).


#### Supported Capabilities


- Discover what HVR offers for SQL database in Microsoft Fabric on our **Capabilities for SQL database in Microsoft Fabric** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-sql-database-in-microsoft-fabric) and [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-sql-database-in-microsoft-fabric)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported SQL database in Microsoft Fabric data types and their mapping, see [Data Type Mapping for SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sql-database-in-microsoft-fabric).


## ODBC Connection


<b>Since</b> v6.3.0/6,  v6.3.5/2

Microsoft ODBC Driver for SQL Server must be installed on the machine from which HVR connects to SQL database in Microsoft Fabric.

HVR uses the ODBC driver to connect to, read from, and write to SQL database in Microsoft Fabric. The connection to SQL database in Microsoft Fabric is encrypted by default.

> **Important:** 
For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the [downloads](https://fivetran.com/dashboard/account/downloads) page.



## Authentication Methods


HVR supports the following authentication methods for authenticating to SQL database in Microsoft Fabric.

### Access token


Use this method to authenticate HVR to SQL database in Microsoft Fabric with an OAuth 2.0 access token. The required [connection parameters](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-sql-database-in-microsoft-fabric) are:

- **OAUTH2 ENDPOINT**: OAuth 2.0 token endpoint URL
- **CLIENT ID**: Client ID of the Microsoft Entra application
- **CLIENT SECRET KEY**: Client secret of the Microsoft Entra application


For more information, see [Microsoft documentation for application and service principal authentication](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals).

### Microsoft Entra ID


Use this method to authenticate HVR to SQL database in Microsoft Fabric with Microsoft Entra ID authentication. The required [connection parameters](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-sql-database-in-microsoft-fabric) are:

- **USER**: Microsoft Entra username
- **PASSWORD**: Microsoft Entra user password


## Related Articles


- [SQL database in Microsoft Fabric as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements/sql-database-in-microsoft-fabric-as-target)
- [Repository Database in SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sql-database-in-microsoft-fabric)
- [Location Connection for SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-sql-database-in-microsoft-fabric)

