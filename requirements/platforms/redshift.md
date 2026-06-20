# Redshift Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/redshift-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/redshift-requirements/index.md)

# Redshift Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using [Amazon Redshift](https://docs.aws.amazon.com/redshift/) for replication.

#### Supported Platforms


- Learn about the Redshift versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Redshift on our **Capabilities for Redshift** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-redshift#capabilitiesforredshift), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-redshift#capabilitiesforredshift), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-redshift#capabilitiesforredshift), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-redshift#capabilitiesforredshift), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-redshift#capabilitiesforredshift), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-redshift#capabilitiesforredshift)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Redshift data types and their mapping, see [Data Type Mapping for Redshift](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-redshift#datatypemappingforredshift).

- 
Understand the character encodings HVR supports for Redshift on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#redshift) page.



## ODBC Connection


HVR uses ODBC connection to the Amazon Redshift clusters. The Amazon Redshift ODBC driver must be installed on the machine from which HVR connects to the Amazon Redshift clusters. For more information about downloading and installing Amazon Redshift ODBC driver, refer to [AWS documentation](http://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html). On Linux, HVR additionally requires unixODBC. For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.

## Related Articles


- [Redshift as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/redshift-requirements/redshift-as-target)
- [Staging for Redshift](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/redshift-requirements/redshift-as-target/staging-for-redshift)


- [Location Connection for Redshift](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-redshift)

