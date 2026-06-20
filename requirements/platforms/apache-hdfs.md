# Apache HDFS Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-hdfs-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/apache-hdfs-requirements/index.md)

# Apache HDFS Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Apache Hadoop Distributed File System (HDFS) for replication.

#### Supported Platforms


- Learn about the Apache HDFS versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page.


## Hadoop Client


The Hadoop client must be installed on the machine from which HVR accesses the HDFS server.

HDFS locations can only be accessed through HVR running on Linux or Windows, and it is not required to run HVR installed on the Hadoop Namenode although it is possible to do so. The Hadoop client should be present on the server from which HVR will access the HDFS. HVR uses HDFS compatible libhdfs API to connect, read, and write data to HDFS during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture), [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), [**Bulk Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity), and [**Direct File Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#directfilecompare). For more information about installing Hadoop client, refer to [Apache Hadoop Releases](http://hadoop.apache.org/releases.html).

### Hadoop Client Configuration


The following are required on the server from which HVR connects to HDFS:

- 
Install [Hadoop 2.4.1 or later versions](http://hadoop.apache.org/releases.html) along with Java Runtime Environment:

- Hadoop versions below 3.0 require JRE 7 or 8
- Hadoop version 3.0 and higher requires only JRE 8


> **Important:** 
Since 6.1.5/10, only Hadoop version 3.3.6 and JRE 8 are supported.




- 
Set the environment variable **$JAVA_HOME** to the Java installation directory. Ensure that this is the directory that has a **bin** folder in it, for example, if the Java **bin** directory path is **d:\java\bin**, then **$JAVA_HOME** should point to **d:\java**.

- 
Set the environment variable **$HADOOP_COMMON_HOME** or **$HADOOP_HOME** or **$HADOOP_PREFIX** to the Hadoop installation directory, or the **hadoop** command line client should be available in the path.

> **Important:** 
Since the binary distribution available in Hadoop website lacks Windows-specific executables, a warning about unable to locate **winutils.exe** is displayed. This warning can be ignored for using Hadoop library for client operations to connect to a HDFS server using HVR. However, the performance on integrate location would be poor due to this warning, so it is recommended to use a Windows-specific Hadoop distribution to avoid this warning. For more information about this warning, refer to [Hadoop Wiki](https://wiki.apache.org/hadoop/WindowsProblems) and Hadoop issue [HADOOP-10051](https://issues.apache.org/jira/browse/HADOOP-10051).




### Verifying Hadoop Client Installation


To verify the Hadoop client installation,

- 
The **HADOOP_HOME/bin** directory in Hadoop installation location should contain the hadoop executables in it.

- 
Execute the following commands to verify Hadoop client installation:
$JAVA_HOME/bin/java -version
$HADOOP_HOME/bin/hadoop version
$HADOOP_HOME/bin/hadoop classpath

- 
If the Hadoop client installation is verified successfully then execute the following command to verify the connectivity between HVR and HDFS:
$HADOOP_HOME/bin/hadoop fs -ls hdfs://<em>cluster</em>/



### Client Configuration Files


Client configuration files are required if [Kerberos authentication](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-hdfs-requirements/hdfs-authentication-and-kerberos) is used in the Hadoop cluster or else they can be useful for debugging. Client configuration files contain settings for different services like HDFS, and others. If the HVR integrate server is not part of the cluster, it is recommended to download the configuration files for the cluster so that the Hadoop client knows how to connect to HDFS.

The client configuration files for Cloudera Manager or Ambari for Hortonworks can be downloaded from the respective cluster manager's web interface. For more information about downloading client configuration files, search for "Client Configuration Files" in the respective documentation for [Cloudera](https://www.cloudera.com/documentation.html) and [Hortonworks](https://docs.hortonworks.com/).

## Hive External Tables


To [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) files that reside on the Apache HDFS location, HVR allows you to create Hive external tables above Apache HDFS. The Hive ODBC connection can be enabled for Apache HDFS location by selecting the [**Hive External Tables**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-apache-hdfs) field while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or [editing the existing location's file connection properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#databaseconnection). For more information about configuring Hive external tables, refer to [Apache Hadoop](https://hadoop.apache.org/docs/current/) documentation.

#### ODBC Connection


HVR uses an ODBC connection to the Hadoop cluster for which it requires the ODBC driver (Amazon ODBC or HortonWorks ODBC) for Hive installed on the machine (or in the same network). The Amazon and HortonWorks ODBC drivers are similar and compatible to work with Hive 2.x release. However, it is recommended to use the Amazon ODBC driver for Amazon Hive and the Hortonworks ODBC driver for HortonWorks Hive. For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in **HVR_HOME** directory or the download page.

> **Important:** 
On Linux, HVR additionally requires unixODBC.


By default, HVR uses Amazon ODBC driver for connecting to Hadoop. However, if you want to use the (user installed) Hortonworks ODBC driver, while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or [editing the existing location's file connection properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#databaseconnection), use the [**ODBC Driver**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-amazon-s3#configurationforhiveexternaltables) field in HVR UI and specify the ODBC driver.

#### Channel Configuration


For the file formats (CSV, JSON, and AVRO) the following action definitions are required to handle certain limitations of the Hive deserialization implementation during Bulk or Row-wise [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data):

- 
For CSV

 Group | Table | Action | Parameter(s) |
 S3 | * | **[FileFormat](https://fivetran.com/docs/hvr6/action-reference/fileformat)** | **[NullRepresentation](https://fivetran.com/docs/hvr6/action-reference/fileformat#nullrepresentation)**=\\N |
 S3 | * | **[TableProperties](https://fivetran.com/docs/hvr6/action-reference/tableproperties)** | **[CharacterMapping](https://fivetran.com/docs/hvr6/action-reference/tableproperties#charactermapping)**="\x00>\\0;\n>\\n;\r>\\r;">\"" |
 S3 | * | **[TableProperties](https://fivetran.com/docs/hvr6/action-reference/tableproperties)** | **[MapBinary](https://fivetran.com/docs/hvr6/action-reference/tableproperties#mapbinary)**=BASE64 |




- 
For JSON

 Group | Table | Action | Parameter(s) |
 S3 | * | **[TableProperties](https://fivetran.com/docs/hvr6/action-reference/tableproperties)** | **[MapBinary](https://fivetran.com/docs/hvr6/action-reference/tableproperties#mapbinary)**=BASE64 |
 S3 | * | **[FileFormat](https://fivetran.com/docs/hvr6/action-reference/fileformat)** | **[JsonMode](https://fivetran.com/docs/hvr6/action-reference/fileformat#jsonmode)**=ROW_FRAGMENTS |


- 
For Avro

 Group | Table | Action | Parameter(s) |
 S3 | * | ****[FileFormat](https://fivetran.com/docs/hvr6/action-reference/fileformat)**** | **[AvroVersion](https://fivetran.com/docs/hvr6/action-reference/fileformat#avroversion)**=v1_8 |


> **Note:** 
**v1_8** is the default value for parameter [**AvroVersion**](https://fivetran.com/docs/hvr6/action-reference/fileformat#avroversion), so it is not mandatory to define this action.




## Related Articles


- [Apache HDFS as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-hdfs-requirements/apache-hdfs-as-target)
- [HDFS Authentication and Kerberos](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-hdfs-requirements/hdfs-authentication-and-kerberos)
- [Location Connection for Apache HDFS](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-apache-hdfs)

