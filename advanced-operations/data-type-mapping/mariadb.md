# Data Type Mapping for MariaDB - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-mariadb

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-mariadb/index.md)

# Data Type Mapping for MariaDB


This section lists the mapping of data types for MariaDB.

## MariaDB as Source


When MariaDB is used as a source location, following is the mapping of data types in MariaDB to the corresponding Fivetran HVR repository data type.

 MariaDB | Capture Support | Repository Data Type |
 bigint | Native | bigint |
 bigint unsigned | Native | bigint unsigned |
 bit | Native | bit (mysql) |
 bool | Native | tinyint signed |
 boolean | Native | tinyint signed |
 dec | Native | decimal |
 decimal | Native | decimal |
 decimal unsigned | Native | decimal |
 double | Native | double |
 double precision | Native | double |
 double unsigned | Native | double |
 fixed | Native | decimal |
 float | Native | real |
 float unsigned | Native | real |
 int | Native | int |
 int unsigned | Native | int unsigned |
 integer | Native | int |
 mediumint | Native | mediumint |
 mediumint unsigned | Native | mediumint unsigned |
 numeric | Native | decimal |
 real | Native | double |
 smallint | Native | smallint |
 smallint unsigned | Native | smallint unsigned |
 tinyint | Native | tinyint signed |
 date | Native | ansidate |
 datetime | Native | datetime (mysql) |
 time | Native | time (mysql) |
 timestamp | Native | timestamp (mysql) |
 year | Native | smallint |
 binary | Native | binary |
 blob | Native | varbinary(max) |
 char | Native | char |
 char byte | Native | binary |
 json | Native | varchar(max) |
 longblob | Native | varbinary(max) |
 longtext | Native | varchar(max) |
 mediumblob | Native | varbinary(max) |
 mediumtext | Native | varchar(max) |
 text | Native | varchar(max) |
 tinyblob | Native | varbinary(max) |
 tinytext | Native | varchar(max) |
 varbinary | Native | varbinary |
 varchar | Native | varchar |
 geometry | Extended | <<geometry>> |
 geometrycollection | Extended | <<geometrycollection>> |
 linestring | Extended | <<linestring>> |
 multilinestring | Extended | <<multilinestring>> |
 multipoint | Extended | <<multipoint>> |
 multipolygon | Extended | <<multipolygon>> |
 point | Extended | <<point>> |
 polygon | Extended | <<polygon>> |


## MariaDB as Target


When MariaDB is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in MariaDB.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | MariaDB (UTF-8) |
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
         | bit(32) |
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
         | char(10) charset utf8mb4 |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) charset utf8mb4 |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | varchar(4000) charset utf8mb4 |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) charset utf8mb4 |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) charset utf8mb4 |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) charset latin1 |
 char as binary | 
            bytelen=10
            
nullable=0
         | binary(10) |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) charset utf8mb4 |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | varchar(2000) charset utf8mb4 |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) charset utf8mb4 |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) charset latin1 |
 clob | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(200) charset utf8mb4 |
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
         | datetime(3) |
 datetime | 
            nullable=0
         | datetime(3) |
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
         | varchar(80) charset ascii |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | datetime(0) |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
 dbclob | 
            nullable=0
         | longtext charset utf16 |
 decfloat | 
            prec=16
            
nullable=0
         | varchar(42) charset utf8mb4 |
 decfloat | 
            prec=34
            
nullable=0
         | varchar(42) charset utf8mb4 |
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
         | char(10) charset utf16 |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) charset ascii |
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
         | json |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
 long byte | 
            nullable=0
         | longblob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
 long nvarchar (db2) | 
            nullable=0
         | longtext charset utf16 |
 long nvarchar | 
            nullable=0
         | longtext charset utf16 |
 long raw | 
            nullable=0
         | longblob |
 long varbinary | 
            nullable=0
         | longblob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
 long | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
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
         | char(10) charset utf16 |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | char(10) charset utf16 |
 nclob | 
            nullable=0
         | longtext charset utf16 |
 ntext | 
            nullable=0
         | longtext charset utf16 |
 number | 
            nullable=0
         | varchar(50) charset utf8mb4 |
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
         | varchar(10) charset utf16 |
 nvarchar(max) | 
            nullable=0
         | longtext charset utf16 |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | varchar(10) charset utf16 |
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
         | varchar(50) charset utf8mb4 |
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
         | varchar(50) charset utf8mb4 |
 postgres cidr | 
            bytelen=20
            
nullable=0
         | varchar(50) charset utf8mb4 |
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
         | char(18) charset ascii |
 rowversion | 
            bytelen=10
            
nullable=0
         | binary(10) |
 sap decfloat | 
            prec=16
            
nullable=0
         | varchar(42) charset utf8mb4 |
 sap decfloat | 
            prec=34
            
nullable=0
         | varchar(42) charset utf8mb4 |
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
         | varchar(10) charset utf8mb4 |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | longtext charset latin1 |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
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
         | longtext charset utf16 |
 univarchar | 
            charlen=10
            
nullable=0
         | varchar(10) charset utf16 |
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
         | varchar(100) charset ascii |
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
         | varchar(10) charset utf8mb4 |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) charset utf8mb4 |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) charset utf8mb4 |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) charset latin1 |
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
         | varchar(10) charset utf8mb4 |
 varchar (sybase) | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) charset utf8mb4 |
 varchar (sybase) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) charset utf8mb4 |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) charset latin1 |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | longtext charset latin1 |
 varchar2 | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) charset utf8mb4 |
 varchar2 | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) charset utf8mb4 |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) charset latin1 |
 vargraphic | 
            charlen=10
            
nullable=0
         | varchar(10) charset utf16 |
 variant | 
            encoding=UTF-8
            
nullable=0
         | longtext charset utf8mb4 |
 xml | 
            nullable=0
         | longtext charset utf16 |
 year (mysql) | 
            nullable=0
         | year |

