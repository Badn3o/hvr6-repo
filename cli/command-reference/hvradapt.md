# hvradapt - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvradapt

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvradapt/index.md)

# hvradapt


## Usage


<b>hvradapt</b> [<b>-R</b><em>url</em>][<em>-options</em>] <b>-l</b><em>loc</em> <em>hub chn</em>

## Description


Command **hvradapt** explores base table definitions in an actual database and compares them with the table information in a channel. It then adapts (either adds, replaces or deletes) the table information in the channel to match the base table definitions by modifying the [**HVR_COLUMN**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrcolumn) and [**HVR_TABLE**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrtable) repository tables.

- If a location (<b>-l</b><em>loc</em>) from where the **hvradapt** explores the base table definitions contains a table that is not present in the channel but is matched by the '[table filter](#tablefiltering)' statement, then it is added to the channel.
- If a table is in the channel but is not matched by the 'table filter' statement, then it is deleted from the channel.
- if a table is both matched by the 'table filter' statement and included in the channel but has incorrect column information in the channel, then this column information is updated.
- If a 'table filter' statement is not supplied, then tables are not added or deleted; only the existing column information is updated where necessary.


> **Note:** 
Command **hvradapt** corresponds to the [**Table Selection**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel) dialog in the [User Interface](https://fivetran.com/docs/hvr6/user-interface).


## Options


This section describes the options available for command **hvradapt**.

 Parameter | Description |
 `**-a**` | 
Add new tables to the channel. This option will not re-describe the tables that are already in the channel.

In the User Interface, this option corresponds to the **[Table Selection](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel)** dialog. |
 `**-d**` | 
Delete any tables from channel that are not available in the database.

In the User Interface, this option corresponds to the **[Table Selection](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel)** dialog. |
 `**-f***fname*` | Write (append) a list of modified or added table names to file `*fname*`. This option can be useful in a script which calls **hvradapt** and then does extra steps (for example, run **hvrrefresh**) for tables which were affected (see [example shell script](#shellscripttorunhvradapt) to run **hvradapt**). |
 `**-g***grpname*` | 
Assign table group name *`grpname`* for the tables being added. The `default` table group name is **GENERAL**.

This option cannot be used in combination with option `**-G**`.

In the User Interface, this option corresponds to the **[Group name](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel#tablegroup)** option in the **Table Selection** dialog. |
 `**-G**` | 
Assign dynamic group name from schema. When tables are being added to the channel, the table's schema name is assigned as the table's group name. If tables are selected from multiple schemas, then each table will be assigned to the respective table group named corresponding to its schema name.

This option cannot be used in combination with option `**-g**`.

In the User Interface, this option corresponds to the **[Auto-assign schema as group name](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel#tablegroup)** option in the **Table Selection** dialog. |
 `**-i***letters*` | 
Ignore certain differences.

Value for `*letters*` can contain:

- **c** - Column was dropped.
- **C** - Column was added.
- **d** - Data type changed.
- **D** - Data type family changed.
- **f** - Column range became smaller.
- **F** - Column range became bigger.
- **h** - Distribution key removed.
- **H** - Distribution key added.
- **k** - Unique index removed.
- **K** - Unique index added.
- **n** - Nullability removed.
- **N** - Nullability added.
- **s** - Encoding changed.

 |
 `**-I**` | Ignore data type localization before comparing. This option controls whether HVR should convert the repository data types into data types that could be created in the DBMS. If supplied, **hvradapt** will not convert data types to the native data types of the database. If not supplied, then the data types are converted before they are compared. |
 `**-l***loc*` | Specifies the adapt location *loc*, typically the capture location of a channel. |
 `**-m***mapdocs*` | 
Specifies a table filter statement for defining which base tables in the database should be included (or excluded) in the channel. The table filter statement can contain names of a schema, table, column and/or a pattern (such as **mytbl***). Multiple table filter statements can be supplied in a single command.

The table filter statement can be supplied inline or as a file `*mapdocs*` that contains the table filter statement(s) for a channel. When supplying the file name, the input must start with a **@**, e.g., `**hvradapt -m****@***mapdocs.txt*`.

For more information about the syntax for table filter statement, see sections [Syntax for Table Filtering](#syntaxfortablefiltering) and [Syntax for SAP Table Filtering](#syntaxforsaptablefiltering). |
 `**-R***url*` | 
Remote hub server. Access the hub server running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

This option is required for [remote CLI access](https://fivetran.com/docs/hvr6/command-line-interface). When using this option, command **[hvrlogin](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)** should be run first, for authentication.
 |
 `**-t***tbls*` | Re-describe only specific tables `*tbls*`. This option will not add new tables to the channel. |
 `**-V**` | 
Show views and materialized views.

For Oracle, the materialized views are always shown.

In the User Interface, this option corresponds to the **Show views** checkbox in the [Table Selection](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel) dialog. |
 `**-x**` | Check-only mode. Do not apply any changes to the repository tables. |


## Table Filtering


Command **hvradapt** supplied with table filter statement allows you to define which base tables in the adapt location should be included in or excluded from the channel. Only tables matching any of the given statement will be included or excluded.

### Syntax for Table Filtering


This section describes the syntax for filtering tables. The syntax for filtering SAP tables is described in section [Syntax for SAP Table Filtering](#syntaxforsaptablefiltering).
[<em>schema</em><b>.</b>]<em>tablename</em>

[<em>schema</em><b>.</b>]<em>tablename</em> [<b>-</b><em>tablename</em>]<b>...</b>

- 
Value *schema* can be a literal only and value *tablename* can be a literal or pattern. Pattern matching can be done using the special symbols *****, **?** or **[***characters***]**. The table name must be enclosed in double quotes if the table name contains a space, a special character (*****, **?**, **/**), or a new line. Since HVR 6.1.0/13, if the table name contains the special character **/**, then it is not required to enclose the table name in double quotes.

- 
Special symbol **-** is used to define negative patterns. Tables matching the negative pattern are excluded from the preceding pattern's result. In the following example, the filter selects all tables whose name begins with **t**, but excludes all tables whose name begins with **tmp** or ends with **_temp**.
t* -tmp* -*_temp



> **Note:** 
Empty lines and comments (e.g. **# Test**) are ignored.


#### Examples for Filtering Tables and Schemas


Most of the examples listed in this section are in the table filter file format.
tbl1                 # Match table named 'tbl1' in default schema.

schema1.*            # Match all tables in 'schema1'.

schema2.tbl1         # Match table named 'tbl1' in 'schema2'.

history_*            # Match all tables whose name begins with 'history_' in default schema.

"my table"           # Match table named "my table" in default schema. Use double quotes
                     # if there is a space in table name.

> **Note:** 
A shell script as shown in section [Shell Script to Run hvradapt](#shellscripttorunhvradapt) can be created to run **hvradapt** for checking new or modified tables in a location.


### Syntax for SAP Table Filtering


This section describes the syntax for filtering SAP tables. The syntax for filtering non-SAP tables is described in section [Syntax for Table Filtering](#syntaxfortablefiltering).
<em>tablename </em>[<b>-</b><em>tablename</em>]<b>...</b>

<em>tablename</em>

- 
Value *tablename* can be a literal or a pattern. Pattern matching can be done (only for tables) using the special symbols *****, **?** or **[***characters***]**. For HVR versions up to 6.1.0/12, if the table name contains the special character **/**, then the table name must be enclosed in double quotes.

- 
Special symbol **-** is used to define negative patterns. Tables matching the negative pattern are excluded from the preceding pattern's result. In the following example, the filter selects all tables whose name begins with **t**, but excludes all tables whose name begins with **tmp** or ends with **_temp**.
t* -tmp* -*_temp



> **Note:** 
Empty lines and comments (e.g. **# Test**) are ignored.


#### Examples for Filtering SAP Tables

mara                 # Match table named 'mara' from all modules.

mar*                 # Match all tables whose name begins with 'mar' from all modules.

"/bev1/lut906"       # Match table named '/bev1/lut906' from all modules.
                     # Use double quotes if there is a slash in table name.

## Shell Script to Run hvradapt


A shell script can be created to run **hvradapt** for checking new or modified tables in a location.

The following example demonstrates the use of a shell script to run **hvradapt** for checking new or modified tables in location **loc1** and if any new or modified tables are found in location **loc1**, the script executes the necessary commands to enroll the tables into the channel **mychn**.
#!/bin/sh
hub=myhub                                           # Hub name
chn=mychn                                           # Channel name
src=loc1                                            # Source location name
F=/tmp/adapt_$chn.out                               # File where hvradapt writes list of new or changed tables
hvradapt -f$F -m@/tmp/adapt.tmpl -l$src $hub $chn   # Add new or changed tables from source to channel based on the
                                                    # patterns defined in the pattern file.

if test -f $F                                       # If file $F exists then new or changed tables were detected
then
    hvrsuspend $hub $chn-integ                      # Suspend integrate jobs
    hvractivate -oelj $hub $chn                         # Regenerate supplemental-logging, jobs and enroll info
    hvrrefresh -r$src -t@$F -qrw -cbkr $hub $chn    # Re-create and online refresh tables in file $F
    hvrstart -u -r $hub $chn-integ                  # Re-trigger suspended jobs
    hvradapt -x -l$src $hub $chn                    # Double-check channel now matches target location (optional)    

    rm $F                                           # Remove file with list of new or changed tables
fi

table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
