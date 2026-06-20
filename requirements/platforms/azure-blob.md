# Azure Blob Storage Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-blob-storage-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/azure-blob-storage-requirements/index.md)

# Azure Blob Storage Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Azure Blob Storage for replication. [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/) is Microsoft's object storage solution for the cloud.

#### Supported Platforms


- Learn about the Azure Blob Storage versions compatible with HVR on our **Platform Support Matrix** page ([6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page.


> **Important:** 
Due to technical limitations, Azure Blob Storage is not supported in the HVR releases since 6.1.5/3 to 6.1.5/9.


## Authentication


HVR does not support client side encryption (customer managed keys) for Azure Blob Storage. For more information about encryption of data in Azure Blob Storage, search for "encryption" in [Azure Blob storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview) documentation.

## Azure Role-Based Access Control


HVR requires the following Azure Role-Based Access Control (RBAC) permissions to function correctly with Azure Blob Storage:

- 
[Microsoft.Storage/storageAccounts/blobServices/getInfo/action](https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftstorage): This is a specific Azure Resource Manager (ARM) action that allows retrieval of information about the Blob service within a storage account.

- 
[Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor): This is a built-in Azure role that grants read, write, and delete permissions to Azure Blob Storage containers and their data.



Both permissions can be combined into a single custom role.

> **Important:** 
While HVR has fallback mechanisms if [Microsoft.Storage/storageAccounts/blobServices/getInfo/action](https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftstorage) permission is not granted, omitting it may lead to potential issues. Proper configuration of these permissions helps prevent unexpected errors when using HVR with Azure Blob Storage.


## Azure Private Endpoints


When using Azure Private Endpoints, configure two private endpoints for the same storage account:

- Blob sub-resource: *account***.blob.core.windows.net**
- DFS sub-resource: *account***.dfs.core.windows.net**


Both hostnames must resolve to private IP addresses inside your virtual network. Creating both private endpoints ensures HVR’s storage operations remain on the private network and avoids connectivity or authorization failures.

## Client Configuration Files


Client configuration files are not required for HVR to perform replication, however, they can be useful for debugging. Client configuration files contain settings for different services like HDFS, and others. If the HVR integrate machine is not part of the cluster, it is recommended to download the configuration files for the cluster so that the Hadoop client knows how to connect to HDFS.

The client configuration files for Cloudera Manager or Ambari for Hortonworks can be downloaded from the respective cluster manager's web interface. For more information about downloading client configuration files, search for "Client Configuration Files" in the respective documentation for [Cloudera](https://www.cloudera.com/documentation.html) and [Hortonworks](https://docs.hortonworks.com/).

## Hive External Tables


To [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) files that reside on the Azure Blob Storage location, HVR allows you to create Hive external tables above Azure Blob Storage. The Hive ODBC connection can be enabled for Azure Blob Storage location by selecting the [**Hive External Tables**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-blob-storage) field while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or [editing the existing location's file connection properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#databaseconnection). For more information about configuring Hive external tables, refer to [Hadoop Azure Support: Azure Blob Storage](https://hadoop.apache.org/docs/current/hadoop-azure/index.html) documentation.

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




## Hadoop Client


For Linux (x64) and Windows (x64), it is not required to install and configure the Hadoop client. However, if you want to use the Hadoop client, set the environment variable **HVR_AZURE_USE_HADOOP**=**1** and follow the steps mentioned below.
Hadoop client configuration steps.
The Hadoop client must be installed on the machine from which HVR will access the Azure Blob Storage. Internally, HVR uses **C API libhdfs** to connect, read, and write data to the Azure Blob Storage during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture), [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), [**Bulk Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity), and [**Direct File Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#directfilecompare).

Azure Blob Storage locations can only be accessed through HVR running on Linux or Windows, and it is not required to run HVR installed on the Hadoop NameNode although it is possible to do so. For more information about installing Hadoop client, refer to [Apache Hadoop Releases](http://hadoop.apache.org/releases.html).

#### Hadoop Client Configuration


The following are required on the machine from which HVR connects to Azure Blob FS:

- Hadoop 2.6.x client libraries with Java 7 Runtime Environment or Hadoop 3.x client libraries with Java 8 Runtime Environment. For downloading Hadoop, refer to [Apache Hadoop Releases](http://hadoop.apache.org/releases.html).
- Set the environment variable **$JAVA_HOME** to the Java installation directory. Ensure that this is the directory that has a bin folder, e.g. if the Java bin directory is d:\java\bin, **$JAVA_HOME** should point to d:\java.
- Set the environment variable **$HADOOP_COMMON_HOME** or **$HADOOP_HOME** or **$HADOOP_PREFIX** to the Hadoop installation directory, or the **hadoop** command line client should be available in the path.
- One of the following configuration is recommended,
- 
Set **$HADOOP_CLASSPATH=$HADOOP_HOME/share/hadoop/tools/lib/***

- 
Create a symbolic link for **$HADOOP_HOME/share/hadoop/tools/lib/** in **$HADOOP_HOME/share/hadoop/common** or any other directory present in classpath.

> **Important:** 
Since the binary distribution available in Hadoop website lacks Windows-specific executables, a warning about unable to locate **winutils.exe** is displayed. This warning can be ignored for using Hadoop library for client operations to connect to a HDFS server using HVR. However, the performance on integrate location would be poor due to this warning, so it is recommended to use a Windows-specific Hadoop distribution to avoid this warning. For more information about this warning, refer to Hadoop issue [HADOOP-10051](https://issues.apache.org/jira/browse/HADOOP-10051).






#### Verifying Hadoop Client Installation


To verify the Hadoop client installation,

- 
The **HADOOP_HOME/bin** directory in Hadoop installation location should contain the hadoop executables in it.

- 
Execute the following commands to verify Hadoop client installation:
$JAVA_HOME/bin/java -version
$HADOOP_HOME/bin/hadoop version
$HADOOP_HOME/bin/hadoop classpath

- 
If the Hadoop client installation is verified successfully then execute the following command to check the connectivity between HVR and Azure Blob FS:

> **Important:** 
To execute this command successfully and avoid the error "ls: Password fs.adl.oauth2.client.id not found", few properties needs to be defined in the file **core-site.xml** available in the hadoop configuration folder (for e.g., **<path>/hadoop-2.8.3/etc/hadoop**). The properties to be defined differs based on the **Mechanism** (authentication mode). For more information, refer to section 'Configuring Credentials' in [Hadoop Azure Blob FS Support](https://hadoop.apache.org/docs/current/hadoop-azure/index.html) documentation.

$HADOOP_HOME/bin/hadoop fs -ls adl://<cluster>/



#### Verifying Hadoop Client Compatibility with Azure Blob Storage


To verify the compatibility of Hadoop client with Azure Blob Storage, check if the following JAR files are available in the Hadoop client installation location ( **$HADOOP_HOME/share/hadoop/tools/lib** ):
hadoop-azure-<version>.jar
azure-storage-<version>.jar

## Related Articles


- [Azure Blob Storage as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-blob-storage-requirements/azure-blob-storage-as-target)
- [Location Connection for Azure Blob Storage](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-blob-storage)

