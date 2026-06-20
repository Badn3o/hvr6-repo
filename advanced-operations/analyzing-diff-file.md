# Analyzing Diff File - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/analyzing-diff-file

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/analyzing-diff-file/index.md)

# Analyzing Diff File


A diff file is a file that stores the differences between source and target locations detected during regular row-by-row compare or refresh. The file is created for each table in which differences are found. A diff file can be viewed in the user interface or command line.

> **Important:** 
The diff file is only created when the differences are detected.


The diff file is generated when:

- performing [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare):
- 
in the user interface: with option [**Keep Difference Files**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#keepdifferencefiles) enabled in the **Compare Data** dialog.

- 
on the command line: using command [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare) with options [**-gr**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#g) and [**-v**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#verbose).



- performing [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh):
- 
in the user interface, with option [**Keep Difference Files**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#repairrowbyrowgranularity) enabled in the ****Refresh Data** into Target** dialog.

- 
on the command line: using command [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) with options [**-gr**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh#g) and [**-v**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh#verbose).





## Viewing Diff File in UI


To view the diff file on the user interface:

- 
On the left sidebar, click **EVENTS** to open the **Events** page.

- 
On the **Events** page, click the required compare event to expand the event details.

- 
Click the **View Results** button. This will open the [**Event Details**](https://fivetran.com/docs/hvr6/user-interface/events/event-details) page related to the compare or refresh event.

- 
On the **Event Details** page, navigate to the **Results** pane and click **View file** in the **DIFF FILE** column. This will open the **View Diff File** dialog.

- 
In the **View Diff File** dialog, click **Inspect Differences**.



> **Note:** 
To view the diff file in CLI, click [**Show Equivalent Fivetran Command Line**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#showequivalenthvrcommandline) and copy the command to the clipboard, then run this command in the Fivetran CLI to view the diff file.


This opens the **Diff File View** displaying the differences between a source location and the target location. For more information, see section [Interpreting Diff File](#interpretingdifffile) below.





### Interpreting Diff File in UI


Each row in the **Diff File Viewer** identifies an operation (an update, insert or delete) to be applied (or already applied in the case of refresh) against a target location to bring it in sync with a source location.

> **Important:** 
When a cell content is too large, a maximum of 400 characters is displayed. In this case, the displayed content starts with the first difference detected.




 Operation | Description |
 **Update** | 
The **Update** operation is represented by a pair of lines having the same key value. The upper pink line starts with a minus (**-**) symbol and identifies the existing row on target, which is out of sync. The lower green line starts with a plus (**+**) symbol and identifies the existing row on the source to update the target row.

In the image above, the update is indicated by the first two rows that have a value of **100** in the **PROD_ID** key column and different values in column **CUST_NAME**. The update operation will replace value **Customer8** on target with value **Customer1** on the source. |
 **Insert** | 
The **Insert** operation is represented by one green line starting with a plus (**+**) symbol.

In the image above, the insert is indicated by the line with value **101** in the **PROD_ID** key column. The insert operation will add the existing row on the source to the target because it is missing from the target. |
 **Delete** | 
The **Delete** operation is represented by one pink line starting with a minus (**-**) symbol.

In the image above, the delete is indicated by the row with a value of **102** in the **PROD_ID** key column. The delete operation will delete the existing row on the target because it is missing from the source. |


#### Inconclusive Difference


The inconclusive difference can only be detected during the [**diff_diff** online compare](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#onlinecompare) when the compare results generated in the first and second compare operations are combined to produce a final compare result. The inconclusive difference means that during a first compare operation, one kind of difference is detected and during the second compare operation, a different difference in the same row is detected.

The inconclusive difference is highlighted in yellow. For example, the following image demonstrates that during the first compare, the value on the source was **90**, the value on target was not **90**, but also was not **96**. Then, in the second compare, the source still has **90**, but the target has **96** this time.



## Viewing Diff File in CLI


To view the diff file on the command line interface (CLI), use command [**hvrrouterview**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrouterview). The corresponding command (marked bold) is displayed after the compare or refresh event is completed.
$ hvrcompare -r src -l tgt -gr -v myhub mychannel

hvrcompare: Fivetran 6.1.6/0 (linux_glibc2.17-x64-64bit)
hvrcompare: Updated job mychannel-cmp-src-tgt with [State='SUSPEND'].
hvrcompare: All suspended jobs are inactive.
hvrcompare: Compare event 2022-04-01T11:25:21.424Z created for job 'mychannel-cmp-src-tgt'.
hvrcompare: Started job 'mychannel-cmp-src-tgt'.
2022-04-01T13:25:21+02:00: mychannel-cmp-src-tgt: Event 2022-04-01T11:25:21.424Z is starting.
2022-04-01T13:25:21+02:00: mychannel-cmp-src-tgt: Checking the consistency of the channel definition.
2022-04-01T13:25:21+02:00: mychannel-cmp-src-tgt: Event status: 0(+1)/10 subtasks done(+busy)/total.
2022-04-01T13:25:22+02:00: mychannel-cmp-src-tgt: Table 'dm51_order' is identical in location 'src' and location 'tgt' (944 rows). This row-wise compare took 0.18 seconds.
2022-04-01T13:25:22+02:00: mychannel-cmp-src-tgt: Table 'dm51_product' in location 'src' (100 rows) and location 'tgt' (100 rows) differ by 1 update (compression=67.2%). This row-wise compare took 0.13 seconds.
2022-04-01T13:25:22+02:00: mychannel-cmp-src-tgt: Row-wise compare of location 'src' and 'tgt' found 1 identical table and 1 different table. (elapsed=0.57s)
2022-04-01T13:25:22+02:00: mychannel-cmp-src-tgt: Event 2022-04-01T11:25:21.424Z is completed. (elapsed=1.27s)
hvrcompare: Differences between src and tgt for table dm51_product from event 2022-04-01T11:25:21.424Z can be viewed by running:
<b>hvrrouterview myhub mychannel /home/hvr/hvr_config/hubs/myhub/channels/mychannel/locs/tgt/diff/mychannel-cmp-src-tgt_2022-04-01_11-25-21_424Z_dm51_product_zRsfn.diff</b>
hvrcompare: Finished. (elapsed=3.11s)

After running the command, you will get the output similar to the following:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hvr_private SYSTEM "lib/hvr_private.dtd">
<hvr_private version="1.0">
    <table name="dm51_product">
        <row>
            <column name="hvr_op">4</column>
            <column name="hvr_diff_mask">----=!=</column>
            <column name="hvr_diff_row_num_left">66</column>
            <column name="hvr_diff_row_num_right">66</column>
            <column name="prod_id">66</column>
            <column name="prod_price">5</column>
            <column name="prod_descrip">Description for product</column>
        </row>
        <row>
            <column name="hvr_op">2</column>
            <column name="hvr_diff_mask">----=!=</column>
            <column name="hvr_diff_row_num_left">66</column>
            <column name="hvr_diff_row_num_right">66</column>
            <column name="prod_id">66</column>
            <column name="prod_price">6</column>
            <column name="prod_descrip">Description for product</column>
        </row>
    </table>
</hvr_private>

### Interpreting Diff File in CLI


The diff file contains rows that specify which operations (update, insert, or delete) need to be applied (or already applied in the case of refresh) against a target location to bring it in sync with a source location.

Each row in a diff file contains:

- system columns **hvr_op**, **hvr_diff_mask**, **hvr_diff_row_num_left** and **hvr_diff_row_num_right**. These columns will help you read and interpret the diff file contents.
- columns from the actual tables on the source and target locations, in which the differences are detected, e.g. **prod_id**, **prod_price**, **prod_descrip**.


### Column hvr_op


Column **hvr_op** defines the Fivetran HVR operation to apply against a target table. Column **hvr_op** can contain the following values.

 hvr_op | Description |
 **0** | Delete on target (existing row on the target) |
 **1** | Insert on target (existing row on the source) |
 **2** | Update on target (existing row on source, new value for target) |
 **4** | Appears before the row with ****hvr_op=**2**. Defines the existing value on target, which is out of sync. |
 **6** | Appears before the row with **hvr_op=0** or **hvr_op=1**. Defines a previous value on the location (source or target) opposite to that shown in the row with **hvr_op=0** or **hvr_op=1**. Explains why insert or delete is required. |


### Column hvr_diff_mask


Column **hvr_diff_mask** shows which columns are identical and which columns are different. It contains a set of characters (shown in the table below), one character for each column. Column **hvr_diff_mask** should be considered in combination with column **hvr_op**.

Column **hvr_diff_mask** can contain the following characters.

 hvr_diff_mask | Description |
 **-** | The column is not relevant. |
 **=** | The column is identical between source and target. |
 **!** | The column is different between source and target. |
 
**>**
**<** | 
Appears on all columns if one side (source or target) finishes early. All remaining rows will be inserts or deletes.

Similar to **hvr_op=6**: explains why an insert/delete is required. |
 
**&**

**{**
**}** | 
The inconclusive difference, only during the [**diff_diff** online compare](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#onlinecompare). Similar to '**!**' , but there is no indication if the rows are identical or different.

- '**{**' means inconclusive because of the source.
- '**}**' means inconclusive because of the target.
- '**&**' means inconclusive because of both sides.

 |


The table below demonstrates different values that can appear in the **hvr_diff_mask** column.

For example, value "**----==!**" indicates the following:

- "**----**" defines the first four system columns (**hvr_op**, **hvr_diff_mask**, **hvr_diff_row_num_left**, **hvr_diff_row_num_right**)
- "**==**" defines the table columns which are equal between source and target
- "**!**" defines the seventh column in this example that differs in source and target




> **Important:** 
- 
The first four characters are normally “**-**” because they are the "**hvr_**" columns.

- 
For updates, key columns will always be identical: “**=**”. For inserts/deletes, the key columns will be different ("**!**") (see **hvr_op=6** followed by **hvr_op=0** in the above image) and non-key columns will be irrelevant ("**-**") because they cannot be compared if they belong to different keys.

- 
Non-key columns can be identical “**=**” or different “**!**".




### Columns hvr_diff_row_num_left and hvr_diff_row_num_right


During a compare or refresh event, HVR runs the query that selects all records in a table and orders them by all key columns (SELECT...ORDER BY), on both source and target locations. Columns **hvr_diff_row_num_left** and **hvr_diff_row_num_right** contain a row number of the query results in which the difference is detected.

- 
Column **hvr_diff_row_num_left** defines the row number on the source

- 
Column **hvr_diff_row_num_right** defines the row number on the target



 **hvr_op=0** | If **hvr_op=0** (delete), column **hvr_diff_row_num_right** will be > 0; this means that the row data is on target. |
 **hvr_op=1** | If **hvr_op=1 (**insert), column **hvr_diff_row_num_left** will be > 0 ; this means that the row data is on source. |
 **hvr_op=6** | 
If **hvr_op=6**, either of ****hvr_diff_row_num_left**** or ******hvr_diff_row_num_right****** will be > 0

It will be the opposite of its pair **hvr_op=0/1** row |
 **hvr_op=4**
**hvr_op=2** | If **hvr_op=2** (update), both **hvr_diff_row_num_left** or ******hvr_diff_row_num_right****** will be > 0.

In **hvr_op=4** and **hvr_op=2** pair, both **hvr_diff_row_num_left** or ******hvr_diff_row_num_right****** will have the same values. |


For example, the following piece of diff file indicates that row 1 on target ( **hvr_diff_row_num_right=1**) containing **prod_id=1**, **prod_price=80 and prod_descrip=Book** needs to be deleted (**hvr_op=0**).
<row>
<column name="hvr_op">0</column>
<column name="hvr_diff_mask">----!--</column>
<column name="hvr_diff_row_num_left">0</column>
<column name="hvr_diff_row_num_right">1</column>
<column name="prod_id">1</column>
<column name="prod_price">80</column>
<column name="prod_descrip">Book</column>
</row>

The following piece of diff file shows that there is a difference between source and target in row **10**. The existing row 10 on target (**hvr_op=4**) with values **prod_id=8**, **prod_price=81**, and **prod_descrip=Pencil** needs to be updated (**hvr_op=2**) with values **prod_id=8**, **prod_price=80**, and **prod_descrip=Book** present in row 10 on source (**hvr_diff_row_num_left=10**).
<table name="dm51_product">
<row>
<column name="hvr_op">4</column>
<column name="hvr_diff_mask">----=!=</column>
<column name="hvr_diff_row_num_left">10</column>
<column name="hvr_diff_row_num_right">10</column>
<column name="prod_id">8</column>
<column name="prod_price">81</column>
<column name="prod_descrip">Pencil</column>
</row>
<row>
<column name="hvr_op">2</column>
<column name="hvr_diff_mask">----=!=</column>
<column name="hvr_diff_row_num_left">10</column>
<column name="hvr_diff_row_num_right">10</column>
<column name="prod_id">8</column>
<column name="prod_price">80</column>
<column name="prod_descrip">Book</column>
</row>
</table></div>

### Rows Which Differ


The difference that requires updating the target row(s) appears only for non-key columns. HVR detects a row with the same key columns in source and target and one or more non-key columns having different values.

The difference is always indicated by a pair: **hvr_op=4** followed by **hvr_op=2**.

- **hvr_op=4**: Existing row value on target
- **hvr_op=2**: New row value for target. This is what HVR detects on the source.


Column **hvr_diff_mask** shows which columns are identical and which columns are different.

- 
Key columns are always identical: “**=**”

- 
Non-key columns can be identical “**=**” or different “**!**”



The table on the right shows three differences that require updates:

- Blue: Row with **prod_id=3100** that has **prod_descrip=x3100** on target must be updated as **3100** to be in sync with the source. Column **prod_price** is identical on source and target.
- Similar updates must be performed on the green and red rows.




### Rows Only on Target


The difference that requires deleting the target row appears when HVR detects a row on target, but does not find it on the source.

This difference may appear in a group: **hvr_op=6**, **hvr_op=0**, **hvr_op=0**, …

- **hvr_op=6** is informational and indicates why the row(s) need to be deleted.
- **hvr_op=0** is the row to be deleted on target.


Column **hvr_diff_mask** shows which key columns are different.

The differences can be viewed as **hvr_op=6** **hvr_op=0**, **hvr_op=6** **hvr_op=0** pairs (similar to **hvr_op=4** **hvr_op=2**); except that all **hvr_op=6** are combined to a single row.

The table on the right shows differences that require deleting rows on target.

HVR detected row **prod_id** to jump from **460** to **1000** on the source, but on the target, it detected rows with **461**, **462**, and **463**.

These rows are extra on target and must be deleted (**hvr_op=0**). The reason is that the row with **hvr_op=6** detected on source (**hvr_diff_row_num_left=462**) with a difference (**hvr_diff_mask=!**) in the **prod_id** key column.



### Rows Only on Source


These are the opposite of '[Rows Only on Target](#rowsonlyontarget)'.

HVR finds a row on the source but does not see it on target.

This difference always appears in a group: **hvr_op=6**, **hvr_op=1**, **hvr_op=1**, …

- **hvr_op=6** is informational and indicates why the row(s) needs to be inserted. However, in this case, it shows the row on target (**hvr_diff_row_num_right > 0**)
- **hvr_op=1** are the rows to be inserted on target. These rows are on the source but not yet on target.




### Deletes or Inserts at the End of Diff File


This difference will appear only at end of the diff file indicating the rows to be inserted or deleted. There is no **hvr_op=6**. Instead, column **hvr_diff_mask** contains all “**<<<<<<<**” or all “**>>>>>>>**”.

It means that during the SELECT...ORDER BY query, one side (source or target) ran out of data before the other side. Therefore, all remaining rows are to be deleted or inserted depending on which side ran out of data.

The diagram on the right demonstrates this.

- **hvr_op=1** indicates rows to be inserted on the target. They exist on the source.
**hvr_diff_mask** will be "**>>>>>>>**".
- **hvr_op=0** indicates rows to be deleted from the target. They do not exist on the source.
**hvr_diff_mask** will be "**<<<<<<<**".



