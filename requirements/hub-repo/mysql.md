# Repository Database in MySQL - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-mysql

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-mysql/index.md)

# Repository Database in MySQL


Fivetran HVR allows you to create a repository database in MySQL. The **Repository Database** section in **Capabilities** ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635#repositorydatabase), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630#repositorydatabase), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#repositorydatabase), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#repositorydatabase), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#repositorydatabase), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#repositorydatabase)) lists the supported MySQL versions that can be used as a repository database.

## Grants for Repository Database


The following grant is required for the repository database in MySQL:

- The repository user should have permission to create and drop HVR [repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables).


## Repository Database Connection


This section describes the details required for connecting to the repository database in MySQL:

 Field | Description | Equivalent Location Property |
 **HOST** | 
Hostname or IP-address of the server on which the MySQL database is running.

Example: **192.168.127.129** | [**Database_Host**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasehost) |
 **PORT** | 
Port number on which the MySQL database server is expecting connections.

Example: **3306** | [**Database_Port**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseport) |
 **DATABASE** | 
Name of the MySQL database.

Example: **mytestdb** | [**Database_Name**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasename) |
 **USER** | 
Username for connecting HVR to the MySQL database.

Example: **dbuser** | [**Database_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databaseuser) |
 **PASSWORD** | Password for the **USER**. | **[Database_Password](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasepassword)** |

