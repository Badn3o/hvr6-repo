# HVR 6 - 08 Action Reference

**Source:** https://fivetran.com/docs/hvr6/action-reference

---

# Action Reference

This section describes Fivetran HVR actions and their parameters. Actions in HVR allow you to define the behavior of replication. When a replication channel is created, at least two actions[Capture](https://fivetran.com/docs/hvr6/action-reference/capture)and[Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate)must be defined on source and target locations respectively to activate replication.

## AdaptDDL

| Parameter | Argument | Description |
|---|---|---|
| AddTablePattern | patt | Add new tables to channel if they match. |
| IgnoreTablePattern | patt | Ignore new tables which match pattern. |
| CaptureSchema | db_schema | Database schema for matching tables. |
| IntegrateSchema | db_schema | Generate schema for target location(s). |
| OnEnrollBreak | policy | Applies a | policy | to control the behavior of capture job for an existing table to handle break in the enroll information. |
| OnAddColumnWithDefault | policy | Applies a | policy | to customize behavior when AdaptDDL detects new columns with default values. |
| OnPreserveAlterTableFail | policy | Applies a | policy | to control the behavior of capture job for an existing table to handle any failure while performing | ALTER TABLE | on the target table. |
| RefreshOptions | refr_opts | Configure options for adapt's refresh of target. |
| OnDropTable | policy | Applies a policy that controls the replication behavior if a | DROP TABLE | is done to a replicated table. |
| KeepExistingStructure | Preserve old columns in target, and do not reduce data types sizes. |
| KeepOldRows | Preserve old rows in target during recreate. |

## AgentPlugin

| Parameter | Argument | Description |
|---|---|---|
| Command | path | Call OS command during replication jobs. |
| DbProc | dbproc | Call database procedure | dbproc | during replication jobs. |
| UserArgument | str | Pass argument | str | to each agent execution. |
| ExecOnHub | Execute agent on hub instead of location's machine. |
| Order | int | Specify order of agent execution. |
| Context | context | Action is only effective/applied if the | context | matches with the context (option | -C | ) defined in | Refresh | or | Compare | . |

## Capture

| Parameter | Argument | Description |
|---|---|---|
| IgnoreSessionName | sess_name | Capture changes directly from DBMS logging system. |
| Coalesce | Coalesce consecutive changes on the same row into a single change. |
| NoBeforeUpdate | Only capture the new values for updated rows. |
| NoTruncate | Do not capture truncate table statements. |
| AugmentIncomplete | col_type | Capture job must select for column values. |
| IgnoreCondition | sql_expr | Ignore changes that satisfy expression. |
| IgnoreUpdateCondition | sql_expr | Ignore update changes that satisfy expression. |
| HashBuckets | int | Hash structure to improve parallelism of captured tables. |
| HashKey | col_list | Hash capture table on specific key columns. |
| DeleteAfterCapture | Delete file after capture, instead of capturing recently changed files. |
| Pattern | pattern | Only capture files whose names match | pattern | . |
| IgnorePattern | pattern | Ignore files whose names match | pattern | . |
| IgnoreUnterminated | pattern | Ignore files whose last line does not match | pattern | . |
| IgnoreSizeChanges | Changes in file size during capture is not considered an error. |
| AccessDelay | secs | Delay read for | secs | seconds to ensure writing is complete. |
| UseDirectoryTime | Check timestamp of parent dir, as Windows move doesn't change mod-time. |

## CollisionDetect

| Parameter | Argument | Description |
|---|---|---|
| TreatCollisionAsError | Do not resolve collisions automatically. |
| TimestampColumn | col_name | Exploit timestamp column | col_name | for collision detection. |
| AutoHistoryPurge | Delete history table row when no longer needed for collision detection. |
| DetectDuringRefresh | colname | During row–wise refresh, discard updates if target timestamp is newer. |
| Context | context | Action is only effective/applied if the | context | matches with the context (option | -C | ) defined in | Refresh | or | Compare | . |

## ColumnProperties

| Parameter | Argument | Description |
|---|---|---|
| Name | col_name | Name of column in the | HVR_COLUMN | repository table. |
| DatatypeMatch | data_type | Data type used for matching instead of | Name | . |
| BaseName | col_name | Database column name differs from the | HVR_COLUMN | repository table. |
| Extra | Column exists in base table but not in the | HVR_COLUMN | repository table. |
| Absent | Column does not exist in base table. |
| CaptureExpression | sql_expr | SQL expression for column value when capturing or reading. |
| CaptureExpressionType | Type of mechanism used by | Capture | , | Refresh | , and | Compare | job to evaluate value in parameter | CaptureExpression | . |
| IntegrateExpression | sql_expr | SQL expression for column value when integrating. |
| ExpressionScope | expr_scope | Operation scope for expressions. |
| CaptureFromRowId | Capture values from table's DBMS row-id. |
| TrimDatatype | int | Reduce width of data type when selecting or capturing changes. |
| Key | Add column to table's replication key. |
| SurrogateKey | Use column instead of the regular key during replication. |
| DistributionKey | Distribution key column. |
| SoftDelete | Convert deletes to update of this column to 1. Value 0 means not deleted. |
| TimeKey | Convert all changes to inserts, using this column for time dimension. |
| IgnoreDuringCompare | Ignore values in column during compare and refresh. |
| Datatype | data_type | Data type in database if it differs from the | HVR_COLUMN | repository table. |
| Length | int | String length in database if it differs from the length in the HVR | repository tables | . |
| Precision | int | Precision in database if it differs from the precision in the HVR | repository tables | . |
| Scale | int | Integer scale in database if it differs from the scale in the HVR | repository tables | . |
| Nullable | Nullability in database if it differs from the nullability in the HVR | repository tables | . |
| Context | context | Action is only effective/applied if the | context | matches with the context (option | -C | ) defined in | Refresh | or | Compare | . |

## DbObjectGeneration

| Parameter | Argument | Description |
|---|---|---|
| NoCaptureInsertTrigger | Inhibit generation of capture insert trigger. |
| NoCaptureUpdateTrigger | Inhibit generation of capture update trigger. |
| NoCaptureDeleteTrigger | Inhibit generation of capture delete trigger. |
| NoCaptureDbProc | Inhibit generation of capture database procedures. |
| NoCaptureTable | Inhibit generation of capture tables. |
| NoIntegrateDbProc | Inhibit generation of integrate database procedures. |
| IncludeSqlFile | file | Search directory for include SQL file. |
| IncludeSqlDirectory | dir | Search directory for include SQL file. |
| BurstTableStorage | Storage for integrate burst table creation statement. |
| RefreshTableStorage | Storage for base table creation statement during | Refresh | . |
| CaptureTableCreateClause | sql_expr | Clause for trigger-based capture table creation statement. |
| StateTableCreateClause | sql_expr | Clause for state table creation statement. |
| BurstTableCreateClause | sql_expr | Clause for integrate burst table creation statement. |
| FailTableCreateClause | sql_expr | Clause for fail table creation statement. |
| HistoryTableCreateClause | sql_expr | Clause for history table creation statement. |
| RefreshTableCreateClause | sql_expr | Clause for base table creation statement during refresh. |
| RefreshTableCreateType | type | Specifies a table type inserted between the | CREATE | and | TABLE | keywords in the | CREATE TABLE | statement during refresh. |
| RefreshTableGrant | Executes a grant statement on the base table created during | Refresh | . |
| BurstTableSchema | schema | Define a schema for storing burst tables, overriding the default schema configuration. |
| StateTableSchema | schema | Defines a schema for storing state tables, overriding the default schema configuration. |

## DbSequence

| Parameter | Argument | Description |
|---|---|---|
| CaptureOnly | Only capture database sequences, do not integrate them. |
| IntegrateOnly | Only integrate database sequences, do not capture them. |
| Name | seq_name | Name of database sequence in the HVR | repository tables | . |
| Schema | db_schema | Schema which owns database sequence. |
| BaseName | seq_name | Name of sequence in database if it differs from name in HVR. |

## Environment

| Parameter | Argument | Description |
|---|---|---|
| Name | name | Name of environment variable. |
| Value | value | Value of environment variable. |
| Context | context | Action is only effective/applied if the | context | matches with the context (option | -C | ) defined in | Refresh | or | Compare | . |

## FileFormat

| Parameter | Argument | Description |
|---|---|---|
| Xml | Transform rows from/into xml-files. |
| Csv | Transforms rows from/into csv files. |
| Avro | Transforms rows into Apache AVRO format. Integrate only. |
| Json | Transforms rows into JSON format. The content of the file depends on the value for parameter | JsonMode | . This parameter only has an effect on the integrate location. |
| Parquet | Read and write files as Parquet format. |
| Compact | Write compact XML tags like <r> and <c> instead of <row> and <column>. |
| Compress | algorithm | Compress/uncompress while writing/reading. |
| Encoding | encoding | Encoding of file. |
| HeaderLine | First line of file contains column names. |
| FieldSeparator | str_esc | Field separator. |
| LineSeparator | str_esc | Line separator. |
| QuoteCharacter | str_esc | Character to quote a field with, if the fields contains separators. |
| EscapeCharacter | str_esc | Character to escape the quote character with. |
| FileTerminator | str_esc | File termination at end-of-file. |
| NullRepresentation | esc_str | String representation for columns with NULL value. |
| JsonMode | mode | Style used to write row into JSON format. |
| BlockCompress | codec | Compression codec for Avro and Parquet. |
| AvroVersion | version | Version of Apache AVRO format. |
| PageSize | Parquet page size in bytes. |
| RowGroupThreshold | Maximum row group size in bytes for Parquet. |
| ParquetVersion | version | Category of data types to represent complex data into Parquet format. |
| BeforeUpdateColumns | prefix | Merges the 'before' and 'after' versions of a row into one. |
| BeforeUpdateColumnsWhenChanged | Adds the | prefix | (defined in | BeforeUpdateColumns | ) only to columns in which values were updated. |
| ConvertNewlinesTo | style | Write files with UNIX or DOS style newlines. |
| CaptureConverter | path | Run files through converter before reading. |
| CaptureConverterArguments | userarg | Arguments to the capture converter. |
| IntegrateConverter | path | Run files through converter after writing. |
| IntegrateConverterArguments | userarg | Arguments to the integrate converter program. |
| Context | context | Action is only effective/applied if the | context | matches with the context (option | -C | ) defined in | Refresh | or | Compare | . |

## Integrate

| Parameter | Argument | Description |
|---|---|---|
| Method | method | Method of writing or integrating changes into the target location. |
| BurstCommitFrequency | freq | Frequency of commits. |
| Coalesce | Enables coalescing on the same row into a single change. |
| CoalesceTimekey | Causes coalescing on | TimeKey | channels when writing to a database target. |
| ReorderRows | mode | Control order in which changes are written to files. |
| Resilient | mode | Resilient integrate for inserts, updates and deletes. |
| OnErrorSaveFailed | Write failed row to fail table. |
| DbProc | Apply changes by calling integrate database procedures. |
| TxBundleSize | int | Bundle small transactions for improved performance. |
| TxSplitLimit | int | Split very large transactions to limit resource usage. |
| NoTriggerFiring | Enable/Disable database triggers during integrate. |
| SessionName | sess_name | Integrate changes with special session name. |
| Topic | expression | Name of the Kafka topic. You can use strings/text or expressions as Kafka topic name. |
| MessageKey | expression | Expression to generate user defined key in a Kafka message. |
| MessageKeySerializer | format | Encodes the generated Kafka message key in a string or Kafka Avro serialization format. |
| MessageHeaders | key | : | value | Add custom headers to the Kafka messages. |
| OnDeleteSendTombstone | Convert | DELETE | operations into Kafka tombstone messages. |
| RenameExpression | expression | Expression to name new files, containing brace substitutions. |
| ComparePattern | patt | Perform direct file compare. |
| ErrorOnOverwrite | Error if a new file has same name as an existing file. |
| MaxFileSize | size | Limit each XML file to | size | bytes. |
| Verbose | Report name of each file integrated. |
| TableName | apitab | API name of table to upload attachments into. |
| KeyName | apikey | API name of attachment table's key column. |
| CycleByteLimit | int | Max amount of routed data (compressed) to process per integrate cycle. |
| JournalRouterFiles | Move processed router files to journal directory on hub. |
| JournalBurstTable | Keep track of changes in the burst table during | Burst Integrate | . |
| Delay | N | Delay integration of changes for | N | seconds. |
| Context | context | Action is only effective/applied if the | context | matches with the context (option | -C | ) defined in | Refresh | or | Compare | . |

## Restrict

| Parameter | Argument | Description |
|---|---|---|
| CaptureCondition | sql_expr | Restrict during capture. |
| IntegrateCondition | sql_expr | Restrict during integration. |
| RefreshCondition | sql_expr | Restrict during refresh and compare. |
| CompareCondition | sql_expr | Restrict during compare. |
| RefreshJoinCondition | sql_expr | Filter rows during refresh. |
| CompareJoinCondition | sql_expr | Filter rows during compare. |
| SliceCountCondition | sql_expr | Defines a SQL expression that determines which rows are included in a specific slice during | Refresh | or | Compare | when slicing by | Count | . |
| SliceSeriesCondition | sql_expr | Defines a SQL expression that determines which rows are included in a specific slice during | Refresh | or | Compare | when slicing by | Series | . |
| HorizColumn | col_name | Horizontal partition table based on value in | col_name | . |
| HorizLookupTable | tbl_name | Join partition column with horizontal lookup table. |
| DynamicHorizLookup | Changes to lookup table also trigger replication. |
| AddressTo | addr | Only send changes to locations specified by address. |
| AddressSubscribe | addr | Get copy of any changes sent to matching address. |
| SelectDistinct | Filter duplicate records during | Refresh | or | Compare | . |

## Scheduling

| Parameter | Argument | Description |
|---|---|---|
| CaptureStartTimes | times | Trigger capture job at specific times, rather than continuous cycling. |
| CaptureOnceOnStart | Capture job runs for one cycle after trigger. |
| IntegrateStartAfterCapture | Trigger integrate job only after capture job routes new data. |
| IntegrateStartTimes | times | Trigger integrate job at specific times, rather than continuous cycling. |
| IntegrateOnceOnStart | Integrate job runs for one cycle after trigger. |
| LatencySLA | threshold | Threshold for the latency. |
| TimeContext | times | Time range during which the | LatencySLA | is active/valid. |

## TableProperties

| Parameter | Argument | Description |
|---|---|---|
| BaseName | tbl_name | Name of a table in a database differs from the name in the HVR | repository tables | . |
| Absent | Exclude table (which is available in the channel) from being replicated/integrated into target. |
| NoDuplicateRows | Replication table cannot have duplicate rows. |
| Schema | schema | Database schema which owns table. |
| CoerceErrorPolicy | Defines a policy to handle type coercion error. |
| CoerceErrorType | Defines which types of coercion errors are affected by | CoerceErrorPolicy | . |
| SapUnpackErrorPolicy | policy | Defines a | policy | to handle type coercion error during SapUnpack |
| PackedInside | Name of the SAP database table that holds the data for the pool or cluster table being unpacked. |
| TrimWhiteSpace | Remove trailing whitespace from | varchar | . |
| TrimTime | policy | Trim time when converting from Oracle and SqlServer date. |
| MapEmptyStringToSpace | Convert between empty varchar and Oracle varchar space. |
| MapEmptyDateToConstant | date | Convert between constant | date | (dd/mm/yyyy) and Ingres empty date. |
| CreateUnicodeDatatypes | On table creation use Unicode data types, e.g. map | varchar | to | nvarchar | . |
| DistributionKeyLimit | int | Maximum number of columns in the implicit distribution key. |
| DistributionKeyAvoidPattern | patt | Avoid putting given columns in the implicit distribution key. |
| CharacterMapping | rules | Specify the replacement rules for unsupported characters. |
| MapBinary | policy | Specify how binary data is represented on the target side. |
| MissingRepresentationString | str | Inserts value | str | into the string data type column(s) if value is missing/empty in the respective column(s) during integration. |
| MissingRepresentationNumeric | str | Inserts value | str | into the numeric data type column(s) if value is missing/empty in the respective column(s) during integration. |
| MissingRepresentationDate | str | Inserts value | str | into the date data type column(s) if value is missing/empty in the respective column(s) during integration. |
| PartitionByDate | Enables partitioning by date for Google BigQuery tables. |
| BQClusterKeys | col_name | Creates Google BigQuery clustered tables. |
| TransientTable | Creates Snowflake transient tables. |
| Context | context | Action is only effective/applied if the | context | matches with the context (option | -C | ) defined in | Refresh | or | Compare | . |

## Transform

| Parameter | Argument | Description |
|---|---|---|
| Command | path | Path to script or executable performing custom transformation. |
| CommandArguments | userarg | Value(s) of parameter(s) for transform (space separated). |
| SapUnpack | Unpack the SAP pool, cluster, and long text table (STXL). |
| ExecOnHub | Execute transform on hub instead of location's machine. |
| Parallel | n | Distribute rows to multiple transformation processes. |
| Context | context | Action is only effective/applied if the | context | matches with the context (option | -C | ) defined in | Refresh | or | Compare | . |