# Data Type Mapping for Avro, Json, and Parquet - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-avro-json-parquet

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-avro-json-parquet/index.md)

# Data Type Mapping for Avro, Json, and Parquet


This section lists the mapping of data types for the file types Avro, Json, and Parquet.

## Avro as Target


In a target location, when the file type is Avro, following is the mapping of Fivetran HVR repository data types to the corresponding data type in Avro.

### Avro 1.6

Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Avro 1.6 |
 ansidate (ingres) | 
            nullable=0
         | bigint |
 ansidate | 
            nullable=0
         | bigint |
 bfile | 
            nullable=0
         | blob |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | varchar(100) |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | float |
 bigint | 
            bytelen=8
            
nullable=0
         | bigint |
 bigtime | 
            timeprec=6
            
nullable=0
         | bigint |
 binary | 
            bytelen=10
            
nullable=0
         | blob |
 binary_double | 
            bytelen=8
            
nullable=0
         | float |
 binary_float | 
            bytelen=4
            
nullable=0
         | real |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | varchar(11) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | varchar(8) |
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
         | blob |
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
         | blob |
 byte | 
            bytelen=10
            
nullable=0
         | blob |
 byteint | 
            bytelen=1
            
nullable=0
         | smallint |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | char(4000) |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | char(8000) |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 char as binary | 
            bytelen=10
            
nullable=0
         | blob |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | char(2000) |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | text |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) |
 date | 
            nullable=0
         | varchar(100) |
 date (hana) | 
            nullable=0
         | bigint |
 date (mysql) | 
            nullable=0
         | bigint |
 date (sybase) | 
            nullable=0
         | bigint |
 datetime (bigquery) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 datetime (sybase) | 
            nullable=0
         | varchar(100) |
 datetime | 
            nullable=0
         | varchar(100) |
 datetime2 | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | text |
 dbclob | 
            nullable=0
         | text |
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
         | varchar(12) |
 decimal | 
            prec=6
            
nullable=0
         | varchar(7) |
 double | 
            bytelen=8
            
nullable=0
         | float |
 epoch | 
            timeprec=0
            
nullable=0
         | bigint |
 float | 
            bytelen=8
            
nullable=0
         | float |
 float4 | 
            bytelen=4
            
nullable=0
         | real |
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
         | char(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) |
 image | 
            nullable=0
         | blob |
 image (sybase) | 
            nullable=0
         | blob |
 ingresdate | 
            nullable=0
         | varchar(100) |
 int unsigned | 
            bytelen=4
            
nullable=0
         | bigint |
 int | 
            bytelen=4
            
nullable=0
         | integer |
 integer | 
            bytelen=4
            
nullable=0
         | integer |
 integer1 | 
            bytelen=1
            
nullable=0
         | smallint |
 integer2 | 
            bytelen=2
            
nullable=0
         | smallint |
 integer4 | 
            bytelen=4
            
nullable=0
         | integer |
 integer8 | 
            bytelen=8
            
nullable=0
         | bigint |
 int64 | 
            bytelen=8
            
nullable=0
         | bigint |
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
         | varchar(100) |
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
         | text |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | text |
 long byte | 
            nullable=0
         | blob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | text |
 long nvarchar (db2) | 
            nullable=0
         | text |
 long nvarchar | 
            nullable=0
         | text |
 long raw | 
            nullable=0
         | blob |
 long varbinary | 
            nullable=0
         | blob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | text |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | text |
 long | 
            encoding=UTF-8
            
nullable=0
         | text |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | integer |
 mediumint | 
            bytelen=3
            
nullable=0
         | integer |
 money (ingres) | 
            nullable=0
         | varchar(16) |
 money | 
            nullable=0
         | varchar(21) |
 nchar | 
            charlen=10
            
nullable=0
         | char(10) |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | char(10) |
 nclob | 
            nullable=0
         | text |
 ntext | 
            nullable=0
         | text |
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
         | varchar(12) |
 number | 
            prec=26
            
nullable=0
         | varchar(27) |
 number | 
            prec=6
            
