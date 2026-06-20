# CollisionDetect - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/collisiondetect

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/collisiondetect/index.md)

# CollisionDetect


Action **CollisionDetect** causes Fivetran HVR integration to detect 'collisions', i.e., when a target row has been changed after the change that is being applied was captured. Collisions can happen during bi-directional replication; if the same row is changed to different values in databases **A** and **B** so quickly that there is no time to replicate the changes to the other database, then there is a danger that the change to **A** will be applied to **B** while the change to **B** is on its way to **A**. Collisions can also happen without bi-directional replication; if changes are made first to **A** and then to **B**, then the change to **B** could reach database **C** before the change from **A** reaches **C**. Undetected collisions can lead to inconsistencies; the replicated database will become more different as time passes.

The default behavior for **CollisionDetect** is automatic resolution using a simple rule; the most recent change is kept, and the older changes are discarded. The timestamps used have a granularity of one microsecond; if the changes occur in the same microsecond, then one arbitrary location (the one whose name sorts first) will 'win'. Parameters are available to change this automatic resolution rule and to tune performance.

Collision detection requires that HVR maintains extra timestamp information for each tuple unless parameter [**TimestampColumn**](#timestampcolumn) is defined. This information is held in a special history table (named *tbl***__h**). This table is created and maintained by both capture and integration for each replicated table. The old rows in this history table are periodically purged using timestamp information from the [integrate receive timestamp table](https://fivetran.com/docs/hvr6/internal-objects/objects-inside-database-locations#integratereceivetimestamptable).

For **CollisionDetect** to function properly, we recommend setting the HVR [isolation](https://en.wikipedia.org/wiki/Isolation_(database_systems)) level to 'SERIALIZABLE'. This is required only if you have a scenario where HVR is integrating changes into a table and, simultaneously, other users are also making changes to the same table. Setting the isolation level to 'SERIALIZABLE' can be achieved by defining the [environment variable](https://fivetran.com/docs/hvr6/getting-started/concepts/environment-variables) **HVR_SQL_INIT**. Following are a few examples for setting the **HVR_SQL_INIT** environment variable:

- 
For Oracle, define action [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) with parameters [**Name**](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=HVR_SQL_INIT [Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)="ALTER SESSION SET ISOLATION_LEVEL=SERIALIZABLE"**. For more information, refer to [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/data-concurrency-and-consistency.html#GUID-2A0FDFF0-5F72-4476-BFD2-060A20EA1685).

- 
For PostgreSQL, define action [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) with parameters [**Name**](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=HVR_SQL_INIT [Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)="SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL SERIALIZABLE"**. For more information, refer to [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-set-transaction.html).

- 
For SQL Server, define action [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) with parameters [**Name**](https://fivetran.com/docs/hvr6/action-reference/environment#name)**=HVR_SQL_INIT [Value](https://fivetran.com/docs/hvr6/action-reference/environment#value)="SET TRANSACTION ISOLATION LEVEL SERIALIZABLE"**. For more information, refer to [SQL Server documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql?view=sql-server-ver16).



> **Important:** 
- 
Action **CollisionDetect** is supported only for certain location classes depending on the parameter defined with the action. For the list of supported location classes, see **Bi-directional Replication** section in the **Capabilities** page ([6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#bidirectionalreplication), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#bidirectionalreplication), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#bidirectionalreplication), [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#bidirectionalreplication)).

- 
Action **CollisionDetect** cannot be combined with the [**Burst Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate#method) method.

- 
Defining the **CollisionDetect** action on a table with no keys that allow duplicates will prevent duplicate inserts. Instead, it will convert them into updates.




---

## Parameters


This section describes the parameters available for action **CollisionDetect**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from HVR documentation, emails, or demo notes.




### TreatCollisionAsError


**Description:** Treat a collision as an error instead of performing automatic resolution using the 'first wins' rule.

If parameter [**OnErrorSaveFailed**](https://fivetran.com/docs/hvr6/action-reference/integrate#onerrorsavefailed) in action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) is defined then the collision will be written to the fail table and the integration of other changes will continue. If parameter [**OnErrorSaveFailed**](https://fivetran.com/docs/hvr6/action-reference/integrate#onerrorsavefailed) is not defined then the integrate job will keep failing until the collision is cleared, either by deleting the row from the history table (using command [**hvrhistorypurge**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhistorypurge)) or by deleting the transaction file in the **HVR_CONFIG/router** directory.

---

### TimestampColumn


**Argument:** *colname*

**Description:** Exploit a timestamp column *colname* in the replicated table for collision detection.

Using this column is crucial for handling collisions, where both databases update a row almost simultaneously during replication. In such cases, HVR decides which change is the most recent.

The timestamp values in this column are not meant for comparing changes over extended periods, like days or years. Instead, its design evaluates recent changes occurring within microseconds or minutes that led to a collision.

One disadvantage of this parameter is that collision handling relies on this column being filled accurately by the application. Another disadvantage is that if changes can occur in more than one database simultaneously, and the changes occur in the same microsecond in both, proper collision detection may not be possible.

> **Important:** 
This parameter does not support DELETE.


---

### AutoHistoryPurge


**Description:** Delete rows from history table once the receive stamp table indicates that they are no longer necessary for collision detection.

These rows can also be deleted manually using command [**hvrhistorypurge**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhistorypurge).

---

### DetectDuringRefresh


**Argument:** *colname*

**Description:** During row-wise refresh, discard updates if the timestamp value in *colname* is newer in the target than the source.

This parameter can be used with [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) (option **-mui**) to reconcile the difference between two databases without removing newer rows from either.

This parameter must be used with parameter [**Context**](#context) (e.g. **Context**=refresh).

---

### Context


**Argument:** *context*

**Description:** Action **CollisionDetect** is effective/applied only if the *context* matches the context defined in [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh). For more information about using Context, see our concept page [Refresh or Compare context](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh-and-compare-contexts).

The value should be a context name, specified as a lowercase identifier. It can also have form **!***context*, which means that the action is effective unless the matching *context* is enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) or [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

One or more contexts can be enabled for [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh).

.actparam {
    padding-left: 20px;
}
