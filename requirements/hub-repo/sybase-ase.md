# Repository Database in Sybase ASE - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sybase-ase

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sybase-ase/index.md)

# Repository Database in Sybase ASE


`**Since** v6.1.5/4`

Fivetran HVR allows you to create a repository database in Sybase ASE. The **Repository Database** section in **Capabilities** ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635#repositorydatabase), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630#repositorydatabase), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#repositorydatabase), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#repositorydatabase), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#repositorydatabase), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#repositorydatabase)) lists the supported Sybase ASE versions that can be used as a repository database.

## Grants for Repository Database


The following grants are required for the repository database in Sybase ASE:
grant create table to <em>username</em>
grant create procedure to <em>username</em>

## Repository Database Connection


This section describes the details required for connecting to the repository database in Sybase ASE:

 Field | Description | Equivalent Location Property |
 **SYBASE** | Directory path where the Sybase ASE database is installed. | [**Sybase**](https://fivetran.com/docs/hvr6/property-reference/location-properties#sybase) |
 **SYBASE CT LIBRARY** | Directory path where the Sybase Open Client (CT library) is installed. | [**Sybase_CT_Library**](https://fivetran.com/docs/hvr6/property-reference/location-properties#sybasectlibrary) |
 **NODE** | 
Hostname or IP-address of the server on which the Sybase ASE database is running.
This field is enabled only if **NETWORK TRANSPORT SOURCE** is set to **Direct**. | [**Database_Host**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasehost) |
 **PORT** | 
Port number on which the Sybase ASE database server is expecting connections.
 This field is enabled only if **NETWORK TRANSPORT SOURCE** is set to **Direct**. | [**Database_Port**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseport) |
 **DATABASE** | Name of the Sybase ASE database. | [**Database_Name**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasename) |
 **AUTHENTICATION METHOD** | 
Authentication method for connecting HVR to Sybase ASE server.

Available options are:

- **User Name and Password**`default`
- **Kerberos**


> **Important:** 
For more information about using **Kerberos** authentication, see section [Kerberos Authentication](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements#kerberosauthentication) in [Sybase ASE Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements).

 | [**Sybase_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#sybaseauthenticationmethod) |
 **USER** | 
Username for connecting HVR to the Sybase ASE database.
 | [**Database_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseuser) |
 **PASSWORD** | 
Password for the **USER**
 This field is enabled only if the **AUTHENTICATION METHOD** is set to **User Name and Password**. | **[Database_Password](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasepassword)** |
 **SECURITY MECHANISM** | 
Name of the security mechanism that performs security services for this connection. Security mechanism names are defined in the Sybase **libtcl.cfg** configuration file.

If value is not entered in this field, the default mechanism defined in the **libtcl.cfg** file will be used.

This field is enabled only if **AUTHENTICATION METHOD** is set to **Kerberos**. | **[Sybase_**Kerberos_**Security_Mechanism](https://fivetran.com/docs/hvr6/property-reference/location-properties#sybasekerberossecuritymechanism)** |
 **SERVER PRINCIPAL** | 
The Kerberos Service Principal Name (SPN) of the Sybase ASE server.

This field is enabled only if **AUTHENTICATION METHOD** is set to **Kerberos**. | [**Sybase_Kerberos_Server_Principal**](https://fivetran.com/docs/hvr6/property-reference/location-properties#sybasekerberosserverprincipal) |
 **KEY TAB** | 
Directory path where the Kerberos keytab file is located. This keytab file contains the security key for the specified **USER**.

This field is enabled only if **AUTHENTICATION METHOD** is set to **Kerberos**. | [**Sybase_Kerberos_Keytab**](https://fivetran.com/docs/hvr6/property-reference/location-properties#sybasekerberoskeytab) |
 **SECURITY SERVICES** | 
Kerberos security mechanism services. It only defines how the connection behaves.

- **Mutual Client/Server Authentication**: Both HVR and the Sybase server are required to authenticate themselves.
- **Encrypted Connection**: Enables encrypted connection between HVR and the Sybase server.
- **Data Integrity Checking**: Enables data integrity checking.
- **Replay Transmission Detection**: Enables data replay detection.
- **Data Out-Of-Sequence Detection**: Enables out-of-sequence detection.
- **Data Origin Verification**: Enables data origin stamping service.
- **Channel Binding**: Enables channel binding.


The Kerberos security mechanism services options are displayed only if **AUTHENTICATION METHOD** is set to **Kerberos**.
 | **[Sybase_Kerberos_Security_Services](https://fivetran.com/docs/hvr6/property-reference/location-properties#sybasekerberossecurityservices)** |

