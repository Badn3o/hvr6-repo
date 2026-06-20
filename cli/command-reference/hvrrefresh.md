# hvrrefresh - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvrrefresh/index.md)

# hvrrefresh


## Usages


<b>hvrrefresh</b> [<b>-R</b><em>url</em>] [<em>-options</em>]... <em>hub</em> <em>chn</em>

## Description


Command **hvrrefresh** copies tables (available in a channel) from source location(s) to target location(s). The source must be a database location, but the targets can be databases or file locations. For more information, see the [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) concept page.

> **Important:** 
For [consumption-based](https://fivetran.com/docs/hvr6/getting-started/licensing#consumptionbased) licensing, Fivetran offers a five-day troubleshooting window per table for performing free **Refreshes** in HVR. This window starts on the day you first perform a **Refresh** on a table in a given month. Any subsequent **Refreshes** done outside this window count towards paid [MAR](https://fivetran.com/docs/hvr6/getting-started/pricing).


Refreshing from a source location is supported only on certain location types. For the list of supported source location types, see section [Refresh and Compare](https://fivetran.com/docs/hvr6/capabilities/610#refreshandcompare) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

> **Note:** 
Command **hvrrefresh** corresponds to the [**Refresh Data into Target**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data) dialog in the [User Interface](https://fivetran.com/docs/hvr6/user-interface).


> **Important:** 
The effects of **hvrrefresh** can be customized by defining various actions in the channel. For example, defining the action [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) with parameter [**RefreshCondition**](https://fivetran.com/docs/hvr6/action-reference/restrict#refreshcondition) allows the refresh of only certain rows in the table. Parameter **Context** can be used with option <b>-C</b> to allow restrictions to be enabled dynamically. Another form of customization is to employ SQL views; **Refresh** can read data from a view in the source database and row-wise refresh can also select from a view in the target database, rather than a real table when comparing the incoming changes.

If row-wise **hvrrefresh** is connecting between different DBMS types, then an ambiguity can occur because of certain data type coercions. For example, HVR coercion maps an empty string from other DBMS's into a **null** in an Oracle **varchar**. If Ingres location **ing** contains an empty string and Oracle location **ora** contains a null, then should HVR report that these tables are the same or different? Command **hvrrefresh** allow both behavior by applying the sensitivity of the 'write' location, not the 'read' location specified by option <b>-r</b>. This means that row-wise refreshing from location **ing** to location **ora** will report the tables were identical, but row-wise refreshing from **ora** to **ing** will say the tables were different.


## Options


This section describes the options available for command **hvrrefresh**.

 Parameter | Description |
 `**-a***max_slices_per_tbl*` | 
Set the number of slices the table will be divided into. The `default` number of slices is **1**, i.e., the table will be processed as a single piece. You can set the value to any integer.

This option cannot be combined with option `**-S**`.

In the User Interface, this option corresponds to the [Number of Slices](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#numberofslices) option.

> **Note:** 
This option is not supported since 6.3.0/0.

 |
 `**-A***rows_per_slice*` | 
Set the number of rows per slice.

The `default` number of rows per slice is **10000000** (ten million). Requires option `**-a**`.

In the User Interface, this option corresponds to the [Rows per slice](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#tuningpreferences) option.

> **Note:** 
This option is not supported since 6.3.0/0.

 |
 `**-b**` | Run in the background: do not wait for the **Refresh** to complete. |
 `**-B***slice_meths*` | 
Methods for slice suggestion (option `**-a**`).

Valid values for `*slice_meths*` are:

- **c**: Suggest from last compare row count. Inspects previous Compare events and tries to find the `Source_Rows_Selected` result for the current table. Then uses this value to suggest the slicing.
- **C**: Repeat the last compare slicing. Repeats slicing from the last Compare job.
- **r**: Suggest from last refresh row count. Inspects previous Refresh events and tries to find the `Source_Rows_Selected` result for the current table. Then uses this value to suggest the slicing.
- **R**: Repeat the last refresh slicing. Repeats slicing from the last Refresh job.
- **s**: Suggest from DBMS statistics. Gets the row count from the DBMS_STATS Oracle package


Several `**-B***slice_meths*` instructions can be supplied together, e.g., `**-BCs**`.


In the User Interface, this option corresponds to the [Slicing Suggestions](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#slicingsuggestions) dialog.

> **Note:** 
This option is not supported since 6.3.0/0.

 |
 
`**-c***createopts*`
 | 
Create new tables. Only 'basic' tables are created, based on the information in the channel. A basic table just has the correct column names and data types without any extra indexes, constraints, triggers, or table spaces.

Valid values for `*createopts*` are:

- 
**b**: Create basic (absent) tables only (mandatory).

- 
**e**: Keep the existing structure.

- 
**f**: Force recreation (always recreate) of tables.

- 
**k**: Create an index (unique key or non-unique index). If the original table does not have a unique key, then a non-unique index is created instead of a unique key.

- 
**o**: Only create tables, do not **Refresh** any data into them.

- 
**p**: Preserve (keep) existing data on recreating.

- 
**r**: Recreate (drop and create) if the column names do not match.



Several `**-c***createopts*` instructions can be supplied together, e.g. `**-cbkr**` which instructs **hvrrefresh** to create new tables in the target database if they do not already exist and re-create if they exist but have the wrong column information. However, if a table’s columns have the same names and data types and differ only in encoding, **hvrrefresh** does not re-create the table.

Action **[DbObjectGeneration](https://fivetran.com/docs/hvr6/action-reference/dbobjectgeneration)** with parameter **[RefreshTable**Create**Clause](https://fivetran.com/docs/hvr6/action-reference/dbobjectgeneration#refreshtablecreateclause)** can be used to add extra SQL to the **Create Table** statement which HVR will generate.

In the User Interface, this option corresponds to different target table creation [configurations](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#noinitialcreationoralteroftargettables) and [Advanced Table Creation Options](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#advancedtablecreationoptions). |
 
`**-C***context*`
 | 
Enable *context*.

This option controls whether actions defined with parameter **Context** are effective or are ignored. For more information, see the [Refresh and Compare Contexts](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts) concept page.

Defining an action with parameter **Context** can have different uses. For example, if action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** with parameters **[RefreshCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#refreshcondition)="{id}>22" [Context](https://fivetran.com/docs/hvr6/action-reference/restrict#context)=qqq** is defined, then normally all data will be refreshed, but if context **qqq** is enabled (**-Cqqq**), then only rows where **id>22** will be refreshed. Variables can also be used in the restrict condition, such as **"{id}>{hvr_var_min}"**. This means that **hvrrefresh -Cqqq -Vmin=99** will only **Refresh** rows with **id>99**.

Action **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** with parameter [**Context**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#context) can also be defined. This can be used to define [**CaptureExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression) parameters which are only activated if a certain context is supplied. For example, to define a **Bulk Refresh** context where SQL expressions are performed on the source database (which would slow down capture) instead of the target database (which would slow down **Bulk Refresh**).

In the User Interface, this option corresponds to the [Contexts](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#contexts) option. |
 `**-d**` | 
Remove (drop) scripts and scheduler jobs & job groups generated by the previous **hvrrefresh** command.

 |
 `**-D**` | Duplicate the last **Refresh** event. This option is used for repeating a **Refresh** operation, using the same arguments. Other command-line options supplied to `**hvrrefresh -D**` will overwrite those from the duplicated event. |
 `**-e**` | Automatically make a duplicate of the refresh event when it is done. |
 `**-E***time*` | 
Schedule time(s) *time* for the refresh job. Valid values for *time* are:

- *date_str_z*: run the refresh job at a specific time once. Valid time formats for *date_str_z* are:

- 
*YYYY-MM-DD [HH:MM:SS]* (in local time)

- 
*YYYY-MM-DD***T***HH:MM:SS+TZD*

- 
*YYYY-MM-DD***T***HH:MM:SSZ*

- 
**today**

- 
**now***[±SECS]*

- 
an integer (seconds since **1970-01-01 00:00:00 UTC**)



- *str*: a crono string, schedule the refresh job to run at specific times repeatedly.



Cannot be combined with option `**-e**`.

For specific usages, see [Examples](#example3schedulerefresh).

In the User Interface, this option corresponds to the [Scheduling Options](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#schedulingoptions). |
 `**-f**` | 
Fire database triggers/rules while applying SQL changes for **Refresh**.

Normally for Oracle and SQL Server, HVR disables any triggers on the target tables before the **Refresh** and re-enables them afterward. On Ingres, the **Refresh** avoids firing databases rules using statement `**set no rules**`. This option prevents this, so if **Refresh** does an `**insert**` statement then it could fire a trigger. But note that refresh often uses a bulk-load method to load data, in which case database triggers will not be fired anyway. Other ways to control trigger firing are described in [Managing Recapturing Using Session Names](https://fivetran.com/docs/hvr6/advanced-operations/managing-recapturing-using-session-names). For integration jobs into Ingres and SQL Server, action **[Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate)** with parameter **[NoTriggerFiring](https://fivetran.com/docs/hvr6/action-reference/integrate#notriggerfiring)** can also be used.

In the User Interface, this option corresponds to the [Disable Triggers](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#disabletriggers) option. |
 `**-F***fkops*` | 
Behavior for foreign key constraint in the target database which either reference or are referenced by a table which should be refreshed.

Valid values for `*fkops*` are:

- 
**i**: Ignore foreign key constraints. Normally this would cause foreign key constraint errors. This cannot be combined with other letters.

- **x**`default`: Disable all such constraints before **Refresh** and re-enable them at the end. If the DBMS does not support disable/re-enable syntax (e.g. Ingres) then constraints are instead dropped before **Refresh** and recreated at the end. Note that for online refresh (option `**-q**`) without a select moment supplied (option `**-M**`) the actual re-enabling of disabled foreign key constraints is not done by the **Refresh** itself but is instead delayed until the end of the next cycle of integration.


> **Important:** 
If option `**-F**` is not supplied, by default, all foreign-key constraints will be disabled before **Refresh** and re-enabled afterward unless HVR has no capability for foreign keys at all (value **i**).


Refreshing from a source location is supported only on certain location types. For the list of supported source location types, see section [Refresh and Compare](https://fivetran.com/docs/hvr6/capabilities/610#refreshandcompare) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).
 |
 `**-g***gran*`** | 
Granularity of refresh in database locations. For more information, see [Refresh Types](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh#refreshtypes).

Valid values for `*gran*` are:

- 
**b**`default`: Bulk refresh using bulk data load.

- 
**r**: Row-by-row refresh of tables.



In the User Interface, this option corresponds to the [Bulk Load](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity) and [Repair](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#repairrowbyrowgranularity) Granularity options. |
 `**-i***isolate_when*` | 
Define when to start isolation for table refresh. Isolated table refresh allows integrate jobs to continue for tables that are not part of the isolated refresh. The integrate jobs for the isolated tables will resume once the refresh is complete.

Valid values for `*isolate_when*` are:

- 
**now**: Start isolation immediately.

- 
**at_start**: Start isolation when the refresh starts. This is useful for scheduled refreshes that will not start immediately.


 |
 `**-I***srange*` | 
Refresh event only performs a subset of slices implied by `**-S**` (table slices) option.

This option is only allowed with option `**-S**`.

Value `*srange*` should be a comma-separated list of one of the following:

- *N*: Only perform 'sub slices' number *N*. Note that these slices are numbered starting from zero.
- *N-M*: Perform from slices from *N* to *M* inclusive.
- *N-*: Perform from slices from *N* onwards.
- *-M*: Perform from slices from the first slices until slice *M*.

 |
 `**-J***task*` | 
Job chaining. After the refresh job is completed, start the capture and/or integrate jobs.

Valid values for `*task*` are:

- **cap**: start capture job
- **integ**: start integrate job

 |
 
`**-l***loc*`
 | 
Target location to refresh to. This means that data will be written into location `*loc*`.

If this option is not supplied then all other locations except the source location are considered as target location(s).

Several `**-l***loc*` instructions can be supplied together.

> **Note:** 
The source (read location) is specified with option `**-r**`.


Valid values for `*loc*` are:

- 
*locname*: Only location *locname*.

- 
*l1***-***l2*: All locations that fall alphabetically between *l1* and *l2* inclusive.

- 
**!***locname*: All locations except *locname*.

- 
**!***l1*-*l2*: All locations except for those that fall alphabetically between *l1* and *l2* inclusive.

> **Important:** 
The character '**!**' can be treated as a special (reserved) character in certain shells. In such cases, use single quotes (' ') or a back slash (\) when specifying the location(s) to be excluded. For example, hvrrefresh -r mysrc -l '!myloc' myhub mychn or hvrrefresh -r mysrc -l \!myloc myhub mychn


- 
*pattern*: All locations matching the specified *pattern*. Pattern matching can be done using the special symbols *****, **?** or **[***characters***]**, where '*****' is any sequence of characters, '**?**' matches any character (exactly one), and '**[]**' matches a selection of characters. For example:

- '**loc***' matches location names starting with 'loc'.
- '***loc**' matches location names ending with 'loc'.
- '**loc?**' matches location names 'loc1', 'loc2', 'loc3', but not 'loc12'.
- '**a[c0-9]**' matches location names with the first letter 'a' and the second letter 'c' or a digit.
- '**a*|b***' Multiple patterns may be specified. In this case, the pattern matches location names starting with 'a' and 'b'.


- 
**@***filename*: All locations listed in file *filename* (a **.txt** file containing location names, one per line).



In the User Interface, this option corresponds to the [Locations](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#specifylocations) option. |
 **-m***mask*
`**Since** v6.2.5/6` | 
Mask (ignore) some differences between the tables that are being refreshed.

Valid values of *mask* can be:

- 
**d**: Skip deleting rows that are present in the target but not in the source.

- 
**i**: Skip inserting rows that are present in the source but not in the target.

- 
**u**: Skip updating rows where the primary key exists in both source and target, but non-key column values differ.



The values/letters can be combined, for example **-mid** means ignore inserts and deletes. If a difference is ignored, then the verbose option (**-v**) will not generate SQL for it and **hvrrefresh** will not rectify it. 

The **-m** option can only be used with row-wise granularity (option **-gr**). |
 
`**-M***select_moment*`
 | 
Select data from each table from the same consistent moment in time.

Valid values for `*select_moment*` are:

- 
*time*: Flashback query with `**select … as of timestamp**`.

Valid formats are *YYYY-MM-DD* [*HH***:***MM***:***SS*] (in local time) or *YYYY-MM-DDTHH:MM:SS+TZD* or *YYYY-MM-DDTHH:MM:SSZ* or **today** or now[[±]*SECS*] or an integer (seconds since **1970-01-01 00:00:00 UTC**). Note that if a symbolic time like `**-Mnow**` is supplied then a new "SCN time" will be retrieved each time the refresh job is run (not only when the **hvrrefresh** command is called). So if **hvrrefresh**`**-Mnow**` is run on Monday, and the refresh job it creates starts running at 10:00 Tuesday and runs again 10:00 on Wednesday, then the first refresh will do a flashback query (for all tables) with an SCN corresponding to Tuesday at 10:00 and the second job run will use flashback query with an SCN corresponding to Wednesday at 10:00.

- 
**scn**=*val*: Flashback query with `**select … as of scn**`. Value *val* is an Oracle SCN number, either in decimal or in hex (when it starts with **0x** or contains hex digits).

- 
**hvr_tx_seq**=*val*: Value from column **[hvr_tx_seq](https://fivetran.com/docs/hvr6/internal-objects/extra-columns-for-capture-fail-and-history-tables#hvrtxseq)** is converted back to an Oracle SCN number (by dividing by **65536**) and used for flashback query with `**select … as of scn**`. Value is either in decimal or in hex (when it starts with **0x** or contains hex digits).

- **snapshot****** (SQL Server only): Select data from a source database using SQL **snapshot** isolation level, which requires enabling **ALLOW_SNAPSHOT_ISOLATION** database option in SQL Server.


This parameter only affects the selects of the leftmost (source) database, not any selects on the rightmost (target) database.

In the User Interface, this option corresponds to the [Select moment with Oracle flashback query](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#oracleflashback)**** option. |
 `**-n**`
`**Since** v6.1.5/2` | 
Add the timekey truncate record as the first record of each table that is refreshed from the source location. This implies all previous timekey records for this table can be ignored by the system or application that consumes the data in the target location.

This option is only supported if the target is a file or Kafka location.

This option can only be used for tables with a [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey) column.

This option cannot be used in combination with option `**-g*r***` (row-by-row granularity).

In the User Interface, this option corresponds to the [Add a Truncate Record Before First Rows](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#addatruncaterecordbeforefirstrows) option.

 |

 `**-p***job_quota*` | Sets **job_quota** refresh job group attribute. It defines a number of jobs `*jobs_quota *`which can be run simultaneously. |
 
`**-P***parallel_sessions*`
 | 
Perform **Refresh** for different tables in parallel using `*parallel_sessions*` sub-processes. The refresh will start by processing `*parallel_sessions*` tables in parallel; when the first of these is finished the next table will be processed, and so on.

In the User Interface, this option corresponds to the [Parallel Sessions](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#parallelsessions) option. |
 `**-q***purge*` | 
Online refresh of data from a database that is continuously being changed. This requires that capture is enabled on the source database. The integration jobs are automatically suspended while the online refresh is running, and restarted afterward. The target database is not yet consistent after the online refresh has finished. Instead, it leaves instructions so that when the replication jobs are restarted, they skip all changes that occurred before the refresh and perform special handling for changes that occurred during the refresh. This means that after the next replication cycle consistency is restored in the target database. If the target database had foreign key constraints, then these will also be restored.

Valid values for `*purge*` are:

- 
**wo**:

Write only. Changes before the online refresh should only be skipped on the write side (by the integrate job), not on the read side (by the capture job). If changes are being replicated from the read location to multiple targets, then this value will avoid skipping changes that are still needed by the other targets.

- 
**rw**:

Read/Write. Changes before the online refresh should be skipped both on the read side (by the capture job) and on the write side (by the integrate job). There are two advantages to skipping changes on the capture side; performance (those changes will not be sent over the network) and avoiding some replication errors (i.e. those caused by an alter table statement). The disadvantage of skipping changes on the capture side is that these changes may be needed by other replication targets. If they were needed, then these other integration locations need a new 'online' refresh, but without `**-qrw**`, otherwise, the original targets will need yet another refresh.

- 
**no**:

No skipping. Changes that occurred before the refresh are not skipped, only special handling is activated for changes that occurred during the refresh. This is useful for the online refresh of a context-sensitive restriction of data ([**hvrrefersh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh)`**-C***context*` and action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** with parameters **[RefreshCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#refreshcondition)** and **[Context](https://fivetran.com/docs/hvr6/action-reference/restrict#context)**).



Internally, the online refresh uses 'control files' to send instructions to other replication jobs (see command [**hvrcontrol**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcontrol)). These files can be viewed using command [**hvrrouterview**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrouterview) with option `**-s**`.

Online refresh (with option `**-q**`) can give errors if duplicate rows are actually changed during the online refresh (see parameter **[NoDuplicateRows](https://fivetran.com/docs/hvr6/action-reference/tableproperties#noduplicaterows)** in action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties)).

In the User Interface, this option corresponds to the [Online refresh controls to affect replication of changes that occurred before and during refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#resilientintegration)**** option. |
 
`**-r***loc*`
 | 
Source location to refresh from. This means that data will be read from location `*loc*` and written to the other location(s).

In the User Interface, this option corresponds to the [Locations](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#specifylocations) option. |
 
`**-R***url*`



 | 
Remote hub server. Access the hub server running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

This option is required for [remote CLI access](https://fivetran.com/docs/hvr6/command-line-interface). When using this option, command **[hvrlogin](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)** should be run first, for authentication.
 |
 `**-s**` | 
Schedule invocation of a refresh script by leaving a refresh job in the **SUSPEND** state. Without this option, the `default` behavior is to start the refresh job immediately.

The refresh job can be invoked using the [**hvrstart**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrstart) command. For example, executing the command `hvrstart -u -w *hub channel*-refr-*src-tgt*` unsuspends (moves to **RUNNING** state) the jobs and instructs the scheduler to run them. Output from the jobs is copied to the [**hvrstart**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrstart) command's **stdout** and the command finishes when all jobs have finished. Jobs created are cyclic which means that after they have run they go back to the **PENDING** state again. They are not generated by a **trig_delay** attribute which means that once they are complete they will stay in the **PENDING** state without getting retriggered. |
 `**-S***sliceexpr*`
 | 
Refresh large tables using **[Slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing)**. Value `*sliceexpr*` can be used to split the table into multiple slices.

The column used to slice a table must be 'stable', i.e., values in it should not change while the job is running. For example, **customer_id** is a stable column, while **last_login** is not. Otherwise, a row could 'move' from one slice to another while the job is running. As a result, the row could be processed in two slices (causing errors) or no slices (causing data loss). If the source database is Oracle, this problem can be avoided using a common select moment (option `**-M**`).

In the User Interface, this option corresponds to the **[Slicing](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#slicing)** section.

For more information on slicing limitations, see [Slicing Limitations](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#slicinglimitations).

Value *`sliceexpr`* must have one of the following forms:

- *col%num*
More details
In this slicing method (**[Modulo Slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#moduloslicing)**), HVR groups the data set by performing a modulo operation using the values from the column (e.g. **mycol** of your choice.

If **-Smycol%3** is supplied then the conditions for the three slices are:
`mod(round(abs(coalesce(mycol, 0)), 0), 3)= 0
mod(round(abs(coalesce(mycol, 0)), 0), 3)= 1
mod(round(abs(coalesce(mycol, 0)), 0), 3)= 2`
Note that the use of extra SQL functions (e.g. **round()**, **abs()** and **coalesce()**) ensure that slicing effect fractions, negative numbers and NULL too. Modulo slicing can only be used on a column with a numeric data type.

> **Important:** 
For **[Modulo slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#moduloslicing)**, parameters **[SliceCountCondition](http://Restrict#SliceCountCondition)** and **[SliceSeriesCondition](http://Restrict#SliceSeriesCondition)** in action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** **must not** be defined.


- *col<b1[<b2]… [<bN]*
More details
In this slicing method (**[Boundary Slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#boundaryslicing)**), HVR groups the data set depending on the boundaries defined for the chosen column (e.g. **mycol**).

If *N* boundaries are defined then *N+1* slices are implied.

If **-Smycol<10<20<30** is supplied then the conditions for the four slices are:
`mycol <= 10 mycol > 10 and 
mycol <= 20 mycol > 20 and
mycol <= 30 mycol > 30 or 
mycol is null`
> **Tip:** 
Strings can be supplied by adding quotes around boundaries, **-Smycol<'x'<'y'<'z'**.


For very large tables consider the DBMS query execution plan. If the DBMS decides to 'walk' an index (with a lookup for each matched row) but this is not optimal (i.e. a 'serial-scan' of the table would be faster) then either use DBMS techniques (**$HVR_SQL_SELECT_HINT** allows Oracle optimizer hints) or consider modulo slicing (*col%num*) instead.

Gathering column histogram statistics is required for this functionality to work. This can be done by calling the **[dbms_stats.gather_table_stats](https://docs.oracle.com/database/121/ARPLS/d_stats.htm#ARPLS68582)** stored procedure.
Examples
- 
Gathers statistics including column histograms, for table 'table_name', using all table rows, for all columns, and a maximum of 254 histogram buckets (therefore up to 254 slice boundaries can be suggested).
`exec dbms_stats.gather_table_stats('schema_name', 'table_name', estimate_percent=>100, method_opt=>'for all columns size 254');`
- 
Gathers statistics including column histograms, for table 'table_name', using all table rows, for all indexed columns, and default number of histogram buckets.
`exec dbms_stats.gather_table_stats('schema_name', 'table_name', estimate_percent=>100, method_opt=>'for all indexed columns');`
- 
Gathers statistics including column histograms, for table 'table_name', using 70% of table rows, for column 'table_column', and a maximum of 150 histogram buckets (therefore up to 150 slice boundaries can be suggested).
`exec dbms_stats.gather_table_stats('schema_name', 'table_name', estimate_percent=>70, method_opt=>'for columns table_column size 150');`
- 
Gathers statistics including column histograms, for table 'table_name', for all columns, and maximum of 254 histogram buckets. This is an obsolete way to generate statistics and there are much fewer options supported.
`analyze table table_name compute statistics for all columns size 254;`


> **Important:** 
For **[Boundary slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#boundaryslicing)**, parameters **[SliceCountCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#slicecountcondition)** and **[SliceSeriesCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#sliceseriescondition)** in action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)****must not** be defined.


- *num*
More details
In this slicing method (**[Count slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#countslicing)**), HVR groups the data set by performing a modulo operation on any column, including the ones with string or date values.

The number of each slice is assigned to substitution **{hvr_slice_num}** which must be mentioned in action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** with parameter **[SliceCountCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#slicecountcondition)** defined for the slice table. Substitution **{hvr_slice_total}** is also assigned to the total number of slices.

- *val1*[*;val2*]…
More details
In this slicing method (**[Series Slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#seriesslicing)**), HVR groups the data set based on a particular value, mostly with distinct data groups.

Each slice has its value assigned directly into substitution **{hvr_slice_value}** must be mentioned in action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** with parameter [**SliceSeriesCondition**](https://fivetran.com/docs/hvr6/action-reference/restrict#sliceseriescondition) defined for the sliced table.


> **Tip:** 
In all of the above slicing methods, the slice expression can be prefixed with a table name specifier `*table***.***sliceexpr*` to apply slicing only to a specific table. The specified table must be in scope of this refresh operation. For example, the expression `mytable.mycol%5` applies modulo slicing to column **mycol** of table **mytable**.

If you are specifying distinct slice expression for multiple tables then option **-S** must be supplied for each table specification (e.g. `-S mytable1.mycol%10 -S mytable2.mycol%5`).


 |
 
`**-t***tbl*`
 | 
Only refresh the specified table(s) `*tbl*`.

Several `**-t***tbl*` instructions can be supplied together.

Valid values for `*tbl*` are:

- 
*tblname*: Only refresh table *tblname*.

- 
*t1***-***t2*: Refresh all table codes that fall alphabetically between *t1* and *t2* inclusive.

- 
**!***tblname*: Refresh all table names except *tblname*.

- 
**!***t1***-***t2*: Refresh all table codes except for those that fall alphabetically between *t1* and *t2* inclusive.

> **Important:** 
The character '**!**' can be treated as a special (reserved) character in certain shells. In such cases, use single quotes (' ') or a back slash (\) when specifying the location(s) to be excluded. For example, hvrrefresh -r mysrc -t '!myloc' myhub mychn or hvrrefresh -r mysrc -t \!myloc myhub mychn


- 
*pattern*: Refresh all tables matching the specified *pattern*. Pattern matching can be done using the special symbols *****, **?** or **[***characters***]**, where '*****' is any sequence of characters, '**?**' matches any character (exactly one), and '**[]**' matches a selection of characters. For example:

- '**tbl***' matches table names starting with 'tbl'.
- '***tbl**' matches table names ending with 'tbl'.
- '**tbl?**' matches table names 'tbl1', 'tbl2', 'tbl3', but not 'tbl12'.
- '**a[c0-9]**' matches table names with the first letter 'a' and the second letter 'c' or a digit.
- '**a*|b***' Multiple patterns may be specified. In this case, the pattern matches table names starting with 'a' and 'b'.


- **@***filename:* Refresh all tables listed in *filename* (a .txt file containing location names, one per line)*.*


In the User Interface, this option corresponds to the [Tables](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#onlyspecifictables) option. |
 `**-T***tsk*` | 
Specify an alternative name for a refresh task to be used for naming scripts and jobs. The task name must begin with an 'r'.

The`default` task name is **refr**, so without this option, the **Refresh** jobs and scripts are named *chn-***refr***-l1-l2*. |
 `**-u**`
`**Since** v6.1.5/2` | 
Perform upsert refresh. This option merges the source rows into the target without initially deleting or truncating the target rows. Similar to [**Burst Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), the data is initially loaded into burst tables named *tbl***_ _rb** and then the burst table is merged with the base table. Changes are applied as inserts or updates, similar to [**Resilient Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#resilient).

> **Important:** 
Deletes or key updates are not covered by this type of refresh. Rows that are deleted on the source will still exist in the target. Rows for which the key has been updated in the source will exist with both the old and new key in the target.


This option is only supported for target locations that support the [**Burst integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method)method.

This option cannot be used for tables with a [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey) column.

This option cannot be used in combination with option `**-g*r***` (row-by-row granularity).

In the User Interface, this option corresponds to the [Merge into Target (No Delete/Truncate on Target)](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#mergeintotarget) option.

 |
 `**-v**` | 
Verbose. This option creates binary diff files containing individual differences detected.

The diff files can be viewed using command [**hvrrouterview**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrouterview). Section [Analyzing Diff File](https://fivetran.com/docs/hvr6/advanced-operations/analyzing-diff-file) explains how to view and interpret the contents of a diff file.

This option must be used in combination with option `**-g*r***` (row-by-row granularity).

In the User Interface, this option corresponds to the [Keep Difference Files](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#keepdifffiles) option. |
 
`**-V***name=value*`
 | 
Supply variable for refresh restrict condition.

This should be supplied if a [**RefreshCondition**](https://fivetran.com/docs/hvr6/action-reference/restrict#refreshcondition) parameter of action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** contains string **{hvr_var_***name***}**. This string is replaced with `*value*`.In the User Interface, this option corresponds to the [Variables](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#variables) option. |
 `**-w***prereads*` | File prereaders per table. Define the number of prereader subtasks per table while performing [direct file compare](#directfilecompare). This option is only allowed if the source or target is a file location.
 |


## Examples


This section provides examples of using the **hvrrefresh** command.

##### Example 1. Bulk refresh


The following command can be used for bulk refresh of table **order** from location **src** to location **tgt**:
hvrrefresh -r src -l tgt -t order myhub mychannel

##### Example 2. Row-by-row refresh


For row-by-row refresh (option <b>-gr</b>) from location **src** to location **tgt**, use the following command:
hvrrefresh -r src -l tgt -gr myhub mychannel

##### Example 3. Schedule refresh


- 
The following command is to schedule a bulk refresh at a specific time (option -E).
hvrrefresh -r src -l tgt -gb -E 2022-04-12T12:50:53+0300 myhub mychannel

- 
The following command schedules a row-by-row refresh to repeat at the 1st day of each month at 10.30 a.m. (option -E).
hvrrefresh -r src -l tgt -gr -E '30 10 1 * *' myhub mychannel



##### Example 4. Isolate Bulk refresh


The following command can be used for isolate bulk refresh of table **order** from location **src** to location **tgt**:
hvrrefresh -i now -r src -l tgt -t order myhub mychannel

##### Example 5. Scheduled Isolate refresh


The following command is to schedule an isolate bulk refresh at a specific time:
hvrrefresh -i at_start -r src -l tgt -t order -gb -E 2022-04-12T12:50:53+0300 myhub mychannel

  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
