# Apache Kafka Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements/index.md)

# Apache Kafka Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Apache Kafka for replication.

#### Supported Platforms


- Learn about the Apache Kafka versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for Apache Kafka on our **Capabilities for Apache Kafka** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-apache-kafka), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-apache-kafka), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-apache-kafka), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-apache-kafka), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-apache-kafka), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-apache-kafka)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of supported Apache Kafka data types and their mapping, see [Data Type Mapping for Apache Kafka](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-kafka).


## Installation Dependencies


On Linux, to use any of the Kafka [authentication methods](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-apache-kafka) (**User Name and Password**, **Kerberos**, **SCRAM-SHA-256**, or **SCRAM-SHA-512**), HVR requires the library **libsasl2.so.2** to be installed. This library is part of Cyrus SASL and can be installed as follows:
$ yum install cyrus-sasl    # On Red Hat Linux, CentOS
$ zypper install cyrus-sasl    # On SUSE Linux

There are no installation dependency for using Kafka authentication methods on Windows.

## Known Issues


### Kafka Broker Version 0.9.0.0 and 0.9.0.1


When using Kafka broker version 0.9.0.0 or 0.9.0.1, a known bug (KAFKA-3547) may cause a timeout error in HVR.

To resolve this issue, define action [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) for the Kafka location as follows:

 Group | Table | Action | Parameter(s) |
 KAFKA | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=**HVR_KAFKA_BROKER_VERSION**
**[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)**=**0.9.0.1** |


> **Important:** 
If you are using Kafka broker version 0.9.0.0, set [**Value**](https://fivetran.com/docs/hvr6/action-reference/environment#value)**=0.9.0.0**


### Amazon MSK


As noted in [the AWS documentation](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html#msk-password-limitations), Amazon MSK only supports SCRAM-SHA-512 authentication.

To override HVR's default authentication method (PLAIN or GSAPI), define action [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) for the Kafka location as follows:

 Group | Table | Action | Parameter(s) |
 KAFKA | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=**HVR_KAFKA_PROPERTY**
**[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)**=**sasl.mechanism=SCRAM-SHA-512** |


## Related Articles


- [Apache Kafka as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements/apache-kafka-as-target)
- [Location Connection for Apache Kafka](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-apache-kafka)

