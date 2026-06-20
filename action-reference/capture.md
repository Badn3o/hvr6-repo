# Capture - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/capture

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/capture/index.md)

# Capture


Action **Capture** instructs Fivetran HVR to capture changes from a location. Various parameters are available to modify the functionality and performance of capture.

For a database location, HVR gives you an option to capture changes using the location's [**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod) property (log-based or trigger-based method). HVR recommends using the log-based data capture because it has less impact on database resources as it reads data directly from its logs, without affecting transactions, manages large volumes of data and supports more data operations, such as truncates, as well as DDL capture. In contrast, the trigger-based data capture creates triggers on tables that require change data capture, so firing the triggers and storing row changes in a shadow table slow down transactions and introduces overhead.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


When defined on a file location this action instructs HVR to capture files from a file location's directory. Changes from a file location can be replicated both to a database location and to a file location if the channel contains table information. In this case any files captured are parsed (see action [**FileFormat**](https://fivetran.com/docs/hvr6/action-reference/fileformat)).

If **Capture** is defined on a file location without table information then each file captured is treated as a 'blob' and is replicated to the integrate file locations without HVR recognizing its format. If such a 'blob' file channel is defined with only actions **Capture** and [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) (no parameters) then all files in the capture location's directory (including files in sub-directories) are replicated to the integrate location's directory. The original files are not touched or deleted, and in the target directory the original file names and sub-directories are preserved. New and changed files are replicated, but empty sub-directories and file deletions are not replicated.

Bidirectional replication (replication in both directions with changes happening in both file locations) is not currently supported for file locations. File deletion is not currently captured by HVR.

