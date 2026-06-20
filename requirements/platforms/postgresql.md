# PostgreSQL Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements/index.md)

# PostgreSQL Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using PostgreSQL for replication.

#### Supported Services


HVR supports the following PostgreSQL database services:

- 
[Generic PostgreSQL](https://www.postgresql.org/)  (including  [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/) and other hosted versions).

- 
[Amazon Aurora PostgreSQL](https://aws.amazon.com/rds/aurora/)

- 
[YugabyteDB](https://docs.yugabyte.com/) <b>Since:</b> v6.2.5/0



> **Note:** 
For more information about our support for hosted databases, see the [Hosted Database Support Policy](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615#hosted_database_support_policy) page.


#### Supported Platforms


- Learn about the PostgreSQL versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- 
Discover what HVR offers for PostgreSQL on our **Capabilities for PostgreSQL** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-postgresql), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-postgresql), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-postgresql), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-postgresql), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-postgresql), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-postgresql)).

- 
For Aurora PostgreSQL-specific capabilities, check out the **Capabilities for Aurora PostgreSQL** page ([6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-aurora-postgresql), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-aurora-postgresql)).



#### Data Management


- 
Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of supported PostgreSQL data types and their mapping, see [Data Type Mapping for PostgreSQL](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-postgresql).

- 
Understand the character encodings HVR supports for PostgreSQL on the [Supported Character Encodings](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings#postgresql) page.



> **Tip:** 
Fivetran provides additional solutions for replicating data from PostgreSQL. For more information, see section [PostgreSQL](https://fivetran.com/docs/connectors/databases/postgresql) in Databases.


## Database Connection


HVR requires the PostgreSQL native client library "libpq" (i.e. **libpq.so.5** and its dependencies) to be installed on the machine from which HVR connects to the PostgreSQL server.

## Connecting to Amazon RDS for PostgreSQL, Aurora PostgreSQL and YugabyteDB


To enable the HVR capture or integrate process to connect to Amazon RDS for PostgreSQL, Aurora PostgreSQL, or YugabyteDB, you must allow inbound traffic on the database listener port to the system running the HVR process.

If an HVR Agent is in place, then communication must be enabled for the system hosting the HVR Agent. When connecting directly from an HVR Hub Server, the connection must be allowed for the HVR Hub Server.

For the HVR system operating within the same Virtual Private Cloud (VPC) as Amazon RDS for PostgreSQL, Aurora PostgreSQL, or YugabyteDB, you can use the internal rather than public IP address for the service to allow access. It is recommended to restrict access strictly to the HVR system that requires it, rather than allowing broader or public access.

The default TCP port that PostgreSQL listens on Amazon RDS for PostgreSQL and Aurora PostgreSQL is 5432. The default TCP port that YugabyteDB listens on is 5433.

## Related Articles


- [PostgreSQL as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements/postgresql-as-source)
- [Capture from PostgreSQL using Direct DBMS Log Reading](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements/postgresql-as-source/capture-from-postgresql-using-direct-dbms-log-reading)
- [Capture from PostgreSQL using Logical Replication](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements/postgresql-as-source/capture-from-postgresql-using-logical-replication)


- [PostgreSQL as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements/postgresql-as-target)
- [Location Connection for PostgreSQL](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-postgresql)

