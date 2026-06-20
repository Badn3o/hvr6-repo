# Snowflake as Target - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements/snowflake-as-target

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements/snowflake-as-target/index.md)

# Snowflake as Target


Fivetran HVR supports integrating changes into Snowflake location. This section describes the configuration requirements for integrating changes (using [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) and [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)) into Snowflake location. For the list of supported Snowflake versions into which HVR can integrate changes, see [Integrate changes into location](https://fivetran.com/docs/hvr6/capabilities/610#integrate) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

HVR uses the Snowflake ODBC driver to write data into Snowflake during [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method) and [**Row-wise Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#repairrowbyrowgranularity).

The preferred methods for writing data into Snowflake are using [**Burst Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method) and [**Bulk Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity) as they provide better performance. However, it is required to create staging files on a temporary location to perform [**Burst Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method) and [**Bulk Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity). For more information about staging, see section [Staging for Snowflake](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements/snowflake-as-target/staging-for-snowflake).

> **Important:** 
Due to technical limitations, external staging on Azure for Snowflake is not supported in the HVR releases since 6.1.5/3 to 6.1.5/9.


## Grants for Integrate and Refresh


This section lists the grants required for integrating changes into Snowflake.

- 
The user (**Role**) should have permission to read and change replicated tables.
grant all privileges on future tables in database <em>databasename</em> to role <em>rolename</em>;

grant select, insert, update, delete, truncate on future tables in database <em>databasename</em> to role <em>rolename</em>;

- 
The user (**Role**) should have permission to create and drop HVR state tables.

- 
The user (**Role**) should have permission to create and drop tables when [Refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) will be used to create target tables.
grant usage, modify, create table on schema <em>schemaname</em> in database <em>databasename</em> to role <em>rolename</em>;



## Intermediate Directory


This option in the HVR UI allows you to specify a directory path for storing intermediate (temporary) files generated during [Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare). These files are created during both "direct file compare" and "online compare" operations.

This option is displayed in the [location creation](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location#configurecaptureintegrate) dialog when [creating a new location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location), and in the [Source and Target Properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#sourceandtargetproperties) pane on the [Location Details](https://fivetran.com/docs/hvr6/user-interface/locations/location-details) page when editing an existing location.

Using an intermediate directory can enhance performance by ensuring that temporary files are stored in a location optimized for the system's data processing needs.

This setting is particularly relevant for target file locations, as it determines where the intermediate files are placed during the Compare operation. If this option is not enabled, the intermediate files are stored by default in the *integratedir***/_hvr_intermediate** directory, where *integratedir* is the replication **DIRECTORY** ([File_Path](https://fivetran.com/docs/hvr6/property-reference/location-properties#filepath)) defined for the target file location.

> **Note:** 
This option is equivalent to the location property [**Intermediate_Directory**](https://fivetran.com/docs/hvr6/property-reference/location-properties#intermediatedirectory).



### Intermediate Directory is Local


This option indicates that the **Intermediate Directory** will be created on the local drive of the location's server. This option is displayed when you select the **Intermediate Directory** option in the HVR UI. It is selected by default and cannot be modified.

Storing intermediate files locally is crucial for optimizing performance by reducing network latency and avoiding potential permission issues associated with remote storage. It enables HVR to process data more efficiently by leveraging the speed and reliability of local storage. This is particularly beneficial when the HVR Agent has access to ample local storage, allowing it to handle large data volumes without relying on networked storage solutions.

> **Note:** 
This option is equivalent to the location property [**Intermediate_Directory_Is_Local**](https://fivetran.com/docs/hvr6/property-reference/location-properties#intermediatedirectoryislocal).


