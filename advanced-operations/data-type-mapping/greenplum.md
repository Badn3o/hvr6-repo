# Data Type Mapping for Greenplum - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-greenplum

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-greenplum/index.md)

# Data Type Mapping for Greenplum


This section lists the mapping of data types for Greenplum.

## Greenplum as Source


When Greenplum is used as a source location, following is the mapping of data types in Greenplum to the corresponding Fivetran HVR repository data type.

 Greenplum | Alias | Capture Support | Repository Data Type |
 bigint | int8 | Native | bigint |
 bigserial | serial8 | Native | bigint |
 bit |  | Extended | <<bit>> |
 bit varying | varbit | Extended | <<bit varying>> |
 boolean | bool | Native | boolean |
 box |  | Extended | <<box>> |
 bytea |  | Native | blob |
 character | char | Native | char |
 character varying | varchar | Native | varchar |
 cidr |  | Extended | <<cidr>> |
 circle |  | Extended | <<circle>> |
 date |  | Native | postgres date |
 decimal | numeric | Native | decimal |
 double precision | float8, float | Native | float |
 inet |  | Extended | <<inet>> |
 integer | int, int4 | Native | integer |
 interval |  | Extended | <<interval>> |
 json |  | Extended | <<json>> |
 jsonb |  | Extended | <<jsonb>> |
 lseg |  | Extended | <<lseg>> |
 macaddr |  | Extended | <<macaddr>> |
 money |  | Extended | <<money>> |
 path |  | Extended | <<path>> |
 point |  | Extended | <<point>> |
 polygon |  | Extended | <<polygon>> |
 real | float4 | Native | real |
 serial | serial4 | Native | integer |
 smallint | int2 | Native | smallint |
 text |  | Native | clob |
 time without time zone |  | Native | time |
 time with time zone | timetz | Native | time with time zone |
 timestamp without time zone |  | Native | postgres timestamp |
 timestamp with time zone | timestamptz | Native | postgres timestamp with time zone |
 uuid |  | Extended | <<uuid>> |
 xml |  | Extended | <<xml>> |
 txid_snapshot |  | Extended | <<txid_snapshot>> |


## Greenplum as Target


When Greenplum is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in Greenplum.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Greenplum (UTF-8) |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | bytea |
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
         | bytea |
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
         | bytea |
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
         | bytea |
 byte | 
            bytelen=10
            
nullable=0
         | bytea |
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
         | bytea |
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
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
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
         | timestamp(0) |
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
         | bytea |
 image (sybase) | 
            nullable=0
         | bytea |
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
         | text |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | text |
 long byte | 
            nullable=0
         | bytea |
 long char | 
            encoding=UTF-8
            
nullable=0
         | char |
 long nvarchar (db2) | 
            nullable=0
         | text |
 long nvarchar | 
            nullable=0
         | text |
 long raw | 
            nullable=0
         | bytea |
 long varbinary | 
            nullable=0
         | bytea |
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
         | numeric |
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
         | decimal(6) |
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
         | timestamp(0) with time zone |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 postgres numeric | 
            bytelen=510
            
nullable=0
         | numeric |
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
         | bytea |
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
         | bytea |
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
         | bytea |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | bytea |
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
         | bytea |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | bytea |
 varbinary(max) | 
            nullable=0
         | bytea |
 varbyte | 
            bytelen=10
            
nullable=0
         | bytea |
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
         | bytea |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | bytea |
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

