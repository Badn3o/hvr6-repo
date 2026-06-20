# Azure SQL Managed Instance Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-sql-managed-instance-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/azure-sql-managed-instance-requirements/index.md)

# Azure SQL Managed Instance Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Azure SQL Managed Instance for replication.

#### Supported Platforms


- Learn about the Azure SQL Managed Instance versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Azure SQL Managed Instance on our **Capabilities for Azure SQL Managed Instance** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-azure-sql-managed-instance), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-azure-sql-managed-instance), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-azure-sql-managed-instance), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-azure-sql-managed-instance), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-azure-sql-managed-instance), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-azure-sql-managed-instance)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page.


> **Note:** 
Fivetran provides additional solutions for replicating data from Azure SQL Managed Instance. For more information, see section [SQL Server](https://fivetran.com/docs/connectors/databases/sql-server) in Databases.


## ODBC Connection


Microsoft [SQL Server Native Client](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/sql-server-native-client?view=sql-server-2017) ODBC driver must be installed on the machine from which HVR connects to Azure SQL Managed Instance. For more information about [downloading](https://www.microsoft.com/en-us/download/details.aspx?id=50402) and [installing SQL Server Native Client](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/applications/installing-sql-server-native-client?view=sql-server-2017), refer to [Microsoft documentation](https://docs.microsoft.com/).

HVR uses the SQL Server Native Client ODBC driver to connect, read, and write data into Azure SQL Managed Instance during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture), [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), and [**Row-wise Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#repairrowbyrowgranularity). The connection to the Azure SQL Managed Instance is encrypted by default (HVR will always add ENCRYPT=YES to the connection string for any Azure SQL connection).

> **Important:** 
For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.


## Authentication Methods


HVR supports the following authentication methods for connecting to Azure SQL Managed Instance databases:

- 
**User and Password**: Use SQL authentication with a username and password to connect to Azure SQL Managed Instance. The location properties required for this authentication method are [**Database_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseuser) and [**Database_Password**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasepassword).

- 
**Access Token**: Use OAuth 2.0 to obtain an access token from Azure Entra ID. HVR then uses this token to authenticate with Azure SQL Managed Instance. The location properties required for this authentication are [**Azure_OAuth2_Endpoint**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2endpoint), [**Azure_OAuth2_Client_Id**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2clientid), and [**Azure_OAuth2_Client_Secret**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2clientsecret).

This method is useful for applications that need to authenticate programmatically. For more information, refer to [Application and service principal authentication](https://docs.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-service-principal-tutorial) in Microsoft's documentation.

> **Note:** 
This method is only available in the HVR UI as of 6.2.5/10. For earlier versions, you can define it using the CLI or REST API.


- 
**Azure Active Directory**: Use Azure AD / Microsoft Entra ID authentication with a username and password to connect to Azure SQL Managed Instance. The location properties required for this authentication method are [**Azure_OAuth2_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2user) and [**Azure_OAuth2_Password**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2password).

> **Note:** 
This method is only available in the HVR UI as of 6.2.5/10. For earlier versions, you can define it using the CLI or REST API.




## Related Articles


- [Azure SQL Managed Instance as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-sql-managed-instance-requirements/azure-sql-managed-instance-as-source)
- [Azure SQL Managed Instance as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-sql-managed-instance-requirements/azure-sql-managed-instance-as-target)
- [Location Connection for Azure SQL Managed Instance](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-sql-managed-instance)

