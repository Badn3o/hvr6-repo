# Transform - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/transform

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/transform/index.md)

# Transform


Action **Transform** defines a data mapping that is applied inside the Fivetran HVR pipeline. A transform can either be a command (a script or an executable), or it can be built into HVR. These transform happens after the data has been captured from a location and before it is integrated into the target, and is fed all the data in that job's cycle. To change the contents of a file as HVR reads it or to change its contents as HVR writes it, use action [**FileFormat**](https://fivetran.com/docs/hvr6/action-reference/fileformat) with parameter [**CaptureConverter**](https://fivetran.com/docs/hvr6/action-reference/fileformat#captureconverter) or [**IntegrateConverter**](https://fivetran.com/docs/hvr6/action-reference/fileformat#integrateconverter). This **Transform** action happens between the changes from those converters.

A command transform is fed data in XML format. This is a representation of all the data that passes through HVR pipeline. A definition is in **HVR_HOME/etc/xml/hvr_private.dtd**.

---

## Parameters


This section describes the parameters available for action **Transform**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from HVR documentation, emails, or demo notes.




### Command


**Argument:** *path*

**Description:** Name of the transform command.

This can be a script or an executable. Scripts can be shell scripts on Unix and batch scripts on Windows or can be files beginning with a 'magic line' containing the interpreter for the script e.g. **#!perl**.

