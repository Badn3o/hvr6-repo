# Data Type Mapping for Teradata - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-teradata

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-teradata/index.md)

# Data Type Mapping for Teradata


This section lists the mapping of data types for Teradata.

## Teradata as Source


When Teradata is used as a source location, following is the mapping of data types in Teradata to the corresponding Fivetran HVR repository data type.

 Teradata | Capture Support | Repository Data Type |
 one-dimensional (1-d) array | Extended | <<A1>> |
 multidimensional (n-d) array | Extended | <<AN>> |
 byte | Native | byte |
 varbyte | Native | varbyte |
 blob | Native | blob |
 char | Native | char |
 varchar | Native | varchar |
 clob | Native | clob |
 avro | Extended | <<data type>> |
 date | Native | ansidate |
 time | Native | time |
 timestamp | Native | timestamp |
 time with time zone | Native | time with time zone |
 timestamp with time zone | Native | timestamp with time zone |
 st_geometry | Extended | <<data type>> |
 mbr | Extended | <<data type>> |
 interval year | Extended | <<YR>> |
 interval year to month | Native | interval year to month |
 interval month | Extended | <<MO>> |
 interval day | Extended | <<DY>> |
 interval day to hour | Extended | <<DH>> |
 interval day to minute | Extended | <<DM>> |
 interval day to second | Native | interval day to second |
 interval hour | Extended | <<HR>> |
 interval hour to minute | Extended | <<HM>> |
 interval hour to second | Extended | <<HS>> |
 interval minute | Extended | <<MI>> |
 interval minute to second | Extended | <<MS>> |
 interval second | Extended | <<SC>> |
 json | Extended | <<data type>> |
 byteint | Native | byteint |
 smallint | Native | smallint |
 integer | Native | integer |
 bigint | Native | bigint |
 decimal/numeric | Native | decimal |
 float/real/double precision | Native | double |
 number | Native | number |
 td_anytype | Extended | <<++>> |
 variant_type | Extended | <<data type>> |
 period(date) | Extended | <<PD>> |
 period(time) | Extended | <<PT>> |
 period(time with time zone) | Extended | <<PZ>> |
 period(timestamp) | Extended | <<PS>> |
 period(timestamp with time zone) | Extended | <<PM>> |
 distinct | Extended | <<UT>> |
 structured | Extended | <<data type>> |
 xml | Extended | <<XM>> |


## Teradata as Target


When Teradata is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in Teradata.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Teradata |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | blob(2097088000) |
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
         | bigint |
 bigtime | 
            timeprec=6
            
nullable=0
         | time(6) |
 binary | 
            bytelen=10
            
nullable=0
         | byte(10) |
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
         | decimal(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | decimal(6,2) |
 bit (mysql) | 
            bitlen=32
            
nullable=0
         | varchar(32) char set latin casespecific |
 bit | 
            bytelen=1
            
nullable=0
         | byteint |
 blob | 
            nullable=0
         | blob(2097088000) |
 bool | 
            bytelen=1
            
nullable=0
         | byteint |
 boolean | 
            bytelen=1
            
nullable=0
         | byteint |
 byte varying | 
            bytelen=10
            
nullable=0
         | varbyte(10) |
 byte | 
            bytelen=10
            
nullable=0
         | byte(10) |
 byteint | 
            bytelen=1
            
nullable=0
         | byteint |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) char set latin casespecific |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) char set latin casespecific |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | char(4000) char set latin casespecific |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | char(8000) char set latin casespecific |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) char set latin casespecific |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) char set latin casespecific |
 char as binary | 
            bytelen=10
            
nullable=0
         | byte(10) |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) char set latin casespecific |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | char(2000) char set latin casespecific |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) char set latin casespecific |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) char set latin casespecific |
 clob | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) char set latin casespecific |
 date | 
            nullable=0
         | timestamp(0) |
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
         | timestamp(0) |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 datetime (sybase) | 
            nullable=0
         | timestamp(3) |
 datetime | 
            nullable=0
         | timestamp(3) |
 datetime2 | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) char set latin casespecific |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
 dbclob | 
            nullable=0
         | clob(1048544000) char set unicode |
 decfloat | 
            prec=16
            
nullable=0
         | varchar(42) char set latin casespecific |
 decfloat | 
            prec=34
            