nullable=0
         | integer |
 numeric (db2i) | 
            prec=10
            
scale=3
            
nullable=0
         | varchar(12) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | varchar(7) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | varchar(12) |
 numeric | 
            prec=26
            
nullable=0
         | varchar(27) |
 numeric | 
            prec=6
            
nullable=0
         | varchar(7) |
 nvarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 nvarchar(max) | 
            nullable=0
         | text |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | varchar(10) |
 postgres date | 
            nullable=0
         | bigint |
 postgres time | 
            timeprec=6
            
nullable=0
         | bigint |
 postgres timestamp with time zone | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | varchar(50) |
 postgres numeric | 
            bytelen=14
            
prec=6
            
nullable=0
         | varchar(7) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | varchar(12) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | varchar(23) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | varchar(19) |
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
         | blob |
 real | 
            bytelen=4
            
nullable=0
         | real |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | char(18) |
 rowversion | 
            bytelen=10
            
nullable=0
         | blob |
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
         | varchar(100) |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | integer |
 smallint | 
            bytelen=2
            
nullable=0
         | smallint |
 smallmoney | 
            nullable=0
         | varchar(12) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | text |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | text |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | integer |
 time (hana) | 
            nullable=0
         | integer |
 time (sybase) | 
            nullable=0
         | integer |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | integer |
 time with time zone | 
            timeprec=0
            
nullable=0
         | integer |
 time | 
            timeprec=0
            
nullable=0
         | integer |
 time | 
            timeprec=3
            
nullable=0
         | integer |
 time2 | 
            nullable=0
         | integer |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | bigint |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | blob |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 timestamp | 
            timeprec=0
            
nullable=0
         | varchar(100) |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint | 
            bytelen=1
            
nullable=0
         | smallint |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | char(36) |
 unitext | 
            nullable=0
         | text |
 univarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | float |
 unsigned int | 
            bytelen=4
            
nullable=0
         | bigint |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | integer |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | varchar(100) |
 varbinary | 
            bytelen=10
            
nullable=0
         | blob |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
 varbinary(max) | 
            nullable=0
         | blob |
 varbyte | 
            bytelen=10
            
nullable=0
         | blob |
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
         | blob |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
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
         | text |
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
         | text |
 xml | 
            nullable=0
         | text |
 year (mysql) | 
            nullable=0
         | smallint |


### Avro 1.8

Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Avro 1.8 |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | blob |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp-micros |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | decimal(20) |
 bigint | 
            bytelen=8
            
nullable=0
         | bigint |
 bigtime | 
            timeprec=6
            
nullable=0
         | time(6) |
 binary | 
            bytelen=10
            
nullable=0
         | blob |
 binary_double | 
            bytelen=8
            
nullable=0
         | float |
 binary_float | 
            bytelen=4
            
nullable=0
         | real |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | decimal(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | decimal(6,2) |
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
         | blob |
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
         | blob |
 byte | 
            bytelen=10
            
nullable=0
         | blob |
 byteint | 
            bytelen=1
            
nullable=0
         | smallint |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | char(4000) |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | char(8000) |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 char as binary | 
            bytelen=10
            
nullable=0
         | blob |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | char(2000) |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | text |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) |
 date | 
            nullable=0
         | timestamp-millis |
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
         | timestamp-millis |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 datetime (sybase) | 
            nullable=0
         | timestamp-millis |
 datetime | 
            nullable=0
         | timestamp-millis |
 datetime2 | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | text |
 dbclob | 
            nullable=0
         | text |
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
         | decimal(10,3) |
 decimal | 
            prec=6
            
nullable=0
         | decimal(6) |
 double | 
            bytelen=8
            
nullable=0
         | float |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 float | 
            bytelen=8
            
nullable=0
         | float |
 float4 | 
            bytelen=4
            
nullable=0
         | real |
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
         | char(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) |
 image | 
            nullable=0
         | blob |
 image (sybase) | 
            nullable=0
         | blob |
 ingresdate | 
            nullable=0
         | timestamp-millis |
 int unsigned | 
            bytelen=4
            
