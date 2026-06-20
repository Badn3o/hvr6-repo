# Google Cloud Storage Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-cloud-storage-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/google-cloud-storage-requirements/index.md)

# Google Cloud Storage Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Google Cloud Storage (GCS) for replication.

#### Supported Platforms


- Learn about the Google Cloud Storage versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page.


> **Important:** 
HVR uses GCS S3-compatible API (cURL library) to connect, read, and write data to Google Cloud Storage during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture), [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), [**Bulk Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity), and [**Direct File Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#directfilecompare).


## Permissions


To run a [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) or [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) or [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) in Google Cloud Storage location, it is recommended that the GCS user has the role of **Storage Admin** (**roles/storage.admin**).

The minimal permission set for capture and integrate location are:

- **storage.buckets.get**
- **storage.multipartUploads.list**
- **storage.objects.list**
- **storage.objects.get**
- **storage.objects.create**
- **storage.objects.delete**


For more information on the Google Cloud Storage role permissions, refer to the [Google Cloud Storage](https://cloud.google.com/storage/docs/access-control/iam-roles) documentation.

## Hive External Tables


To [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) files that reside on the Google Cloud Storage location, HVR allows you to create Hive external tables above Google Cloud Storage. The Hive ODBC connection can be enabled for Google Cloud Storage location by selecting the [**Hive External Tables**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-azure-blob-storage) field while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or [editing the existing location's file connection properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#databaseconnection). For more information about configuring Hive external tables, refer to [Apache Hadoop](https://hadoop.apache.org/docs/current/) documentation.

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


- 


## Related Articles


- [Google Cloud Storage as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-cloud-storage-requirements/google-cloud-storage-as-target)
- [Location Connection for Google Cloud Storage](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-google-cloud-storage)

