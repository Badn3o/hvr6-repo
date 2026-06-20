# Hub Repository Database Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/hub-repository-database-requirements/index.md)

# Hub Repository Database Requirements


Fivetran HVR uses its repository database to store the replication definitions (which tables must be replicated between which 'locations') as well as run-time status (which jobs are currently running).

In the repository database, the information is stored in the [repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). HVR supports the creation of repository database on certain DBMSs only. For the list of supported DBMSs, see section [Repository Database]([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635#repositorydatabase), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630#repositorydatabase), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#repositorydatabase), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#repositorydatabase), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#repositorydatabase), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#repositorydatabase)) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

## Topics


The following sections describe the pre-requisites, access privileges, and other configuration required for using the supported DBMS as repository database.

- [Repository Database in Aurora MySQL](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-aurora-mysql)
- [Repository Database in Aurora PostgreSQL](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-aurora-postgresql)
- [Repository Database in Azure SQL Database](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-azure-sql-database)
- [Repository Database in Azure SQL Managed Instance](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-azure-sql-managed-instance)
- [Repository Database in SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sql-database-in-microsoft-fabric)
- [Repository Database in Db2 for Linux, Unix and Windows](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-db2-for-linux-unix-and-windows)
- [Repository Database in MariaDB](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-mariadb)
- [Repository Database in MySQL](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-mysql)
- [Repository Database in Oracle](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-oracle)
- [Repository Database in PostgreSQL](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-postgresql)
- [Repository Database in SQL Server](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sql-server)
- [Repository Database in Sybase ASE](https://fivetran.com/docs/hvr6/requirements/hub-repository-database-requirements/repository-database-in-sybase-ase)

