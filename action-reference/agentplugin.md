# AgentPlugin - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/agentplugin

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/agentplugin/index.md)

# AgentPlugin


An agent plugin is a block of user–supplied logic which is executed by Fivetran HVR during replication. An agent plugin can be an operating system command or a database procedure. Each time HVR executes an agent plugin it passes parameters to indicate what stage the job has reached (e.g. start of capture, end of integration etc.). If action **AgentPlugin** is defined on a specific table, then it affects the entire job including data from other tables for that location.

By default, HVR will only execute binaries and scripts available inside **HVR_CONFIG/plugin/agent**, **HVR_CONFIG/plugin/transform**, **HVR_CONFIG/plugin/authentication**, and **HVR_CONFIG/plugin/rewrite**. These directories are not created by default, and must be manually created if required. It is recommended to save custom scripts/agent plugins in these directories. HVR can also execute binaries and scripts available inside other directories if they are safelisted. Directories can be safelisted by defining the property **Allowed_Plugin_Paths** in file **HVR_CONFIG/etc/hvrosaccess.conf**. For reference, the sample configuration file **hvrosaccess.conf_example** can be found in **HVR_HOME/etc/hvrosaccess.conf_example**.

---

## Parameters


This section describes the parameters available for action **AgentPlugin**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from HVR documentation, emails, or demo notes.




### Command


**Argument:** *path*

**Description:** Name of the agent plugin command. This can be a script or an executable.

Scripts can be shell scripts on Unix and batch scripts on Windows or can be files beginning with a 'magic line' (shebang) containing the interpreter for the script e.g. **#!perl**.

Argument *path* can be an absolute or a relative pathname. If a relative pathname is supplied the agents should be located in **HVR_HOME/plugin/agent**, **HVR_HOME/plugin/transform**, **HVR_CONFIG/plugin/agent**, **HVR_CONFIG/plugin/transform**, **HVR_CONFIG/plugin/authentication**, **HVR_CONFIG/plugin/rewrite**, or in a safelisted directory.