nullable=0
         | varchar(42) char set latin casespecific |
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
         | timestamp(0) |
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
         | char(10) char set unicode casespecific |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) char set latin casespecific |
 image | 
            nullable=0
         | blob(2097088000) |
 image (sybase) | 
            nullable=0
         | blob(2097088000) |
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
         | integer |
 integer | 
            bytelen=4
            
nullable=0
         | integer |
 integer1 | 
            bytelen=1
            
nullable=0
         | byteint |
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
         | timestamp(0) |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | timestamp(0) |
 interval month to second | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 interval year to month (ingres) | 
            nullable=0
         | timestamp(0) |
 interval year to month | 
            yearprec=0
            
nullable=0
         | timestamp(0) |
 json | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
 long byte | 
            nullable=0
         | blob(2097088000) |
 long char | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
 long nvarchar (db2) | 
            nullable=0
         | clob(1048544000) char set unicode |
 long nvarchar | 
            nullable=0
         | clob(1048544000) char set unicode |
 long raw | 
            nullable=0
         | blob(2097088000) |
 long varbinary | 
            nullable=0
         | blob(2097088000) |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
 long | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
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
         | char(10) char set unicode casespecific |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | char(10) char set unicode casespecific |
 nclob | 
            nullable=0
         | clob(1048544000) char set unicode |
 ntext | 
            nullable=0
         | clob(1048544000) char set unicode |
 number | 
            nullable=0
         | number |
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
         | varchar(10) char set unicode casespecific |
 nvarchar(max) | 
            nullable=0
         | clob(1048544000) char set unicode |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | varchar(10) char set unicode casespecific |
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
         | timestamp(0) with time zone |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | number |
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
         | decimal(12,20) |
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
         | varchar(41) char set latin casespecific |
 postgres inet | 
            bytelen=20
            
nullable=0
         | varchar(50) char set latin casespecific |
 postgres cidr | 
            bytelen=20
            
nullable=0
         | varchar(50) char set latin casespecific |
 raw | 
            bytelen=10
            
nullable=0
         | varbyte(10) |
 real | 
            bytelen=4
            
nullable=0
         | float |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | char(18) char set latin casespecific |
 rowversion | 
            bytelen=10
            
nullable=0
         | byte(10) |
 sap decfloat | 
            prec=16
            
nullable=0
         | varchar(42) char set latin casespecific |
 sap decfloat | 
            prec=34
            
nullable=0
         | varchar(42) char set latin casespecific |
 smalldatetime | 
            nullable=0
         | timestamp(0) |
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
         | varchar(10) char set latin casespecific |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob(2097088000) char set latin  |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
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
         | time(0) with time zone |
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
         | timestamp(0) with time zone |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
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
         | timestamp(0) |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | byte(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | varbyte(10) |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
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
         | byteint |
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
         | byte(16) |
 unitext | 
            nullable=0
         | clob(1048544000) char set unicode |
 univarchar | 
            charlen=10
            
nullable=0
         | varchar(10) char set unicode casespecific |
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
         | varchar(100) char set latin casespecific |
 varbinary | 
            bytelen=10
            
nullable=0
         | varbyte(10) |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | varbyte(10) |
 varbinary(max) | 
            nullable=0
         | blob(2097088000) |
 varbyte | 
            bytelen=10
            
nullable=0
         | varbyte(10) |
 varchar | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) char set latin casespecific |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) char set latin casespecific |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) char set latin casespecific |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) char set latin casespecific |
 varchar as varbinary | 
            bytelen=10
            
nullable=0
         | varbyte(10) |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | varbyte(10) |
 varchar (sybase) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) char set latin casespecific |
 varchar (sybase) | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) char set latin casespecific |
 varchar (sybase) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) char set latin casespecific |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) char set latin casespecific |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob(2097088000) char set latin  |
 varchar2 | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) char set latin casespecific |
 varchar2 | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) char set latin casespecific |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) char set latin casespecific |
 vargraphic | 
            charlen=10
            
nullable=0
         | varchar(10) char set unicode casespecific |
 variant | 
            encoding=UTF-8
            
nullable=0
         | clob(2097088000) char set latin  |
 xml | 
            nullable=0
         | clob(1048544000) char set unicode |
 year (mysql) | 
            nullable=0
         | smallint |

