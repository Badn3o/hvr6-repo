# Azure Synapse Analytics Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-synapse-analytics-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/azure-synapse-analytics-requirements/index.md)

# Azure Synapse Analytics Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Azure Synapse Analytics (formerly Azure SQL Data Warehouse) for replication. Azure Synapse Analytics is the Platform as a Service (PaaS) data warehouse and big data analytics of Microsoft's Azure Cloud Platform. HVR supports Azure Synapse Analytics through its regular SQL Server driver.

#### Supported Platforms


- Learn about the Azure Synapse Analytics versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Azure Synapse Analytics on our **Capabilities for Azure Synapse Analytics** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-azure-synapse-analytics), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-azure-synapse-analytics), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-azure-synapse-analytics), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-azure-synapse-analytics), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-azure-synapse-analytics), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-azure-synapse-analytics)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Azure Synapse Analytics data types and their mapping, see [Data Type Mapping for Azure Synapse Analytics](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-azure-synapse-analytics).


## ODBC Connection


Microsoft [SQL Server Native Client](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/sql-server-native-client?view=sql-server-2017) must be installed on the machine from which HVR connects to Azure Synapse. For more information about [downloading](https://www.microsoft.com/en-us/download/details.aspx?id=50402) and [installing SQL Server Native Client](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/applications/installing-sql-server-native-client?view=sql-server-2017), refer to [Microsoft documentation](https://docs.microsoft.com/).

For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.

## Related Articles


- [Azure Synapse Analytics as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-synapse-analytics-requirements/azure-synapse-analytics-as-target)
- [Location Connection for Azure Synapse Analytics](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-synapse-analytics)

