# Databricks Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/databricks-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/databricks-requirements/index.md)

# Databricks Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Databricks for replication.

#### Supported Databricks Environments and Services


- 
HVR supports the following Databricks cloud environments:

- [Databricks on AWS](https://docs.databricks.com/aws/en/)
- [Databricks on Azure](https://learn.microsoft.com/en-us/azure/databricks/)
- [Databricks on GCP](https://docs.databricks.com/gcp/en/)


- 
HVR supports [Databricks serverless compute](https://docs.databricks.com/aws/en/compute/serverless/) for SQL warehouses and jobs.



#### Supported Platforms


- Learn about the Databricks versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Databricks on our **Capabilities for Databricks** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-databricks), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-databricks), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-databricks), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-databricks), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-databricks), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-databricks)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Databricks data types and their mapping, see [Data Type Mapping for Databricks](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-databricks).


> **Note:** 
Due to technical limitations, Databricks on Azure is not supported in the HVR releases since 6.1.5/3 to 6.1.5/9.


## ODBC Connection


The Simba Spark ODBC driver must be installed on the machine from which HVR connects to Databricks. For detailed instructions on downloading and installing the driver, refer to the Databricks documentation - [Databricks on AWS](https://docs.databricks.com/en/integrations/odbc/index.html), [Databricks on Azure](https://learn.microsoft.com/en-us/azure/databricks/integrations/odbc/) or [Databricks on GCP](https://docs.gcp.databricks.com/en/integrations/odbc/index.html).

For information about the supported ODBC driver versions, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.

## Related Articles


- [Databricks as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/databricks-requirements/databricks-as-target)
- [Location Connection for Databricks](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-databricks)

