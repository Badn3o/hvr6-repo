# Data Type Mapping for Ingres - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-ingres

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-ingres/index.md)

# Data Type Mapping for Ingres


This section lists the mapping of data types for Ingres.

## Ingres as Source


When Ingres is used as a source location, following is the mapping of data types in Ingres to the corresponding Fivetran HVR repository data type.

 Ingres | Capture Support | Repository Data Type |
 bigint | Native | integer8 |
 decimal | Native | decimal |
 float | Native | float8 |
 float4 | Native | float4 |
 float8 | Native | float8 |
 integer | Native | integer4 |
 integer1 | Native | integer1 |
 integer2 | Native | integer2 |
 integer4 | Native | integer4 |
 integer8 | Native | integer8 |
 real | Native | float4 |
 smallint | Native | integer2 |
 tinyint | Native | integer1 |
 ansidate | Native | ansidate |
 ingresdate | Native | ingresdate |
 interval day to second | Native | interval day to second (ingres) |
 interval year to month | Native | interval year to month (ingres) |
 time with local time zone | Native | time with local time zone |
 time with time zone | Native | time with time zone |
 time without time zone | Native | time |
 timestamp with local timezone | Native | timestamp with local timezone |
 timestamp with time zone | Native | timestamp with time zone |
 timestamp without time zone | Native | timestamp (ingres) |
 c | Native | c |
 char | Native | char |
 clob | Native | long varchar |
 long nvarchar | Native | long nvarchar |
 long varchar | Native | long varchar |
 nchar | Native | nchar |
 nclob | Native | long nvarchar |
 nvarchar | Native | nvarchar |
 text | Native | text (ingres) |
 varchar | Native | varchar |
 ipv4 | Extended | <<ipv4>> |
 ipv6 | Extended | <<ipv6>> |
 logical_key | Extended | <<logical_key>> |
 money | Native | money (ingres) |
 uuid | Extended | <<uuid>> |
 byte | Native | byte |
 byte varying / varbyte | Native | byte varying |
 long byte | Native | long byte |
 boolean | Native | boolean |
 circularstring | Extended | <<circularstring>> |
 compoundcurve | Extended | <<compoundcurve>> |
 curvepolygon | Extended | <<curvepolygon>> |
 geometry | Extended | <<geometry>> |
 geometrycollection | Extended | <<geometrycollection>> |
 linestring | Extended | <<linestring>> |
 multicurve | Extended | <<multicurve>> |
 multilinestring | Extended | <<multilinestring>> |
 multipoint | Extended | <<multipoint>> |
 multipolygon | Extended | <<multipolygon>> |
 multisurface | Extended | <<multisurface>> |
 point | Extended | <<point>> |
 polygon | Extended | <<polygon>> |
 polyhedralsurface | Extended | <<polyhedralsurface>> |
 tin | Extended | <<tin>> |
 triangle | Extended | <<triangle>> |


## Ingres as Target


When Ingres is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in Ingres.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Ingres (UTF-8) |
 ansidate (ingres) | 
            nullable=0
         | ansidate |
 ansidate | 
            nullable=0
         | ansidate |
 bfile | 
            nullable=0
         | long byte |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | timestamp(6) without time zone |
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
         | time(6) without time zone |
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
         | float4 |
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
         | long byte |
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
         | byte varying(10) |
 byte | 
            bytelen=10
            
nullable=0
         | byte(10) |
 byteint | 
            bytelen=1
            
nullable=0
         | i1 |
 c | 
            bytelen=10
            
encoding=UTF-8
            
nullable=0
         | c10 |
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
         | char(40) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(20) |
 char as binary | 
            bytelen=10
            
nullable=0
         | byte(10) |
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
         | long varchar |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(800) |
 date | 
            nullable=0
         | ingresdate |
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
         | timestamp(0) without time zone |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp(0) without time zone |
 datetime (sybase) | 
            nullable=0
         | ingresdate |
 datetime | 
            nullable=0
         | ingresdate |
 datetime2 | 
            timeprec=0
            
nullable=0
         | timestamp(0) without time zone |
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
         | long varchar |
 dbclob | 
            nullable=0
         | long nvarchar |
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
         | timestamp(0) with local time zone |
 float | 
            bytelen=8
            
nullable=0
         | float |
 float4 | 
            bytelen=4
            
nullable=0
         | float4 |
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
         | varchar(4000) |
 image | 
            nullable=0
         | long byte |
 image (sybase) | 
            nullable=0
         | long byte |
 ingresdate | 
            nullable=0
         | ingresdate |
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
         | interval day to second(0) |
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
         | interval year to month |
 interval year to month | 
            yearprec=0
            
nullable=0
         | interval year to month |
 json | 
            encoding=UTF-8
            
nullable=0
         | long varchar |
 jsonb | 
            encoding=UTF-8
            
nullable=0
         | long varchar |
 long byte | 
            nullable=0
         | long byte |
 long char | 
            encoding=UTF-8
            
nullable=0
         | long varchar |
 long nvarchar (db2) | 
            nullable=0
         | long nvarchar |
 long nvarchar | 
            nullable=0
         | long nvarchar |
 long raw | 
            nullable=0
         | long byte |
 long varbinary | 
            nullable=0
         | long byte |
 long varchar (db2) | 
            encoding=UTF-8
            
nullable=0
         | long varchar |
 long varchar | 
            encoding=UTF-8
            
nullable=0
         | long varchar |
 long | 
            encoding=UTF-8
            
nullable=0
         | long varchar |
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
         | long nvarchar |
 ntext | 
            nullable=0
         | long nvarchar |
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
         | nvarchar(10) |
 nvarchar(max) | 
            nullable=0
         | long nvarchar |
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
         | timestamp(0) without time zone |
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
         | byte varying(10) |
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
         | byte(10) |
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
         | ingresdate |
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
         | text(10) |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | long varchar |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | long varchar |
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
         | time(0) with local time zone |
 time with time zone | 
            timeprec=0
            
nullable=0
         | time(0) with time zone |
 time | 
            timeprec=0
            
nullable=0
         | time(0) without time zone |
 time | 
            timeprec=3
            
nullable=0
         | time(3) without time zone |
 time2 | 
            nullable=0
         | time(0) without time zone |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | timestamp(0) without time zone |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | timestamp(0) without time zone |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | timestamp(0) without time zone |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | timestamp(0) without time zone |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | timestamp(0) with local time zone |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | timestamp(0) without time zone |
 timestamp (sqlserver) | 
            bytelen=10
            
nullable=0
         | byte(10) |
 timestamp (sybase) | 
            bytelen=10
            
nullable=0
         | byte varying(10) |
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
         | timestamp(0) without time zone |
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
         | byte(16) |
 unitext | 
            nullable=0
         | long nvarchar |
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
         | byte varying(10) |
 varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | byte varying(10) |
 varbinary(max) | 
            nullable=0
         | long byte |
 varbyte | 
            bytelen=10
            
nullable=0
         | byte varying(10) |
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
         | varchar(40) |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) |
 varchar as varbinary | 
            bytelen=10
            
nullable=0
         | byte varying(10) |
 varchar as varbinary (sybase) | 
            bytelen=10
            
nullable=0
         | byte varying(10) |
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
         | long varchar |
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
 variant | 
            encoding=UTF-8
            
nullable=0
         | long varchar |
 xml | 
            nullable=0
         | long nvarchar |
 year (mysql) | 
            nullable=0
         | smallint |

