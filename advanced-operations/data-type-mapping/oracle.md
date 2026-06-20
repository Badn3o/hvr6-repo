# Data Type Mapping for Oracle - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-oracle

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-oracle/index.md)

# Data Type Mapping for Oracle


This section lists the mapping of data types for Oracle.

## Oracle as Source


When Oracle is used as a source location, following is the mapping of data types in Oracle to the corresponding Fivetran HVR repository data type.

 Oracle | Capture Support | Repository Data Type |
 binary_double | Native | binary_double |
 binary_float | Native | binary_float |
 float | Native | number |
 long | Native | long |
 number | Native | number |
 date | Native | date |
 interval day to second | Native | interval day to second |
 interval year to month | Native | interval year to month |
 timestamp | Native | timestamp (oracle) |
 timestamp with local time zone | Native | timestamp with local tz (oracle) |
 timestamp with time zone | Native | timestamp with tz (oracle) |
 char | Native | char (oracle) |
 nchar | Native | nchar (oracle) |
 nvarchar2 | Native | nvarchar2 |
 varchar | Native | varchar2 |
 [varchar2*](#footnote) | Native | varchar2 |
 long raw | Native | long raw |
 raw | Native | raw |
 bfile | Native | bfile |
 blob | Native | blob |
 clob | Native | clob |
 nclob | Native | nclob |
 rowid | Native | rowid |
 urowid | Native | urowid |
 extended data types | Extended | <<data type>> |
 ref | Extended | <<data type>> |
 varrays | Extended | <<data type>> |
 nested tables | Extended | <<data type>> |
 anytype | Extended | <<data type>> |
 anydata | Extended | <<data type>> |
 anydataset | Extended | <<data type>> |
 uri | Extended | <<data type>> |
 xmltype | Extended | <<xmltype>> |
 sdo_geometry | Extended | <<data type>> |
 sdo_georaster | Extended | <<data type>> |
 sdo_topo_geometry | Extended | <<data type>> |
 media | Extended | <<data type>> |




*HVR does not support varchar2 columns larger than 4000 bytes as key columns.


## Oracle as Target


When Oracle is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in Oracle.

### Oracle (al32utf8)

Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Oracle (AL32UTF8) |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | bfile |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp(6) |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | number(20) |
 bigint | 
            bytelen=8
            
nullable=0
         | number(19) |
 bigtime | 
            timeprec=6
            
nullable=0
         | varchar2(15 byte) |
 binary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 binary_double | 
            bytelen=8
            
nullable=0
         | binary_double |
 binary_float | 
            bytelen=4
            
nullable=0
         | binary_float |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | number(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | number(6,2) |
 bit (mysql) | 
            bitlen=32
            
nullable=0
         | varchar2(32 byte) |
 bit | 
            bytelen=1
            
nullable=0
         | number(1) |
 blob | 
            nullable=0
         | blob |
 bool | 
            bytelen=1
            
nullable=0
         | number(1) |
 boolean | 
            bytelen=1
            
nullable=0
         | number(1) |
 byte varying | 
            bytelen=10
            
nullable=0
         | raw(10) |
 byte | 
            bytelen=10
            
nullable=0
         | raw(10) |
 byteint | 
            bytelen=1
            
nullable=0
         | number(3) |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 byte) |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 byte) |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | varchar2(4000 byte) |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 char) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10 char) |
 char as binary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 byte) |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | char(2000 byte) |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 char) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10 char) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | clob |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar2(200 char) |
 date | 
            nullable=0
         | date |
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
         | timestamp(6) |
 datetime | 
            nullable=0
         | timestamp(6) |
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
         | varchar2(80 byte) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | clob |
 dbclob | 
            nullable=0
         | nclob |
 decfloat | 
            prec=16
            
nullable=0
         | varchar2(42 byte) |
 decfloat | 
            prec=34
            
nullable=0
         | varchar2(42 byte) |
 decimal | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 decimal | 
            prec=6
            
nullable=0
         | number(6) |
 double | 
            bytelen=8
            
nullable=0
         | binary_double |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 float | 
            bytelen=8
            
