# Data Type Mapping for Vector - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-vector

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-vector/index.md)

# Data Type Mapping for Vector


This section lists the mapping of data types for Vector.

## Vector as Target


When Vector is used as a target location, following is the mapping of Fivetran HVR repository data types to the corresponding data type in Vector.
Text in green cell indicates the native data type of the DBMS
 HVR Repository Data Types | Attributes | Vector |
 ansidate (ingres) | 
            nullable=0
         | ansidate[native] |
 ansidate | 
            nullable=0
         | ansidate |
 bfile | 
            nullable=0
         | varchar(32000) |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp(6) |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | decimal(20) |
 bigint | 
            bytelen=8
            
nullable=0
         | bigint[native] |
 bigtime | 
            timeprec=6
            
nullable=0
         | time(6) without time zone |
 binary | 
            bytelen=10
            
nullable=0
         | char(10) |
 binary_double | 
            bytelen=8
            
nullable=0
         | float |
 binary_float | 
            bytelen=4
            
nullable=0
         | float4 |
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
         | varchar(32000) |
 bool | 
            bytelen=1
            
nullable=0
         | boolean[native] |
 boolean | 
            bytelen=1
            
nullable=0
         | boolean[native] |
 byte varying | 
            bytelen=10
            
nullable=0
         | varchar(10) |
 byte | 
            bytelen=10
            
nullable=0
         | char(10) |
 byteint | 
            bytelen=1
            
nullable=0
         | i1 |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | c10[native] |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10)[native] |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | char(4000)[native] |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | char(8000)[native] |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(40)[native] |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(20) |
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
         | char(40) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(20) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | varchar(32000) |
 date | 
            nullable=0
         | timestamp(0) |
 date (hana) | 
            nullable=0
         | ansidate |
 date (mysql) | 
            nullable=0
         | ansidate |
 date (sybase) | 
            nullable=0
         | ansidate |
 datetime (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 datetime (sybase) | 
            nullable=0
         | ansidate |
 datetime | 
            nullable=0
         | ansidate |
 datetime2 | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | varchar(32000) |
 dbclob | 
            nullable=0
         | nvarchar(16000) |
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
         | decimal(10,3)[native] |
 decimal | 
            prec=6
            
nullable=0
         | decimal(6)[native] |
 double | 
            bytelen=8
            
nullable=0
         | float |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
 float | 
            bytelen=8
            
nullable=0
         | float[native] |
 float4 | 
            bytelen=4
            
nullable=0
         | float4[native] |
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
         | nchar(10) |
 image | 
            nullable=0
         | varchar(32000) |
 image (sybase) | 
            nullable=0
         | varchar(32000) |
 ingresdate | 
            nullable=0
         | timestamp(0) |
 int unsigned | 
            bytelen=4
            
nullable=0
         | bigint |
 int | 
            bytelen=4
            
nullable=0
         | integer[native] |
 integer | 
            bytelen=4
            
nullable=0
         | integer[native] |
 integer1 | 
            bytelen=1
            
nullable=0
         | i1 |
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
         | interval day to second(0)[native] |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | interval day to second(0) |
 interval month to second | 
            timeprec=0
            
nullable=0
         | interval day to second(0) |
 interval year to month (ingres) | 
            nullable=0
         | interval year to month[native] |
 interval year to month | 
            yearprec=0
            
nullable=0
         | interval year to month |
 json | 
            nullable=0
         | varchar(32000) |
 jsonb | 
            nullable=0
         | varchar(32000) |
 long byte | 
            nullable=0
         | varchar(32000) |
 long char | 
            encoding=UTF-8
            
nullable=0
         | varchar(32000) |
 long nvarchar (db2) | 
            nullable=0
         | nvarchar(16000) |
 long nvarchar | 
            nullable=0
         | nvarchar(16000) |
 long raw | 
            nullable=0
         | varchar(32000) |
 long varbinary | 
            nullable=0
         | varchar(32000) |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | varchar(32000) |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | varchar(32000) |
 long | 
            encoding=UTF-8
            
nullable=0
         | varchar(32000) |
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
         | money[native] |
 money | 
            nullable=0
         | money |
 nchar | 
            charlen=10
            
nullable=0
         | nchar(10)[native] |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | nchar(10) |
 nclob | 
            nullable=0
         | nvarchar(16000) |
 ntext | 
            nullable=0
         | nvarchar(16000) |
 number | 
            nullable=0
         | decimal(38,4) |
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
         | nvarchar(10)[native] |
 nvarchar(max) | 
            nullable=0
         | nvarchar(16000) |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | nvarchar(10) |
 postgres date | 
            nullable=0
         | ansidate |
 postgres time | 
            timeprec=6
            
nullable=0
         | time(6) without time zone |
 postgres timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 raw | 
            bytelen=10
            
nullable=0
         | varchar(10) |
 real | 
            bytelen=4
            
nullable=0
         | float4 |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | char(18) |
 rowversion | 
            bytelen=10
            
nullable=0
         | char(10) |
 smalldatetime | 
            nullable=0
         | ansidate |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | integer |
 smallint | 
            bytelen=2
            
nullable=0
         | smallint[native] |
 smallmoney | 
            nullable=0
         | decimal(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | text(10)[native] |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | varchar(32000) |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | varchar(32000) |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | time(0) without time zone |
 time (hana) | 
            nullable=0
         | time(0) without time zone |
 time (sybase) | 
            nullable=0
         | time(3) without time zone |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | time(0) with local time zone[native] |
 time with time zone | 
            timeprec=0
            
nullable=0
         | time(0) with time zone[native] |
 time | 
            timeprec=0
            
nullable=0
         | time(0) without time zone[native] |
 time | 
            timeprec=3
            
nullable=0
         | time(3) without time zone[native] |
 time2 | 
            nullable=0
         | time(0) without time zone |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | timestamp(0)[native] |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | char(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | varchar(10) |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone[native] |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone[native] |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 timestamp | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | i1 |
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
         | nvarchar(16000) |
 univarchar | 
            charlen=10
            
nullable=0
         | nvarchar(10) |
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
         | varchar(10) |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | varchar(10) |
 varbinary(max) | 
            nullable=0
         | varchar(32000) |
 varbyte | 
            bytelen=10
            
nullable=0
         | varchar(10) |
 varchar | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10)[native] |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000)[native] |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(40)[native] |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) |
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
         | varchar(40) |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | varchar(32000) |
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
         | varchar(40) |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) |
 vargraphic | 
            charlen=10
            
nullable=0
         | nvarchar(10) |
 xml | 
            nullable=0
         | nvarchar(16000) |
 year (mysql) | 
            nullable=0
         | smallint |

