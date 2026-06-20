# Data Type Mapping for Snowflake - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-snowflake

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-snowflake/index.md)

# Data Type Mapping for Snowflake


This section lists the mapping of data types for Snowflake.

## Snowflake as Target


When Snowflake is used as a target location, the following is the mapping of Fivetran HVR repository data types to the corresponding data type in Snowflake.

> **Important:** 
Since 6.1.5/7, HVR supports the **VARIANT** type natively in Snowflake target tables. From 6.1.5/7 through 6.3.5/3, HVR only supports the JSON format for **VARIANT** columns. Since 6.3.5/4, HVR also supports the XML format. However, XML is not supported when using Snowflake internal staging.

[HVR Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) does not support the **VARIANT** type. Using **Compare** with **VARIANT** columns may produce unreliable results.


> **Warning:** 
A known issue occurs when using the **VARIANT** data type with HVR Agent versions earlier than 6.1.5/7 together with HVR Hub versions 6.1.5/7 or later, but earlier than 6.2.0/24 or 6.2.5/10. In this scenario, the following error may appear: F_JD20EC: An unknown datatype with code 'vt.4.16777216'. To resolve this issue, upgrade either the HVR Agent to version 6.1.5/7 or later, or the HVR Hub to version 6.2.0/24, 6.2.5/10, or later.

Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Snowflake |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | binary(8388608) |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp_ntz(6) |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | number(38) |
 bigint | 
            bytelen=8
            
nullable=0
         | number(38) |
 bigtime | 
            timeprec=6
            
nullable=0
         | time(6) |
 binary | 
            bytelen=10
            
nullable=0
         | binary(10) |
 binary_double | 
            bytelen=8
            
nullable=0
         | float |
 binary_float | 
            bytelen=4
            
nullable=0
         | float |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | number(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | number(6,2) |
 bit (mysql) | 
            bitlen=32
            
nullable=0
         | varchar(32) |
 bit | 
            bytelen=1
            
nullable=0
         | boolean |
 blob | 
            nullable=0
         | binary(8388608) |
 bool | 
            bytelen=1
            
nullable=0
         | boolean |
 boolean | 
            bytelen=1
            
nullable=0
         | boolean |
 byte varying | 
            bytelen=10
            
nullable=0
         | binary(10) |
 byte | 
            bytelen=10
            
nullable=0
         | binary(10) |
 byteint | 
            bytelen=1
            
nullable=0
         | number(38) |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | varchar(4000) |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) |
 char as binary | 
            bytelen=10
            