nullable=0
         | binary_double |
 float4 | 
            bytelen=4
            
nullable=0
         | binary_float |
 float8 | 
            bytelen=8
            
nullable=0
         | binary_double |
 float64 | 
            bytelen=8
            
nullable=0
         | binary_double |
 graphic | 
            charlen=10
            
nullable=0
         | nchar(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar2(4000 byte) |
 image | 
            nullable=0
         | blob |
 image (sybase) | 
            nullable=0
         | long raw |
 ingresdate | 
            nullable=0
         | date |
 int unsigned | 
            bytelen=4
            
nullable=0
         | number(10) |
 int | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer1 | 
            bytelen=1
            
nullable=0
         | number(3) |
 integer2 | 
            bytelen=2
            
nullable=0
         | number(5) |
 integer4 | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer8 | 
            bytelen=8
            
nullable=0
         | number(19) |
 int64 | 
            bytelen=8
            
nullable=0
         | number(19) |
 interval day to second (ingres) | 
            timeprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval month to second | 
            timeprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval year to month (ingres) | 
            nullable=0
         | interval year(0) to month |
 interval year to month | 
            yearprec=0
            
nullable=0
         | interval year(0) to month |
 json | 
            encoding=UTF-8
            
nullable=0
         | clob |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long byte | 
            nullable=0
         | blob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long nvarchar (db2) | 
            nullable=0
         | nclob |
 long nvarchar | 
            nullable=0
         | nclob |
 long raw | 
            nullable=0
         | long raw |
 long varbinary | 
            nullable=0
         | blob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long | 
            encoding=UTF-8
            
nullable=0
         | long |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | number(8) |
 mediumint | 
            bytelen=3
            
nullable=0
         | number |
 money (ingres) | 
            nullable=0
         | number(14,2) |
 money | 
            nullable=0
         | number(19,4) |
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
         | nclob |
 ntext | 
            nullable=0
         | nclob |
 number | 
            nullable=0
         | number |
 number | 
            prec=10
            
scale=-127
            
nullable=0
         | float(10) |
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
         | number(10,3) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | number(6) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 numeric | 
            prec=26
            
nullable=0
         | number(26) |
 numeric | 
            prec=6
            
nullable=0
         | number(6) |
 nvarchar | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 nvarchar(max) | 
            nullable=0
         | nclob |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 postgres date | 
            nullable=0
         | date |
 postgres time | 
            timeprec=6
            
nullable=0
         | varchar2(15 byte) |
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
         | number(6) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | number(12,20) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | number(12,-6) |
 postgres numeric | 
            bytelen=30
            
prec=40
            
nullable=0
         | varchar2(41 byte) |
 postgres inet | 
            bytelen=20
            
nullable=0
         | varchar2(50 byte) |
 postgres cidr | 
            bytelen=20
            
nullable=0
         | varchar2(50 byte) |
 raw | 
            bytelen=10
            
nullable=0
         | raw(10) |
 real | 
            bytelen=4
            
nullable=0
         | binary_float |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | rowid |
 rowversion | 
            bytelen=10
            
nullable=0
         | raw(10) |
 sap decfloat | 
            prec=16
            
nullable=0
         | varchar2(42 byte) |
 sap decfloat | 
            prec=34
            
nullable=0
         | varchar2(42 byte) |
 smalldatetime | 
            nullable=0
         | date |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | number(5) |
 smallint | 
            bytelen=2
            
nullable=0
         | number(5) |
 smallmoney | 
            nullable=0
         | number(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | long |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time (hana) | 
            nullable=0
         | varchar2(8 byte) |
 time (sybase) | 
            nullable=0
         | varchar2(12 byte) |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time with time zone | 
            timeprec=0
            
nullable=0
         | varchar2(14 byte) |
 time | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time | 
            timeprec=3
            
nullable=0
         | varchar2(12 byte) |
 time2 | 
            nullable=0
         | varchar2(8 byte) |
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
         | raw(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
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
         | number(3) |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | number(3) |
 tinyint | 
            bytelen=1
            
nullable=0
         | number(3) |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | raw(16) |
 unitext | 
            nullable=0
         | nclob |
 univarchar | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | number(20) |
 unsigned int | 
            bytelen=4
            
nullable=0
         | number(10) |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | number(5) |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | urowid(75) |
 varbinary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varbinary(max) | 
            nullable=0
         | blob |
 varbyte | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 char) |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 char) |
 varchar as varbinary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar (sybase) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar (sybase) | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 varchar (sybase) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 char) |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 char) |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob |
 varchar2 | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar2 | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 char) |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 char) |
 vargraphic | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 variant | 
            encoding=UTF-8
            