This field is disabled when parameter [**DbProc**](#dbproc) is selected.

---

### DbProc


**Argument:** *dbproc*

**Description:** Call database procedure *dbproc* during replication jobs.

The database procedures are called in a new transaction, except [**Burst**](https://fivetran.com/docs/hvr6/action-reference/integrate#method) integrate with [**BurstCommitFrequency**](https://fivetran.com/docs/hvr6/action-reference/integrate#burstcommitfrequency) set to **CYCLE** (the default), when it runs as part of the transaction that updates the destination table. During [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh), it is executed after all tables are refreshed and committed, but before their indexes are recreated.

**DbProc** cannot be used with parameters [**Command**](#command), and [**ExecOnHub**](#execonhub).

This field is disabled when parameter [**Command**](#command) is selected.

---

### UserArgument


**Argument:** *userarg*

**Description:** Pass extra argument *userarg* to each agent plugin execution.

---

### ExecOnHub


**Description:** Execute agent plugin on hub machine instead of location's machine.

This field is disabled when parameter [**DbProc**](#dbproc) is selected.

---

### Order


**Argument:** *int*

**Description:** Order of executing the agent plugin.

---

### Context


**Argument:** *context*

**Description:** Action **AgentPlugin** is effective/applied only if the *context* matches the context defined in [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh). For more information about using Context, see our concept page [Refresh or Compare context](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).

The value should be a context name, specified as a lowercase identifier. It can also have form **!***context*, which means that the action is effective unless the matching *context* is enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

One or more contexts can be enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

---

## Agent Plugin Arguments


If an agent plugin is defined, it is called several times at different points of the replication job. On execution, the first argument that is passed indicates the position in the job, for example **cap_begin** for when the agent plugin is called before capture.

Argument *mode* is either **cap_begin**, **cap_end**, **integ_begin**, **integ_end**, **refr_read_begin**, **refr_read_end**, **refr_write_begin** or **refr_write_end** depending on the position in the replication job where the agent plugin was called. Agent plugins are not called during [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data).

Modes **cap_end** and **integ_end** are passed information about whether data was actually replicated.

Command agent plugins can use **$HVR_TBL_NAMES** or **$HVR_FILE_NAMES** and database procedure agent plugins can use parameter **hvr_changed_tables**. An exception if an integrate job is interrupted; the next time it runs it does not know anymore which tables were changed so it will set these variables to an empty string or **-1**.

Command procedure agent plugins (specified in parameter [**Command**](#command)) are called as follows:
<em> agent mode chn_name loc_name userarg</em>

Database procedure agent plugins (specified in parameter [**DbProc**](#dbproc)) are called as follows:

- 
In Ingres,
execute procedure <em>agent</em> (hvr_agent_mode='<em>mode</em>', hvr_chn_name='<em>chn_name</em>', hvr_loc_name='<em>loc_name</em>', hvr_agent_arg='<em>userarg</em>', hvr_changed_tables=<em>N</em>);

- 
In Oracle,
<em>agent</em> (hvr_agent_mode$=>'<em>mode</em>', hvr_chn_name$=>'<em>chn_name</em>', hvr_loc_name$=>'<em>loc_name</em>', hvr_agent_arg$=>'<em>userarg</em>', hvr_changed_tables$=<em>N</em>);

- 
In SQL Server,
execute <em>agent</em> @hvr_agent_mode='<em>mode</em>', @hvr_chn_name='<em>chn_name</em>', @hvr_loc_name='<em>loc_name</em>', @hvr_agent_arg='<em>userarg</em>', @hvr_changed_tables=<em>N</em>;



> **Note:** 
The parameter **hvr_changed_tables** specifies the number (*N*) of tables that were changed.


---

## Agent Plugin Interpreter


If the agent plugin is a script, HVR will consider its shebang line to execute it with an interpreter. It is recommended that only the interpreter program name is specified here (for example, **#!perl** or **#!python**). It is not required to specify the absolute path in the shebang line. HVR will automatically determine the path for the specified interpreter using the environment variable **PATH**.

---

## Agent Plugin Environment


An agent plugin inherits the environment of its parent process. On the hub, the parent of the agent plugin's parent process is the [**Scheduler**](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler). On a remote Unix machine it is the inetd daemon. On a remote Windows machine it is the HVR Remote Listener service. Differences with the environment of the parent process are as follows:

- 
Environment variable **$HVR_TBL_NAMES** is set to a colon–separated list of tables for which the job is replicating (for example **HVR_TBL_NAMES=tbl1:tbl2:tbl3**). Also variable **$HVR_BASE_NAMES** is set to a colon–separated list of table 'base names', which are prefixed by a schema name if action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties) is defined with parameter [**Schema**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#schema) (for example **HVR_BASE_NAMES=base1:sch2.base2:base3**).
For modes **cap_end** and **integ_end** these variables are restricted to only the tables actually processed. Environment variables **$HVR_TBL_KEYS** and **$HVR_TBL_KEYS_BASE** are colon–separated lists of keys for each table specified in **$HVR_TBL_NAMES** (e.g. **k1,k2:k:k3,k4**). The column list is specified in **$HVR_COL_NAMES** and **$HVR_COL_NAMES_BASE**.

- 
Environment variable **$HVR_CONTEXTS** is defined with a comma–separated list of contexts defined with HVR Refresh or Compare (option **–C***ctx*).

- 
Environment variables **$HVR_VAR_***XXX* are defined for each context variable supplied to HVR Refresh or Compare (option **–V***xxx=val*).

- 
For database locations, environment variable **$HVR_LOC_DB_NAME**, **$HVR_LOC_DB_USER** (unless no value is necessary).

- 
For Oracle locations, the environment variables **$HVR_LOC_DB_USER**, **$ORACLE_HOME** and **$ORACLE_SID** are set and **$ORACLE_HOME/bin** is added to the path.

- 
For Ingres locations the environment variable **$II_SYSTEM** is set and **$II_SYSTEM/ingres/bin** is added to the path.

- 
For SQL Server locations, the environment variables **$HVR_LOC_DB_SERVER**, **$HVR_LOC_DB_NAME**, **$HVR_LOC_DB_USER** and **$HVR_LOC_DB_PWD** are set (unless no value is necessary).

- 
For file locations variables **$HVR_FILE_LOC** and **$HVR_LOC_STATEDIR** are set to the file location's top and state directory respectively.

- For modes **cap_end** and **integ_end** variable **$HVR_FILE_NAMES** is set to a colon–separated list of replicated files, unless this information is not available because of recovery. For mode **integ_end**, the following environment variables are also set: **$HVR_FILE_NROWS** containing colon-separated list of number of rows per file for each file specified in **$HVR_FILE_NAMES** (for example **HVR_FILE_NROWS=1005:1053:1033**); **$HVR_TBL_NROWS** containing colon-separated list of number of rows per table for each table specified in **$HVR_TBL_NAMES**; **$HVR_TBL_CAP_TSTAMP** containing colon-separated list of first row's capture timestamp for each table specified in **$HVR_TBL_NAMES**; **$HVR_TBL_OPS** containing colon-separated list of comma-separated *hvr_op**=**count* pairs per table for each table specified in **$HVR_TBL_NAMES** (for example **HVR_TBL_OPS=1=50,2=52:1=75,2=26:1=256**). If the number of files or tables replicated are extremely large then these values are abbreviated and suffixed with "**...**". If the values are abbreviated, refer to **$HVR_LONG_ENVIRONMENT** for the actual values.


- 
Environment variables with too long values for operating system are abbreviated and suffixed with "**...**". If the values are abbreviated, HVR creates a temporary file containing original values of these environment variables. The format for this temporary file is a JSON map consisting of key value pairs and the absolute path of this file is set in **$HVR_LONG_ENVIRONMENT**.

- 
Any variable defined by action [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) is also set in the agent plugin's environment.

- 
The current working directory for local file locations (not FTP, SFTP, SharePoint/WebDAV, HDFS or S3) is the top directory of the file location. For other locations (e.g. database locations) it is **HVR_TMP**, or **HVR_CONFIG/tmp** if this is not defined.

- 
**stdin** is closed and **stdout** and **stderr** are redirected (via network pipes) to the job's logfiles.



If a command agent plugin encounters a problem it should write an error message and return with exit code 1, which will cause the replication job to fail. If the agent does not want to do anything for a mode or does not recognize the mode (new modes may be added in future HVR versions) then the agent should return exit code 2, without writing an error message.

---

## Examples


This section lists few examples of agent plugin scripts:

##### Example 1: An agent plugin script (in Perl), which prints "hello world"

#!perl # Exit codes: 0=success, 1=error, 2=ignore_mode if($ARGV[0] eq "cap_begin") \{ print "Hello World\n"; exit 0; \} else \{ exit 2; \}

##### Example 2: An agent plugin script (in Perl), which prints out arguments and environment at the end of every integrate cycle

#!perl require 5; if ($ARGV[0] eq "integ_end") \{ print "DEMO INTEGRATE END AGENT ("; foreach $arg (@ARGV) \{ print "$arg "; \} print ")\n"; # print current working directory use Cwd; printf("cwd=%s\n", cwd()); # print (part of the) environment printf("HVR_FILE_NAMES=$ENV\{HVR_FILE_NAMES\}\n"); printf("HVR_FILE_LOC=$ENV\{HVR_FILE_LOC\}\n"); printf("HVR_LOC_STATEDIR=$ENV\{HVR_LOC_STATEDIR\}\n"); printf("HVR_TBL_NAMES=$ENV\{HVR_TBL_NAMES\}\n"); printf("HVR_BASE_NAMES=$ENV\{HVR_BASE_NAMES\}\n"); printf("HVR_TBL_KEYS=$ENV\{HVR_TBL_KEYS\}\n"); printf("HVR_TBL_KEYS_BASE=$ENV\{HVR_TBL_KEYS_BASE\}\n"); printf("HVR_COL_NAMES=$ENV\{HVR_COL_NAMES\}\n"); printf("HVR_COL_NAMES_BASE=$ENV\{HVR_COL_NAMES_BASE\}\n"); printf("PATH=$ENV\{PATH\}\n"); exit 0; # Success \} else \{ exit 2; # Ignore mode \}

##### Example 3: An agent plugin script (in Python), which utilizes $HVR_LONG_ENVIRONMENT to print environment variables at the end of every integrate cycle

 #!python

 import os
 import sys
 import json

 if __name__ == "__main__":
     if sys.argv[1] == 'integ_end':
         if 'HVR_LONG_ENVIRONMENT' in os.environ:
             with open(os.environ['HVR_LONG_ENVIRONMENT'], 'r') as f:
                 long_environment= json.loads(f.read())
         else:
             long_environment= \{\}  # empty dict

         # print (part of the) environment
         if 'HVR_FILE_NAMES' in long_environment:
             print 'HVR_FILE_NAMES=\{0\}'.format(long_environment['HVR_FILE_NAMES'])
         elif 'HVR_FILE_NAMES' in os.environ:
             print 'HVR_FILE_NAMES=\{0\}'.format(os.environ['HVR_FILE_NAMES'])
         else:
             print 'HVR_FILE_NAMES=<not set>'
         if 'HVR_TBL_NAMES' in long_environment:
             print 'HVR_TBL_NAMES=\{0\}'.format(long_environment['HVR_TBL_NAMES'])
         elif 'HVR_TBL_NAMES' in os.environ:
             print 'HVR_TBL_NAMES=\{0\}'.format(os.environ['HVR_TBL_NAMES'])
         else:
             print 'HVR_TBL_NAMES=<not set>'

         if 'HVR_BASE_NAMES' in long_environment:
             print 'HVR_BASE_NAMES=\{0\}'.format(long_environment['HVR_BASE_NAMES'])
         elif 'HVR_BASE_NAMES' in os.environ:
             print 'HVR_BASE_NAMES=\{0\}'.format(os.environ['HVR_BASE_NAMES'])
         else:
             print 'HVR_BASE_NAMES=<not set>'

         sys.exit(0)  # Success
     else:
         sys.exit(2)  # Ignore mode

##### Example 4: A database procedure agent plugin that populates table **order_line** after a refresh.

 create procedure [dbo].[refr_agent] (
    @hvr_agent_mode varchar(20),
    @hvr_chn_name varchar(20),
    @hvr_loc_name varchar(20),
    @hvr_agent_arg varchar(20),
    @hvr_changed_tables numeric
 ) as
 begin
    if @hvr_agent_mode = 'refr_write_begin'
    begin
        begin try
            delete from order_line
        end try
        begin catch
           -- ignore errors; nothing to delete
        end catch
    end
    else if @hvr_agent_mode = 'refr_write_end'
    begin
        insert into order_line
            SELECT i.item_id,
              i.item_no,
              i.description,
              i.attribute,
              i.item_type,
              p.id,
              p.date_set,
              p.price
              FROM items i, price p
    end
 end

.actparam {
    padding-left: 20px;
}
