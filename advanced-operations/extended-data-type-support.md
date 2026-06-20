# Extended Data Type Support - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/extended-data-type-support

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/extended-data-type-support/index.md)

# Extended Data Type Support


There are database-specific data types that are not natively supported by Fivetran HVR. These data types are called "extended data types" in HVR. Different extended data types need different capture and integrate expressions to be defined on a channel to convert them to the ones supported by HVR. Generally, a cast to a **varchar** or **clob** column works well, though some types might be better represented by a numeric data type. For nested object types, a stored procedure to serialize the object may be defined. For examples, see section [Expression Library](#expressionlibrary) below.

When a table with an extended data type is added to a channel, the [Table Details](https://fivetran.com/docs/hvr6/user-interface/tables/table-details) page displays the extended data types as a data type name enclosed in special markers: **<<***datatype***>>**. The *datatype* is the name of the data type as defined in a particular database and can be used in data type pattern matching similar to the regular data types. The following images shows the Oracle's **<<sdo_geometry>>** data type.


Advantages and Disadvantages
The primary advantage of the extended data type feature is that it allows HVR to access data types that are not supported, and also allows full flexibility to tune the use of otherwise unsupported or totally custom data types, even in heterogeneous replication scenarios. The downside includes performance costs and the requirement to add custom expressions.

- 
**Capture Performance**

Since HVR can not process the native representation of extended data types, there is a performance cost of capturing these types. For each row, HVR will need to do a query to the source database to augment in the value as a supported type. This also causes the consistency to change to eventual consistency since there will be a time discrepancy between the commit and the execution of the capture expression in the order of the capture latency.

Integration has no noticeable overhead.

- 
**Bulk Refresh Performance**

In general, during bulk refresh, HVR uses the bulk load APIs of the target database platform. These, however, require native support for all data types of the interface, and generally, do not allow expressions. If extended data types are present in a table, this table drops down to batched SQL statements for insertion.

Bulk compare or row-wise refresh and compare have no noticeable overhead.

- 
**Coercion**

HVR coerces data types from the source database to the target database, but can not do this for extended data types. However, HVR ensures that the data type returned by the capture expression is localized to a data type supported by the integrate location. It is the responsibility of the integrate expression to deal with possible incompatibilities that might result from interpreting a value. This means that actions like [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) with the **CoerceErrorPolicy** parameter only apply to the localization of the data type, not to the processing of the integrate expression.


Restrictions
- 
Executing capture expressions during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) requires a <strong>WHERE</strong> clause containing key information, so a key column with an extended data type cannot be used during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture).

- 
Extended data types cannot be used on a primary key column.


Using AdaptDDL with Extended Data Types
When using [**AdaptDDL**](https://fivetran.com/docs/hvr6/action-reference/adaptddl) in combination with extended data types, the following should be considered:

- Tables with extended data types require pre-defined expressions. If **AdaptDDL** adds tables to your channel without pre-defined expressions, the channel will fail. To avoid this, use parameter [**DataTypeMatch**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch) (in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties)) to define the expressions for data types that will be adapted in the future.
- There is a limitation when comparing extended data types. HVR does not assign meaning to the name the database gives the data type enclosed in markers **<< >>**. For comparison, HVR treats all extended data types as equal and cannot detect differences for updating channel definitions or executing <strong>ALTER TABLE</strong> statements on the target.


## Configuring Channel for Extended Data Types


Since extended data types are not natively supported, HVR cannot interpret them directly. To interpret these data types, you must define action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with specific parameters on the source and target locations. This will convert the extended data type into a native data type understandable by HVR, such as **varchar** or **number**.

