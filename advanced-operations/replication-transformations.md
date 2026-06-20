# Replication Transformations Between Non-Identical Tables - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/replication-transformations-between-non-identical-tables

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/replication-transformations-between-non-identical-tables/index.md)

# Replication Transformations Between Non-Identical Tables


Fivetran HVR can replicate data between tables with identical structure. It can also perform transformations when replicating data between non-identical tables.

Replication between different DBMS (e.g., between Oracle and SQL Server) does not necessarily count as a "transformation" since HVR will automatically convert between the data types as necessary.

Transformation logic can be performed during capture, inside the HVR pipeline, or during integration. These transformations can be defined in HVR using different techniques:

- Declarative actions, which add special HVR actions to the channel. These actions can be defined on the capture side or on the integrate side. For example:
- Capture side action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) with parameter **CaptureExpression="lowercase({** *colname* **})"** can be used to perform an SQL expression whenever reading from column *colname*. This SQL expression can also do a sub select (if the DBMS supports that syntax).
- Capture side action [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) with parameter **CaptureCondition="{** *colname* **}>22"** restricts HVR to only capture certain changes.
- Integrate side action [**ColumnProperties**](https://fivetran.com/docs/hvr6/action-reference/columnproperties) **IntegrateExpression="lowercase({** *colname* **})"** can be used to perform an SQL expression whenever writing into column *colname*. This SQL expression could also do a sub select.
- Integrate side action [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) with parameter **IntegrateCondition="{** *colname* **}>22"** restricts HVR to only apply certain changes.


- Injection of blocks of business logic inside HVR's normal processing. For example, action [**DbObjectGeneration**](https://fivetran.com/docs/hvr6/action-reference/dbobjectgeneration) shows how a block of user-supplied SQL can be injected inside the procedure used to update a certain table.
- Replacement of HVR's normal logic with user-supplied logic. For more details, see [**DbObjectGeneration**](https://fivetran.com/docs/hvr6/action-reference/dbobjectgeneration).
- Using an SQL view on the capture database. This means the transformation can be encapsulated in an SQL view, which HVR then replicates from. See example section [**DbObjectGeneration**](https://fivetran.com/docs/hvr6/action-reference/dbobjectgeneration) .
- In an agent plugin. An agent plugin is a user supplied program which is defined in the channel and is then scheduled by HVR inside its capture or integration jobs. See section [**AgentPlugin**](https://fivetran.com/docs/hvr6/action-reference/agentplugin) .


> **Note:** 
HVR can apply transformations:

- during replication (capture and integration);
- or during a compare or refresh between the source and target databases.


