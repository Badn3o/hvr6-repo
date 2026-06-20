# TableProperties - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/tableproperties

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/tableproperties/index.md)

# TableProperties


Action **TableProperties** defines properties of a replicated table in a database location. The action has no effect other than that of its parameters. These parameters affect both replication (on the [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) and [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) side), [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), and [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data).

---

## Parameters


This section describes the parameters available for action **TableProperties**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from Fivetran HVR documentation, emails, or demo notes.




### BaseName


**Argument**: *tbl_name*

**Description**: Defines the actual name of the table in the database location, as opposed to the table name that HVR has in the channel.

This parameter is needed if the [base name](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/table-name-and-base-name) of the table is different in the capture and integrate locations. In that case, the table name in the HVR channel should have the same name as the 'base name' in the capture database and parameter **BaseName** should be defined on the integrate side. An alternative is to define the parameter **BaseName** on the capture database and have the name for the table in the HVR channel the same as the base name in the integrate database.

This parameter  is also necessary if different tables have the same table name in a database location but have different owners (parameter [**Schema**](#schema)). Or if a table's base name is not allowed as an HVR name, for example, if it contains special characters or if it is too long.

If this parameter is not defined then HVR uses the base name column (this is stored in the **tbl_base_name** column of the [**HVR_TABLE**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrtable) repository table. The concept of the 'base name' in a location as opposed to the name in the HVR channel applies to both columns and tables, see parameter [**BaseName**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#basename) in [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties).

Parameter **BaseName** can also be defined for file locations (to change the name of the table in XML tag) or for Salesforce locations (to match the Salesforce API name).

---

### Absent


**Description**: Table does not exist in database. For example, this parameter can be defined if a table needs to be excluded from one integrate location but included in another integrate location for a channel with parallel integration jobs.

---

### NoDuplicateRows


**Description**: Replication table cannot contain duplicate rows. This parameter only has effect if no replication key column(s) is defined for the [**HVR_COLUMN**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrcolumn) repository table. If no replication key column(s) are defined on the table and this parameter is not set, then all updates are treated as key updates and are replicated as a delete and an insert. Additionally, in [continuous mode](https://fivetran.com/docs/hvr6/action-reference/integrate#method), each delete is integrated using a special SQL subselect that ensures only a single row is deleted, not multiple rows. In [burst mode](https://fivetran.com/docs/hvr6/action-reference/integrate#method), the deletion of a row will process all rows with the respective key values.

---

### Schema


**Argument**: *schema*

**Description**: Name of database schema or user who owns the base table. By default, the base table is assumed to be owned by the database username that HVR uses to connect to the database.

---

### CoerceErrorPolicy


**Argument**: *policy*

**Description**: Defines a *policy* to handle type coercion error (an error that occurs while converting a value from one data type to a target data type). This *policy* typically affects all types of coercion errors, unless parameter [**CoerceErrorType**](#coerceerrortype) is defined in the same action. Multiple actions with parameter **CoerceErrorPolicy** can be defined to apply different policies to different coercion error types.
Expand to see the options available for this parameter
Available options for *policy* are:

- 
**FATAL** default: The replication job fails and displays an error message mentioning the table and column name where the bad values are encountered.

- 
**SILENT**: The bad value is silently (without notification) coerced/replaced with a value that is legal. The coercion details are not written into the job's log file. For details about how bad values are replaced/coerced, see [**CoerceErrorType**](#coerceerrortype) below.

- 
**WARNING**: A warning message is written into the job's log file. The warning message contains the table and column name, the type of coercion (see [**CoerceErrorType**](#coerceerrortype) below), and the number of rows affected.

- 
**WARNING_FILE**: The rows with bad values and the values in the key columns are written into a binary file (with extension **.coererr**) on the hub machine and also a warning message is written into the job's log file. This warning contains the table and column name, the type of coercion (see [**CoerceErrorType**](#coerceerrortype) below), the number of rows affected, and the binary file name. The binary file has the same format as HVR transaction files. To view its contents, use command [**hvrrouterview**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrouterview):
hvrrouterview hub chn $HVR_CONFIG/router/hub/chn/coerceerror/YYYYMMDD/YYYYMMMDDHHmmSS-jobname.coererr

> **Important:** 
Capture from CSV returns a different **.coererr** binary file. It contains **hvr_file_name** column (the CSV file name), **hvr_line_num** column (number of the row where HVR encountered the bad value), and the columns populated with bad values. Columns with the correct values are not included.




---

### CoerceErrorType


**Argument**: *types*

**Description**: Defines which types of coercion errors are affected by the parameter [**CoerceErrorPolicy**](#coerceerrorpolicy).

If only [**CoerceErrorPolicy**](#coerceerrorpolicy) is defined (without **CoerceErrorType**), all coercion error types listed below are affected by default. When multiple *types* are selected, it should be a comma-separated list.
Expand to see the options available for this parameter
Available options for *types* are:

- 
**NUMERIC_RANGE**: When the value exceeds the minimum or maximum value allowed in the target numeric data type and the [**CoerceErrorPolicy**](#coerceerrorpolicy) is not **FATAL**, the bad value will be replaced with the minimum or maximum legal value.

- 
**DATE_RANGE**: When the value exceeds the minimum or maximum value allowed in the target date data type and the [**CoerceErrorPolicy**](#coerceerrorpolicy) is not **FATAL**, the bad value will be replaced with the minimum or maximum legal value.

- 
**STRING_TRUNCATION**: When the value exceeds the number of bytes or characters allowed in the target string data type and the [**CoerceErrorPolicy**](#coerceerrorpolicy) is not **FATAL**, the bad value will be replaced with a truncated value.

- 
**ROUNDING**: When the value’s precision exceeds the precision allowed in the target date data type (dates and timestamps), and [**CoerceErrorPolicy**](#coerceerrorpolicy) is not **FATAL**, the bad value will be rounded ([rounding toward zero/truncate](https://en.wikipedia.org/wiki/Rounding#Rounding_toward_zero)) to a legal value. However, for numbers or decimals, values beyond the precision are always truncated silently, regardless of the policy selected in [**CoerceErrorPolicy**](#coerceerrorpolicy).

- 
**ENCODING**: When invalid sequences are encountered during encoding from source to target string data type and the [**CoerceErrorPolicy**](#coerceerrorpolicy) is not **FATAL**, the sequence will be sanitized with a replacement sequence.

- 
**NULLS**: When a null value is encountered for non-nullable target data type and the [**CoerceErrorPolicy**](#coerceerrorpolicy) is not **FATAL**, the bad value will be replaced with a default value (zero or an empty string depending on the data type).

- 
**OTHER**: Anything that does not match any of the above *types* (e.g., non-number string '**hello**' being coerced to a target numeric data type), and the [**CoerceErrorPolicy**](#coerceerrorpolicy) is not **FATAL**, this will be replaced with NULL or a default value (zero or empty string) depending on the data type.



> **Important:** 
After adding parameter **CoerceErrorType** to a capture location, [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) must be run with options [**Jobs**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication#jobs) and [**Table Enrollment**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication#tableenrollment) to make the change effective.


---

### SapUnpackErrorPolicy


**Argument**: *policy*

**Description**: Defines a *policy* to handle type coercion error during SapUnpack (when parameter [**SapUnpack**](https://fivetran.com/docs/hvr6/action-reference/transform#sapunpack) in action [**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform) is defined). Type coercion error is an error that occurs while converting a value from one data type to a target data type.

This *policy* typically affects all types of coercion errors, unless parameter [**CoerceErrorType**](#coerceerrortype) is defined in the same action. Multiple actions with [**CoerceErrorPolicy**](#coerceerrorpolicy) can be defined to apply different policies to different coercion error types.
Expand to see the options available for this parameter
Available options for *policy* are:

- 
**FATAL** default: The replication job fails and displays an error message mentioning the table and column name where the bad values are encountered.

- 
**SILENT** : The bad value is silently (without notification) coerced/replaced with a value that is legal. The coercion details are not written into the job's log file. For details about the how bad values are replaced/coerced, see the description for parameter [**CoerceErrorType**](#coerceerrortype).

- 
**WARNING** : A warning message is written into the job's log file. The warning message contains the table and column name, the type of coercion (see [**CoerceErrorType**](#coerceerrortype)), and the number of rows affected.

- 
**WARNING_FILE** : The rows with bad values and the values in the key columns are written into a binary file (with extension **.coererr**) on the hub machine and also a warning message is written into the job's log file. This warning contains the table and column name, the type of coercion (see [**CoerceErrorType**](#coerceerrortype)), the number of rows affected, and the binary file name. The binary file has the same format as HVR transaction files. To view its contents, use [**Hvrrouterview**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrouterview) command:
hvrrouterview hub chn $HVR_CONFIG/router/hub/chn/coerceerror/YYYYMMDD/YYYYMMMDDHHmmSS-jobname.coererr



> **Important:** 
This parameter is required to convert source data using SAP dictionary meta-data.


---

### PackedInside


**Description**: Name of the SAP database table that holds the data for the pool or cluster table being unpacked. Action **TableProperties** with this parameter is defined automatically when adding a pool or cluster table using a SAP data-source.

> **Important:** 
- 
Manually changing the value in this parameter or deleting this action definition will make the SAP table invalid in the channel.

- 
This parameter is required to unpack the SAP tables using parameter [**SapUnpack**](https://fivetran.com/docs/hvr6/action-reference/transform#sapunpack) in action [**Transform**](https://fivetran.com/docs/hvr6/action-reference/transform).




---

### TrimWhiteSpace


**Description**: Remove trailing whitespace from **varchar**.

---

### TrimTime


**Argument**: *policy*

**Description**: Trim **time** when converting **date** from Oracle and SQL Server.

Available options for *policy* are:

- 
**YES**: Always trim **time**

- 
**NO** default: Never trim **time**

- 
**MIDNIGHT**: Only trim if value has **time** as **00:00:00**



---

### MapEmptyStringToSpace


**Description**: Convert empty Ingres or SQL Server **varchar** values to an Oracle **varchar2** containing a single space and vice versa.

---

### MapEmptyDateToConstant


**Argument**: *date*

**Description**: Convert between Ingres empty date and a special constant *date*. Value *date* must have form *DD***/***MM***/***YYYY*.

---

### CreateUnicodeDatatypes


**Description**: On table creation use Unicode data types for string columns. For example, map **varchar** to **nvarchar**

---

### DistributionKeyLimit


**Argument**: *int*

**Description**: Maximum number of columns in the implicit distribution key.

The default value is **1** (just one column). Value **0** means all key columns (or regular columns) can be used.

A table's distribution key can be set explicitly or implicitly. An explicit distribution key can be set by clicking the checkboxes in the table's dialog, or by defining parameter [**DistributionKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#distributionkey) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties). If no explicit distribution key is defined, then HVR uses the implicit distribution key rule. The implicit rule is to use the first N columns; either from the replication key, or (if the table has no replication key) from the regular columns which do not have a LOB data type.

Some DBMSes (such as Redshift) are limited to only one distribution key column.

---

### DistributionKeyAvoidPattern


**Argument**: *patt*

**Description**: Avoid putting given columns in the implicit distribution key. For a description of the implicit distribution key, see parameter [**DistributionKeyLimit**](#distributionkeylimit) above.

The default value is **''** (no column is avoided).

If this parameter is defined then HVR will avoid adding any columns whose name matches the implicit distribution key. For example, if a table has replication key columns (**k1 k2 k3 k4**) and action parameters **DistributionKeyAvoidPattern**=**'k2|k3'** and [**DistributionKeyLimit**](#distributionkeylimit)=**2** are defined, then the implicit distribution key would be (**k1 k4**). However, if these parameters are defined as **DistributionKeyAvoidPattern**=**'k2|k3'** and [**DistributionKeyLimit**](#distributionkeylimit)=**4**, then the implicit distribution key would be (**k1 k2 k3 k4**).

For SAP databases, column **'mandt'** is often constant, so parameter **DistributionKeyAvoidPattern**=**mandt** should be used.

---

### CharacterMapping


**Argument**: *rules*

**Description**: Allows to replace some characters (potentially unsupported) in string columns with a replacement sequence. Value *rules* should be a semicolon-separated list of elements, each with form *char***>***chars*. Each *char* be a literal character or have form **\n**, **\r**, **\t**, **\\**, **\x***NN*, **\u***NNNN*, **\U***NNNNNNN* (where *N* is a hex digit). Example;**"\n>\\n;\r>\\r;\x00>\\0"**.

> **Important:** 
The mapping is performed during integration, [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) and [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), so the HVR **Compare** does not show an earlier mapping as a difference.


---

### MapBinary


**Argument**: *policy*

**Description**: Controls the way binary columns are mapped to a string.

This parameter is relevant only if either of the following is true:

- 
the location does not support any binary data type (e.g., Redshift) or

- 
if action [**FileFormat**](https://fivetran.com/docs/hvr6/action-reference/fileformat) with parameter [**Csv**](https://fivetran.com/docs/hvr6/action-reference/fileformat#csv) or [**Json**](https://fivetran.com/docs/hvr6/action-reference/fileformat#json) is defined for the location or

- 
a binary column is explicitly mapped to a string column using parameters [**DatatypeMatch**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatypematch) and [**Datatype**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#datatype) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties).



Available options for *policy* are:

- 
**COPY** (default for CSV and databases): Memory copy of the binary data. This can cause invalid characters in the output.

- 
**HEX**: The binary value is represented as HEX string.

- 
**BASE64** (default for Json): The binary value is represented as Base64 string.



---

### MissingRepresentationString


File  Kafka

**Argument**: *str*

**Description**: Inserts value *str* into the string data type column(s) if the value is missing/empty in the respective column(s) during integration. The value *str* defined here should be a valid input for the column(s) in target database.

When parameter [**MissingRepresentationNumeric**](#missingrepresentationnumeric) or [**MissingRepresentationDate**](#missingrepresentationdate) is used without defining **MissingRepresentationString** then a default value (for example, an empty string) is inserted into the string data type column(s) in which the value is missing/empty.

Defining **MissingRepresentationString** enables HVR to use parameter [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) without requiring supplemental logging all.

---

### MissingRepresentationNumeric


File  Kafka

**Argument**: *str*

**Description**: Inserts value *str* into the numeric data type column(s) if the value is missing/empty in the respective column(s) during integration. The value *str* defined here should be a valid input for the column(s) in target database.

When parameter [**MissingRepresentationString**](#missingrepresentationstring) or [**MissingRepresentationDate**](#MissingRepresentationDate) is used without defining **MissingRepresentationNumeric** then a default value (e.g., 0) is inserted into the numeric data type column(s) in which the value is missing/empty.

Defining **MissingRepresentationNumeric** enables HVR to use parameter [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) without requiring supplemental logging all.

---

### MissingRepresentationDate


File  Kafka

**Argument**: *str*

**Description**: Inserts value *str* into the date data type column(s) if the value is missing/empty in the respective column(s) during integration. The value *str* defined here should be a valid input for the column(s) in target database.

When parameter [**MissingRepresentationString**](#missingrepresentationstring) or [**MissingRepresentationNumeric**](#missingrepresentationnumeric) is used without defining **MissingRepresentationDate** then a default value is inserted into the date data type column(s) in which the value is missing/empty.

Defining parameter **MissingRepresentationNumeric** enables HVR to use parameter [**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey) in action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) without requiring supplemental logging all.

---

### PartitionByDate


Google BigQuery

**Description**: Enables partitioning by date for Google BigQuery tables.

Google BigQuery allows to [partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables) by date, ingestion time, or integer range. Defining this parameter allows to use date partitioning by default. For other partitioning flavors, use parameter [**RefreshTableCreateClause**](https://fivetran.com/docs/hvr6/action-reference/dbobjectgeneration#refreshtablecreateclause) in action [**DbObjectGeneration**](https://fivetran.com/docs/hvr6/action-reference/dbobjectgeneration).

---

### BQClusterKeys


Google BigQuery

**Argument**: *col_name*

**Description**: Creates Google BigQuery clustered tables.

Google BigQuery allows to create [clustered tables](https://cloud.google.com/bigquery/docs/clustered-tables). This automatically organizes data based on the contents of one or more columns in the table's schema.

When multiple *col_name* are supplied, it should be a comma-separated list. For example, *column1,column2,column3*.

Google BigQuery limits the maximum number of supported clusters. For more information, refer to [Google BigQuery documentation](https://cloud.google.com/bigquery/docs/creating-clustered-tables#limitations).

---

### TransientTable


<b>Since</b> v6.2.5/1   Snowflake

**Description**: Creates Snowflake [transient tables](https://docs.snowflake.com/en/user-guide/tables-temp-transient).

The tables selected within the action scope are created as transient tables in the target Snowflake location.

This parameter applies only to newly created tables and tables re-created due to schema changes.

This parameter is visible only if your channel contains a Snowflake location.

---

### Context


**Argument**: *context*

**Description**: Action **TableProperties** is effective/applied only if the *context* matches the context defined in [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh). For more information about using Context, see our concept page [Refresh or Compare context](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).

The value should be a context name, specified as a lowercase identifier. It can also have the form **!***context*, which means that the action is effective unless the matching *context* is enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

One or more contexts can be enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

Defining an action that is only effective when the context is enabled can have different uses. For example, if action **TableProperties** with parameters **BaseName=other_name** and **Context=diff_base** is defined, then normally the default base name is used, but if context **diff_base** is enabled (**–C diff_base**), then the base name **other_name** is used.

.actparam {
    padding-left: 20px;
}