If **Capture** is defined on a file location without parameter [**DeleteAfterCapture**](#deleteaftercapture) and location property [**File_State_Directory**](https://fivetran.com/docs/hvr6/property-reference/location-properties#filestatedirectory) is used to define a state directory outside of the file location's top directory, then HVR file capture becomes read only; write permissions are not needed.

---

## Parameters


This section describes the parameters available for action **Capture**. By default, only the supported parameters for the selected location type(s) are displayed in the **Capture** dialog.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from HVR documentation, emails, or demo notes.




### IgnoreSessionName


**Argument**: *sess_name*

**Description**: Instruct the capture job to ignore changes performed by the specified session name. Multiple ignore session names can be defined for a job, either by defining **IgnoreSessionName** multiple times or by specifying a comma-separated list of names as its value.

Normally HVR capture avoids recapturing changes made during HVR integration by ignoring any changes made by sessions named **hvr_integrate**. This prevents looping during bidirectional replication but means that different channels ignore each other's changes. The session name actually used by integration can be changed using action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) with parameter [**SessionName**](https://fivetran.com/docs/hvr6/action-reference/integrate). For more information, see [Managing Recapturing Using Session Names](https://fivetran.com/docs/hvr6/advanced-operations/managing-recapturing-using-session-names).

If this parameter is defined for any table with log based capture, then it affects all tables captured from that location.

An example for using this parameter is available in section [Using IgnoreSessionName](#usingignoresessionname) (below).

---

### Coalesce


**Description**: Causes coalescing of multiple operations on the same row into a single operation. For example, an INSERT and an UPDATE can be replaced by a single INSERT; five UPDATEs can be replaced by one UPDATE, or an INSERT and a DELETE of a row can be filtered out altogether. The disadvantage of not replicating these intermediate values is that some consistency constraints may be violated on the target database.

This parameter should not be used together with parameter [**SapUnpack**](https://fivetran.com/docs/hvr6/action-reference/transform#sapunpack) in action [**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform#sapxform).

---

### NoBeforeUpdate


**Description**: Do not capture 'before row' for an update unless it is a key update. By default when an update happens HVR will capture both the 'before' and 'after' version of the row. This lets integration only update columns which have been changed and also allows collision detection to check the target row has not been changed unexpectedly. Defining this parameter can improve performance, because less data is transported. But that means that integrate will update all columns (normally HVR will only update the columns that were actually changed by the update statements and will leave the other columns unchanged).

If this parameter is defined for any table with log based capture, then it affects all tables captured from that location.

---

### NoTruncate


**Description**: Do not capture SQL truncate table statements such as TRUNCATE in Oracle and **modify** *mytbl* **to truncated** in Ingres.

If this parameter is not defined, then these operations are replicated using [**hvr_op**](https://fivetran.com/docs/hvr6/internal-objects/extra-columns-for-capture-fail-and-history-tables#hvrop) value **5**.

For Db2 for z/OS, this parameter affects only TRUNCATE IMMEDIATE. HVR will always capture TRUNCATE if used without IMMEDIATE option (this will be replicated using [**hvr_op**](https://fivetran.com/docs/hvr6/internal-objects/extra-columns-for-capture-fail-and-history-tables) value **0**).

This parameter is not supported for Microsoft SQL Server.

---

### AugmentIncomplete


**Argument**: *col_type*

**Description**: During **Capture**, HVR may receive partial/incomplete values for certain column types. Partial/incomplete values are the values that HVR cannot **Capture** entirely due to technical limitations in the database interface. This parameter instructs HVR to perform additional steps to retrieve the full value from the source database, this is called augmenting. This parameter also augments the missing values for key updates.

> **Important:** 
- Defining this parameter can adversely affect the **Capture** performance.
- If this parameter is not defined, and when a partial/incomplete value is received, the **Capture** will fail with an error.



Valid values for *col_type* are:

- 
**NONE** default: No extra augmenting is done.

- 
**LOB**: Capture will augment partial/incomplete values for all columns of a table, if that table contains at least one lob column. For key-updates, missing values are augmented too.

- 
**ALL**: Capture will augment partial/incomplete values for all columns of any table. For key-updates, missing values are augmented too.



In certain situations, the default behavior changes and you should not override it to a 'lesser' value to prevent data inconsistency.

- 
For Db2 for Linux Unix and Windows, **LOB** should be selected to capture columns with **xml** data type.

- 
For Db2 for z/OS, the default *col_type* is **LOB** and can only be changed to **ALL**.

- 
For Oracle, when [capturing using Logminer](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-logminer) ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod) = **LOGMINER**), the default *col_type* is **LOB** and can only be changed to **ALL**.

- 
For SQL Server, when [capturing using SQL Access](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements/sql-server-as-source/capture-from-sql-server-using-sql-access) ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod) = **SQL**), and tables contain non-key columns, the default *col_type* is **ALL** and can not be changed.

- 
Since v6.1.0/22, if action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameter [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey) is defined on a target, the default *col_type* is **LOB**. It can be changed to **NONE**. Augmenting will also be done for both key and non-key updates.



---

### IgnoreCondition


**Argument**: *sql_expr*

**Description**: Ignore (do not capture) any changes that satisfy expression *sql_expr* (e.g., **Prod_id < 100**). This logic is added to the HVR capture rules/triggers and procedures.

This parameter differs from the [**CaptureCondition**](https://fivetran.com/docs/hvr6/action-reference/restrict#capturecondition) parameter in the [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) action as follows:

- 
The SQL expression is simpler, i.e. it cannot contain subselects.

- 
The sense of the SQL expression is reversed (changes are only replicated if the expression is false).

- 
No 'restrict update conversion'. Restrict update conversion means if an update changes a row which did not satisfy the condition into a row that does satisfy the condition then the update is converted to an insert.



This parameter requires location property [**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod) set to **DB_TRIGGER**.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)**=DB_TRIGGER**) has been deprecated since 6.2.0/0.


---

### IgnoreUpdateCondition


**Argument**: *sql_expr*

**Description**: Ignore (do not capture) any update changes that satisfy expression *sql_expr*. This logic is added to the HVR capture rules/triggers and procedures.

This parameter requires location property [**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod) set to **DB_TRIGGER**.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)**=DB_TRIGGER**) has been deprecated since 6.2.0/0.


---

### HashBuckets


