# Supported Character Encodings - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/supported-character-encodings/index.md)

# Supported Character Encodings


Fivetran HVR supports a large number of character encodings for each DBMSs.

## Db2 for i


HVR supports the following character encodings for [Db2 for i](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-i-requirements):

- GBK
- GBK-FULLWIDTH
- IBM037
- IBM273
- IBM277
- IBM278
- IBM280
- IBM284
- IBM285
- IBM297
- IBM500
- IBM833 <b>Since</b> v6.1.0/31
- IBM836
- IBM838 <b>Since</b> v6.1.0/31
- IBM870 <b>Since</b> v6.1.0/31
- IBM871
- IBM875
- IBM930 <b>Since</b> v6.2.0/18, <b>Since</b> v6.2.5/8
- IBM933 <b>Since</b> v6.1.0/59, <b>Since</b> v6.1.5/8
- IBM937 <b>Since</b> v6.1.0/36
- IBM939 <b>Since</b> v6.1.0/32
- IBM943 As CHAR FOR BIT DATA or BINARY types only *
- IBM1025 <b>Since</b> v6.1.0/31
- IBM1026 <b>Since</b> v6.1.0/31
- IBM1047
- IBM1123 <b>Since</b> v6.1.0/31
- IBM1156 <b>Since</b> v6.1.0/59, <b>Since</b> v6.1.5/9
- IBM1157 <b>Since</b> v6.1.0/59, <b>Since</b> v6.1.5/9
- IBM1364 <b>Since</b> v6.1.0/59, <b>Since</b> v6.1.5/8
- IBM1388 <b>Since</b> v6.1.0/32
- IBM00924
- IBM01140
- IBM01141
- IBM01142
- IBM01143
- IBM01144
- IBM01145
- IBM01146
- IBM01147
- IBM01148
- IBM01149
- IBM28709 <b>Since</b> v6.1.0/36
- IBM-935-DB2I
- US-ASCII
- UTF-8
- UTF-16BE / UTF-16LE
- WINDOWS-1251
- WINDOWS-1252


> **Note:** 
* For Db2 for i some character encodings are supported as a binary data (HEX codes of symbols) stored in CHAR FOR BIT DATA or BINARY column types only. To capture such columns the HVR_DB_CHARSET_BITDATA or HVR_DB_CHARSET_BITDATA (respectively) environment variable should be set in a channel to instruct HVR to treat CCSID 65535 data as character data with the specified encoding.


## Db2 for Linux, Unix and Windows


HVR supports the following character encodings for [Db2 for Linux, Unix and Windows](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-linux-unix-and-windows-requirements):

- GBK
- IBM943 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- ISO-8859-1
- ISO-8859-2
- ISO-8859-5
- ISO-8859-6 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- ISO-8859-9
- ISO-8859-15
- UTF-8
- WINDOWS-874 ("TIS620-1")  <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- WINDOWS-950 ("Big5") <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- WINDOWS-1250 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- WINDOWS-1251
- WINDOWS-1252
- WINDOWS-1253 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- WINDOWS-1254 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- WINDOWS-1255 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- WINDOWS-1256 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- WINDOWS-1257 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- WINDOWS-1258 <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9


## Db2 for z/OS


HVR supports the following character encodings for [Db2 for z/OS](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/db2-for-z-os-requirements):

- GBK
- GBK-FULLWIDTH
- IBM037
- IBM273
- IBM277
- IBM278
- IBM280
- IBM284
- IBM285
- IBM297
- IBM500
- IBM833 <b>Since</b> v6.1.0/31
- IBM836
- IBM838 <b>Since</b> v6.1.0/31
- IBM870 <b>Since</b> v6.1.0/31
- IBM871
- IBM875
- IBM930 <b>Since</b> v6.2.0/18, <b>Since</b> v6.2.5/8
- IBM933 <b>Since</b> v6.1.0/59, <b>Since</b> v6.1.5/8
- IBM937 <b>Since</b> v6.1.0/36
- IBM939 <b>Since</b> v6.1.0/32
- IBM943 <b>Since</b> v6.1.0/32
- IBM1025 <b>Since</b> v6.1.0/31
- IBM1026 <b>Since</b> v6.1.0/31
- IBM1047
- IBM1123 <b>Since</b> v6.1.0/31
- IBM1156 <b>Since</b> v6.1.0/59, <b>Since</b> v6.1.5/9
- IBM1157 <b>Since</b> v6.1.0/59, <b>Since</b> v6.1.5/9
- IBM1364 <b>Since</b> v6.1.0/59, <b>Since</b> v6.1.5/8
- IBM1388 <b>Since</b> v6.1.0/32
- IBM00924
- IBM01140
- IBM01141
- IBM01142
- IBM01143
- IBM01144
- IBM01145
- IBM01146
- IBM01147
- IBM01148
- IBM01149
- IBM01162 <b>Since</b> v6.1.0/32
- IBM28709 <b>Since</b> v6.1.0/36
- IBM-935
- US-ASCII
- UTF-8
- UTF-16BE
- WINDOWS-1251
- WINDOWS-1252


## Google BigQuery


HVR supports the following character encoding for [Google BigQuery](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/google-bigquery-requirements):

- UTF-8-NONUL (zero byte 0x00 is not supported in this encoding)