nullable=0
         | clob |
 xml | 
            nullable=0
         | nclob |
 year (mysql) | 
            nullable=0
         | number(4) |


### Oracle (cesu-8)

Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Oracle (CESU-8) |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | bfile |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp(6) |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | number(20) |
 bigint | 
            bytelen=8
            
nullable=0
         | number(19) |
 bigtime | 
            timeprec=6
            
nullable=0
         | varchar2(15 byte) |
 binary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 binary_double | 
            bytelen=8
            
nullable=0
         | binary_double |
 binary_float | 
            bytelen=4
            
nullable=0
         | binary_float |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | number(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | number(6,2) |
 bit (mysql) | 
            bitlen=32
            
nullable=0
         | varchar2(32 byte) |
 bit | 
            bytelen=1
            
nullable=0
         | number(1) |
 blob | 
            nullable=0
         | blob |
 bool | 
            bytelen=1
            
nullable=0
         | number(1) |
 boolean | 
            bytelen=1
            
nullable=0
         | number(1) |
 byte varying | 
            bytelen=10
            
nullable=0
         | raw(10) |
 byte | 
            bytelen=10
            
nullable=0
         | raw(10) |
 byteint | 
            bytelen=1
            
nullable=0
         | number(3) |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(20 char) |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(20 char) |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | clob |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(20 char) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10 char) |
 char as binary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(20 char) |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | clob |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(20 char) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10 char) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | clob |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar2(400 char) |
 date | 
            nullable=0
         | date |
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
         | timestamp(6) |
 datetime | 
            nullable=0
         | timestamp(6) |
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
         | varchar2(80 byte) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | clob |
 dbclob | 
            nullable=0
         | nclob |
 decfloat | 
            prec=16
            
nullable=0
         | varchar2(42 byte) |
 decfloat | 
            prec=34
            
nullable=0
         | varchar2(42 byte) |
 decimal | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 decimal | 
            prec=6
            
nullable=0
         | number(6) |
 double | 
            bytelen=8
            
nullable=0
         | binary_double |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 float | 
            bytelen=8
            
nullable=0
         | binary_double |
 float4 | 
            bytelen=4
            
nullable=0
         | binary_float |
 float8 | 
            bytelen=8
            
nullable=0
         | binary_double |
 float64 | 
            bytelen=8
            
nullable=0
         | binary_double |
 graphic | 
            charlen=10
            
