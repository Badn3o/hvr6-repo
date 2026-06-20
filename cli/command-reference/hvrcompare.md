# hvrcompare - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvrcompare/index.md)

# hvrcompare


## Usage


<b>hvrcompare</b> [<b>-R</b><em>url</em>] <b>-r</b><em>loc</em> [<b>-l</b><em>loc</em>]... [<em>-options</em>]... <em>hub chn</em>

## Description


Command **hvrcompare** allows you to compare data in two or more locations in a channel <em>chn</em>. It supports comparing both database and file locations. For more information, see the [Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) concept page.

> **Note:** 
Command **hvrcompare** corresponds to the [**Compare Data**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) dialog in the [User Interface](https://fivetran.com/docs/hvr6/user-interface).


## Options


This section describes the options available for command **hvrcompare**.

 Parameter | Description |
 `**-a***max_slices_per_tbl*` | 
Set the number of slices the table will be divided into. The `default` number of slices is **1**, i.e., the table will be processed as a single piece. You can set the value to any integer.

This option cannot be combined with option `**-S**`.

In the User Interface, this option corresponds to the **[Number of slices](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#numberofslices)** option.

> **Note:** 
This option is not supported since 6.3.0/0.

 |
 `**-A***rows_per_slice*` | 
Set the number of rows per slice.

The `default` number of rows per slice is **10000000** (ten million). Requires option `**-a**`.

In the User Interface, this option corresponds to the **[Tuning Preferences](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#tuningpreferences)** option.

> **Note:** 
This option is not supported since 6.3.0/0.

 |
 `**-b**` | Run compare job in background: do not wait for the compare to complete. |
 `**-B***slice_meths*` | 
Methods for slice suggestion (option `**-a**`).

Valid values for `*slice_meths*` are:

- **c**: Suggest from last compare row count. Inspects previous Compare events and tries to find the `Source_Rows_Selected` result for the current table. Then uses this value to suggest the slicing.
- **C**: Repeat the last compare slicing. Repeats slicing from the last Compare job.
- **r**: Suggest from last refresh row count. Inspects previous Refresh events and tries to find the `Source_Rows_Selected` result for the current table. Then uses this value to suggest the slicing.
- **R**: Repeat the last refresh slicing. Repeats slicing from the last Refresh job.
- **s**: Suggest from DBMS statistics. Gets the row count from the DBMS_STATS Oracle package


Several `**-B***slice_meths*` instructions can be supplied together, e.g., `**-BCs**`.


In the User Interface, this option corresponds to the **[Slicing Suggestions](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#slicingsuggestions)** dialog.

> **Note:** 
This option is not supported since 6.3.0/0.

 |
 `**-C***context*`*
* | 
Enable *context*.

This controls whether actions defined with parameter **Context** are effective or are ignored. For more information, see the [Refresh and Compare Contexts](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts) concept page.

Defining an action with **Context** can have different uses. For example, if action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** with parameters **[CompareCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#comparecondition)**=**"{id}>22"** and **[Context](https://fivetran.com/docs/hvr6/action-reference/restrict#context)**=**qqq** is defined, then normally all data will be compared, but if context **qqq** is enabled (`**-Cqqq**`), then only rows where **id>22** will be compared. Variables can also be used in the restrict condition, such as **"{id}>{hvr_var_min}"**. This means that `**hvrcompare -Cqqq -Vmin**=**99**` will compare only rows with **id>99**. To [supply variables for restrict condition](#supplyvariable) use option `**-V**`.

Action **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** can also be defined with parameter [**Context**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#context) on both source and target. This way, the parameter **[CaptureExpression](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression)** will only be activated if a certain context is supplied.

In the User Interface, this option corresponds to the [**Contexts**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#contexts) option.
 |
 `**-D**`
 | Duplicate the last compare event. This option is used for repeating a compare operation, using the same arguments. Other command-line options supplied to `**hvrcompare -D**` will overwrite those from the duplicated event. |
 `**-d**` | Remove (drop) scripts, scheduler jobs, and job groups generated by previous **hvrcompare** command. |
 `**-e**` | Automatically make a duplicate of the compare event when it is done. |
 `**-E***time*` | 
Schedule time(s) *time* for the compare job. Valid values for *time* are:

- *date_str_z*: run the compare job at a specific time once. Valid time formats for *date_str_z* are:

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



- *str*: a crono string, schedule the compare job to run at specific times repeatedly.


Cannot be combined with option `**-e**`.

For specific usages, see [Examples](#example3schedulecompare).

In the User Interface, this option corresponds to the **[Scheduling Options](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#schedulingoptions)** option. |
 `**-g***x*`** | 
Granularity of compare operation in database locations. For more information, see [Compare Types](https://fivetran.com/docs/hvr6/getting-started/concepts/compare#comparetypes).

Valid values of `*x*` are:

- **b**`default`: Bulk compare using checksums.
- **r**: Row-by-row compare of tables.


In the User Interface, this option corresponds to the **[Table Checksums Only](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#tablechecksumsonly)** option. |
 `**-G**` | Only count rows, do not compare data. |
 `**-i***x*`*
* | 
Retain and reuse intermediate files. This option allows you to retain the intermediate files that are generated during direct file compare. It also allows you to reuse the retained intermediate files that were generated earlier by a similar compare. A compare is similar if the location, channel, tables, and action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** with parameter **[SliceCountCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#slicecountcondition)** (if any) are identical.

This option is applicable only for [direct file compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare#directfilecompare).


Valid values of `*x*` are:

- 
**k**: Keep/retain intermediate files generated during this compare.

- 
**r**: Reuse the retained intermediate files that were generated earlier by a similar compare and after the compare operation is completed, the reused intermediate files and the intermediate files generated during this compare are deleted.

- 
**kr**: Reuse retained intermediate files and retain the intermediate files generated during this compare.


 |
 `**-I***srange*`*
* | 
Compare event only perform a subset of slices implied by `**-S**` (table slices) option.

This option is only allowed with option `**-S**`.

Value `*srange*` should be a comma-separated list of one of the following:

- *N*: Only perform 'sub slices' number *N*. Note that these slices are numbered starting from zero.
- *N-M*: Perform from slices from *N* to *M* inclusive.
- *N-*: Perform from slices from *N* onwards.
- *-M*: Perform from slices from the first slices until slice *M*.


In the User Interface, this option corresponds to the **[Slice Selection](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#sliceselection)** option in the **Table Slicing** dialog. |
 `**-l***x*` | 
Target location of compare. The other (read location) is specified with option `**-r**`. If this option is not supplied then all locations except the read location are targets.

Values of `*x*` maybe one of the following:

- *loc*: Only location *loc*.
- *l1***-***l2*: All locations that fall alphabetically between *l1* and *l2* inclusive.
- **!***loc*: All locations except *loc*.
- 
**!***l1***-***l2*: All locations except for those that fall alphabetically between *l1* and *l2* inclusive.

> **Important:** 
The character '**!**' can be treated as a special (reserved) character in certain shells. In such cases, use single quotes (' ') or a back slash (\) when specifying the location(s) to be excluded. For example, hvrcompare -r mysrc -l '!myloc' myhub mychn or hvrcompare -r mysrc -l \!myloc myhub mychn


- 
*pattern*: All locations matching the specified *pattern*. Pattern matching can be done using the special symbols *****, **?** or **[***characters***]**, where '*****' is any sequence of characters, '**?**' matches any character (exactly one), and '**[]**' matches a selection of characters. For example:

- '**loc***' matches location names starting with 'loc'.
- '***loc**' matches location names ending with 'loc'.
- '**loc?**' matches location names 'loc1', 'loc2', 'loc3', but not 'loc12'.
- '**a[c0-9]**' matches location names with first letter 'a' and second letter 'c' or a digit.
- '**a*|b***' Multiple patterns may be specified. In this case, the pattern matches location names starting with 'a' and 'b'.


- **@***filename:* All locations listed in *filename* (a .txt file containing location names, one per line).


Several `**-l***x*` instructions can be supplied together.

In the User Interface, this option corresponds to the **[Locations](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#specifylocations)** option. |
 **-m***mask*
`**Since** v6.2.5/6` | 
Mask (ignore) some differences between the tables that are being compared.

Valid values of *mask* can be:

- **d**: Ignore rows that are present in the target but not in the source.
- **i**: Ignore rows that are present in the source but not in the target.
- **u**: Ignore rows where the primary key matches in both source and target, but non-key column values differ.


The values/letters can be combined, for example **-mid** means ignore inserts and deletes. If a difference is ignored, then the verbose option (**-v**) will not generate SQL for it. 

The **-m** option can only be used with row-wise granularity (option **-gr**). |
 `**-M***moment*` | 
Select data from each table of a source from the same consistent *moment* in time.

Value *moment* can be one of the following:

- *time*: Flashback query with **select … as of timestamp**. Valid formats are *YYYY-MM-DD [HH:MM:SS]* (in local time) or *YYYY-MM-DDTHH:MM:SS+TZD* or *YYYY-MM-DDTHH:MM:SS*Z or **today** or **now**[[+|-]*SECS*] or an integer (seconds since **1970-01-01 00:00:00 UTC**). Note that if a symbolic time like `**-Mnow**` is supplied then a new "SCN time" will be retrieved each time the compare job is run (not only when the **hvrcompare** command is called. So if `**hvrcompare****-Mnow**` is run on Monday, and the compare job it creates starts running at 10:00 Tuesday and runs again 10:00 on Wednesday, then the first compare will do a flashback query (for all tables) with an SCN corresponding to Tuesday at 10:00 and the second job run will use flashback query with an SCN corresponding to Wednesday at 10:00.

- **scn**=*val*: Flashback query with **select … as of scn**. Value is an Oracle SCN number, either in decimal or in hex (when it starts with **0x** or contains hex digits).

- **hvr_tx_seq**=*val*: Value from column **hvr_tx_seq** is converted back to an Oracle SCN number (by dividing by **65536**) and used for flashback query with **select … as of scn**. Value is either in decimal or in hex (when it starts with **0x** or contains hex digits).


In the User Interface, this option corresponds to the **Compare Oracle Flashback Moment of Source with Time-Restricted View of Target** option in the **[Online Compare](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#onlinecompare)** section. |
 `**-N***secs*`*
* | 
Compare tables twice with a `*secs*` (seconds) delay in between. In CLI, this option can only be used along with option `**-o diff_diff**`. **[Capture](https://fivetran.com/docs/hvr6/action-reference/capture)** and **[Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate)** jobs are not required for performing this mode of online compare.

This online compare mode is similar to option `**-o**``**diff_diff**` (compare tables twice with a **Capture** and **Integrate** flush in between), however, with one difference. HVR performs a regular compare which produces a result (also known as diff). HVR then waits for *secs* seconds after which it again performs the regular compare which produces a second result (diff). The compare results generated in the first and second compare are combined to produce a final compare result. For example, `hvrcompare -gr -o diff_diff -N 5 -r src -l tgt mychannel`

In the User Interface, this option corresponds to the **Do Compare Twice and Report Only Differences which Occur Twice** option in the **[Online Compare](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#onlinecompare)** section.
 |
 
`**-o***mode*`


 | 
Online compare. Performs live compare between locations where data is rapidly changing. This option can only be used if option `**-gr**` (row by row granularity) is supplied.

The results of online compare are displayed in [Events](https://fivetran.com/docs/hvr6/user-interface/events).


Value `*mode*` can be either:

- 
**diff_cap**:

Compare tables once and combine differences with captured transactions. Performs a regular compare which produces a result (also known as **diff**). This result (**diff**) is compared with the transaction files (which are continuously created by the **Capture** job) to identify and remove the pending transaction from the result (**diff**) for producing the final compare result. This compare mode is supported for comparing databases and files.

- 
**diff_diff**:

Compare tables twice with a **Capture** and **Integrate** flush in between. Performs a regular compare which produces a result (also known as **diff**). HVR then waits for the completion of the full **Capture** and **Integrate** cycle after which it again performs the regular compare which produces a second result (**diff**). The compare results generated in the first and second compare operations are combined to produce a final compare result. This compare mode is only supported for comparing databases.

> **Important:** 
If option `**-N***secs*` (compare tables twice with a delay in between) is supplied with **diff_diff**), HVR waits for a fixed amount of time (seconds) defined, instead of waiting for the completion of **Capture** and **Integrate** cycle in between compares. For more information, see option `**-N***secs*` above. **[Capture](https://fivetran.com/docs/hvr6/action-reference/capture)** and **[Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate)** jobs are not required for performing this mode of online compare.


> **Important:** 
If a running **diff_cap** online compare job is suspended, HVR will continue to accumulate **tx** files with each capture cycle, which will lead to higher disk space usage.




In the User Interface, this option corresponds to the **Combine Initial Differences with Changes Captured while Compare is Running** option in the **[Online Compare](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#onlinecompare)** section. |
 `**-p***num_jobs*` | Set **job_quota** compare job group attribute. It defines a number of jobs `*num_jobs*` that can be run simultaneously. |
 `**-P***M*` | 
Parallelism for sessions. Perform compare for different tables in parallel using `*M*` sub-processes. The job will start processing `*M*` tables in parallel; when the first of these is finished the next table will be processed, and so on.

In the User Interface, use the **[Parallel Sessions](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#parallelsessions)** option to perform compare for different tables in parallel. |
 `**-r***loc*` | Read location. This means that location `*loc*` is passive; the data is piped from here to the other location(s) and the work of comparing the data is performed there instead. |
 
`**-R***url*`
 | 
Remote hub server. Access the hub server running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

This option is required for [remote CLI access](https://fivetran.com/docs/hvr6/command-line-interface). When using this option, command **[hvrlogin](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)** should be run first, for authentication.

In the User Interface, use the **[Parallel Sessions](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#parallelsessions)** option to perform compare for different tables in parallel. |
 `**-s**` | 
Schedule invocation of a compare script by leaving a compare job in the **SUSPEND** state. Without this option, the `default` behavior is to start the compare job immediately.

The compare job can be invoked using the [**hvrstart**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrstart) command. For example, executing the command `hvrstart -u -w *hub channel*-cmp-*src-tgt*` unsuspends (moves to **RUNNING** state) the jobs and instructs the scheduler to run them. The output from the jobs is copied to the **[Hvrstart](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrstart)** command's **stdout** and the command finishes when all jobs have finished. Jobs created are cyclic which means that after they have run they go back to the **PENDING** state again. They are not generated by a **trig_delay** attribute which means that once they are complete they will stay in the **PENDING** state without getting retriggered. |
 
`**-S***sliceexpr*`

 | 
Compare large tables using **[Slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing)**. Value `*sliceexpr*` can be used to split the table into multiple slices.

The compare job is named *channel-***cmp***-location1-location2* (the task name **cmp** can be overridden using option `**-T**`).

The column used to slice a table must be 'stable', i.e., values in it should not change while the job is running. For example, **customer_id** is a stable column, while **last_login** is not. Otherwise, a row could 'move' from one slice to another while the job is running. As a result, the row could be processed in two slices (causing errors) or no slices (causing data loss). If the source database is Oracle, this problem can be avoided using a common select moment (option `**-M**`).

For more information on slicing limitations, see [Slicing Limitations](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#slicinglimitations).

In the User Interface, this option corresponds to the **[Slicing](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#slicing)** section.

Value *`sliceexpr`* must have one of the following forms:

- *col%num*
More details
In this slicing method (**[Modulo Slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing#moduloslicing)**), HVR groups the data set by performing a modulo operation using the values from the column (e.g. **mycol**) of your choice.

If **-Smycol%3** is supplied then the conditions for the three slices are:
`mod(round(abs(coalesce(mycol, 0)), 0), 3)= 0
mod(round(abs(coalesce(mycol, 0)), 0), 3)= 1
mod(round(abs(coalesce(mycol, 0)), 0), 3)= 2`
Note that the use of extra SQL functions (e.g. **round()**, **abs()** and **coalesce()**) ensure that slicing affect fractions, negative numbers and NULL too.

Modulo slicing can only be used on a column with a numeric data type.

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
Gathers statistics including column histograms, for table 'table_name', using 70% of table rows, for column 'table_column', and maximum of 150 histogram buckets (therefore up to 150 slice boundaries can be suggested).
`exec dbms_stats.gather_table_stats('schema_name', 'table_name', estimate_percent=>70, method_opt=>'for columns table_column size 150');`
- 
Gathers statistics including column histograms, for table 'table_name', for all columns, and maximum 254 histogram buckets. This is an obsolete way to generate statistics and there are much less options supported.
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
 `**-t***tbl*` | 
Only compare tables specified by `*tbl*`.

Values of `*tbl*` may be one of the following:

- *table*: Compare only the table with name *table*.
- *t1***-***t2*: Compare all tables that fall alphabetically between *t1* and *t2* inclusive.
- **!***table*: Compare all tables except *table*.
- 
**!***t1***-***t2*: Compare all tables except for those that fall alphabetically between *t1* and *t2* inclusive.

> **Important:** 
The character '**!**' can be treated as a special (reserved) character in certain shells. In such cases, use single quotes (' ') or a back slash (\) when specifying the location(s) to be excluded. For example, hvrcompare -r mysrc -t '!tbl' myhub mychn or hvrcompare -r mysrc -t \!tbl myhub mychn


- 
*pattern*: Compare all tables matching the specified *pattern*. Pattern matching can be done using the special symbols *****, **?** or **[***characters***]**, where '*****' is any sequence of characters, '**?**' matches any character (exactly one), and '**[]**' matches a selection of characters. For example:

- '**tbl***' matches table names starting with 'tbl'.
- '***tbl**' matches table names ending with 'tbl'.
- '**tbl?**' matches table names 'tbl1', 'tbl2', 'tbl3', but not 'tbl12'.
- '**a[c0-9]**' matches table names with first letter 'a' and second letter 'c' or a digit.
- '**a*|b***' Multiple patterns may be specified. In this case, the pattern matches table names starting with 'a' and 'b'.


- **@***filename:* Compare all tables listed in *filename* (a .txt file containing location names, one per line)*.*


Several `**-t***tbl*` instructions can be supplied together.

In the User Interface, this option corresponds to the **[Tables](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#onlyspecifictables)** option. |
 `**-T***tsk*` | 
Specify an alternative name for a compare task to be used for naming scripts and jobs. The task name must start with a 'c'.

When this option is not defined, the `default` task name is **cmp**, so the compare jobs are named *chn*-**cmp**-*l1*-*l2*. |
 `**-v**`**** | 
Verbose. This option creates binary diff files containing individual differences detected.

The diff files can be viewed using command [**hvrrouterview**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrouterview). Section [Analyzing Diff File](https://fivetran.com/docs/hvr6/advanced-operations/analyzing-diff-file) explains how to view and interpret the contents of a diff file.

This option must be used in combination with option `**-g*r***` (row-by-row granularity). |
 `**-V***nm=val*`*
* | Supply variable for a restrict condition. This should be supplied if parameter **[CompareCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#comparecondition)** in action [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) contains string **{hvr_var_***name***}**. This string is replaced with `*val*`. |
 `**-w***prereads*`
 | File prereaders per table. Define the number of prereader subtasks per table while performing [direct file compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare#directfilecompare). This option is only allowed if the source or target is a file location.
 |


## Examples


This section provides examples of using the **hvrcompare** command.

> **Note:** 
By default, HVR performs bulk compare. It is not required to explicitly define option <b>-g</b><em>b</em>.


##### Example 1. Compare tables


The following command compares all tables in locations **src** and **tgt**:
 hvrcompare -r src -l tgt myhub mychannel

##### Example 2. Compare specific table


The following command compare table **order** (option **-t**) in location **src** and location **tgt**:
hvrcompare -r src -l tgt -t order myhub mychannel

##### Example 3. Schedule compare


The following command is to schedule compare to run at a specific time (option **-E**).
hvrcompare -r src -l tgt -E now+1h myhub mychannel

The following command is to schedule compare to run at the 1st day of each month at 10.30 a.m. (option **-E**).
hvrcompare -r src -l tgt -E '30 10 1 * *' myhub mychannel

  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
