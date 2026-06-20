# Hub Server Properties - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/property-reference/hub-server-properties

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/property-reference/hub-server-properties/index.md)

# Hub Server Properties


This section lists and describes the hub server properties.

A hub server property specifies the characteristics/attributes of server where HVR Hub System is installed/running. In the Command Line interface (CLI), the hub server properties can be set using the commands [**hvrhubserver**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserver), [**hvrhubserverconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserverconfig).

> **Note:** 
A property that is automatically discovered by Fivetran HVR when it connects to a database/location is called discovered property. A user cannot specify/input value into a discovered property.

An array property and map property can store multiple values. The syntax for updating them from the [Command Line Interface (CLI)](https://fivetran.com/docs/hvr6/command-line-interface/managing-properties-in-cli) varies.


---

### Authentication_Method


<strong>Since</strong> v6.1.5/8

**Argument:** *JSON string*

**Description:** User authentication methods for accessing the HVR Hub System.

Valid values for this property are:

- **password**: User is authenticated by their username and password.
- **login_token**: User is authenticated by one-time login token.
- **saml** <strong>Since</strong> v6.2.5/2: User is authenticated by a third-party identity provider using SAML 2.0.


The default behavior when this property is not defined is **password** authentication.

Example JSON to allow multiple authentication methods:
Authentication_Method={"password":"true","login_token":"true"} 

This is a map property that can store multiple values.

---

### Azure_OAuth2_Client_Id


**Argument:** *id*

**Description:** Application ID used for obtaining the Microsoft Entra ID (formerly Azure Active Directory) access token.

This property is required only if the [**SqlServer_Authentication_Method**](#sqlserverauthenticationmethod) is set to **CLIENT_CREDS**.

---

### Azure_OAuth2_Client_Secret


**Argument:** *key*

**Description:** Secret key of the **Azure_OAuth2_Client_Id**.

This property is required only if the [**SqlServer_Authentication_Method**](#sqlserverauthenticationmethod) is set to **CLIENT_CREDS**.

---

### Azure_OAuth2_Endpoint


**Argument:** *url*

**Description:** URL used for obtaining the bearer token with credential token.

Ensure that you are using the OAuth 2.0 endpoint. The URL path should include **v2.0**. The format for the endpoint URL is https://login.microsoftonline.com/<em>tenant</em>/oauth2/<b>v2.0</b>/token

This property is required only if the [**SqlServer_Authentication_Method**](#sqlserverauthenticationmethod) is set to **CLIENT_CREDS**.

---

### Azure_OAuth2_Password


**Argument:** *password*

**Description:** Password for **Azure_OAuth2_User**.

---

### Azure_OAuth2_User


**Argument:** *user*

**Description:** URL used for obtaining the bearer token with credential token.

---

### Database_Host


**Argument:** *host*

**Description:** Hostname or IP-address of the server on which the database is running.

For Db2 for i, this is the hostname or IP-address of the Db2 for i system.

---

### Database_Name


**Argument:** *dbname*

**Description:** Name of the database.

For Db2 for i, this is the named database in Db2 for i. It could be on another (independent) auxiliary storage pool (IASP). The user profile's default setting will be used when no value is specified. Specifying ***SYSBAS** will connect a user to the SYSBAS database.

---

### Database_Password


**Argument:** *password*

**Description:** Password for the [**Database_User**](#databaseuser).

---

### Database_Port


**Argument:** *port*

**Description:** Port number on which the database (defined in [**Database_Host**](#databasehost)) server is expecting connections.

---

### Database_User


**Argument:** *user*

**Description:** Username for connecting HVR to the database (defined in [**Database_Name**](#databasename)).

For Azure SQL Database, this is the user name and host name of the Azure SQL Database server. The format to be used is <em>username</em><b>@</b><em>hostname</em>.

---

### Db2_DB2INSTANCE


**Argument:** *instance*

**Description:** When using "Db2 client or Db2 server or Db2 Connect", the name of the Db2 *instance* must be specified.

When using "IBM Data Server Driver for ODBC and CLI" this property should not be defined.

---

### Db2_INSTHOME


**Argument:** *path*

**Description:** When using "Db2 client or Db2 server or Db2 Connect" the directory *path* of the Db2 installation must be specified.

When using "IBM Data Server Driver for ODBC and CLI" the directory *path* of the IBM Data Server Driver for ODBC and CLI installation on HVR machine (e.g., **/distr/db2/driver/odbc_cli/clidriver**) must be specified.

---

### HTTP_Port


**Argument:** *port*

**Description:** Port number for HVR Hub Server when HTTP protocol is used.

If HTTPS port is defined, all traffic/requests will be redirected that port.

The default port is **4340**.

---

### HTTPS_Port


**Argument:** *port*

**Description:** Port number for HVR Hub Server when HTTPS protocol is used.

The default port is **4341**.

---

### HTTPS_Private_Key_Password


**Argument:** *password*

**Description:** Password for the hub server private key.

---

### Hub_Server_HVR_CONFIG


**Description:** This is a discovered property that stores the directory path of **HVR_CONFIG** for the HVR Hub Server.

---

### Hub_Server_HVR_HOME


**Description:** This is a discovered property that stores the directory path of **HVR_HOME** for the HVR Hub Server.

---

### Hub_Server_HVR_Version


**Description:** This is a discovered property that stores the version of the HVR installed on the HVR Hub Server.

---

### Hub_Server_OS_Fingerprint


**Description:** This is a discovered property that stores the unique identifier (fingerprint) of the server on which the HVR Hub Server is installed.

---

### Hub_Server_Operating_System


**Description:** This is a discovered property that stores the name of the operating system on which the HVR Hub Server is installed/running.

---

### Hub_Server_Password_Manager_Configured


<strong>Since</strong> v6.1.5/0

**Description:** This discovered property is set to **true** if the **hvrmanagedpassword** file exists in the **HVR_CONFIG/plugin/authentication** directory.

If the property is **true**, all UI fields for entering secrets get an option to enter the token for the external password manager. For more information, see [Managed Secrets](https://fivetran.com/docs/hvr6/advanced-operations/managed-secrets).

---

### Hub_Server_Platform


**Description:** This is a discovered property that stores the name of the HVR platform used for installing the HVR Hub Server.

---

### Ingres_II_SYSTEM


**Argument:** *path*

**Description:** Directory *path* where the Actian Vector or Ingres database is installed.

---

### License_Agreement_Accepted


**Argument:** true

**Description:** If set to **true**, indicates that the HVR license agreement has been accepted.

---

### Log_Rotate_Interval


<strong>Since</strong> v6.1.0/3

**Argument:** *secs*

**Description:** Interval (*secs*) at which log files are automatically rotated. For more information, see [Log Rotation](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrmaintlogrotate#automatedlogrotation).

---

### Minimum_TLS_Supported


<strong>Since</strong> v6.1.0/18

**Argument:** *version*

**Description:** Minimum TLS *version* accepted by the HVR Hub Server.

Valid values for *version* are:

- **TLSv1_3**: TLS version 1.3
- **TLSv1_2** default: TLS version 1.2
- **TLSv1_2_WEAK_CIPHERS** <strong>Since</strong> v6.1.0/20: TLS version 1.2 with weak ciphers enabled
- **TLSv1_1**: TLS version 1.1
- **TLSv1_0**: TLS version 1.0


---

### ODBC_DM_Lib_Path


**Argument:** *path*

**Description:** Directory *path* where the ODBC Driver Manager Library is installed. This property is applicable only for Linux/Unix operating system.

For a default installation, the ODBC Driver Manager Library is available at **/usr/lib64** and does not need to be specified. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/lib**.

---

### ODBC_Driver


**Argument:** *odbcdriver*

**Description:** Name of the user defined (installed) ODBC driver used for connecting HVR to the database.

---

### ODBC_Inst


**Argument:** *path*

**Description:** Directory *path* where the **odbcinst.ini** file is located. This property is applicable only for Linux/Unix operating system.

---

### ODBC_Sysini


**Argument:** *path*

**Description:** Directory *path* where the **odbc.ini** and **odbcinst.ini** files are located. This property is applicable only for Linux/Unix operating system.

For a default installation, these files are available at **/etc** directory and do not need to be specified using this property. However, when UnixODBC is installed in for example **/opt/unixodbc** the value for this field would be **/opt/unixodbc/etc**.

For Azure SQL Database, the **odbcinst.ini** file should contain information about the Azure SQL Database ODBC Driver under the heading **[ODBC Driver** *version* **for SQL Server]**.

For Db2 for i, the **odbcinst.ini** file should contain information about the IBM i Access Client Solutions ODBC Driver under the heading **[IBM i Access ODBC Driver 64-bit]**.

For Redshift, the **odbcinst.ini** file should contain information about the Amazon Redshift ODBC Driver under the heading **[Amazon Redshift (x64)]**.

For SAP HANA, the **odbcinst.ini** file should contain information about the HANA ODBC Driver under heading **[HDBODBC]** or **[HDBODBC32]**.

For Snowflake, the **odbcinst.ini** file should contain information about the Snowflake ODBC Driver under the heading **[SnowflakeDSIIDriver]**.

---

### Oracle_Home


**Argument:** *path*

**Description:** Directory *path* where Oracle is installed.

---

### Oracle_SID


**Argument:** *identifier*

**Description:** Unique name identifier of the Oracle instance/database.

---

### Oracle_TNS


**Argument:** *connstring*

**Description:** Connection string for connecting to the Oracle database using TNS (Transparent Network Substrate).

The format for the connection string is <em>host</em><b>:</b><em>port</em><b>/</b><em>service_name</em>.

Alternatively, you can add the connection details into the clients **tnsnames.ora** file and use that net service name in this field. This method requires easy connect enabled

---

### PostgreSQL_Pglib


**Argument:** *path*

**Description:** Directory *path* containing the current PostgreSQL **xlog** files.

---

### Public_Host


<strong>Since</strong> v6.2.5/2

**Argument:** *listen_port*

**Description:** Public or external host address for accessing the HVR Hub Server via browser or HVR CLI (**-R** option).

The value can be either a Fully Qualified Domain Name (FQDN) like *hostname.domain*, or an FQDN followed by a port, such as *hostname.domain*:*port*.

The default host is the hostname of the machine running the HVR Hub Server (without the domain).

The default port is the active HTTP or HTTPS listener port.

If HTTPS is configured, the public certificate (used to enable HTTPS for the Hub Server) must match this hostname.

---

### Repository_Class


**Argument:** *class*

**Description:** Class of the repository database.

---

### Repository_Class_Flavor


**Description:** This is a discovered property that stores the flavor of the specific database [**Repository_Class**](https://fivetran.com/docs/hvr6/user-interface/system/hub-server). The combination of **Repository_Class** and **Repository_Class_Flavor** forms the location type.

---

### Saml_IDP_Metadata


<strong>Since</strong> v6.2.5/2

**Argument:** *base64*

**Description:** Metadata of the Identity Provider (IdP) used for **saml** authentication.

---

### Saml_IDP_Name


<strong>Since</strong> v6.2.5/2

**Description:** Custom name for the IdP to be displayed in the HVR UI.

By default, the text on the login button for **saml** authentication is **Sign in with SSO**. When you set this property, the specified value replaces **SSO** in the button text. For example, if the value is set to **Corporate Login**, the button displays **Sign in with Corporate Login**.

---

### Saml_IDP_User_Claim


<strong>Since</strong> v6.2.5/2

**Description:** Claim attribute in the SAML response containing the username.

The username from the claim attribute returned by the IdP is used to match an existing SAML user of HVR for authentication. If this property is not defined, the subject name-id returned by the IdP is used instead.

---

### Saml_SP_Public_Certificate


<strong>Since</strong> v6.2.5/2

**Argument:** *base64*

**Description:** Public certificate of the Service Provider (HVR Hub Server) used for **saml** authentication.

This X.509 certificate is shared with the Identity Provider (IdP) to establish trust and secure communication between the service provider and IdP.

---

### Saml_SP_Private_Key


<strong>Since</strong> v6.2.5/2

**Argument:** *base64*

**Description:** Service Provider's X.509 private key for **saml** authentication.

---

### Saml_SP_Private_Key_Password


<strong>Since</strong> v6.2.5/2

**Argument:** *password*

**Description:** Password for the **Saml_SP_Private_Key**.

---

### Setup_Mode


**Argument:** true

**Description:** Setup mode for the HVR Hub Server.

If set to **true**, enables the HVR Hub System setup while disabling most replication features of HVR.

---

### SqlServer_Authentication_Method


<strong>Since</strong> v6.1.0/4

**Argument:** *method*

**Description:** Authentication *method* for connecting HVR to Azure SQL database.

Valid values for *method* are:

- **CLIENT_CREDS**: Authenticate using the Azure SQL access token.
- **USER_PASS**: Authenticate using the username and password.
- **AZURE_AD** <strong>Since</strong> v6.1.0/5: Authenticate using the Azure SQL active directory (AD).


---

### SqlServer_Server


**Argument:** *server*

**Description:** Name of the *server* (host) on which SQL Server is running and the Port number or the instance name of SQL Server.

The following formats are supported for this property:

- *server_name*: Specify only the server name and HVR will automatically use the default port to connect to the server on which SQL Server is running. For example, **myserver**.
- *server_name***,***port_number*: Specify the server name and port number separated by a comma (**,**) to connect to the server on which SQL Server is running. For example, **myserver,1435**. 
This format is required when using custom port for connection or when [**SqlServer_Native_Replicator_Connection**](#sqlservernativereplicatorconnection) is defined.
- *server_name***\***server_instance_name* : Specify the server name and server instance name separated by a backslash (**\**) to connect to the server on which SQL Server is running. For example, **myserver\HVR6048**. 
This format is not supported on Linux.


---

### Teradata_TPT_Lib_Path


**Argument:** *path*

**Description:** Directory *path* where the Teradata TPT Library is installed. For example, **/opt/teradata/client/16.10/odbc_64/lib**.

---

### Worker_Age


**Argument:** *secs*

**Description:** Shut down HVR Hub Server worker after it has reached the age of *secs* seconds.

The default is **3600** seconds (60 minutes).

> **Tip:** 
A worker is a process used by the HVR Hub Server to execute the REST calls.


---

### Worker_Environment


**Argument:** *JSON string*

**Description:** Sets one or more environment variables for hub server workers.

The value of the **Worker_Environment** is a JSON string and can be used to set multiple environment variables at once.

> **Important:** 
In case the **Worker_Environment** property is changed, the hub server recognizes the changes and all new workers being used adhere to the newly configured environment variables.


Example:
hvrhubserverconfig Worker_Environment='{"HVR_SQL_TRACE":"1","HVR_PROC_TRACE":"2"}'
hvrhubserverconfig Worker_Environment='{\"HVR_SQL_TRACE\":\"1\",\"HVR_PROC_TRACE\":\"2\"}'

This is a map property that can store multiple values.

---

### Worker_Idle


**Argument:** *secs*

**Description:** Shut down HVR Hub Server worker after it has remained idle for *secs* seconds.

The default is **600** seconds (10 minutes).

---

### Worker_Kill_Grace


<strong>Since</strong> v6.1.0/30

**Argument:** *secs*

**Description:** Extra time (in seconds) granted to the HVR Hub Server worker to finish a canceled API request before forcefully terminating the worker.

The default is **10** seconds.

> **Note:** 
For optimal performance, the HVR Hub Server workers actively cache the repository database contents, which is crucial for large systems. If a new worker replaces the terminated one, a significant amount of time is required to rebuild that cache. Consequently, worker termination proves to be resource-intensive. Therefore, introducing a grace period before forceful termination helps conserve system resources.


---

### Worker_Max_Hard


**Description:** Maximum number of workers that HVR Hub Server spawns at the same time.

The default is **100** workers.

---

### Worker_Max_Soft


**Description:** Threshold after which the HVR Hub Server worker slows down spawning of workers.

The default threshold is **30**.

.actparam {
    padding-left: 20px;
}
