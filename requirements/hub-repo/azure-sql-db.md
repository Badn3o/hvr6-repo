# Repository Database in Azure SQL Database - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-azure-sql-database

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-azure-sql-database/index.md)

# Repository Database in Azure SQL Database


Fivetran HVR allows you to create a repository database in Azure SQL Database.

It is recommended to create a new database (schema) for HVR repository. If an existing database is to be used for HVR repository, then the HVR [repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables) can be separated by creating a new database schema and associating it with HVR's user as follows:
create schema <em>schemaname</em>;

## Grants for Repository Database


The following grants are required for the repository database user in Azure SQL Database:
grant create table to <em>username</em>;
grant create procedure to <em>username</em>;
grant select, insert, delete, update on schema::<em>schemaname</em> to <em>username</em>;
grant control on schema::<em>schemaname</em> to <em>username</em>;
alter user <em>username</em> with default_schema=<em>schemaname</em>;

## Repository Database Connection


This section describes the details required for connecting to the repository database in Azure SQL Database:

 Field | Description | Equivalent Hub Server Property |
 **SERVER** | 
Fully qualified domain name (FQDN) of the Azure SQL Database.

Example: **cbiz2nhmpv.database.windows.net** | [**SqlServer_Server**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#sqlserverserver) |
 **DATABASE** | 
Name of the database in Azure SQL Database.

Example: **mytestdb** | [**Database_Name**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#databasename) |
 **AUTHENTICATION METHOD** | 
Authentication method for connecting HVR to Azure SQL database.

Available options are:

- 
**Access Token**`**Since** v6.1.0/4`: Authenticate using the Azure SQL access token.

- 
**User and Password**: Authenticate using the username and password.

- 
**Microsoft Entra ID**`**Since** v6.1.0/5`: Authenticate using Microsoft Entra ID (formerly Azure Active Directory).


 | **[SqlServer_Authentication_Method](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#sqlserverauthenticationmethod)** |
 **OAUTH2 ENDPOINT** | 
URL used for obtaining the bearer token with credential token.

Ensure that you are using the OAuth 2.0 endpoint. The URL path should include **v2.0**. The format for the endpoint URL is `https://login.microsoftonline.com/*tenant*/oauth2/**v2.0**/token`

This field is available only if the **AUTHENTICATION METHOD** is set to **Access Token**. | [**Azure_OAuth2_Endpoint**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#azureoauth2endpoint) |
 **CLIENT ID** | 
Client ID used to obtain Microsoft Entra ID (formerly Azure Active Directory) access token.

This field is available only if the **AUTHENTICATION METHOD** is set to **Access Token**. | [**Azure_OAuth2_Client_Id**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#azureoauth2clientid) |
 **CLIENT SECRET KEY** | 
Secret key of the ****CLIENT ID****.

This field is available only if the **AUTHENTICATION METHOD** is set to **Access Token**. | [**Azure_OAuth2_Client_Secret**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#azureoauth2clientsecret) |
 **USER** | 
User name and host name of the Azure SQL Database server. The format to be used is *username***@***hostname*.

Example: **user@cbiz2nhmpv**

This field is available only if the **AUTHENTICATION METHOD** is set to **User and Password** or **Microsoft Entra ID**. | [**Database_User**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#databaseuser) |
 **PASSWORD** | 
Password for the **USER**.

This field is available only if the **AUTHENTICATION METHOD** is set to **User and Password** or **Microsoft Entra ID**. | **[Database_Password](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#databasepassword)** |


### Advanced Settings


 Field | Description | Equivalent Hub Server Property |
 **LINUX / UNIX ODBC DRIVER MANAGER LIBRARY PATH**
 | 
Directory path where the ODBC Driver Manager Library is installed. This field is applicable only for Linux/Unix operating system.

For a default installation, the ODBC Driver Manager Library is available at **/usr/lib64** and does not need to be specified. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/lib**. | [**ODBC_DM_Lib_Path**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#odbcdmlibpath) |
 **ODBCSYSINI** | 
Directory path where the **odbc.ini** and **odbcinst.ini** files are located. This field is applicable only for Linux/Unix operating system.

For a default installation, these files are available at **/etc** directory and do not need to be specified using this field. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/etc**.

The **odbcinst.ini** file should contain information about the Snowflake ODBC Driver under the heading **[ODBC Driver***version***for SQL Server]**. | [**ODBC_Sysini**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#odbcsysini) |
 **ODBC DRIVER** | Name of the user defined (installed) ODBC driver used for connecting HVR to the Azure SQL Database. | [**ODBC_Driver**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#odbcdriver) |

