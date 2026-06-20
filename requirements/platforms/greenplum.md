# Greenplum Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/greenplum-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/greenplum-requirements/index.md)

# Greenplum Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using [Greenplum](https://docs.greenplum.org/) for replication.

#### Supported Platforms


- Learn about the Greenplum versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Greenplum on our **Capabilities for Greenplum** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-greenplum), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-greenplum), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-greenplum), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-greenplum), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-greenplum), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-greenplum)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Greenplum data types and their mapping, see [Data Type Mapping for Greenplum](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-greenplum#datatypemappingforgreenplum).

- 
Understand the character encodings HVR supports for Greenplum on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#greenplum) page.



## ODBC Connection


It is not required to install HVR on any of the nodes of the Greenplum cluster. HVR can be installed on a standalone machine from which it connects to the Greenplum cluster. HVR requires the DataDirect Connect XE ODBC driver for Greenplum installed (on the machine from which HVR connects to a Greenplum server).

For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.

## Limitation


- HVR does not support comparing tables with **bytea** data type in Greenplum version 6.


## Related Articles


- [Greenplum as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/greenplum-requirements/greenplum-as-source)
- [Greenplum as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/greenplum-requirements/greenplum-as-target)
- [Staging for Greenplum](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/greenplum-requirements/greenplum-as-target/staging-for-greenplum)


- [Location Connection for Greenplum](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-greenplum)

