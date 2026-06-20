# Table Details - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/user-interface/tables/table-details

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/user-interface/tables/table-details/index.md)

# Table Details


The **Table Details** page provides detailed information about a specific table.

## Table Naming


The header section of the **Table Details** page displays information about the table's name in a channel, base name, name in a source database, name in a target database, and the table group. For more information about table names, see section [Table Name and Base Name](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/table-name-and-base-name).

The **Change** button in the **Names** section opens the **Rename Table** dialog, where you can change the table's name in the channel and base name. For the steps to renaming a table, see section [Renaming Table](https://fivetran.com/docs/hvr6/user-interface/tables/renaming-table).

The **Change** button in the **Other information** section opens the **Change Table Group** dialog, where you can change the table group for the table.



 Field | Description |
 **BASE NAME** | The actual name of a replicated table in a source or target database. Every table involved in replication will be assigned a **Base Name** and **Table Name**. The **Base Name** of a table may differ from the **Table Name** defined in the channel, e.g. if it contains special characters that are not supported by HVR or if its name is too long. |
 **NAME IN SOURCE** | The actual name of a table in a source database including a schema name (if supported by a DBMS). This is what the **Table Name** is actually mapped to in the source database. |
 **NAME IN TARGET** | The actual name of a table in a target database including a schema name (if supported by a DBMS). This is what the **Table Name** is actually mapped to in the target database. |
 **TABLE GROUP** | A logical group of one or more tables. Combining tables in one table group allows you to define a single action on multiple tables at a time, rather than defining multiple identical actions for each table separately. |


## Columns


Under the **Columns** tab, you can find a grid with detailed information about each column in the table.



 Column | Description |
 **COLUMN NAME** | Unique name of a column as defined in a replication channel. |
 **DEFINITION DATA TYPE** | Data type of a column as defined inside your channel definition. |
 **KEY** | A column defined as a replication key that HVR uses for replication. |
 **DATA TYPE DEFINED FOR SOURCE** | The actual data type in a source database. |
 **DATA TYPE DEFINED FOR TARGET** | 
The actual data type in a target database. Usually, the **Definition Data Type** matches the **Data Type Defined for Source**, but it is quite common that the **Data Type Defined for Target** is slightly different. For example, if there is a column in an Oracle source location with data type **number**, then the **Definition Data Type** will be number. But on an SQL Server target location, it will be **decimal**.

For more information on data type mapping in HVR, see section [Data Type Mapping](https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping).
 |


