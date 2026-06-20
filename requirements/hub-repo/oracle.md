# Repository Database in Oracle - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-oracle

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-oracle/index.md)

# Repository Database in Oracle


Fivetran HVR allows you to create a repository database (schema) in Oracle. The repository database (schema) can be located inside an Oracle instance on the hub machine, or it can be located on another machine and connected using a TNS connection. The **Repository Database** section in **Capabilities** ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635#repositorydatabase), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630#repositorydatabase), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#repositorydatabase), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#repositorydatabase), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#repositorydatabase), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#repositorydatabase)) lists the supported Oracle versions that can be used as a repository database.

## Grants for Repository Database


The following grants are required for the repository database in Oracle:
grant create session to <em>username</em>; 
grant create table to <em>username</em>; 
grant create procedure to <em>username</em>;

## Repository Database Connection


This section describes the details required for connecting to the repository database in Oracle:

 Field | Description | Equivalent Location Property |
 **ORACLE_HOME**
 | 
Directory path where Oracle is installed.

Example: **D:\oracle** or **distr/oracle** | [**Oracle_Home**](https://fivetran.com/docs/hvr6/property-reference/location-properties#oraclehome) |
 **Local connect to database** | Connect to Oracle database using local connection. | 
 |
 **SID** | 
Unique name identifier of the Oracle instance/database.

Example: **ORA1900** | **[Oracle_SID](https://fivetran.com/docs/hvr6/property-reference/location-properties#oraclesid)** |
 **Oracle TNS** | Connect to Oracle database using TNS (Transparent Network Substrate). | 
 |
 **ORACLE TNS** | 
Connection string for connecting to the Oracle database using TNS.

The format for the connection string is *host***:***port***/***service_name*.

Alternatively, you can add the connection details into the clients **tnsnames.ora** file and use that net service name in this field. This method requires easy connect enabled | [**Oracle_TNS**](https://fivetran.com/docs/hvr6/property-reference/location-properties#oracletns) |
 **USER** | Username for connecting HVR to the Oracle database. | [**Database_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseuser) |
 **PASSWORD** | Password of the **USER**. | **[Database_Password](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasepassword)** |