nullable=0
         | binary(10) |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | varchar(2000) |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | varchar(16777216) |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) |
 date | 
            nullable=0
         | timestamp_ntz(0) |
 date (hana) | 
            nullable=0
         | date |
 date (mysql) | 
            nullable=0
         | date |
 date (sybase) | 
            nullable=0
         | date |
 datetime (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 datetime (sybase) | 
            nullable=0
         | timestamp_ntz(3) |
 datetime | 
            nullable=0
         | timestamp_ntz(3) |
 datetime2 | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | timestamp_tz(0) |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp_tz(0) |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | varchar(16777216) |
 dbclob | 
            nullable=0
         | varchar(16777216) |
 decfloat | 
            prec=16
            
nullable=0
         | varchar(42) |
 decfloat | 
            prec=34
            
nullable=0
         | varchar(42) |
 decimal | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 decimal | 
            prec=6
            
nullable=0
         | number(6) |
 double | 
            bytelen=8
            
nullable=0
         | float |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 float | 
            bytelen=8
            
nullable=0
         | float |
 float4 | 
            bytelen=4
            
nullable=0
         | float |
 float8 | 
            bytelen=8
            
nullable=0
         | float |
 float64 | 
            bytelen=8
            
nullable=0
         | float |
 graphic | 
            charlen=10
            
nullable=0
         | varchar(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) |
 image | 
            nullable=0
         | binary(8388608) |
 image (sybase) | 
            nullable=0
         | binary(8388608) |
 ingresdate | 
            nullable=0
         | timestamp_ntz(0) |
 int unsigned | 
            bytelen=4
            
nullable=0
         | number(38) |
 int | 
            bytelen=4
            
nullable=0
         | number(38) |
 integer | 
            bytelen=4
            
nullable=0
         | number(38) |
 integer1 | 
            bytelen=1
            
nullable=0
         | number(38) |
 integer2 | 
            bytelen=2
            
nullable=0
         | number(38) |
 integer4 | 
            bytelen=4
            
nullable=0
         | number(38) |
 integer8 | 
            bytelen=8
            
nullable=0
         | number(38) |
 int64 | 
            bytelen=8
            
nullable=0
         | number(38) |
 interval day to second (ingres) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | varchar(100) |
 interval month to second | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 interval year to month (ingres) | 
            nullable=0
         | varchar(100) |
 interval year to month | 
            yearprec=0
            
nullable=0
         | varchar(100) |
 json | 
            encoding=UTF-8
            
nullable=0
         | variant |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | variant |
 long byte | 
            nullable=0
         | binary(8388608) |
 long char | 
            encoding=UTF-8
            
nullable=0
         | varchar(16777216) |
 long nvarchar (db2) | 
            nullable=0
         | varchar(16777216) |
 long nvarchar | 
            nullable=0
         | varchar(16777216) |
 long raw | 
            nullable=0
         | binary(8388608) |
 long varbinary | 
            nullable=0
         | binary(8388608) |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | varchar(16777216) |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | varchar(16777216) |
 long | 
            encoding=UTF-8
            
nullable=0
         | varchar(16777216) |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | number(38) |
 mediumint | 
            bytelen=3
            
nullable=0
         | number(38) |
 money (ingres) | 
            nullable=0
         | number(14,2) |
 money | 
            nullable=0
         | number(19,4) |
 nchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | varchar(10) |
 nclob | 
            nullable=0
         | varchar(16777216) |
 ntext | 
            nullable=0
         | varchar(16777216) |
 number | 
            nullable=0
         | varchar(50) |
 number | 
            prec=10
            
scale=-127
            
nullable=0
         | float |
 number | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 number | 
            prec=26
            
nullable=0
         | number(26) |
 number | 
            prec=6
            
nullable=0
         | number(6) |
 numeric (db2i) | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | number(6) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 numeric | 
            prec=26
            
nullable=0
         | number(26) |
 numeric | 
            prec=6
            
nullable=0
         | number(6) |
 nvarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 nvarchar(max) | 
            nullable=0
         | varchar(16777216) |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | varchar(10) |
 postgres date | 
            nullable=0
         | date |
 postgres time | 
            timeprec=6
            
nullable=0
         | time(6) |
 postgres timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp_tz(0) |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | varchar(50) |
 postgres numeric | 
            bytelen=14
            
prec=6
            
nullable=0
         | number(6) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | number(20,20) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | number(18) |
 postgres numeric | 
            bytelen=30
            
prec=40
            
nullable=0
         | varchar(41) |
 postgres inet | 
            bytelen=20
            
nullable=0
         | varchar(50) |
 postgres cidr | 
            bytelen=20
            
nullable=0
         | varchar(50) |
 raw | 
            bytelen=10
            
nullable=0
         | binary(10) |
 real | 
            bytelen=4
            
nullable=0
         | float |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | varchar(18) |
 rowversion | 
            bytelen=10
            
nullable=0
         | binary(10) |
 sap decfloat | 
            prec=16
            
nullable=0
         | varchar(42) |
 sap decfloat | 
            prec=34
            
nullable=0
         | varchar(42) |
 smalldatetime | 
            nullable=0
         | timestamp_ntz(0) |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | number(38) |
 smallint | 
            bytelen=2
            
nullable=0
         | number(38) |
 smallmoney | 
            nullable=0
         | number(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | varchar(16777216) |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | varchar(16777216) |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | time(0) |
 time (hana) | 
            nullable=0
         | time(0) |
 time (sybase) | 
            nullable=0
         | time(3) |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | time(0) |
 time with time zone | 
            timeprec=0
            
nullable=0
         | time(0) |
 time | 
            timeprec=0
            
nullable=0
         | time(0) |
 time | 
            timeprec=3
            
nullable=0
         | time(3) |
 time2 | 
            nullable=0
         | time(0) |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp_tz(0) |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | binary(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | binary(10) |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp_ltz(0) |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp_ltz(0) |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp_tz(0) |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp_tz(0) |
 timestamp | 
            timeprec=0
            
nullable=0
         | timestamp_ntz(0) |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | number(38) |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | number(38) |
 tinyint | 
            bytelen=1
            
nullable=0
         | number(38) |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | binary(16) |
 unitext | 
            nullable=0
         | varchar(16777216) |
 univarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | number(38) |
 unsigned int | 
            bytelen=4
            
nullable=0
         | number(38) |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | number(38) |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | varchar(100) |
 varbinary | 
            bytelen=10
            
nullable=0
         | binary(10) |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | binary(10) |
 varbinary(max) | 
            nullable=0
         | binary(8388608) |
 varbyte | 
            bytelen=10
            
nullable=0
         | binary(10) |
 varchar | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) |
 varchar as varbinary | 
            bytelen=10
            
nullable=0
         | varchar(10) |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | varchar(10) |
 varchar (sybase) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 varchar (sybase) | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) |
 varchar (sybase) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | varchar(16777216) |
 varchar2 | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 varchar2 | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) |
 vargraphic | 
            charlen=10
            
nullable=0
         | varchar(10) |
 variant | 
            encoding=UTF-8
            
nullable=0
         | variant |
 xml | 
            nullable=0
         | varchar(16777216) |
 year (mysql) | 
            nullable=0
         | number(4) |