nullable=0
         | bigint |
 int | 
            bytelen=4
            
nullable=0
         | integer |
 integer | 
            bytelen=4
            
nullable=0
         | integer |
 integer1 | 
            bytelen=1
            
nullable=0
         | smallint |
 integer2 | 
            bytelen=2
            
nullable=0
         | smallint |
 integer4 | 
            bytelen=4
            
nullable=0
         | integer |
 integer8 | 
            bytelen=8
            
nullable=0
         | bigint |
 int64 | 
            bytelen=8
            
nullable=0
         | bigint |
 interval day to second (ingres) | 
            timeprec=0
            
nullable=0
         | interval month to second |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | interval month to second |
 interval month to second | 
            timeprec=0
            
nullable=0
         | interval month to second |
 interval year to month (ingres) | 
            nullable=0
         | interval month to second |
 interval year to month | 
            yearprec=0
            
nullable=0
         | interval month to second |
 json | 
            encoding=UTF-8
            
nullable=0
         | text |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | text |
 long byte | 
            nullable=0
         | blob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | text |
 long nvarchar (db2) | 
            nullable=0
         | text |
 long nvarchar | 
            nullable=0
         | text |
 long raw | 
            nullable=0
         | blob |
 long varbinary | 
            nullable=0
         | blob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | text |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | text |
 long | 
            encoding=UTF-8
            
nullable=0
         | text |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | integer |
 mediumint | 
            bytelen=3
            
nullable=0
         | integer |
 money (ingres) | 
            nullable=0
         | decimal(14,2) |
 money | 
            nullable=0
         | decimal(19,4) |
 nchar | 
            charlen=10
            
nullable=0
         | char(10) |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | char(10) |
 nclob | 
            nullable=0
         | text |
 ntext | 
            nullable=0
         | text |
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
         | decimal(10,3) |
 number | 
            prec=26
            
nullable=0
         | decimal(26) |
 number | 
            prec=6
            
nullable=0
         | integer |
 numeric (db2i) | 
            prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | decimal(6) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 numeric | 
            prec=26
            
nullable=0
         | decimal(26) |
 numeric | 
            prec=6
            
nullable=0
         | decimal(6) |
 nvarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 nvarchar(max) | 
            nullable=0
         | text |
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
         | timestamp-millis |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | varchar(50) |
 postgres numeric | 
            bytelen=14
            
prec=6
            
nullable=0
         | decimal(6) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | decimal(20,20) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | decimal(18) |
 postgres numeric | 
            bytelen=30
            
prec=40
            
nullable=0
         | decimal(40) |
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
         | blob |
 real | 
            bytelen=4
            
nullable=0
         | real |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | char(18) |
 rowversion | 
            bytelen=10
            
nullable=0
         | blob |
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
         | timestamp-millis |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | integer |
 smallint | 
            bytelen=2
            
