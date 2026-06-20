# SAP HANA Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements/index.md)

# SAP HANA Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using SAP HANA for replication.

#### Supported Platforms


- Learn about the SAP HANA versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Redshift on our **Capabilities for SAP HANA** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-sap-hana), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-sap-hana), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-sap-hana), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-sap-hana), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-sap-hana), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-sap-hana)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported SAP HANA data types and their mapping, see [Data Type Mapping for SAP HANA](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sap-hana#datatypemappingforsaphana).

- 
Understand the character encodings HVR supports for SAP HANA on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#saphana) page.



> **Note:** 
Fivetran provides additional solutions for replicating data from SAP database. For more information, see section [SAP](https://fivetran.com/docs/connectors/databases/sap) in Databases.


## ODBC Connection


HVR requires the HANA client (which contains the HANA ODBC driver) to be installed on the machine from which HVR connects to HANA. HVR uses the HANA ODBC driver to connect, read, and write data to HANA. For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **hvr_home** directory or the download page.

HVR does not support integrating changes captured from HANA into databases where the distribution key cannot be updated (e.g. Greenplum, Azure Synapse Analytics).

## Connecting to Remote HANA Location from Hub


HVR allows you to connect from a hub machine to a remote HANA database by using any of the following two methods:

- Connect to an HVR installation running on the HANA database machine using HVR's protocol on a special TCP port number (e.g. 4343). This option must be used for log-based capture from HANA.
- Use ODBC to connect directly to a HANA database remotely. In this case no additional software is required to be installed on the HANA database server itself. This option cannot be used for log-based capture from HANA database.


## Upgrading HANA Database


When upgrading a HANA database (e.g. from HANA 2.0 SPS 04 to HANA 2.0 SPS 05), HVR may fail with the 'invalid column name' DBMS error.

The solution is to recreate all the views in the **_HVR** schema by running the **HVR_HOME/dbms/hana/hvrhanaviews.sql** script after the upgrade. The script must be run by the **SYSTEM** user.

## Notes for Migrating from HVR 5.x


In HVR, the name of the views in the **_HVR** schema has changed, so the views with new names should be created. This can be done by executing the **hvrhanaviews.sql** script from the **HVR_HOME/dbms/hana** directory.

The 'old' views from HVR5 can then be dropped manually, unless both HVR and HVR5 need to be used simultaneously.

## Related Articles


- [SAP HANA as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements/sap-hana-as-source)
- [SAP HANA as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements/sap-hana-as-target)
- [Staging for SAP HANA](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements/sap-hana-as-target/staging-for-sap-hana)


- [Location Connection for SAP HANA](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-sap-hana)

