# Data Type Mapping for Aurora PostgreSQL - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-aurora-postgresql

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-aurora-postgresql/index.md)

# Data Type Mapping for Aurora PostgreSQL


This section lists the mapping of data types for Aurora PostgreSQL.

## Aurora PostgreSQL as Source


When Aurora PostgreSQL is used as a source location, following is the mapping of data types in Aurora PostgreSQL to the corresponding Fivetran HVR repository data type.
 PostgreSQL Type | Capture Support | Repository Data Type |
 bit | Extended | <<bit>> |
 bool / boolean | Native | boolean |
 box | Extended | <<_box>> |
 bpchar / character | Native | char |
 bytea | Native | blob |
 cidr | Native | postgres cidr**[3](#footnote)** |
 circle | Extended | <<circle>> |
 date | Native | postgres date |
 datemultirange | Extended | <<datemultirange>> |
 daterange | Extended | <<daterange>> |
 float4 / real | Native | real |
 float8 / double precision | Native | float |
 inet | Native | postgres inet**[3](#footnote)** |
 int2 / smallint / smallserial | Native | smallint |
 int4 / integer / serial | Native | integer |
 int4multirange | Extended | <<int4multirange>> |
 int4range | Extended | <<int4range>> |
 int8 / bigint / bigserial | Native | bigint |
 int8multirange | Extended | <<int8multirange>> |
 int8range | Extended | <<int8range>> |
 interval | Extended | <<interval>> |
 json | Native | json |
 jsonb | Native | jsonb |
 line | Extended | <<line>> |
 lseg / line segment | Extended | <<_lseg>> |
 macaddr | Extended | <<macaddr>> |
 macaddr8 | Extended | <<macaddr8>> |
 money | Extended | <<money>> |
 numeric / decimal | Native | postgres numeric**[2](#footnote)** |
 nummultirange | Extended | <<nummultirange>> |
 numrange | Extended | <<numrange>> |
 oid | Extended | <<oid>> |
 oid8 | Extended | <<oid8>> |
 path | Extended | <<path>> |
 pg_lsn | Extended | <<pg_lsn>> |
 point | Extended | <<point>> |
 polygon | Extended | <<polygon>> |
 text | Native | clob |
 tid | Extended | <<tid>> |
 time / time without time zone | Native | time |
 timestamp / timestamp without time zone | Native | postgres timestamp |
 timestamptz / timestamp with time zone | Native | postgres timestamp with time zone |
 timetz / time with time zone | Native | time with time zone |
 tsmultirange | Extended | <<tsmultirange>> |
 tsquery | Extended | <<tsquery>> |
 tsrange | Extended | <<tsrange>> |
 tstzmultirange | Extended | <<tstzmultirange>> |
 tstzrange | Extended | <<tstzrange>> |
 tsvector | Extended | <<tsvector>> |
 uuid | Native | uniqueidentifier |
 varbit / bit varying | Extended | <<varbit>> |
 varchar / character varying | Native | varchar or clob (if char length is large) |
 xid | Extended | <<xid>> |
 xid8 | Extended | <<xid8>> |
 xml | Native | postgres xml**[1](#footnote)** |

1 - Supported since HVR 6.1.5/10
2 - Supported since HVR 6.3.5/0. In earlier versions, it maps to "number".
3 - Supported since HVR 6.3.5/2


HVR does not support array types, enumerated types, domains, extensions, and user-defined types.

## Aurora PostgreSQL as Target


When Aurora PostgreSQL is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in Aurora PostgreSQL.
Text in green cell indicates the native data type of the DBMS
 HVR Repository Data Types | Attributes | Aurora PostgreSQL (UTF-8) |
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
         | numeric(20) |
 bigint | 
            bytelen=8
            
nullable=0
         | bigint[native] |
 bigtime | 
            timeprec=6
            
nullable=0
         | time(6)[native] |
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
         | bytea[native] |
 bool | 
            bytelen=1
            
nullable=0
         | boolean[native] |
 boolean | 
            bytelen=1
            
nullable=0
         | boolean[native] |
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
         | char(10)[native] |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
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
         | text[native] |
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
         | numeric(10,3)[native] |
 decimal | 
            prec=6
            
nullable=0
         | numeric(6)[native] |
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
         | float[native] |
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
         | integer[native] |
 integer | 
            bytelen=4
            
nullable=0
         | integer[native] |
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
            nullable=0
         | json[native] |
 jsonb | 
            nullable=0
         | jsonb[native] |
 long byte | 
            nullable=0
         | bytea |
 long char | 
            encoding=UTF-8
            
nullable=0
         | char[native] |
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
         | numeric(14,2) |
 money | 
            nullable=0
         | numeric(19,4) |
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
         | numeric[native] |
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
         | numeric(6) |
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
         | date[native] |
 postgres time | 
            timeprec=6
            
nullable=0
         | time(6)[native] |
 postgres timestamp with time zone | 
            timeprec=0
            
nullable=0
         | timestamp(0) with time zone[native] |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | timestamp(0)[native] |
 raw | 
            bytelen=10
            
nullable=0
         | bytea |
 real | 
            bytelen=4
            
nullable=0
         | real[native] |
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
         | smallint[native] |
 smallmoney | 
            nullable=0
         | numeric(10,4) |
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
         | time(0) with time zone[native] |
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
         | uuid[native] |
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
         | numeric(20) |
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
         | varchar(10)[native] |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
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
 xml | 
            nullable=0
         | text |
 year (mysql) | 
            nullable=0
         | smallint |

