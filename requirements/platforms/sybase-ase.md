# Sybase ASE Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements/index.md)

# Sybase ASE Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Sybase Adaptive Server Enterprise (ASE) for replication.

#### Supported Platforms


- Learn about the Sybase ASE versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Sybase ASE on our **Capabilities for Sybase ASE** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-sybase-ase), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-sybase-ase), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-sybase-ase), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-sybase-ase), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-sybase-ase), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-sybase-ase)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Sybase ASE data types and their mapping, see [Data Type Mapping for Sybase ASE](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sybase-ase).

- 
Understand the character encodings HVR supports for Sybase ASE on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#sybasease) page.



## Supported Editions


HVR supports the following Sybase ASE editions:

- Developer Edition
- Enterprise Edition
- Express Edition


## Kerberos Authentication


Before you configure HVR for Kerberos authentication with Sybase ASE, refer to the [Sybase ASE documentation](https://help.sap.com/viewer/2705a3b1e3df4514ab089cfedf87750d/16.0.4.0/en-US/a926b8dabc2b10148f05924e5890f89d.html) for information about how to configure Kerberos for Sybase ASE.

HVR supports two ways for Kerberos authentication:

- 
Accessing the kerberized Sybase ASE server with the **User** and **Key Tab** parameters supplied. In this case, HVR will run **kinit** to authenticate itself. To use a **keytab** file with HVR, enter the details in the **User** and **Key Tab** fields of the **Location Connection** dialog.

Additionally, the following action must be defined for a Sybase ASE location:

 Group | Table | Action | Parameter(s) |
 Sybase ASE | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=**KRB5_CONFIG****[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)**=*full path to the krb5.conf file* |


- 
Accessing the kerberized Sybase ASE server without supplying the **User** and **Key Tab** parameters. In this case, the [**HVR Agent Listener**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener) (in case of a remote HVR Agent connecting to Sybase ASE) or the [**Scheduler**](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) (in case of a local HVR connecting to Sybase ASE) should be started from an already Kerberos-authenticated environment.



## Related Articles


- [Sybase ASE as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements/sybase-ase-as-source)
- [Sybase ASE as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements/sybase-ase-as-target)
- [Location Connection for Sybase ASE](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-sybase-ase)

