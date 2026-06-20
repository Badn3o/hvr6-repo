# FileFormat - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/fileformat

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/fileformat/index.md)

# FileFormat


Action **FileFormat** can be used on file locations (including HDFS and S3) and on Kafka locations.

- 
For file locations, it controls how Fivetran HVR reads and writes files. The default format for file locations is our [own XML format](#hvrxmlformat).

- 
For Kafka, it controls the format of each message. By default, the Kafka location sends messages to the Kafka broker in JSON format, unless the location property [**Kafka_Schema_Registry**](https://fivetran.com/docs/hvr6/property-reference/location-properties#kafkaschemaregistry) is defined, in which case each message uses Kafka Connect's compact Avro-based format. Note that this is not a true Avro because each message would not be a valid Avro file (e.g., no file header). Rather, each message is a 'micro Avro', containing fragments of data encoded using Avro's data type serialization format. Both JSON (using mode SCHEMA_PAYLOAD, see parameter [**JsonMode**](#jsonmode) below) and the 'micro AVRO' format conform to Confluent's 'Kafka Connect' message format standard. The default Kafka message format can be overridden by parameter such as [**Xml**](#xml), [**Csv**](#csv), [**Avro**](#avro), [**Json**](#json) or [**Parquet**](#parquet).



A custom format can be defined by using parameters [**CaptureConverter**](#captureconverter) or [**IntegrateConverter**](#integrateconverter). Many parameters only have effect if the channel contains table information; for a 'blob file channel' the jobs do not need to understand the file format.

> **Important:** 
- 
If this action is defined on a specific table, then it affects all tables in the same location.

- 
Defining more than one file format ([**Xml**](#xml), [**Csv**](#csv), [**Avro**](#avro), [**Json**](#json) or [**Parquet**](#parquet)) for the same file location using this action is not supported, i.e., defining different file formats for each table in the same location is not possible. For example, if one table has the file format defined as [**Xml**](#xml) then another table in the same location cannot have [**Csv**](#csv) file format defined.




---

## Parameters


This section describes the parameters available for action **FileFormat**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from Fivetran HVR documentation, emails, or demo notes.




### Xml


**Description**: Read and write files as [HVR's XML format](#hvrxmlformat). This parameter is applicable only for the channels with table information; not a 'blob file'.

---

### Csv


**Description**: Read and write files as Comma-separated values (CSV) format. This parameter is applicable only for the channels with table information; not a'blob file'.

---

### Avro


**Description**: Transforms the captured rows into Avro format during [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate).

An Avro file contains the schema defining data types in JSON and a compact binary representation of the data. See [Apache Avro documentation](https://avro.apache.org/docs/1.8.1/spec.html#schemas) for the detailed description of schema definition and data representation.
Expand for more information
Avro supports both primitive and [logical data types](https://avro.apache.org/docs/1.8.1/spec.html#Logical+Types). The normal way to represent Avro file in human-readable format is by converting it to JSON using the [Apache Avro tools](https://avro.apache.org/docs/1.8.1/gettingstartedjava.html). However, there is a limitation in representing **decimal** values using standard Avro tools utilities. The **decimal** type in Avro is supported as a logical type and is defined in the Avro schema file as follows:
{
  "type": "bytes",
  "logicalType": "decimal",
  "precision": precision,
  "scale": scale
}

Where, precision is the total number of digits in the number and scale is the number of digits after the decimal point.

The **decimal** logical type represents an arbitrary-precision signed decimal number of the form **unscaled** **× 10-scale**. For example, value **1.01** with a precision of **3** and scale of **2**, is represented as **101**.

The **decimal** values are encoded as a sequence of bytes in Avro. In their JSON representation, **decimal** values are displayed as an unreadable string instead of human-readable values.

When using Hive (Hive external table) to read Avro files, the **decimal** data type is displayed properly.

For example:

A source table is defined as follows:
CREATE TABLE dec (c1 NUMBER(10,2), c2 NUMBER(10,4));

where, the column **c1** stores a decimal value with precision **10** and scale **2**, and the column **c2** stores a decimal value with precision **10** and scale **4**.

If we insert values (1, 1) into the **dec** table and select them from the table, we expect to see (1, 1) as an output. But Avro format uses the specified scales and represents them in binary format as 100 (1.00) in column c1 and 10000 (1.0000) in column c2. According to the JSON specification, a binary array is encoded as a string. JSON will display these values as "d" (wherein "d" is 100 according to ASCII ) and "**'**\x10" (wherein 10000 is 0x2710, and 0x27 is **'** according to the ASCII encoding).

> **Note:** 
Formats like [**Parquet**](#parquet) with [**ParquetVersion**](#parquetversion)**=v2** or **v3**, [**Json**](#json) with [**JsonMode**](#jsonmode)**=SCHEMA_PAYLOAD** uses the same rules to encode decimal data types.


---

### Json


**Description**: Transforms the captured rows into JSON format during [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate). The content of the file depends on the value for parameter [**JsonMode**](#jsonmode).

---

### Parquet


**Description**: Transforms the captured rows into Parquet format during [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate).

---

### Compact


**Description**: Write compact XML tags like **<r>** & **<c>** instead of **<row>** and **<column>**. This parameter can be used only if [**Xml**](#xml) is selected.

---

### Compress


**Argument**: algorithm_

**Description**: HVR will compress files while writing them, and uncompress them while reading.

Available options for *algorithm* are:

- **GZIP**
- **LZ4**


The file suffix is ignored but when integrated, a suffix can be added to the files by defining action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) with parameter [**RenameExpression**](https://fivetran.com/docs/hvr6/action-reference/integrate)**="{hvr_cap_filename}.gz"**.

This parameter is not supported for [**Avro**](#avro) and [**Parquet**](#parquet).

---

### Encoding


**Argument**: *encoding*

**Description**: Encoding for reading or writing files.

Available options for *encoding* are:

- **US-ASCII**
- **ISO-8859-1**
- **ISO-8859-9**
- **WINDOWS-1251**
- **WINDOWS-1252**
- **UTF-8**
- **UTF-16LE**
- **UTF-16BE**


---

### HeaderLine


**Description**: First line of CSV file contains column names.

---

### FieldSeparator


**Argument**: *str_esc*

**Description**: Field separator for CSV files.

The **default** value for this parameter is comma (**,**).

Note that only a single Unicode glyph is supported as a separator for this parameter.

Examples: **,** **\x1f** or **\t**.

This parameter can be used only if the parameter [**Csv**](#csv) is selected.

---

### LineSeparator


**Argument**: *str_esc*

**Description**: Line separator for CSV files.

The **default** value for this parameter is newline (**\n**).

Examples: **;\n** or **\r\n**

This parameter can be used only if the parameter [**Csv**](#csv) is selected.

> **Important:** 
HVR only supports single-byte line separators for CSV sources.


---

### QuoteCharacter


**Argument**: *str_esc*

**Description**: Character to quote a field with, if the fields contains separators.

The **default** value for this parameter is double quotes (**"**).

This parameter can be used only if the parameter [**Csv**](#csv) is selected.

---

### EscapeCharacter


**Argument**: *str_esc*

**Description**: Character to escape the quote character with.

The **default** value for this parameter is double quotes (**"**).

This parameter can be used only if the parameter [**Csv**](#csv) is selected.

---

### FileTerminator


**Argument**: *str_esc*

**Description**: File termination at end-of-file.

Example: **EOF** or **\xff**.

This parameter can be used only if the parameter [**Csv**](#csv) is selected.

---

### NullRepresentation


**Argument**: *str_esc*

**Description**: String representation for column with NULL value.

Note that Hive 'deserializers' recognize **\N** as NULL when reading a CSV file back as an SQL row, this can be configured by setting this parameter to **\\N**".

Example: **\\N**

This parameter can be used only if the parameter [**Csv**](#csv) is selected.

---

### JsonMode


**Argument**: *mode*

**Description**: Style used to write row into JSON format.
Expand to see the options available for this parameter
Available options for *mode* are:

- 
**ROW_FRAGMENTS**: This format is compatible with Hive and BigQuery deserializers. Note that this option produces an illegal JSON file as soon as there is more than one row in the file.
Example:
{ "c1":44, "c2":55 }
{ "c1":66, "c2":77 }

- 
**ROW_ARRAY**:
Example:
[
  { "c1":44, "c2":55 },
  { "c1":66, "c2":77 }
]

- 
**TABLE_OBJECT** (defaultJSON mode for all location types except for Kafka):
Example:
{
  "tab1":[
    { "c1":44, "c2":55 },
    { "c1":66, "c2":77 }
  ]
}

- 
**TABLE_OBJECT_BSON**: This format is the same as **TABLE_OBJECT**, but in BSON format (binary). Note that a BSON file cannot be bigger than 2GB. This makes this format inapplicable for some tables (e.g., when LOB values are present).

- 
**TABLE_ARRAY**: This mode is useful if parameter [**RenameExpression**](https://fivetran.com/docs/hvr6/action-reference/integrate#renameexpression) in action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) does not contain a substitution which depends on the table name and when the location class is not Kafka.
Example:
[
  {
    "tab1":[
      { "c1":44, "c2":55 },
      { "c1":66, "c2":77 }
    ]
  },
  {
    "tab2":[
      { "c1":88, "c2":99 }
    ]
  }
]

- 
**SCHEMA_PAYLOAD** (defaultJSON mode for Kafka): This format is compatible with Apache Kafka Connect deserializers. Note that this option produces an illegal JSON file as soon as there is more than one row in the file.
Example:
{ 
  "schema": { 
    "type": "struct", 
    "name": "tab1", 
    "fields": [
      { "name": "c1", "type": "int" },
      { "name": "c2", "type": "int" }
    ]
  }, 
  "payload": { "c1": 44, "c2": 55 }
}
{ 
  "schema": { 
    "type": "struct", 
    "name": "tab1", 
    "fields": [
      { "name": "c1", "type": "int" },
      { "name": "c2", "type": "int" }
    ]
  }, 
  "payload": { "c1": 66, "c2": 77 }
}



This parameter can be used only if the parameter [**Json**](#json) is selected.

---

### BlockCompress


**Argument**: *algorithm*

**Description**: Compression *algorithm* for [**Avro**](#avro) and [**Parquet**](#parquet). This parameter sets the native compression algorithm supported by these file formats.

Available options for *algorithm* are:

- 
**NONE**
This option can be used with [**Avro**](#avro) and [**Parquet**](#parquet).

- 
**DEFLATE**
This option can be used only with [**Avro**](#avro). Also, this is the default compression method for [**Avro**](#avro) if **BlockCompress** is not defined.

- 
**GZIP**
This option can be used only with [**Parquet**](#parquet). This is the default compression method for [**Parquet**](#parquet) if **BlockCompress** is not defined.

- 
**LZ4**
This option can be used only with [**Parquet**](#parquet). Mapped internally to **LZ4_RAW**.

> **Note:** 
The original **LZ4** format is deprecated and not used. If you select **LZ4**, HVR automatically uses **LZ4_RAW** in the output file.




This parameter can be used only if the parameter [**Avro**](#avro) or [**Parquet**](#parquet) is selected.

---

### AvroVersion


**Argument**: *version*

**Description**: Version of Avro format. Available options for *version* are:

- 
**v1_6**: This version supports only the following basic types: **Boolean**, **int** (32-bit size), **long** (64-bit size), **float**, **double**, **bytes**, and **string**.

- 
**v1_7**: This version supports only the following basic types: **Boolean**, **int** (32-bit size), **long** (64-bit size), **float**, **double**, **bytes**, and **string**.

- 
**v1_8** (default): This version supports the above mentioned basic types and the following logical types: **decimal**, **date**, **time** and **timestamp** (with micro and millisecond resolutions), and **duration**.



This parameter can be used only if the parameter [**Avro**](#avro) is selected.

---

### PageSize


**Description**: Parquet page size in bytes.

**Default** value is 1MB.

This parameter can be used only if the parameter [**Parquet**](#parquet) is selected.

---

### RowGroupThreshold


**Description**: Maximum row group size in bytes for Parquet.

This parameter can be used only if the parameter [**Parquet**](#parquet) is selected.

---

### ParquetVersion


**Argument**: *version*

**Description**: Category of data types to represent complex data into Parquet format.

- 
**v1** : Supports only the basic data types - **boolean**, **int32**, **int64**, **int96**, **float**, **double**, **byte_array** to represent any data. The logical data types **decimal** and **date/time** types are not supported. However, **decimal** is encoded as **double**, and **date/time** types are encoded as **int96**.

- 
**v2** (default): Supports all basic data types and one logical data type (**decimal**). The **date/time** types are encoded as **int96**. This is compatible with Hive, Impala, Spark, and Vertica.

- 
**v3** : Supports basic data types and logical data types - **decimal**, **date**, **time_millis**, **time_micros**, **timestamp_millis**, **timestamp_micros**.



> **Important:** 
- 
For Hive, the **date/time** data type is encoded as **int96**. So, for Hive with **date/time** in source, only **v1** or **v2** can be used.

- 
For more information about parquet data types, refer to [Parquet Documentation](https://parquet.apache.org/docs/).




This parameter can be used only if the parameter [**Parquet**](#parquet) is selected.

---

### BeforeUpdateColumns


File/FTP/SFTP   Kafka

**Argument**: *prefix*

**Description**: By default, HVR captures an UPDATE operation as two rows: one for the 'before' version and one for the 'after' version of a row. This parameter merges these rows into a single row during an UPDATE operation and adds the *prefix* to the 'before' version columns.

For example, consider the following SQL operations:
INSERT INTO tab1 VALUES (1, 1, 1);
UPDATE tab1 SET c2 = 2 WHERE c1 = 1;

When this parameter is defined, the output will be as follows:
{"c1": 1, "c2": 2, "c3": 1, "old&c1": 1, "old&c2": 1, "old&c3": 1}

Here, old& is the *prefix* specified in this parameter, applied to the 'before' version columns.

For File/FTP/SFTP, this parameter can be used only if the parameter [**Xml**](#xml), [**Csv**](#csv), [**Avro**](#avro), [**Json**](#json), or [**Parquet**](#parquet) is selected.

---

### BeforeUpdateColumnsWhenChanged


File/FTP/SFTP   Kafka

**Description**: Adds the *prefix* (defined in [**BeforeUpdateColumns**](#beforeupdatecolumns)) only to columns where the values have been updated. This is supported only for JSON and XML formats.

For example, consider the following SQL operations:
INSERT INTO tab1 VALUES (1, 1, 1);
UPDATE tab1 SET c2 = 2 WHERE c1 = 1;

When this parameter is defined, the output will be as follows:
{"c1": 1, "c2": 2, "c3": 1, "old&c2": 1}

Here, old& is the *prefix* specified in the parameter [**BeforeUpdateColumns**](#beforeupdatecolumns). Note that the *prefix* is applied only to c2, as it is the column with an updated value.

This option can be applied only when parameter [**BeforeUpdateColumns**](#beforeupdatecolumns) is selected.

For File/FTP/SFTP, this parameter can be used only if the parameter [**Xml**](#xml) or [**Json**](#json) is selected.

---

### ConvertNewlinesTo


**Argument**: *style*

**Description**: Write files with **UNIX** or **DOS** style newlines.

---

### CaptureConverter


**Argument**: *path*

**Description**: Run files through converter before reading. Value *path* can be a script or an executable. Scripts can be shell scripts on Unix and batch scripts on Windows or can be files beginning with a 'magic line' containing the interpreter for the script (e.g., **#!perl**).

A converter command should read from its **stdin** and write to **stdout**. Argument *path* can be an absolute or a relative pathname. If a relative pathname is supplied, the command should be located in the **HVR_CONFIG/plugin/transform** directory. For more information about the converter commands and environment, see the [Capture and Integrate Converters](#captureandintegrateconverters) section below.

> **Important:** 
This field is displayed only when the action definition is for a file location or if the channel contain a file location.


---

### CaptureConverterArguments


**Argument**: *userarg*

**Description**: Arguments to the capture converter.

> **Important:** 
This field is displayed only when the action definition is for a file location or if the channel contain a file location.


---

### IntegrateConverter


**Argument**: *path*

**Description**: Run files through converter before writing. Value *path* can be a script or an executable. Scripts can be shell scripts on Unix and batch scripts on Windows or can be files beginning with a 'magic line' containing the interpreter for the script (e.g., **#!perl**). For more information about the converter commands and environment, see the [Capture and Integrate Converters](#captureandintegrateconverters) section below.

A converter command should read from its **stdin** and write to **stdout**. Argument *path* can be an absolute or a relative pathname. If a relative pathname is supplied the command should be located in the **HVR_CONFIG/plugin/transform** directory.

---

### IntegrateConverterArguments


**Argument**: *userarg*

**Description**: Arguments to the integrate converter (**IntegrateConverter**) program.

---

### Context


**Argument**: *context*

**Description**: Action **FileFormat** is effective/applied only if the *context* matches the context defined in [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh). For more information about using Context, see our concept page [Refresh or Compare context](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).

The value should be a context name, specified as a lowercase identifier. It can also have form **!***context*, which means that the action is effective unless the matching *context* is enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

One or more contexts can be enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

---

## HVR's XML Format


The XML schema used by HVR can be found in the **HVR_HOME/etc/xml/hvr.dtd** file.

### Simple Example

Expand to see the simple example
Following is a simple example of an XML file containing changes which were replicated from a database location.
<?xml version="1.0" encoding="UTF–8" standalone="yes"?>
<hvr version="1.0">
    <table name="dm01_product">
        <row>
            <column name="prod_id">1</column>
            <column name="prod_price">30</column>
            <column name="prod_descrip">DVD</column>
        </row>
        <row>
            <column name="prod_id">2</column>
            <column name="prod_price">300</column>
            <column name="prod_descrip" is_null="true"/>
        </row>
    </table>
</hvr>

### Extended Example

Expand to see the extended example
Following is an extended example of HVR XML.

- 
Create tables in Oracle:
CREATE TABLE mytab (
    aa NUMBER NOT NULL,
    bb DATE,
    CONSTRAINT mytab_pk PRIMARY KEY (aa)
);

CREATE TABLE tabx (
    a NUMBER NOT NULL,
    b VARCHAR2(10) NOT NULL,
    c BLOB,
    CONSTRAINT tabx_pk PRIMARY KEY (a, b)
);

- 
Switch to a different user to create a new table with same name **tabx**.
CREATE TABLE tabx (
    c1 NUMBER,
    c2 CHAR(5),
    CONSTRAINT tabx_pk PRIMARY KEY (c1)
);

- 
Define an HVR channel with the following actions and parameters:
 Group | Table | Action | Parameter(s) | Remarks |
 SOURCE | * | [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) |  |  |
 TARGET | * | [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) |  |  |
 TARGET | * | [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) | [**Name**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#name)**=hvr_op_val** 
[**IntegrateExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#integrateexpression)**={hvr_op}** 
[**Extra**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#extra) | Causes an extra column named **hvr_op_val** to be shown, which indicates the operation type (**0**=delete, **1**=insert, **2**=update, **3**=before key update, **4**=before non-key update). |
 TARGET | * | [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) | [**Name**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#name)**=hvr_timekey** 
[**IntegrateExpression**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#integrateexpression)**={hvr_integ_key**} 
[**Extra**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#extra) 
[**TimeKey**](https://fivetran.com/docs/hvr6/action-reference/columnproperties#timekey) | This is needed if the target location is a file or Kafka location to replicate delete operations. |

- 
Apply changes to the source database using the following SQL statements:
INSERT INTO tabx (a, b, c)  -- Note: column c contains binary/hex data
VALUES (1, 'hello', '746f206265206f72206e6f7420746f2062652c007468617420697320746865');

INSERT INTO tabx (a, b, c)
VALUES (2, '<world>', '7175657374696f6e');

INSERT INTO mytab (aa, bb)
VALUES (33, SYSDATE);

UPDATE tabx
SET c = NULL
WHERE a = 1;

COMMIT;

UPDATE mytab
SET aa = 5555
WHERE aa = 33;  -- Note: key update

DELETE FROM tabx;  -- Note: deletes two rows

INSERT INTO user2.tabx (c1, c2)  -- Note: different tables share same name
VALUES (77, 'seven');

COMMIT;



The above SQL statements would be represented by the following XML output.
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<hvr version="1.0">
    <table name="tabx">
        <row>
            <column name="hvr_op_val">1</column>
            <column name="hvr_timekey">5FFEF1E300000001</column>
            <column name="a">1</column>               <-- Note: Hvr_op=1 means insert -->
            <column name="b">hello</column>
            <column name="c" format="hex">          <-- Note: Binary shown in hex       -->
                                                    <-- Note: Text after hash (#) is comment -->
                746f 2062 6520 6f72 206e 6f74 2074 6f20     # to be or not to
                6265 2c00 7468 6174 2069 7320 7468 65       # be,.that is the
            </column>
        </row>
        <row>
            <column name="hvr_op_val">1</column>
             <column name="hvr_timekey">5FFEF1E300000002</column>
            <column name="a">2</column>
            <column name="b"><world></column>       <-- Note: Standard XML escapes used -->
            <column name="c" format="hex">
                7175 6573 7469 6f6e                 # question
            </column>
        </row>
    </table>                                      <-- Note: Table tag switches current table -->

    <table name="mytab">
        <row>
            <column name="hvr_op_val">1</column>
             <column name="hvr_timekey">5FFEF1E300000003</column>
            <column name="aa">33</column>
            <column name="bb">2012-09-17 17:32:27</column>    <-- Note: HVR own date format -->
        </row>
    </table>

    <table name="tabx">
        <row>
            <column name="hvr_op_val">4</column>  <-- Note: Hvr_op=4 means non-key update before -->
            <column name="hvr_timekey">5FFEF1E300000004</column>
            <column name="a">1</column>
            <column name="b">hello</column>
        </row>
        <row>                                       <-- Note: No table tag because no table switch -->
            <column name="hvr_op_val">2</column>  <-- Note: Hvr_op=2 means update-after -->
            <column name="hvr_timekey">5FFEF1E300000005</column>
            <column name="a">1</column>
            <column name="b">hello</column>
            <column name="c" is_null="true"/>       <-- Note: Nulls shown in this way -->
        </row>
    </table>

    <table name="mytab">
        <row>
            <column name="hvr_op_val">3</column>  <-- Note: Hvr_op=4 means key update-before -->
            <column name="hvr_timekey">5FFEF1E300000006</column>
            <column name="aa">33</column>
        </row>
        <row>
            <column name="hvr_op_val">2</column>
            <column name="hvr_timekey">5FFEF1E300000007</column>
            <column name="aa">5555</column>
        </row>
    </table>

    <table name="tabx">
        <row>
            <column name="hvr_op_val">0</column>  <-- Note: Hvr_op=0 means delete -->
            <column name="hvr_timekey">5FFEF1E300000008</column>
            <column name="a">1</column>
            <column name="b">hello</column>
            <column name="c" is_null="true"/>
        </row>
        <row>
            <column name="hvr_op_val">0</column>  <-- Note: One SQL statement generated 2 rows -->
            <column name="hvr_timekey">5FFEF1E300000009</column>
            <column name="a">2</column>
            <column name="b"><world></column>  
            <column name="c" format="hex">
                7175 6573 7469 6f6e                 # question
            </column>
        </row>
    </table>

    <table name="tabx1">    <-- Note: Name used here is channels name for table.   -->
                          <-- Note: This may differ from actual table 'base name' -->
        <row>
            <column name="hvr_op">1</column>
            <column name="hvr_timekey">5FFEF1E300000010</column>
            <column name="c1">77</column>
            <column name="c2">seven</column>
        </row>
    </table>
</hvr>            <-- Note: No more changes in the replication cycle -->

---

## Capture and Integrate Converters


### Environment


A command specified with parameter [**CaptureConverter**](#captureconverter) or [**IntegrateConverter**](#integrateconverter) should read from its **stdin** and write the converted bytes to **stdout**. If the command encounters a problem, it should write an error to **stderr** and return with exit code **1**, which will cause the replication jobs to fail. The transform command is called with multiple arguments, which should be defined with [**CaptureConverterArguments**](#captureconverterarguments) or [**IntegrateConverterArguments**](#integrateconverterarguments).

The output of a capture converter must conform the format implied by other parameters of the **FileFormat** action. Therefore if parameter [**Csv**](#csv) is not defined then the command should be XML.

A converter command inherits the environment from its parent process. On the hub, the parent of the parent process is the Scheduler. On a remote Unix machine, it is the **inetd** daemon. On a remote Windows machine it is the HVR Remote Listener service.
Expand for more information
Differences with the environment process are as follows:

- 
Environment variables **$HVR_CHN_NAME** and **$HVR_LOC_NAME** are set.

- 
Environment variable **$HVR_TRANSFORM_MODE** is set to either value **cap**, **integ**, **cmp**, **refr_read** or **refr_write**.

- 
Environment variable **$HVR_CONTEXTS** is defined with a comma–separated list of contexts defined with HVR Refresh or Compare (option **–C***ctx*).

- 
Environment variables **$HVR_VAR_***XXX* are defined for each context variable supplied to HVR Refresh or Compare (option **–V***xxx*=*val*).

- 
For file locations variables **$HVR_FILE_LOC** and **$HVR_LOC_STATEDIR** are set to the file location's top and state directory respectively.

- 
For an integrate converter for 'blob' file channel without table information and for all capture converters, environment variables **$HVR_CAP_LOC**, **$HVR_CAP_TSTAMP**, **$HVR_CAP_FILENAME** and **$HVR_CAP_SUBDIRS** are set with details about the current file.

- 
Environment variable **$HVR_FILE_PROPERTIES** contains a colon–separated *name=value* list of other file properties. This includes values set by 'named patterns' (see parameter [**Pattern**](https://fivetran.com/docs/hvr6/action-reference/capture#pattern) in action [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture)).

If a channel contains tables, the environment variable **$HVR_TBL_NAMES** is set to a colon–separated list of tables for which the job is replicating or refreshing (for example **HVR_TBL_NAMES**=**tbl1:tbl2:tbl3**). Also variable **$HVR_BASE_NAMES** is set to a colon–separated list of table 'base names', which are prefixed by a schema name if action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) with parameter [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema) is defined (for example **HVR_BASE_NAMES**=**base1:sch2.base2:base3**). For modes **cap_end** and **integ_end** these variables are restricted to only the tables actually processed. Environment variables **$HVR_TBL_KEYS** and **$HVR_TBL_KEYS_BASE** are colon–separated lists of keys for each table specified in **$HVR_TBL_NAMES** (e.g., **k1**,**k2:k:k3**,**k4**). The column list is specified in **$HVR_COL_NAMES** and **$HVR_COL_NAMES_BASE**. Any variable defined by action [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) is also set in the converter's environment.

- 
The current working directory is **HVR_TMP**, or **HVR_CONFIG/tmp** if this is not defined.

- 
**stdin** is redirected to a socket (HVR writes the original file contents into this), whereas **stdout** and **stderr** are redirected to separate temporary files. HVR replaces the contents of the original file with the bytes that the converter writes to its **stdout**. Anything that the transform writes to its **stderr** is printed in the job's log file on the hub machine.




The **HVR_HOME/plugin_examples/transform** directory contains examples of transform commands written in Perl:

- 
**hvrcsv2xml.pl** maps CSV files (Comma-separated values) to HVR XML.

- 
**hvrxml2csv.pl** maps HVR XML back to CSV format.

- 
**hvrfile2column.pl** maps the contents of a file into an HVR compatible XML file; the output is a single record/row.



### Example


The following is a simple example where **FileFormat** is defined with parameters [**IntegrateConverter**](#integrateconverter)**=perl** and [**IntegrateConverterArguments**](#integrateconverterarguments)**="-e s/a/z/g"**. This replaces all occurrences of the letter **a** with **z**.



.Table_table__KJiU7 {
    overflow-x: unset !important;
}

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }

.actparam {
    padding-left: 20px;
}
