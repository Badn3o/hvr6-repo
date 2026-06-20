# Repository Database in SQL Server - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sql-server

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sql-server/index.md)

# Repository Database in SQL Server


Fivetran HVR allows you to create a repository database in SQL Server. The **Repository Database** section in **Capabilities** ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635#repositorydatabase), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630#repositorydatabase), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#repositorydatabase), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#repositorydatabase), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#repositorydatabase), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#repositorydatabase)) lists the supported SQL Server versions that can be used as a repository database.

It is recommended to create a new database (schema) for HVR repository. If an existing database is to be used for HVR repository, then the HVR [repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables) can be separated by creating a new database schema and associating it with HVR's user as follows:
create schema <em>schemaname</em>;

## Grants for Repository Database


The following grants are required for the repository database user in SQL Server:
grant create table to <em>username</em>;
grant create procedure to <em>username</em>;
grant select, insert, delete, update on schema::<em>schemaname</em> to <em>username</em>;
grant control on schema::<em>schemaname</em> to <em>username</em>;
alter user <em>username</em> with default_schema=<em>schemaname</em>;

## Repository Database Connection


This section describes the details required for connecting to the repository database in SQL Server:

 Field | Description | Equivalent Hub Server Property |
 **SERVER** | 
Name of the server (host) on which SQL Server is running and the Port number or the instance name of SQL Server.

The following formats are supported for this field:

- *server_name* : Specify only the server name and HVR will automatically use the default port to connect to the server on which SQL Server is running.

Example: **myserver**
- *server_name***,***port_number* : Specify the server name and port number separated by a comma (**,**) to connect to the server on which SQL Server is running.

This format is required when using custom port for connection or when **[SqlServer_Native_Replicator_Connection](#sqlservernativereplicatorconnection)** is defined.

Example: **myserver,1435**
- *server_name***\***server_instance_name* : Specify the server name and server instance name separated by a backslash (**\**) to connect to the server on which SQL Server is running.

This format is not supported on Linux.

Example: **myserver\instance6048**

 | [**SqlServer_Server**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#sqlserverserver) |
 **DATABASE** | Name of the SQL Server database. | [**Database_Name**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#databasename) |
 **USER** | 
Username for connecting HVR to the SQL Server database.

> **Important:** 
The login/user account used for connecting HVR to SQL Server database engine should be defined with SQL Server Authentication or Windows Authentication. If Windows Authentication is used for connecting to SQL Server database, the **USER** and **PASSWORD** field should be left blank (empty).

 | [**Database_User**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#databaseuser) |
 **PASSWORD** | Password for the **USER**. | **[Database_Password](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#databasepassword)** |


### Advanced Settings


 Field | Description | Equivalent Hub Server Property |
 **LINUX / UNIX ODBC DRIVER MANAGER LIBRARY PATH**
 | 
Directory path where the ODBC Driver Manager Library is installed. This field is applicable only for Linux/Unix operating system.

For a default installation, the ODBC Driver Manager Library is available at **/usr/lib64** and does not need to be specified. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/lib**. | [**ODBC_DM_Lib_Path**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#odbcdmlibpath) |
 **LINUX / UNIX ODBCSYSINI** | 
Directory path where the **odbc.ini** and **odbcinst.ini** files are located. This field is applicable only for Linux/Unix operating system.

For a default installation, these files are available at **/etc** directory and do not need to be specified using this field. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/etc**. | [**ODBC_Sysini**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#odbcsysini) |
 **ODBC DRIVER** | Name of the user defined (installed) ODBC driver used for connecting HVR to the SQL Server database.It is recommended to leave this field empty, HVR will automatically load the correct driver for your current platform. Otherwise, select one of the available **SQL Server Native Client** options. | [**ODBC_Driver**](https://fivetran.com/docs/hvr6/property-reference/location-properties#odbcdriver) |

