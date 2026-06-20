# AdaptDDL - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/adaptddl

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/adaptddl/index.md)

# AdaptDDL


By default, Fivetran HVR only handles database DML statements (such as INSERT, UPDATE and DELETE). The **AdaptDDL** action extends this capability, enabling HVR to handle DDL statements such as CREATE TABLE, DROP TABLE, ALTER TABLE ... ADD COLUMN, or DROP COLUMN.

This action is typically defined on both the capture location and the integrate location.
Expand for more information
When defined on the capture database, the **Capture** job reacts to DDL changes in tables already in the channel by updating the column information in the HVR repository tables. If parameter [**AddTablePattern**](#addtablepattern) is defined it will also add new tables to the channel.

If the action is also defined on the integrate database then the **Capture** job will then apply these DDL changes to the integrate databases. In some situations, it will perform ALTER TABLE on the target table in the integrate database. In other situations, it will do a [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), which will either CREATE or ALTER the target table and then resend the data from the capture database.

> **Important:** 
The DDL operation of adding/dropping columns in a table with [implicit key](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/keys#replicationkeys) will cause a [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).


The mechanism of **AdaptDDL** shares many 'regular' components of HVR replication. In fact the **Capture** job automatically handles each DDL change just as a careful operator using the HVR UI should. So if a **Capture** job encounters a DDL it will re-inspect the source table (as if it used [**Select/Add Tables**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel)); if it sees for example that a new table is needed it will automatically add it to the HVR repository tables. Sometimes the **Capture** job will do a [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), although where possible HVR will instead do an ALTER TABLE on the target table, for efficiency. A consequence of this mechanism is that many strong features of HVR will work normally with **AdaptDDL**:

- 
Heterogeneous replication (between different DBMS's) works normally with **AdaptDDL**

- 
Actions such as [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties), [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties), [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) and [**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform) work normally with **AdaptDDL**.

> **Important:** 
These actions must be defined for all tables (table="*****") for them to affect a new table that is added to a channel by **AdaptDDL**.


- 
Different [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) options (see parameter [**RefreshOptions**](#refreshoptions)) work normally with **AdaptDDL**.



Note that internally the **AdaptDDL** mechanism does NOT work by just getting the full CREATE TABLE SQL statement from the DBMS logging system and sending that through HVR internal pipeline. Instead the **Capture** job reacts to any DDL it detects by re-inspecting the table and 'adapting' the channel to reflect the new situation that it sees at that time (which may be later than the original DDL). This delayed response (instead of sending SQL DDL through a pipeline) has some advantages:

- 
In many situations the DBMS logging does not contain enough data after a DDL statement to continue (or start) replicating the table, so a [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) is necessary anyway. For example, during a big upgrade, DBMS logging on a table may have been disabled to bulk-load data.

- 
If a table has been dropped and created multiple times (maybe HVR was turned off during a weekend upgrade) then HVR will not waste time performing each intermediate change; it will instead 'skip' to the last version of the table.

- 
Sharing the 'regular' components of HVR allows its rich functionality to be used in an 'adaptive' channel. Otherwise **AdaptDDL** would only be usable in an homogeneous situation e.g.,a channel from Oracle version 11.1 to Oracle 11.1 with no special actions defined.



---

## Restrictions


- 
Capturing DDL changes using action **AdaptDDL** is supported only for certain location types. For the list of supported location types, see [Log-based capture of DDL statements using action AdaptDDL](https://fivetran.com/docs/hvr6/capabilities/610#adaptddlcap) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

- 
Action **AdaptDDL** is not supported when the target is a file location.

- 
Action **AdaptDDL** cannot be used together with parameter [**SapUnpack**](https://fivetran.com/docs/hvr6/action-reference/transform#sapunpack) in action [**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform).

- 
For Oracle, action **AdaptDDL** is not supported when [capturing from Oracle using LogMiner](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-using-logminer).

- 
For SQL Server, action **AdaptDDL** is not supported when capturing from a SQL Server Always On secondary node.



---

## Parameters


This section describes the parameters available for action **AdaptDDL**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from HVR documentation, emails, or demo notes.




### AddTablePattern


**Argument:** *pattern*

**Description:** Add new tables to the channel if the new table name matches *pattern*. If this parameter is not defined then new tables are never added to the channel.

Patterns can include wildcards (***** or **o?_line_***) or ranges (**ord_[a-f]**). For a list of patterns, either use a pattern containing a **|** symbol (example, **tmp*|temp***) or defining multiple **AdaptDDL** actions with **AddTablePattern** parameter. This action should be defined on all tables and typically on both capture and integrate locations. If parameter [**CaptureSchema**](#captureschema) is not defined then this table must be in the location's 'current' schema.

A table will not be replicated more than once, even if it matches multiple **AdaptDDL** actions defined with the **AddTablePattern** parameter.

> **Important:** 
- 
This parameter is only effective when defined on a capture location.

- 
This parameter is supported only for certain location types. For the list of supported location types, see [Log-based capture of DDL statements using action AdaptDDL](https://fivetran.com/docs/hvr6/capabilities/610#adaptddlcap) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).




---

### IgnoreTablePattern


**Argument:** *pattern*

**Description:** Ignore a new table despite it matching a pattern defined by the [**AddTablePattern**](#addtablepattern) parameter.

The styles of pattern matching for this parameter are the same as those of [**AddTablePattern**](#addtablepattern).

This parameter only affects tables matched by the [**AddTablePattern**](#addtablepattern) parameter in the same **AdaptDDL** action, not those matched by other [**AddTablePattern**](#addtablepattern) parameters in other **AdaptDDL** actions.

For example, when a channel has two **AdaptDDL** actions defined with the following parameters:
 Action | Parameters |
 **AdaptDDL** | [**AddTablePattern**](#addtablepattern)**=t***, **IgnoreTablePattern=tmp*|temp*** |
 **AdaptDDL** | [**AddTablePattern**](#addtablepattern)**=*x** |

This channel will automatically add tables **tab_1** and **tmp_x** but not table **tmp_y**.

> **Important:** 
- 
This parameter is only effective when defined on a capture location.

- 
This parameter is supported only for certain location types. For the list of supported location types, see [Log-based capture of DDL statements using action AdaptDDL](https://fivetran.com/docs/hvr6/capabilities/610#adaptddlcap) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).




---

### CaptureSchema


**Argument:** *schema*

**Description:** This parameter controls which schema's new tables are matched by parameter [**AddTablePattern**](#addtablepattern). Value *schema* is not a pattern (no '*****' wildcards) but it is case-insensitive.

If this parameter is not defined then the only new table that are matched are those in the location's 'current' or 'default' schema. When a new table is added using this parameter then HVR **Capture** job will automatically define the [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) action with [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema) parameter, unless the schema is the capture location's current schema.

> **Important:** 
- 
This parameter is only effective when defined on a capture location.

- 
This parameter is supported only for certain location types. For the list of supported location types, see [Log-based capture of DDL statements using action AdaptDDL](https://fivetran.com/docs/hvr6/capabilities/610#adaptddlcap) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).




---

### IntegrateSchema


**Argument:** *schema*

**Description:** This parameter allows a new table which is matched in a schema on a capture database defined with parameter [**CaptureSchema**](#captureschema) to be sent to a schema different from the default schema on an integrate database. One or more mappings to be defined.

For example, when a channel has two **AdaptDDL** actions defined with the following parameters:
 Action | Parameters |
 **AdaptDDL** | [**AddTablePattern**](#addtablepattern)**="*"**, [**CaptureSchema**](#captureschema)**=aa1**, **IntegrateSchema=bb1** |
 **AdaptDDL** | [**AddTablePattern**](#addtablepattern)**="*"**, [**CaptureSchema**](#captureschema)**=aa2**, **IntegrateSchema=bb2** |

Then table **aa1.tab** would be created in the integrate database as **bb1.tab** whereas table **aa2.tab** would be created in the target database as **bb2.tab**. Each table would be added to the channel with two [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) action defined with [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema) parameter; one on the capture location and one on the integrate location.

> **Important:** 
- 
This parameter is only effective when defined on a capture location, even though it actually causes actions to be generated on the integrate location group(s).

- 
This parameter is supported only for certain location types. For the list of supported location types, see [Log-based capture of DDL statements using action AdaptDDL](https://fivetran.com/docs/hvr6/capabilities/610#adaptddlcap) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).




---

### OnEnrollBreak


**Argument:** *policy*

**Description:** This parameter applies a *policy* to control the behavior of the **Capture** job for an existing table when there is a break in the enroll information (such as data type changes or partition changes). The job can execute a [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) in response to a DDL change.

For Oracle source tables, partition maintenance can change the partition metadata version that HVR stores in the capture enrollment information. In the capture job log, this appears as partition version updated. HVR treats this as a break in the enrollment information because the existing metadata may not be sufficient to ensure the correct row mapping and continuous change capture.

- With OnEnrollBreak=REFRESH (default), HVR refreshes the affected table and updates the capture enrollment metadata.
- With OnEnrollBreak=WARNING, HVR issues a warning and continues without the planned refresh. If necessary, it may only perform the ALTER TABLE. You must review the change and manually refresh, re-activate replication, or otherwise resolve the affected table if the target may no longer be consistent.
- With OnEnrollBreak=FAIL_INTEG_JOB, HVR omits the planned refresh and sends a breakpoint control to the involved **Integrate** jobs. After changes up to the DDL sequence are integrated, the control causes the **Integrate** job to fail. You must resolve the issue and remove the control manually.

Expand to see the options available for this parameter
Available values for *policy* are:

- 
**REFRESH** default: [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) the table.

- 
**FAIL_INTEG_JOB**: Send a breakpoint control to all involved **Integrate** jobs. Once all changes up to the DDL sequence are integrated, the control will cause the **Integrate** job to fail with an error. The problem must be solved manually and the control must be removed manually.

- 
**WARNING**: Issue a warning and then continue without the [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data). If necessary, perform only the ALTER TABLE.

This policy overrides the default behavior of the **OnEnrollBreak** parameter. In this policy, HVR will not automatically take actions it deems appropriate and instead only issues a warning, relying on user discretion. Choosing **WARNING** may lead to data discrepancies during replication. Since you are overriding the default behavior, any errors resulting from this choice are solely your responsibility and cannot be attributed to the product itself. Exercise caution when using this option and consider the potential consequences before proceeding.




> **Important:** 
- 
This parameter does not control the behavior of a **Capture** job for a new table being added to the channel.

- 
This parameter is only effective if defined on the target location where the [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) would load data into.

- 
If **OnEnrollBreak** is set to **WARNING** and [**OnAddColumnWithDefault**](#onaddcolumnwithdefault) is set to **REFRESH**, a table [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) needs to be performed when a new column with a default value is added.




---

### OnAddColumnWithDefault


<strong>Since</strong> v6.2.5/2

**Argument:** *policy*

**Description:** This parameter applies a *policy* to customize behavior when AdaptDDL detects new columns with default values.
Expand to see the options available for this parameter
Available values for *policy* are:

- 
**ADD_COLUMN_WITH_EMPTY_DEFAULT** default: Maintain the default behavior, where no distinction is made between columns with and without default values.

- 
**REFRESH**: Always [refresh](https://fivetran.com/docs/hvr6//getting-started/concepts/refresh) the table, replacing the data to ensure the source default value is present in the target.

- 
**FAIL_INTEG_JOB**: Send a breakpoint control to all involved **Integrate** jobs. Once all changes up to the DDL sequence are integrated, the control causes the **Integrate** job to fail with an error. The issue must be solved manually, and the control must be manually removed.

- 
**WARNING**: Perform the same behavior as **ADD_COLUMN_WITH_EMPTY_DEFAULT** but issue a warning.




> **Important:** 
- 
This parameter is only effective when defined on the target location where the [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) operation would load data into.

- 
If [**OnEnrollBreak**](#onenrollbreak) is set to **WARNING** and **OnAddColumnWithDefault** is set to **REFRESH**, a table [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) needs to be performed when a new column with a default value is added.

- 
Supported source databases include Oracle, SQL Server, Db2 for LUW, Db2 for i, Db2 for z/OS, PostgreSQL, MySQL, and Sybase ASE.




---

### OnPreserveAlterTableFail


**Argument:** *policy*

**Description:** This parameter applies a *policy* to control the behavior of **Capture** job for an existing table to handle any failure while performing ALTER TABLE on the target table.
Expand to see the options available for this parameter
Available values for *policy* are:

- 
**CREATE_AS_SELECT** default: Move existing table to a temporary table and create new table with new layout as selected from old table.

- 
**FAIL_INTEG_JOB**: Send a breakpoint control to all involved **Integrate** jobs. Once all changes up to the DDL sequence are integrated, the control will cause the **Integrate** job to fail with an error. The problem must be solved manually and the control must be removed manually.

- 
**WARNING**: Issue a warning and then continue replication without retrying to perform the ALTER TABLE.

This policy overrides the default behavior of the **OnPreserveAlterTableFail** parameter. In this policy, HVR will not automatically take actions it deems appropriate and instead only issues a warning, relying on user discretion. Choosing **WARNING** may lead to data discrepancies during replication. Since you are overriding the default behavior, any errors resulting from this choice are solely your responsibility and cannot be attributed to the product itself. Exercise caution when using this option and consider the potential consequences before proceeding.




> **Important:** 
This parameter is only effective if defined on the target location where the ALTER TABLE is being performed.


---

### RefreshOptions


**Argument:** *refropts*

**Description:** Configure which [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) options the **Capture** job should use to create or alter the target table(s) and (when necessary) re-populate the data.

All refreshes implied by **AdaptDDL** use context **adaptddl** (like [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) -Cadaptddl) so data truncated and selected can be controlled using action [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) with parameter [**Context**](https://fivetran.com/docs/hvr6/action-reference/restrict#context)=**adaptddl**.

> **Note:** 
Click the ellipsis (...) button to view the **Refresh Options** dialog. Once you select the desired option(s) in the **Refresh Options** dialog and click **Select**, the equivalent option letter is displayed in the **RefreshOptions** field of the **AdaptDDL** action dialog. You can also enter the option letters directly in the **RefreshOptions** field. If you are entering multiple options, they must be separated by a space.

Expand to see the options available for this parameter
Available options for *refropts* are:

- 
**Bulk Granularity**: Perform [bulk refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh#bulkrefresh) using bulk data load.

The equivalent option letter is -gb.

- 
**Row by Row Granularity**: Perform [row–wise refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh#rowbyrowrefresh).

The equivalent option letter is -gr.

- 
**Verbose**: This causes row–wise refresh to display each difference detected. Differences are presented as SQL statements.

The equivalent option letter is -v and it must be used with -gr (row-wise refresh).

- 
**Fire Triggers During Refresh**: Fire database triggers/rules while applying SQL changes with row-wise refresh. The default behavior is that database trigger/rule firing is disabled during refresh.

For Oracle and SQL Server, this is avoided by disabling and re-enabling the triggers.

The equivalent letter option is -f and it must be used with -gr (row-wise refresh).

- 
**Apply**: Mask (ignore) some differences between the tables that are being compared. If a difference is masked out, then the [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) will not rectify it.

The equivalent letter option is -m<em>mask</em> and it must be used with -gr (row-wise refresh).

Available options for *mask* are:

- **All**: Mask out all (DELETE, INSERT, UPDATE) differences.
- **No Deletes**: Mask out DELETE differences. The equivalent letter option is d.
- **No Inserts**: Mask out INSERT differences. The equivalent letter option is i.
- **No Updates**: Mask out UPDATE differences. The equivalent letter option is u.
- **No Deletes and Inserts**: Mask out DELETE and INSERT differences. The equivalent letter option is di.
- **No Deletes and Updates**: Mask out DELETE and UPDATE differences. The equivalent letter option is du.
- **No Inserts and Updates**: Mask out INSERT and UPDATE differences. The equivalent letter option is iu.




- 
**Parallelism for Locations**: Perform [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) into multiple locations in parallel using sub–processes.

The equivalent letter option is -p<em>N</em>. Where *N* is the number of sub–processes.

> **Important:** 
This parameter has no effect if there is only one integrate location.


- 
**Isolate Tables During Refresh**  <strong>Since</strong> v6.2.5/0: Isolate the table that is being refreshed. This allows the **Integrate** job to continue processing other tables without being suspended. Additionally, the **Capture** job can continue working during the **Refresh**. The isolated table is integrated after the [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) is completed.

The default value for this option is **now**, which means start isolation immediately once the isolate refresh event is created.

The equivalent letter option is -inow. Currently, this option do not support any other values.




> **Important:** 
This parameter is only effective when defined on an integrate location.


---

### OnDropTable


**Argument:** *policy*

**Description:** Applies a *policy* that controls the replication behavior if a DROP TABLE is done to a replicated table.

Available values for *policy* are:

- 
**KEEP**: Table will remain in channel. The **Capture** job will write a warning message in log. The next [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) will give table not found error when it attempts to regenerate enroll information for this channel.

- 
**DROP_FROM_CHANNEL_ONLY** default: Table (and its actions) are deleted from the repository tables only, but the table is left in any target databases.

- 
**DROP_FROM_CHANNEL_AND_TARGET**: Table (and all its actions) are deleted from the repository tables and the target table is dropped from the target databases.



> **Important:** 
If this is the last table in the channel, then HVR will not drop it from the repository table, instead the **Capture** job will fail because an HVR channel must always contains at least one table. If the value is **KEEP** or **DROP_FROM_CHANNEL_ONLY** and the table is created again in the capture database, then the old table in the integrate database will be reused; it will be recreated or an ALTER TABLE done to make its columns match.


---

### KeepExistingStructure


**Description:** Preserve old columns in target, and do not reduce data types sizes. This means if an ALTER TABLE statement was performed on the capture table to drop a column or make it smaller (e.g.,**varchar(12)** to **varchar(5)**) this will not be propagated to the target table. This can be used to protect historical data, which could have been purge of the capture database was not replicated (using action [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) with parameter [**IgnoreSessionNames**](https://fivetran.com/docs/hvr6/action-reference/capture#ignoresessionnames)) or if the integrate table contains a row for each capture change (using action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameter [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey)).

> **Important:** 
This parameter is only effective when defined on a integrate location.


---

### KeepOldRows


**Description:** Preserve old/existing rows ([**hvrrefresh -cp**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh)) in target table if the table is dropped and recreated with a new layout during [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data).

> **Important:** 
This parameter is only effective when **[RefreshOptions](#refreshoptions)** is set to **Row by Row Granularity**.


---

## Behavior for Specific DDL Statements and Capture DBMSs


This section explains the behavior of specific DDL statements during replication, with and without the **AdaptDDL** action defined, along with notes specific to supported capture DBMSs.

 DDL SQL Statement | Behavior without AdaptDDL | Behavior with AdaptDDL Defined | Notes for specific capture DBMS |
 `CREATE TABLE` | 
Capture job ignores DDL.

Operator must manually perform 'Adapt steps' (including **[Select/Add Tables](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel)** and **[Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)**) to add table to channel. | 
If new table is not in channel but the capture location has action **AdaptDDL** with a matching **[AddTablePattern](#addtablepattern)** defined then the table is added to the channel and supplemental logging is enabled (if necessary). If integrate database(s) also have action **AdaptDDL** then the capture job will do an HVR refresh which will also create the table in the target database(s).This refresh should be quick because the new table should be empty or at least very small.

If the table already existed in the integrate database it will be recreated or an `ALTER TABLE` used to make its columns match.

If parameter **[AddTablePattern](#addtablepattern)** is not defined or the table name does not match then this DDL statement is ignored. | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables.

For PostgreSQL, this DDL statement is not supported.
 |
 `DROP TABLE` | 
If a table was in the channel then capture job will write a warning message in log.

The next **[hvractivate](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate)** will give error ('table not found') when it attempts to regenerate enroll information for this channel. | If the table is in the channel then the behavior depends on value of **AdaptDDL** parameter **[OnDropTable](#ondroptable)**. | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables.

For PostgreSQL, this DDL statement is not supported.

For SQL Server, this is not allowed if the location property **[Supplemental_Logging](https://fivetran.com/docs/hvr6/property-reference/location-properties#supplementallogging)** is set to **ARTICLE_OR_CDCTAB** and if the table has a primary key because when HVR is capturing a table, the `DROP TABLE` statement gives "Cannot drop table … because it is being used for replication" [error 3724].
 |
 `CREATE TABLE` followed quickly by `DROP TABLE` | Both DDL statements are ignored. | 
If the `DROP TABLE` is already complete by the time the capture job encounters the first `CREATE TABLE` in the DBMS logging then the capture job will ignore both DDL statements.

If the `DROP TABLE` occurs after the capture job has finished processing the `CREATE TABLE` statement then each DDL statement will processed individually (see lines above). But if the `DROP TABLE` occurs while the capture job is still processing the `CREATE TABLE` statement then its refresh may fail with a 'table not found' error. But the capture job will then retry and succeed, because the `DROP TABLE` is already complete (see above). | For SAP HANA, multiple DDL operations in one transaction are not supported. |
 `DROP TABLE`, followed quickly by `CREATE TABLE` | Capture job will write a warning message when it sees the `DROP TABLE` and when it sees `CREATE TABLE` it will update its internal enroll information so that it can still parse new values. | If the `CREATE TABLE` is already complete by the time the capture job encounters the first `DROP TABLE` in the DBMS logging then the capture job will refresh the table again, because there may be updates to the newly recreated table which HVR cannot process because supplemental logging had no been created yet. It will then update its internal enroll information so that it can still parse new values. If the `CREATE TABLE` is has not happened by the time the capture job encounters the first `DROP TABLE` then these statements will be processed individually. | 
For SAP HANA, multiple DDL operations in one transaction are not supported.
 |
 `ALTER TABLE ... ADD COLUMN` – without a specified default value clause | New column will be ignored; it won't be added to target and its value won't be replicate or refreshed. But replication of other columns continues normally. Subsequent **[hvractivate](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate)** or **[hvrrefresh](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh)** commands will also work normally. | Capture job will add the column to the channel repository tables. If an integrate database(s) has action **AdaptDDL** then the capture job's behavior will do an `ALTER TABLE` to add the column to the table in the target database(s). For some DBMSs, the capture job will then refresh the data into the integrate location(s). Then replication will resume. | 
For Oracle and SQL Server, HVR will not refresh the data and just continue replication.

For PostgreSQL, the change made using this DDL statement is not immediately captured.
HVR detects this change during the next `INSERT` or `UPDATE` operation.
Since `6.2.5/5`, HVR detects this change during the next DML operation.

 |
 `ALTER TABLE ... ADD COLUMN` – with a specified default value clause | Same as regular `ALTER TABLE ... ADD COLUMN` above. | Similar to the regular `ALTER TABLE ... ADD COLUMN` command above, the target table will receive an  `ALTER TABLE ... ADD COLUMN` statement with a default value defined by HVR. This means that when HVR creates or alters tables, it assigns a default value to mandatory columns. The default value depends on the data type and is not inherited from the source database. As a result, when a column with a default value is added to the source database, the new column on the target will display the HVR default value for existing rows. Newly replicated values will get the correct value from the source. This default behavior can be modified by defining parameter **[OnAddColumnWithDefault](#onaddcolumnwithdefault)**.  | Same as for regular `ALTER TABLE ... ADD COLUMN`. |
 `ALTER TABLE ... DROP COLUMN` | Capture job will only update its internal enroll information so that it can still parse new values. If this was a key column or it was not nullable and had no default then integrate errors will start to occur. | Capture job will drop the column from the channel repository tables. If an integrate database(s) has action **AdaptDDL** then the capture job will use `ALTER TABLE` to drop the column to the table in the target database(s), unless parameter **[KeepExistingStructure](#keepexistingstructure)** is defined. In this case the columns is kept in the target. For some DBMSs, the capture job will then refresh the data into the integrate location(s). Then replication will resume. | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables. 
Db2 for z/OS requires a **REORG** to be performed after a column is dropped using this statement.

For Oracle and SQL Server, HVR will not refresh the data; it will simply continue with replication.

Note that both `ALTER TABLE ... ADD COLUMN` and `ALTER TABLE ... DROP COLUMN` usually resume replication without a refresh. However, there are some exceptions to this rule. If a column was dropped and then added again, HVR needs to refresh the data to assure that all data is replicated correctly.

For PostgreSQL, the change made using this DDL statement is not immediately captured.
HVR detects this change during the next `INSERT` or `UPDATE` operation.
Since `6.2.5/5`, HVR detects this change during the next DML operation.


Additionally, for SQL Server locations which have [**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod) set to **SQL**, dropping a column will cause a refresh to prevent potential issues with the ongoing capture.
 |
 `ALTER TABLE ... ALTER/CHANGE/MODIFY COLUMN` – to make column 'bigger', e.g., **varchar(5)** to **varchar(12)**. | Capture job will only update its internal enroll information so that it can still parse new values. But when a new large value is captured it will either cause an error in the integrate job, or if parameter **[CoerceErrorPolicy](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrorpolicy)** in action **[TableProperties](https://fivetran.com/docs/hvr6/action-reference/tableproperties)** is defined it will be truncated. | Capture job will change the column's information from the channel repository tables. If an integrate database(s) has action **AdaptDDL** then the capture job's will do an `ALTER TABLE` to change the target column's width. No refresh will be done to the target table. Then replication will resume. | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables. 
HVR requires a **REORG** to be performed if the size of a fixed length column is increased using the `ALTER TABLE ALTER COLUMN` statement.

For PostgreSQL, this DDL statement is supported since `6.2.5/5`.
 |
 `ALTER TABLE ... ALTER/CHANGE/MODIFY COLUMN` – to make column 'smaller', e.g., **varchar(12)** to **varchar(5)**. | Capture job will only update its internal enroll information so that it can still parse new values. No errors. | Capture job will change the column's information from the channel repository tables. If an integrate database(s) has action **AdaptDDL** then the capture job's will do an `ALTER TABLE` to change the target column's width, unless parameter **[KeepExistingStructure](#keepexistingstructure)** is defined. The capture job will then refresh the target table. Then replication will resume. | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables. 
Db2 for z/OS requires a **REORG** to be performed if the size of a column is decreased using the `ALTER TABLE ALTER COLUMN` statement.

For SAP HANA, this is not supported. You cannot make the field/column length smaller.

For PostgreSQL, this DDL statement is supported since `6.2.5/5`.
 |
 `ALTER TABLE ... ALTER/CHANGE/MODIFY COLUMN` – to change 'data type', e.g., **number** to **varchar(5)**. | Capture job will only update its internal enroll information so that it can still parse new values. But when a new value is captured the integrate job may give an error if it cannot convert the new value into the target's old data type. | Capture job will change the column's information in the channel repository tables. HVR refresh has the ability to alter columns on some database platforms, typically based on database limitations. If an integrate database(s) has action **AdaptDDL** then the capture job will either do an `ALTER TABLE` to drop the column to the table in the target database(s), or if `ALTER TABLE` in the target DBMS cannot change data types (e.g., for BigQuery, Databricks, and SingleStore) then the table will be dropped and recreated. The capture job will then refresh the target table. Then replication will resume. | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables. 
Db2 for z/OS requires a **REORG** to be performed if the data type of a column is changed using this statement.

For PostgreSQL, this DDL statement is supported since `6.2.5/5`.
 |
 `ALTER TABLE ... MODIFY COLUMN` – to change 'encryption', e.g., enable encryption or change encryption algorithm. | Capture job will warn that the channel definition should be upgraded and a refresh should be done. It will also give an error because it cannot handle the encrypted columns correctly. | Capture job will change the column's encryption information in its internal enroll information. It will then refresh the target table. Then replication will resume. The capture job will not replicate the encryption setting change to the target table. | This is supported only on Oracle 11 and higher. For more information on HVR support of Oracle's encryption feature (TDE), see [Capture from Oracle TDE](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements/oracle-as-source/capture-from-oracle-tde). |
 `ALTER TABLE ... RENAME COLUMN` | Capture job will only update its internal enroll information so that it can still parse new values. If this was a key column or it was not nullable and had no default then integrate errors will start to occur. | Capture job will change the table's information in the channel repository tables. If an integrate database(s) has action **AdaptDDL** then the capture job will either do an `ALTER TABLE` to rename the column to the table in the target database(s), or if `ALTER TABLE` in the target DBMS cannot rename columns then the table will be dropped and recreated. The capture job will then refresh the target table. Then replication will resume. | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables.

For PostgreSQL, the change made using this DDL statement is not immediately captured.
HVR detects this change during the next `INSERT` or `UPDATE` operation.
Since `6.2.5/5`, HVR detects this change during the next DML operation.

SQL Server and Sybase does not support `ALTER TABLE ... RENAME COLUMN` but it uses the build in function **sp_rename**.

For Sybase, this operation is not supported during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture).
 |
 `TRUNCATE TABLE` | HVR captures this as a special DML statement (**hvr_op=5**), unless action **[Capture](https://fivetran.com/docs/hvr6/action-reference/capture)** is defined with parameter **[NoTruncate](https://fivetran.com/docs/hvr6/action-reference/capture#notruncate)**. This changes is applied as `TRUNCATE TABLE` by the integrate job, unless action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** is defined with parameter **[RefreshCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#refreshcondition)**. | HVR captures this as a special DML statement (**hvr_op=5**), unless action **[Capture](https://fivetran.com/docs/hvr6/action-reference/capture)** is defined with parameter **[NoTruncate](https://fivetran.com/docs/hvr6/action-reference/capture#notruncate)**. This changes is applied as `TRUNCATE TABLE` by the integrate job, unless action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** is defined with parameter **[RefreshCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#refreshcondition)**. | 
In Db2 for z/OS, `TRUNCATE TABLE` is captured as `DELETE` records for each row present. This is the default behavior of Db2 for z/OS for tables that are replicated. For more information, see [Db2 for z/OS documentation](https://www.ibm.com/docs/en/db2-for-zos/13?topic=statements-truncate#db2z_sql_truncate__title__6).

For PostgreSQL, `TRUNCATE` of table partitions is not captured.
 |
 `ALTER INDEX ... ON ... REBUILD` – in online mode, e.g., with **(online=on)** SQL Server only | Capture job will only update its internal enroll information so that it can still parse new values. | Capture job will only update its internal enroll information so that it can still parse new values. | 
 |
 `ALTER TABLE ... ADD CONSTRAINT ... PRIMARY KEY`
`CREATE UNIQUE INDEX`
`CREATE INDEX ... LOCAL (PARTITION ...)`
`DROP INDEX` | Ignored. But if a uniqueness constraint is relaxed on the capture database (for example if the primary key gets an extra column) then a uniqueness constraint violation error could occur during integration. | HVR maintains only a single key, known as replication key, in the HVR channel repository tables and in the target tables. If a capture table has multiple uniqueness constraints (for example, a primary key and several unique indexes), HVR applies an internal hierarchy to determine which constraint becomes the replication key. The primary key takes precedence if it exists. When the capture job encounteres this DDL statement, it will re-inspect the capture table to determine whether the replication key has changed. If the replication key has changed, the capture job will update the channel repository tables by adding, removing, or modifying the replication index. If the integrate database(s) are configured with the AdaptDDL action, the capture job will also update the replication index on the corresponding target tables. HVR ignores the index name and other attributes (such as fill factor), and all secondary indexes on the capture table. No refresh is needed after these changes. 
For Databricks targets in versions earlier than 6.2.5/9, HVR does not support replication of primary key constraints. | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables.

For PostgreSQL, this DDL statement is supported since `6.2.5/5`.
 |
 `ALTER TABLE ... ADD FOREIGN KEY` | Ignored. Replication continues correctly. | Ignored. Replication continues correctly. DDL not replicated/propagated to target database(s). | 
 |
 `ALTER TABLE ... RENAME TO ...` – Rename table | Capture job will write a warning message in log. The next [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) will give error ('table not found') when it attempts to regenerate enroll information for this channel. | This is treated like a `DROP TABLE` and a `CREATE TABLE`. So the old name is deleted from the repository tables and added to the target depending on parameter **[OnDropTable](#ondroptable)**. If the new table name matches parameter **[AddTablePattern](#addtablepattern)** then it is added to the channel. If integrate database(s) also have action **AdaptDDL** then the capture job will do a **[Refresh Data](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)** which will also create the new table name in the target database(s). | 
For Db2 for z/OS, this statement requires [supplemental logging enabled](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements/db2-for-z-os-as-source#capturingddlchanges) on **SYSIBM.SYSTABLES** and **SYSIBM.SYSINDEXES** system catalog tables.

For PostgreSQL, this DDL statement is not supported.

For MySQL, this DDL statement is not supported.

SQL Server and Sybase does not support `ALTER TABLE ... RENAME TO ...` but it uses the build in function **sp_rename**.

For Sybase, this operation is not supported during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture).
 |
 `ALTER TABLE ... TRUNCATE PARTITION` | Ignored. The deletes implied by this DDL statement will not be replicated. | If an integrate database(s) has action **AdaptDDL** then the capture job will refresh the target table. Then replication will resume. | 
For Sybase, this operation may cause a forced **[Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)**.

For SAP HANA, this is not supported.
 |
 `ALTER TABLE ... MERGE PARTITION` | Ignored. Replication continues correctly. | Ignored. Replication continues correctly. DDL not replicated/propagated to target database(s). | 
For Sybase, the enroll information will be updated and capture will continue.

For SAP HANA, any partition-related operation may cause a forced **[Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)**. The only exception is when adding a new partition to a table with a single partitioning scheme, provided that this scheme does not contain the **OTHERS** partition.
 |
 `ALTER TABLE ... SPLIT PARTITION` | Ignored. Replication continues correctly. | Ignored. Replication continues correctly. DDL not replicated/propagated to target database(s). | 
For Sybase, the enroll information will be updated and capture will continue.

For SAP HANA, any partition-related operation may cause a forced **[Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)**. The only exception is when adding a new partition to a table with a single partitioning scheme, provided that this scheme does not contain the **OTHERS** partition.
 |
 `ALTER TABLE ... EXCHANGE PARTITION` | Ignored. The changes implied by this DDL statement will not be replicated. | If an integrate database(s) has action **AdaptDDL** then the capture job will refresh the target table. Then replication will resume. | 
For Sybase, the enroll information will be updated and capture will continue.

For SAP HANA, this is not supported.
 |
 `ALTER TABLE ... MOVE TABLESPACE` | Ignored. Replication continues correctly. | Ignored. Replication continues correctly. DDL not replicated/propagated to target database(s). | 
 |
 `ALTER TABLESPACE ...` | Ignored. Replication continues correctly. | Ignored. Replication continues correctly. DDL not replicated/propagated to target database(s). | 
 |
 `CREATE SEQUENCE` | Changes captured and integrated if action **DbSequence** is defined. See that action for limitations. | Changes captured and integrated if action **[DbSequence](https://fivetran.com/docs/hvr6/action-reference/dbsequence)** is defined. See that action for limitations. | 
 |
 `DROP SEQUENCE` | Ignored. | Ignored. | 
 |
 `CREATE/DROP VIEW`
`CREATE/DROP SYNONYM` | Ignored. Replication continues correctly. | Ignored. Replication continues correctly. DDL not replicated/propagated to target database(s). | 
 |
 `CREATE/DROP TRIGGER` | Ignored. Replication continues correctly. | Ignored. Replication continues correctly. DDL not replicated/propagated to target database(s). | 
 |
 `CREATE/DROP PROCEDURE`
`CREATE/ALTER/DROP FUNCTION`
`CREATE/ALTER/DROP USER`
`CREATE/ALTER/DROP ROLE`
`CREATE/DROP DIRECTORY` | Ignored. Replication continues correctly. | Ignored. Replication continues correctly. DDL not replicated/propagated to target database(s). | 
 |
 **dbms_redefintion** – to change tables storage (partitioning, compression, tablespace, LOB storage etc..) but not information stored in HVR repository tables (column names, data types or key) | Capture job will only update its internal enroll information so that it can still parse new values. | HVR recognizes Oracle **dbms_redefintion** because it sees that the create time is same but the table id has changed. HVR assumes that no other zero other DDL (alter table) subsequently. in which case no refresh needed. Enroll information will be updated and capture will continue. | This is supported only on Oracle. |
 **dbms_redefintion** – to change tables storage (partitioning, compression, tablespace, LOB storage etc..) but not info stored in the HVR repository tables (column names, data types or key), followed by an alter table to change other column information. | Capture job will only update its internal enroll information, and will treat the subsequent DDL statement individually. | HVR recognizes Oracle **dbms_redefintion** because it sees that the create time is same but the table id has changed. HVR assumes (incorrectly) that no other zero other DDL (alter table) subsequently so it neglects to do a refresh. | This is supported only on Oracle. |
 **dbms_redefintion** – which changes information in the HVR repository tables (the column names, data types or primary key) | See row above showing behavior for specific `ALTER TABLE` type. | See row above showing behavior for specific `ALTER TABLE` type. | This is supported only on Oracle. |


---

## Use of Capture Start Moment with AdaptDDL


Problems can occur when [**Capture Start Moment**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication#capturestartmoment) (capture rewind) is used to go back to a time before a DDL statement changed a replicated table.

Background: The capture job parses its tables changes (called 'DML') using 'enroll information' which is created by [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication). This has an option called [**Table Enrollment**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication#tableenrollment) (option -oe) can be used to either (a) not regenerate this enroll information or to (b) only regenerate this enroll information. When the capture job encounters a DDL statement it will re-inspect the table and save the table's new structure as a 'revision' to its original enrollment information. This will help it process subsequent DML statements from the logging.

But if [**Capture Start Moment**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication#capturestartmoment) is used with [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) then the 'original' enrollment information created by that command may be newer than the DML changes that the capture job must parse. If a DDL statement (such as ALTER TABLE ... DROP COLUMN) was performed between the 'rewind' point where the capture job must start parsing and the moment when [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) generated the enrollment information, the capture job may fail when fail if it encounters a DML record using the old table structure. Such errors will no longer happen after the capture job encounters the actual DDL statement or after it passes the moment that [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) was run.

If the channel already existed, then one tactic to avoid such capture errors is to not regenerate existing enroll information when using [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) for capture rewind. But this could cause a different error, if a DDL statement happened after the 'old' capture job stopped running and before the new rewind point.

.Table_table__KJiU7 {
    overflow-x: unset !important;
    margin-bottom: 0rem !important;
}

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }

.actparam {
    padding-left: 20px;
}
