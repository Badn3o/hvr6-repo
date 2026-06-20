# SAP NetWeaver Requirements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements/index.md)

# SAP NetWeaver Requirements


This section describes the requirements, access privileges, and other features of Fivetran HVR when using SAP NetWeaver for replication.

#### Supported Platforms


- Learn about the SAP NetWeaver versions compatible with HVR on our **Platform Support Matrix** page ([6.3.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-635), [6.3.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-630), [6.2.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-625), [6.2.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-620), [6.1.5](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-615), and [6.1.0](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610)).


#### Supported Capabilities


- Discover what HVR offers for SAP NetWeaver on HANA on our **Capabilities for SAP NetWeaver on HANA** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-sap-netweaver-on-hana), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-sap-netweaver-on-hana), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-sap-netweaver-on-hana), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-sap-netweaver-on-hana), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-sap-netweaver-on-hana), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-sap-netweaver-on-hana)).
- Discover what HVR offers for SAP NetWeaver on Oracle on our **Capabilities for SAP NetWeaver on Oracle** page ([6.3.5](https://fivetran.com/docs/hvr6/capabilities/635/capabilities-for-sap-netweaver-on-oracle), [6.3.0](https://fivetran.com/docs/hvr6/capabilities/630/capabilities-for-sap-netweaver-on-oracle), [6.2.5](https://fivetran.com/docs/hvr6/capabilities/625/capabilities-for-sap-netweaver-on-oracle), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620/capabilities-for-sap-netweaver-on-oracle), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615/capabilities-for-sap-netweaver-on-oracle), and [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610/capabilities-for-sap-netweaver-on-oracle)).


#### Data Management


- Learn how HVR maps data types between source and target DBMSes or file systems on the [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping) page. For the list of the supported SAP data types and their mapping, see [Data Type Mapping for SAP](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sap).


> **Note:** 
Fivetran provides additional solutions for replicating data from SAP database. For more information, see section [SAP](https://fivetran.com/docs/connectors/databases/sap) in Databases.


## Introduction


HVR allows you to capture changes from SAP ECC or S/4 system on Oracle or SAP HANA where you do not have a full use database license. The connection to the database is established indirectly via the SAP's application layer (NetWeaver).

HVR connects to SAP NetWeaver using the SAP’s native Remote Function Call (RFC) libraries and then calls the HVR specific ABAP functions (also called as AppConnect) to start the data extraction process. HVR's AppConnect is used for all communication (metadata queries, [adding tables](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel) to a channel, [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), and [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare). All data transport is done in compressed format via RFC. For more information about the ports for RFC, refer to the [SAP documentation](https://help.sap.com/viewer/ports).



## Prerequisites


The following are required for HVR when using SAP NetWeaver for replication:

- SAP ABAP version 7.5 and above.
- SAP system must be unicode.
- Oracle or SAP HANA database.


## License for SAP NetWeaver


The regular [license](https://fivetran.com/docs/hvr6/getting-started/licensing) does not allow you to use the location type SAP NetWeaver, so an additional license is needed. Contact HVR Support to obtain the proper license for using HVR with SAP NetWeaver.

> **Note:** 
HVR supports multi-licensing, where multiple license files are added for a system.


## SAP NetWeaver User Permissions


To connect to SAP Netweaver, HVR requires a SAP Communication user. This user must be granted the following authorizations:

### RFC Access to Standard SAP Functions


Required to establish the RFC connection and perform system checks.
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_RFC | ACTVT | 16 |
  | RFC_TYPE | FUGR |
  | RFC_NAME | BTCH   
RFC1   
SDIFRUNTIME |
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_RFC | ACTVT | 16 |
  | RFC_TYPE | FUNC |
  | RFC_NAME | RFCPING |

### RFC Access to HVR Function Group


Required to allow HVR to call its custom RFC function modules.
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_RFC | ACTVT | 16 |
  | RFC_TYPE | FUGR |
  | RFC_NAME | /HVR/SAPAPPCONNECT |

### Batch Job Administration


Required for scheduling and managing background jobs.
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_RFC | ACTVT | 16 |
  | RFC_TYPE | FUGR |
  | RFC_NAME | S_BTCH_JOB |
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_BTCH_ADM | BTCADMIN | Y |
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_BTCH_JOB | JOBACTION | RELE |
  | JOBGROUP | * |

### Data Access Authorizations


HVR requires database-level authorizations to read SAP NetWeaver application tables and metadata. Depending on your organization’s security policy, you can configure database grants using one of the following methods.
Option 1: Grant Full Access
To simplify configuration, grant access to all tables.

> **Note:** 
This option is easiest to maintain, but may not meet stricter security policies.

 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_TABU_SQL | ACTVT | 33 |
  | DBSID | * |
  | TABOWNER | standard DB schema(SAPABAP1) |
  | TABLE | * |
Option 2: Restrict Access and Allow Only Specific Tables
To restrict access, you must grant **S_TABU_SQL** authorizations for:

- Specific data tables – the application tables you want to replicate.
- ABAP tables - common SAP metadata/control tables
- Database-specific system tables – depending on whether you’re on HANA or Oracle


> **Important:** 
When granting permissions only to specific data tables, the authorization object **S_TABU_SQL** must be added to the user profile.


- 
**Specific Data Tables** - Grant access to the individual data tables that you plan to replicate:
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_TABU_SQL | ACTVT | 33 |
  | DBSID | * |
  | TABOWNER | standard DB schema(SAPABAP1) |
  | TABLE | *Target table name* |

- 
**ABAP Tables** - Grant access to ABAP dictionary and control tables for metadata and replication management:
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_TABU_SQL | ACTVT | 33 |
  | DBSID | * |
  | TABOWNER | standard DB schema(SAPABAP1) |
  | TABLE | /HVR/BACKUP_CONFIGURATION  
/HVR/LOG_PARTITIONS  
/HVR/SERVICE_LOG_POSITIONS  
/HVR/TABLE_COLUMNS  
/HVR/TABLE_VIRTUAL_FILES  
/HVR/BACKUP_CATALOG_LOG_FILES 
/HVR/BACKUP_PARAMETER_FILE 
/HVR/ROOT_KEYS_EXTRACT 
 DD02L*  
DD02T*  
DD03L*  
DD04L*  
DD06T*  
DD08L*  
DD09L*  
DD16S  
DDNTF  
DDNTT*  
HVR_IS_ARCHBLK  
HVR_STIN_ARCBLK  
TADIR* |

- 
**Database-specific System Tables**
NetWeaver on SAP HANA
Grant access to the following SYS schema tables in addition to specific data tables and ABAP tables.
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_TABU_SQL | ACTVT | 33 |
  | DBSID | * |
  | TABOWNER | * |
  | TABLE | CLIENTSIDE_ENCRYPTION_COLUMN_K 
 CS_ALL_COLUMNS 
CS_COLUMNS_ 
CS_CONCAT_ATTRIBUTES_ 
CS_TABLES_ 
DUMMY 
HAS_NEEDED_SYSTEM_PRIV 
HAS_NEEDED_SYSTEM_PRIV_INCL_SY 
INDEX_COLUMNS 
M_CONNECTIONS 
M_DATABASE 
NUMA_NODE_PREFERENCE_ 
P_DATATYPES_ 
P_GRANTEDPRIVS_ 
P_INDEXES_ 
P_MASK_EXPRESSION_ 
P_OBJTYPES_ 
P_PRINCIPALS_ 
P_PROCEDURES_ 
P_SCHEMAS_ 
P_USERS_ 
RS_COLUMNS_ 
RS_TABLES_ 
SERIES_DATA_ 
TABLES 
TABLE_COLUMNS 
VIRTUAL_COLUMNS_ 
VIRTUAL_TABLES_ 
_SYS_CS_TABLE_COLUMNS 
_SYS_GRANTED_OBJECTS 
_SYS_GRANTEE_OIDS 
_SYS_RS_TABLE_COLUMNS 
_SYS_SCHEMAS_WITH_PRIVILEGES_O 
_SYS_VIRTUAL_TABLE_COLUMNS |
NetWeaver on Oracle
Grant access to the following Oracle dictionary and system objects in addition to specific data tables and ABAP tables.
 AUTHORIZATION OBJECT | AUTHORIZATION FIELD | AUTHORIZATION VALUE |
 S_TABU_SQL | ACTVT | 33 |
  | DBSID | * |
  | TABOWNER | * |
  | TABLE | _SYS_CS_TABLE_COLUMNS  
 _SYS_GRANTED_OBJECTS  
 _SYS_GRANTEE_OIDS  
 _SYS_RS_TABLE_COLUMNS  
 _SYS_SCHEMAS_WITH_PRIVILEGES_O  
 _SYS_VIRTUAL_TABLE_COLUMNS  
 :BF0000  
 ALL_LOBS  
 ALL_NESTED_TABLES  
 ALL_OBJECTS  
 ATTRCOL$  
 CDEF$  
 CLIENTSIDE_ENCRYPTION_COLUMN_K  
 CLU$  
 COL$  
 COLLECTION$  
 COLTYPE$  
 CON$  
 CS_ALL_COLUMNS  
 CS_COLUMNS_  
 CS_CONCAT_ATTRIBUTES_  
 CS_TABLES_  
 DBA_OBJECTS  
 DEFERRED_STG$  
 DEPENDENCY$  
 DUAL  
 DUMMY  
 ENC_IDX  
 FILE$  
 HAS_NEEDED_SYSTEM_PRIV  
 HAS_NEEDED_SYSTEM_PRIV_INCL_SY  
 IND$  
 INDEX_COLUMNS  
 INDPART$  
 INDSUBPART$  
 I_ATTRCOL1  
 I_COBJ#  
 I_COLLECTION1  
 I_COLTYPE2  
 I_CON2  
 I_DEFERRED_STG1  
 I_DEPENDENCY1  
 I_FILE#_BLOCK#  
 I_FILE2  
 I_HH_OBJ#_INTCOL#  
 I_IND1  
 I_INDPART_OBJ$  
 I_INDSUBPART_OBJ$  
 I_LINK1  
 I_LOB$_FRAGOBJ$  
 I_LOB2  
 I_NTAB3  
 I_OBJ#  
 I_OBJ1  
 I_OBJ2  
 I_OBJ3  
 I_OBJ4  
 I_OBJ5  
 I_OBJAUTH1  
 I_OLAP_CUBES$  
 I_SUM$_1  
 I_TABCOMPART$  
 I_TABPART_OBJ$  
 I_TABSUBPART$_OBJ$  
 I_TRIGGER2  
 I_TS#  
 I_TYPE2  
 I_UNDO2  
 I_USER#  
 I_USER1  
 I_USER2  
 LOB$  
 LOBFRAG$  
 M_CONNECTIONS  
 M_DATABASE  
 NTAB$  
 NUMA_NODE_PREFERENCE_  
 OBJ$  
 PARTLOB$  
 P_DATATYPES_  
 P_GRANTEDPRIVS_  
 P_INDEXES_  
 P_MASK_EXPRESSION_  
 P_OBJTYPES_  
 P_PRINCIPALS_  
 P_PROCEDURES_  
 P_SCHEMAS_  
 P_USERS_  
 RS_COLUMNS_  
 RS_TABLES_  
 SEG$  
 SERIES_DATA_  
 SUM$  
 SYS_DBA_SEGS  
 SYS_OBJECTS  
 TAB$  
 TABCOMPART$  
 TABLES  
 TABLE_COLUMNS  
 TABPART$  
 TABSUBPART$  
 TRIGGER$  
 TS$  
 UNDO$  
 USER$  
 USER_EDITIONING$  
 VIRTUAL_COLUMNS_  
 VIRTUAL_TABLES_  
 VW*  
 X$CON  
 X$DNFS_FILES  
 X$KCCAL  
 X$KCCDI  
 X$KCCDI2  
 X$KCCFN  
 X$KCCIC  
 X$KCCLE  
 X$KCCLE (IND:1)  
 X$KCCRT*  
 X$KGLCURSOR_CHILD  
 X$KQLFXPL*  
 X$KRSTDEST  
 X$KSLED*  
 X$KSLWT  
 X$KSPPCV  
 X$KSPPI  
 X$KSPPSV  
 X$KSUSE*  
 X$KTADM  
 X$KTCXB  
 X$KZEKMENCWAL  
 X$KZSPR  
 X$KZSRO  
 X$NLS_PARAMETERS  
 X$VERSION |




## Configuration


The following must be configured to use HVR with SAP NetWeaver for replication:

### Install NetWeaver RFC SDK Libraries


HVR requires NetWeaver RFC SDK version **7.50.8** or above installed on the machine from where HVR connects to the SAP NetWeaver.

- 
Go to the SAP software [download](https://support.sap.com/) page.

- 
Download and extract the Unicode SAP NetWeaver RFC SDK libraries that are specific to the operating system.

- 
Copy the below mentioned files from the **/lib** directory (available in the extracted path) to any directory of your preference.
Click here for the list of library files to be copied. OPERATING SYSTEM | LIBRARIES |
 Linux 64 bit | libicudata.so.*xx*  
libicudecnumber.so  
libicui18n.so.*xx*  
libicuuc.so.*xx*  
libsapnwrfc.so  
libsapucum.so |
 Windows 64 bit | icudtxx.dll  
icuinxx.dll  
icuucxx.dll  
libsapucum.dll  
libicudecnumber.dll  
sapnwrfc.dll |

- 
For Linux, set the <b>read</b>, <b>write</b>, and <b>execute</b> permissions for each NetWeaver RFC library files.



### Import HVR’s Transports


Import the transports containing HVR’s ABAP functions. Use your company's default method to import the transports provided.

> **Note:** 
While importing you may need to use the option **Ignore Invalid Component Version** to suppress import errors.


The transport files are available in the **HVR_HOME/dbms/netweaver** directory. For information about the latest transports files, refer to the **readme.txt** available in the same directory.

### Configure AppConnect in SAP


HVR's AppConnect has a number of configuration parameters that can be used to tune and optimize the data extraction. These parameters can be accessed via the SAP transaction - **/N/HVR/CONFIG**.

In most cases, these parameters can be left with the default values. When you need to make a change, trigger a change mode and save new values into variant "ACTIVE".
 PARAMETER | DESCRIPTION |
 Max wait background | Maximum idle runtime for background processes. |
 Max wait foreground | Maximum idle runtime for foreground processes. |
 DB read max wait active | Maximum time spent in active mode in DB read process. |
 DB read max wait passive | Maximum time spent in passive (wait) mode in DB read process. |
 RFC read max wait passive | Maximum time spent in passive (wait) mode in RFC read process. |
 Memory tunnel size | Size of shared memory buffer used in SAP. |
 Max size uncompressed | Maximum data package size. |
 Application server | Name of the dedicated application server. Value for this parameter can be set to **NONE**, however, it should only be used when instructed by Fivetran support. |
 DB connection name | Secondary database connection name to be used in case you do not want to use the standard SAP database connection. Value for this parameter can be set to **DEFAULT**, however, it should only be used when instructed by Fivetran support. |
 Activate event log | Activate logging for DB read process (job logs). |
 Activate RFC trace | Activate logging for RFC read processes (application log). |

## Limitations


- HVR's AppConnect does not support replicating LOB (BLOB, CLOB, NCLOB) data that is larger than 30k bytes. In case the LOB contains more than 30k bytes, data is silently truncated.
- In versions prior to 6.1.0/3, for [NetWeaver on Oracle](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements/sap-netweaver-as-source#capture), HVR does not support unpacking the SAP tables using the parameter [**SapUnpack**](https://fivetran.com/docs/hvr6/action-reference/transform#sapunpack) in action [**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform).


## Related Articles


- [SAP NetWeaver as Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements/sap-netweaver-as-source)
- [Location Connection for SAP NetWeaver](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection/location-connection-for-sap-netweaver)

