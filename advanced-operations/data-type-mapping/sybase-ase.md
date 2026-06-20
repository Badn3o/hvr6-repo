# Data Type Mapping for Sybase ASE - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sybase-ase

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sybase-ase/index.md)

# Data Type Mapping for Sybase ASE


This section lists the mapping of data types for Sybase ASE.

## Sybase ASE as Source


When Sybase ASE is used as a source location, following is the mapping of data types in Sybase ASE to the corresponding Fivetran HVR repository data type.

 Sybase ASE | Capture Support | Repository Data Type |
 bigint | Native | bigint |
 int | Native | int |
 smallint | Native | smallint |
 tinyint | Native | tinyint |
 unsigned bigint | Native | unsigned bigint |
 unsigned int | Native | unsigned int |
 unsigned smallint | Native | unsgined smallint |
 numeric (precision, scale) | Native | numeric |
 decimal (precision, scale) | Native | decimal |
 double precision | Native | float |
 real | Native | real |
 smallmoney | Native | smallmoney |
 money | Native | money |
 smalldatetime | Native | smalldatetime |
 datetime | Native | datetime (sybase) |
 date | Native | date (sybase) |
 time | Native | time (sybase) |
 bigdatetime | Native | bigdatetime |
 bigtime | Native | bigtime |
 char(n) | Native | char |
 varchar(n) | Native | varchar (sybase) |
 unichar | Native | unichar |
 univarchar | Native | univarchar |
 nchar(n) | Native | char |
 nvarchar(n) | Native | varchar (sybase) |
 text | Native | text (sybase) |
 unitext | Native | unitext |
 binary(n) | Native | binary |
 varbinary(n) | Native | varbinary (sybase) |
 image | Native | image (sybase) |
 bit | Native | bit |
 timestamp | Native | timestamp (sybase) |
 sysname | Native[1](#footnote) | varchar (sybase) |
 longsysname | Native[1](#footnote) | varchar (sybase) |


1 - Native mapping supported since HVR 6.3.0/1 


## Sybase ASE as Target


When Sybase ASE is used as a target location, following is the mapping of HVR repository data types to the corresponding data type in Sybase ASE.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | Sybase ASE |
 ansidate (ingres) | 
            nullable=0
         | date |
 ansidate | 
            nullable=0
         | date |
 bfile | 
            nullable=0
         | image |
 bigdatetime | 
            timeprec=6
            
nullable=0
         | bigdatetime |
 bigint unsigned | 
            bytelen=8
            
nullable=0
         | unsigned bigint |
 bigint | 
            bytelen=8
            
nullable=0
         | bigint |
 bigtime | 
            timeprec=6
            
nullable=0
         | bigtime |
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
         | bit |
 blob | 
            nullable=0
         | image |
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
         | char(40) |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(20) |
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
         | char(40) |
 char (oracle) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(20) |
 clob | 
            encoding=UTF-8
            
nullable=0
         | text |
 datalink | 
            bytelen=800
            
charlen=200
            
encoding=UTF-8
            
nullable=0
         | varchar(800) |
 date | 
            nullable=0
         | bigdatetime |
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
         | bigdatetime |
 datetime (mysql) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 datetime (sybase) | 
            nullable=0
         | datetime |
 datetime | 
            nullable=0
         | bigdatetime |
 datetime2 | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 db2 rowid | 
            bytelen=40
            
nullable=0
         | varchar(80) |
 db2 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 db2 xml | 
            encoding=UTF-8
            
nullable=0
         | text |
 dbclob | 
            nullable=0
         | unitext |
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
         | bigdatetime |
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
         | unichar(10) |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | varchar(4000) |
 image | 
            nullable=0
         | image |
 image (sybase) | 
            nullable=0
         | image |
 ingresdate | 
            nullable=0
         | bigdatetime |
 int unsigned | 
            bytelen=4
            
nullable=0
         | unsigned int |
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
         | bigdatetime |
 interval day to second | 
            timeprec=0
            
dayprec=0
            
nullable=0
         | bigdatetime |
 interval month to second | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 interval year to month (ingres) | 
            nullable=0
         | bigdatetime |
 interval year to month | 
            yearprec=0
            
nullable=0
         | bigdatetime |
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
         | image |
 long char | 
            encoding=UTF-8
            
nullable=0
         | text |
 long nvarchar (db2) | 
            nullable=0
         | unitext |
 long nvarchar | 
            nullable=0
         | unitext |
 long raw | 
            nullable=0
         | image |
 long varbinary | 
            nullable=0
         | image |
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
         | unsigned int |
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
         | unichar(10) |
 nchar (oracle) | 
            bytelen=20
            
charlen=10
            
nullable=0
         | unichar(10) |
 nclob | 
            nullable=0
         | unitext |
 ntext | 
            nullable=0
         | unitext |
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
         | univarchar(10) |
 nvarchar(max) | 
            nullable=0
         | unitext |
 nvarchar2 | 
            charlen=10
            
nullable=0
         | univarchar(10) |
 postgres date | 
            nullable=0
         | date |
 postgres time | 
            timeprec=6
            
nullable=0
         | bigtime |
 postgres timestamp with time zone | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 postgres timestamp | 
            timeprec=0
            
nullable=0
         | bigdatetime |
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
         | unsigned smallint |
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
         | text |
 text(sybase) | 
            encoding=UTF-8
            
nullable=0
         | text |
 time (mysql) | 
            timeprec=0
            
nullable=0
         | bigtime |
 time (hana) | 
            nullable=0
         | bigtime |
 time (sybase) | 
            nullable=0
         | time |
 time with local time zone | 
            timeprec=0
            
nullable=0
         | bigtime |
 time with time zone | 
            timeprec=0
            
nullable=0
         | bigtime |
 time | 
            timeprec=0
            
nullable=0
         | bigtime |
 time | 
            timeprec=3
            
nullable=0
         | bigtime |
 time2 | 
            nullable=0
         | bigtime |
 timestamp (bigquery) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp (databricks) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp (db2) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp (hana) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp (ingres) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp (mysql) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp (oracle) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
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
         | bigdatetime |
 timestamp with local tz (oracle) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp with time zone | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp with tz (oracle) | 
            timeprec=0
            
nullable=0
         | bigdatetime |
 timestamp | 
            timeprec=0
            
nullable=0
         | bigdatetime |
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
         | binary(16) |
 unitext | 
            nullable=0
         | unitext |
 univarchar | 
            charlen=10
            
nullable=0
         | univarchar(10) |
 unsigned bigint | 
            bytelen=8
            
nullable=0
         | unsigned bigint |
 unsigned int | 
            bytelen=4
            
nullable=0
         | unsigned int |
 unsigned smallint | 
            bytelen=2
            
nullable=0
         | unsigned smallint |
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
         | image |
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
         | varchar(40) |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) |
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
         | varchar(40) |
 varchar (sybase) | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) |
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
         | varchar(40) |
 varchar2 | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(20) |
 vargraphic | 
            charlen=10
            
nullable=0
         | univarchar(10) |
 variant | 
            encoding=UTF-8
            
nullable=0
         | text |
 xml | 
            nullable=0
         | unitext |
 year (mysql) | 
            nullable=0
         | smallint |

