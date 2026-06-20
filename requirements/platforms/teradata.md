# Teradata Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/teradata-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/teradata-requirements/index.md)

# Teradata Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Teradata (Database or Vantage) for replication.

#### Supported Platforms


- Learn about the Teradata versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Teradata on our **Capabilities for Teradata** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-teradata), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-teradata), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-teradata), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-teradata), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-teradata), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-teradata)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Teradata data types and their mapping, see [Data Type Mapping for Teradata](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-teradata).

- 
Understand the character encodings HVR supports for Teradata on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#teradata) page.



## ODBC Connection


HVR uses ODBC connection to the Teradata server for which it requires the Teradata ODBC driver installed on the machine from which it connects to the Teradata server. For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.

HVR also requires Teradata Parallel Transporter(TPT) packages to perform [**Bulk Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity).

Teradata ODBC driver and TPT packages can be installed using Teradata Tools and Utilities (TTU) package. TTU 16.10 is available for [Linux](https://downloads.teradata.com/download/tools/teradata-tools-and-utilities-linux-installation-package-0) and [Windows](https://downloads.teradata.com/download/tools/teradata-tools-and-utilities-windows-installation-package) on Teradata download page, and TTU 15.00 is available for download from [Teradata Support Portal](http://access.teradata.com/) (requires user authentication).

The following action definitions are required for TTU to find the correct message files:

 Group | Table | Action | Parameter(s) | Annotation |
 Teradata | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=*NLSPATH* | 
 |
 Teradata | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | **[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)**=**"/opt/teradata/client/***teradata_version***/odbc_64/msg/%N:/opt/teradata/client/***teradata_version***/tbuild/msg/%"** | For Teradata 15.00 |
 Teradata | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | ******[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)**="/opt/teradata/client/*****teradata_version*****/odbc_64/msg/%N:/opt/teradata/client/*****teradata_version*****/msg/%N"**** | For Teradata 16.10 and higher |


## Related Articles


- [Teradata as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/teradata-requirements/teradata-as-source)
- [Teradata as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/teradata-requirements/teradata-as-target)
- [Location Connection for Teradata](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-teradata)

