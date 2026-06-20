# Environment - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/environment

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/environment/index.md)

# Environment


Action **Environment** sets an operating system [environment variable](https://fivetran.com/docs/hvr6/getting-started/concepts/environment-variables) for the Fivetran HVR process which connects to the affected location. It also affects an agent called for this location.

If this action is defined on a specific table, then it affects the entire job including data from other tables for that location.

---

## Parameters


This section describes the parameters available for action **Environment**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from HVR documentation, emails, or demo notes.




### Name


**Argument:** *name*

**Description:** Name of the environment variable.

---

### Value


**Argument:** *value*

**Description:** Value of the environment variable.

---

### Context


**Argument:** *context*

**Description:** Action **Environment** is effective/applied only if the *context* matches the context defined in [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh). For more information about using Context, see our concept page [Refresh or Compare context](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).

The value should be a context name, specified as a lowercase identifier. It can also have form **!***context*, which means that the action is effective unless the matching *context* is enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

One or more contexts can be enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

---

## Examples


Following are a few HVR environment variables:

- 
**HVR_SORT_BYTE_LIMIT**
Allows you to set the amount of memory to use before sorting large data volumes in temporary files.
The default limit is **512Mb**.

- 
**HVR_SORT_ROW_LIMIT**
Allows you to set the number of rows to keep in memory before sorting large amounts of data using temporary files.
The default limit is **10M**.

- 
**HVR_LOG_RELEASE_DIR**
PostgreSQL
Allows you to specify an alternative directory for reading DBMS backup log files. The value points to a location where HVR can find backups of the transaction files, as an alternative to the location indicated in the database dictionary. This variable is particularly useful for locating archive files in PostgreSQL.
For other DBMSs, such as Oracle, SQL Server, SAP HANA, SAP NetWeaver on HANA, and Sybase ASE, use the location property [**Archive_Log_Path**](https://fivetran.com/docs/hvr6/property-reference/location-properties#archivelogpath) instead.



.actparam {
    padding-left: 20px;
}