Ingres

**Argument**: *int*

**Description**: Identify the number *int* of hash buckets, with which the capture table is created. This implies that Ingres capture tables have a hash structure. This reduces the chance of locking contention between parallel user sessions writing to the same capture table. It also makes the capture table larger and I/O into it sparser, so it should only be used when such locking contention could occur. Row level locking (default for Oracle and SQL Server and configurable for Ingres) removes this locking contention too without the cost of extra I/O.

This parameter requires location property [**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod) set to **DB_TRIGGER**.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)**=DB_TRIGGER**) has been deprecated since 6.2.0/0.


---

### HashKey


Ingres

**Argument**: *col_list*

**Description**: Identify the list of columns *col_list*, the values of which are used to calculate the hash key value.

The default hash key is the replication key for this table.

The key specified does not have to be unique; in some cases concurrency is improved by choosing a non-unique key for hashing.

This parameter requires location property [**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod) set to **DB_TRIGGER**.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)**=DB_TRIGGER**) has been deprecated since 6.2.0/0.


---

### DeleteAfterCapture


File/FTP/SFTP

**Description**: Delete file after capture, instead of capturing recently changed files.

If this parameter is defined, then the channel moves files from the location. Without it, the channel copies files if they are new or modified.

---

### Pattern


File/FTP/SFTP

**Argument**: *pattern*

**Description**: Only capture files whose names match pattern.

The **default** pattern is **'**/*'** which means search all sub-directories and match all files.
Expand to see the possible patterns for this parameter
Possible *patterns* are:

- 
**'*.c'** – Wildcard, for files ending with **.c**. A single asterisk matches all or part of a file name or sub-directory name.

- 
**'**/*txt'** – Recursive Sub-directory Wildcard, to walk through the directory tree, matching files ending with **txt**. A double asterisk matches zero, one or more sub-directories but never matches a file name or part of a sub-directory name.

- 
**'*.lis'** Files ending with **.lis** or **.xml**

