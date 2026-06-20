# Compare - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/concepts/compare

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/concepts/compare/index.md)

# Compare


After you run the [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) job and the data replication process starts, you might want to verify that the data in source and target [locations](https://fivetran.com/docs/hvr6/getting-started/concepts/location) is in sync. For this, Fivetran HVR provides the **Compare** functionality, which allows you to compare data in two or more locations in a channel.

HVR supports comparing both database and file locations. For more information about comparing file locations, see the [Direct File Compare](#directfilecompare) section. You can compare a single source location with multiple target locations. Additionally, you can compare an entire database (all tables) or only specific tables. The **Compare** functionality compares both the table structures and the data they contain.

HVR also supports comparing data in heterogeneous DBMSes where source and target data types may not match and have different character encoding.
**Data Type Handling and Transformations**
When comparing data across different DBMSes or formats, HVR automatically handles differences in data types and character encoding between source and target location using coercion and transformation techniques.

HVR standardizes data types internally during comparison by coercing values to fit the internal representation. You can configure how HVR handles coercion errors in the channel definition using the [**CoerceErrorPolicy**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrorpolicy) and [**CoerceErrorType**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#coerceerrortype) parameters in the [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) action. By default, a coercion error results in a fatal error.

HVR also supports transformations using actions that control compare behavior. For example, you can use the [**CaptureExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#captureexpression) parameter in the [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) action to convert data to lowercase before comparison. You can apply transformations per table, location, channel, or installation.

> **Important:** 
When comparing between different DBMS types, ambiguity can occur due to data type coercions. Different systems interpret data types and values differently, which can lead to inconsistencies during comparison. HVR resolves this by applying the rules of the target location (also known as the "write" location), not the source (also known as "read") location. This ensures that comparison results match the behavior of the system receiving the data.

For example, Oracle treats an empty string and NULL as equivalent, while Ingres treats them as distinct. During replication, HVR may map an empty string in the Ingres (**ing**) location to a NULL in a varchar column in the Oracle (**ora**) location. During comparison, whether these values are considered identical or different depends on the comparison direction:

- When comparing from **ing** to **ora**, HVR uses Oracle’s rules and reports the tables as identical because Oracle treats empty strings and NULL as the same.
- When comparing from **ora** to **ing**, HVR uses Ingres’s rules and reports the tables as different because Ingres treats empty strings and NULL as distinct values.




> **Note:** 
You can run **Compare** using the following methods:

- via **UI** – see [Comparing Data](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data)
- via **CLI** – see [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare)
- via **REST API** – see **/api/latest/hubs/{hub}/channels/{channel}/compare** in [Activate, Refresh, and Compare Interface](https://fivetran.com/docs/hvr6/rest-api/rest-api-reference/610/6100/activate-refresh-and-compare).




## Compare Types


If your source table has been pre-populated with data, there are two types of **Compare** you can choose from:

- 
**Bulk Compare**: HVR calculates the checksum for each table in the channel and compares these checksum to report whether the replicated tables are identical.

- 
**Row-by-Row Compare**: HVR extracts the data from a source (read) location, compresses it, and transfers the data to a target (write) location(s) to perform a row level **Compare**. Each individual row is compared to produce a 'diff' result. For each detected difference, an SQL statement is written: an INSERT, UPDATE, or DELETE. This compare type is also referred to as **row-wise compare** in this documentation.



> **Important:** 
Bulk and online row-wise compare are not supported for packed SAP tables; only offline row-wise compare is available.


> **Note:** 
You can set a **Compare** type in the CLI using [**-g** option](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#g) of [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare) or in the UI enable **Bulk Compare** by selecting the [**Table Checksums Only**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#tablechecksumsonly) option.



## Online Compare


You can choose to perform online compare, which is a live **Compare** between locations with rapidly changing data. While performing a compare, if the online compare option is defined, HVR processes the changes that occur during the compare and does not miscount them as differences. You can define the online compare in CLI using [**-o** option](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#onlinecompare) of [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare) or in the UI by selecting the [**Online Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#onlinecompare) option.

## Direct File Compare


HVR also allows you to perform the **Compare** on the file locations using the **Direct File Compare** method, which is performed against a file location. This **Compare** method is a faster alternative for file compare via Hive External Tables and also helps to avoid compare mismatches caused by data type coercion through Hive deserializer.

During direct file **Compare**, HVR reads and parses (deserialize) files directly from the file location instead of using the HIVE external tables (even if it is configured for that location). In direct file compare, the files of each table are sliced and distributed to prereader subtasks. Each prereader subtasks reads, sorts, and parses (deserialize) the files to generate compressed(encrypted) intermediate files. These intermediate files are then compared with the database on the other side.

- 
The number of prereader subtasks used during direct file **Compare** can be configured using the compare option [File Prereaders per Table](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#fileprereaderspertable) (CLI [option **-w**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare#prereadersubtasks)).

- 
The location to store the intermediate files generated during **Compare** can be configured using the location property [Intermediate_Directory](https://fivetran.com/docs/hvr6/property-reference/location-properties#intermediatedirectory).



To perform a direct file compare:

- 
against a source file location, action [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) with parameter [**Pattern**](https://fivetran.com/docs/hvr6/action-reference/capture#pattern) should be defined.

- 
against a target file location, action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) with parameter [**ComparePattern**](https://fivetran.com/docs/hvr6/action-reference/integrate#comparepattern) should be defined.



### Limitations


Following are the direct file compare limitations:

- 
Direct file **Compare** does not support Avro, Parquet or JSON file formats.

- 
Direct file **Compare** is not supported if action [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) with parameter [**RefreshCondition**](https://fivetran.com/docs/hvr6/action-reference/restrict#refreshcondition) is defined on a file location involved in the compare.

- 
Direct file **Compare** is not supported when the channel is a 'blob' file channel. A blob file channel has no table information and simply treats each file as a sequence of bytes without understanding their file format.

- 
Direct file **Compare** for XML files requires each XML file to contain a single table.



## Slicing


Sometimes, the amount of data that the **Compare** job needs to process is too big. In this case, you can choose to divide the table into a few batches and process them in parallel. In HVR, this is achieved via the [**Slicing**](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing) functionality. By configuring **Slicing**, you can divide your database table into a few pieces that will be processed in parallel saving you a lot of time.

HVR suggests a few types of slicing, each fitting best for a specific business case. For more information about slicing types and when it is best to use them, refer to the [**Slicing**](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing) article.