If you click the **Columns** button near the **Data Type Defined For Target** column, you will see the list of additional columns for displaying advanced information for the current table.

 Column | Description |
 **COLUMN PROPERTIES FOR SOURCE** | The [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) action(s) defined on the table for a specific column on a source location. Clicking the property will open the **[Actions](https://fivetran.com/docs/hvr6/user-interface/action-list)** panel with a filter on the **ColumnProperties** action. |
 **COLUMN PROPERTIES FOR TARGET** | The [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) action(s) defined on the table for a specific column on a target location. Clicking the property will open the **[Actions](https://fivetran.com/docs/hvr6/user-interface/action-list)** panel with a filter on the **ColumnProperties** action.
 |


### Contexts


The **Contexts** area is displayed on the **Columns** tab when actions [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) and/or [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameter **Context** are defined for the table. The main purpose of this option is to reflect the state of the table if the context was enabled. For example, if action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameters [**Name**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#name)=**extra_col**, [**Extra**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#extra) and [**Context**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#context)=**extra** is defined for a table, and context **extra** is enabled in the **Contexts** area, column **extra_col** will be displayed in the table grid. For more information, see the concept page [Refresh and Compare Contexts](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).



## Managing Columns


The following options to manage columns are available on the **Columns** tab as well as under the **More Options** menu :

- 
[**Add Column**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-columns-to-table)
Add column(s) to the table.

- 
[**Check Definition Against Actual Source or Target**](https://fivetran.com/docs/hvr6/user-interface/tables/checking-definition-against-source-or-target)
Compare the table definitions in the channel with the actual table definition(s) in the database.

- 
[**Redefine Table From Actual Source or Target**](https://fivetran.com/docs/hvr6/user-interface/tables/redefining-table-from-source-or-target)
Compare the actual table definition in a database (source or target) with the table definition in the channel and update the table definition in the channel accordingly.

- 
[**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication)
Start replication for the current table. Set or reset replication components if required.

- 
[**Deactivate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication)
Stop replication for the current table. This will drop replication components that were created for this table.

- 
[**Compare Data**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data)
Compare tables in the current table between source and target.

- 
[**Refresh Data**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)
Copy data in the current table from the source location to the target location.

- 
[**Create/Alter Target Table**](https://fivetran.com/docs/hvr6/user-interface/tables/creating-or-altering-target-tables)
Copy the current table to a target location. This will either create a new table (if absent) or alter the existing table in the target location, and optionally fill the table with the data from the source.

- 
[**Export Table Definition**](https://fivetran.com/docs/hvr6/user-interface/tables/importing-and-exporting-table-definitions)
Export one or multiple table definitions into a JSON file.

- 
[**View Actions**](https://fivetran.com/docs/hvr6/user-interface/action-list)
View actions defined in a channel in the **Actions** panel.

- 
[**Add Action**](https://fivetran.com/docs/hvr6/user-interface/action-list/adding-action)
Add action to define the behavior of the replication.



Each column has its own **More Options** menu  with the following options:

- [**Edit Column**](https://fivetran.com/docs/hvr6/user-interface/tables/editing-column)
Edit column name and data type, add attributes, make it a key column.
- [**Add Column Before**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-columns-to-table)
Add a column to the table before the current column.
- [**Add Column After**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-columns-to-table)
Add a column to the table after the current column.
- [**Delete  from Definition**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-columns-to-table)
Delete the column from the channel definition.


## Compare and Refresh History


Under the **Compare History** and **Refresh History** tab, you can find detailed information about compare and refresh operations performed on the table. Each time you run a compare or refresh operation, a corresponding event is created in the [event](https://fivetran.com/docs/hvr6/getting-started/concepts/events) system. The **Compare History** and **Refresh History** tables display the details of compare and refresh events associated with the current table.



 Field | Description |
 **EVENT** | Timestamp of the event. |
 **SOURCE LOCATION** | Source location of which the table is a member. |
 **TARGET LOCATION** | Target locations of which the table is a member. |
 **EVENT STATE** | 
Status of the event.

The following event states are available:

- 
**CURRENT** - The event is not completed yet.

- 
**CANCELED** - The event was canceled by a user.

- **DONE** - The event is completed successfully.
- **FAILED** - The event failed to complete due to an error.
- **WAITING** - The event will run at a scheduled time.

 |
 **TABLE STATE** | 
Status of the table.

The following table states are available:

- 
**BUSY** - The event is busy with subtasks for this table.

- **BUSY/DIFFERENT** - The event is busy with subtasks for this table. A compare difference was detected already.
- **DONE** - The event has completed all subtasks for this table.
- 
**DONE/DIFFERENT** - The event has completed all subtasks for this table. A compare difference was detected: the tables are NOT identical in source and target locations.

- 
**DONE/IDENTICAL** - The event has completed all subtasks for this table. No compare difference was detected: tables are identical in source and target locations.

- 
**DONE/INCONCLUSIVE** - (applicable only for **Online Compare**). The event has completed all subtasks for this table. Compare differences were encountered, but it cannot be determined whether these are persistent or due to online/live change.

- **PENDING** - The event has not yet started subtasks for this table.

 |
 **SOURCE ROWS SELECTED** | Total number of rows selected in the source table for comparing/refreshing. |
 **TARGET ROWS SELECTED** | Total number of rows selected in the target table for comparing/refreshing. |
 **DURATION** | Time taken to compare/refresh the table. |
 **SPEED** | Speed of compare/refresh operation in rows per second. |


If you click the **Columns** button, a drop-down menu will show additional columns for displaying advanced information about the compare and refresh operations. For more information about data displayed in these columns, see [Event Details](https://fivetran.com/docs/hvr6/user-interface/events/event-details).

The timestamp in the **EVENT** column is a link to the corresponding [Event Details](https://fivetran.com/docs/hvr6/user-interface/events/event-details) page. Names of source and target locations are links to the corresponding [Location Details](https://fivetran.com/docs/hvr6/user-interface/locations/location-details) page.