nullable=0
         | nchar(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar2(4000 byte) |
 image | 
            nullable=0
         | blob |
 image (sybase) | 
            nullable=0
         | long raw |
 ingresdate | 
            nullable=0
         | date |
 int unsigned | 
            bytelen=4
            
nullable=0
         | number(10) |
 int | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer1 | 
            bytelen=1
            
nullable=0
         | number(3) |
 integer2 | 
            bytelen=2
            
nullable=0
         | number(5) |
 integer4 | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer8 | 
            bytelen=8
            
nullable=0
         | number(19) |
 int64 | 
            bytelen=8
            
nullable=0
         | number(19) |
 interval day to second (ingres) | 
            timeprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval month to second | 
            timeprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval year to month (ingres) | 
            nullable=0
         | interval year(0) to month |
 interval year to month | 
            yearprec=0
            
nullable=0
         | interval year(0) to month |
 json | 
            encoding=UTF-8
            
nullable=0
         | clob |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long byte | 
            nullable=0
         | blob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long nvarchar (db2) | 
            nullable=0
         | nclob |
 long nvarchar | 
            nullable=0
         | nclob |
 long raw | 
            nullable=0
         | long raw |
 long varbinary | 
            nullable=0
         | blob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long | 
            encoding=UTF-8
            
nullable=0
         | long |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | number(8) |
 mediumint | 
            bytelen=3
            
nullable=0
         | number |
 money (ingres) | 
            nullable=0
         | number(14,2) |
 money | 
            nullable=0
         | number(19,4) |
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
         | nclob |
 ntext | 
            nullable=0
         | nclob |
 number | 
            nullable=0
         | number |
 number | 
            prec=10
            
scale=-127
            
nullable=0
         | float(10) |
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
         | number(10,3) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | number(6) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 numeric | 
            prec=26
            
nullable=0
         | number(26) |
 numeric | 
            prec=6
            
nullable=0
         | number(6) |
 nvarchar | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 nvarchar(max) | 
            nullable=0
         | nclob |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 postgres date | 
            nullable=0
         | date |
 postgres time | 
            timeprec=6
            
nullable=0
         | varchar2(15 byte) |
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
         | number(6) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | number(12,20) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | number(12,-6) |
 postgres numeric | 
            bytelen=30
            
prec=40
            
nullable=0
         | varchar2(41 byte) |
 postgres inet | 
            bytelen=20
            
nullable=0
         | varchar2(50 byte) |
 postgres cidr | 
            bytelen=20
            
nullable=0
         | varchar2(50 byte) |
 raw | 
            bytelen=10
            
nullable=0
         | raw(10) |
 real | 
            bytelen=4
            
nullable=0
         | binary_float |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | rowid |
 rowversion | 
            bytelen=10
            
nullable=0
         | raw(10) |
 sap decfloat | 
            prec=16
            
nullable=0
         | varchar2(42 byte) |
 sap decfloat | 
            prec=34
            
nullable=0
         | varchar2(42 byte) |
 smalldatetime | 
            nullable=0
         | date |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | number(5) |
 smallint | 
            bytelen=2
            
nullable=0
         | number(5) |
 smallmoney | 
            nullable=0
         | number(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(20 char) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | long |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time (hana) | 
            nullable=0
         | varchar2(8 byte) |
 time (sybase) | 
            nullable=0
         | varchar2(12 byte) |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time with time zone | 
            timeprec=0
            
nullable=0
         | varchar2(14 byte) |
 time | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time | 
            timeprec=3
            
nullable=0
         | varchar2(12 byte) |
 time2 | 
            nullable=0
         | varchar2(8 byte) |
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
         | raw(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
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
         | number(3) |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | number(3) |
 tinyint | 
            bytelen=1
            
nullable=0
         | number(3) |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | raw(16) |
 unitext | 
            nullable=0
         | nclob |
 univarchar | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | number(20) |
 unsigned int | 
            bytelen=4
            
nullable=0
         | number(10) |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | number(5) |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | urowid(75) |
 varbinary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varbinary(max) | 
            nullable=0
         | blob |
 varbyte | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(20 char) |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(20 char) |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 char) |
 varchar as varbinary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar (sybase) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(20 char) |
 varchar (sybase) | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 varchar (sybase) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(20 char) |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 char) |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob |
 varchar2 | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(20 char) |
 varchar2 | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(20 char) |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 char) |
 vargraphic | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 variant | 
            encoding=UTF-8
            
nullable=0
         | clob |
 xml | 
            nullable=0
         | nclob |
 year (mysql) | 
            nullable=0
         | number(4) |


### Oracle (windows-1252)

Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Oracle (Windows-1252) |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | bfile |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp(6) |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | number(20) |
 bigint | 
            bytelen=8
            
nullable=0
         | number(19) |
 bigtime | 
            timeprec=6
            
nullable=0
         | varchar2(15 byte) |
 binary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 binary_double | 
            bytelen=8
            
nullable=0
         | binary_double |
 binary_float | 
            bytelen=4
            
nullable=0
         | binary_float |
 binary decimal | 
            prec=9
            
scale=3
            
