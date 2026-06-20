# Data Type Mapping for Databricks - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-databricks

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-databricks/index.md)

# Data Type Mapping for Databricks


This section lists the mapping of data types for Databricks.

## Databricks as Target


When Databricks is used as a target location, following is the mapping of Fivetran HVR repository data types to the corresponding data type in Databricks.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Databricks |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | binary |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp |
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
         | string |
 binary | 
            bytelen=10
            
nullable=0
         | binary |
 binary_double | 
            bytelen=8
            
nullable=0
         | double |
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
         | string |
 bit | 
            bytelen=1
            
nullable=0
         | boolean |
 blob | 
            nullable=0
         | binary |
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
         | binary |
 byte | 
            bytelen=10
            
nullable=0
         | binary |
 byteint | 
            bytelen=1
            
nullable=0
         | tinyint |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | string |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | string |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | string |
 char as binary | 
            bytelen=10
            
nullable=0
         | binary |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | string |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | string |
 clob | 
            encoding=UTF-8
            
nullable=0
         | string |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | string |
 date | 
            nullable=0
         | timestamp |
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
         | timestamp |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp |
 datetime (sybase) | 
            nullable=0
         | timestamp |
 datetime | 
            nullable=0
         | timestamp |
 datetime2 | 
            timeprec=0
            
nullable=0
         | timestamp |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | timestamp |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | string |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | string |
 dbclob | 
            nullable=0
         | string |
 decfloat | 
            prec=16
            
nullable=0
         | string |
 decfloat | 
            prec=34
            
nullable=0
         | string |
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
         | timestamp |
 float | 
            bytelen=8
            
nullable=0
         | double |
 float4 | 
            bytelen=4
            
nullable=0
         | real |
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
         | string |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | string |
 image | 
            nullable=0
         | binary |
 image (sybase) | 
            nullable=0
         | binary |
 ingresdate | 
            nullable=0
         | timestamp |
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
         | string |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | string |
 interval month to second | 
            timeprec=0
            
nullable=0
         | timestamp |
 interval year to month (ingres) | 
            nullable=0
         | string |
 interval year to month | 
            yearprec=0
            
nullable=0
         | string |
 json | 
            encoding=UTF-8
            
nullable=0
         | string |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | string |
 long byte | 
            nullable=0
         | binary |
 long char | 
            encoding=UTF-8
            
nullable=0
         | string |
 long nvarchar (db2) | 
            nullable=0
         | string |
 long nvarchar | 
            nullable=0
         | string |
 long raw | 
            nullable=0
         | binary |
 long varbinary | 
            nullable=0
         | binary |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | string |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | string |
 long | 
            encoding=UTF-8
            
nullable=0
         | string |
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
         | decimal(14,2) |
 money | 
            nullable=0
         | decimal(19,4) |
 nchar | 
            charlen=10
            
nullable=0
         | string |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | string |
 nclob | 
            nullable=0
         | string |
 ntext | 
            nullable=0
         | string |
 number | 
            nullable=0
         | string |
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
         | string |
 nvarchar(max) | 
            nullable=0
         | string |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | string |
 postgres date | 
            nullable=0
         | date |
 postgres time | 
            timeprec=6
            
nullable=0
         | string |
 postgres timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | string |
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
         | string |
 postgres inet | 
            bytelen=20
            
nullable=0
         | string |
 postgres cidr | 
            bytelen=20
            
nullable=0
         | string |
 raw | 
            bytelen=10
            
nullable=0
         | binary |
 real | 
            bytelen=4
            
nullable=0
         | real |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | string |
 rowversion | 
            bytelen=10
            
nullable=0
         | binary |
 sap decfloat | 
            prec=16
            
nullable=0
         | string |
 sap decfloat | 
            prec=34
            
nullable=0
         | string |
 smalldatetime | 
            nullable=0
         | timestamp |
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
         | decimal(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | string |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | string |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | string |
 time (hana) | 
            nullable=0
         | string |
 time (sybase) | 
            nullable=0
         | string |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | string |
 time with time zone | 
            timeprec=0
            
nullable=0
         | string |
 time | 
            timeprec=0
            
nullable=0
         | string |
 time | 
            timeprec=3
            
nullable=0
         | string |
 time2 | 
            nullable=0
         | string |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | binary |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | binary |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp | 
            timeprec=0
            
nullable=0
         | timestamp |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | tinyint |
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
         | binary |
 unitext | 
            nullable=0
         | string |
 univarchar | 
            charlen=10
            
nullable=0
         | string |
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
         | int |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | string |
 varbinary | 
            bytelen=10
            
nullable=0
         | binary |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | binary |
 varbinary(max) | 
            nullable=0
         | binary |
 varbyte | 
            bytelen=10
            
nullable=0
         | binary |
 varchar | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | string |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | string |
 varchar as varbinary | 
            bytelen=10
            
nullable=0
         | binary |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | binary |
 varchar (sybase) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 varchar (sybase) | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | string |
 varchar (sybase) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | string |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | string |
 varchar2 | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 varchar2 | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | string |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | string |
 vargraphic | 
            charlen=10
            
nullable=0
         | string |
 variant | 
            encoding=UTF-8
            
nullable=0
         | string |
 xml | 
            nullable=0
         | string |
 year (mysql) | 
            nullable=0
         | smallint |

