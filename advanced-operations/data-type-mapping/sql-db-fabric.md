# Data Type Mapping for SQL database in Microsoft Fabric - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sql-database-in-microsoft-fabric

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sql-database-in-microsoft-fabric/index.md)

# Data Type Mapping for SQL database in Microsoft Fabric


This section lists the mapping of data types for SQL database in Microsoft Fabric.

## SQL database in Microsoft Fabric as Target


When SQL database in Microsoft Fabric is used as a target location, following is the mapping of Fivetran HVR repository data types to the corresponding data type in SQL database in Microsoft Fabric.
Text in green cell indicates the native data type of the DBMS
 Repository Data Type | Attributes | SQL database in Microsoft Fabric |
 ansidate | 
            nullable=0
         | date |
 bigint | 
            bytelen=8
            
nullable=0
         | bigint |
 binary | 
            bytelen=10
            
nullable=0
         | binary(10) |
 bit | 
            bytelen=1
            
nullable=0
         | bit |
 char | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | char(10) |
 char | 
            bytelen=18
            
encoding=WINDOWS-1252
            
nullable=0
         | char(18) |
 char | 
            bytelen=2000
            
encoding=WINDOWS-1252
            
nullable=0
         | char(2000) |
 char | 
            bytelen=4000
            
encoding=WINDOWS-1252
            
nullable=0
         | char(4000) |
 char | 
            bytelen=8000
            
encoding=WINDOWS-1252
            
nullable=0
         | char(8000) |
 datetime | 
            nullable=0
         | datetime |
 datetime2 | 
            timeprec=0
            
nullable=0
         | datetime2(0) |
 datetime2 | 
            timeprec=3
            
nullable=0
         | datetime2(3) |
 datetime2 | 
            timeprec=6
            
nullable=0
         | datetime2(6) |
 datetimeoffset | 
            timeprec=0
            
nullable=0
         | datetimeoffset(0) |
 float | 
            bytelen=8
            
nullable=0
         | float |
 hierarchyid | 
            bytelen=892
            
nullable=0
         | hierarchyid |
 image | 
            nullable=0
         | varbinary(max) |
 int | 
            bytelen=4
            
nullable=0
         | int |
 money | 
            nullable=0
         | money |
 nchar | 
            charlen=10
            
nullable=0
         | nchar(10) |
 ntext | 
            nullable=0
         | nvarchar(max) |
 numeric | 
            prec=6
            
nullable=0
         | numeric(6) |
 numeric | 
            prec=6
            
scale=2
            
nullable=0
         | numeric(6,2) |
 numeric | 
            prec=9
            
scale=3
            
nullable=0
         | numeric(9,3) |
 numeric | 
            prec=10
            
scale=3
            
nullable=0
         | numeric(10,3) |
 numeric | 
            prec=18
            
nullable=0
         | numeric(18) |
 numeric | 
            prec=20
            
nullable=0
         | numeric(20) |
 numeric | 
            prec=20
            
scale=20
            
nullable=0
         | numeric(20,20) |
 numeric | 
            prec=26
            
nullable=0
         | numeric(26) |
 nvarchar | 
            charlen=10
            
nullable=0
         | nvarchar(10) |
 nvarchar(max) | 
            nullable=0
         | nvarchar(max) |
 real | 
            bytelen=4
            
nullable=0
         | real |
 rowversion | 
            bytelen=8
            
nullable=0
         | binary(8) |
 smalldatetime | 
            nullable=0
         | smalldatetime |
 smallint | 
            bytelen=2
            
nullable=0
         | smallint |
 smallmoney | 
            nullable=0
         | smallmoney |
 text (sqlserver) | 
            encoding=WINDOWS-1252
            
nullable=0
         | varchar(max) |
 time | 
            timeprec=0
            
nullable=0
         | time(0) |
 time | 
            timeprec=3
            
nullable=0
         | time(3) |
 time | 
            timeprec=6
            
nullable=0
         | time(6) |
 timestamp (sqlserver) | 
            bytelen=8
            
nullable=0
         | binary(8) |
 tinyint | 
            bytelen=1
            
nullable=0
         | tinyint |
 uniqueidentifier | 
            bytelen=16
            
nullable=0
         | uniqueidentifier |
 varbinary | 
            bytelen=10
            
nullable=0
         | varbinary(10) |
 varbinary(max) | 
            nullable=0
         | varbinary(max) |
 varchar | 
            bytelen=10
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(10) |
 varchar | 
            bytelen=32
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(32) |
 varchar | 
            bytelen=41
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(41) |
 varchar | 
            bytelen=42
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(42) |
 varchar | 
            bytelen=50
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(50) |
 varchar | 
            bytelen=80
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(80) |
 varchar | 
            bytelen=100
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(100) |
 varchar | 
            bytelen=200
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(200) |
 varchar | 
            bytelen=4000
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(4000) |
 varchar | 
            bytelen=8000
            
encoding=WINDOWS-1252
            
nullable=0
         | varchar(8000) |
 varchar(max) | 
            encoding=WINDOWS-1252
            
nullable=0
         | varchar(max) |
 xml | 
            nullable=0
         | xml |