nullable=0
         | number(9,3) |
 binary decimal | 
            prec=6
            
scale=2
            
nullable=0
         | number(6,2) |
 bit (mysql) | 
            bitlen=32
            
nullable=0
         | varchar2(32 byte) |
 bit | 
            bytelen=1
            
nullable=0
         | number(1) |
 blob | 
            nullable=0
         | blob |
 bool | 
            bytelen=1
            
nullable=0
         | number(1) |
 boolean | 
            bytelen=1
            
nullable=0
         | number(1) |
 byte varying | 
            bytelen=10
            
nullable=0
         | raw(10) |
 byte | 
            bytelen=10
            
nullable=0
         | raw(10) |
 byteint | 
            bytelen=1
            
nullable=0
         | number(3) |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 byte) |
 char | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 byte) |
 char | 
            bytelen=4000
            
encoding=UTF-8
            
nullable=0
         | varchar2(4000 byte) |
 char | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 char | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 byte) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10 byte) |
 char as binary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 char (oracle) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 byte) |
 char (oracle) | 
            bytelen=2000
            
encoding=UTF-8
            
nullable=0
         | char(2000 byte) |
 char (oracle) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | char(10 byte) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10 byte) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | clob |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar2(200 byte) |
 date | 
            nullable=0
         | date |
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
         | timestamp(6) |
 datetime | 
            nullable=0
         | timestamp(6) |
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
         | varchar2(80 byte) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | clob |
 dbclob | 
            nullable=0
         | nclob |
 decfloat | 
            prec=16
            
nullable=0
         | varchar2(42 byte) |
 decfloat | 
            prec=34
            
nullable=0
         | varchar2(42 byte) |
 decimal | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 decimal | 
            prec=6
            
nullable=0
         | number(6) |
 double | 
            bytelen=8
            
nullable=0
         | binary_double |
 epoch | 
            timeprec=0
            
nullable=0
         | timestamp(0) |
 float | 
            bytelen=8
            
nullable=0
         | binary_double |
 float4 | 
            bytelen=4
            
nullable=0
         | binary_float |
 float8 | 
            bytelen=8
            
nullable=0
         | binary_double |
 float64 | 
            bytelen=8
            
nullable=0
         | binary_double |
 graphic | 
            charlen=10
            
