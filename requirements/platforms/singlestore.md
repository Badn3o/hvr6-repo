# SingleStore Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/singlestore-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/singlestore-requirements/index.md)

# SingleStore Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using SingleStore (formerly MemSQL) for replication.

#### Supported Platforms


- Learn about the SingleStore versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for SingleStore on our **Capabilities for SingleStore** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-singlestore#capabilitiesforsinglestore), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-singlestore#capabilitiesforsinglestore), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-singlestore#capabilitiesforsinglestore), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-singlestore#capabilitiesforsinglestore), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-singlestore#capabilitiesforsinglestore), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-singlestore#capabilitiesforsinglestore)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported SingleStore data types and their mapping, see [Data Type Mapping for SingleStore](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-singlestore).

- 
Understand the character encodings HVR supports for SingleStore on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#singlestore) page.



## SingleStore Server Time Zone


To use the **timestamp** data type in SingleStore database, the SingleStore server's time zone must be set to **UTC** or **+00:00** using the **[default_time_zone](https://docs.singlestore.com/v7.1/guides/cluster-management/maintain-your-cluster/setting-the-time-zone/setting-the-time-zone/#setting-the-time-zone-in-singlestore-db)** configuration parameter. For more information about setting the time zone, refer to [Setting the Time Zone](https://docs.singlestore.com/v7.1/guides/cluster-management/maintain-your-cluster/setting-the-time-zone/setting-the-time-zone/#setting-the-time-zone-on-the-host-linux-os) in [SingleStore documentation](https://docs.singlestore.com/).

For example, to set the time zone to **UTC** on a host, run the command:
sdb-admin update-config --key default_time_zone --value "+00:00" --all

> **Note:** 
While updating a time zone on a host, it is required to update it identically on all hosts in the cluster and then the cluster must be restarted.


## Using Authentication Plugins


HVR supports using MariaDB authentication plugins for user authentication. For more information about authentication plugins, refer to the [Authentication Plugins](https://mariadb.com/kb/en/authentication-plugins/) section in the MariaDB documentation. To use authentication plugins installed in a custom directory, you must define the environment variable **MARIADB_PLUGIN_DIR**. You can define this environment variable using the action [Environment](https://fivetran.com/docs/hvr6/action-reference#environment) with parameters [Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)=MARIADB_PLUGIN_DIR and [Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)=*path_to_directory*.

## Related Articles


- 
[SingleStore as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/singlestore-requirements/singlestore-as-source)

- 
[SingleStore as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/singlestore-requirements/singlestore-as-target)

- [Staging for SingleStore](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/singlestore-requirements/singlestore-as-target/staging-for-singlestore)


- 
[Location Connection for SingleStore](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-singlestore)


