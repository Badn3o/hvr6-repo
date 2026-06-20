# Snowflake Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements/index.md)

# Snowflake Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using [Snowflake](https://docs.snowflake.com/en/) for replication.

#### Supported Platforms


- Learn about the Snowflake versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Snowflake on our **Capabilities for Snowflake** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-snowflake), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-snowflake), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-snowflake), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-snowflake), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-snowflake), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-snowflake)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Snowflake data types and their mapping, see [Data Type Mapping for Snowflake](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-snowflake).

- 
Understand the character encodings HVR supports for Snowflake on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#snowflake) page.



> **Important:** 
Due to technical limitations, external staging on Azure for Snowflake is not supported in the HVR releases since 6.1.5/3 to 6.1.5/9.


## ODBC Connection


HVR requires that the Snowflake ODBC driver is installed on the machine from which HVR connects to Snowflake. For more information on downloading and installing Snowflake ODBC driver, see [Snowflake Documentation](https://docs.snowflake.net/). For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.

> **Important:** 
After installing the Snowflake ODBC driver, configure the **LogLevel** configuration parameter as specified in [ODBC Configuration and Connection Parameters](https://docs.snowflake.net/manuals/user-guide/odbc-parameters.html) of the [Snowflake Documentation](https://docs.snowflake.net/).


## Snowflake Authentication


HVR supports both username/password and certificate-based authentication for **Snowflake**.

For certificate-based authentication, **Snowflake** requires a **Key Pair**, which includes a private key ([**Database_Client_Private_Key**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseclientprivatekey)) and password ([**Database_Client_Private_Key_Password**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseclientprivatekeypassword)). Steps to create a **Key Pair** are described in the [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).

## Related Articles


- [Snowflake as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements/snowflake-as-source)
- [Snowflake as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements/snowflake-as-target)
- [Staging for Snowflake](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements/snowflake-as-target/staging-for-snowflake)


- [Location Connection for Snowflake](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-snowflake)

