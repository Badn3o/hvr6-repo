# File, FTP, SFTP Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/file-ftp-sftp-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/file-ftp-sftp-requirements/index.md)

# File, FTP, SFTP Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using File/FTP/SFTP for replication.

#### Supported Platforms


- Learn about the File/FTP/SFTP versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page.


## Introduction


HVR supports different kinds of file locations:

- regular file locations (a directory on a local file system);
- FTP file locations;
- SFTP file locations.


Generally, the behavior of HVR replication is the same for all of these kinds of file locations. For all of them, capture is defined with action [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) and integration is defined with action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate). All other file location parameters are supported and behave normally.

HVR can connect to an FTP or SFTP file location using a file protocol in two ways:

- connecting with this protocol directly from the hub machine;
- or first connecting to a remote machine with HVR's remote protocol, and them connecting to the file location from that machine using FTP or SFTP.


These two options have small difference in the timing and latency of capture jobs:

- direct file capture jobs check for new files once a second;
- indirect capture (capture from a non-local file location) jobs check for new files every 10 seconds.


Also, if action **Capture** is defined without the [**DeleteAfterCapture**](https://fivetran.com/docs/hvr6/action-reference/capture#deleteaftercapture) parameter, the capture job may have to wait for up to a minute before capturing new files. This happens because these jobs rely on comparing timestamps, but the file timestamps in the FTP protocol have low granularity (minutes not seconds).

A proxy server to connect to FTP or SFTP can be configured with **File_Proxy_*** [**location properties**](https://fivetran.com/docs/hvr6/property-reference/location-properties).

HVR uses the cURL library to communicate with the file systems.

## Integrate Limitations


By default, for file-based target locations, HVR does not replicate the <b>delete</b> operation performed at the source location.

## FTPS: Server Authentication


FTP and WebDAV support certificates for authentication. These are held in the certificate directory **HVR_HOME/etc/cert**. The following files are included or can be easily created:

- 
**ca-bundle.crt**: Used by HVR to authenticate SSL servers, like FTPS.
To override this, create a new file named *host***.pub_cert** in this same certificate directory. No authentication is done if neither file is found. Delete or relocate both files to disable FTPS authentication.
The **ca-bundle.crt** file can be copied from the **/usr/share/ssl/certs/" directory on Unix/Linux.

- 
*host***.pub_cert**: Used by HVR to override **ca-bundle.crt** for server verification for *host*.
FTP connections can be unencrypted or they can have three types of encryption; this is called FTPS, and should not be confused with SFTP. These FTPS encryption types are SSL/TLS implicit encryption (standard port: **990**), SSL explicit encryption and TLS explicit encryption (standard port: **21**).



> **Important:** 
If the FTP/SFTP connection is made via a remote HVR machine, then the certificate directory on the remote HVR machine is used, not the one on the hub machine.


## FTPS: Client Authentication


Normally, clients (HVR) are authenticated using a username and password. In addition to this, you can use client-side SSL certificates.
To set this up, you need to have a public/private key pair in PEM format. Place them in the **HVR_CONFIG/etc/cert** directory as *client***.pub_cert** and *client***.priv_key**, and define the following actions:

 **Group** | **Table** | **Action/Parameters** |
 File/FTP | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)**
**[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)=HVR_SSL_CLIENT_CERT**, **[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)=***client***.pub_cert** |
 File/FTP | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)**
**[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)=HVR_SSL_CLIENT_KEY**, **[Value=](https://fivetran.com/docs/hvr6/action-reference/environment#value)***client***.priv_key** |
 File/FTP | * | If you have a password/phrase on your key, set:
**[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)**
**[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)=HVR_SSL_CLIENT_KEY_PASSWD**, **[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)=***passwd* |


You can encrypt the password for HVR by running: shell {% process=false %}     hvrcrypt <em>client passwd</em>      

If you have a PKCS#12 or PFX file, you can convert it to PEM format using openssl: shell {% process=false %}     openssl pkcs12 -in <em>cert</em>.p12 -clcerts -nokeys -out <em>client</em>.pub_cert      shell {% process=false %}     openssl pkcs12 -in <em>cert</em>.p12 -nocerts -out <em>client</em>.priv_key     

## SFTP: Server Authentication


A file (named **HVR_CONFIG/files/known_hosts**) is used internally during SFTP connections. It is updated the first time HVR connects to reach the SFTP machine. On Unix or Linux this file can be initialized by copying it from **HOME/.ssh/known_hosts**.

> **Important:** 
If the FTP/SFTP connection is made via a remote HVR machine, then the certificate directory on the remote HVR machine is used, not the one on the hub machine.


## SFTP: Client Authentication


Normally, clients (HVR) are authenticated using a username and password. Instead of this, you can use client-side keys.
To set this up, you need to have a public/private key pair. Place them in the **HVR_CONFIG/etc/cert** directory as *client***.pub** and *client*, and define the following actions:

 **Group** | **Table** | **Action/Parameters** |
 File/FTP | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)**
**[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)=HVR_SSH_PUBLIC_KEY**, **[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)=***client***.pub** |
 File/FTP | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)**
**[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)=HVR_SSH_PRIVATE_KEY**, **[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)=***client*

Note: If you have a password/phrase on your private key, you can set it in the **PASSWORD** field of the location.
 |


You can generate keys using:
 ssh-keygen -f  <em>client</em> 

## State Directory


By default, HVR creates its internal state files in a sub-directory named **_hvr_state** within the location’s top directory.

This option in HVR UI allows you to specify a custom path for HVR’s internal state files, which are used during file replication. The state directory can be configured as a path within the location’s top directory or placed outside of it. If a relative path (for example, **../work**) is specified, it will be interpreted relative to the location’s top directory.

If the state directory is on the same file system as the location’s top directory, HVR ensures that file move operations are ‘atomic,’ so users only see fully written files and never partial versions.

> **Note:** 
This option is equivalent to the location property [**File_State_Directory**](https://fivetran.com/docs/hvr6/property-reference/location-properties#filestatedirectory).



## Intermediate Directory


This option in the HVR UI allows you to specify a directory path for storing intermediate (temporary) files generated during [Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare). These files are created during both "direct file compare" and "online compare" operations.

This option is displayed in the [location creation](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location#configurecaptureintegrate) dialog when [creating a new location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location), and in the [Source and Target Properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#sourceandtargetproperties) pane on the [Location Details](https://fivetran.com/docs/hvr6/user-interface/locations/location-details) page when editing an existing location.

Using an intermediate directory can enhance performance by ensuring that temporary files are stored in a location optimized for the system's data processing needs.

This setting is particularly relevant for target file locations, as it determines where the intermediate files are placed during the Compare operation. If this option is not enabled, the intermediate files are stored by default in the *integratedir***/_hvr_intermediate** directory, where *integratedir* is the replication **DIRECTORY** ([File_Path](https://fivetran.com/docs/hvr6/property-reference/location-properties#filepath)) defined for the target file location.

> **Note:** 
This option is equivalent to the location property [**Intermediate_Directory**](https://fivetran.com/docs/hvr6/property-reference/location-properties#intermediatedirectory).



## Related Articles


- [Location Connection for File/FTP/SFTP](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-file-ftp-sftp)