The action parameters required for HVR to interpret the extended data types during [capture](https://fivetran.com/docs/hvr6/action-reference/capture), [integrate](https://fivetran.com/docs/hvr6/action-reference/integrate), [compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), and [refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), depend on the following use cases.

### Use Case 1


Source location has an extended data type that needs to be mapped to a native data type on the target location.
Channel configuration for capturing an extended data type
- To capture an extended data type, define action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameters **DatatypeMatch**, **CaptureExpression**, and **CaptureExpressionType**.
- To integrate into a native data type (that comes out of the **CaptureExpression=from_datatype({{hvr_col_name}})**), define action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameters **DatatypeMatch** and **Datatype**. No **IntegrateExpression** is needed since it integrates the data already present in the channel pipeline. The core conversion logic is handled by the capture expression.


The final action definition will be as follows.
 Group | Table | Action | Parameters |
 Source | * | [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) | [**DatatypeMatch**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch)**=<<***extended_datatype***>>** 
[**CaptureExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression)**=from_datatype({{hvr_col_name}})** 
[**CaptureExpressionType**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpressiontype)**=SQL_WHERE_ROW** |
 Target | * | [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) | [**DatatypeMatch**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch)=*native_datatype* 
[**Datatype**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatype)=*native_datatype* |

> **Important:** 
- 
For certain data types, you may need to define additional parameters. For example, parameter [**Length**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#length) must be defined for non-long string data types, such as **varchar**.

- 
The capture expression may vary depending on the database involved in the replication. See section [Expression Library](#expressionlibrary) below for the corresponding database-specific capture and integrate expressions.

- 
Ensure to set the [**Datatype**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatype) parameter on the target side only.





### Use Case 2


Source location has a native data type that needs to be mapped to an extended data type on target location.
Channel configuration to integrate into an extended data type
To integrate into an extended data type, HVR requires an integrate expression to translate the data from what was captured to the extended data type. Define action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameters **DatatypeMatch** and **IntegrateExpression**.

The final action definition will be as follows.
 Group | Table | Action | Parameters |
 Target | * | [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) | [**DatatypeMatch**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch)**=<<***extended_datatype***>>** 
[**IntegrateExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#integrateexpression)**=to_datatype({{hvr_col_name}})** |

> **Important:** 
- 
The integrate expression may vary depending on the database involved in the replication. See section [Expression Library](#expressionlibrary) below for the corresponding database-specific capture and integrate expressions.

- 
If a table with an extended data type needs to be created in the target location, you must define the [**Datatype**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatype) parameter along with the above parameters for the target location. For more information, see section [Creating Table with Extended Data Type on Target](#creatingtablewithextendeddatatypeontarget).





### Use case 3


Source location has an extended data type that needs to be mapped to an extended data type on target location.
Channel configuration to capture and integrate into extended data types
- To capture an extended data types, define action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameters **DatatypeMatch**, **CaptureExpression**, and **CaptureExpressionType**.
- To integrate into an extended data type, HVR requires an integrate expression to translate the data from what was captured to the extended data type. Define action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameters **DatatypeMatch** and **IntegrateExpression**.


The final action definition will be as follows.
 Group | Table | Action | Parameters |
 Source | * | [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) | [**DatatypeMatch**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch)**=<<***extended_datatype***>>** 
[**CaptureExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression)**=from_datatype({{hvr_col_name}})** 
 [**CaptureExpressionType**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpressiontype)**=SQL_WHERE_ROW** |
 Target | * | [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) | [**DatatypeMatch**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch)**=<<***extended_datatype***>>** 
[**IntegrateExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#integrateexpression)**=to_datatype({{hvr_col_name}})** |

> **Important:** 
- 
The capture and integrate expressions may vary depending on the database involved in the replication. See section [Expression Library](#expressionlibrary) below for the corresponding database-specific capture and integrate expressions.

- 
If a table with an extended data type needs to be created in the target location, you must define the [**Datatype**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatype) parameter along with the above parameters for the target location. For more information, see section [Creating Table with Extended Data Type on Target](#creatingtablewithextendeddatatypeontarget).





> **Note:** 
The **DatatypeMatch** parameter, in combination with the **{{hvr_col_name}}** pattern in capture and integrate expressions, allows you to define the expression based on the data type of the column rather than the column name. This parameter fully supports extended data types, enabling you to specify a single expression for all columns of a specific extended data type across all tables.


> **Note:** 
The **CaptureExpressionType** parameter automatically generates extra SQL required to run the specified capture expression against the table being replicated.

When **CaptureExpressionType=SQL_WHERE_ROW** is defined, HVR will:

- execute the capture expression once for each row,
- add a FROM clause for the table being replicated, and
- add a WHERE clause matching the key of the current row.


For example, **CaptureExpression=cast(col as varchar)** and **CaptureExpressionType=SQL_WHERE_ROW** instruct HVR to generate the following SQL expression:
select (cast(col as varchar)) from schema.table where key1=key1, ...


### Configuration steps


The following step-by-step instructions provide an example of how to configure a channel for capturing an extended data type, such as PostgreSQL's **interval**, and integrate it to a native data type, such as **varchar**.

- 
Define action **ColumnProperties** on a source location. On the [Channel Details](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details) page, click the **More Options** icon at the top right  and select **View Actions**. This will open the **Actions** panel.

- 
In the **Actions** panel, click the **Add Action** button and select **ColumnProperties**.

- 
In the **New Action: ColumnProperties** dialog, select the **SOURCE** location group.

- 
Select **DatatypeMatch** and type in **<<interval>>**.

- 
Select **CaptureExpression** and type in **cast({{hvr_col_name}} as varchar(100))**, which is the [PostgreSQL-specific](https://fivetran.com/docs/hvr6/advanced-operations/extended-data-type-support#postgresql) capture expression.

- 
Select the **CaptureExpressionType** parameter and choose **SQL_WHERE_ROW** from the drop-down list.

- 
Click **Save** to add the above action configuration to the source location.

- 
Define the **ColumnProperties** action on the target location. In the **Actions** panel, click the **Add Action** button and select **ColumnProperties**.

- 
In the **New Action: ColumnProperties** dialog, select the **TARGET** location group.

- 
Select **DatatypeMatch** and choose **varchar** from the drop-down list.

- 
Select **Datatype** and choose **varchar** from the drop-down list. Note that parameter **Length** must also be defined for non-long string data types.



The resulting channel configuration will be as follows:



### Creating Table with Extended Data Type on Target


In HVR, the extended data type defined as **<<***datatype***>>** is just a base name of a specific data type without any attributes such as **NOT NULL**, **DEFAULT**, or allowed values in enumeration-like data types. This may not be sufficient for creating a table on the target side.

If a table with an extended data type needs to be created in the target location, either during a [refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) or [integrate](https://fivetran.com/docs/hvr6/action-reference/integrate) (when action [**AdaptDDL**](https://fivetran.com/docs/hvr6/action-reference/adaptddl) with parameter [**AddTablePattern**](https://fivetran.com/docs/hvr6/action-reference/adaptddl#addtablepattern) is defined), you must define the **DataType** parameter with the necessary attributes on the target location. HVR will incorporate these attributes into the CREATE TABLE statement during the [refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) or [integrate](https://fivetran.com/docs/hvr6/action-reference/integrate).



The example configuration of action **ColumnProperties** that integrates into an extended data type may be as follows:
 Group | Table | Action/Parameters |
 Target | * | [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) 
  **DatatypeMatch=<<***extended_datatype***>>** 
  **IntegrateExpression=to_datatype({{hvr_col_name}})** 
  **DataType=<<***extended_datatype***(42) NOT NULL DEFAULT '(zero)'::***extended_datatype***>>** |

> **Important:** 
For limitations on action **AdaptDLL** in a channel with extended data types, see section [Using AdaptDDL with Extended Data Types](#usingadaptddlwithextendeddatatypes).


## Excluding Extended Data Types from Replication


To ignore replication of an extended data type enrolled in the table definitions of the HVR repository tables, define action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with the **Absent** parameter. Since the capture of columns with the **Absent** parameter requires a capture expression, you can use a dummy expression to satisfy that requirement. By adding the **CaptureExpression** parameter of type **SQL_PER_CYCLE**, the number of executions of this expression is reduced to one per cycle, mitigating the performance cost. This is useful when tables need to be enrolled as they are in the source database, especially when the target database cannot accommodate this data type.

 Group | Table | Action/Parameters |
 * | * | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**DatatypeMatch=<<***datatype***>>**
**CaptureExpression="0"**
**CaptureExpressionType=SQL_PER_CYCLE**
**Absent**
 |


## Expression Library


This section lists the capture and integrate expressions to be defined on a channel to convert the extended data types.

> **Important:** 
If the [**CaptureExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression) converts an extended data type on a source location to a generic data type that is supported on a target location, then the [**IntegrateExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#integrateexpression) is not required on the target location.

For example, if **CaptureExpression=cast({{hvr_col_name}} as char)** is defined on a MySQL source location for the **set** data type, the **IntegrateExpression** is not required on a Snowflake target location because Snowflake supports the **char** data type.


### MySQL


 Extended Data Type | Action/Parameters |
 set | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**CaptureExpression=cast({{hvr_col_name}} as char)**
**IntegrateExpression={{hvr_col_name}} **
 |
 enum | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** (source)

**CaptureExpression=coalesce(convert({{hvr_col_name}},char),'')**
**CaptureExpressionType=SQL_WHERE_ROW**

**[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)** (target)

**IntegrateExpression={{hvr_col_name}}**
**Datatype=varchar**
**Length=***x*

> **Important:** 
- 
**Datatype=varchar** is not required if the target table is defined with the correct enum data type on the corresponding column. If you are uncertain about the maximum length, **clob** can be used instead of **varchar**.

- 
The value defined in **Length** must be the same or greater than the length in the source table's column.

- 
Ensure to set the **Datatype** parameter on the target side only.



 |


### Oracle


 Extended Data Type | Action/Parameters |
 xmltype | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**CaptureExpression=xmltype.getClobVal({{hvr_col_name}})**
**IntegrateExpression=xmltype.createXml({{hvr_col_name}})**
 |
 SDO_GEOMETRY | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**CaptureExpression=SDO_UTIL.TO_WKTGEOMETRY({{hvr_col_name}})**
**IntegrateExpression=SDO_UTIL.FROM_WKTGEOMETRY({{hvr_col_name}})**
 |


### PostgreSQL


 Extended Data Type | Action/Parameters |
 interval | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**CaptureExpression=cast({{hvr_col_name}} as varchar(100))**
**IntegrateExpression=cast({{hvr_col_name}} as interval)**
 |


### SQL Server


 Extended Data Type | Action/Parameters |
 sql_variant | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**CaptureExpression=convert(nvarchar,{{hvr_col_name}}, 1)**
**IntegrateExpression=cast({{hvr_col_name}} as nvarchar)**

> **Important:** 
Using these expressions integrates each values with a **BaseType** of **nvarchar**.

 |
 geometry | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**CaptureExpression={{hvr_col_name}}.ToString()**
**IntegrateExpression=geometry::STGeomFromText({{hvr_col_name}},0)**
 |
 geography | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**CaptureExpression={{hvr_col_name}}.STAsText()**
**IntegrateExpression=geography::STGeomFromText({{hvr_col_name}},4326)**
 |
 hierarchyid | **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**

**CaptureExpression={{hvr_col_name}}.ToString()**
**IntegrateExpression=hierarchyid::Parse({{hvr_col_name}})**

> **Important:** 
Since 6.1.5/9, hierarchyid is supported as a native data type. As a result, it is no longer necessary to define actions for mapping hierarchyid as an extended data type; HVR can now directly map it without additional configuration.

 |

