# Data Type Mapping for Google BigQuery - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-google-bigquery

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-google-bigquery/index.md)

# Data Type Mapping for Google BigQuery


This section lists the mapping of data types for Google BigQuery.

## Google BigQuery as Target


When Google BigQuery is used as a target location, following is the mapping of Fivetran HVR repository data types to the corresponding data type in Google BigQuery.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | BigQuery |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | bytes |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | datetime |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | numeric |
 bigint | 
            bytelen=8
            
nullable=0
         | int64 |
 bigtime | 
            timeprec=6
            
nullable=0
         | time |
 binary | 
            bytelen=10
            
nullable=0
         | bytes |
 binary_double | 
            bytelen=8
            
nullable=0
         | float64 |
 binary_float | 
            bytelen=4
            
nullable=0
         | float64 |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | numeric |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | numeric |
 bit (mysql) | 
            bitlen=32
            
nullable=0
         | string |
 bit | 
            bytelen=1
            
nullable=0
         | bool |
 blob | 
            nullable=0
         | bytes |
 bool | 
            bytelen=1
            
nullable=0
         | bool |
 boolean | 
            bytelen=1
            
nullable=0
         | bool |
 byte varying | 
            bytelen=10
            
nullable=0
         | bytes |
 byte | 
            bytelen=10
            
nullable=0
         | bytes |
 byteint | 
            bytelen=1
            
nullable=0
         | int64 |
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
         | bytes |
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
         | datetime |
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
         | datetime |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | datetime |
 datetime (sybase) | 
            nullable=0
         | datetime |
 datetime | 
            nullable=0
         | datetime |
 datetime2 | 
            timeprec=0
            
nullable=0
         | datetime |
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
         | numeric |
 decimal | 
            prec=6
            
nullable=0
         | numeric |
 double | 
            bytelen=8
            
nullable=0
         | float64 |
 epoch | 
            timeprec=0
            
nullable=0
         | datetime |
 float | 
            bytelen=8
            
nullable=0
         | float64 |
 float4 | 
            bytelen=4
            
nullable=0
         | float64 |
 float8 | 
            bytelen=8
            
nullable=0
         | float64 |
 float64 | 
            bytelen=8
            
nullable=0
         | float64 |
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
         | bytes |
 image (sybase) | 
            nullable=0
         | bytes |
 ingresdate | 
            nullable=0
         | datetime |
 int unsigned | 
            bytelen=4
            
nullable=0
         | int64 |
 int | 
            bytelen=4
            
nullable=0
         | int64 |
 integer | 
            bytelen=4
            
nullable=0
         | int64 |
 integer1 | 
            bytelen=1
            
nullable=0
         | int64 |
 integer2 | 
            bytelen=2
            
nullable=0
         | int64 |
 integer4 | 
            bytelen=4
            
nullable=0
         | int64 |
 integer8 | 
            bytelen=8
            
nullable=0
         | int64 |
 int64 | 
            bytelen=8
            
nullable=0
         | int64 |
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
         | datetime |
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
         | bytes |
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
         | bytes |
 long varbinary | 
            nullable=0
         | bytes |
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
         | int64 |
 mediumint | 
            bytelen=3
            
nullable=0
         | int64 |
 money (ingres) | 
            nullable=0
         | numeric |
 money | 
            nullable=0
         | numeric |
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
         | float64 |
 number | 
            prec=10
            
scale=3
            
nullable=0
         | numeric |
 number | 
            prec=26
            
nullable=0
         | numeric |
 number | 
            prec=6
            
nullable=0
         | int64 |
 numeric (db2i) | 
            prec=10
            
scale=3
            
nullable=0
         | numeric |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | numeric |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | numeric |
 numeric | 
            prec=26
            
nullable=0
         | numeric |
 numeric | 
            prec=6
            
nullable=0
         | numeric |
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
         | time |
 postgres timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | datetime |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | string |
 postgres numeric | 
            bytelen=14
            
prec=6
            
nullable=0
         | numeric |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | numeric |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | bignumeric |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | numeric |
 postgres numeric | 
            bytelen=30
            
prec=40
            
nullable=0
         | bignumeric |
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
         | bytes |
 real | 
            bytelen=4
            
nullable=0
         | float64 |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | string |
 rowversion | 
            bytelen=10
            
nullable=0
         | bytes |
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
         | datetime |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | int64 |
 smallint | 
            bytelen=2
            
nullable=0
         | int64 |
 smallmoney | 
            nullable=0
         | numeric |
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
         | time |
 time (hana) | 
            nullable=0
         | time |
 time (sybase) | 
            nullable=0
         | time |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | time |
 time with time zone | 
            timeprec=0
            
nullable=0
         | time |
 time | 
            timeprec=0
            
nullable=0
         | time |
 time | 
            timeprec=3
            
nullable=0
         | time |
 time2 | 
            nullable=0
         | time |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | datetime |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | datetime |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | datetime |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | datetime |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | datetime |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | datetime |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | bytes |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | bytes |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | datetime |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | datetime |
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
         | datetime |
 tinyint signed | 
            bytelen=1
            
nullable=0
         | int64 |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | int64 |
 tinyint | 
            bytelen=1
            
nullable=0
         | int64 |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | bytes |
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
         | numeric |
 unsigned int | 
            bytelen=4
            
nullable=0
         | int64 |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | int64 |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | string |
 varbinary | 
            bytelen=10
            
nullable=0
         | bytes |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | bytes |
 varbinary(max) | 
            nullable=0
         | bytes |
 varbyte | 
            bytelen=10
            
nullable=0
         | bytes |
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
         | bytes |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | bytes |
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
         | int64 |

