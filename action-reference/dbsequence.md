# DbSequence - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/action-reference/dbsequence

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/action-reference/dbsequence/index.md)

# DbSequence


Action **DbSequence** allows database sequences to be replicated.

If a single **DbSequence** action is defined without any parameters for the entire channel (i.e., location group '*') then operations on all database sequences in the capture location(s) that are owned by the current schema will be replicated to all integrate locations. This means that if a **nextval** is done on the capture database, then after replication a **nextval** on the target database is guaranteed to return a higher number. However, note that if database sequence 'caching' is enabled in the DBMS, the **nextval** on the target database may display a 'jump' in values.

The SQL statement CREATE SEQUENCE is also replicated, whereas DROP SEQUENCE is not replicated.

[**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) and [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) also affect any database sequences matched by action **DbSequence**. Database sequences which are only in the 'write' database are ignored.

> **Important:** 
- 
This action cannot be used with parameter [**Burst**](https://fivetran.com/docs/hvr6/action-reference/integrate#burst) in action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate).

- 
This action is only supported for certain DBMSs, for more information see **Replicate database sequences (using action DbSequence)** in the **Capabilities** page ([6.2.5](https://fivetran.com/docs/hvr6/capabilities/625#dbsequence), [6.2.0](https://fivetran.com/docs/hvr6/capabilities/620#dbsequence), [6.1.5](https://fivetran.com/docs/hvr6/capabilities/615#dbsequence), [6.1.0](https://fivetran.com/docs/hvr6/capabilities/610#dbsequence))

- 
Capture of database sequence requires log–based capture ([**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture)).

- 
For an Oracle RAC cluster, sequences should be defined with parameter **ORDER** (default is **NOORDER**), unless the next values are only generated on one node. For more information on this parameter, refer to [Oracle's documentation](https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/CREATE-SEQUENCE.html).




---

## Parameters


This section describes the parameters available for action **DbSequence**.

Following are the two tabs/ways, which you can use for defining action parameters in this dialog:

- **Regular**: Allows you to define the required parameters by using the UI elements like checkbox and text field.
- **Text**: Allows you to define the required parameters by specifying them in the text field. You can also copy-paste the action definitions from Fivetran HVR documentation, emails, or demo notes.




### CaptureOnly


**Description:** Only capture database sequences, do not integrate them.

---

### IntegrateOnly


**Description:** Only integrate database sequences, do not capture them.

---

### Name


**Argument:** *seq*

**Description:** Name of database sequence. Only capture or integrate database sequence named *seq*. By default, this action affects all sequences.

---

### Schema


**Argument:** *dbschema*

**Description:** Schema that owns database sequence. By default, this action only affects sequences owned by the current user name.

---

### BaseName


**Argument:** *seq*

**Description:** Name of sequence in database, if this differs from the name used in HVR. This allows a single channel to capture multiple database sequences that have the same sequence name but different owners.

---

## Notes for DbSequence


To replicate a specific sequence, use the parameter [**Name**](#name). To replicate all sequences in a schema, use the parameter [**Schema**](#schema) without [**Name**](#name). To replicate all sequences owned by the current user, do not use either [**Name**](#name) or [**Schema**](#schema).

Capturing all sequences from multiple schemas cannot be achieved by defining multiple **DbSequence** actions with parameter [**Schema**](#schema) but without [**Name**](#name). Instead, you can either define multiple **DbSequence** actions, each with both parameters [**Schema**](#schema) and [**Name**](#name), or use multiple capture locations or channels, with each having its own **DbSequence** action defined with parameter [**Schema**](#schema).

---

## Bidirectional Replication


Bidirectional replication of sequences causes problems because the sequence change will 'boomerang back'. This means that after the integrate job has changed the sequence, the HVR capture job will detect this change and send it back to the capture location. These boomerangs make it impossible to run capture and integrate jobs simultaneously. But it is possible to do bidirectional replication for a failover system; i.e. when replication is normally only running from A to B, but after a failover the replication will switch to run from B to A. Immediately after the switchover a single boomerang will be sent from B to A, but afterwards the system will consistent and stable again.

If bidirectional replication is defined, then HVR Refresh of database sequences will also cause a single 'boomerang' to be captured by the target database's capture job.

Session names cannot be used to control bidirectional replication of database sequences in the way that they work for changes to tables. For more information, see [Managing Recapturing Using Session Names](https://fivetran.com/docs/hvr6/advanced-operations/managing-recapturing-using-session-names).

---

## Replication of Sequence Attributes


Database sequence 'attributes' (such as minimum, maximum, increment, randomness, and cycling) are not replicated by HVR. When HVR has to create a sequence, it uses default attributes and only the value is set accurately. This means that if a database sequence has non–default attributes, then sequence must be manually created (outside of HVR) on the target database with the same attributes as on the capture database. But once these attributes are set correctly, then HVR will preserve these attributes while replicating the **nextval** operations.

.actparam {
    padding-left: 20px;
}
