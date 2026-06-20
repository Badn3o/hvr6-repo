# Oracle as Source - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/index.md)

# Oracle as Source


## Capture


Fivetran HVR allows you to capture changes from Oracle database. This section describes the configuration requirements for capturing changes from Oracle database. For the list of supported Oracle versions from which HVR can capture changes, see [Capture changes from location](https://fivetran.com/docs/hvr6/capabilities/610#capture) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

By default, HVR performs log-based capture.

### Table Types


HVR supports capture from the following table types in Oracle:

- Ordinary (heap-organized) tables
- Partitioned tables
- Index-organized tables


### Capture Methods


HVR allows the following methods for capturing ([**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture)) changes from Oracle:

- [**Direct Redo Access**](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-direct-redo-access)
Capture changes directly from Oracle's redo and archive file.
- [**Archive Only**](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-archive-only)
Capture changes from Oracle's transaction log backup files.
- [**LogMiner**](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-logminer)
Capture changes using Oracle LogMiner over an SQL connection.
- [**BFile**](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-bfile)
Capture changes using Oracle BFile method.


### Grants for Log-Based Capture


This section lists the grants required for capturing changes from Oracle database.

> **Note:** 
HVR can either connect to the database as the owner of the replicated tables, or it can connect as a special user (e.g. *username*).


- 
The HVR database **User** must be granted the <b>create session</b> privilege:
grant create session to <em>username</em>;

- 
To improve the performance of [Activate Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) ([**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate)) for channels with a large number of tables (more than 150), HVR creates a temporary table (**hvr_sys_table**) within a schema.
The HVR database **User** must be granted the <b>create table</b> privilege so that HVR can automatically create this temporary table:

> **Note:** 
If you do not wish to provide <b>create table</b> privilege to the HVR database **User**, the alternative method is to manually create this temporary table using the SQL statement:
create global temporary table hvr_sys_table (table_name varchar(128), table_owner varchar(128));

This temporary table is not used when capturing from a Data Guard standby database.


- 
The HVR database **User** must be granted the <b>select any table</b> privilege to replicate tables that are owned by other schemas (using the parameter [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema) in action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties)). Else, the HVR database **User** must be granted the individual table-level <b>select</b> privileges.
grant select any table to <em>username</em>;

- 
The HVR database **User** must be granted the <b>select any dictionary</b> privilege to read the data dictionaries in Oracle's **SYS** schema.
grant select any dictionary to <em>username</em>;

Alternatively, the HVR database **User** may be granted <b>select</b> privilege only for the required data dictionary objects:
Click here for the specific grantsgrant select on sys.v_$archive_dest to <em>username</em>;

grant select on sys.v_$archived_log to <em>username</em>;

grant select on sys.v_$database to <em>username</em>;

grant select on sys.v_$database_incarnation to <em>username</em>;




/* The following grant (sys.v_$dnfs_files) is required for identifying the redo files located on DirectNFS */

grant select on sys.v_$dnfs_files to <em>username</em>;




/* The following grant (sys.v_$encryption_wallet) is required for decryption */

grant select on sys.v_$encryption_wallet to <em>username</em>;

grant select on sys.v_$log to <em>username</em>;

grant select on sys.v_$logfile to <em>username</em>;




/* The following grant (sys.v_$logmnr_contents) is required for Oracle LogMiner capture method. */

grant select on sys.v_$logmnr_contents to <em>username</em>;

grant select on sys.v_$nls_parameters to <em>username</em>;

grant select on sys.v_$parameter to <em>username</em>;

grant select on sys.v_$pdbs to <em>username</em>;

grant select on sys.v_$session to <em>username</em>;




/* The following grant (sys.v_$system_parameter) is required for reading the value of 'filesystemio_options' parameter which in turn is used for reading the redo logs */

grant select on sys.v_$system_parameter to <em>username</em>;

grant select on sys.all_cons_columns to <em>username</em>;

grant select on sys.all_constraints to <em>username</em>;

grant select on sys.all_ind_columns to <em>username</em>;

grant select on sys.all_indexes to <em>username</em>;

grant select on sys.all_lobs to <em>username</em>;

grant select on sys.all_log_groups to <em>username</em>;

grant select on sys.all_objects to <em>username</em>;

grant select on sys.all_tab_cols to <em>username</em>;

grant select on sys.all_tables to <em>username</em>;

grant select on sys.all_triggers to <em>username</em>;

grant select on sys.all_encrypted_columns to <em>username</em>;

grant select on sys.dba_tablespaces to <em>username</em>;

