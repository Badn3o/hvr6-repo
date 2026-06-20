# Azure SQL Database Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-sql-database-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/azure-sql-database-requirements/index.md)

# Azure SQL Database Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Azure SQL Database for replication. Azure SQL Database is the Platform as a Service (PaaS) database of Microsoft's Azure Cloud Platform.

#### Supported Platforms


- Learn about the Azure SQL Database versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Azure SQL Database on our **Capabilities for Azure SQL Database** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-azure-sql-database), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-azure-sql-database), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-azure-sql-database), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-azure-sql-database), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-azure-sql-database), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-azure-sql-database)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of supported Azure SQL Database data types and their mapping, see [Data Type Mapping for Azure SQL Database](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-azure-sql-database).


> **Tip:** 
Fivetran provides additional solutions for replicating data from Azure SQL Database. For more information, see section [SQL Server](https://fivetran.com/docs/connectors/databases/sql-server) in Databases.


## ODBC Connection


Microsoft [SQL Server Native Client](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/sql-server-native-client?view=sql-server-2017) ODBC driver must be installed on the machine from which HVR connects to Azure SQL Database. For more information about [downloading](https://www.microsoft.com/en-us/download/details.aspx?id=50402) and [installing SQL Server Native Client](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/applications/installing-sql-server-native-client?view=sql-server-2017), refer to [Microsoft documentation](https://docs.microsoft.com/).

HVR uses the SQL Server Native Client ODBC driver to connect, read, and write data into Azure SQL Database during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture), [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), and [**Row-wise Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#repairrowbyrowgranularity). The connection to the Azure SQL Database is encrypted by default (HVR will always add ENCRYPT=YES to the connection string for any Azure SQL connection).

> **Important:** 
For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the [downloads](https://fivetran.com/dashboard/account/downloads) page.


## Firewall Configuration


The Azure SQL Database server has a firewall setting that prevents incoming connections by default. However, this can be configured/changed under **Database server/Show firewall settings**. To allow access to the Azure services, when connecting from an Azure VM (through an agent), set option **Allow access to Azure services** to **ON**.

When connecting directly from an on-premises hub, add the HVR Hub Server's IP address to the allowed range. For more information about adding your server to the allowed IP address list, refer to the [Azure SQL Database documentation](https://docs.microsoft.com/en-us/azure/azure-sql/database/firewall-configure#create-and-manage-ip-firewall-rules).



## Authentication Methods


HVR supports the following authentication methods for connecting to Azure SQL database:

- 
**SQL authentication (Username and Password)**: This method uses SQL authentication to connect to Azure SQL Database. The [connection parameters](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-sql-database) required for this authentication method are:

- **USER**: User name and host name of the Azure SQL Database server.
- **PASSWORD**: The password for the SQL Server account.


- 
**Service-to-Service (Access Token)**: This method is used if an application needs to directly authenticate itself with Azure SQL Database using OAuth 2.0. The [connection parameters](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-sql-database) required for this authentication method are:

- **OAUTH2 ENDPOINT**: The OAuth 2.0 token endpoint URL.
- **CLIENT ID**: The client ID of the Azure Entra ID application.
- **CLIENT SECRET KEY**: The client secret of the Azure application.


This method is useful for applications that need to authenticate programmatically. For more information on service-to-service authentication, refer to [Application and service principal authentication](https://docs.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-service-principal-tutorial) in Microsoft's documentation.

- 
**Microsoft Entra ID (Azure Active Directory)**: This method uses Azure Active Directory (Azure AD / Azure Entra ID) authentication to connect to Azure SQL Database. The connection parameters required for this authentication method are:

- [**Azure_OAuth2_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2user): The Azure AD username.
- [**Azure_OAuth2_Password**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2password): The Azure AD user's password.




## Related Articles


- [Azure SQL Database as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-sql-database-requirements/azure-sql-database-as-source)
- [Azure SQL Database as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-sql-database-requirements/azure-sql-database-as-target)
- [Location Connection for Azure SQL Database](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-sql-database)

