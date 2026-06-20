# Azure Data Lake Storage Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-data-lake-storage-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/azure-data-lake-storage-requirements/index.md)

# Azure Data Lake Storage Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Azure Data Lake Storage (DLS) for replication.

#### Supported Platforms


- Learn about the Azure Data Lake Storage versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page.


> **Important:** 
Due to technical limitations, Azure Data Lake Storage is not supported in the HVR releases since 6.1.5/3 to 6.1.5/9.


## Hadoop Client for ADLS Gen1


For ADLS Gen1, the Hadoop client must be installed on the machine from which HVR accesses the Azure DLS. HVR uses **C API libhdfs** to connect, read, and write data into the Azure Data Lake Storage during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture), [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), [**Bulk Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity), and [**Direct File Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#directfilecompare). Azure DLS locations can only be accessed through HVR running on Linux or Windows, and it is not required to run HVR installed on the Hadoop NameNode although it is possible to do so. For more information about installing Hadoop client, refer to [Apache Hadoop Releases](https://hadoop.apache.org/releases.html).

> **Important:** 
For ADLS Gen2, it is not required to install and configure the Hadoop client.


> **Important:** 
On Linux, the following warning may be displayed: "WARNING: HADOOP_PREFIX has been replaced by HADOOP_HOME. Using value of HADOOP_PREFIX".

To fix this, comment out the following line in the **$HADOOP_PREFIX/libexec/hadoop-condig.sh** file:
hadoop_deprecate_envvar HADOOP_PREFIX HADOOP_HOME


### Hadoop Client Configuration


The following are required on the machine from which HVR connects to Azure DLS:

- Hadoop 2.6.x client libraries with Java 7 Runtime Environment or Hadoop 3.x client libraries with Java 8 Runtime Environment. For downloading Hadoop, refer to [Apache Hadoop Releases](https://hadoop.apache.org/releases.html).
- Set the environment variable **$JAVA_HOME** to the Java installation directory. Ensure that this is the directory that has a bin folder, e.g. if the Java bin directory is d:\java\bin, **$JAVA_HOME** should point to d:\java.
- Set the environment variable **$HADOOP_COMMON_HOME** or **$HADOOP_HOME** or **$HADOOP_PREFIX** to the Hadoop installation directory, or the **hadoop** command line client should be available in the path.
- One of the following configuration is recommended:
- Set **$HADOOP_CLASSPATH=$HADOOP_HOME/share/hadoop/tools/lib/***
- Create a symbolic link for **$HADOOP_HOME/share/hadoop/tools/lib** in **$HADOOP_HOME/share/hadoop/common** or any other directory present in classpath.




> **Important:** 
Since the binary distribution available in Hadoop website lacks Windows-specific executables, a warning about unable to locate **winutils.exe** is displayed. This warning can be ignored for using Hadoop library for client operations to connect to a HDFS server using HVR. However, the performance on integrate location would be poor due to this warning, so it is recommended to use a Windows-specific Hadoop distribution to avoid this warning. For more information about this warning, refer to Hadoop issue [[HADOOP-10051](https://issues.apache.org/jira/browse/HADOOP-10051)].


### Verifying Hadoop Client Installation


To verify the Hadoop client installation:

- 
The **HADOOP_HOME/bin** directory in Hadoop installation location should contain the Hadoop executables in it.

- 
Execute the following commands to verify Hadoop client installation:
$JAVA_HOME/bin/java -version
$HADOOP_HOME/bin/hadoop version
$HADOOP_HOME/bin/hadoop classpath

- 
If the Hadoop client installation is verified successfully then execute the following command to verify the connectivity between HVR and Azure DLS:

> **Important:** 
To execute this command successfully and avoid the error "ls: Password fs.adl.oauth2.client.id not found", few properties needs to be defined in the file **core-site.xml** available in the Hadoop configuration folder (for e.g., **<path>/hadoop-2.8.3/etc/hadoop**). The properties to be defined differs based on the [authentication](#authenticationmethods) method selected. For more information, refer to section [Configuring Credentials and FileSystem](https://hadoop.apache.org/docs/current/hadoop-azure-datalake/index.html#Configuring_Credentials_and_FileSystem) in [Hadoop Azure Data Lake Support](null) documentation.

$HADOOP_HOME/bin/hadoop fs -ls adl://<cluster>/



### Verifying Hadoop Client Compatibility with Azure DLS


To verify the compatibility of Hadoop client with Azure DLS, check if the following JAR files are available in the Hadoop client installation location (**$HADOOP_HOME/share/hadoop/tools/lib**):
hadoop-azure-<version>.jar
hadoop-azure-datalake-<version>.jar
azure-data-lake-store-sdk-<version>.jar
azure-storage-<version>.jar

## Client Configuration Files


Client configuration files are not required for HVR to perform replication, however, they can be useful for debugging. Client configuration files contain settings for different services like HDFS, and others. If the HVR integrate machine is not part of the cluster, it is recommended to download the configuration files for the cluster so that the Hadoop client knows how to connect to HDFS.

The client configuration files for Cloudera Manager or Ambari for Hortonworks can be downloaded from the respective cluster manager's web interface. For more information about downloading client configuration files, search for "Client Configuration Files" in the respective documentation for [Cloudera](https://www.cloudera.com/documentation.html) and [Hortonworks](https://docs.hortonworks.com/).

## Authentication Methods


HVR supports the following authentication methods for connecting to ADLS:

### Shared Key


In this method, the HVR **User** gains full access to all operations on all resources, including setting owner and changing Access Control List (ACL). The connection parameter required in this authentication mode is a shared secret key ([**Azure_Shared_Secret_Key**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azuresharedsecretkey)) that Azure generates for the storage account. For more information on how to manage access keys for Shared Key authorization, refer to [Manage storage account access keys](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage).

> **Important:** 
- With this authentication mode, no identity is associated with a user, and permission-based authorization cannot be implemented.
- This authentication method is not supported for ADLS Gen1.



### User Name and Password


This method is used to connect to Azure DLS Gen2 storage account directly with OAuth 2.0 using the user credentials. The connection parameters required for this authentication mode are OAuth username ([**Azure_OAuth2_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2user)) and password ([**Azure_OAuth2_Password**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2password)). For more information, refer to [Azure Data Lake Storage Gen2](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) documentation.

> **Important:** 
This authentication method is not supported for ADLS Gen1.


### Service-to-service


This method is used if an application needs to directly authenticate itself with ADLS. The connection parameters required in this authentication mode are OAuth2 Endpoint ([**Azure_OAuth2_Endpoint**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2endpoint)), Client ID ([**Azure_OAuth2_Client_Id**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2clientid)), and Client Secret Key ([**Azure_OAuth2_Client_Secret**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2clientsecret)). For more information about the connection parameters, search for "Service-to-service authentication" in [Data Lake Store Documentation](https://docs.microsoft.com/en-us/azure/data-lake-store/).

### Refresh Token


This method is used if a user's Azure credentials are used to authenticate with ADLS. The connection parameters required in this authentication mode are Client ID ([**Azure_OAuth2_Client_Id**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2clientid)) and Refresh Token ([**Azure_OAuth2_Refresh_Token**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2refreshtoken)). For more information about the connection parameters and end-user authentication using REST API, search for "End-user authentication" in [Data Lake Store Documentation](https://docs.microsoft.com/en-us/azure/data-lake-store/).

### MSI


This method is used when you have HVR running on a VM in Azure. Managed Service Identity (MSI) allows you to authenticate to services that support Microsoft Entra ID (formerly Azure Active Directory) authentication. For this authentication mode to work, the VM should have access to Azure DLS and the MSI authentication should be enabled on the VM in Azure. The connection parameters required in this authentication mode is the Port number ([**Azure_OAuth2_MSI_Port**](https://fivetran.com/docs/hvr6/property-reference/location-properties#azureoauth2msiport)). For more information about providing access to Azure DLS and enabling MSI on the VM, search for "Access Azure Data Lake Store" in [Microsoft Entra ID Managed Service Identity Documentation](https://docs.microsoft.com/en-us/azure/active-directory/managed-service-identity/).

## Hive External Tables


To [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) files that reside on the Azure Data Lake Storage Gen1 location, HVR allows you to create Hive external tables above Azure Data Lake Storage. The Hive ODBC connection can be enabled for Azure Data Lake Storage location by selecting the [**Hive External Tables**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-blob-storage) field while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or [editing the existing location's file connection properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#databaseconnection). For more information about configuring Hive external tables, refer to [Hadoop Azure Data Lake Support](null) documentation.

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


- [Azure Data Lake Storage as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-data-lake-storage-requirements/azure-data-lake-storage-as-target)
- [Location Connection for Azure Data Lake Storage](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-data-lake-storage)

