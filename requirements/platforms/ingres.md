# Ingres Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/ingres-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/ingres-requirements/index.md)

# Ingres Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Ingres for replication.

#### Supported Platforms


- Learn about the Ingres versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Ingres on our **Capabilities for Ingres** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-ingres), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-ingres), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-ingres), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-ingres), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-ingres), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-ingres)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of supported Ingres data types and their mapping, see [Data Type Mapping for Ingres](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-ingres)

- 
Understand the character encodings HVR supports for Ingres on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#ingres) page.



## Access Privileges


This section describes the access privileges required for capturing or integrating changes into an Ingres location.

For an Ingres database location, each account used by HVR must have permission to use Ingres. Typically, HVR connects to database locations as the owner of that database. This means that either HVR is already running as the owner of the database, or it is running as a user with Ingres **Security Privilege**. HVR can also connect to a database location as a user who is not the database's owner, although the [**Row-wise Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#repairrowbyrowgranularity) into such a database is not supported if database rules are defined on the target tables.

**Accessdb permission screen:**



**DBA permission screen:**



## Related Articles


- [Ingres as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/ingres-requirements/ingres-as-source)
- [Ingres as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/ingres-requirements/ingres-as-target)
- [Location Connection for Ingres](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-ingres)

