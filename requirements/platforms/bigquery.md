# Google BigQuery Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-bigquery-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/google-bigquery-requirements/index.md)

# Google BigQuery Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Google BigQuery for replication.

#### Supported Platforms


- Learn about the Google BigQuery versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Google BigQuery on our **Capabilities for Google BigQuery** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-bigquery), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-bigquery), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-bigquery), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-bigquery), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-bigquery), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-bigquery)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of supported Google BigQuery data types and their mapping, see [Data Type Mapping for Google BigQuery](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-google-bigquery).

- 
Understand the character encodings HVR supports for PostgreSQL on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#googlebigquery) page.



## ODBC Connection


[Simba ODBC driver for Google BigQuery](https://cloud.google.com/bigquery/providers/simba-drivers) must be installed on the machine from which HVR connects to Google BigQuery.

HVR uses the Simba ODBC driver for Google BigQuery to connect and write data into BigQuery during [**integration**](https://fivetran.com/docs/hvr6/action-reference/integrate#method) and [**refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

> **Important:** 
For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.


## Related Articles


- [Google BigQuery as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-bigquery-requirements/google-bigquery-as-source)
- [Google BigQuery as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-bigquery-requirements/google-bigquery-as-target)
- [Staging for BigQuery](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-bigquery-requirements/google-bigquery-as-target/staging-for-bigquery)


- [Location Connection for Google BigQuery](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-google-bigquery)

