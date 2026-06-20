# Location Properties - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/property-reference/location-properties

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/property-reference/location-properties/index.md)

# Location Properties


This section lists and describes the location properties.

A location property specifies the characteristics/attributes of a location in Fivetran HVR. This can include location connection parameters, location/database type, database version, method of capture, etc.

> **Note:** 
A property that is automatically discovered by HVR when it connects to a database/location is called discovered property. A user cannot specify/input value into a discovered property.

An array property and map property can store multiple values. The syntax for updating them from the [Command Line Interface (CLI)](https://fivetran.com/docs/hvr6/command-line-interface/managing-properties-in-cli) varies.


---

### ABFS_Account


**Argument**: *account*

**Description**: Name of the Azure Data Lake Storage Gen2 storage account.

This property is required for connecting HVR to an ADLS Gen2 location.

---

### ABFS_Authentication_Method


**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to Azure Data Lake Storage (ADLS) Gen2 server.

Valid values for *method* are:

- **SHARED_KEY**
- **CLIENT_CREDS**
- **USER_PASS**
- **MSI**
- **REFRESH_TOKEN**


For more information about these authentication methods, see section [Authentication Methods](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-data-lake-storage-requirements#authenticationmethods) in [Azure Data Lake Storage Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-data-lake-storage-requirements).

---

### ABFS_Container


**Argument**: *container*

**Description**: Name of the container available within the Azure Data Lake Storage Gen2 storage account (defined in [**ABFS_Account**](#abfsaccount)).

---

### ADL_Authentication_Method


**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to Azure Data Lake Storage Gen1 server.

Valid values for *method* are:

- **CLIENT_CREDS**
- **MSI**
- **REFRESH_TOKEN**


For more information about these authentication methods, see section [Authentication Methods](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-data-lake-storage-requirements#authenticationmethods) in [Azure Data Lake Storage Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/azure-data-lake-storage-requirements).

---

### Agent_Client_Kerberos_Keytab


**Argument**: *keytabfile*

**Description**: Directory path to the Kerberos keytab file that contains a security key for identifying the hub to the agent during authentication (when connecting hub to the agent). If defined, this keytab file will be used instead of the operating system defaults.

---

### Agent_Client_Kerberos_Principal


**Argument**: *principal*

**Description**: Kerberos principal name for identifying the hub to the agent during authentication (when connecting hub to the agent). If defined, this principal name will be used instead of the operating system defaults.

---

### Agent_Client_Kerberos_Ticket_Cache


**Argument**: *file*

**Description**: Directory path to the Kerberos ticket cache *file* for identifying the hub to the agent during authentication (when connecting hub to the agent). If defined, this ticket cache file will be used instead of the operating system defaults.

---

### Agent_Fingerprint


**Description**: This is a discovered property that stores the unique identifier (fingerprint) of the server on which the HVR Agent is installed.

---

### Agent_Host


**Argument**: *host*

**Description**: Hostname or IP-address of the server on which the [HVR Agent](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener) is installed/running.

---

### Agent_HVR_CONFIG


**Description**: This is a discovered property that stores the directory path of **HVR_CONFIG** for HVR Agent.

---

### Agent_HVR_HOME


**Description**: This is a discovered property that stores the directory path of **HVR_HOME** for HVR Agent.

---

### Agent_Operating_System


**Description**: This is a discovered property that stores the name of the operating system on which HVR Agent is installed/running.

---

### Agent_Oracle_RAC_Port


**Argument**: *port*

**Description**: Port number of the Oracle RAC database available on the remote server.

---

### Agent_Oracle_RAC_Service


**Argument**: *service*

**Description**: Service name of the Oracle RAC database available on the remote server. For example, **HVR1900**.

---

### Agent_Password


**Argument**: *password*

**Description**: Password for the HVR Agent (defined in [**Agent_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties)).

---

### Agent_Platform


**Description**: This is a discovered property that stores the name of the HVR platform (e.g, **linux_glibc2.12-x64-64bit**, **windows-x64-64bit**) used for installing the HVR Agent.

---

### Agent_Port


**Argument**: *port*

**Description**: TCP/IP port number of the [**HVR Agent**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener). This is used for connecting HVR Hub to the HVR Agent.

For Oracle RAC connection, this is the TCP/IP port number of the [**HVR Agent**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener) on the RAC nodes.

---

### Agent_Server_Kerberos_Principal


**Argument**: *principal*

**Description**: User specified Kerberos principal name for identifying the agent to the hub during authentication (when connecting hub to the agent).

---

### Agent_Server_Public_Certificate


**Argument**: *base64*

**Description**: The SSL public certificate file for the HVR Agent.

This property is discovered on first connection to the agent and verified for all future connections.

---

### Agent_User


**Argument**: *username*

**Description**: Username for the HVR Agent. This property is used for connecting HVR Hub to the HVR Agent.

---

### Agent_Version


**Description**: This is a discovered property that stores the version of the HVR Agent.

---

### Archive_Log_Format


**Argument**: *format*

**Description**: Describes the filename format (template) of the transaction log archive files stored in the directory specified by the [**Archive_Log_Path**](#archivelogpath) property.

The list of supported format variables and the default *format* string are database-specific:
Oracle
- **%d** - match numbers (zero or more decimal digits). Numbers matched using this variable are ignored by HVR.
- **%r** or **%R** - resetlogs ID
- **%s** or **%S** - log sequence number
- **%t** or **%T** - thread number
- **%z** or **%Z** - match alphanumeric characters. Characters matched using this variable are ignored by HVR.


> **Important:** 
Wildcard character ***** is not supported.


For more information about the format variables, refer to the article [LOG_ARCHIVE_FORMAT](https://docs.oracle.com/cd/B19306_01/server.102/b14237/initparams103.htm#REFRN10089) in Oracle's documentation.

When this location property is not defined, then by default HVR will query the database for Oracle's initialization property **LOG_ARCHIVE_FORMAT**.
SQL Server
- **%d** - database name
- **%Y** - year (up to 4 digit decimal integer)
- **%M** - month (up to 2 digit decimal integer)
- **%D** - day (up to 2 digit decimal integer)
- **%h** - hours (up to 2 digit decimal integer)
- **%m** - minutes (up to 2 digit decimal integer)
- **%s** - seconds (up to 2 digit decimal integer)
- **%n** - file sequence number (up to 64 bit decimal integer)
- **%%** - matches %
- ***** - wildcard, matches zero or more characters


> **Note:** 
- HVR uses the **%Y**, **%M**, **%D**, **%h**, **%m**, **%s** and **%n** values to sort and processes the log backup files in the correct (chronological) order.
- The combinations of the **%Y**, **%M**, **%D** and **%h**, **%m**, **%s** values are expected to form valid date and time values; however, no validation is performed.
- Any value that is missing from the *format* string is considered to be **0**.
- When sorting the files comparison is done in the following order: **%Y**, **%M**, **%D**, **%h**, **%m**, **%s**, **%n**.



This property has no default *format* value and must be specified if [**Archive_Log_Path**](#archivelogpath) property is defined.
SAP HANA
- **%v** - log volume ID
- **%p** - log partition ID
- **%s** - start sequence number
- **%e** - end sequence number
- **%t** - start timestamp (in milliseconds since UNIX epoch)
- **%%** - matches %
- ***** - wildcard, matches zero or more characters


> **Note:** 
The **%s**, **%e** and **%t** format variables are mandatory.


Defining this property is optional. When this property is not defined, the default *format* value is **log_backup_%v_%p_%s_%e.%t**.
Sybase ASE
- ***** - wildcard, matches zero or more characters
- **?** - matches any single character


Defining this property is optional. When this property is not defined, by default HVR scans all files available in the **Archive_Log_Path**.

---

### Archive_Log_Path


**Argument**: *dir*

**Description**: HVR will search for the transaction log archives in the specified directory (path) *dir*.

The behavior of this property is database-specific:
Oracle
HVR will search for the log archives in the specified directory *dir* in addition to the primary Oracle archive directory.

If the [**Capture_Method**](#capturemethod) is set to **ARCHIVE_ONLY** then HVR will search for the log archives in the directory *dir* only. Any process could be copying log archive files to this directory; the Oracle archiver (if another **LOG_ARCHIVE_DEST_***N* is defined), **RMAN**, or a simple shell script.

It should be ensured that the files in this directory are purged periodically, otherwise the directory will fill up.
SQL Server
HVR normally locates the transaction log backup files by querying the backup history table in the msdb database. Specifying this property tells HVR to search for the log backup files in the specified directory *dir* instead.

If this property is defined, then [**Archive_Log_Format**](#archivelogformat) must also be defined.
SAP HANA
HVR will search for the log backups in the directory *dir* in addition to the default log backup location for the source database. For HVR versions prior to 6.1.1/0 and 6.1.0/1, HVR will search for the log backups only in the specified directory *dir* instead of the default log backup location for the source database.
SAP NetWeaver on HANA
HVR will search for the log backups in the directory *dir* in addition to the default log backup location for the source database. For HVR versions prior to 6.1.1/0 and 6.1.0/1, HVR will search for the log backups only in the specified directory *dir* instead of the default log backup location for the source database.
Sybase ASE
HVR will search for the transaction log backups in the specified directory *dir*.

---

### AWS_Access_Key_Id


**Argument**: *keyid*

**Description**: Access key ID of IAM user for connecting HVR to Amazon S3.

This property is used together with [**AWS_Secret_Access_Key**](#awssecretaccesskey) when connecting HVR to Amazon S3 using IAM User Access Keys.

For more information about Access Keys, refer to [Understanding and Getting Your Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html) in AWS documentation.

---

### AWS_IAM_Role


**Argument**: *role*

**Description**: AWS IAM role name for connecting HVR to Amazon S3.

This property is used when connecting HVR to Amazon S3 using AWS Identity and Access Management (IAM) Role. This property may be used only if the HVR Agent or the HVR Hub System is running inside the AWS network on an EC2 instance and the AWS IAM role specified here should be attached to this EC2 instance. When a role is used, HVR obtains temporary Access Keys Pair from the EC2 server. For more information about IAM Role, refer to [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in AWS documentation.

---

### AWS_Secret_Access_Key


**Argument**: *key*

**Description**: Secret access key of IAM user for connecting HVR to Amazon S3.

This property is used together with [**AWS_Access_Key_Id**](#awsaccesskeyid) when connecting HVR to Amazon S3 using IAM User Access Keys.

---

### Azure_Auth_Proxy_Host


**Argument**: *host*

**Description**: Host name of the authentication proxy server used for connecting HVR to the Azure DLS server.

---

### Azure_Auth_Proxy_Password


**Argument**: *password*

**Description**: Password for the [**Azure_Auth_Proxy_User**](#azureauthproxyuser).

---

### Azure_Auth_Proxy_Port


**Argument**: *port*

**Description**: Port number of the authentication proxy server host used for connecting HVR to the Azure DLS server.

---

### Azure_Auth_Proxy_Scheme


**Argument**: *protocol*

**Description**: Protocol for the authentication proxy server host used for connecting HVR to the Azure DLS server.

Valid value for *protocol* is:

- **HTTP**: Use HTTP protocol.


---

### Azure_Auth_Proxy_User


Username for the authentication proxy server host used for connecting HVR to the Azure DLS server.

---

### Azure_OAuth2_Client_Id


**Argument**: *id*

**Description**: Client ID (or application ID) used to obtain Microsoft Entra ID (formerly Azure Active Directory) access token.

This property is required only if the authentication method ([**ABFS_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) or [**ADL_Authentication_Method**](#adlauthenticationmethod) or [**SqlServer_Authentication_Method**](#sqlserverauthenticationmethod)) is set to **CLIENT_CREDS** or **REFRESH_TOKEN**.

---

### Azure_OAuth2_Client_Secret


**Argument**: *key*

**Description**: Secret key of the [**Azure_OAuth2_Client_Id**](#azureoauth2clientid).

This property is required only if the authentication method ([**ABFS_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) or [**ADL_Authentication_Method**](#adlauthenticationmethod) or [**SqlServer_Authentication_Method**](#sqlserverauthenticationmethod)) is set to **CLIENT_CREDS**.

---

### Azure_OAuth2_Endpoint


**Argument**: *url*

**Description**: URL used for obtaining the bearer token with credential token.

Ensure that you are using the OAuth 2.0 endpoint. The URL path should include **v2.0**. The format for the endpoint URL is https://login.microsoftonline.com/<em>tenant</em>/oauth2/<b>v2.0</b>/token

This property is required only if the authentication method ([**ABFS_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) or [**ADL_Authentication_Method**](#adlauthenticationmethod) or [**SqlServer_Authentication_Method**](#sqlserverauthenticationmethod)) is set to **CLIENT_CREDS**.

---

### Azure_OAuth2_MSI_Port


**Argument**: *port*

**Description**: Port number for the REST endpoint of the token service exposed to localhost by the identity extension in the Azure VM.

The default value for this property is **50342**.

This property is required only if the authentication method ([**ADL_Authentication_Method**](#adlauthenticationmethod)} is set to **MSI**.

---

### Azure_OAuth2_MSI_Tenant


**Argument**: *url*

**Description**: URL for the REST endpoint of the token service exposed to localhost by the identity extension in the Azure VM.

For Azure Data Lake Storage, this property is required only if the authentication method ([**ABFS_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties)) is set to **MSI**.

---

### Azure_OAuth2_Password


**Argument**: *password*

**Description**: Password for [**Azure_OAuth2_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties).

---

### Azure_OAuth2_Refresh_Token


**Argument**: *path*

**Description**: Directory *path* to the text file containing the refresh token.

This property is required only if the authentication method ([**ABFS_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) or [**ADL_Authentication_Method**](#adlauthenticationmethod)) is set to **REFRESH_TOKEN**.

---

### Azure_OAuth2_User


**Argument**: *user*

**Description**: Username for the OAuth 2.0 authentication.

This property is required only if the authentication method ([**ABFS_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties)) is set to **USER_PASS**.

---

### Azure_Shared_Secret_Key


**Argument**: *account*

**Description**: Access key of the Azure storage account.

For Azure Data Lake Storage, this property is required only if the authentication method ([**ABFS_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties)) is set to **SHARED_KEY**.

---

### BigQuery_Region


**Description**: Geographic location of the dataset. For more information about dataset locations, refer to [Dataset Locations](https://cloud.google.com/bigquery/docs/locations) in [BigQuery](https://cloud.google.com/bigquery/docs/) Documentation.

A few examples - **US**, **europe-west4**, **us-west4**

---

### Capture_Checkpoint_Frequency


**Argument**: *secs*

**Description**: Checkpointing frequency in seconds for long running transactions, so the capture job can recover quickly when it restarts. Value *secs* is the interval (in seconds) at which the capture job creates checkpoints.

Thedefaultcheckpoint frequency is **300** seconds (5 minutes). If value **0** is set, checkpoints are not written.

Without checkpoints, capture jobs must rewind back to the start of the oldest open transaction, which can take a long time and may require access too many old DBMS log files (e.g. archive files).

The checkpoints are written into the **HVR_CONFIG/hubs/***hub***/channels/***channel***/locs/***location***/capckp** directory. If a transaction continues to make changes for a long period then successive checkpoints will not rewrite its same changes each time; instead the checkpoint will only write new changes for that transaction; for older changes it will reuse files written by earlier checkpoints.

Checkpoints are written only for long-running transactions. For example, if the checkpoint frequency is each 5 minutes but users always do an SQL commit within 4 minutes then checkpoints will never be written. However, if users keep transactions open for 10 minutes, then those transactions will be saved but shorter-lived ones in the same period will not.

The frequency with which capture checkpoints are written is relative to the capture jobs own clock, but it decides whether a transaction has been running long enough to be checkpointed by comparing the timestamps in its DBMS logging records. As a consequence, the maximum (worst-case) time that an interrupted capture job would need to recover (rewind back over all its open transactions) is its checkpoint frequency plus the amount of time it takes to reread the amount of changes that the DBMS can write in that period of time.

When a capture job is recovering it will only use checkpoints which were written before the 'capture cycle' was completed. This means that very frequent capture checkpointing (say every 10 seconds) is wasteful and will not speed up capture job recovery time.

> **Important:** 
This property is supported only for certain location types. For the list of supported location types, see [Log-based capture checkpointing using location property **Capture_Checkpoint_Frequency**](https://fivetran.com/docs/hvr6/capabilities/620#capcheckpoint) in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle)) section.


> **Note:** 
For SAP Hana, if any table in the channel includes a LOB column, this property is automatically disabled for that channel.


---

### Capture_Checkpoint_Retention


**Argument**: *secs*

**Description**: Retains capture checkpoint files up to the specified period *secs* (in seconds).

The retained checkpoint files are saved in the **HVR_CONFIG/hubs/***hub***/channels/***channel***/locs/***location***/capckpretain** directory.

Depending on the storage location defined in [**Capture_Checkpoint_Storage**](#capturecheckpointstorage), this directory can be located either on the capture location or hub.

---

### Capture_Checkpoint_Storage


**Argument**: *stor*

**Description**: Storage location of capture checkpoint files for quick capture recovery.

Valid values for *stor* are:

- 
**LOCATION** default: Checkpoint files are saved in a directory on capture location.

- 
**HUB**: Checkpoint files are saved in a directory on hub server.

Writing checkpoints on the hub is more expensive because extra data must be sent across the network. When capturing changes from an Oracle RAC, the checkpoint files should be stored on the hub server because the directory on the remote location where the capture job would otherwise write checkpoints may not be shared inside the RAC cluster, so it may not be available when the capture job restarts.



For both the storage locations, the checkpoint files are saved in the **HVR_CONFIG/hubs/***hub***/channels/***channel***/locs/***location***/capckp** directory.

When the capture job is restarted and if it cannot find the most recent checkpoint files (perhaps the contents of that directory have been lost during a failover) then it will write a warning and rewind back to the start of the oldest open transaction.

> **Important:** 
On busy systems, it is recommended to change this parameter only when there are no existing capture checkpoints, otherwise, there can be performance costs and superfluous warnings when the capture job starts for the first time with new settings.


---

### Capture_Method


**Argument**: *method*

**Description**: Method of reading/capturing changes from the DBMS log file.
Expand to view the valid values for this property
Valid values for *method* are:

- 
**DIRECT** default: Reads transaction log records directly from the DBMS log file using file I/O. This method is generally faster and more efficient than the SQL mode. The **DIRECT** log read method requires that HVR Agent is installed on the source database server.

For SQL Server, this capture method requires Windows Administrator privileges, and reduced permission models are not supported.

> **Important:** 
This capture method is supported only for certain location types. For the list of supported location types, see [Direct access to logs on a file system](https://fivetran.com/docs/hvr6/capabilities/620#caplogbasedlogreadmethoddirect) in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle)) section.


- 
**SQL**: Reads transaction log records using a special SQL function. The advantage of this method is that it reads change data over an SQL connection and does not require an HVR Agent to be installed on the source database server. The disadvantages of the **SQL** method is that it is slower than the **DIRECT** method and exposes additional load on the source database.

For SQL Server, this capture method supports reduced permission models but it may require incomplete row augmenting.

> **Important:** 
This capture method is supported only for certain location types. For the list of supported location types, see [Access to logs using SQL interface](https://fivetran.com/docs/hvr6/capabilities/620#caplogbasedlogreadmethoddirect) in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle)) section.


- 
**LOGMINER**: Reads data using Oracle's LogMiner. The advantage of this method is that it reads change data over an SQL connection and does not require an HVR Agent to be installed on the source database server. The disadvantages of the **LOGMINER** method is that it is slower than the **DIRECT** method and exposes additional load on the source database.

> **Important:** 
- 
This capture method is supported only for Oracle.

- 
Capture from Oracle using the **LOGMINER** method is deprecated in HVR 6.2 and will be removed from the product in HVR 6.3. Consider migrating to **BFILE** or **DIRECT** capture methods, or evaluate [Fivetran's Oracle Connector](https://fivetran.com/docs/connectors/databases/oracle/oracle-connector)




- 
**BFILE** <strong>Since</strong> v6.1.0/2: Reads Oracle's redo and archive log files through directory objects. HVR first tries to access the redo or archive log files through the existing directory objects or creates a new directory object if it do not exist. This method is comparable in speed with the **DIRECT** and **SQL** capture methods. The **BFILE** method does not require the HVR Agent to be installed on the source database machine.

> **Important:** 
This capture method is supported only for Oracle.


- 
**ARCHIVE_ONLY**: Reads data from the archived redo files in directory defined using [**Archive_Log_Path**](#archivelogpath) property and do not read anything from online redo files or the 'primary' archive destination. This allows the HVR process to reside on a different server than the Oracle DBMS or SQL Server and read changes from files that are sent to it by some remote file copy mechanism (e.g. **FTP**). The capture job still needs an SQL connection to the database for accessing dictionary tables, but this can be a regular connection.

Replication in this capture method can have longer delays in comparison with the 'online' mode.

For Oracle, to control the delays it is possible to force Oracle to issue an archive once per predefined period of time.

For Oracle RAC systems, delays are defined by the slowest or the least busy node. This is because archives from all threads have to be merged by SCNs in order to generate replicated data flow.

> **Important:** 
This capture method is supported only for certain location types. For the list of supported location types, see [Capture from Archive log files only](https://fivetran.com/docs/hvr6/capabilities/620#caplogbasedarchiveonly) in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle)) section.


- 
**DB_TRIGGER**: Capture changes through DBMS triggers generated by HVR, instead of using log-based capture.

> **Note:** 
In HVR UI, when [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location), the option **Database Triggers** is displayed only if HVR detects database triggers in the connected database. You can also manually make this option visible by executing the following command:
hvruserconfig <em>user_name</em> Show_Deprecated_Features=true


> **Important:** 
This capture method is supported only for certain location types. For the list of supported location types, see [Trigger-based capture](https://fivetran.com/docs/hvr6/capabilities/620#captrigbased) in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle)) section.

The trigger-based capture method ([**Capture_Method**](#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.





> **Important:** 
This property is supported only for location types from which HVR can capture changes. For the list of supported location types, see [Capture changes from location](https://fivetran.com/docs/hvr6/capabilities/620#capture) in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle)) section.


---

### Capture_Method_Unavailable


**Description**: This is a discovered property that stores information whether the location supports a specific capture method.

---

### Case_Sensitive_Names


**Argument**: true

**Description**: The **Case_Sensitive_Names** location property determines whether HVR treats database table and column names as case-sensitive.

When this property is set to true, HVR treats DBMS table and column names as case-sensitive. By default, for DBMSs that do not enforce case sensitivity, HVR converts table and column names to the default case convention of the DBMS (for example, uppercase for Oracle). Enabling **Case_Sensitive_Names** allows replication of tables and columns with mixed-case names or names that do not follow the DBMS default case convention.

For example, Oracle normally stores table names in uppercase (**MYTAB**). To replicate a table named **mytab** or **MyTab**, you must enable this location property.

For the list of DBMSes that support this parameter, see 'Treat DBMS table names and columns case sensitive' in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#configcasesensitivedbnames), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#configcasesensitivedbnames), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#configcasesensitivedbnames), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#configcasesensitivedbnames)).

> **Important:** 
For always case-sensitive DBMSes (such as MySQL and PostgreSQL), this location property has no effect. In these systems, HVR uses the table and column names exactly as the DBMS stores them internally. For the list of DBMSs where case-sensitivity is always enforced, see 'Always treat DBMS table names and columns as case-sensitive' in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#alwayscasesensitivedbnames), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#alwayscasesensitivedbnames), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#alwayscasesensitivedbnames), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#alwayscasesensitivedbnames)).


> **Important:** 
Columns with duplicate names that differ only by case are not supported within the same table (for example, **column1** and **COLUMN1**).


---

### Class


**Argument**: *class*

**Description**: This property specifies *class* of the database. For example, **oracle**, **sqlserver**, etc.

---

### Class_Flavor


**Description**: This is a discovered property that stores the flavor of the specific database [**Class**](https://fivetran.com/docs/hvr6/property-reference/location-properties). The combination of **Class** and **Class_Flavor** forms the location type.

Example: For Azure Database, the **Class** is **sqlserver** and **Class_Flavor** is **azure**.

---

### Class_Version


**Description**: This is a discovered property that stores the version of the database [**Class**](https://fivetran.com/docs/hvr6/property-reference/location-properties).

---

### Connection_Timezone_Name


<strong>Since</strong> 6.1.5/5

**Argument**: *timezone*

**Description**: Time zone for the Databricks location. Specifying value in this property ensures that the time zone of the HVR Agent and the Databricks database match. It is not required to define this property if the time zone is UTC. For example, **America/Los_Angeles**.

This parameter is applicable only for Databricks target locations.

---

### Copy_Yes_Path


**Argument**: *path*

**Description**: Directory *path* for storing the backup image of the loaded data when using the **COPY YES** option in the Db2 LUW’s **LOAD** utility.

This property enables bulk load logging for Db2 LUW target locations during HVR [Refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) and [Burst Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate#method) operations. When this property is set, HVR uses Db2’s **LOAD** utility with the **COPY YES** option. This allows the load operation to be logged in the Db2 recovery log, making it compatible with the [IBM HADR (High Availability Disaster Recovery)](https://www.ibm.com/docs/en/db2/11.5.x?topic=server-high-availability-disaster-recovery-hadr) configurations.

The value of this property must be a valid *path* to a local directory on the Db2 server.  You are responsible for maintaining and cleaning up files in this directory.

To use this property, you must configure the target Db2 database as recoverable by enabling archive logging. For detailed steps, see the [Enable Archive Logging](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-linux-unix-and-windows-requirements/db2-for-luw-as-source#enablearchivelogging) section in the Db2 for LUW as Source requirements.

---

### Database_Char_Encoding


**Description**: This is a discovered property that stores the character encoding of the database (defined in [**Database_Name**](#databasename)).

---

### Database_Client_Private_Key


**Argument**: *path*

**Description**: Directory *path* where the **.pem** file containing the client's SSL private key is located.

This property is required for enabling two way SSL.

Defining this property along with [**Database_Public_Certificate**](#databasepubliccertificate), [**Database_Client_Public_Certificate**](#databaseclientpubliccertificate), and [**Database_Client_Private_Key_Password**](#databaseclientprivatekeypassword) will enable two way SSL, which means, HVR will authenticate the Hive server by validating the SSL certificate shared by the Hive server.

---

### Database_Client_Private_Key_Password


**Argument**: *password*

**Description**: Password of the client's SSL private key specified in **Database_Client_Private_Key**.

This property is required for enabling two way SSL.

Defining this property along with [**Database_Public_Certificate**](#databasepubliccertificate), [**Database_Client_Public_Certificate**](#databaseclientpubliccertificate), and [**Database_Client_Private_Key**](#databaseclientprivatekey) will enable two way SSL, which means, HVR will authenticate the Hive server by validating the SSL certificate shared by the Hive server.

---

### Database_Client_Public_Certificate


**Argument**: *path*

**Description**: Directory *path* where the **.pem** file containing the client's SSL public certificate is located.

This property is required for enabling two way SSL.

Defining this property along with [**Database_Public_Certificate**](#databasepubliccertificate), [**Database_Client_Private_Key**](#databaseclientprivatekey), and [**Database_Client_Private_Key_Password**](#databaseclientprivatekeypassword) will enable two way SSL, which means, HVR will authenticate the Hive server by validating the SSL certificate shared by the Hive server.

---

### Database_Default_Case


<strong>Since</strong> v6.1.5/7

**Description**: This is a discovered property that stores the default case used in the database.

Available values:

- **upper**: Indicates uppercase.
- **lower**: Indicates lowercase.
- **preserve**: Indicates mixed case (both lower and upper cases).


---

### Database_Default_Schema


**Description**: This is a discovered property that stores the name of the default schema in the database ([**Database_Name**](#databasename)).

---

### Database_Host


**Argument**: *host*

**Description**: Hostname or IP-address of the server on which the database is running.

For Db2 for i, this is the hostname or IP-address of the Db2 for i system.

---

### Database_Name


**Argument**: *dbname*

**Description**: Name of the database.

For Db2 for i, this is the named database in Db2 for i. It could be on another (independent) auxiliary storage pool (IASP). The user profile's default setting will be used when no value is specified. Specifying ***SYSBAS** will connect a user to the SYSBAS database.

For Db2 for LUW and Db2 for z/OS, the following formats are supported for this property:

- alias for the database in Db2 for LUW or Db2 for z/OS
- *database***:***server***:***port*
- *database* is the name of the database in Db2 for LUW or Db2 for z/OS
- *server* can either be a hostname or an IP-address of the database server
- *port* is the TCP/IP port used for connecting to the database server




For BigQuery, this is the name of the [dataset](https://cloud.google.com/bigquery/docs/datasets-intro#datasets) in Google BigQuery.

For HANA, this is the name of the specific database in a multiple-container environment.

---

### Database_Nchar_Encoding


**Description**: This is a discovered property that stores the national character encoding of the database (defined in [**Database_Name**](#databasename)).

---

### Database_Password


**Argument**: *password*

**Description**: Password for the [**Database_User**](#databaseuser).

---

### Database_Port


**Argument**: *port*

**Description**: Port number on which the database (defined in [**Database_Host**](#databasehost)) server is expecting connections.

---

### Database_Public_Certificate


**Argument**: *path*

**Description**: Directory *path* where the **.pem** file containing the server's public SSL certificate signed by a trusted CA is located.

Defining this property will enable (one way) SSL, which means, HVR will authenticate the Hive server by validating the SSL certificate shared by the Hive server.

This property is also required for enabling two way SSL.

For enabling two way SSL, this property must be defined along with [**Database_Client_Public_Certificate**](#databaseclientpubliccertificate), [**Database_Client_Private_Key**](#databaseclientprivatekey), and [**Database_Client_Private_Key_Password**](#databaseclientprivatekeypassword).

---

### Database_Schema


**Argument**: *schema*

**Description**: Name of the default schema to be used for this connection.

---

### Database_User


**Argument**: *user*

**Description**: Username for connecting HVR to the database (defined in [**Database_Name**](#databasename)).

For Azure SQL Database, this is the user name and host name of the Azure SQL Database server. The format to be used is *username***@***hostname*.

For Sybase ASE, this property can be used only if the [**Sybase_Authentication_Method**](#sybaseauthenticationmethod) is set to **USER_PASS**.

For Teradata, this is the username for connecting HVR to the Teradata **Node**.

---

### Databricks_Authentication_Method


**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to Databricks server.

Valid values for *method* are:

- **USER_PASS** : Authenticate using the username and password.
- **PERSONAL_ACCESS_TOKEN** : Authenticate using the Databricks personal access tokens.
- **CLIENT_CREDS**  <strong>Since</strong> v6.1.5/9: Authenticate with a service principal using the OAuth access tokens.


---

### Databricks_Catalog


<strong>Since</strong> v6.1.0/33

**Argument**: *name*

**Description**: Catalog *name* in a Unity Catalog metastore. If the target database is implemented in the Unity Catalog, and if this property is not defined, Databricks will use the default catalog **hive_metastore**.

---

### Databricks_Client_Id


<strong>Since</strong> v6.1.5/9

**Argument**: *id*

**Description**: Client ID of your service principal, used to obtain the OAuth access token.

This property is required only if the [**Databricks_Authentication_Method**](#databricksauthenticationmethod) is set to **CLIENT_CREDS**.

---

### Databricks_Client_Secret


<strong>Since</strong> v6.1.5/9

**Argument**: *key*

**Description**: Secret key associated with the [**Databricks_Client_Id**](#databricksclientid) of your service principal. The key is used in combination with the [**Databricks_Client_Id**](#databricksclientid) to authenticate and obtain the OAuth access token.

This property is required only if the [**Databricks_Authentication_Method**](#databricksauthenticationmethod) is set to **CLIENT_CREDS**.

---

### Databricks_HTTP_Path


**Argument**: *url*

**Description**: URL for the Databricks compute resource. For more information, refer to [Azure Databricks](https://docs.microsoft.com/en-us/azure/databricks/integrations/bi/jdbc-odbc-bi#--odbc-configuration-and-connection-parameters) documentation.

---

### Databricks_Location


**Argument**: *path*

**Description**: Path for the external tables in Databricks.

For staging on AWS S3, this can be a mount path **/mnt/...** (optionally prefixed with **dbfs:**) or an **s3://** URL.

For staging on ADLS, this can be a mount path **/mnt/...** (optionally prefixed with **dbfs:**) or an **abfss://** URL.

For staging on GCS, this can be a mount path **/mnt/...** (optionally prefixed with **dbfs:**) or an **gs://** URL.

If a path is defined without specifying the URI **dbfs:/** or **abfss://** or **s3://** or **gs://**, it is assumed to be a mount path beginning with **dbfs:/**.

---

### Databricks_Location_ABFSS


**Argument**: *url*

**Description**: URL (**abfss://**) for the external tables in Databricks.

This property is required only if the **Databricks_Location** is set to a mount path (**/mnt/...** or **dbfs:/...**).

---

### Databricks_Location_GSS


**Argument**: *url*

**Description**: URL (**gs://**) for the external tables in Databricks.

This property is required only if the **Databricks_Location** is set to a mount path (**/mnt/...** or **dbfs:/...**).

---

### Databricks_Location_S3S


**Argument**: *url*

**Description**: URL (**s3s://**) for the external tables in Databricks.

This property is required only if the **Databricks_Location** is set to a mount path (**/mnt/...** or **dbfs:/...**).

---

### Databricks_Personal_Access_Token


**Argument**: *token*

**Description**: Databricks personal access token for your workspace.

This property is required only if the [**Databricks_Authentication_Method**](#databricksauthenticationmethod) is set to **PERSONAL_ACCESS_TOKEN**.

---

### Databricks_Transactions


<strong>Since</strong> 6.3.5/4

**Argument**: true

**Description**: If set to **true**, enables multi-statement transactions for target Databricks tables. This allows HVR to commit changes to target tables in such a way that recovery does not create duplicate rows.

When this property is set to **true**, all tables included in a transaction must be enabled for **catalog commits**. If the target table is not enabled for catalog commits, HVR will alter the table to enable catalog commits.

When this property is set to **true**, the default value for [**BurstCommitFrequency**](https://fivetran.com/docs/hvr6/action-reference/integrate#burstcommitfrequency) parameter in the [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) action is **TABLE** instead of **CYCLE**.

To set this property to **true**, the Databricks compute resource or SQL warehouse that is configured in the location must support **transactions**. In addition, the Databricks ODBC driver must be at least version 2.10.0.

> **Note:** 
As of version 2.10.0, the Databricks ODBC driver has been renamed from Simba Spark ODBC driver to Databricks ODBC driver.


---

### Databricks_Version_Recovery


<strong>Since</strong> 6.2.5/6

**Argument**: true

**Description**: If set to **true**, enables version-based recovery for target Databricks tables. This allows HVR to restore the table to its previous state if the **Integrate** job fails and avoid creating duplicate rows.

HVR achieves this by utilizing the [DESCRIBE HISTORY](https://docs.databricks.com/en/sql/language-manual/delta-describe-history.html) and [RESTORE TABLE ... TO VERSION AS OF ...](https://docs.databricks.com/en/sql/language-manual/delta-restore.html) statements.

When this property is set to **true**, and if [**BurstCommitFrequency**](https://fivetran.com/docs/hvr6/action-reference/integrate#burstcommitfrequency) parameter in the [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) action is set to **CYCLE**, HVR will treat it as **TABLE** to support version-based recovery. For best performance, we recommend using **TABLE**. Setting it to **STATEMENT** results in a higher number of SQL statements being issued.

When this property is set to **true**, it adds a new column (**last_successful_version**) to the burst state table. You do not need to recreate the table manually; if the additional column is missing, it will be automatically added.

> **Note:** 
This property does not handle recovery of enrichment rows. To prevent duplicates created by enrichment, enable enrichment cleanup by setting the **HVR_BURST_ENRICHMENT_CLEANUP** environment variable to **-1** or **1**.


---

### DB2i_Log_Journal


**Description**: Name of the Db2 for i journal from which data changes will be captured. It is mandatory to define this property when creating a Db2 for i capture location.

A channel can only contain tables that share the same journal. To capture changes from tables associated with different journals, use separate channels for each journal.

---

### DB2i_Log_Journal_Schema


**Description**: Schema or library of the Db2 for i journal ([**DB2i_Log_Journal**](#db2ilogjournal)).

It is mandatory to define this property when creating a Db2 for i capture location.

---

### DB2i_Log_Journal_SysSeq


**Description**: Capture from journal using ***SYSSEQ**. This property requires **DB2i_Log_Journal** and **DB2i_Log_Journal_Schema**.

> **Important:** 
Since HVR versions 6.2.0/2 and 6.1.0/64, it is not required to define this location property for capturing changes from journal.


---

### Db2_DB2INSTANCE


**Argument**: *instance*

**Description**: When using "Db2 client or Db2 server or Db2 Connect", the name of the Db2 *instance* must be specified.

When using "IBM Data Server Driver for ODBC and CLI" this property should not be defined.

---

### Db2_INSTHOME


**Argument**: *path*

**Description**: When using "Db2 client or Db2 server or Db2 Connect" the directory *path* of the Db2 installation must be specified.

When using "IBM Data Server Driver for ODBC and CLI" the directory *path* of the IBM Data Server Driver for ODBC and CLI installation on an HVR machine (e.g. **/distr/db2/driver/odbc_cli/clidriver**) must be specified.

---

### Db2_Use_SSL


<strong>Since</strong> 6.1.5/9

**Argument**: true

**Description**: Enable/disable (one way) SSL. If set to **true**, HVR authenticates the location connection by validating the SSL certificate shared by the database server.

For SSL connection configuration requirements on Linux, see [Configuration for SSL connection on Linux](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-i-requirements#configurationforsslconnectiononlinux).

---

### Description


**Argument**: *description*

**Description**: Description for location created in HVR.

---

### File_Host


**Argument**: *host*

**Description**: Hostname or IP-address of the server on which the file server is running.

---

### File_Password


**Argument**: *password*

**Description**: Password for the [**File_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties).

---

### File_Path


**Argument**: *path*

**Description**: Directory *path* where the files are replicated to or captured from.

For Amazon S3, this is the directory *path* in the S3 **BUCKET** where the files are replicated to or captured from.

For Azure Blob Storage, this is the directory path in the container (defined in [**WASB_Container**](#wasbcontainer)) where the files are replicated to or captured from.

For Azure Data Lake Storage Gen1, this is the directory *path* where the files are replicated to or captured from.

For Azure Data Lake Storage Gen2, this is the directory path in container (defined in [**ABFS_Container**](#abfscontainer)) where the files are replicated to or captured from.

For Google Cloud Storage, this is the directory *path* in the Google Cloud Storage **BUCKET** where the files are replicated to or captured from.

---

### File_Port


**Argument**: *port*

**Description**: Port number on which the file server (defined in [**File_Host**](#filehost)) is expecting connections.

---

### File_Proxy_Host


**Argument**: *host*

**Description**: Host name of the proxy server used for connecting HVR to the file server (defined in [**File_Host**](#filehost)).

---

### File_Proxy_Password


**Argument**: *password*

**Description**: Password for the [**File_Proxy_User**](#fileproxyuser).

---

### File_Proxy_Port


**Argument**: *port*

**Description**: Port number for the proxy server (defined in [**File_Proxy_Host**](#fileproxyhost)) used for connecting HVR to the file server ([**File_Host**](#filehost)).

---

### File_Proxy_Scheme


**Argument**: *protocol*

**Description**: Protocol for the proxy server (defined in [**File_Proxy_Host**](#fileproxyhost)) used for connecting HVR to the file server (defined in [**File_Host**](#filehost)).

Valid values for *protocol* are:

- **HTTP**
- **SOCKS4**
- **SOCKS4A**
- **SOCKS5**
- **SOCKS5H**


---

### File_Proxy_User


**Argument**: *username*

**Description**: Username for the proxy server (defined in [**File_Proxy_Host**](#fileproxyhost)) used for connecting HVR to the file server (defined in [**File_Host**](#filehost)).

---

### File_Scheme


**Argument**: *protocol*

**Description**: Protocol for connecting HVR to the file server (defined in [**File_Host**](#filehost)).

Valid values supported for *protocol* are location type-specific:
Amazon S3
- **S3S**
- **S3**

Azure Blob Storage
- **WASBS**
- **WASB**

Azure Data Lake Storage
- **ABFSS** (applicable only for Azure DLS Gen2)
- **ABFS** (applicable only for Azure DLS Gen2)
- **ADL** (applicable only for Azure DLS Gen1)

File/FTP/SFTP
- **FTP**
- **FTPS**
- **SFTP**

Google Cloud Storage
- **GSS**
- **GS**

Sharepoint / WebDAV
- **WEBDAVS**
- **WEBDAV**


---

### File_State_Directory


**Argument**: *path*

**Description**: Directory *path* for internal state files used by HVR during file replication. By default, these files are created in sub-directory **_hvr_state** which is created inside the file location top directory.

If *path* is relative (e.g. **../work**), then the path used is relative to the file location's top directory. The state directory can either be defined to be a path inside the location's top directory or put outside this top directory. If the state directory is on the same file system as the file location's top directory, then HVR integrates file move operations will be 'atomic', so users will not be able to see the file partially written. Defining this property on a SharePoint/WebDAV integrate location ensures that the SharePoint version history is preserved.

---

### File_State_Directory_Is_Local


**Argument**: true

**Description**: If set to **true**, the directory specified in [**File_State_Directory**](#filestatedirectory) is stored on the local drive of the file location's server.

If this property is not set to **true** or enabled, then by default the internal state files are stored in file location. For example, in Amazon S3, by default the state directory is stored in the S3 bucket.

---

### File_User


**Argument**: *username*

**Description**: Username for connecting HVR to the file server (defined in [**File_Host**](#filehost)).

---

### Force_Case


<strong>Since</strong> v6.1.0/34

**Argument**: *sensitivity*

**Description**: Manage case *sensitivity* of object names created in the target DBMS tables. This property applies to [Activating Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication), [Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), or [Compare](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data).

Valid values for case *sensitivity* are:

- **no** default: Create table and column names in the same case as received from the source, which can be either lowercase or uppercase.
- **upper**: Create table and column names in uppercase.
- **lower**: Create table and column names in lowercase.


> **Important:** 
This property is applicable only for [Databricks](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/databricks-requirements/databricks-as-target#columnnamesforcedcase) (since 6.1.0/37) and [PostgreSQL](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements/postgresql-as-target#tableandcolumnnamesforcedcase) (since 6.1.0/34). Databricks supports only lowercase table names, so this property affects only column names.


---

### FTP_Encryption_Type


**Argument**: *type*

**Description**: Encryption type used for connecting HVR to the file server (defined in [**File_Host**](#filehost)). This is applicable only if **File_Scheme** is set to **FTP**.

Valid values for *type* are:

- **SSL**
- **TLS**


---

### GCloud_Authentication_Method


**Argument**: *method*

**Description**: Authentication method for connecting HVR to the Google Cloud server (Cloud Storage and Google BigQuery).

Valid values supported for *method* are location type-specific:
Google Cloud Storage
- **OAUTH_ENV**: Authentication (OAuth) using the credentials (service account key) fetched from the environment variable **GOOGLE_APPLICATION_CREDENTIALS**. For more information about setting this [environment variable](https://cloud.google.com/docs/authentication/getting-started#setting_the_environment_variable), refer to the [Google Cloud](https://cloud.google.com/docs) documentation.
- **OAUTH_FILE**: Authentication (OAuth) using the credentials supplied in the service account key file ([**GCloud_OAuth_File**](#gcloudoauthfile)). For more information about creating the [service account key file](https://cloud.google.com/docs/authentication/getting-started#creating_a_service_account), refer to the [Google Cloud](https://cloud.google.com/docs/) documentation.
- **HMAC**: Authentication using the credentials supplied as hash-based message authentication code (HMAC) keys, which comprises an Access key ([**GS_HMAC_Access_Key_Id**](#gshmacaccesskeyid)) and a Secret ([**GS_HMAC_Secret_Access_Key**](#gshmacsecretaccesskey)). For more information about [HMAC keys](https://cloud.google.com/storage/docs/authentication/hmackeys), refer to the [Google Cloud](https://cloud.google.com/docs) documentation.

Google BigQuery
- **OAUTH_ENV**: Authentication (OAuth) using the credentials (service account key) fetched from the environment variable **GOOGLE_APPLICATION_CREDENTIALS**. For more information about setting this [environment variable](https://cloud.google.com/docs/authentication/getting-started#setting_the_environment_variable), refer to the [Google Cloud](https://cloud.google.com/docs) documentation.
- **OAUTH_FILE**: Authentication (OAuth) using the credentials supplied in the service account key file ([**GCloud_OAuth_File**](#gcloudoauthfile)). For more information about creating the [service account key file](https://cloud.google.com/docs/authentication/getting-started#creating_a_service_account), refer to the [Google Cloud](https://cloud.google.com/docs/) documentation.


---

### GCloud_Email


**Argument**: *email*

**Description**: Service account email for connecting HVR to the Google BigQuery server.

---

### GCloud_OAuth_Env


**Argument**: true

**Description**: If set to **true**, enables OAuth 2.0 protocol based authentication for connecting HVR to the Google Cloud Storage.

This method connects using the credentials fetched from the environment variable **GOOGLE_APPLICATION_CREDENTIALS**. For more information about configuring this environment variable, see [Getting Started with Authentication](https://cloud.google.com/docs/authentication/getting-started) in [Google Cloud Storage](https://cloud.google.com/storage/docs/) documentation.

---

### GCloud_OAuth_File


**Argument**: *path*

**Description**: Directory *path* for the service account key file (JSON) used in OAuth 2.0 protocol based authentication.

This property is required only if [**GCloud_Authentication_Method**](#gcloudauthenticationmethod) is set to **OAUTH_FILE**.

---

### GCloud_Project


**Argument**: *id*

**Description**: ID of the google cloud project. For more information about google cloud projects, refer to [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in [BigQuery](https://cloud.google.com/bigquery/docs) Documentation.

---

### GS_Bucket


**Argument**: *bucket*

**Description**: Name or IP address of the Google Cloud Storage bucket.

---

### GS_Bucket_Region


**Argument**: *region*

**Description**: Geographic location of the dataset. For more information about dataset locations, refer to Dataset Locations in BigQuery Documentation.

---

### GS_HMAC_Access_Key_Id


**Argument**: *id*

**Description**: The HMAC access ID of the service account.

This property is required only if [**GCloud_Authentication_Method**](#gcloudauthenticationmethod) is set to **HMAC** when connecting HVR to the Google Cloud Storage.

---

### GS_HMAC_Secret_Access_Key


**Argument**: *key*

**Description**: The HMAC secret of the service account.

This property is required only if [**GCloud_Authentication_Method**](#gcloudauthenticationmethod) is set to **HMAC** when connecting HVR to the Google Cloud Storage.

---

### GS_Storage_Integration


**Argument**: *name*

**Description**: Integration name of the google cloud storage.

---

### Hana_Backint_Executable_Path


**Argument**: *path*

**Description**: Directory *path* for the Backint application installed on the same node as the HVR.

---

### Hana_Backint_Configuration_Path


**Argument**: *path*

**Description**: Directory *path* for the Backint configuration on the same node as the HVR.

---

### HANA_Root_Keys_Backup_Password


**Argument**: *password*

**Description**: Password for encrypting root key backups in SAP HANA.

This should be same as the password set for encrypting root key backups in SAP HANA.

---

### HDFS_Kerberos_Credential_Cache


**Argument**: *path*

**Description**: Directory *path* for the Kerberos ticket cache file.

It is not required to define this property if **keytab** file is used for authentication or if Kerberos is not used on the Hadoop cluster.

For more information about using Kerberos authentication, see [HDFS Authentication and Kerberos](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-hdfs-requirements/hdfs-authentication-and-kerberos).

---

### HDFS_Namenode


**Argument**: *host*

**Description**: Hostname of the HDFS NameNode.

---

### Hive_Authentication_Method


**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to Hive Server 2.

This property is required only if [**Hive_Server_Type**](#hiveservertype) is set to **2**.

Valid values for *method* are:

- **NONE**
- **USER**
- **USER_PASS**
- **KERBEROS**
- **HDINSIGHT**


---

### Hive_HTTP_Path


**Argument**: *url*

**Description**: The partial URL corresponding to the Hive server.

This property is required only if [**Hive_Thrift_Transport**](#hivethrifttransport) is set to **HTTP**.

---

### Hive_Kerberos_Host


**Argument**: *host*

**Description**: Fully Qualified Domain Name (FQDN) of the Hive server host. This is the host part of Kerberos principal of the Hive server. For example, if the principal is "hive/example.host@EXAMPLE.REALM" then "example.host" should be specified here.

The value for this property may be set to **_HOST** to use the Hive server hostname as the domain name for Kerberos authentication.

If [**Hive_Service_Discovery_Mode**](#hiveservicediscoverymode) is set to **NONE**, then the driver uses the value specified in the Host connection attribute.

If [**Hive_Service_Discovery_Mode**](#hiveservicediscoverymode) is set to **ZOOKEEPER**, then the driver uses the **Hive Server 2** host name returned by the ZooKeeper.

This property is required only if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **Kerberos**.

---

### Hive_Kerberos_Realm


**Argument**: *realm*

**Description**: Realm of the Hive Server 2 host.

It is not required to specify any value in this property if the realm of the Hive Server 2 host is defined as the default realm in Kerberos configuration.

This property is required only if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **Kerberos**.

---

### Hive_Kerberos_Service


**Argument**: *name*

**Description**: Kerberos service principal name of the Hive server. This is the service name part of Kerberos principal of the Hive server.

For example, if the Kerberos service principal is **hive/example.host.com@EXAMPLE.REALM** then **hive** should be specified in this property.

This property is required only if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **Kerberos**.

---

### Hive_Server_Type


**Argument**: *type*

**Description**: Type of the Hive server.

Valid values for *type* are:

- **1**: HVR will connect to Hive Server 1 instance.
- **2**: HVR will connect to Hive Server 2 instance.


---

### Hive_Service_Discovery_Mode


**Argument**: *mode*

**Description**: Mode for connecting HVR to Hive Server 2.

This property is required only if [**Hive_Server_Type**](#hiveservertype) is set to **2**.

Valid values for *mode* are:

- **NONE**: HVR connects to Hive Server 2 without using the ZooKeeper service.
- **ZOOKEEPER**: HVR discovers Hive Server 2 services using the ZooKeeper service.


---

### Hive_Thrift_Transport


**Argument**: *protocol*

**Description**: Transport protocol to use in the Thrift layer.

This property is required only if [**Hive_Server_Type**](#hiveservertype) is set to **2**.

Valid values for *protocol* are:

- **BINARY** (This value can be used only if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **NONE** or **USER_PASS**.)
- **SASL** (This value can be used only if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **USER** or **USER_PASS** or **KERBEROS**.)
- **HTTP** (This value can be used only if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **NONE** or **USER_PASS** or **KERBEROS** or **HDINSIGHT**.)


> **Note:** 
For information about determining which Thrift transport protocols your Hive server supports, refer to [HiveServer2 Overview](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Overview) and [Setting Up HiveServer2](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2) sections in [Hive documentation](https://cwiki.apache.org/confluence/display/Hive/Home).


---

### Hive_Zookeeper_Namespace


**Argument**: *namespace*

**Description**: Namespace on ZooKeeper under which Hive Server 2 nodes are added.

This property is required only if [**Hive_Service_Discovery_Mode**](#hiveservicediscoverymode) is set to **ZooKeeper**.

---

### Ingres_II_SYSTEM


**Argument**: *path*

**Description**: Directory *path* where the Actian Vector or Ingres database is installed.

---

### Intermediate_Directory


**Argument**: *path*

**Description**: Directory *path* for storing 'intermediate files' that are generated during [compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare#directfilecompare). Intermediate files are generated while performing direct file or online compare.

If this property is not defined, then by default the intermediate files are stored in *integratedir***/_hvr_intermediate** directory. The *integratedir* is the replication directory ([**File_Path**](#filepath)) defined while creating a file location.

---

### Intermediate_Directory_Is_Local


**Argument**: true

**Description**: If set to **true**, the directory specified in [**Intermediate_Directory**](#intermediatedirectory) is stored on the local drive of the file location's server.

If not set to **true**, then by default the intermediate files are stored in file location. For example, in Amazon S3, by default the intermediate directory is stored in the S3 bucket.

---

### Kafka_Authentication_Method


**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to Kafka server (**Broker**).

Valid values for *method* are:

- **NONE**
- **USER_PASS**
- **KERBEROS**
- **SCRAM-SHA-256** <strong>Since</strong> v6.3.5/0
- **SCRAM-SHA-512** <strong>Since</strong> v6.3.5/0


> **Important:** 
On Linux, to use any of the Kafka authentication methods (**USER_PASS**, **KERBEROS**, **SCRAM-SHA-256**, or **SCRAM-SHA-512**), HVR requires the library **libsasl2.so.2** to be installed. For more information, see section [Installation Dependencies](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements#installationdependencies) in [Apache Kafka Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements).


---

### Kafka_Brokers


list:*host*, *ports*

Hostname or IP address of the Kafka broker server(s) along with the TCP port that the Kafka server uses to listen for client connections.

The default port is **9092**.

This is an array property that can store multiple values.

---

### Kafka_Default_Topic


**Argument**: *topic*

**Description**: Kafka *topic* to which the messages are written.

You can use strings/text or expressions as Kafka topic name. Following are the expressions to substitute capture location or table or schema name as topic name:

- **{hvr_cap_loc}** - for capture location name.
- **{hvr_tbl_name}** - for current table name. This is only allowed if the channel is defined with tables.
- **{hvr_schema}**- for schema name of the table. This is only allowed if the channel contains tables that have action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) with parameter [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema)=*my_schema* explicitly defined for these tables on the target file location.


The Kafka topics used should either exist already in the Kafka broker or it should be configured to auto-create Kafka topic when HVR sends a message.

---

### Kafka_Kerberos_Client_Principal


**Argument**: *host*

**Description**: Full Kerberos principal of the client connecting to the Kafka server. This property definition is required only on Linux/Unix.

This property is required only if [**Kafka_Authentication_Method**](#kafkaauthenticationmethod) is set to **KERBEROS**.

---

### Kafka_Kerberos_Keytab


**Argument**: *path*

**Description**: Directory *path* where the Kerberos keytab file containing key for the **Kafka_Kerberos_Client_Principal** is located.

This property is required only if [**Kafka_Authentication_Method**](#kafkaauthenticationmethod) is set to **KERBEROS**.

---

### Kafka_Kerberos_Service


**Argument**: *name*

**Description**: Kerberos Service Principal Name (SPN) of the Kafka server.

This property is required only if [**Kafka_Authentication_Method**](#kafkaauthenticationmethod) is set to **KERBEROS**.

---

### Kafka_Message_Bundling


**Argument**: *mode*

**Description**: Number of messages written (bundled) into single Kafka message. Regardless of the file format chosen, each Kafka message contains one row by default.

Valid values for *mode* are:

- **ROW**: Each Kafka message contains a single row; this mode does not support bundling of multiple rows into a single message. Note that this mode causes a key-update to be sent as multiple Kafka messages (first a 'before update' with **hvr_op=3**, and then an 'after update' with **hvr_op=2**).
- **CHANGE**: Each Kafka message is a bundle containing two rows (a 'before update' and an 'after update' row) whereas messages for other changes (e.g. insert and delete) contain just one row. During refresh there is no concept of changes, so each row is put into a single message. Therefore in that situation, this behavior is the same as mode **ROW**.
- **TRANSACTION**: During replication, each message contains all rows in the original captured transaction. An exception is if the message size looks like it will exceed the bundling threshold (see property [**Kafka_Message_Bundling_Threshold**](https://fivetran.com/docs/hvr6/property-reference/location-properties)). During refresh, all changes are treated as if they are from a single capture transaction so this mode behaves the same as bundling mode **THRESHOLD**.
- **THRESHOLD**: Each Kafka message is bundled with rows until it exceeds the message bundling threshold (see property [**Kafka_Message_Bundling_Threshold**](https://fivetran.com/docs/hvr6/property-reference/location-properties)).


> **Important:** 
- 
When the *mode* is set to **TRANSACTION** or **THRESHOLD** and if the name of the Kafka topic contains an expression such as **{hvr_tbl_name}** then the rows of different tables will not be bundled into the same message.

- 
If [**Kafka_Schema_Registry**](#kafkaschemaregistry) is defined, you must use only the **ROW** *mode* for message bundling. Using any other *mode* is unsupported and may lead to data integrity issues.

- 
Confluent's Kafka Connect only allows certain message formats and does not allow any message bundling, therefore **Kafka_Message_Bundling** must either be undefined or set to **ROW**. Bundled messages simply consist of the contents of several single-row messages concatenated together.




---

### Kafka_Message_Bundling_Threshold


**Argument**: *threshold*

**Description**: Threshold (in bytes) for bundling rows in a Kafka message. Rows continue to be bundled into the same message until this threshold is exceeded, after which, the message is sent and new rows are bundled into the next message.

The default value is **800,000** bytes.

This property may be defined only if [**Kafka_Message_Bundling**](#kafkamessagebundling) is set to **TRANSACTION** or **THRESHOLD**.

> **Note:** 
By default, the maximum size of a Kafka message is 1,000,000 bytes; HVR will not send a message exceeding this size and will instead give a fatal error.


---

### Kafka_Message_Compress


**Argument**: *algorithm*

**Description**: HVR will configure the Kafka transport protocol to compress message sets transmitted to Kafka broker using one of the available *algorithms*. The compression allows to decrease the network latency and save disk space on the Kafka broker. Each message set can contain more than one Kafka message. For more information, see section Kafka Message Bundling and Size in [Apache Kafka Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements).

Valid values for the *algorithm* are:

- **NONE** (recommended if action [**FileFormat**](https://fivetran.com/docs/hvr6/action-reference/fileformat) is defined with property [**Compress**](https://fivetran.com/docs/hvr6/action-reference/fileformat#compress) or [**AvroCompression**](https://fivetran.com/docs/hvr6/action-reference/fileformat))
- **LZ4**
- **GZIP**
- **SNAPPY**


> **Important:** 
**LZ4** compression is not supported on the Windows platform if Kafka broker version is less than 1.0.


---

### Kafka_Schema_Registry


**Argument**: *url*

**Description**: URL (**http://** or **https://**) of the schema registry to use Confluent compatible messages in Avro format.

For HVR versions until 6.1.0/27, if the basic authentication is configured for the schema registry, then the login credentials (username and password) must be specified in the URL. The format is **http**[**s**]**://***user***:***password***@***schemaregistry_url***:***port*

For HVR versions since 6.1.0/28, the login credentials (username and password) must be specified in the location properties **Kafka_Schema_User** and **Kafka_Schema_Registry_Password**.

For more information, see section [Kafka Message Format](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements/apache-kafka-as-target#kafkamessageformat) in [Apache Kafka Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements).

---

### Kafka_Schema_Registry_Password


<strong>Since</strong> v6.1.0/28

**Argument**: *password*

**Description**: Password of the Kafka schema registry user (**Kafka_Schema_User**).

---

### Kafka_Schema_User


<strong>Since</strong> v6.1.0/28

**Argument**: *url*

**Description**: Username for accessing the Kafka schema registry.

If the basic authentication is configured for the schema registry, then the login credentials (username and password) must be specified.

---

### Kafka_Schema_Registry_Format


**Argument**: *format*

**Description**: Format of the Kafka message. For more information, see section [Kafka Message Format](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements/apache-kafka-as-target#kafkamessageformat) in [Apache Kafka Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/apache-kafka-requirements).

Valid values for *format* are:

- **AVRO**
- **JSON**


---

### Key_Only_Trigger_Tables


**Argument**: true

**Description**: If set to **true**, then write only the key columns into the capture table to improve the performance of trigger-based capture.

The non-key columns are extracted using an OUTER JOIN from the capture table to the replicated table. Internally HVR uses the same OUTER JOIN technique to capture changes to long columns (e.g., **long varchar**). This is necessary because DBMS rules/triggers do not support long data types.

The disadvantage of this technique is that 'transient' column values can sometimes be replicated, for example, if a DELETE happens just after the toggle has changed, then the OUTER JOIN could produce a **NULL** for a column which never had that value.

This property requires [**Capture_Method**](#capturemethod) set to **DB_TRIGGER**.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


---

### Log_Truncater


**Argument**: *method*

**Description**: Specify who advances the SQL Server/Sybase ASE transaction log truncation point (truncates the log).

Valid values for *method* are database-specific:
SQL Server
- 
**CAP_JOB** default: This method is used to indicate that the capture job regularly calls **sp_repldone** to unconditionally release the hold of the truncation point for replication. When this method is selected and [**Activate Replication**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate) ([**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate)) is run, depending on the value of the property **Supplemental_Logging**, HVR will also drop/disable the SQL Server agent jobs that are created when CDC tables are created through the CDC stored procedures and the agent jobs related to data distribution. As a result, the additional impact of auxiliary database objects to enable supplemental logging is minimized. For example, the CDC tables are not populated (and the space allocation increased) because the agent job to do this is dropped. Multiple [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) jobs can be set up on a single database with method **CAP_JOB** selected. However, note that if no [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) job is running with the CDC tables and/or Articles in place, the transaction log will grow because the truncation point for replication is not released. Do not set this method if there is another data replication solution or the database uses CDC tables.

- 
**CAP_JOB_RETAIN**: This method should be used when capturing from a SQL Server database with the recovery mode set to Simple Recovery. The capture job moves the truncation point of the transaction log forward by calling the stored procedure **sp_repldone** at the end of each sub-cycle. Only part of the transaction log that has already been processed (captured) is marked for truncation (this is different from the **CAP_JOB** mode, where all records in the transaction log are marked for truncation, including those that have not been captured yet). This value is not compatible with multi-capture and does not allow for coexistence with a third party replication solution. This setting will also result in SQL Server's agent jobs being dropped/disabled, so the transaction log will grow when the capture job is not running and CDC tables and/or Articles are still in place. Do not set this method if another data replication solution is in place or CDC tables are used in the database.

- 
**LOGRELEASE_TASK**: This method should be used if a separate job/task is created to release the truncation point for replication. For example, schedule a separate SQL Server Agent job to unconditionally call **sp_repldone** at an interval. Choosing the method **LOGRELEASE_TASK** will also result in SQL Server's agent jobs being dropped/disabled. However, as long as the scheduled log release task runs, the truncation point for replication is released, even if the capture job(s) is(are) not running. This method should only be used in conjunction with another replication or CDC solution if the log release task that is scheduled is aware of the requirements of the other solution.

- 
**NATIVE_DBMS_AGENT**: This method should be used if native replication and/or CDC tables are used on the database. With this method, HVR will not drop/disable the native SQL Server agent jobs that are created when CDC tables and/or Articles are created. HVR will also not interfere with the release of the truncation point for replication. If CDC tables are used to enable supplemental logging it may cause I/O overhead (SQL Server jobs copy each change to a CDC table, which no-one uses).


Sybase ASE
- 
**NONE** default: HVR does not enable the secondary truncation point during [replication activation](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication). However, if the secondary truncation point was enabled outside of HVR, it remains enabled.

In the case of [replication deactivation](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication), HVR does not attempt to disable the secondary truncation point.

Not using truncation points allows multiple systems to capture from the same database. Still, you must ensure that older transaction files are retained and available as transaction dumps until they are replicated. HVR will search for the transaction dumps in the directory specified in [**Archive_Log_Path**](#archivelogpath).

- 
**CAP_JOB_RETAIN**: This method ensures that Sybase transactions are always available for HVR. HVR enables the secondary truncation point during [replication activation](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication).

In the case of [replication deactivation](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication), HVR attempts to disable the secondary truncation point, unless there are objects enabled for replication still present in the database. In this case, deactivation initially disables replication for all requested source tables (by default, for all tables in the channel). Subsequently, HVR performs a check to ascertain if any replicated objects, such as tables or stored procedures, persist in the database. The secondary truncation point is only disabled if there are no objects enabled for replication.

> **Important:** 
Log device usage will grow if the capture job is idle. Additionally, this value is incompatible with multi-capture and does not allow for coexistence with a third party replication solution.




---

### Log_Truncater_Unavailable


**Description**: This is a discovered property that stores information regarding HVR support for log truncation.

---

### MySQL_CA_Certificate_File


<strong>Since</strong> v6.1.5/3

**Argument**: *path*

**Description**: Absolute *path* of the Certificate Authority (CA) certificate file. The value in this field must point to the same certificate used by the server. If a value is specified in this field, the server's Common Name (CN) in its certificate is verified against the hostname used for the connection. If there is a mismatch between the CN and the hostname, the connection will be rejected.

This property requires [**MySQL_Use_SSL**](#mysqlusessl).

This property can be defined only for Aurora MySQL, MariaDB, and MySQL.

---

### MySQL_Client_Pub_Cert_File


<strong>Since</strong> v6.1.5/3

**Argument**: *path*

**Description**: Absolute *path* of the client public key certificate file.

This property requires [**MySQL_Use_SSL**](#mysqlusessl).

This property can be defined only for Aurora MySQL, MariaDB, and MySQL.

---

### MySQL_Client_Priv_Key_File


<strong>Since</strong> v6.1.5/3

**Argument**: *path*

**Description**: Absolute *path* of the client private key file.

This property requires [**MySQL_Use_SSL**](#mysqlusessl).

This property can be defined only for Aurora MySQL, MariaDB, and MySQL.

---

### MySQL_Server_Pub_Key_File


<strong>Since</strong> v6.1.5/3

**Argument**: *path*

**Description**: Absolute *path* to a **.pem** file containing the client-side copy of the public key required by the server for RSA key pair-based password exchange.

This is relevant only for clients using the **sha256_password** authentication plugin. It is ignored for accounts using other authentication plugins or when RSA-based password exchange is not in use, such as when the client connects to the server via a secure connection.

---

### MySQL_SSL_Cipher


<strong>Since</strong> v6.1.5/3

**Argument**: *cipher*

**Description**: Encryption algorithm (*cipher*) permitted for establishing a secure connection between HVR and the database server. If this field is left empty, a default set of ciphers will be used. To specify multiple ciphers, list them as comma-separated values.

For the connection to succeed, both HVR and the database server must support at least one common cipher from the specified list. The SSL/TLS library will then select the highest-priority cipher compatible with the provided certificate.

---

### MySQL_SSL_CRL_File


<strong>Since</strong> v6.1.5/3

**Argument**: *path*

**Description**: Absolute *path* to a file containing one or more revoked X.509 certificates to use for TLS.

---

### MySQL_SSL_Min_TLS_Version


<strong>Since</strong> v6.1.5/3

**Argument**: *tls_version*

**Description**: Minimum protocols the client permits for a TLS connection.

Valid values for *tls_version* are:

- **TLS v1**
- **TLS v1.1**
- **TLS v1.2**
- **TLS v1.3**


This property requires [**MySQL_Use_SSL**](#mysqlusessl).

This property can be defined only for Aurora MySQL, MariaDB, and MySQL.

---

### MySQL_Use_SSL


<strong>Since</strong> v6.1.5/3

**Argument**: true

**Description**: Enable/disable (one way) SSL. If set to **true**, HVR authenticates the location connection by validating the SSL certificate shared by the database server.

This property can be defined only for Aurora MySQL, MariaDB, and MySQL.

---

### MS_Fabric_Authentication_Method


**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to SQL database in Microsoft Fabric.

Valid values for *method* are:

- **ACCESS_TOKEN**: Authenticates using an access token obtained through OAuth2 client credentials.
- **AZURE_ACTIVE_DIRECTORY**: Authenticates using Microsoft Entra ID (formerly Azure Active Directory) username and password.


This property can be defined only for [SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

For more information about these authentication methods, see section [Authentication Methods](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements#authenticationmethods) in [SQL database in Microsoft Fabric Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

---

### MS_Fabric_Entra_Password


**Argument**: *password*

**Description**: Password for the Microsoft Entra ID user specified in [**MS_Fabric_Entra_User**](#msfabricentrauser).

This property is required when [**MS_Fabric_Authentication_Method**](#msfabricauthenticationmethod) is set to **AZURE_ACTIVE_DIRECTORY**.

This property can be defined only for [SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

---

### MS_Fabric_Entra_User


**Argument**: *user*

**Description**: Microsoft Entra ID (formerly Azure Active Directory) username for connecting to [SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

This property is required when [**MS_Fabric_Authentication_Method**](#msfabricauthenticationmethod) is set to **AZURE_ACTIVE_DIRECTORY**.

This property can be defined only for [SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

---

### MS_Fabric_OAuth2_Client_Id


**Argument**: *clientid*

**Description**: Client ID used to obtain the access token for connecting to SQL database in Microsoft Fabric.

This property is required when [**MS_Fabric_Authentication_Method**](#msfabricauthenticationmethod) is set to **ACCESS_TOKEN**.

This property can be defined only for [SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

---

### MS_Fabric_OAuth2_Client_Secret


**Argument**: *clientsecret*

**Description**: Secret key of the client ID specified in [**MS_Fabric_OAuth2_Client_Id**](#msfabricoauth2clientid).

This property is required when [**MS_Fabric_Authentication_Method**](#msfabricauthenticationmethod) is set to **ACCESS_TOKEN**.

This property can be defined only for [SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

---

### MS_Fabric_OAuth2_Endpoint


**Argument**: *endpoint*

**Description**: URL *endpoint* used for obtaining the bearer token with client credentials for connecting to SQL database in Microsoft Fabric.

Ensure that you are using the OAuth 2.0 endpoint. The URL path should include **v2.0**. The format for the endpoint URL is https://login.microsoftonline.com/&lt;tenant&gt;/oauth2/v2.0/token.

This property is required when [**MS_Fabric_Authentication_Method**](#msfabricauthenticationmethod) is set to **ACCESS_TOKEN**.

This property can be defined only for [SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

---

### MS_Fabric_Server


**Argument**: *server*

**Description**: SQL connection endpoint of the SQL database in Microsoft Fabric *server*.

This property can be defined only for [SQL database in Microsoft Fabric](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-database-in-microsoft-fabric-requirements).

---

### NetWeaver_Native_DB_Dictionaries


**Argument**: true

**Description**: If set to **true**, HVR will query the native database dictionaries instead of the SAP dictionaries. When this property is defined, you cannot select/add the SAP Cluster and Pool tables to channel.

---

### ODBC_DM_Lib_Path


**Argument**: *path*

**Description**: Directory *path* where the ODBC Driver Manager Library is installed. This property is applicable only for Linux/Unix operating system.

For a default installation, the ODBC Driver Manager Library is available at **/usr/lib64** and does not need to be specified. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/lib**.

---

### ODBC_Driver


**Argument**: *odbcdriver*

**Description**: Name of the user defined (installed) ODBC driver used for connecting HVR to the database.

---

### ODBC_Inst


**Argument**: *path*

**Description**: Directory *path* where the **odbcinst.ini** file is located. This property is applicable only for Linux/Unix operating system.

For Databricks, the **odbcinst.ini** file should contain information about the Simba Spark ODBC Driver under the heading **[Simba Spark ODBC Driver 64-bit]**.

---

### ODBC_Sysini


**Argument**: *path*

**Description**: Directory *path* where the **odbc.ini** and **odbcinst.ini** files are located. This property is applicable only for Linux/Unix operating system.

For a default installation, these files are available at **/etc** directory and do not need to be specified using this property. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/etc**.

For Azure SQL Database, the **odbcinst.ini** file should contain information about the Azure SQL Database ODBC Driver under the heading **[ODBC Driver** *version* **for SQL Server]**.

For Db2 for i, the **odbcinst.ini** file should contain information about the IBM i Access Client Solutions ODBC Driver under the heading **[IBM i Access ODBC Driver 64-bit]**.

For Redshift, the **odbcinst.ini** file should contain information about the Amazon Redshift ODBC Driver under the heading **[Amazon Redshift (x64)]**.

For SAP HANA, the **odbcinst.ini** file should contain information about the HANA ODBC Driver under heading **[HDBODBC]** or **[HDBODBC32]**.

For Snowflake, the **odbcinst.ini** file should contain information about the Snowflake ODBC Driver under the heading **[SnowflakeDSIIDriver]**.

---

### Oracle_ASM_Home


**Argument**: *path*

**Description**: Directory *path* where the Oracle ASM instance is installed. In Linux/Unix, by default, this is located in **/etc/oratab** file.

This property is only relevant for a source Oracle with redo and/or archive files in ASM and [**Capture_Method**](#capturemethod) is **DIRECT**.

The value of this property explicitly sets the system identifier (SID) for the ASM instance. Typically the value is **+ASM** or **+ASM[***instance_number***]**, but in some cases it may be **+asm** in lowercase. HVR can automatically assess what it should be.

> **Note:** 
To find the value for the SID on a Linux/Unix environment, execute the following command:
ps -ef |grep pmon

This command returns the pmon (process monitor) processes for all instances running on the server, including the ASM instance(s), that always starts with a **+** symbol.


---

### Oracle_ASM_Password


**Argument**: *password*

**Description**: Password for [**Oracle_ASM_User**](#oracleasmuser).

---

### Oracle_ASM_TNS


**Argument**: *connstring*

**Description**: Connection string for connecting HVR to Oracle's Automatic Storage Management (ASM) using Transparent Network Substrate (TNS).

The format for the connection string is *host***:***port***/***service_name*.

---

### Oracle_ASM_User


**Argument**: *username*

**Description**: Username for connecting to Oracle ASM instance. This user must have **sysasm** privileges.

---

### Oracle_BFile_Dirs_Mapping


**Argument**: *JSON string*

**Description**: Set the real path to the wallet directory if the path includes symbolic links. This is necessary because Oracle does not allow access through the BFile interface to a directory that has symbolic links in its path.

For example, if the wallet directory is **/var/foo/xxx**, where **/var/foo/** is a symbolic link to path **/yyy/zzz**. Thus, the real path to the wallet directory is **/yyy/zzz/xxx**. In this case, the property should be set as follows: **Oracle_BFile_Dirs_Mapping={"/var/foo":"/yyy/zzz"}**.

This is a map property that can store multiple values.

---

### Oracle_Container


**Description**: This is a discovered property that stores information whether the Oracle database is **Root Container** or Pluggable Database (**PDB)**.

---

### Oracle_Container_Root_Password


**Argument**: *password*

**Description**: Password for the [**Oracle_Container_Root_User**](#oraclecontainerrootuser).

---

### Oracle_Container_Root_RAC_Service


<strong>Since</strong> v6.1.0/27

**Argument**: *service*

**Description**: Service name of the Oracle database for the root container.

---

### Oracle_Container_Root_SID


**Argument**: *identifier*

**Description**: Unique name identifier of the Oracle root container.

---

### Oracle_Container_Root_TNS


**Argument**: *connstring*

**Description**: Connection string for connecting HVR to Oracle root container using Transparent Network Substrate (TNS).

The format for the connection string is *host***:***port***/***service_name*.

---

### Oracle_Container_Root_User


**Argument**: *username*

**Description**: Username for connecting to Oracle root container.

---

### Oracle_Dataguard_Primary_Password


**Argument**: *password*

**Description**: Password for [**Oracle_Dataguard_Primary_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties).

---

### Oracle_Dataguard_Primary_TNS


**Argument**: *connstring*

**Description**: Connection string for connecting HVR to the Oracle data guard primary database using Transparent Network Substrate (TNS).

The format for the connection string is *host***:***port***/***service_name*.

---

### Oracle_Dataguard_Primary_User


**Argument**: *username*

**Description**: Username for connecting HVR to the primary database.

---

### Oracle_Home


**Argument**: *path*

**Description**: Directory *path* where either Oracle or the Oracle client is installed.

When connecting to an Oracle instance through an HVR Agent installed on the database server, this property should point to the **ORACLE_HOME** directory of the Oracle source database. In all other cases, it should point to the directory where an Oracle client is installed.

---

### Oracle_NLS_LANG


**Description**: This is a discovered property that stores the value of Oralce's NLS_LANG parameter used for connecting to Oracle database.

---

### Oracle_Show_Invisible_Columns


**Argument**: true

**Description**: Enables replication of invisible columns in Oracle tables. For example, it can be used to capture information stored by Oracle Label Security. This property should be set for the location from which you want to replicate the invisible columns.

> **Important:** 
Invisible columns will be displayed only in tables added after the property has been set. Tables that were present in a channel before the property was set will not be affected.


---

### Oracle_SID


**Argument**: *identifier*

**Description**: Unique name identifier of the Oracle instance/database.

---

### Oracle_TDE_Wallet_Password


**Argument**: *password*

**Description**: Password for the Oracle TDE wallet.

---

### Oracle_TDE_Wallet_Reading_By_BFile


**Argument**: *Boolean*

**Description**: Enables access to the Oracle TDE wallet through the BFIile interface. This property allows to access the wallet remotely. The primary usage of this property is remote capturing on ASM systems. For configuration steps, see section [Configuring access to TDE wallet through BFile interface](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-tde#configuringaccesstotdewalletthroughbfileinterface).

---

### Oracle_TNS


**Argument**: *connstring*

**Description**: Connection string for connecting to the Oracle database using TNS (Transparent Network Substrate).

The format for the connection string is *host***:***port***/***service_name*.

Alternatively, you can add the connection details into the clients **tnsnames.ora** file and use that net service name in this field. This method requires easy connect enabled

---

### PostgreSQL_Pglib


**Argument**: *path*

**Description**: Directory *path* of the library (lib) directory in the PostgreSQL installation. For example, **/postgres/935/lib**.

This property can be left empty to use the system default path.

---

### PostgreSQL_XLog


**Argument**: *path*

**Description**: Directory *path* containing the current PostgreSQL **xlog** files.

---

### Publication_Name


<strong>Since</strong> v6.2.5/2

**Argument**: *name*

**Description**: A custom name for the PostgreSQL publication on a PostgreSQL location. This property applies the specified publication name to that location in all channels.

Using this property can prevent the same location from being used in multiple channels, depending on the use case. PostgreSQL requires each publication name to be unique within a cluster. If multiple channels use the same location, they all attempt to use the same custom publication name, which causes a conflict.

---

### Replication_Slot_Name


<strong>Since</strong> v6.2.5/1

**Argument**: *name*

**Description**: Custom name to be used for the replication slot on a PostgreSQL location. This property specifies a custom name for replication slots for the location in all channels.

> **Important:** 
When this property is set, it may prevent the same location from being used in multiple channels, depending on the use case. For example, PostgreSQL requires each replication slot to have a unique name within the cluster. If multiple channels attempt to use the same location, they would all try to use the same custom slot name, resulting in a conflict.


---

### S3_Bucket


**Argument**: *bucket*

**Description**: Name or IP address of the Amazon S3 bucket.

---

### S3_Bucket_Region


**Description**: This is a discovered property that stores the region of the S3 bucket for the connected location.

---

### S3_Encryption_KMS_Access_Key_Id


**Argument**: *keyid*

**Description**: If client-side encryption using a CMK stored in AWS KMS is enabled ([**S3_Encryption_KMS_Customer_Master_Key_Id**](#s3encryptionkmscustomermasterkeyid) without [**S3_Encryption_SSE_KMS**](#s3encryptionssekms)), this specifies the AWS access key id when querying KMS. By default, the credentials of the S3 connection is used.

---

### S3_Encryption_KMS_Customer_Master_Key_Id


**Argument**: *keyid*

**Description**: If [**S3_Encryption_SSE_KMS**](#s3encryptionssekms) is defined, this specifies the KMS CMK ID which is used for the server-side encryption. Otherwise, it enables client-side encryption using a CMK stored in AWS KMS. For client-side encryption, each object is encrypted with a unique AES256 data key obtained from KMS. This data key is stored alongside the S3 object.

> **Note:** 
The *keyid* can be the ID of the key available in your own account or the full ARN if it is in another account.


---

### S3_Encryption_KMS_IAM_Role


**Argument**: *role*

**Description**: If client-side encryption using a CMK stored in AWS KMS is enabled ([**S3_Encryption_KMS_Customer_Master_Key_Id**](#s3encryptionkmscustomermasterkeyid) without [**S3_Encryption_SSE_KMS**](#s3encryptionssekms)), this specifies the IAM role when querying KMS. By default, the credentials of the S3 connection is used.

---

### S3_Encryption_KMS_Region


**Argument**: *region*

**Description**: If client-side encryption using a CMK stored in AWS KMS is enabled ([**S3_Encryption_KMS_Customer_Master_Key_Id**](#s3encryptionkmscustomermasterkeyid) without [**S3_Encryption_SSE_KMS**](#s3encryptionssekms)), this specifies the KMS region when querying KMS. By default, the region of the S3 connection is used.

---

### S3_Encryption_KMS_Secret_Access_Key


**Argument**: *key*

**Description**: If client-side encryption using a CMK stored in AWS KMS is enabled ([**S3_Encryption_KMS_Customer_Master_Key_Id**](#s3encryptionkmscustomermasterkeyid) without [**S3_Encryption_SSE_KMS**](#s3encryptionssekms)), this specifies the AWS secret access key when querying KMS. By default, the credentials of the S3 connection is used.

---

### S3_Encryption_Master_Symmetric_Key


**Argument**: *key*

**Description**: Enable client-side encryption using a master symmetric key for AES. Each object is encrypted with a unique AES256 data key. This data key is encrypted using AES256 with the specified master symmetric key and then stored alongside the S3 object.

---

### S3_Encryption_Materials_Description


**Argument**: *desc*

**Description**: Provides optional encryption materials description which is stored alongside the S3 object. If used with KMS, the value must be a JSON object containing only string values.

---

### S3_Encryption_SSE


**Argument**: true

**Description**: If set to **true**, enables server-side encryption with Amazon S3 managed keys.

---

### S3_Encryption_SSE_KMS


**Argument**: true

**Description**: If set to **true**, enables server-side encryption with customer master keys (CMKs) stored in AWS key management service (KMS). If [**S3_Encryption_KMS_Customer_Master_Key_Id**](#s3encryptionkmscustomermasterkeyid) is not defined, a KMS managed CMK is used.

---

### Salesforce_Bulk_API


**Argument**: true

**Description**: If set to **true**, use Salesforce Bulk API instead of the SOAP interface.

This is more efficient for large volumes of data, because less round-trips are used across the network. A potential disadvantage is that some [Salesforce.com](http://Salesforce.com) licenses limit the number of bulk API operations per day.

If this property is defined for any table, then it affects all tables captured from that location.

---

### Salesforce_Dataloader


**Argument**: *path*

**Description**: Directory *path* where the Salesforce **dataloader.jar** file is located.

> **Note:** 
HVR uses Salesforce Dataloader tool for connecting to the Salesforce location.


---

### Salesforce_Endpoint


**Argument**: *url*

**Description**: Complete URL for connecting HVR to Salesforce.

---

### Salesforce_Serial_Mode


**Argument**: true

**Description**: If set to **true**, force serial mode instead of parallel processing for Bulk API.

The default is parallel processing, but enabling **Salesforce_Serial_Mode** can be used to avoid some problems inside [Salesforce.com](http://salesforce.com/).

If this property is defined for any table, then it affects all tables captured from that location.

---

### SAP_Archiving


<strong>Since</strong> v6.1.5/7

**Argument**: true

**Description**: If set to **true**, HVR can recognize records manually deleted by a user and records automatically archived by SAP on HANA database.

For SAP HANA, this property requires [**SAP_Source_Schema**](#sapsourceschema) to be defined. For more information about using this property with SAP HANA, see section [Recognizing SAP Archived Records](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements/sap-hana-as-source#recognizingsaparchivedrecords) in [SAP HANA as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements/sap-hana-as-source).

For more information about using this property with SAP NetWeaver on HANA, see section [Recognizing SAP Archived Records](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements/sap-netweaver-as-source/capture-from-netweaver-on-hana#recognizingsaparchivedrecords) in [Capture from SAP NetWeaver on HANA](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements/sap-netweaver-as-source/capture-from-netweaver-on-hana).

---

### SAP_Authentication_Method


**Argument**: *method*

**Description**: Authentication method for connecting HVR to the SAP system.

Valid value for *method* is:

- **USER_PASS**: Authenticate using the username and password.


---

### SAP_Client


**Argument**: *clientid*

**Description**: Three digit (**000**-**999**) identifier of the SAP client, which is sent to an **AS ABAP** upon logon.

---

### SAP_Connection_Type


<strong>Since</strong> v6.1.0/17

**Argument**: *type*

**Description**: Connection type for the SAP systems.

---

### SAP_Database_Owner


**Description**: This is a discovered property that stores information about the database schema that contain the SAP data. This property is discovered when creating or modifying a SAP NetWeaver location.

When SAP dictionaries are used, HVR will add only SAP tables from the database to the channel.

---

### SAP_Instance_Number


**Argument**: *number*

**Description**: Two digit *number* (**00**-**97**) of the SAP instance within its host.

---

### SAP_MessageServer_Group


<strong>Since</strong> v6.1.0/17

**Argument**: *name*

**Description**: Name of the SAP logon group. The default value is **PUBLIC**.

> **Note:** 
SAP logon group is a group of servers that belongs to one SAP system.


---

### SAP_MessageServer_Service


<strong>Since</strong> v6.1.0/17

**Argument**: *name or port*

**Description**: Port number or service name (like sapms&lt;SID&gt;) available in local **/etc/services** file. Specify this parameter only if the message server does not listen on the standard service sapms&lt;SysID&gt; or if this service is not defined in the services file, and you need to specify the network port directly.

> **Important:** 
On Unix, the services are defined in **/etc/services**.

On Windows, the services are defined in **c:\windows\system32\drivers\etc\services**.


---

### SAP_MessageServer_SystemID


<strong>Since</strong> v6.1.0/17

**Argument**: *id*

**Description**: Unique identifier &lt;sapsid&gt; of the SAP system.

---

### SAP_MessageServer_Use_Symbolic_Names


<strong>Since</strong> v6.1.0/17

**Argument**: true

**Description**: If set to **true**, only symbolic name can be specified in **SAP_MessageServer_Service**

---

### SAP_SNC_Name


<strong>Since</strong> v6.1.0/17

**Argument**: *name*

**Description**: Token/identifier representing the external RFC program, client SNC name (DataStage Server SNC Name). It is also referred as client Personal Security Environment (PSE) name.

---

### SAP_SNC_Partner_Name


<strong>Since</strong> v6.1.0/17

**Argument**: *name*

**Description**: Token/identifier representing the backend system, the communication partner’s SNC name.

---

### SAP_SNC_Library_Path


<strong>Since</strong> v6.1.0/17

**Argument**: *path*

**Description**: Path for the external security product’s library.

---

### SAP_Source_Schema


**Argument**: *schema*

**Description**: Name of the database *schema* that contain the SAP data. Defining this property enables the SAP table explore and the SAP unpack feature. If this property is defined, the SAP dictionaries are used, HVR will add only SAP tables from the database to the channel.

---

### SAP_NetWeaver_RFC_Library_Path


**Argument**: *path*

**Description**: Directory *path* containing the SAP NetWeaver RFC SDK library files.

For more information about the NetWeaver RFC SDK library file location, see section [Install NetWeaver RFC SDK Libraries](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements#installnetweaverrfcsdklibraries) in [SAP NetWeaver Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements).

---

### Service_Password


**Argument**: *password*

**Description**: Password for the Salesforce [**Service_User**](#serviceuser).

---

### Service_User


**Argument**: *username*

**Description**: Username for connecting HVR to Salesforce.

---

### Snowflake_Role


**Argument**: *role*

**Description**: Name of the Snowflake *role*.

---

### Snowflake_Warehouse


**Argument**: *warehouse*

**Description**: Name of the Snowflake *warehouse*.

---

### SqlServer_Authentication_Method


<strong>Since</strong> v6.1.0/4

**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to Azure SQL database.

Valid values for *method* are:

- **CLIENT_CREDS**: Authenticate using the Azure SQL access token.
- **USER_PASS**: Authenticate using the username and password.
- **AZURE_AD** <strong>Since</strong> v6.1.0/5: Authenticate using the Azure SQL active directory (AD).


---

### SqlServer_Native_Replicator_Connection


**Argument**: true

**Description**: If set to **true**, disables the firing of database triggers, foreign key constraints, and check constraints during integration, provided these objects were defined with the NOT FOR REPLICATION option. This is done by connecting to the database with the SQL Server replication connection capability.

If you are using HVR version 6.1.5/8 (or older) or an MSODBC driver older than version 17.8, the database connection string format in **SqlServer_Server** must be *server_name***,***port_number*; the alternative connection string formats are not supported. The *port_number* must be configured in the **Network Configuration** section of the **SQL Server Configuration Manager**.

> **Important:** 
When this property is defined, encryption of the ODBC connection is not supported if you are using HVR version is 6.1.5/8 or older, or an MSODBC driver older than version 17.8.


---

### SqlServer_Role_Name


<strong>Since</strong> v6.2.0

**Argument**: *role*

**Description**: Name of the database role that controls and restricts access to CDC-related objects (for example, CDC tables, stored procedures, and functions) that HVR creates when supplemental logging with CDC tables is enabled. When this property is set, only users who are members of the specified role can access the CDC tables and related objects created during the supplemental-logging enablement process.

> **Note:** 
- 
If the property is not set, the default SQL Server CDC behavior and permissions apply.

- 
This property replaces the environment variable **HVR_MSSQL_CDC_ENABLE_ROLENAME**, which remains supported temporarily for backward compatibility.




---

### SqlServer_Server


**Argument**: *server*

**Description**: Server/instance name for connecting to SQL Server, Azure SQL Database, Azure SQL Managed Instance, and Azure Synapse Analytics.

Valid values supported for *server* are location type-specific:
Azure SQL Database
Fully qualified domain name (FQDN) of the Azure SQL Database. For example, **cbiz2nhmpv.database.windows.net**.
Azure SQL Managed Instance
Fully qualified host name of the Azure SQL Managed Instance.

The format for this property is **tcp:***server name***,***port number*. Specify the host name and port number separated by a comma (**,**). For example, **tcp:hvr-managed-instance.public.hd6fjk12b8a9.database.windows.net,3342**.
Azure Synapse Analytics
Fully qualified domain name (FQDN) of the Azure Synapse Analytics server.

The format for this property is:**tcp:***server name*. For example, **tcp:hvrdw.database.windows.net**.
SQL Server
Name of the *server* (host) on which SQL Server is running and the Port number or the instance name of SQL Server.

The following formats are supported:

- 
*server_name*: Specify only the server name and HVR will automatically use the default port to connect to the server on which SQL Server is running. For example, **myserver**.

- 
*server_name***,***port_number*: Specify the server name and port number separated by a comma (**,**) to connect to the server on which SQL Server is running. For example, **myserver,1435**.

If the HVR version is 6.1.5/8 (or older) or when using a MSODBC driver older than 17.8, this format is required when using custom port for connection or when [**SqlServer_Native_Replicator_Connection**](#sqlservernativereplicatorconnection) is defined.

- 
*server_name***\***server_instance_name*: Specify the server name and server instance name separated by a backslash (**\**) to connect to the server on which SQL Server is running. For example, **myserver\HVR6048**.

This format is not supported on Linux.



---

### SqlServer_TDE_AKV_Vault_URLs


<strong>Since</strong> v6.2.5/10

**Argument**: *url*

**Description**: URL (also known as a Vault URI) to access the secure secrets, keys, and certificates stored in the Azure Key Vault (AKV). The format is https://&lt;your-unique-keyvault-name&gt;.vault.azure.net/.

---

### SqlServer_TDE_AKV_Key_Names


<strong>Since</strong> v6.2.5/10

**Argument**: *name*

**Description**: Name of the versioned key stored in the Azure Key Vault. The format is *KeyName/UUID* (e.g., **mykey/8f4c79c7e6714a**).

---

### SqlServer_TDE_AKV_Tenant_IDs


<strong>Since</strong> v6.2.5/10

**Argument**: *id*

**Description**: The tenant ID of the Microsoft Entra ID service principal. This property is required only when using Service Principal with a Secret for authentication.

---

### SqlServer_TDE_AKV_Client_Ids


<strong>Since</strong> v6.2.5/10

**Argument**: *id*

**Description**: The client ID of the Microsoft Entra ID service principal. This property is required only when using Service Principal with a Secret for authentication.

---

### SqlServer_TDE_AKV_Client_Secrets


<strong>Since</strong> v6.2.5/10

**Argument**: *secret*

**Description**: The client secret of the Microsoft Entra ID service principal. This property is required only when using Service Principal with a Secret for authentication.

---

### SqlServer_TDE_AKV_MI_Ids


<strong>Since</strong> v6.2.5/10

**Argument**: *id*

**Description**: ID of the user-assigned managed identity. This property is optional and can be defined only when using Managed Identity for authentication. If it is not defined, the system-assigned managed identity is used by default.

---

### SqlServer_TDE_Database_Certificates


<strong>Since</strong> v6.1.0/10

**Argument**: *certificate*

**Description**: Certificate used to protect a database encryption key (DEK). This property is defined by a key-value pair, where the key is a certificate name (a string) and the value is the respective certificate. The certificate must be a base64-encoded string. HVR accepts DER and PEM encoded certificates.

This is a map property that can store multiple values.

---

### SqlServer_TDE_Database_Private_Keys


<strong>Since</strong> v6.1.0/10

**Argument**: *key*

**Description**: Private key associated with the certificate (defined in [**SqlServer_TDE_Database_Certificates**](#sqlservertdedatabasecertificates)). This property is defined by a key-value pair, where the key is a certificate name (a string) and the value is the respective certificate private key. The private key must be a base64-encoded string. HVR accepts PVK and PEM encoded private keys. The private key is stored encrypted in the repository database.

This is a map property that can store multiple values.

---

### SqlServer_TDE_Database_Private_Key_Passwords


<strong>Since</strong> v6.1.0/10

**Argument**: *password*

**Description**: Password of the private key (defined in [**SqlServer_TDE_Database_Private_Keys**](#sqlservertdedatabaseprivatekeys)). This property is defined by a key-value pair, where the key is a certificate name (string) and the value is the respective password. The password must be a string. The password is stored encrypted in the repository database.

This is a map property that can store multiple values.

---

### Staging_Directory


**Argument**: *path*

**Description**: Directory *path* for bulk load staging files. For certain databases (Redshift and Snowflake), HVR splits large amount data into multiple staging files, to optimize performance.

For MariaDB or MySQL, when direct loading by the MySQL/MariaDB server option is used, this should be a directory local to the MySQL/MariaDB server on which the HVR user has write access from the server that HVR uses to connect to the DBMS. And when initial loading by the MySQL/MariaDB client option is used, this should be a local directory on the server where HVR connects to the DBMS.

For Redshift and Snowflake, this should be an S3 location.

> **Important:** 
This property is supported only for certain location classes. For the list of supported location classes, see [Bulk load requires a staging area](https://fivetran.com/docs/hvr6/capabilities/620#bulkloadrequiresstaging) in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle)) section.


---

### Staging_Directory_Database


**Argument**: *path*

**Description**: Directory *path* for the bulk load staging files visible from the database. This property should point to the same files as [**Staging_Directory**](#stagingdirectory).

For Greenplum, this should either be a local directory on the Greenplum head-node or it should be a URL pointing to [**Staging_Directory**](#stagingdirectory), for example a path starting with **gpfdist:** or **gpfdists:**.

For HANA, this should be a local directory on the HANA server which is configured for importing data by HANA.

For MariaDB or MySQL, when direct loading by the MySQL/MariaDB server option is used, this should be the directory from which the MySQL/MariaDB server should load the files. And when initial loading by the MySQL/MariaDB client option is used, this should be left empty.

For Redshift and Snowflake, this should be the S3 location that is used for [**Staging_Directory**](#stagingdirectory).

> **Important:** 
- 
This property requires [**Staging_Directory**](#stagingdirectory).

- 
This property is supported only for certain location classes. For the list of supported location classes, see [Bulk load requires a staging area](https://fivetran.com/docs/hvr6/capabilities/610#bulkloadrequiresstaging) in our **Capabilities** ([6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-oracle), and [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-oracle)) section.




---

### Staging_Directory_Is_Local


**Argument**: true

**Description**: If set to **true**, the directory specified in [**Staging_Directory_Database**](#stagingdirectorydatabase) is stored on the local drive of the file location's server.

If this property is not set to **true** or enabled, then by default the bulk load staging files are stored in the bucket or container available in the file location. For example, in Amazon S3, by default the staging directory is stored in the S3 bucket.

---

### Staging_File_Format


<strong>Since</strong> v6.2.5/1

**Argument**: *format*

**Description**: Format of the staging files. This property is applicable only to staging files on [BigQuery](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-bigquery-requirements/google-bigquery-as-target/staging-for-bigquery), [Databricks](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/databricks-requirements/databricks-as-target/staging-for-databricks), [Redshift](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/redshift-requirements/redshift-as-target/staging-for-redshift), and [Snowflake](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements/snowflake-as-target/staging-for-snowflake).

Valid values for *format* are:

- **csv**
- **parquet**


---

### Stream_Client_Private_Key


**Argument**: *path*

**Description**: Directory *path* where the **.pem** file containing the client's SSL private key is located.

---

### Stream_Client_Private_Key_Password


**Argument**: *password*

**Description**: Password of the private key file that is specified in [**Stream_Client_Private_Key**](#streamclientprivatekey).

---

### Stream_Client_Public_Certificate


**Argument**: *path*

**Description**: Directory *path* where the **.pem** file containing the client's SSL public certificate is located.

---

### Stream_Password


**Argument**: *password*

**Description**: Password of the [**Stream_User**](#streamuser).

---

### Stream_Public_Certificate


**Argument**: *path*

**Description**: Directory *path* where the file containing public certificate of Kafka server is located.

---

### Stream_User


**Argument**: *username*

**Description**: Username for connecting HVR to the Kafka server.

This property is required only if [**Kafka_Authentication_Method**](#kafkaauthenticationmethod) is set to **USER_PASS**, **SCRAM-SHA-256**, or **SCRAM-SHA-512**.

---

### Supplemental_Logging


**Argument**: *method*

**Description**: Specify what action should be performed to enable supplemental logging for tables.

Supplemental logging should be enabled for HVR to perform log-based capture of updates. For more details see, section [Supplemental Logging](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/sql-server-as-source#supplementallogging) in [SQL Server Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements).

Valid values for *method* are:

- 
**CDCTAB_ARTICLE** (default): Enable supplemental logging of updates by creating a CDC table for the source table.

If it is not possible to create the CDC table, then HVR will create replication articles instead. And, if it is not possible to create the replication articles also, then an error will be displayed.

- 
**ARTICLE_CDCTAB**: Enable supplemental logging of updates by creating SQL Server transactional replication articles if the source table has a primary key.

If it is not possible to create replication articles or if the source table does not have a primary key, then HVR will create CDC table instead. And, if it is not possible to create the CDC table also, then an error will be displayed.

- 
**EXISTING_CDCTAB_ARTICLE**: Enable supplemental logging of updates by using the existing CDC table or replication article for the source table. If neither the CDC tables nor the replication article exists, then HVR will create a CDC table for the source table.

If it is not possible to create the CDC table, then HVR will create replication articles instead. And, if it is not possible to create replication articles also, then an error will be displayed.

- 
**EXISTING_ARTICLE_CDCTAB**: Enable supplemental logging of updates by using the existing CDC table or replication articles for the source table. If neither the CDC tables nor the replication article exist, then HVR will create replication articles for the source table.

If it is not possible to create replication articles, then HVR will create a CDC table instead. And, if it is not possible to create the CDC table also, then an error will be displayed.



---

### Supplemental_Logging_Unavailable


**Description**: This is a discovered property that stores information whether the database supports supplemental logging.

---

### Sybase


**Argument**: *path*

**Description**: Directory *path* where the Sybase ASE database is installed.

---

### Sybase_ASE_Server_Name


<strong>Since</strong> v6.1.5/7

**Argument**: *name*

**Description**: Name of the Sybase ASE database server.

The interfaces file contains an entry for each SAP Sybase server on the network, identified by a server name. It enables the Open Client library used by HVR to locate the correct entry within the file.

This property is required only if the [**Sybase_Net_Trans_Source**](#sybasenettranssource) is set to **INTERFACES_FILE**.

---

### Sybase_Authentication_Method


**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to Sybase ASE server.

Valid values for *method* are:

- **USER_PASS**
- **KERBEROS**


> **Important:** 
For more information about using **KERBEROS** authentication, see section [Kerberos Authentication](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements#kerberosauthentication) in [Sybase ASE Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements).


---

### Sybase_CT_Library


**Argument**: *path*

**Description**: Directory *path* where the Sybase Open Client (CT library) is installed.

---

### Sybase_Kerberos_Keytab


**Description**: Directory *path* where the Kerberos keytab file is located. This keytab file contains the security key for the [**Database_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties).

This property is required only if [**Sybase_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) is set to **KERBEROS**.

---

### Sybase_Kerberos_Security_Mechanism


**Description**: Name of the security mechanism that performs security services for this connection. Security mechanism names are defined in the Sybase **libtcl.cfg** configuration file.

If this property is not defined, the default mechanism defined in the **libtcl.cfg** file will be used.

This property is required only if [**Sybase_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) is set to **KERBEROS**.

---

### Sybase_Kerberos_Security_Services


**Argument**: *service*

**Description**: Kerberos security mechanism *service*. It only defines how the connection behaves.

Valid values for *service* are:

- **Mutual Client/Server Authentication**: Both HVR and the Sybase server are required to authenticate themselves.
- **Encrypted Connection**: Enables encrypted connection between HVR and the Sybase server.
- **Data Integrity Checking**: Enables data integrity checking.
- **Replay Transmission Detection**: Enables data replay detection.
- **Data Out-Of-Sequence Detection**: Enables out-of-sequence detection.
- **Data Origin Verification**: Enables data origin stamping service.
- **Channel Binding**: Enables channel binding.


This property is required only if [**Sybase_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) is set to **KERBEROS**. Defining this property is otherwise optional.

This is a map property that can store multiple values.

---

### Sybase_Kerberos_Server_Principal


**Description**: The Kerberos Service Principal Name (SPN) of the Sybase ASE server.

This property is required only if [**Sybase_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) is set to **KERBEROS**.

---

### Sybase_Net_Trans_Source


<strong>Since</strong> v6.1.5/7

**Argument**: *source*

**Description**: Source of the network transport information required to connect HVR to the Sybase ASE database server.

Valid values for *source* are:

- **INTERFACES_FILE**: Use the SAP Open Client’s interfaces file to get network transport information.
- **DIRECT**: Use the network transport information specified directly in the HVR's location definition for Sybase ASE.


---

### Sybase_SSL_Enabled


<strong>Since</strong> v6.1.5/7

**Argument**: true

**Description**: SSL based authentication for Sybase ASE location connection.

If set to **true**, HVR authenticates the Sybase ASE database server by validating the SSL certificate shared by the Sybase ASE database server.

This property can be used only if the [**Sybase_Net_Trans_Source**](#sybasenettranssource) is set to **DIRECT**.

---

### Sybase_SSL_Common_Name


<strong>Since</strong> v6.1.5/7

**Argument**: *name*

**Description**: ASE server name for SSL certificate validation.

The name specified in this property should match the Sybase ASE database server name as specified in the command used to start ASE. For more information, see section [Common Name Validation in an SDC Environment](https://help.sap.com/docs/SAP_OPEN_SERVER/5f03751b7077424c8889d7275299e1ba/bfb790886db61014bf8f040071e613d7.html?locale=en-US) in SAP documentation.

This property is required only if [**Sybase_SSL_Enabled**](#sybasesslenabled) is selected set to **true**.

---

### Teradata_TPT_Lib_Path


**Argument**: *path*

**Description**: Directory *path* where the Teradata TPT Library is installed. For example, **/opt/teradata/client/16.10/odbc_64/lib**.

---

### Trigger_Quick_Toggle


**Argument**: true

**Description**: If set to **true**, allows end user transactions to avoid lock on toggle table.

The toggle table is changed by HVR during trigger-based capture. Normally all changes from user transactions before a toggle is put into one set of capture tables and changes from after a toggle are put in the other set. This ensures that transactions are not split. If an end user transaction is running when HVR changes the toggle then HVR must wait, and if other end user transactions start then they must wait behind HVR.

Defining this property allows other transactions to avoid waiting, but the consequence is that their changes can be split across both sets of capture tables. During integration these changes will be applied in separate transactions; in between these transactions the target database is not consistent.

This property requires [**Capture_Method**](#capturemethod) set to **DB_TRIGGER**.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


---

### Trigger_Toggle_Frequency


**Argument**: *secs*

**Description**: Instruct HVR trigger-based capture jobs to wait for a fixed interval *secs* (in seconds) before toggling and reselecting capture tables. This property requires [**Capture_Method**](#capturemethod) set to **DB_TRIGGER**.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


---

### View_Class


**Argument**: *class*

**Description**: Class of the database (defined in [**View_Database_Name**](#viewdatabasename)) that is used for providing an SQL based view on the file location. For example, Hive External Tables.

---

### View_Class_Flavor


**Description**: This is a discovered property that stores the flavor of the database (defined in [**View_Database_Name**](#viewdatabasename)).

---

### View_Class_Version


**Description**: This is a discovered property that stores the version of the database (defined in [**View_Database_Name**](#viewdatabasename)). HVR stores and uses this number internally to determine which Hive functionality should HVR attempt to use. For example, if value **121** is stored in this property it indicates Hive version 1.2.1.

---

### View_Database_Char_Encoding


**Description**: This is a discovered property that stores the character encoding of the database (defined in [**View_Database_Name**](#viewdatabasename)).

---

### View_Database_Client_Private_Key


**Argument**: *path*

**Description**: Directory *path* where the **.pem** file containing the client's SSL private key is located.

---

### View_Database_Client_Private_Key_Password


**Argument**: *password*

**Description**: Password for the private key file specified in [**View_Database_Client_Private_Key**](#viewdatabaseclientprivatekey).

---

### View_Database_Client_Public_Certificate


**Argument**: *path*

**Description**: Directory *path* where the **.pem** file containing the client's SSL public certificate is located.

---

### View_Database_Default_Schema


**Argument**: *schema*

**Description**: This is a discovered property that stores the name of the default schema in the database (defined in [**View_Database_Name**](#viewdatabasename)).

---

### View_Database_Host


**Argument**: *host*

**Description**: The hostname or IP-address of the server on which the database (defined in [**View_Database_Name**](https://fivetran.com/docs/hvr6/property-reference/location-properties)) is running.

---

### View_Database_Name


**Argument**: *name*

**Description**: Name of the database used for an SQL based view on the file location.

---

### View_Database_Nchar_Encoding


**Argument**: *charset*

**Description**: This is a discovered property that stores the national character encoding of the database (defined in [**View_Database_Name**](#viewdatabasename)).

---

### View_Database_Password


**Argument**: *password*

**Description**: Password for the [**View_Database_User**](#viewdatabaseuser).

---

### View_Database_Port


**Argument**: *port*

**Description**: Port number for the database (defined in [**View_Database_Name**](#viewdatabasename)).

---

### View_Database_Public_Certificate


**Argument**: *path*

**Description**: Directory path where the **.pem** file containing the server's public SSL certificate signed by a trusted CA is located.

---

### View_Database_User


**Argument**: *user*

**Description**: Username for connecting to the database (defined in [**View_Database_Name**](#viewdatabasename)).

---

### View_Hive_Authentication_Method


**Argument**: *method*

**Description**: Authentication *method* for connecting HVR to **Hive Server 2** instance.

This property is required only if [**View_Hive_Server_Type**](#viewhiveservertype) is set to **Hive Server 2**.

Valid values for *method* are:

- **NONE**
- **KERBEROS**
- **USER**
- **USER_PASS**
- **HDINSIGHT**


---

### View_Hive_HTTP_Path


**Argument**: *url*

**Description**: The partial URL corresponding to the Hive server.

This property is required only if [**View_Hive_Thrift_Transport**](#viewhivethrifttransport) is set to **HTTP**.

---

### View_Hive_Kerberos_Host


**Argument**: *name*

**Description**: Fully Qualified Domain Name (FQDN) of the **Hive Server 2** host. The value of **Host** can be set to **_HOST** to use the Hive server hostname as the domain name for Kerberos authentication.

If [**Hive_Service_Discovery_Mode**](#hiveservicediscoverymode) is disabled, then the driver uses the value specified in the Host connection attribute.

If [**Hive_Service_Discovery_Mode**](#hiveservicediscoverymode) is set to **ZooKeeper**, then the driver uses the **Hive Server 2** host name returned by ZooKeeper.

This property is required only if [**View_Hive_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) is set to **Kerberos**.

---

### View_Hive_Kerberos_Realm


**Argument**: *realm*

**Description**: Realm of the Hive Server 2 host.

It is not required to specify any value in this property if the realm of the Hive Server 2 host is defined as the default realm in Kerberos configuration.

This property is required only if [**View_Hive_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) is set to **Kerberos**.

---

### View_Hive_Kerberos_Service


**Argument**: *name*

**Description**: Kerberos service principal *name* of the Hive server.

This property is required only if [**View_Hive_Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties) is set to **Kerberos**.

---

### View_Hive_Server_Type


**Argument**: *type*

**Description**: Type of the Hive server to which HVR will be connected.

Valid values for *type* are:

- **Hive Server 1**: HVR connects to a Hive Server 1 instance.
- **Hive Server 2**: HVR connects to a Hive Server 2 instance.


---

### View_Hive_Service_Discovery_Mode


**Argument**: *mode*

**Description**: Mode for connecting to Hive.

This property is required only if [**View_Hive_Server_Type**](#viewhiveservertype) is set to **Hive Server 2**.

Valid values for *mode* are:

- **NONE**: HVR connects to Hive server without using the ZooKeeper service.
- **ZOOKEEPER**: HVR discovers Hive Server 2 services using the ZooKeeper service.


---

### View_Hive_Thrift_Transport


**Argument**: *protocol*

**Description**: Transport *protocol* to use in the Thrift layer.

This property is required only if [**View_Hive_Server_Type**](#viewhiveservertype) is set to **Hive Server 2**.

Valid values for *protocol* are:

- **BINARY**: This value can be used only if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **NONE** or **USER_PASS**.
- **SASL**: This value can be used only if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **KERBEROS** or **USER** or **USER_PASS**.
- **HTTP**: This value cannot be used if [**Hive_Authentication_Method**](#hiveauthenticationmethod) is set to **USER**.


> **Note:** 
For information about determining which Thrift transport protocols your Hive server supports, refer to [HiveServer2 Overview](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Overview) and [Setting Up HiveServer2](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2) sections in [Hive documentation](https://cwiki.apache.org/confluence/display/Hive/Home).


---

### View_Hive_Zookeeper_Namespace


**Argument**: *namespace*

**Description**: Namespace on ZooKeeper under which Hive Server 2 nodes are added.

This property is required only if [**View_Hive_Service_Discovery_Mode**](#viewhiveservicediscoverymode) is **ZooKeeper**.

---

### View_ODBC_DM_Lib_Path


**Argument**: *path*

**Description**: Directory *path* where the ODBC Driver Manager Library is installed. This property is applicable only for Linux/Unix operating system.

For a default installation, the ODBC Driver Manager Library is available at **/usr/lib64** and does not need to be specified. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/lib**.

---

### View_ODBC_Driver


**Argument**: *drivername*

**Description**: User defined (installed) ODBC driver for connecting HVR to the database.

---

### View_ODBC_Sysini


**Argument**: *path*

**Description**: Directory *path* where the **odbc.ini** and **odbcinst.ini** files are located. This property is applicable only for Linux/Unix operating system.

For a default installation, these files are available at **/etc** and do not need to be specified. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this property would be **/opt/unixodbc/etc**.

- For Db2i, the **odbcinst.ini** file should contain information about the IBM i Access Client Solutions ODBC Driver under the heading **[IBM i Access ODBC Driver 64-bit]**.
- For Redshift, the **odbcinst.ini** file should contain information about the Amazon Redshift ODBC Driver under the heading **[Amazon Redshift (x64)]**.
- For SAP HANA, the **odbcinst.ini** file should contain information about the HANA ODBC Driver under heading **[HDBODBC]** or **[HDBODBC32]**.
- For Snowflake, the **odbcinst.ini** file should contain information about the Snowflake ODBC Driver under the heading **[SnowflakeDSIIDriver]**.
- For Azure SQL Database, the **odbcinst.ini** file should contain information about the Snowflake ODBC Driver under the heading **[ODBC Driver** *version* **for SQL Server]**.


---

### WASB_Account


**Argument**: *account*

**Description**: Name of the Azure Blob Storage *account*.

---

### WASB_Container


**Argument**: *container*

**Description**: Name of the *container* available within the Azure Blob Storage account.

.actparam {
    padding-left: 20px;
}