Argument *path* can be an absolute or a relative pathname. If a relative pathname is supplied, the agents should be located in **HVR_CONFIG/plugin/transform**.
Expand for more information
A transform command should read from its **stdin** and write the transformed bytes to **stdout**. If a transform command encounters a problem, it should write an error to **stderr** and return with exit code **1**, which will cause the replication jobs to fail. The transform command is called with multiple arguments, which should be defined using parameter [**CommandArguments**](#commandarguments).

This parameter can either be defined on a specific table or on all tables (*****). Defining it on a specific table could be slower because the transform will be stopped and restarted each time the current table name alternates. However, defining it on all tables (*****) requires that all data must go through the transform, which could also be slower and costs extra resource (e.g. disk space for a **Command** transform).
Command Transform Environment
A transform command inherits the environment from its parent process. On the hub, the parent of the transform's parent process is the **Scheduler**. On a remote Unix machine, it is the **inetd** daemon. On a remote Windows machine, it is the HVR Agent Listener service. Differences with the environment process are as follows:

- Environment variables **HVR_CHN_NAME** and **HVR_LOC_NAME** are set.
- Environment variable **HVR_TRANSFORM_MODE** is set to either value **cap**, **integ**, **cmp**, **refr_read** or **refr_write**.
- Environment variable **HVR_CONTEXTS** is defined with a comma-separated list of contexts defined with HVR Refresh or Compare (option <strong>–C</strong>_ctx_).
- Environment variables **HVR_VAR_***XXX* are defined for each context variable supplied to HVR Refresh or Compare (option <strong>–V</strong>_xxx_=_val_).
- Any variable defined by action [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) is also set in the transform's environment, unless parameter [**ExecOnHub**](#execonhub) is defined.
- The current working directory is **HVR_TMP**, or **HVR_CONFIG/tmp**, if this is not defined.
- **stdin** is redirected to a socket (HVR writes the original file contents into this), whereas **stdout** and **stderr** are redirected to separate temporary files. HVR replaces the contents of the original file with the bytes that the transform writes to its **stdout**. Anything that the transform writes to its **stderr** is printed in the job's log file on the hub machine.


---

### CommandArguments


**Argument:** *userarg*

**Description:** Value(s) of parameter(s) for transform (space separated).

---

### SapUnpack


**Description:** Unpack the SAP pool, cluster, and long text table (STXL). By defining this parameter, HVR can capture changes from the SAP pool, cluster, and long text tables (binary STXL data) and transform them into unpacked readable data. For information about the requirements for using this parameter, see section [Requirements for SapUnpack](#requirementsforsapunpack).

In case of a HANA source system, unpacking of STXL table (for long text) is possible only during [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), it is not possible to unpack during [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) from the database log.

This parameter:

- requires [**Burst Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method) defined in the channel.
- must be defined only on the target location. Defining on the source location will result in an error.
- can be used together with parameter [**ExecOnHub**](#execonhub), however, it is not advised because it can have negative impact on the performance.
- should not be used together with action [**AdaptDDL**](https://fivetran.com/docs/hvr6/action-reference/adaptddl) or with the parameter [**Coalesce**](https://fivetran.com/docs/hvr6/action-reference/capture#coalesce) in action [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture).

Additional information about SapUnpack
- 
The SapUnpack functionality works both with Unicode and non-Unicode SAP systems (**since** v6.1.0/14). For more information about the non-Unicode SAP systems support, see [SapUnpack for Non-Unicode SAP Systems](#sapunpackfornonunicodesapsystems)

- 
When this parameter is defined for long text table (STXL), HVR makes the following changes to the target table:

- Fields **SRTF2** and **CLUSTR** are removed from the target.
- Field **CLUSTD** is converted from type **varbinary** to **CLOB**/**NVARCHAR(MAX)**.
- Field **CLUSTD** stores the text in Unicode format.


- 
SAP stores long text table (STXL) in binary format. Each binary text record can have its own encoding. This encoding can be different from the encoding of the SAP system. The SapUnpack functionality for long text supports converting the following SAP code pages to Unicode:

- **1100, iso-8859-1**
- **1401, iso-8859_2** <strong>Since</strong> 6.1.0/45
- **1500, iso-8859-5**
- **1610, iso-8859_9** <strong>Since</strong> 6.1.0/45
- **4102, utf-16be**
- **4103, utf-16le**


> **Important:** 
- 
In case the SapUnpack encounters unsupported code page, an error will be displayed. This error can be handled by defining the parameter [**SapUnpackCoerceErrorPolicy**](https://fivetran.com/docs/hvr6/action-reference/tableproperties#sapunpackcoerceerrorpolicy). in action [**TableProperties**](https://fivetran.com/docs/hvr6/action-reference/tableproperties).

- 
Currently, the SapUnpack functionality does not support converting Japanese stored in an ISO code page.






---

### ExecOnHub


**Description:** Execute transform on hub instead of location's machine.

---

### Parallel


**Argument:** *n*

**Description:** Run transform in *n* multiple parallel branches. Rows will be distributed using hash of their distribution keys, or round robin if distribution key is not available. Parallelization starts only after first 1000 rows.

---

### Context


**Argument:** *context*

**Description:** Action **Transform** is effective/applied only if the *context* matches the context defined in [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh). For more information about using Context, see our concept page [Refresh or Compare context](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).

The value should be a context name, specified as a lowercase identifier. It can also have form **!***context*, which means that the action is effective unless the matching *context* is enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

One or more contexts can be enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

Defining an action that is effective only when a specific context is enabled can have various uses. For example, if the parameters [**Command**](#command)=**"C:/hvr/script/myscriptfile"** and **Context**=**qqq** is defined, then during replication the **Transform** action will not be performed. However, if a [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) is performed with context **qqq** enabled (option –Cqqq), the **Transform** action will be performed.

Additionally, If a 'context variable' is supplied (using option –Vxxx=<em>val</em>) then this is passed to the **Transform** action as environment variable **$HVR_VAR_XXX**.

---

## Requirements for SapUnpack


HVR's SapUnpack feature enables [capturing](https://fivetran.com/docs/hvr6/action-reference/capture) changes from SAP pool, cluster, and long text table (STXL) and replicate into target database as "unpacked" data. For example, HVR can capture the SAP cluster table (**RFBLG**) from an Oracle based SAP system and unpack the contents (**BSEG**, **BSEC**) of the cluster table into a Redshift database; the HVR pipeline does the 'unpacking' dynamically.

The SapUnpack feature supports capturing changes from SAP system with either of the databases - Db2 for i, Db2 for LUW, Oracle, SAP NetWeaver on Oracle, and SQL Server.

> **Important:** 
HVR does not support capture from cluster and STXL tables with compressed LOBS.


### SAP System


The SAP database typically contains tables that fall into one of the following three categories:

- **Transparent tables**: ordinary database tables which can be replicated in a usual way.
- **Pooled and cluster tables**: are special in that the data for several pooled or cluster tables are grouped and physically stored together in a single database table.
- **SAP catalogs**: contain metadata and do not usually need to be replicated. HVR SapUnpack feature needs data from the SAP catalogs for processing the pooled and cluster tables.


> **Important:** 
To enable replication from SAP database using SapUnpack, ensure that the SAP Dictionary tables (**DD02L**, **DD02T**, **DD03L**, **DD06T**, **DD08L**, **DD09L**, **DD16S**, **DDNTF**, **DDNTT**, **TADIR**) exist in the source database. HVR uses the information available in SAP dictionary for unpacking data from SAP pool and cluster tables.

There are tables that SAP does not identify in its dictionary as cluster tables even though the tables contain clustered data. These are not supported. Examples include **PCL1**, **PCL2**, and **MDTC**.


### License for Unpacking SAP Tables


For [Usage-based Subscription](https://fivetran.com/docs/hvr6/getting-started/licensing), an additional SAP Unpack license is required to unpack the cluster and pool tables from the SAP database. Contact [Fivetran Technical Support](https://support.fivetran.com/hc/en-us) to obtain the necessary SAP Unpack license. For the [Consumption-based](https://fivetran.com/docs/hvr6/getting-started/licensing) model, a separate license is NOT required.

> **Note:** 
HVR supports multi-licensing for Usage-based Subscription; this means a hub system can have several licenses registered simultaneously. For example, one license enables all HVR features (except SapUnpack) to be used perpetually and another license enables the SapUnpack feature.


### SapUnpack for Non-Unicode SAP Systems


<strong>Since</strong> v6.1.0/14

The HVR SapUnpack feature supports unpacking (decoding) cluster and pool tables of non-Unicode SAP systems. This functionality is supported for the following databases: Db2 for i, Db2 for LUW, Oracle and SQL Server and will work with any encodings [supported by HVR](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings) for these databases.

Data in cluster and pool tables are encoded using the SAP application server's codepage. To replicate data correctly, you need to define the **HVR_DB_CHARSET** environmental variable on a source location and the **HVR_SAP_APPLICATION_CHARSET** environment variable on a target location. Both environment variables must be set to the appropriate encoding [supported by HVR](https://fivetran.com/docs/hvr6/advanced-operations/supported-character-encodings) for a particular database.

For example, for Oracle's **ISO-8859-1** encoding, the environmental variables must be defined as follows:

 Group | Table | Action | Parameter(s) |
 SOURCE | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=**HVR_DB_CHARSET**
**[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)=ISO-8859-1** |
 TARGET | * | **[Environment](https://fivetran.com/docs/hvr6/action-reference/environment)** | **[Name](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=**HVR_SAP_APPLICATION_CHARSET**
**[Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)=ISO-8859-1** |


> **Important:** 
For [compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), the **HVR_SAP_APPLICATION_CHARSET** environment variable must be also added to the job system environment variables:

- In UI, this can be done using the [**Job System Environment Variables**](https://fivetran.com/docs/hvr6/user-interface/jobs#jobsystemenvvar) on the [Jobs](https://fivetran.com/docs/hvr6/user-interface/jobs) page
- In CLI, this can be done using command [**hvrjobconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrjobconfig) with option **-E**.



.actparam {
    padding-left: 20px;
}
