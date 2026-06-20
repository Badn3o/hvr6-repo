# Amazon S3 Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/amazon-s3-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/amazon-s3-requirements/index.md)

# Amazon S3 Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using Amazon S3(Simple Storage Service) for replication.

#### Supported Platforms


- Learn about the Amazon S3 versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page.


> **Note:** 
- HVR uses the S3 REST interface (cURL library) to connect, read, and write data to S3 during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture), [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), [**Bulk Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity), and [**Direct File Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#directfilecompare).
- If there is an HVR Agent running on Amazon EC2 node, which is in the AWS network together with the S3 bucket, then the communication between the HVR Hub and AWS network is done via HVR protocol, which is more efficient than direct S3 transfer. Another approach to avoid the described bottleneck is to configure the HVR Hub on an EC2 node.



## Permissions


To [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) or [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) into an Amazon S3 location, it is recommended that the AWS user has the **AmazonS3FullAccess** permission policy. The user permission policy **AmazonS3ReadOnlyAccess** is sufficient for capture locations that have the location property [**File_State_Directory**](https://fivetran.com/docs/hvr6/property-reference/location-properties#filestatedirectory) defined.

For more information on the Amazon S3 permissions policy, refer to the [AWS S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html).

Alternatively, the following minimal permission set can also be used for integrate location:

- **s3:GetBucketLocation**
- **s3:ListBucket**
- **s3:ListBucketMultipartUploads**
- **s3:AbortMultipartUpload**
- **s3:GetObject**
- **s3:PutObject**
- **s3:DeleteObject**

Sample JSON with a user role permission policy for S3 location{
    "Statement": [
        {
            "Sid": <identifier>,
            "Effect": "Allow",
            "Principal": {
                    "AWS": "arn:aws:iam::<account_id>:<user>/<username>",
            },
            "Action": [
                    "s3:GetObject",
                    "s3:GetObjectVersion",
                    "s3:PutObject",
                    "s3:DeleteObject",
                    "s3:DeleteObjectVersion",
                    "s3:AbortMultipartUpload"
            ],
            "Resource": "arn:aws:s3:::<bucket_name>/*"
        },
        {
            "Sid": <identifier>,
            "Effect": "Allow",
            "Principal": {
                    "AWS": "arn:aws:iam::<account_id>:<user>/<username>"
            },
            "Action": [
                    "s3:ListBucket",
                    "s3:GetBucketLocation",
                    "s3:ListBucketMultipartUploads"
            ],
            "Resource": "arn:aws:s3:::<bucket_name>"
        }
    ]
}

For minimal permission, since version 6.1.0/10, HVR also supports the [AWS temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html). There are two ways to request for the AWS Security Token Service (STS) temporary credentials:

- 
Using a combination of **AWS STS Role ARN**, **AWS Access Key Id**, and **AWS Secret Access Key**
Sample JSON{
     "Version": "2012-10-17", 
     "Statement": [ 
         {
             "Sid": "", 
             "Effect": "Allow", 
             "Principal": { 
                     "AWS": "arn:aws:iam::<account_id>:<user>/<username>"
              },
             "Action": "sts:AssumeRole"
         } 
     ] 
}

- 
Using a combination of **AWS STS Role ARN** and **AWS IAM Role** (a role that has access to an EC2 machine)
Sample JSON{ 
     "Version": "2012-10-17",
      "Statement": [ 
          { 
               "Sid": "",
               "Effect": "Allow",
               "Principal": {
                        "AWS": [ 
                              "arn:aws:iam::<account_id>:<user>/<username>", 
                              "arn:aws:iam::<account_id>:<role>/<username>"
                         ] 
                },
               "Action": "sts:AssumeRole" 
          } 
     ]
 }



## S3 Bucket Region


By default, HVR connects to **us-east-1** once for determining your [S3 bucket region](https://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region). If a firewall restriction or a service such as Amazon Private Link is preventing the determination of your S3 bucket region, you can change this region (**us-east-1**) to the region where your S3 bucket is located by defining the following action:

 Group | Table | Action | Parameter(s) |
 Snowflake | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=**HVR_S3_BOOTSTRAP_REGION**,******[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)**=*s3_bucket_region* |


## AWS China


For enabling HVR to interact with AWS China cloud, define the [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) variable **HVR_AWS_CLOUD** with value **CHINA** on the HVR Hub and remote machine.

> **Important:** 
S3 encryption with Key Management Service (KMS) is not supported in the AWS China cloud.


## Hive External Tables


To [compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) files stored in the Amazon S3 location, HVR allows you to create Hive external tables on S3. You can enable the Hive ODBC connection for the S3 location by selecting the [**Hive External Tables**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-amazon-s3#configurationforhiveexternaltables) option when [creating an S3 location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or [editing the connection properties of the existing S3 location](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#databaseconnection). For more information about configuring Hive external tables, refer to the following documentation - [Hadoop - Integration with Amazon Web Services](https://hadoop.apache.org/docs/current/hadoop-aws/tools/hadoop-aws/index.html) and [Apache Hadoop - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop.html).

#### ODBC Connection


HVR uses an ODBC connection to the Hadoop cluster for which it requires the ODBC driver (Amazon ODBC or HortonWorks ODBC) for Hive installed on the machine (or in the same network). The Amazon and HortonWorks ODBC drivers are similar and compatible to work with Hive 2.x release. However, it is recommended to use the Amazon ODBC driver for Amazon Hive and the Hortonworks ODBC driver for HortonWorks Hive. For information about the supported ODBC driver version, refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (**hvr.rel**) available in **HVR_HOME** directory or the download page.

> **Important:** 
On Linux, HVR additionally requires unixODBC.


By default, HVR uses Amazon ODBC driver for connecting to Hadoop. However, if you want to use the (user installed) Hortonworks ODBC driver, while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or [editing the existing location's file connection properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#databaseconnection), use the [**ODBC Driver**](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-amazon-s3#configurationforhiveexternaltables) field in HVR UI and specify the ODBC driver.

Amazon does not recommend changing the security policy of the EMR. This is the reason why it is required to create a tunnel between the machine where the ODBC driver is installed and the EMR cluster. On Linux, Unix and macOS you can create the tunnel with the following command:
ssh -i ~/mykeypair.pem -N -L 8157:ec2-###-##-##-###.compute-1.amazonaws.com:8088 hadoop@ec2-###-##-##-###.compute-1.amazonaws.com

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


- [Amazon S3 as Target](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/amazon-s3-requirements/amazon-s3-as-target)
- [Location Connection for Amazon S3](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-amazon-s3)

