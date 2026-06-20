# Restrict - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/restrict

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/restrict/index.md)

# Restrict


Action **Restrict** defines that only rows meeting a certain condition should be replicated. The restriction logic is enforced during capture and integration and also during [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

---

## Parameters


This section describes the parameters available for action **Restrict**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from Fivetran HVR documentation, emails, or demo notes.




### CaptureCondition


**Argument**: *sql_expr*

**Description**: Defines a condition to filter rows during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture). Only rows where the SQL expression *sql_expr* evaluates to TRUE are captured.
Expand to see the possible substitutions for the SQL expression
The SQL expression *sql_expr* can contain the following substitutions:

- 
**{***colname***}** is replaced with the value of current table's column *colname*.

For Db2 for z/OS, you must cast the column values to the exact data type. For more information, see [Column Substitution](#columnsubstitution) section below.

- 
**{hvr_cap_loc}** is replaced with the location name.

- 
**{hvr_cap_tstamp}** is replaced with the moment (time) that the change occurred in the source location.

- 
**{hvr_cap_user}** is replaced with the name of the user who made the change.



A subselect can be supplied. For example, EXISTS (SELECT 1 FROM lookup WHERE id={id}).

This parameter enables “update conversion”, where UPDATE changes to rows are transformed into different operations (like DELETE or INSERT) based on whether the rows satisfy a specified condition. For example, if an UPDATE changes a row that satisfies a condition into one that does not; such an UPDATE is converted into a DELETE. However, if the UPDATE changes a row from not satisfying the condition to satisfying it, the UPDATE is converted into an INSERT. The [**IgnoreCondition**](https://fivetran.com/docs/hvr6/action-reference/capture#ignorecondition) parameter in [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) action has a similar effect to this parameter but does not do "update conversion".

---

### IntegrateCondition


**Argument**: *sql_expr*

**Description**: Defines a condition to filter rows during [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate). Only rows where the SQL expression *sql_expr* evaluates to TRUE are integrated.
Expand to see the possible substitutions for the SQL expression
The SQL expression *sql_expr* can contain the following substitutions:

- 
**{***colname***}** is replaced with the value of current table's column *colname*.

For Db2 for z/OS, you must cast the column values to the exact data type. For more information, see [Column Substitution](#columnsubstitution).

- 
**{hvr_cap_loc}** is replaced with the location where the capture was changed.

- 
**{hvr_cap_tstamp}** is replaced with the moment (time) that the change occurred in source location.

- 
**{hvr_cap_user}** is replaced with the name of the user who made the change.



A subselect can be supplied. For example, EXISTS (SELECT 1 FROM lookup WHERE id={id}).

For [**Burst Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), this parameter acts as a filter that is applied on the integration. Note that if in a single integrate cycle a row was inserted and subsequently deleted then the row will not be integrated with **BURST** defined, regardless of the filter.

For [**Continuous Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method), this parameter performs 'update conversion.' Update conversion occurs when. For example, an update changes a row that previously satisfied a condition, making it into a row that no longer satisfies the condition. In such cases, the update is converted to a delete. However, if the update changes the row from not satisfying the condition to satisfying it, then the update is converted to an insert.

> **Important:** 
- 
This parameter is supported only for database locations.

- 
If you are filtering a large number of rows, you may observe a spike in [MAR](https://fivetran.com/docs/core-concepts/usage-based-pricing#hvr). To address this situation, you can instead use [**CaptureCondition**](#capturecondition) or [**AddressTo**](#addressto)/[**AddressSubscribe**](#addresssubscribe).




---

### RefreshCondition


**Argument**: *sql_expr*

**Description**: Defines a condition to filter rows during [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh). Only rows where the SQL expression *sql_expr* evaluates to TRUE are refreshed.
Expand to see the possible substitutions for the SQL expression
The SQL expression *sql_expr* can contain the following substitutions:

- 
**{***colname***}** is replaced with the value of current table's column *colname*.

For Db2 for z/OS, you must cast the column values to the exact data type. For more information, see [Column Substitution](#columnsubstitution).

- 
**{hvr_var_***xxx***}** is replaced with value of 'context variable' *xxx*. The value of a context variable can be supplied using option **–V***xxx***=***val* to command [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) or [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare).

- 
**{hvr_local_loc}** is replaced with the current location name.

- 
**{hvr_schema}** is replaced with the schema name of the table. This is only allowed if the channel is defined with the tables. This can only be used when action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) with parameter [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema)=*my_schema* is explicitly defined for these tables on the target file location.

- 
**{hvr_tbl_base_name}** is replaced with the base name of the current table.

- 
**{hvr_opposite_loc}** on the source database is replaced with the target location name and on the target database it is replaced with the source location name. This feature allows compare and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) to be made aware of horizontal partitioning.



For [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), the effect of this parameter depends on whether it is defined on the source or on the target side.

- 
If defined on the source side, it affects which rows are selected for refreshing (SELECT * FROM <em>source</em> WHERE <em>condition</em>).

- 
If defined on the target side, during [**Bulk Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh#refreshtypes) it protects non–matching rows from bulk delete (DELETE FROM <em>target</em> WHERE <em>condition</em>, instead of just TRUNCATE <em>target</em>).

- 
If defined for [**Row-wise Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh#refreshtypes), it prevents some rows from being selected for comparison with the source rows (SELECT * FROM <em>target</em> WHERE <em>condition</em>).



> **Important:** 
- 
If the [**CompareCondition**](#comparecondition) parameter is not defined, then [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) will use **RefreshCondition** to determine which rows are compared.

- 
This parameter should not be defined with the [**SliceCondition**](#slicecondition) parameter.

- 
This parameter is supported only for database locations or for file locations with Hive External Tables.




---

### CompareCondition


**Argument**: *sql_expr*

**Description**: Defines a condition to filter rows during [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare). Only rows where the SQL expression *sql_expr* evaluates to TRUE are compared.
Expand to see the options available for this parameter
The SQL expression *sql_expr* can contain substitutions:

- 
**{***colname***}** is replaced with the value of current table's column *colname*.

For Db2 for z/OS, you must cast the column values to the exact data type. For more information, see [Column Substitution](#columnsubstitution).

- 
**{hvr_var_***xxx***}** is replaced with value of 'context variable' *xxx*. The value of a context variable can be supplied using option **–V***xxx*=*val* to command [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) or [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare).

- 
**{hvr_local_loc}** is replaced with the current location name.

- 
**{hvr_opposite_loc}** on the source database is replaced with the target location name and on the target database it is replaced with the source location name. This feature allows compare to be made aware of horizontal partitioning.

- 
**{hvr_schema}** is replaced with the schema name of the table. This is only allowed if the channel is defined with the tables. This can only be used when action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) with parameter [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema)=*my_schema* is explicitly defined for these tables on the target file location.

- 
**{hvr_tbl_base_name}** is replaced with the base name of the current table.

- 
**{hvr_integ_seq}**, **{hvr_tx_seq}**, **{hvr_tx_scn}** are replaced with values corresponding to SCN of the Oracle 'flashback moment' on the Oracle source database. These substitutions are only available on the target when option **Select Moment** (option **-M**) is supplied to [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh). For example, if the target is defined with action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) (parameters [**Name**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#name)=*tkey* and [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey) and [**IntegrateExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#integrateexpression)**="{hvr_integ_seq}"**) and action **Restrict** (parameter **CompareCondition="***tkey* **<= {hvr_integ_seq}"**) then an "on-line compare" can be done by supplying a **Select Moment** (option **-M**) with time or SCN older than the current latency.



> **Important:** 
- 
If this parameter is not defined, [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) will use the [**RefreshCondition**](#refreshcondition) parameter to determine which rows are compared.

- 
This parameter should not be defined with the [**SliceCondition**](#slicecondition) parameter.

- 
Restricting [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) based on a non-key column can lead to inaccurate results if an update to the restricted column has not yet been replicated to the target location before [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) starts, or if the restricted column is updated while an [Online Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare#onlinecompare) is running.




---

### RefreshJoinCondition


<strong>Since</strong> 6.2.5/5

**Argument**: *sql_expr*

**Description**: Defines a join condition to filter rows during a **[Refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh)** operation. Only rows for which the SQL join expression *sql_expr* evaluates to TRUE are refreshed.

The SQL expression *sql_expr* can include the following substitution:

- **{***colname***}** - Replaced with the value of the current table's column *colname*.


This parameter can be used in conjunction with the **[RefreshCondition](#refreshcondition)** to control which rows are selected for refresh.It influences the SQL query generated during refresh, for example:
SELECT * FROM <em>source</em> <em>join condition</em> WHERE <em>condition</em>

**Example:**

To join your source table column **src1** with column **ext1** in an external table **ext_tab**, the join condition might be:
INNER JOIN ext_tab ON {src1} = ext_tab.ext1

The **[RefreshCondition](#refreshcondition)** parameter can then reference the external table in a WHERE clause, for example:
ext_tab.other_column > 1000

> **Important:** 
- 
This parameter must not be used together with **[SliceCondition](#slicecondition)**.

- 
This parameter is supported only for SQL Server locations.

- 
This parameter applies only to the source side; it is ignored when specified for the target side.




---

### CompareJoinCondition


<strong>Since</strong> 6.2.5/5

**Argument**: *sql_expr*

**Description**: Defines a join condition to filter rows during a **[Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare)** operation. Only rows for which the SQL join expression *sql_expr* evaluates to TRUE are compared.

The SQL expression *sql_expr* can include the following substitution:

- **{***colname***}** - Replaced with the value of the current table's column *colname*.


> **Important:** 
- 
This parameter must not be used together with **[SliceCondition](#slicecondition)**.

- 
Filtering during **[Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare)** based on non-key columns may lead to inaccurate results. For example, if the restricted column has not yet been replicated to the target location when **[Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare)** starts, or if the restricted column is updated while an **[Online Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare#onlinecompare)** is running, mismatches may be missed.

- 
This parameter is supported only for SQL Server locations.

- 
This parameter applies only to the source side; it is ignored when specified for the target side.




---

### SliceCountCondition


**Argument**: *sql_expr*

**Description**: Defines a condition for performing slicing during [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#slicing) or [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#slicing). Only rows where the SQL expression *sql_expr* evaluates to TRUE are affected.

The SQL expression *sql_expr* can contain the following substitutions:

- 
**{hvr_slice_num}** contains current slice number (starting from **0**) if slicing is defined with a **Count** (option **-S***num*).

- 
**{hvr_slice_total}** contains total number of slices if slicing is defined with a **Count** (option **-S***num*).



> **Important:** 
- 
This parameter is allowed and required only for the **Count** (option *num*) type of slicing.

- 
It is recommended to define parameter [**Context**](#context) when using these substitutions so it can be easily disabled or enabled.




When using this parameter, it must be defined on both source and target locations. It can be defined using single or multiple action definition. When the sql expression is same on source and target location, a single action definition can be used, else multiple action definition is required.

If defined on the source side, it affects which rows are selected for refreshing or comparing (SELECT * FROM <em>source</em> WHERE <em>condition</em>).

If defined on the target side,

- 
during [**Bulk Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh#refreshtypes) it protects non–matching rows from bulk delete (DELETE FROM <em>target</em> WHERE <em>condition</em>, instead of just TRUNCATE <em>target</em>).

- 
during row–wise refresh it prevents some rows from being selected for comparison with the source rows (SELECT * FROM <em>target</em> WHERE <em>condition</em>).

- 
during compare it affects which rows are selected (SELECT * FROM <em>source</em> WHERE <em>condition</em>).



---

### SliceSeriesCondition


**Argument**: *sql_expr*

**Description**: Defines a condition for performing slicing during [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#slicing) or [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#slicing). Only rows where the SQL expression *sql_expr* evaluates to TRUE are affected.

The SQL expression *sql_expr* can contain only the following substitution:

- **{hvr_slice_value}** contains current slice value if slicing is defined with a **Series** of values (option **-S***v1*[**;***v2*]...[**;***vN*]).


> **Important:** 
- 
This parameter is allowed and required only for the **Series** (option *val1*[**;***val2*]...) type of slicing.

- 
It is recommended to define parameter [**Context**](#context) when using these substitutions so it can be easily disabled or enabled.




When using this parameter, it must be defined on both source and target locations. It can be defined using single or multiple action definition. When the syntax/sql expression is same on source and target location, single action definition can be used, else multiple action definition is required. The effect of this parameter depends on whether it is defined on the source or on the target side.

If defined on the source side, it affects which rows are selected for refreshing or comparing (SELECT * FROM <em>source</em> WHERE <em>condition</em>).

If defined on the target side,

- 
during [**Bulk Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh#refreshtypes) it protects non–matching rows from bulk delete (DELETE FROM <em>target</em> WHERE <em>condition</em>, instead of just TRUNCATE <em>target</em>).

- 
during [**Row-wise Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh#refreshtypes) it prevents some rows from being selected for comparison with the source rows (**select * from** *target* **where** *condition*).

- 
during compare it affects which rows are selected (SELECT * FROM <em>source</em> WHERE <em>condition</em>).



---

### HorizColumn


**Argument**: *col_name*

**Description**: Horizontal partitioning column. The contents of the column of the replicated table is used to determine the integrate address. If parameter [**HorizLookupTable**](#horizlookuptable) is also defined then the capture will join using this column to that table. If it is not defined then the column's value will be used directly as an integrate address. An integrate address can be one of the following:

- 
An integrate location name (e.g., **dec01**).

- 
A location group name containing integrate locations (e.g., **DECEN**).

- 
An alias for an integrate location, defined with [**AddressSubscribe**](#addresssubscribe) (e.g., **22**).

- 
A pattern to match one of the above (e.g., **dec***).

- 
A list of the above, separated by a semicolon, colon, or comma (e.g., **dec01,22**).



This parameter must be defined for trigger-based capture ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**). When used with trigger–based capture, this parameter does 'update conversion'. Update conversion is when (for example) an update changes a row which did satisfy a condition and makes it into a row that does not satisfy the condition; such an update would be converted to a delete. If however the update changes the row from not satisfying the condition to satisfying it, then the update is converted to an insert. No update conversion is done if this parameter is used with log–based capture.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


---

### HorizLookupTable


**Argument**: *tbl_name*

**Description**: Lookup table for value in column specified by parameter [**HorizColumn**](#horizcolumn). The lookup table should have a column which has the name of the [**HorizColumn**](#horizcolumn) parameter. It should also have a column named **hvr_address**. The capture logic selects rows from the lookup table and for each row found stores the change (along with the corresponding **hvr_address**) into the capture table. If no rows match then no capture is done. And if multiple rows match then the row is captured multiple times (for different destination addresses).

This parameter is supported only for trigger-based capture ([Capture_Method](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**).

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


A possible alternative for log–based capture channels is to define parameters [**AddressTo**](#addressto) and [**AddressSubscribe**](#addresssubscribe).

---

### DynamicHorizLookup


**Description**: Dynamic replication of changes to lookup table. Normally only changes to the horizontally partitioned table are replicated. This parameter causes changes to the lookup table to also trigger capture. This is done by creating extra rules/triggers that fire when the lookup table is changed. These rules/triggers are name *tbl***__li**, *tbl***__lu**, *tbl***__ld**.

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


Changes are replicated in their actual order, so for example if a transaction inserts a row to a lookup table and then a matching row to the main replicated table, then perhaps the lookup table's insert would not cause replication because it has no match (yet). But the other insert would trigger replication (because it now matches the lookup table row). This dynamic lookup table replication feature is suitable if the lookup table is dynamic and there are relatively few rows of the partitioned replicated table for each row of the lookup table. But if for example a huge table is partitioned into a few sections which each correspond to a row of a tiny lookup table then this dynamic feature could be expensive because an update of one row of the lookup table could mean millions of rows being inserted into the capture table. A more efficient alternative could be to perform a [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) whenever the lookup table is changed and use parameter [**RefreshCondition**](#refreshcondition) with pattern **{hvr_opposite_loc}** in the condition so that the [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) is aware of the partitioning.

This parameter is supported only for trigger-based capture ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**).

> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


A possible alternative for log–based capture channels is to define parameters [**AddressTo**](#addressto) and [**AddressSubscribe**](#addresssubscribe).

---

### AddressTo


**Argument**: *addr*

**Description**: Captured changes should only be sent to integrate locations that match integrate address *addr*. The address can be one of the following:

- 
An integrate location name (e.g., **dec01**).

- 
A location group name containing integrate locations (e.g., **DECEN**).

- 
An alias for an integrate location, defined with parameter [**AddressSubscribe**](#addresssubscribe). For example **22** or **Alias7**).

- 
A pattern to match one of the above (e.g., **dec***).

- 
A column name enclosed in braces like **{***column_name***}**. The contents of this column will be used as an integrate address. This is similar to parameter **/HorizColumn**.

- 
Since v6.1.5/5, a column name enclosed in braces with **%[literal]** argument like **{***column_name* **%[literal]}**. The exact contents of this column will be used as an integrate address without parsing it into a pattern since the **%[literal]** is used.

- 
A list of the above, separated by a semicolon, colon, or comma (e.g., **dec01,{col3}**).



This parameter should be defined with [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture). This parameter does not do 'update conversion'.

---

### AddressSubscribe


**Argument**: *addr*

**Description**: This integrate location should be sent a copy of any changes that match integrate address *addr*.

The address can be one of the following:

- 
A different integrate location name (e.g., **dec01**).

- 
A location group name containing other integrate locations (e.g., **DECEN**).

- 
A pattern to match one of the above (e.g., **dec***).

- 
An alias to match an integrate address defined with parameter [**AddressTo**](#addressto) or [**HorizColumn**](#horizcolumn) or matched by **{hvr_address}** in parameter [**Pattern**](https://fivetran.com/docs/hvr6/action-reference/capture#pattern) of action [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture). An alias can contain numbers, letters, and underscores (e.g., **22** or **Alias7**).

- 
A list of the above, separated by a semicolon, colon, or comma (e.g., **dec***, **CEN**).



This parameter should be defined with [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate).

---

### SelectDistinct


**Description**: Filter/ignore duplicate records by performing SELECT DISTINCT instead of SELECT during **Refresh** or **Compare**. This helps to avoid fatal errors caused by duplicate records during **Compare** (applicable only to S3 or HDFS with Hive external tables and failover).

This parameter should be enabled only if duplicate records are not relevant.

---

### Context


**Argument**: *context*

**Description**: Action **Restrict** is effective/applied only if the *context* matches the context defined in [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh). For more information about using Context, see our concept page [Refresh or Compare context](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).

The value should be a context name, specified as a lowercase identifier. It can also have form **!***context*, which means that the action is effective unless the matching *context* is enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

One or more contexts can be enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

Defining an action which is only effective when a context is enabled can have different uses. For example, if action **Restrict** with parameter [**RefreshCondition**](#refreshcondition)="**{id}>22**" and **Context**=**qqq** is defined, then normally all data will be compared, but if context **qqq** is enabled (**-Cqqq**), then only rows where **id>22** will be compared. Variables can also be used in the restrict condition (e.g., "**{id}>{hvr_var_min}**"). This means that **hvrcompare -Cqqq -Vmin**=**99** will compare only rows with **id>99**.

---

## Horizontal Partitioning


Horizontal partitioning means that different parts of a table should be replicated into different directions. Logic is added inside capture to calculate the destination address for each change, based on the row's column values. The destination is put in a special column of the capture table named **hvr_address**. Normally during routing each capture change is sent to all other locations which have a [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) action defined for that row, but this **hvr_address** column overrides this. The change is sent instead to only the destinations specified.

Column **hvr_address** can contain a location name (lowercase), a location group name (UPPERCASE) or an asterisk (*). An asterisk means send to all locations with [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) defined. It can also contain a comma-separated list of the above.

---

## Column Substitution


For DB2 for z/OS, when using the column substitution (**{***colname***}**) you must cast the column values to the exact data type, especially for string types like Char, Varchar, and CLOB.

For example, if the column (e.g., **column1**) has a type **varchar(10)**, using the substitution {column1}='ABC' may result in the **F_JD0274** error during capture. The correct substitution that you need to use is {column1}=varchar('ABC', 10). This ensures the expected behavior without encountering errors.

---

## Examples


This section provides examples of how to use the following parameters of the **Restrict** action - [**CaptureCondition**](#capturecondition), [**RefreshCondition**](#refreshcondition), [**AddressTo**](#addressto), and [**AddressSubscribe**](#addresssubscribe).
Example 1: Using CaptureCondition and RefreshCondition
To replicate only rows of table **product** having **id** between 1000000 and 2000000, use parameters **CaptureCondition** and **RefreshCondition**.



Also, only rows of table **order** for products which are in state 16 need to be captured. This is implemented with another **CaptureCondition** parameter.


Example 2: Using AddressTo and AddressSubscribe
This section describes the examples of using action **Restrict** with parameters [**AddressTo**](#addressto) and [**AddressSubscribe**](#addresssubscribe).

The following replication configuration is used:

- location group **SOURCE** having 1 source location **src**
- location group **TARGET** having 2 target locations **tgt1** and **tgt2**


Create table (**order**) on the source location:
CREATE TABLE order (
   id NUMBER PRIMARY KEY,
   subid NUMBER,
   name VARCHAR2(15),
   street VARCHAR2(15),
   address_to VARCHAR(20)
);

The **address_to** column will serve as a field for enforcing the restriction logic during replication, i.e. captured changes will be replicated to one of the target locations based on the values inserted in this column.

- Scenario 1
This example requires changes captured from location **src** to be replicated only to location **tgt1**. In this case, the integrate address is restricted by the content of the **AddressTo** parameter set to the **{address_to}** column defined on the source location **src** as shown in the screenshot below.



When value 'tgt1' is inserted in the **address_to** column on the source location, the change should be replicated only to target location **tgt1**.
INSERT INTO order VALUES (1, 1, 'Tester', 'Boardwalk', 'tgt1');

To verify that the change was replicated correctly, make a selection from both **tgt1** and **tgt2**.
SELECT * FROM tgt1.order;

Result:
        ID      SUBID NAME            STREET          ADDRESS_TO
---------- ---------- --------------- --------------- ----------
         1          1 Tester          Boardwalk       tgt1
SELECT * FROM tgt2.order;

Result:
no rows selected

- Scenario 2
This example requires changes captured from location **src** to be replicated to target group **TARGET**, but only to target location **tgt2**, even though location **tgt1** is also a part of **TARGET**. In this case, action **Restrict** with parameter **AddressTo** should be defined on **SOURCE** with value set to **{address_to}** and the integrate address is restricted by the content of the **AddressSubscribe** parameter set to alias **a** defined on the target location **tgt2** as shown in the screenshot below.



When value **a** is inserted in the **address_to** column on the source location, the change should be replicated only to target location **tgt2**, omitting **tgt1**:
INSERT INTO order VALUES (5, 5, 'Tester', 'Boardwalk', 'a');

To verify that the change was replicated correctly, make a selection from both **tgt1** and **tgt2**.
SELECT * FROM tgt2.order WHERE id = 8;

Result:
        ID      SUBID NAME            STREET          ADDRESS_TO
---------- ---------- --------------- --------------- ----------
         8          6 Tester          Boardwalk       a
SELECT * FROM tgt1.order WHERE id = 8;

Result:
no rows selected


Example 3: Using Subselect on Non-replicated Table in RefreshCondition
This is an example of using action **Restrict** with parameter [**RefreshCondition**](#REFRESHCONDITION) for updating key values from a source table to a target table based on a subset of values from a table in the source that is not included in the channel.

#### Prerequisites


- An Oracle-to-Oracle channel **mychannel** with the **product** table on both source and target locations.
- The **orders** table on the source location that is not in the channel.


#### Scenario


Suppose we need to update the values of the **prod_id** column in the **product** table with only values falling under a certain subset, such as 5, 10, 15, 20, and 25, from another non-replicated table **orders**. To achieve this, we will define a sub-query expression for the **RefreshCondition** parameter, that will select specific values from the **orders** table on the source even though this table is not in the channel definition.

#### Steps


- 
In the UI, define action **Restrict** on the source table:

a. On the [**Channel Details**](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details) page, click the **More Options** icon  in the top right menu and select **View Actions**.

b. In the [**Actions**](https://fivetran.com/docs/hvr6/user-interface/action-list) panel, click **Add Action** in the top-right menu and select **Restrict**.

c. In the **New Action: Restrict** dialog, select **RefreshCondition** and type in the following expression: **{prod_id} in (select prod_id from source.orders corr where corr.prod_id in (5, 10, 15, 20, 25))**. Click **OK**.



- 
In the top-right menu of the **Channel Details** page, click [**Refresh Data**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data).

- 
In the **Refresh Data** dialog, click the **Tables** tab and select the **product** table.

- 
Click the **Refresh Data** button at the bottom of the **Refresh Data** dialog.



When the [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) job starts, a notification appears at the top of the page. Click the **View Refresh event** link in the notification to open the [**Event Details**](https://fivetran.com/docs/hvr6/user-interface/events/event-details) page displaying detailed information about the [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) event.



.actparam {
    padding-left: 20px;
}