- 
**'a?b[d0-9]'** Files with first letter **a**, third letter **b** and fourth letter **d** or a digit. Note that [**a-f**] matches characters, which are alphabetically between **a** and **f**. Ranges can be used to escape too; [*****] matches ***** only and [**[**] matches character **[** only.

- 
'***.csv|*.xml|*.pdf**' Multiple patterns may be specified. In this case, all csv files, all xml files, all pdf files will be captured.

- 
**{***hvr_tbl_name***}** is only used when data is replicated from structured files to a database with multiple tables. If there are multiple tables in your channel, the capture job needs to determine to which table a file should be replicated and will use the file name for this. In this case, action **Capture** must be defined with parameter **Pattern**. This parameter is not required for channels with only 1 table in them.

- 
*Example 1*: In your channel, there is a file named **audit.csv** that needs to be replicated to a table called **audit**, where the column names match those in the CSV file. To achieve this, define action **Capture** on the source group with the parameter **Pattern={hvr_tbl_name}.csv** and action [**FileFormat**](https://fivetran.com/docs/hvr6/action-reference/fileformat) with the parameters [**Csv**](https://fivetran.com/docs/hvr6/action-reference/fileformat#csv) and [**HeaderLine**](https://fivetran.com/docs/hvr6/action-reference/fileformat#headerline).

- 
*Example 2*: In your channel, there is an S3 file named **202409261132205511628390000000000-ee7ba38d57f42998-2-3-00000000-sales_data-1.csv** that needs to be replicated to a table called **sales_data**, where the column names match those in the CSV file. To achieve this, define action **Capture** on the source group with the parameter **Pattern=*-*-*-*-*-{hvr_tbl_name}-*.csv** and action [**FileFormat**](https://fivetran.com/docs/hvr6/action-reference/fileformat) with the parameters [**Csv**](https://fivetran.com/docs/hvr6/action-reference/fileformat#csv) and [**HeaderLine**](https://fivetran.com/docs/hvr6/action-reference/fileformat#headerline). This pattern ensures that the portion of the filename matching **{hvr_tbl_name}** (in this case, **sales_data**) maps to the **sales_data** table in the target database.



- 
**{***hvr_address***}** When a file is matched with this pattern, it is only replicated to integrate locations specified by the matching part of the file name. Locations can be specified as follows:

- 
An integrate location name, such as **tgt1**.

- 
A location group name containing integrate locations, such as **TGTGRP**.

- 
An alias for an integrate location, defined using parameter [**AddressSubscribe**](https://fivetran.com/docs/hvr6/action-reference/restrict#addresssubscribe) in action [Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)**. For example, **22** or **Alias7**.

- 
A list of the above, separated by a semicolon, colon or comma, such as **src**, **tgt1**.



- 
**{***name***}** is only used for replicating files between directories ("blob file" or "flat file"). An example of the **{***name***}** pattern is **{abc}.txt**. The value inside the braces is an identifier. Although the 'named pattern' works the same as a wildcard (*****), but it also associates the captured file with a property named **{abc}**. This property can be used in the 'named substitution' (see [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) parameter [**RenameExpression**](https://fivetran.com/docs/hvr6/action-reference/integrate#renameexpression)).

*Example 1*: suppose a channel has capture pattern **{office}.txt** and rename expression **xx_{office}.data**. If file **paris.txt** is matched, theproperty **{office}** is assigned string value **paris**. This means it is renamed to **xx_paris.data**.

*Example 2*: suppose the **77-99.pdf** file on source needs to be renamed to **new-77-suff-99.pdf2** on target. In this case, the **Pattern** is **{a}-{b}.pdf**, and define action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) with parameter [**RenameExpression**](https://fivetran.com/docs/hvr6/action-reference/integrate#renameexpression)=**new-{a}-suff-{b}-pdf2**.



On Unix and Linux, file name matching is case sensitive (e.g., ***.lis** does not match file **FOO.LIS**), but on Windows it is case-insensitive. For FTP and SFTP the case sensitivity depends on the OS on which HVR is running, not the OS of the FTP/SFTP server.

---

### IgnorePattern


File/FTP/SFTP

**Argument**: *pattern*

**Description**: Ignore files whose names match *pattern*. For example, to ignore all files underneath sub-directory **qqq** specify ignore pattern **qqq/**/***. The rules and valid forms for **IgnorePattern** are the same as for [**Pattern**](#pattern), except that 'named patterns' are not allowed.

---

### IgnoreUnterminated


File/FTP/SFTP

**Argument**: *pattern*

**Description**: Ignore files whose last line does not match *pattern*. This ensures that incomplete files are not captured. This pattern matching is supported for UTF 8 files but not for UTF 16 file encoding.

---

### IgnoreSizeChanges


File/FTP/SFTP

**Description**: Changes in file size during capture is not considered an error when capturing from a file location.

---

### AccessDelay


File/FTP/SFTP

**Argument**: *secs*

**Description**: Delay reading file for *secs* seconds to ensure that writing is complete. HVR will ignore this file until its last create or modify timestamp is more than *secs* seconds old.

---

### UseDirectoryTime


File/FTP/SFTP

**Description**: When checking the timestamp of a file, check the modify timestamp of the parent directory (and its parent directories), as well as the file's own modify timestamp.

This can be necessary on Windows when parameter [**DeleteAfterCapture**](#deleteaftercapture) is not defined to detect if a new file has been added by someone moving it into the file location's directory; on Windows file systems moving a file does not change its timestamp. It can also be necessary on Unix/Windows if a sub-directory containing files is moved into the file location directory.

The disadvantage of this parameter is that when one file is moved into a directory, then all of the files in that directory will be captured again. This parameter cannot be defined with parameter [**DeleteAfterCapture**](#deleteaftercapture) (it is not necessary).

---

### OnCaptureTableEndCycle


**Description**: Manage the timing of capture and integration cycles. When enabled for a specific table, this parameter forces the immediate termination of both the capture and integration cycles after processing a transaction that includes the specified table.

This is particularly useful in scenarios requiring immediate processing after specific transactions, enabling the execution of an [AgentPlugin](https://fivetran.com/docs/hvr6/action-reference/agentplugin) on either the integrate or capture side right after the transaction is processed.

The primary effect of **OnCaptureTableEndCycle** is to ensure that any changes involving the specified tables are promptly captured and integrated, minimizing latency between data capture and integration. By ending the cycle immediately, it facilitates the rapid execution of subsequent processes or scripts that depend on the completion of the data capture and integrate cycle.

This parameter is only set on the source, typically with a single table in scope. It is generally used in conjunction with other **Capture** actions that have a [broader scope](https://fivetran.com/docs/hvr6/user-interface/action-list/adding-action#actionscopeselector), ensuring that while specific tables are processed immediately, the overall data capture strategy remains comprehensive.

---

## Writing Files while HVR is Capturing Files


It is often better to avoid having HVR capture from files while they are still being written. One reason is to prevent HVR replicating an incomplete version of the file to the integrate machine. Another problem is that if parameter [**DeleteAfterCapture**](#deleteaftercapture) is defined, then HVR will attempt to delete the file before it is even finished.

Capture of incomplete files can be avoided by defining [**AccessDelay**](#accessdelay) or [**IgnoreUnterminated**](#ignoreunterminated).

Another technique is to first write the data into a filename that HVR capture will not match (outside the file location directory or into a file matched with [**IgnorePattern**](#ignorepattern)) and then move it when it is ready to a filename that HVR will match. On Windows this last technique only works if [**DeleteAfterCapture**](#deleteaftercapture) is defined, because the file modify timestamp (that HVR capture would otherwise rely on) is not changed by a file move operation.

A group of files can be revealed to HVR capture together by first writing them in sub-directory and then moving the whole sub-directory into the file location's top directory together.

> **Important:** 
- 
If column [**hvr_op**](https://fivetran.com/docs/hvr6/internal-objects/extra-columns-for-capture-fail-and-history-tables#hvrop) is not defined, then it defaults to **1** (INSERT). Value **0** means DELETE, and value **2** means UPDATE.

- 
Binary values can be given with the **format** attribute (see example above).

- 
If the **name** attribute is not supplied for the **<column>** tag, then HVR assumes that the order of the **<column>** tags inside the **<row>** matches the order in the HVR repository tables (column **col_sequence** of the [**HVR_COLUMN**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrcolumn) repository table).




---

## Examples


This section includes an example of using the parameter [**IgnoreSessionName**](#ignoresessionname).

### Using IgnoreSessionName


HVR allows to run a purge process on an Oracle source location without stopping active replication. Purging is deleting obsolete data from a database. To ensure that the deleted data does not replicate to a target location, the purge process must be started by a database user (e.g., **PurgeAdmin**) other than the user (e.g., **hvruser**) under which the replication process is running, and HVR must be configured to ignore the session name of the **PurgeAdmin**.

The steps for implementing this scenario are as follows:

- 
In a source database, create a new user **PurgeAdmin** that will run a purge script against this database.

- 
Grant the applicable permissions to user **PurgeAdmin**. For example, a privilege to delete rows in another schema:
GRANT DELETE ANY TABLE TO PurgeAdmin;

- 
In the UI, update action **Capture** defined on the existing channel by adding parameter [**IgnoreSessionName**](#ignoresessionname):

- 
In the [**Actions**](https://fivetran.com/docs/hvr6/user-interface/action-list) panel, click on the row containing action **Capture**.

- 
In the **Action: Capture** dialog, select parameter [**IgnoreSessionName**](#ignoresessionname) and specify the user name **PurgeAdmin**.

- 
Click **OK**.




- 
Perform [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) to re-activate the capture job and apply the changes in action **Capture**:

- Click **Only Specific Replication Components** and enable only **Jobs**. [**Activating Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) with option **Jobs** will suspend and restart the affected jobs automatically.





.actparam {
    padding-left: 20px;
}
