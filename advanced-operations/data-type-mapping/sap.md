# Data Type Mapping for SAP - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sap

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/data-type-mapping/data-type-mapping-for-sap/index.md)

# Data Type Mapping for SAP


This section lists the mapping of data types for SAP (or SAP dictionary). This mapping applies when SAP-based databases are used with HVR for replication, such as SAP ECC on Oracle, SAP ECC on HANA, SAP S/4HANA, SAP on DB2, and SAP on SQL Server.

## SAP as Source


When a SAP-based database is used in the source location, following is the mapping of data types in SAP (or SAP dictionary) to the corresponding Fivetran HVR repository data type.

 SAP | Capture Support | Repository Data Type |
 d16r | Native | varbinary / sap decfloat[2](#footnote) |
 d16s | Native | varbinary / sap decfloat[2](#footnote) |
 d34r | Native | varbinary / sap decfloat[2](#footnote) |
 d34s | Native | varbinary / sap decfloat[2](#footnote) |
 raw | Native | varbinary |
 accp | Native | nvarchar |
 char | Native | nvarchar |
 clnt | Native | nvarchar |
 cuky | Native | nvarchar |
 dats | Native | nvarchar / date[1](#footnote) |
 lang | Native | nvarchar |
 numc | Native | nvarchar |
 sstr | Native | nvarchar |
 tims | Native | nvarchar |
 unit | Native | nvarchar |
 lchr | Native | nclob |
 lraw | Native | blob |
 rstr | Native | blob |
 strg | Native | clob |
 curr | Native | decimal(p,s) |
 dec | Native | decimal(p,s) |
 d16d | Native | decfloat |
 d34d | Native | decfloat |
 fltp | Native | float |
 int1 | Native | integer1 |
 int2 | Native | integer2 |
 int4 | Native | integer4 |
 prec | Native | integer2 |
 quan | Native | decimal(p,s) |
 varc | Not supported |  |



1 - For SAP systems on Db2 for i, Db2 for LUW, Oracle, SAP HANA, SAP NetWeaver (on Oracle or HANA), SQL Server, and Sybase ASE databases, if the option **SAP Data Types Conversion** is defined, the `dats` data type will be localized using the source database's date data type and then mapped to the corresponding HVR repository data type. For example, in an SAP system on SQL Server, the `dats` data type will be localized as SQL Server's `date` type, which is then mapped to `ansidate` in HVR repository data type. 


2 - Since HVR 6.3.0/0 and 6.3.5/0, if the environment variable **HVR_SAP_DESCRIBE_HANDLE_RAW_DF=1** is defined, the SAP data types `d16r`, `d16s`, `d34r`, and `d34s` are mapped to the `decfloat(sap)` data type instead of the default `varbinary`.

