# Tables - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/user-interface/tables

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/user-interface/tables/index.md)

# Tables


This section describes and illustrates how to add, view, and manage tables. For better understanding of concepts like table name in channel, table name in source, and table name in target, base name, see [Table Name in Source or Target and Base Name](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/table-name-and-base-name).

The **Tables** page displays a list of all tables in all channels or in a selected channel, related to the current HVR Hub. This page provides summary information about the tables, as well as various options to [manage tables](#managingtables).



The **Tables** page displays the following information about tables:

 Field | Description |
 **TABLE** | A table name as defined in the replication channel, as opposed to the **BASENAME** column displaying the actual names of tables in a source or target database. |
 **CHANNEL** | A channel to which a table belongs. |
 **NAME IN SOURCE** | The actual name (basename) of a table in a source location including its schema name (if supported by a DBMS). |
 **NAME IN TARGET** | The actual name (basename) of a table in a target location including its schema name (if supported by a DBMS). |
 **RECENT REFRESH** | 
Information on the most recent refresh operation performed on the table, including table state, the number of rows refreshed, and the time of the last refresh operation. See the available table states in the **RECENT COMPARE** row below.

If a table belongs to multiple source or multiple target locations in a channel and option **Automatic** is selected in the **NAME IN SOURCE** or **NAME IN TARGET** columns (see section [Name in Source or Target](#nameinsourceortarget) below), the **RECENT REFRESH** column shows the data for that location on which the most recent refresh was performed.

If a specific location is selected in the **NAME IN SOURCE** or **NAME IN TARGET** column (see section [Name in Source or Target](#nameinsourceortarget) below), the **RECENT REFRESH** column shows the recent refresh data for that location.
**NONE** means there were no refresh events on the table. |
 **RECENT COMPARE** | 
Information on the most recent compare operation performed on the table, including table state, the number of rows compared, and the time of the last compare operation.

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


If a table belongs to multiple source or multiple target locations in a channel and option **Automatic** is selected in the **NAME IN SOURCE** or **NAME IN TARGET** columns (see section [Name in Source or Target](#nameinsourceortarget) below), the **RECENT COMPARE** column shows the data for that location on which the most recent compare was performed.


If a specific location is selected in the **NAME IN SOURCE** or **NAME IN TARGET** column (see section [Name in Source or Target](#nameinsourceortarget) below), the **RECENT COMPARE** column shows the recent compare data for that location.
**NONE** means there were no compare events on the table. |


The **Columns** button allows you to display additional information about the tables. You can choose the columns to be displayed/hidden so only the required information is displayed on the page.

 Field | Description |
 **BASE NAME** | The actual name of a table in a source or target database, as opposed to the table name (column **TABLE**) in the channel. For more information, see [Table Name in Source or Target and Base Name](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/table-name-and-base-name). |
 **TABLE GROUP** | A table group to which a table belongs.**** For more information on tables groups, see section [Table Groups](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/table-groups). |
 **AVG CHANGES** | A sparkgraph reflecting the average number of changes in a table per the time range selected in the **Graph Range** filter. |


## Filtering Tables


By default, the page displays all tables available in all channels related to a current hub. You can easily find the tables you need using one of the following filters.

- **Channels** selector allows you to display only the tables belonging to a specific channel.
- **Table Group** selector allows you to display only tables belonging to a specific table group(s).
- **Search** field allows you to search table(s) by name. The tables get filtered as you type.




## Name in Source or Target


This section describes columns **NAME IN SOURCE** and **NAME IN TARGET**.

> **Important:** 
The following description is related to column **NAME IN SOURCE**. The same applies to target locations in column **NAME IN TARGET**.


The **NAME IN SOURCE** column displays the actual table names (base names) in the source locations prefixed by schema names (if supported by a DBMS).

To display only the table names of a specific source location, click the **SOURCE** link and select the required location from the list of available locations. Only the tables belonging to the selected location will be displayed, the other rows in the **NAME IN SOURCE** column become empty. Click the sort icon  to display the table names at the top of the list.

**Automatic** is the default option to display the table names for all source locations.

> **Important:** 
If a specific channel is selected (pinned) in the **Channels** selector, only locations belonging to this channel are displayed when you click the **SOURCE** link.




In certain scenarios, the same table can be named differently in several source locations (for example, have different base names or schema names). In such cases, the **NAME IN SOURCE** columns displays the table name as follows:

 Table name in Location1 | Table name in Location2 | Displayed in NAME IN SOURCE |
 schema1.table1 | schema2.table1 | table1 |
 schema1.table1 | schema1.table2 | schema1.table1+ |
 schema1.table1 | schema2.table2 | table1+ |




If a table name is too long to fit into the cell, it is displayed with the three dots. Hover over the table name to see the full table name.



## Sorting Tables


All columns in the table list can be sorted. Simply click the necessary column heading to sort the data in it.

- Columns **Table**, **Basename**, **Channel**, **Table Group**, **Name In Source**, and **Name In Target** are sorted alphabetically.
- Columns **Recent Refresh** and **Recent Compare** are sorted by the time the operation took place.
- Column **Changes** is sorted by the number of changed rows.


## Managing Tables


The following options to manage tables are available at the top right menu, as well as under the **More options** menu .

> **Note:** 
To select multiple tables in one go, select the first table, hold the **Shift** key and then select the last table - all tables in between the first and the last will be selected.


- 
[**Add Tables**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel)
Add tables to a channel from one of the existing locations.

- 
[**Delete Tables**](https://fivetran.com/docs/hvr6/user-interface/tables/deleting-tables-from-channel)
Delete the selected table(s) from a specific channel.

- 
[**Compare Data**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data)
Compare data in the selected table(s) between source and target locations. To enable this option, select a specific channel in the **Channels** selector.

- 
[**Refresh Data**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)
Copy data in the selected tables(s) from source to target. To enable this option, select a specific channel in the **Channels** selector.

- 
[**Create/Alter Target Tables**](https://fivetran.com/docs/hvr6/user-interface/tables/creating-or-altering-target-tables)
Create table(s) that are absent in a target location or alter the existing tables in the target location, and optionally fill the tables with the data from the source.

- 
**Copy Table Names**
Copy the selected table names to the clipboard. The copied table names can be used in the [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) dialog to activate replication only for these specific tables.

- 
**Copy Names in Source**
Copy the selected table names as they are given in the source. The copied table names can be used for filtering tables in the [**Adding Tables to a Channel**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel) and the [**Adding SAP Tables to a Channel**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-sap-tables-to-a-channel) dialogs.

- 
[**Import and Exporting Table Definitions**](https://fivetran.com/docs/hvr6/user-interface/tables/importing-and-exporting-table-definitions)
Import and export one or more table definitions from/to a JSON file.

- 
[**Check Definition Against Actual Source/Target**](https://fivetran.com/docs/hvr6/user-interface/tables/checking-definition-against-source-or-target)
Compare the table definitions in the channel with the actual table definition(s) in the database.

- 
[**Redefine Table From Actual Source or Target**](https://fivetran.com/docs/hvr6/user-interface/tables/redefining-table-from-source-or-target)
Compare the actual table definition in a database (source or target) with the table definition in the channel and update the table definition accordingly.

- 
[**Change Table Group**](https://fivetran.com/docs/hvr6/user-interface/tables/changing-table-group)
Assign a table to one of the existing table groups or create a new group for the table.

- 
[**Activating Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication)
Start replication for the selected table(s). Set or reset replication components if required.

- 
[**Deactivate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication)
Stop all replication jobs for the selected tables(s). This will drop the replication components created for the table(s).

- 
[**View Actions**](https://fivetran.com/docs/hvr6/user-interface/action-list)
View actions defined in a channel in the [**Actions List Drawer**](https://fivetran.com/docs/hvr6/user-interface/action-list).

- 
**Show Start Page**
Open the Start page. This is a landing page that opens when you first access the [web user interface](https://fivetran.com/docs/hvr6/user-interface). This page offers a starting point for new users that helps them build up a replication channel in HVR.


