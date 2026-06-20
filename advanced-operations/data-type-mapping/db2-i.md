# Data Type Mapping for Db2 for i - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-db2-for-i

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-db2-for-i/index.md)

# Data Type Mapping for Db2 for i


This section lists the mapping of data types for Db2 for i.

## Db2 for i as Source


When Db2 for i is used as a source location, following is the mapping of data types in Db2 for i to the corresponding Fivetran HVR repository data type.

 Db2 for i | Capture Support | Repository Data Type |
 bigint | Native | bigint |
 decfloat | Native | decfloat |
 decimal | Native | decimal |
 double | Native | double |
 integer | Native | integer |
 numeric | Native | numeric (db2i) |
 real | Native | real |
 smallint | Native | smallint |
 date | Native | ansidate |
 time | Native | time2 |
 timestamp | Native | timestamp |
 char | Native | char |
 clob | Native | clob |
 varchar | Native | varchar |
 binary | Native | binary |
 blob | Native | blob |
 varbinary | Native | varbinary |
 datalink | Native[2](#footnote) | datalink |
 xml | Native[2](#footnote) | db2 xml |
 rowid | Native[2](#footnote) | db2 rowid |
 binary decimal[3](#footnote) | Native | binary decimal |
 boolean[1](#footnote) | Native | boolean |
 dbclob | Native | clob |
 graphic | Native | nchar |
 vargraphic | Native | nvarchar |
 user defined | Extended | <<user defined>> |


1 - Supported since HVR 6.2.0/0 
2 - Native mapping supported since HVR 6.2.0/2 
3 - Supported since HVR 6.2.0/3 


## Db2 for i as Target


When Db2 for i is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in Db2 for i.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | DB2 for i |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | blob(2147483647) |
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
         | time |
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
         | varchar(32) CCSID 1208 |
 bit | 
            bytelen=1
            
nullable=0
         | smallint |
 blob | 
            nullable=0
         | blob(2147483647) |
 bool | 
            bytelen=1
            
nullable=0
         | smallint |
 boolean | 
            bytelen=1
            
nullable=0
         | smallint |
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
         | char(10) CCSID 1208 |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) CCSID 1208 |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | char(4000) CCSID 1208 |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | char(8000) CCSID 1208 |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(40) CCSID 1208 |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(20) CCSID 1208 |
 char as binary | 
            bytelen=10
            
nullable=0
         | binary(10) |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10) CCSID 1208 |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | char(2000) CCSID 1208 |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(40) CCSID 1208 |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(20) CCSID 1208 |
 clob | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | datalink(200) |
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
         | rowid generated by default |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | xml CCSID 1208 |
 dbclob | 
            nullable=0
         | dbclob(1073741823) CCSID 13488 |
 decfloat | 
            prec=16
            
nullable=0
         | decfloat(16) |
 decfloat | 
            prec=34
            
nullable=0
         | decfloat(34) |
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
         | nchar(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) CCSID 1208 |
 image | 
            nullable=0
         | blob(2147483647) |
 image (sybase) | 
            nullable=0
         | blob(2147483647) |
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
         | timestamp |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | timestamp |
 interval month to second | 
            timeprec=0
            
nullable=0
         | timestamp |
 interval year to month (ingres) | 
            nullable=0
         | timestamp |
 interval year to month | 
            yearprec=0
            
nullable=0
         | timestamp |
 json | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 long byte | 
            nullable=0
         | blob(2147483647) |
 long char | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 long nvarchar (db2) | 
            nullable=0
         | dbclob(1073741823) CCSID 13488 |
 long nvarchar | 
            nullable=0
         | dbclob(1073741823) CCSID 13488 |
 long raw | 
            nullable=0
         | blob(2147483647) |
 long varbinary | 
            nullable=0
         | blob(2147483647) |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 long | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
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
         | nchar(10) |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | nchar(10) |
 nclob | 
            nullable=0
         | dbclob(1073741823) CCSID 13488 |
 ntext | 
            nullable=0
         | dbclob(1073741823) CCSID 13488 |
 number | 
            nullable=0
         | varchar(50) CCSID 1208 |
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
         | integer |
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
         | dbclob(1073741823) CCSID 13488 |
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
         | time |
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
         | varchar(50) CCSID 1208 |
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
         | varchar(50) CCSID 1208 |
 postgres cidr | 
            bytelen=20
            
nullable=0
         | varchar(50) CCSID 1208 |
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
         | char(18) CCSID 1208 |
 rowversion | 
            bytelen=10
            
nullable=0
         | binary(10) |
 sap decfloat | 
            prec=16
            
nullable=0
         | varchar(42) CCSID 1208 |
 sap decfloat | 
            prec=34
            
nullable=0
         | varchar(42) CCSID 1208 |
 smalldatetime | 
            nullable=0
         | timestamp |
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
         | varchar(10) CCSID 1208 |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
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
         | binary(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
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
         | binary(16) |
 unitext | 
            nullable=0
         | dbclob(1073741823) CCSID 13488 |
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
         | varchar(100) CCSID 1208 |
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
         | blob(2147483647) |
 varbyte | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
 varchar | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) CCSID 1208 |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) CCSID 1208 |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(40) CCSID 1208 |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) CCSID 1208 |
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
         | varchar(10) CCSID 1208 |
 varchar (sybase) | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | varchar(8000) CCSID 1208 |
 varchar (sybase) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(40) CCSID 1208 |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) CCSID 1208 |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 varchar2 | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(10) CCSID 1208 |
 varchar2 | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar(40) CCSID 1208 |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) CCSID 1208 |
 vargraphic | 
            charlen=10
            
nullable=0
         | nvarchar(10) |
 variant | 
            encoding=UTF-8
            
nullable=0
         | clob(2147483647) CCSID 1208 |
 xml | 
            nullable=0
         | xml CCSID 1208 |
 year (mysql) | 
            nullable=0
         | smallint |