grant select on sys.obj$ to <em>username</em>;




/* The following grant (sys.ecol$) is required for Oracle Database 11.2 and above since default values for added columns are stored differently. */

grant select on sys.ecol$ to <em>username</em>;




grant select on sys.user$ to <em>username</em>;

grant select on sys.col$ to <em>username</em>;

grant select on sys.enc$ to <em>username</em>;

grant select on sys.indpart$ to <em>username</em>;

grant select on sys.tabpart$ to <em>username</em>;

grant select on sys.tabsubpart$ to <em>username</em>;




/* The following three grants are required for Refreshing Data (<b>hvrrefresh</b> with option <b>-qrw</b>) and action <b>AdaptDDL</b> */

grant select on sys.v_$locked_object to <em>username</em>;

grant select on sys.v_$transaction to <em>username</em>;

grant select on sys.dba_objects to <em>username</em>;

- 
The HVR database **User** must be granted the following privilege to capture <b>create table</b> statements and add supplemental logging to the newly created table(s):
grant alter any table to <em>username</em>;

- 
The HVR database **User** must be granted the following privileges to use action [**DbSequence**](https://fivetran.com/docs/hvr6/action-reference/dbsequence):
grant select any sequence to <em>username</em>;

grant select on sys.seq$ to <em>username</em>;



> **Note:** 
An alternative to all of the above grants is to provide the **sysdba** privilege to the HVR database **User** (e.g. *username*):

- 
On Unix and Linux, add the user name used by HVR to the line in **/etc/group** for the Oracle sysadmin group.

- 
On Windows, right-click **My Computer** and select **Manage ▶ Local Users and Groups ▶ Groups ▶ ora_dba ▶ Add to Group ▶ Add**.




### Supplemental Logging


HVR needs the Oracle supplemental logging feature enabled on replicate tables that it replicates. Otherwise, when an <b>update</b> is done, Oracle will only log the columns which are changed. But HVR also needs other data (e.g. the key columns) so that it can generate a full <b>update</b> statement on the target database. The Oracle supplemental logging can be set at the database level and on specific tables. In certain cases, this requirement can be dropped by defining action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameter [**CaptureFromRowId**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#capturefromrowid), for more information, see section [Capturing from Oracle ROWID](#capturingfromoraclerowid).

> **Important:** 
- 
Oracle database versions prior to 12.2 limit the [names of identifiers](https://docs.oracle.com/en/database/oracle/oracle-data-access-components/19.3/odpnt/EFCoreIdentifier.html#GUID-FA43F1A1-EDA2-462F-8844-45D49EF67607) (such as tables, columns, and primary keys) to 30 characters.

- 
Oracle database versions 12.2 and higher allow up to 128 characters. To enable the supplemental logging for identifiers (such as tables, columns, and primary keys) whose names exceed 30 characters in versions 12.2 and higher, you must set the [**ENABLE_GOLDENGATE_REPLICATION**](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ENABLE_GOLDENGATE_REPLICATION.html#GUID-600FC071-1516-49B2-B3B3-C1C5430C5917) parameter to **true** on the source Oracle database. Ensure that you have the necessary license to use this parameter.




The very first time that [Activate Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) ([**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate)) runs, it will check if the database allows any supplemental logging at all. If it is not, then [Activate Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) will attempt statement <b>alter database add supplemental log data</b> (see [Extra Grants for Supplemental Logging](#extragrantsforsupplementallogging) to execute this statement). Note that this statement will hang if other users are changing tables. This is called 'minimal supplemental logging'; it does not actually cause extra logging; that only happens once supplemental logging is also enabled on a specific table.

Following are the SQL statements for enabling/disabling the supplemental logging manually:

- 
To enable minimal database-level supplemental logging:
 alter database add supplemental log data;

- 
To enable table-level supplemental logging -

- If the table does not have a primary key or unique index, or if action **ColumnProperties** is defined with parameter [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey): alter table <em>tablename</em> add supplemental log data (all) columns;

- If the table has a primary key: alter table <em>tablename</em> add supplemental log data (primary key) columns;

- If the table does not have a primary key but has a unique index: alter table <em>tablename</em> add supplemental log group <em>groupname</em> (column_1, column_2,...) always;



- 
To check the status of supplemental logging at database-level:
 select supplemental_log_data_min, supplemental_log_data_pk, supplemental_log_data_all from v$database;

This query should return at least **['YES', 'NO', 'NO']**

- 
To check the status of supplemental logging at table level:
 select log_group_type from all_log_groups where table_name='<em>tablename</em>';

- 
To disable supplemental logging at database-level:
 alter database drop supplemental log data;

- 
To disable supplemental logging at table level -

- 
If the table does not have a primary key or unique index:
 alter table <em>tablename</em> drop supplemental log data (all) columns;

- 
If the table has a primary key:
 alter table <em>tablename</em> drop supplemental log data (primary key) columns;





[Activate Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) will normally only enable supplemental logging for the key columns of each replicated table, using statement <b>alter table</b> <em>tab1</em> <b>add supplemental log data (primary key) columns</b>. But in some cases, [Activate Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) will instead perform <b>alter table</b> <em>tab1</em> <b>add supplemental log data (all) columns</b>, this will happen if either of the following condition is met:

- the key defined in the replication channel differs from the Oracle table's primary key or
- a table has any type of compression enabled or
- no key is defined in the replication channel and parameter [**NoDuplicateRows**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#duplicaterows) of action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) is not defined on the table or
- one of the following actions with the mentioned parameters is defined on the table:
- 
On the capture location:

 Location | Action | Parameter |
 Source | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** | **[CaptureExpression](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression)** |
 Source | **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** | **[CaptureCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#capturecondition)**, **[HorizColumn](https://fivetran.com/docs/hvr6/action-reference/restrict#horizcolumn)** |


- 
On the target location:

 Location | Action | Parameter |
 Target | **[FileFormat](https://fivetran.com/docs/hvr6/action-reference/fileformat)** | **[BeforeUpdateColumns](https://fivetran.com/docs/hvr6/action-reference/fileformat#beforeupdatecolumns)** |


- 
On any location:

 Location | Action | Parameter |
 * | **[CollisionDetect](https://fivetran.com/docs/hvr6/action-reference/collisiondetect)** | 
 |
 * | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** | ****[IntegrateExpression](https://fivetran.com/docs/hvr6/action-reference/columnproperties#integrateexpression)**, **[Key](https://fivetran.com/docs/hvr6/action-reference/columnproperties#key)**** or ****[TimeKey](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey)**** |
 * | **[Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate)** | **[DbProc](https://fivetran.com/docs/hvr6/action-reference/integrate#dbproc)** or **[Resilient](https://fivetran.com/docs/hvr6/action-reference/integrate#resilient)** |
 * | **[Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate)** | **[RenameExpression](https://fivetran.com/docs/hvr6/action-reference/integrate#renameexpression)** |
 * | **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** | **[AddressTo](https://fivetran.com/docs/hvr6/action-reference/restrict#addressto)** or **[IntegrateCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#integratecondition)** |






#### Supplemental Log Data Subset Database Replication


HVR does not support the 'Supplemental Log Data Subset Database Replication' option on Oracle 19c and higher versions. This feature must be disabled for your Oracle database when using HVR for replication.

To verify whether the database is enabled for subset database replication (**'YES'** or **'NO'**), use the following query:
select supplemental_log_data_sr from v$database;

To disable this option, use the following query:
alter database drop supplemental log data subset database replication;

#### Capturing from Oracle ROWID


If none of the above requirements force HVR to enable supplemental logging on all columns, the requirement for supplemental logging on key columns can be removed by defining action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameters [**CaptureFromRowId**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#capturefromrowid) and [**SurrogateKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#surrogatekey) to the channel. When these actions are defined, HVR will consider the Oracle **rowid** column as part of the table and will use it as the key column during replication, and integrate it into the target database. The following two actions should be defined to the channel to instruct HVR to capture **rowid** values and to use them as surrogate replication keys. Note that these actions should be added before adding tables to the channel.

 Location | Action | Parameter | Annotation |
 Source | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/columnproperties#name)**=**hvr_rowid**, **[CaptureFromRowId](https://fivetran.com/docs/hvr6/action-reference/columnproperties#capturefromrowid)** | This action should be defined for capture location(s) only. |
 * | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/columnproperties#name)**=**hvr_rowid**, [**SurrogateKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#surrogatekey) | This action should be defined for both capture and integrate locations. |


#### Grants for Supplemental Logging


The HVR database **User** must be granted the privileges mentioned in section [Grants for Log-Based Capture](#grantsforlogbasedcapture) and additionally the following grants for using supplemental logging:

- To execute <b>alter database add supplemental log data</b>, the HVR database **User** must have the **sysdba** privilege. Otherwise, HVR will write an error message which requests that a different user (who does have this privilege) execute this statement.
- If HVR needs to replicate tables that are owned by other schemas, then optionally the HVR user can also be granted <b>alter any table</b> privilege, so that [Activate Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) ([**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate)) can enable supplemental logging on each of the replicated tables. If this privilege is not granted then [Activate Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) will not be able to execute the <b>alter table…add supplemental log data</b> statements itself; instead, it will write all the statements that it needs to execute into a file and then write an error message which requests that a different user (who does have this privilege) execute these <b>alter table</b> statements.


### Accessing and Managing Redo and Archive Log Files


For HVR to capture changes from Oracle, the Oracle instance must have archiving enabled. If archiving is not enabled, HVR will lose changes if it falls behind the redo logs or it is suspended for some time.

To enable archiving, execute the following command as **sysdba** against a mounted but unopened database:
alter database archivelog;

The current state of archiving can be checked with:
select log_mode from v$database;

#### Direct-Load Insert Capture


HVR supports capturing changes from Oracle's Direct-Load INSERT feature (e.g. using <b>insert</b> statements with 'append hints' such as <b>insert /*+ append */ into</b>). For HVR to capture these changes:

- A table/tablespace must not be in the **NOLOGGING** mode, as this mode bypasses redo logging.
- Archive log mode must be enabled.


#### Archive Destination Management


The current archive destination can be verified with:
select destination, status from v$archive_dest;

By default, this returns values like **USE_DB_RECOVERY_FILE_DEST, VALID**, indicating that HVR will read changes from the Flashback Recovery Area.

Alternatively, a custom archive destination can be defined:
alter system set log_archive_dest_1='location=/disk1/arch';

After changing the archive destination, restart the instance.

#### Retaining Archive Files for HVR


To prevent HVR from failing due to missing archive files, it is important to configure RMAN (Recovery Manager) to retain these files for an adequate period. HVR may need to access the oldest transaction that was still open, especially in the case of long-running transactions, or if the system falls behind in replication. Ensure that the retention period is sufficient to accommodate your system's configuration, typically requiring archive files to be available for a longer duration (e.g., 2 days).

In log-based capture scenarios, HVR may need to revert to reading Oracle archive or redo files. If your backup/recovery regime (such as RMAN) deletes these files too quickly, reconfigure it to guarantee that archive files remain available for the necessary period. The retention duration depends on factors like the maximum time replication might be interrupted and the potential need for a [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

### Capturing from SAP Source


HVR allows you to capture changes from an Oracle database which is used by an SAP ECC system. To enable capture using SAP dictionary, the location property **SAP Source** ([**SAP_Source_Schema**](https://fivetran.com/docs/hvr6/property-reference/location-properties#sapsourceschema)) must be defined while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) or by [editing the existing location's source and target properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#sourceandtargetproperties). Then while adding tables to a channel, the [**Table Selection**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-sap-tables-to-a-channel) dialog will display the SAP tables defined in the SAP dictionaries.

> **Important:** 
For [Usage-based Subscription](https://fivetran.com/docs/hvr6/getting-started/licensing), an additional SAP Unpack license is required to unpack the cluster and pool tables from the SAP database. Contact [Fivetran Technical Support](https://support.fivetran.com/hc/en-us) to obtain the necessary SAP Unpack license. For the [Consumption-based](https://fivetran.com/docs/hvr6/getting-started/licensing) model, a separate license is NOT required.


When SAP pool, cluster, and long text (STXL) tables are added to a channel using the [**Table Selection**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-sap-tables-to-a-channel) dialog, the following actions are automatically defined:

- 
[**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) with parameters [**PackedInside**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#packedinside), [**CoerceErrorPolicy**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrorpolicy), and [**CoerceErrorType**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrortype)

> **Important:** 
- For each container (pool/cluster) table a separate action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) is defined.
- This action is not defined for long text (STXL) tables.



- 
[**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform) with parameter [**SapUnpack**](https://fivetran.com/docs/hvr6/action-reference/transform#sapunpack)

> **Important:** 
Irrespective of the number of tables, only a single action [**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform) is defined.




> **Note:** 
SAP columns are non-nullable by default. They will be described as nullable in the hub's repository and thus as nullable in the target. This is valid for the non-key columns. Key columns will remain non-nullable.


#### SAP Data Types Conversion


<b>Since</b> v6.1.0/7

This option enables conversion/mapping of SAP specific data types (available in SAP dictionary meta-data) in source location to corresponding data type in the target location. The SAP specific data type will be localized with the source DB's data type and then mapped to HVR's Repository data type. For example, if you have an SAP system on Oracle, the DATS data type will be localized as Oracle's Date type, and then it is mapped to HVR Repository type ansidate.

This feature is supported for the following SAP specific data types:

- 
DATS

For primary key columns with the DATS data type, HVR converts the column to STRING instead of a date type to prevent target load failures caused by invalid date values.



> **Important:** 
If the **SAP Data Types Conversion** option is NOT selected, SAP specific data types are mapped to various other HVR Repository data types. For more information, see [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping#datatypemappingsourcetotargetdbms) for SAP NetWeaver (or SAP dictionary).


If the **SAP Data Types Conversion** option is selected during [location creation](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location), HVR will automatically define action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) with parameters [**CoerceErrorPolicy**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrorpolicy) and [**CoerceErrorType**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrortype).

> **Note:** 
If the **SAP Source** ([**SAP_Source_Schema**](https://fivetran.com/docs/hvr6/property-reference/location-properties#sapsourceschema)) location property/option is selected during [location creation](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location), by default, the **SAP Data Types Conversion** option also gets selected.


However, to enable SAP data type conversion for an existing location, select the **SAP Data Types Conversion** option by [editing the location's source and target properties](https://fivetran.com/docs/hvr6/user-interface/locations/location-details#sourceandtargetproperties) and then manually define action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) with parameters [**CoerceErrorPolicy**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrorpolicy) and [**CoerceErrorType**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrortype).

### Time Zone


The time zone of the machine running the HVR Agent (or the Capture process) must match the time zone of the Oracle database server. If they differ, set the [**TZ**](https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html) environment variable on the Oracle location to align the time zones:
 Group | Table | Action | Parameter(s) |
 ORACLE | * | [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) | [**Name**](https://fivetran.com/docs/hvr6/action-reference/environment#name)=**TZ** 
[**Value**](https://fivetran.com/docs/hvr6/action-reference/environment#value)=*time_zone* |

> **Note:** 
If the time zones are not aligned, the Capture process may fail when resetting to the current time. The reported latency may also be inaccurate.


## Compare and Refresh from Oracle


HVR allows you to perform only [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) and [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) from Oracle database (without using [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture)). This section describes the configuration requirements for performing only [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) and [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) from Oracle database.

### Grants for Compare and Refresh from Oracle


This section lists the grants required for performing only [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) and [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) from Oracle database.

- 
The HVR database **User** must be granted the <b>create session</b> privilege:
grant create session to <em>username</em>;

- 
The HVR database **User** must be granted the <b>select any table</b> privilege, if [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) and [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) needs to read from tables which are owned by other schemas (using the parameter [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema) in action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties)):
grant select any table to <em>username</em>;

- 
The HVR database **User** must be granted the following privileges to use the option **Select Moment** (option **-M** in CLI) available in [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) and [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data):
grant select flashback any table to <em>username</em>;

grant select any transaction to <em>username</em>;



## Best Practice for Upgrading Oracle Database on Source Location


When upgrading Oracle source database to a next release version, e.g. from 11g to 12c, the compatible mode can still be set to 11g.

The best practice when upgrading an Oracle source database to ensure no data is lost would be as follows:

- Stop the application making changes to the database.
- Ensure all the changes made by the application are captured: anticipate the latency to be at zero. For more information on monitoring the replication latency, refer to the [**Statistics**](https://fivetran.com/docs/hvr6/user-interface/statistics) page.
- Suspend all capture and integrate [jobs](https://fivetran.com/docs/hvr6/user-interface/jobs).
- Upgrade the database.
- Run [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) with the following options selected: **Jobs**, **Table Enrollment**, and **Capture Time and** **Transaction Files**.
- Restart all the [jobs](https://fivetran.com/docs/hvr6/user-interface/jobs).
- Start the application.


## Related Articles


- [Capture from Oracle using Direct Redo Access](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-direct-redo-access)
- [Capture from Oracle ASM](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-direct-redo-access/capture-from-oracle-asm)
- [Capture from Oracle Data Guard](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-direct-redo-access/capture-from-oracle-data-guard)


- [Capture from Oracle using Archive Only](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-archive-only)
- [Capture from Oracle using LogMiner](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-logminer)
- [Capture from Amazon RDS for Oracle](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-logminer/capture-from-amazon-rds-for-oracle)


- [Capture from Oracle using BFile](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-bfile)
- [Capture from Oracle TDE](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-tde)
- [Capture from Oracle Pluggable Database](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-pluggable-database)
- [Capture from Oracle RAC](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-rac)

