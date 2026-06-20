# Db2 for i Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-i-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/db2-for-i-requirements/index.md)

# Db2 for i Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Db2 for i for replication.

#### Supported Platforms


- Learn about the Db2 for i versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Db2 for i on our **Capabilities for Db2 for i** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-db2-for-i), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-db2-for-i), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-db2-for-i), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-db2-for-i), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-db2-for-i), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-db2-for-i)).


#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported Db2 for i data types and their mapping, see [Data Type Mapping for Db2 for i](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-db2-for-i).

- 
Understand the character encodings HVR supports for Db2 for i on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#db2fori) page.



> **Note:** 
Fivetran provides additional solutions for replicating data from Db2 for i. For more information, see section [Db2 for i](https://fivetran.com/docs/connectors/databases/hva-db2i) in Databases.


## ODBC Connection


HVR is not installed on the Db2 for i system itself but is instead installed on a Linux or Windows machine, from which it uses ODBC to connect to the Db2 for i system. HVR uses ODBC connection to read and write data to Db2 for i location.

The following are required for HVR to establish an ODBC connection to the Db2 for i system:

- 
**On Linux:**

- IBM i Access Client Solutions ODBC Driver 64-bit
- ODBC driver manager UnixODBC


- 
**On Windows:**

- IBM i Access Client Solutions ODBC Driver




> **Important:** 
The IBM i Access Client Solutions ODBC Driver is available for download from [IBM ESS Website](https://www-304.ibm.com/servers/eserver/ess/ProtectedServlet.wss) (requires user authentication). Choose product-number '5770-SS1', and then choose package 'IBM i Access - Client Solutions' for your platform. For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.


## SSL Connection


<b>Since</b> v6.1.5/9 <b>Since</b> v6.2.0/0

HVR supports SSL connection for Db2 for i on both Linux and Windows.

To enable SSL authentication for a Db2 for i location, select the [**Use SSL**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-db2-for-i) option while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or by [editing the existing location's source and target properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#sourceandtargetproperties) (or define the equivalent location property [**Db2_Use_SSL**](https://fivetran.com/docs/hvr6/property-reference/location-properties#db2usessl)).

### Configuration for Linux


To use SSL with HVR installed on Linux, configure the OpenSSL libraries by creating a symbolic link to the system trust store.

- 
Run the following command to locate your system's trust store:
openssl version -d

This command returns a path, typically **/usr/lib/ssl** or **/etc/ssl**.

- 
Append **/certs** to the path returned by the previous command to locate your system's certificate store.

- 
Create a symbolic link from this directory to **/usr/local/ssl/certs** by executing the following command:
sudo ln -s /usr/lib/ssl/certs /usr/local/ssl/certs



> **Important:** 
For information about the ODBC driver version that supports SSL connection on Linux, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in the **HVR_HOME** directory or the download page.


## Firewall


If a Firewall is configured between the HVR capture machine and the IBM i-series, the following default ports need to be opened in order to be able to connect via ODBC from the capture to the IBM i-series:

 PC Function | Service name i-series | Port non-SSL | SSL Port |
 Server mapper | as-svrmap | 449 | 449 |
 License Management | as-central | 8470 | 9470 |
 RPC/DPC (Remote command) | as-rmtcmd | 8475 | 9475 |
 Sign-On Verification | as-signon | 8476 | 9476 |
 Database Access | as-database | 8471 | 9471 |


> **Important:** 
The port numbers mentioned here are the default port numbers. To verify the default port numbers for the services names, use the command **wrksrvtble** on AS/400 console.


## Related Articles


- [Db2 for i as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-i-requirements/db2-for-i-as-source)
- [Db2 for i as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-i-requirements/db2-for-i-as-target)
- [Location Connection for Db2 for i](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-db2-for-i)