nullable=0
         | nchar(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar2(4000 byte) |
 image | 
            nullable=0
         | blob |
 image (sybase) | 
            nullable=0
         | long raw |
 ingresdate | 
            nullable=0
         | date |
 int unsigned | 
            bytelen=4
            
nullable=0
         | number(10) |
 int | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer1 | 
            bytelen=1
            
nullable=0
         | number(3) |
 integer2 | 
            bytelen=2
            
nullable=0
         | number(5) |
 integer4 | 
            bytelen=4
            
nullable=0
         | number(10) |
 integer8 | 
            bytelen=8
            
nullable=0
         | number(19) |
 int64 | 
            bytelen=8
            
nullable=0
         | number(19) |
 interval day to second (ingres) | 
            timeprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval month to second | 
            timeprec=0
            
nullable=0
         | interval day(0) to second(0) |
 interval year to month (ingres) | 
            nullable=0
         | interval year(0) to month |
 interval year to month | 
            yearprec=0
            
nullable=0
         | interval year(0) to month |
 json | 
            encoding=UTF-8
            
nullable=0
         | clob |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long byte | 
            nullable=0
         | blob |
 long char | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long nvarchar (db2) | 
            nullable=0
         | nclob |
 long nvarchar | 
            nullable=0
         | nclob |
 long raw | 
            nullable=0
         | long raw |
 long varbinary | 
            nullable=0
         | blob |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | clob |
 long | 
            encoding=UTF-8
            
nullable=0
         | long |
 mediumint unsigned | 
            bytelen=3
            
nullable=0
         | number(8) |
 mediumint | 
            bytelen=3
            
nullable=0
         | number |
 money (ingres) | 
            nullable=0
         | number(14,2) |
 money | 
            nullable=0
         | number(19,4) |
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
         | nclob |
 ntext | 
            nullable=0
         | nclob |
 number | 
            nullable=0
         | number |
 number | 
            prec=10
            
scale=-127
            
nullable=0
         | float(10) |
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
         | number(10,3) |
 numeric (db2i) | 
            prec=6
            
nullable=0
         | number(6) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 numeric | 
            prec=26
            
nullable=0
         | number(26) |
 numeric | 
            prec=6
            
nullable=0
         | number(6) |
 nvarchar | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 nvarchar(max) | 
            nullable=0
         | nclob |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 postgres date | 
            nullable=0
         | date |
 postgres time | 
            timeprec=6
            
nullable=0
         | varchar2(15 byte) |
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
         | number(6) |
 postgres numeric | 
            bytelen=16
            
prec=10
            
scale=3
            
nullable=0
         | number(10,3) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=20
            
nullable=0
         | number(12,20) |
 postgres numeric | 
            bytelen=16
            
prec=12
            
scale=-6
            
nullable=0
         | number(12,-6) |
 postgres numeric | 
            bytelen=30
            
prec=40
            
nullable=0
         | varchar2(41 byte) |
 postgres inet | 
            bytelen=20
            
nullable=0
         | varchar2(50 byte) |
 postgres cidr | 
            bytelen=20
            
nullable=0
         | varchar2(50 byte) |
 raw | 
            bytelen=10
            
nullable=0
         | raw(10) |
 real | 
            bytelen=4
            
nullable=0
         | binary_float |
 rowid | 
            bytelen=18
            
charlen=18
            
encoding=US-ASCII
            
nullable=0
         | rowid |
 rowversion | 
            bytelen=10
            
nullable=0
         | raw(10) |
 sap decfloat | 
            prec=16
            
nullable=0
         | varchar2(42 byte) |
 sap decfloat | 
            prec=34
            
nullable=0
         | varchar2(42 byte) |
 smalldatetime | 
            nullable=0
         | date |
 smallint unsigned | 
            bytelen=2
            
nullable=0
         | number(5) |
 smallint | 
            bytelen=2
            
nullable=0
         | number(5) |
 smallmoney | 
            nullable=0
         | number(10,4) |
 text (ingres) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | long |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time (hana) | 
            nullable=0
         | varchar2(8 byte) |
 time (sybase) | 
            nullable=0
         | varchar2(12 byte) |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time with time zone | 
            timeprec=0
            
nullable=0
         | varchar2(14 byte) |
 time | 
            timeprec=0
            
nullable=0
         | varchar2(8 byte) |
 time | 
            timeprec=3
            
nullable=0
         | varchar2(12 byte) |
 time2 | 
            nullable=0
         | varchar2(8 byte) |
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
         | raw(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 timestamp with local time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
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
         | number(3) |
 tinyint unsigned | 
            bytelen=1
            
nullable=0
         | number(3) |
 tinyint | 
            bytelen=1
            
nullable=0
         | number(3) |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | raw(16) |
 unitext | 
            nullable=0
         | nclob |
 univarchar | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | number(20) |
 unsigned int | 
            bytelen=4
            
nullable=0
         | number(10) |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | number(5) |
 urowid | 
            bytelen=100
            
charlen=100
            
encoding=US-ASCII
            
nullable=0
         | urowid(75) |
 varbinary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varbinary(max) | 
            nullable=0
         | blob |
 varbyte | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 varchar | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 byte) |
 varchar as varbinary | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | raw(10) |
 varchar (sybase) | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar (sybase) | 
            bytelen=8000
            
encoding=UTF-8
            
nullable=0
         | clob |
 varchar (sybase) | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 byte) |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | clob |
 varchar2 | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar2 | 
            bytelen=40
            
charlen=10
            
encoding=UTF-8
            
nullable=0
         | varchar2(10 byte) |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar2(10 byte) |
 vargraphic | 
            charlen=10
            
nullable=0
         | nvarchar2(10) |
 variant | 
            encoding=UTF-8
            
nullable=0
         | clob |
 xml | 
            nullable=0
         | nclob |
 year (mysql) | 
            nullable=0
         | number(4) |

