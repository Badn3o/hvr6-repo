# Comparing Data - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/user-interface/channels/comparing-data/index.md)

# Comparing Data


Option **Compare Data** allows you to compare data in two or more locations in a channel. It supports comparing both database and file locations. For more information, see the [Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) concept page.

> **Note:** 
Option **Compare Data** is equivalent to the [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare) CLI command.


This option is available on the following pages:

- [**Channel Details**](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details): the **Compare Data** button at the top right of the page.
- [**Locations**](https://fivetran.com/docs/hvr6/user-interface/locations): the **Compare Data** option under the **More Options** menu  at the top right of a page.
- [**Location Details**](https://fivetran.com/docs/hvr6/user-interface/locations/location-details): the **Compare Data** option under the **More Options** menu  related to each channel in the **Channel Membership** pane.
- [**Tables**](https://fivetran.com/docs/hvr6/user-interface/tables): the **Compare Data** option under the **More Options** menu  at the top right of a page.
- [**Table Details**](https://fivetran.com/docs/hvr6/user-interface/tables/table-details): the **Compare Data** option under the **More Options** menu  at the top right of a page.
- [**Event Details**](https://fivetran.com/docs/hvr6/user-interface/events/event-details): (related to a compare event): the **Repeat Compare** button at the to right of the page.
- [**Jobs**](https://fivetran.com/docs/hvr6/user-interface/jobs): the **New Compare** option under the **More Options** menu  related to a compare job.


> **Important:** 
The **Compare Data** option may appear disabled in certain cases, for example, on the **Channel Details** page, if no locations are added to a channel. On the **Tables** page, you need to select one or more tables to enable the option, etc. When you hover over the disabled option, a tooltip will appear with an appropriate explanation.


The option opens the **Compare Data** dialog allowing you to choose specific locations and tables to be compared and configure different options to customize the compare operation. For detailed information about each of the options available in the dialog, see section [Compare Options](#compareoptions) below.

## Compare Options


 Option | Description |
 **Locations**
 | 
Select the source and target location(s) in which the tables will be compared. The location selected in the **SOURCE** field is also called a 'read' location, while the location in the **TARGET** field is called a 'write' location.

The 'read' and 'write' concepts are used to define the behavior of the compare operation, in particular the location where the actual data comparison is performed. For example, if you are comparing data between different types of DBMSes, an ambiguity may occur due to certain data type coercions. The coercion feature maps an empty string from certain DBMSes into a **null** value in the Oracle **varchar** data type. For example, if an Ingres location (**ing**) contains an empty string mapped to a **null** in an Oracle location (**ora**), then should we report that these tables are the same or different? The **Compare Data** option allows both behaviors by applying the sensitivity of the 'write' location rather than the 'read' location. The 'read' location is passive: the data is piped from the ‘read' location to the ‘write’ location, and the work of comparing the data is performed in the ‘write’
location. This means that comparing location **ing** as a source and location **ora** as a target will report that the tables are identical, but comparing **ora** as a source and **ing** as a target will say the tables are different. |
 **Tables
** | 
Select the specific tables to be compared.
 |
 **Table Checksums Only** | 
Enables the **bulk** compare mode. This comparison mode computes a checksum for every row based on all data values, with a final checksum computed across all the checksums for every row. The compare result is determined by whether or not the checksum from the source location matches the checksum from the target location. HVR will report a difference between the source and target tables if the checksum is different, irrespective of whether the reported row count is identical. The bulk mode runs on a database server and only passes the checksum to the hub so it is very efficient in terms of network traffic. However, the bulk mode provides limited detail on the difference. Only the row count is reported, and whether or not the checksum values came out identical.

If this option is not enabled, the `default`compare mode is **row by row**. In this mode, HVR extracts the data from a source (read) location, compresses it and transfers the data to a target (write) location(s) to perform a row by row comparison. Each individual row is compared to produce a 'diff' result. |
 **Table Row Counts Only** | Only count rows, do not compare data.

> **Important:** 
This option is only displayed when option **[Table Checksums Only](#tablechecksumsonly)** is selected.

 |
 **Keep Difference Files ** | 
Verbose. This option creates binary diff files containing individual differences detected.

Section [Analyzing Diff File](https://fivetran.com/docs/hvr6/advanced-operations/analyzing-diff-file) explains how to view and interpret the contents of a diff file.

> **Important:** 
This option is only displayed for the **row by row** compare mode (not available when option **[Table Checksums Only](#tablechecksumsonly)** is selected).

 |
 **Online Compare
** | 
Performs live compare between locations where data is rapidly changing.

> **Important:** 
This option is only displayed for the **row by row** compare mode (not available when option **[Table Checksums Only](#tablechecksumsonly)** is selected).




The online compare has the following modes:

- 
**Combine Initial Differences with Changes Captured while Compare is Running**


Compare tables once and combine differences with captured transactions. Performs a regular compare which produces a result (also known as **diff**). This result (**diff**) is compared with the transaction files (which are continuously created by the **Capture** job) to identify and remove the pending transaction from the result (**diff**) for producing the final compare result. This compare mode is supported for comparing databases and files.

> **Important:** 
If this online compare job is suspended, HVR will continue to accumulate **tx** files with each capture cycle, which will lead to higher disk space usage.


- **Do Compare Twice and Report Only Differences which Occur Twice**
******Delay Between First and Second Compares******
- **Wait**

Compare tables twice with a delay in between. [Capture](https://fivetran.com/docs/hvr6/action-reference/capture) and [Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate) jobs are not required for performing this mode of online compare. This online compare mode is similar to **Flush Capture and Integrate Jobs**, however, with one difference: HVR waits for a specified amount of time, instead of waiting for the completion of the [Capture](https://fivetran.com/docs/hvr6/action-reference/capture) and [Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate) cycle in between compares. Performs a regular compare which produces a result (referred to as **diff**). HVR then waits for the specified time, after which it again performs the regular compare and produces a second result (**diff**). The compare results generated in the first and second compares are combined to produce a final compare result.
- 
**Flush Capture and Integrate Jobs**

Compare tables twice with a **Capture** and **Integrate** flush in between. Performs a regular compare which produces a result (also known as **diff**). HVR then waits for the completion of the full **Capture** and **Integrate** cycle after which it again performs the regular compare which produces a second result (**diff**). The compare results generated in the first and second compare operations are combined to produce a final compare result. This compare mode is only supported for comparing databases.



- 
**Compare Oracle Flashback Moment of Source with Time-Restricted View of Target**


Select data from each table of the source from the same consistent moment in time. Options can be one of the following:

- 
**Now**: If this option is selected, then a new "SCN time" will be retrieved each time the compare job is run. So if **Now** is run on Monday, and the compare job it creates starts running at 10:00 Tuesday and runs again at 10:00 on Wednesday, then the first compare will do a flashback query (for all tables) with an SCN corresponding to Tuesday at 10:00 and the second job run will use flashback query with an SCN corresponding to Wednesday at 10:00.

- **Specific Time**: Flashback query with `**select … as of timestamp**`.
- **hvr_tx_seq**: Value from column **hvr_tx_seq** is converted back to an Oracle SCN number (by dividing by **65536**) and used for flashback query with `**select … as of scn**`. Value is either in decimal or in hex (when it starts with **0x** or contains hex digits).
- **Oracle SCN**: Flashback query with `**select … as of scn**`. Value is an Oracle SCN number, either in decimal or in hex (when it starts with **0x** or contains hex digits).



 |
 **Parallel Sessions** | Parallelism for sessions. Perform compare for different tables in parallel using `` sub-processes. The job will start processing `` tables in parallel; when the first of these is finished the next table will be processed, and so on. |
 **File Prereaders per Table** | 
File prereaders per table. Define the number of prereader subtasks per table while performing a direct file compare. For more information, see section [Direct File Compare](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#directfilecompare).

> **Important:** 
This option is only displayed if the source or target location is a file location.

 |
 **Contexts** | 
This controls whether actions defined with parameter **Context** are effective or are ignored.

Defining an action with **Context** can have different uses. For example, if action **[Restrict](https://fivetran.com/docs/hvr6/action-reference/restrict)** with parameters **[CompareCondition](https://fivetran.com/docs/hvr6/action-reference/restrict#comparecondition)**=**"{id}>22"** and **[Context](https://fivetran.com/docs/hvr6/action-reference/restrict#context)**=**qqq** is defined, then normally all data will be compared, but if context **qqq** is enabled (`**-Cqqq**`), then only rows where **id>22** will be compared. Variables can also be used in the restrict condition, such as **"{id}>{hvr_var_min}"**. This means that `**hvrcompare -Cqqq -Vmin**=**99**` will compare only rows
with **id>99**. To [supply variables for restrict condition](#supplyvariable) use option `**-V**`.

Action **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** can also be defined with parameter [**Context**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#context) on both source and target. This way, the parameter **[CaptureExpression](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression)** will only be activated if a certain context is supplied.

For more information, see the concept page - [Refresh and Compare Contexts](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).

> **Important:** 
This option is only displayed if you have an action ([**CollisionDetect**](https://fivetran.com/docs/hvr6/action-reference/collisiondetect), [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties), [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment), [**FileFormat**](https://fivetran.com/docs/hvr6/action-reference/fileformat), [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate), [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict), [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties), [**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform)) defined with parameter **Context**.

 |
 **Variables** | 
Supply value for the compare restrict condition or add a new variable.
 |
 
**Slicing**
 | 
The slicing section allows you to configure the slicing options. For more information, see the [Slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing) concept page.

**Table Slicing** dialog can be invoked by clicking the **Add Table** button. In this dialog, you can choose the slicing separately for each table in your source.
 |
 **Choose Table** | Table for which the slicing is to be configured. |
 **Choose Type**
 | 
Types of slicing that can be applied to the table:

- **Modulo**
- **Boundary**
- **Count**
- **Series**

 |
 **Choose Column** | 
The table will be sliced by the chosen column's data.

> **Important:** 
Slicing on a non-key column can cause errors if an update moves a row between slices.


The **Distinct Values** field is shown if [dbms_stats](https://docs.oracle.com/database/121/ARPLS/d_stats.htm#ARPLS059) gathering is enabled for the database. The **Distinct Values** column is only available for Oracle.

This option is available when **Modulo** or **Boundary** slicing type is chosen. |
 **Number of Slices** | The number of slices the table will be divided into. |
 **Boundaries** | 
Set the boundaries for each slice. To set them, you have to know the data in your table.

This option is available when the **Boundary** slicing type is chosen. |
 **
Data Type** | 
Choose the data type for slicing. To set it, you have to know the data in your table.

This option is available when the **Boundary** slicing type is chosen. |
 **
Series Values** | 
Set values for each slice. To set them, you have to know the data in your table.

This option is available when the **Series** slicing type is chosen. |
 **Slice Selection** | 
Choose which slices you want to perform the job on.

For example, you have chosen **Boundary** slicing and have set the boundaries to 1000, 3500, and 6000. In this case, you will have 5 slices: with values 0 to 999, 1000 to 3499, 3500 to 5999, and 6000 to the end of the table.

You can choose only the second and third slices so that the **Refresh** job is performed on rows with values 1000 to 5999. |
 
****The **Slicing Suggestions** dialog can be invoked by:

- clicking the **Suggest Slicing** button in the **Slicing** section;
- or by clicking the **Suggest** button in the **Table Slicing** dialog.


In the **Slicing Suggestions** dialog, you can configure the slicing settings for the current job.

> **Note:** 
This option is not supported since 6.3.0/0.

 |
 **
Slicing Suggestions** | 
Repeat a previous slicing job or base it upon certain data:

- **Repeat slicing from last refresh**. Repeats slicing from the last Refresh event.
- **Repeat slicing from last compare**. Repeats slicing from the last Compare event.
- **Based on row-count from last refresh**. Inspects previous Refresh events and suggests the new slicing based on its result.
- **Based on row-count from last compare**. Inspects previous Compare events and suggests the new slicing based on its result.
- **Based on row-counts from DB statistics**. Gets the row count from the Oracle package.


> **Note:** 
This option is not supported since 6.3.0/0.

 |
 **
Tuning Preferences** | 
**Rows per slice** – sets the number of rows per slice. Set to 10 million by default.
**Max slices per table** – sets the maximum number of suggested slices per table. By default, the number is set to 5.

> **Note:** 
This option is not supported since 6.3.0/0.

 |
 **Advanced Compare Options** | 
**Only Count Certain Differences**`**Since** v6.2.5/6`: 
Ignore certain types of differences when comparing data between the source and target systems. When enabled, these difference types are not included in the comparison results. They are also excluded from SQL output generated by the [Verbose mode](#keepdifferencefiles). 

Available options are:

- **No Inserts (when Key only exists in Source)**: Ignores rows that are present in the source but not in the target.
- **No Deletes (when Key only exists in Target)**: Ignores rows that are present in the target but not in the source.
- **No Updates (if Key exists in Source and Target but Other Columns Differ)**: Ignores rows where the primary key matches in both source and target, but non-key column values differ.


> **Important:** 
This option is only displayed for the **row by row** compare mode (not available when option **[Table Checksums Only](#tablechecksumsonly)** is selected).


In the CLI, this option corresponds to the `**-m**` option in [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare).
 |
 **Scheduling Options** | 


Schedule the time to run the compare job. Available options are:

- **Start Immediately**: Invoke the compare job immediately after clicking the **Compare Data** button.
- **Schedule Once at**: Schedule the compare job to run at a specific time once.
- **Schedule Repeatedly at**: Schedule the compare job to run at specific times repeatedly.
- **Delay Running Compare Job**: Schedule invocation of the compare job by leaving it in the **SUSPEND** state.

 |
 **Show Equivalent HVR Command Line** | 
Show CLI command equivalent to the UI options selected in the dialog. You can use (copy and paste) the equivalent line to manually repeat or perform this operation later on.

In cases when the command line equivalents are different for Linux/Unix and Windows, both options are shown.

Select option **Include -R (Remote hub server) argument** to include the parameters for accessing a hub server that runs on a remote machine. For more information about this CLI option, see **hvrcompare[-R](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#rurl)**. |


## Viewing Compare Results


Clicking the **Compare Data** button in the **Compare Data** dialog will start the compare job. You will see the following notification at the top of the page.



Once the compare job has started, the following notification will appear at the top of the page. Click the **View Compare event** link to open the **Event Details** page displaying detailed information about the compare event.



On the **Channel Details** page, the compare job state is displayed on the **Jobs** pane. To open the **Event Details**, click the **More Options** icon  related to the compare job and select **Go To Event**.



The following is an example of the **Event Details** page showing a compare event.

- 
The top pane shows information about the channel and location(s) related to the compare event, the event state, the job name associated with the event, the time the event was started and the event duration.

- 
The middle pane shows additional details related to the configuration parameters set in the **Compare Data** dialog, such as [granularity](#tablechecksumsonly), the number of [parallel sessions](#paralellsessions), etc.

- 
The **Results** pane shows the compare statistics for each table involved in the compare event, such as the number of rows in source and target that were compared, rows that differ, and others. The **View file** link opens the **View Diff File** dialog that allows to inspect a diff file containing the list of differences detected. Section [Analyzing Diff File](https://fivetran.com/docs/hvr6/advanced-operations/analyzing-diff-file) explains how to view and interpret the contents of the diff file. For details on each parameter in the **Results** pane, see section [Refresh and Compare Results](https://fivetran.com/docs/hvr6/user-interface/events/event-details#refreshandcompareresults).