nullable=0
         | smallint |
 smallmoney | 
            nullable=0
         | decimal(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | text |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | text |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | time(3) |
 time (hana) | 
            nullable=0
         | time(3) |
 time (sybase) | 
            nullable=0
         | time(3) |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | time(3) |
 time with time zone | 
            timeprec=0
            
nullable=0
         | time(3) |
 time | 
            timeprec=0
            
nullable=0
         | time(3) |
 time | 
            timeprec=3
            
nullable=0
         | time(3) |
 time2 | 
            nullable=0
         | time(3) |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | blob |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint | 
            bytelen=1
            
nullable=0
         | smallint |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | char(36) |
 unitext | 
            nullable=0
         | text |
 univarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | decimal(20) |
 unsigned int | 
            bytelen=4
            
nullable=0
         | bigint |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | integer |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | varchar(100) |
 varbinary | 
            bytelen=10
            
nullable=0
         | blob |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
 varbinary(max) | 
            nullable=0
         | blob |
 varbyte | 
            bytelen=10
            
nullable=0
         | blob |
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
         | blob |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
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
         | text |
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
         | text |
 xml | 
            nullable=0
         | text |
 year (mysql) | 
            nullable=0
         | smallint |


## Json as Target


In a target location, when the file type is Json, following is the mapping of HVR repository data types to the corresponding data type in Json.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Json |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | blob |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp-micros |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | decimal(20) |
 bigint | 
            bytelen=8
            
nullable=0
         | bigint |
 bigtime | 
            timeprec=6
            
nullable=0
         | time(6) |
 binary | 
            bytelen=10
            
nullable=0
         | blob |
 binary_double | 
            bytelen=8
            
nullable=0
         | float |
 binary_float | 
            bytelen=4
            
nullable=0
         | real |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | decimal(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | decimal(6,2) |
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
         | blob |
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
         | blob |
 byte | 
            bytelen=10
            
nullable=0
         | blob |
 byteint | 
            bytelen=1
            
nullable=0
         | smallint |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | char(4000) |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | char(8000) |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 char as binary | 
            bytelen=10
            
nullable=0
         | blob |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | char(2000) |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | text |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) |
 date | 
            nullable=0
         | timestamp-millis |
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
         | timestamp-millis |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 datetime (sybase) | 
            nullable=0
         | timestamp-millis |
 datetime | 
            nullable=0
         | timestamp-millis |
 datetime2 | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | text |
 dbclob | 
            nullable=0
         | text |
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
         | decimal(10,3) |
 decimal | 
            prec=6
            
nullable=0
         | decimal(6) |
 double | 
            bytelen=8
            
nullable=0
         | float |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 float | 
            bytelen=8
            
nullable=0
         | float |
 float4 | 
            bytelen=4
            
nullable=0
         | real |
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
         | char(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) |
 image | 
            nullable=0
         | blob |
 image (sybase) | 
            nullable=0
         | blob |
 ingresdate | 
            nullable=0
         | timestamp-millis |
 int unsigned | 
            bytelen=4
            
nullable=0
         | bigint |
 int | 
            bytelen=4
            
nullable=0
         | integer |
 integer | 
            bytelen=4
            
nullable=0
         | integer |
 integer1 | 
            bytelen=1
            
nullable=0
         | smallint |
 integer2 | 
            bytelen=2
            
nullable=0
         | smallint |
 integer4 | 
            bytelen=4
            
nullable=0
         | integer |
 integer8 | 
            bytelen=8
            
nullable=0
         | bigint |
 int64 | 
            bytelen=8
            
nullable=0
         | bigint |
 interval day to second (ingres) | 
            timeprec=0
            
nullable=0
         | interval month to second |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | interval month to second |
 interval month to second | 
            timeprec=0
            
nullable=0
         | interval month to second |
 interval year to month (ingres) | 
            nullable=0
         | interval month to second |
 interval year to month | 
            yearprec=0
            
nullable=0
         | interval month to second |
 json | 
            encoding=UTF-8
            
nullable=0
         | text |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | text |
 long byte | 
            nullable=0
         | blob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | text |
 long nvarchar (db2) | 
            nullable=0
         | text |
 long nvarchar | 
            nullable=0
         | text |
 long raw | 
            nullable=0
         | blob |
 long varbinary | 
            nullable=0
         | blob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | text |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | text |
 long | 
            encoding=UTF-8
            
nullable=0
         | text |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | integer |
 mediumint | 
            bytelen=3
            
nullable=0
         | integer |
 money (ingres) | 
            nullable=0
         | decimal(14,2) |
 money | 
            nullable=0
         | decimal(19,4) |
 nchar | 
            charlen=10
            
nullable=0
         | char(10) |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | char(10) |
 nclob | 
            nullable=0
         | text |
 ntext | 
            nullable=0
         | text |
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
         | decimal(10,3) |
 number | 
            prec=26
            
nullable=0
         | decimal(26) |
 number | 
            prec=6
            
nullable=0
         | integer |
 numeric (db2i) | 
            prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | decimal(6) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 numeric | 
            prec=26
            
nullable=0
         | decimal(26) |
 numeric | 
            prec=6
            
nullable=0
         | decimal(6) |
 nvarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 nvarchar(max) | 
            nullable=0
         | text |
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
         | timestamp-millis |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | varchar(50) |
 postgres numeric | 
            bytelen=14
            
prec=6
            
nullable=0
         | decimal(6) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | decimal(20,20) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | decimal(18) |
 postgres numeric | 
            bytelen=30
            
prec=40
            
nullable=0
         | decimal(40) |
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
         | blob |
 real | 
            bytelen=4
            
nullable=0
         | real |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | char(18) |
 rowversion | 
            bytelen=10
            
nullable=0
         | blob |
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
         | timestamp-millis |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | integer |
 smallint | 
            bytelen=2
            
nullable=0
         | smallint |
 smallmoney | 
            nullable=0
         | decimal(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | text |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | text |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | time(3) |
 time (hana) | 
            nullable=0
         | time(3) |
 time (sybase) | 
            nullable=0
         | time(3) |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | time(3) |
 time with time zone | 
            timeprec=0
            
nullable=0
         | time(3) |
 time | 
            timeprec=0
            
nullable=0
         | time(3) |
 time | 
            timeprec=3
            
nullable=0
         | time(3) |
 time2 | 
            nullable=0
         | time(3) |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | blob |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint | 
            bytelen=1
            
nullable=0
         | smallint |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | char(36) |
 unitext | 
            nullable=0
         | text |
 univarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | decimal(20) |
 unsigned int | 
            bytelen=4
            
nullable=0
         | bigint |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | integer |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | varchar(100) |
 varbinary | 
            bytelen=10
            
nullable=0
         | blob |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
 varbinary(max) | 
            nullable=0
         | blob |
 varbyte | 
            bytelen=10
            
nullable=0
         | blob |
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
         | blob |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
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
         | text |
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
         | text |
 xml | 
            nullable=0
         | text |
 year (mysql) | 
            nullable=0
         | smallint |


## Parquet as Target


In a target location, when the file type is Parquet, following is the mapping of HVR repository data types to the corresponding data type in Parquet.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Parquet |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | blob |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp-micros |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | decimal(20) |
 bigint | 
            bytelen=8
            
nullable=0
         | bigint |
 bigtime | 
            timeprec=6
            
nullable=0
         | time(6) |
 binary | 
            bytelen=10
            
nullable=0
         | blob |
 binary_double | 
            bytelen=8
            
nullable=0
         | float |
 binary_float | 
            bytelen=4
            
nullable=0
         | real |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | decimal(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | decimal(6,2) |
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
         | blob |
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
         | blob |
 byte | 
            bytelen=10
            
nullable=0
         | blob |
 byteint | 
            bytelen=1
            
nullable=0
         | smallint |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | char(4000) |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | char(8000) |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 char as binary | 
            bytelen=10
            
nullable=0
         | blob |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | char(2000) |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | text |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) |
 date | 
            nullable=0
         | timestamp-millis |
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
         | timestamp-millis |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 datetime (sybase) | 
            nullable=0
         | timestamp-millis |
 datetime | 
            nullable=0
         | timestamp-millis |
 datetime2 | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | text |
 dbclob | 
            nullable=0
         | text |
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
         | decimal(10,3) |
 decimal | 
            prec=6
            
nullable=0
         | decimal(6) |
 double | 
            bytelen=8
            
nullable=0
         | float |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 float | 
            bytelen=8
            
nullable=0
         | float |
 float4 | 
            bytelen=4
            
nullable=0
         | real |
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
         | char(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) |
 image | 
            nullable=0
         | blob |
 image (sybase) | 
            nullable=0
         | blob |
 ingresdate | 
            nullable=0
         | timestamp-millis |
 int unsigned | 
            bytelen=4
            
nullable=0
         | bigint |
 int | 
            bytelen=4
            
nullable=0
         | integer |
 integer | 
            bytelen=4
            
nullable=0
         | integer |
 integer1 | 
            bytelen=1
            
nullable=0
         | smallint |
 integer2 | 
            bytelen=2
            
nullable=0
         | smallint |
 integer4 | 
            bytelen=4
            
nullable=0
         | integer |
 integer8 | 
            bytelen=8
            
nullable=0
         | bigint |
 int64 | 
            bytelen=8
            
nullable=0
         | bigint |
 interval day to second (ingres) | 
            timeprec=0
            
nullable=0
         | interval month to second |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | interval month to second |
 interval month to second | 
            timeprec=0
            
nullable=0
         | interval month to second |
 interval year to month (ingres) | 
            nullable=0
         | interval month to second |
 interval year to month | 
            yearprec=0
            
nullable=0
         | interval month to second |
 json | 
            encoding=UTF-8
            
nullable=0
         | text |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | text |
 long byte | 
            nullable=0
         | blob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | text |
 long nvarchar (db2) | 
            nullable=0
         | text |
 long nvarchar | 
            nullable=0
         | text |
 long raw | 
            nullable=0
         | blob |
 long varbinary | 
            nullable=0
         | blob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | text |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | text |
 long | 
            encoding=UTF-8
            
nullable=0
         | text |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | integer |
 mediumint | 
            bytelen=3
            
nullable=0
         | integer |
 money (ingres) | 
            nullable=0
         | decimal(14,2) |
 money | 
            nullable=0
         | decimal(19,4) |
 nchar | 
            charlen=10
            
nullable=0
         | char(10) |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | char(10) |
 nclob | 
            nullable=0
         | text |
 ntext | 
            nullable=0
         | text |
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
         | decimal(10,3) |
 number | 
            prec=26
            
nullable=0
         | decimal(26) |
 number | 
            prec=6
            
nullable=0
         | integer |
 numeric (db2i) | 
            prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | decimal(6) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 numeric | 
            prec=26
            
nullable=0
         | decimal(26) |
 numeric | 
            prec=6
            
nullable=0
         | decimal(6) |
 nvarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 nvarchar(max) | 
            nullable=0
         | text |
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
         | timestamp-millis |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | varchar(50) |
 postgres numeric | 
            bytelen=14
            
prec=6
            
nullable=0
         | decimal(6) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | decimal(10,3) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | decimal(20,20) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | decimal(18) |
 postgres numeric | 
            bytelen=30
            
prec=40
            
nullable=0
         | decimal(40) |
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
         | blob |
 real | 
            bytelen=4
            
nullable=0
         | real |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | char(18) |
 rowversion | 
            bytelen=10
            
nullable=0
         | blob |
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
         | timestamp-millis |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | integer |
 smallint | 
            bytelen=2
            
nullable=0
         | smallint |
 smallmoney | 
            nullable=0
         | decimal(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | text |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | text |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | time(3) |
 time (hana) | 
            nullable=0
         | time(3) |
 time (sybase) | 
            nullable=0
         | time(3) |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | time(3) |
 time with time zone | 
            timeprec=0
            
nullable=0
         | time(3) |
 time | 
            timeprec=0
            
nullable=0
         | time(3) |
 time | 
            timeprec=3
            
nullable=0
         | time(3) |
 time2 | 
            nullable=0
         | time(3) |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | blob |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 timestamp | 
            timeprec=0
            
nullable=0
         | timestamp-millis |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint | 
            bytelen=1
            
nullable=0
         | smallint |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | char(36) |
 unitext | 
            nullable=0
         | text |
 univarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | decimal(20) |
 unsigned int | 
            bytelen=4
            
nullable=0
         | bigint |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | integer |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | varchar(100) |
 varbinary | 
            bytelen=10
            
nullable=0
         | blob |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
 varbinary(max) | 
            nullable=0
         | blob |
 varbyte | 
            bytelen=10
            
nullable=0
         | blob |
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
         | blob |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | blob |
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
         | text |
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
         | text |
 xml | 
            nullable=0
         | text |
 year (mysql) | 
            nullable=0
         | smallint |