## Greenplum


HVR supports the following character encodings for [Greenplum](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/greenplum-requirements):

- ISO-8859-1
- UTF-8-NONUL (zero byte 0x00 is not supported in this encoding)
- WINDOWS-1252


## Ingres


HVR supports the following character encodings for [Ingres](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/ingres-requirements):

- ISO-8859-1
- ISO-8859-15 <b>Since</b> v6.1.0/12
- UTF-8
- UTF-16BE / UTF-16LE
- WINDOWS-1252


> **Important:** 
There is a known issue in Ingres when using prepared statements to insert data with UTF-8 encoding into columns with the LONG VARCHAR data type. This can sometimes cause the data to be corrupted. 
 For further assistance on addressing this issue (Ingres issue number II-11621), refer to [Ingres documentation](https://docs.actian.com/ingres) or contact Actian Ingres support.


## MySQL


HVR supports the following character encodings for [MySQL](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/mysql-requirements):

- GBK
- UCS-2BE
- US-ASCII
- UTF-8
- UTF-8-BMP
- UTF-16BE
- WINDOWS-1251
- WINDOWS-1252


## Oracle


HVR supports the following character encodings for [Oracle](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/oracle-requirements):

- CESU-8
- CL8ISO8859P5MN
- GBK
- ISO-8859-1
- ISO-8859-5
- ISO-8859-6 <b>Since</b> v6.1.5/7, <b>Since</b> v6.1.0/53
- ISO-8859-9 <b>Since</b> v6.1.0/75, <b>Since</b> v6.2.0/13, <b>Since</b> v6.2.5/5
- ISO-8859-15
- JA16SJIS <b>Since</b> v6.1.5/7, <b>Since</b> v6.1.0/54
- TH8TISASCII <b>Since</b> v6.1.0/32
- US-ASCII
- UTF-8
- UTF-16BE / UTF-16LE
- WINDOWS-949
- WINDOWS-1252


## PostgreSQL


HVR supports the following character encodings for [PostgreSQL](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/postgresql-requirements):

- UTF8 (zero byte 0x00 is not supported in this encoding)
- ISO_8859_5
- ISO_8859_6 <b>Since</b> v6.1.5/8
- LATIN1 (ISO88591)
- LATIN5 <b>Since</b> v6.1.5/8
- LATIN9 <b>Since</b> v6.1.5/8
- WIN1250 <b>Since</b> v6.1.5/8
- WIN1251
- WIN1252
- WIN1253 <b>Since</b> v6.1.5/8
- WIN1254 <b>Since</b> v6.1.5/8
- WIN1255 <b>Since</b> v6.1.5/8
- WIN1256 <b>Since</b> v6.1.5/8
- WIN1257 <b>Since</b> v6.1.5/8
- WIN1258 <b>Since</b> v6.1.5/8


> **Important:** 
Special characters in table and column names are not supported for PostgreSQL.


## Redshift


HVR supports the following character encoding for [Redshift](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/redshift-requirements):

- UTF-8-BMP-NONUL (zero byte 0x00 is not supported in this encoding)


## SAP HANA


HVR supports the following character encoding for [SAP HANA](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements):

- CESU-8-REG


## SingleStore


HVR supports the following character encoding for [SingleStore](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/singlestore-requirements):

- UTF-8-BMP


## Snowflake


HVR supports the following character encoding for [Snowflake](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/snowflake-requirements):

- UTF-8


## SQL Server


HVR supports the following character encodings for [SQL Server](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sql-server-requirements):

- IBM437
- IBM850
- UTF-8 <b>Since</b> v6.1.0/83, <b>Since</b> v6.2.0/21, <b>Since</b> v6.2.5/9
- UTF-16LE
- WINDOWS-874
- WINDOWS-932
- WINDOWS-936
- WINDOWS-949
- WINDOWS-950
- WINDOWS-1250
- WINDOWS-1251
- WINDOWS-1252
- WINDOWS-1253
- WINDOWS-1254
- WINDOWS-1255
- WINDOWS-1256
- WINDOWS-1257
- WINDOWS-1258


## Sybase ASE


HVR supports the following character encodings for [Sybase ASE](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sybase-ase-requirements):

- IBM437
- IBM850
- GBK
- ISO-8859-1
- ISO-8859-5
- ISO-8859-15
- UTF-8
- UTF-16BE / UTF-16LE
- WINDOWS-874
- WINDOWS-932
- WINDOWS-936
- WINDOWS-949
- WINDOWS-950
- WINDOWS-1250
- WINDOWS-1251
- WINDOWS-1252
- WINDOWS-1253
- WINDOWS-1254
- WINDOWS-1255
- WINDOWS-1256
- WINDOWS-1257
- WINDOWS-1258


## Teradata


HVR supports the following character encodings for [Teradata](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/teradata-requirements):

- ISO-8859-1
- UTF-8
- UTF-16BE / UTF-16LE


> **Note:** 
There are some code points not supported by Teradata. You can find the full list here:
[Unsupported Teradata Codepoints.txt](https://fivetran.com/assets-docs/hvr6-docs/supported-character-encodings/60918221.txt)

div.multicol > ul {
columns: 2;
-webkit-columns: 2;
-moz-columns: 2;
}
