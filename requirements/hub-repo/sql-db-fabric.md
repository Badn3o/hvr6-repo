# Repository Database in SQL database in Microsoft Fabric - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sql-database-in-microsoft-fabric

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sql-database-in-microsoft-fabric/index.md)

# Repository Database in SQL database in Microsoft Fabric


Fivetran HVR allows you to create a repository database in SQL database in Microsoft Fabric.

It is recommended to create a new database (schema) for HVR repository. If an existing database is to be used for HVR repository, then the HVR [repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables) can be separated by creating a new database schema and associating it with HVR's user as follows:
create schema <em>schemaname</em>;

## Grants for Repository Database


The following grants are required for the repository database user in SQL database in Microsoft Fabric:
grant create table to <em>username</em>;
grant create procedure to <em>username</em>;
grant select, insert, delete, update on schema::<em>schemaname</em> to <em>username</em>;
grant control on schema::<em>schemaname</em> to <em>username</em>;
alter user <em>username</em> with default_schema=<em>schemaname</em>;

## Repository Database Connection


This section describes the details required for connecting to the repository database in SQL database in Microsoft Fabric:

 Field | Description | Equivalent Location Property |
 **MICROSOFT FABRIC SQL DATABASE ENDPOINT** | 
SQL connection endpoint of the SQL database in Microsoft Fabric. For example, `tcp:*servername*.database.fabric.microsoft.com,1433`.
 | [**MS_Fabric_Server**](https://fivetran.com/docs/hvr6/property-reference/location-properties#msfabricserver) |
 **DATABASE** | Name of the SQL database in Microsoft Fabric. | [**Database_Name**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasename) |
 **AUTHENTICATION METHOD** | 
Authentication method for connecting HVR to SQL database in Microsoft Fabric.

Available options are:

- 
**Access Token**`**Since** v6.3.0/6`: Authenticate using an OAuth 2.0 access token obtained from Microsoft Entra ID.

- 
**Microsoft Entra ID**`**Since** v6.3.0/6`: Authenticate using a Microsoft Entra username and password.



For more information about these options, see the [Authentication Methods](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements#authenticationmethods) section.
 | [**MS_Fabric_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#msfabricauthenticationmethod) |
 **OAUTH2 ENDPOINT** | 
URL used to obtain the bearer token using client credentials.

Use the OAuth 2.0 endpoint. The URL must include **v2.0**. For example, `https://login.microsoftonline.com/*tenant*/oauth2/**v2.0**/token`

This field is available only if the **AUTHENTICATION METHOD** is set to **Access Token**. | [**MS_Fabric_OAuth2_Endpoint**](https://fivetran.com/docs/hvr6/property-reference/location-properties#msfabricoauth2endpoint) |
 **CLIENT ID** | 
Client ID used to obtain the access token.

This field is available only if the **AUTHENTICATION METHOD** is set to **Access Token**. | [**MS_Fabric_OAuth2_Client_Id**](https://fivetran.com/docs/hvr6/property-reference/location-properties#msfabricoauth2clientid) |
 **CLIENT SECRET KEY** | 
Client secret associated with the **CLIENT ID**.

This field is available only if the **AUTHENTICATION METHOD** is set to **Access Token**. | [**MS_Fabric_OAuth2_Client_Secret**](https://fivetran.com/docs/hvr6/property-reference/location-properties#msfabricoauth2clientsecret) |
 **USER** | 
Microsoft Entra username used to connect to SQL database in Microsoft Fabric.

This field is available only if the **AUTHENTICATION METHOD** is set to **Microsoft Entra ID**. | [**MS_Fabric_Entra_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#msfabricentrauser) |
 **PASSWORD** | 
Password for the Microsoft Entra **USER**.

This field is available only if the **AUTHENTICATION METHOD** is set to **Microsoft Entra ID**. | [**MS_Fabric_Entra_Password**](https://fivetran.com/docs/hvr6/property-reference/location-properties#msfabricentrapassword) |


### Advanced Settings


 Field | Description | Equivalent Location Property |
 **LINUX / UNIX ODBC DRIVER MANAGER LIBRARY PATH**
 | 
Directory path where the ODBC Driver Manager Library is installed. This field applies only to Linux/Unix operating systems.

For a default installation, the ODBC Driver Manager Library is available at **/usr/lib64** and does not need to be specified. However, when UnixODBC is installed in a non-default location, for example **/opt/unixodbc**, the value for this field would be **/opt/unixodbc/lib**. | [**ODBC_DM_Lib_Path**](https://fivetran.com/docs/hvr6/property-reference/location-properties#odbcdmlibpath) |
 **ODBCSYSINI** | 
Directory path where the **odbc.ini** and **odbcinst.ini** files are located. This field applies only to Linux/Unix operating systems.

For a default installation, these files are available at **/etc** directory and do not need to be specified using this field. However, when UnixODBC is installed in a non-default location, for example **/opt/unixodbc**, the value for this field would be **/opt/unixodbc/etc**. | [**ODBC_Sysini**](https://fivetran.com/docs/hvr6/property-reference/location-properties#odbcsysini) |
 **ODBC DRIVER** | Name of the installed, user-defined ODBC driver used for connecting HVR to SQL database in Microsoft Fabric. | [**ODBC_Driver**](https://fivetran.com/docs/hvr6/property-reference/location-properties#odbcdriver) |

