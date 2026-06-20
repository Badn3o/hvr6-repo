# Data Type Mapping for SingleStore - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-singlestore

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-singlestore/index.md)

# Data Type Mapping for SingleStore


This section lists the mapping of data types for SingleStore.

## SingleStore as Target


When SingleStore is used as a target location, following is the mapping of Fivetran HVR repository data types to the corresponding data type in SingleStore.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | MemSQL |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | longblob |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | datetime(6) |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | bigint unsigned |
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
         | binary(10) |
 binary_double | 
            bytelen=8
            
nullable=0
         | double |
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
         | bit(64) |
 bit | 
            bytelen=1
            
nullable=0
         | tinyint |
 blob | 
            nullable=0
         | longblob |
 bool | 
            bytelen=1
            
nullable=0
         | tinyint |
 boolean | 
            bytelen=1
            
nullable=0
         | tinyint |
 byte varying | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
 byte | 
            bytelen=10
            
nullable=0
         | binary(10) |
 byteint | 
            bytelen=1
            
nullable=0
         | tinyint |
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
         | char(10) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 char as binary | 
            bytelen=10
            
nullable=0
         | binary(10) |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) |
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
         | char(10) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) |
 date | 
            nullable=0
         | datetime(0) |
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
         | datetime(0) |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 datetime (sybase) | 
            nullable=0
         | datetime(6) |
 datetime | 
            nullable=0
         | datetime(6) |
 datetime2 | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 dbclob | 
            nullable=0
         | longtext |
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
         | double |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 float | 
            bytelen=8
            
nullable=0
         | double |
 float4 | 
            bytelen=4
            
nullable=0
         | float |
 float8 | 
            bytelen=8
            
nullable=0
         | double |
 float64 | 
            bytelen=8
            
nullable=0
         | double |
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
         | longblob |
 image (sybase) | 
            nullable=0
         | longblob |
 ingresdate | 
            nullable=0
         | datetime(0) |
 int unsigned | 
            bytelen=4
            
nullable=0
         | int unsigned |
 int | 
            bytelen=4
            
nullable=0
         | int |
 integer | 
            bytelen=4
            
nullable=0
         | int |
 integer1 | 
            bytelen=1
            
nullable=0
         | tinyint |
 integer2 | 
            bytelen=2
            
nullable=0
         | smallint |
 integer4 | 
            bytelen=4
            
nullable=0
         | int |
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
         | datetime(0) |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | datetime(0) |
 interval month to second | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 interval year to month (ingres) | 
            nullable=0
         | datetime(0) |
 interval year to month | 
            yearprec=0
            
nullable=0
         | datetime(0) |
 json | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 long byte | 
            nullable=0
         | longblob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 long nvarchar (db2) | 
            nullable=0
         | longtext |
 long nvarchar | 
            nullable=0
         | longtext |
 long raw | 
            nullable=0
         | longblob |
 long varbinary | 
            nullable=0
         | longblob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 long | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | mediumint unsigned |
 mediumint | 
            bytelen=3
            
nullable=0
         | mediumint |
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
         | longtext |
 ntext | 
            nullable=0
         | longtext |
 number | 
            nullable=0
         | varchar(50) |
 number | 
            prec=10
            
scale=-127
            
nullable=0
         | double |
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
         | int |
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
         | longtext |
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
         | datetime(0) |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | datetime(0) |
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
         | varbinary(10) |
 real | 
            bytelen=4
            
nullable=0
         | float |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | char(18) |
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
         | datetime(0) |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | smallint unsigned |
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
         | longtext |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | longtext |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | time(0) |
 time (hana) | 
            nullable=0
         | time(0) |
 time (sybase) | 
            nullable=0
         | time(6) |
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
         | time(6) |
 time2 | 
            nullable=0
         | time(0) |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | binary(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 timestamp | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | tinyint |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | tinyint unsigned |
 tinyint | 
            bytelen=1
            
nullable=0
         | tinyint unsigned |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | binary(16) |
 unitext | 
            nullable=0
         | longtext |
 univarchar | 
            charlen=10
            
nullable=0
         | varchar(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | bigint unsigned |
 unsigned int | 
            bytelen=4
            
nullable=0
         | int unsigned |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | smallint unsigned |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | varchar(100) |
 varbinary | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
 varbinary(max) | 
            nullable=0
         | longblob |
 varbyte | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
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
         | varbinary(10) |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
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
         | longtext |
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
         | longtext |
 xml | 
            nullable=0
         | longtext |
 year (mysql) | 
            nullable=0
         | year |

