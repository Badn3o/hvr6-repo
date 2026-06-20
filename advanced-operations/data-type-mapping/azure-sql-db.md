# Data Type Mapping for Azure SQL Database - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-azure-sql-database

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-azure-sql-database/index.md)

# Data Type Mapping for Azure SQL Database


This section lists the mapping of data types for Azure SQL Database.

## Azure SQL Database as Source


When Azure SQL Database is used as a source location, following is the mapping of data types in Azure SQL Database to the corresponding Fivetran HVR repository data type.

 Azure SQL Database | Capture Support | Repository Data Type |
 int | Native | int |
 bigint | Native | bigint |
 smallint | Native | smallint |
 tinyint | Native | tinyint |
 numeric | Native | numeric |
 decimal | Native | numeric |
 bit | Native | bit |
 money | Native | money |
 smallmoney | Native | smallmoney |
 float | Native | float |
 real | Native | real |
 date | Native | ansidate |
 datetime | Native | datetime |
 datetime2 | Native | datetime(2) |
 datetimeoffset | Native | datetimeoffset |
 smalldatetime | Native | smalldatetime |
 time | Native | time |
 char | Native | char |
 varchar | Native | varchar |
 text | Native | text (sqlserver) |
 nchar | Native | nchar |
 nvarchar | Native | nvarchar |
 ntext | Native | ntext |
 binary | Native | binary |
 varbinary | Native | varbinary |
 image | Native | image |
 uniqueidentifier | Native | uniqueidentifier |
 xml | Native | xml |
 cursor | Extended | <<cursor>> |
 hierarchyid | Extended | <<hierarchyid>> |
 rowversion | Extended | <<rowversion>> |
 sql_variant | Extended | <<sql_variant>> |
 spatial geometry types | Extended | <<geometry>> |
 spatial geography types | Extended | <<geography>> |
 table | Extended | <<table>> |


## Azure SQL Database as Target


When Azure SQL Database is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in Azure SQL Database.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Azure SQL Database |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | varbinary(max) |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | datetime2(6) |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | numeric(20) |
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
         | float |
 binary_float | 
            bytelen=4
            
nullable=0
         | real |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | numeric(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | numeric(6,2) |
 bit (mysql) | 
            bitlen=32
            
nullable=0
         | varchar(32) |
 bit | 
            bytelen=1
            
nullable=0
         | bit |
 blob | 
            nullable=0
         | varbinary(max) |
 bool | 
            bytelen=1
            
nullable=0
         | bit |
 boolean | 
            bytelen=1
            
nullable=0
         | bit |
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
         | char(10) |
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
         | varchar(max) |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) |
 date | 
            nullable=0
         | datetime2(0) |
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
         | datetime2(0) |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 datetime (sybase) | 
            nullable=0
         | datetime2(3) |
 datetime | 
            nullable=0
         | datetime |
 datetime2 | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | datetimeoffset(0) |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | datetimeoffset(0) |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | xml |
 dbclob | 
            nullable=0
         | nvarchar(max) |
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
         | numeric(10,3) |
 decimal | 
            prec=6
            
nullable=0
         | numeric(6) |
 double | 
            bytelen=8
            
nullable=0
         | float |
 epoch | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
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
         | nchar(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | hierarchyid |
 image | 
            nullable=0
         | varbinary(max) |
 image (sybase) | 
            nullable=0
         | varbinary(max) |
 ingresdate | 
            nullable=0
         | datetime2(0) |
 int unsigned | 
            bytelen=4
            
nullable=0
         | bigint |
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
         | smallint |
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
         | datetime2(0) |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | datetime2(0) |
 interval month to second | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 interval year to month (ingres) | 
            nullable=0
         | datetime2(0) |
 interval year to month | 
            yearprec=0
            
nullable=0
         | datetime2(0) |
 json | 
            encoding=UTF-8
            
nullable=0
         | varchar(max) |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | varchar(max) |
 long byte | 
            nullable=0
         | varbinary(max) |
 long char | 
            encoding=UTF-8
            
nullable=0
         | varchar(max) |
 long nvarchar (db2) | 
            nullable=0
         | nvarchar(max) |
 long nvarchar | 
            nullable=0
         | nvarchar(max) |
 long raw | 
            nullable=0
         | varbinary(max) |
 long varbinary | 
            nullable=0
         | varbinary(max) |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | varchar(max) |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | varchar(max) |
 long | 
            encoding=UTF-8
            
nullable=0
         | varchar(max) |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | int |
 mediumint | 
            bytelen=3
            
nullable=0
         | int |
 money (ingres) | 
            nullable=0
         | money |
 money | 
            nullable=0
         | money |
 nchar | 
            charlen=10
            
nullable=0
         | nchar(10) |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | nchar(10) |
 nclob | 
            nullable=0
         | nvarchar(max) |
 ntext | 
            nullable=0
         | nvarchar(max) |
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
         | numeric(10,3) |
 number | 
            prec=26
            
nullable=0
         | numeric(26) |
 number | 
            prec=6
            
nullable=0
         | int |
 numeric (db2i) | 
            prec=10
            
scale=3
            
nullable=0
         | numeric(10,3) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | numeric(6) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | numeric(10,3) |
 numeric | 
            prec=26
            
nullable=0
         | numeric(26) |
 numeric | 
            prec=6
            
nullable=0
         | numeric(6) |
 nvarchar | 
            charlen=10
            
nullable=0
         | nvarchar(10) |
 nvarchar(max) | 
            nullable=0
         | nvarchar(max) |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | nvarchar(10) |
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
         | datetimeoffset(0) |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | varchar(50) |
 postgres numeric | 
            bytelen=14
            
prec=6
            
nullable=0
         | numeric(6) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | numeric(10,3) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | numeric(20,20) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | numeric(18) |
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
         | varbinary(10) |
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
         | smalldatetime |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | int |
 smallint | 
            bytelen=2
            
nullable=0
         | smallint |
 smallmoney | 
            nullable=0
         | smallmoney |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | varchar(max) |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | varchar(max) |
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
         | datetimeoffset(0) |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
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
         | datetime2(0) |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | datetimeoffset(0) |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | datetimeoffset(0) |
 timestamp | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | smallint |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | tinyint |
 tinyint | 
            bytelen=1
            
nullable=0
         | tinyint |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | uniqueidentifier |
 unitext | 
            nullable=0
         | nvarchar(max) |
 univarchar | 
            charlen=10
            
nullable=0
         | nvarchar(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | numeric(20) |
 unsigned int | 
            bytelen=4
            
nullable=0
         | bigint |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | int |
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
         | varbinary(max) |
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
         | varchar(max) |
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
         | nvarchar(10) |
 variant | 
            encoding=UTF-8
            
nullable=0
         | varchar(max) |
 xml | 
            nullable=0
         | xml |
 year (mysql) | 
            nullable=0
         | smallint |

