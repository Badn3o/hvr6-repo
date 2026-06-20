# Manually Adapting a Channel for DDL Statements - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/manually-adapting-a-channel-for-ddl-statements

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/manually-adapting-a-channel-for-ddl-statements/index.md)

# Manually Adapting a Channel for DDL Statements


For the first target location, use the option

There are a few cases in Fivetran HVR when a channel needs to be adapted:

- when new tables are added to an existing channel;
- when the table definitions change for the tables that are already being replicated;
- when tables are removed from a channel.


For certain databases, HVR continuously watches for Data Definition Language (DDL) statements using action [**AdaptDDL**](https://fivetran.com/docs/hvr6/action-reference/adaptddl) and automatically performs the steps required to adapt a channel. For the list of supported databases, see [Log-based capture of DDL statements using action AdaptDDL](https://fivetran.com/docs/hvr6/capabilities/610#adaptddlcap) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

There are also cases when the action [**AdaptDDL**](https://fivetran.com/docs/hvr6/action-reference/adaptddl) is not defined, or when the database source does not support capture of DDL statements using action [**AdaptDDL**](https://fivetran.com/docs/hvr6/action-reference/adaptddl). In these scenarios, HVR only captures the DML statements – <b>insert</b>, <b>update</b> and <b>delete</b>, as well as <b>truncate</b> table (modify to truncated) and replicates these to an integrate database. Since in these cases HVR does not capture DDL statements, such as <b>create</b>, <b>drop</b>, and <b>alter</b> table, the steps to capture them need to be performed manually.

> **Important:** 
When DDL statements are used, the following must be considered:

- These statements are not replicated by HVR, so they must be applied manually on both capture and integrate databases.
- The HVR channel that replicates the database must be changed ('adapted') to contain the new list of tables and columns, and the enroll information contains the correct internal table id number.
- For Ingres log–based capture, after an <b>alter table</b> statement an extra modify statement is needed to convert all the rows which are stored with the old column format. The statement is <b>modify</b> <em>mytbl</em> <b>to reconstruct</b>, or (assuming the old structure was a unique **btree**) <b>modify to</b> <em>mytbl</em> <b>btree unique</b>.



There are two ways to manually adapt an HVR channel:

- 
[**Online Manual Adapt**](#onlinemanualadapt): This method is less disruptive: while performing it, you can still make changes to all tables.

- 
[**Offline Manual Adapt**](#offlinemanualadapt): This method is more disruptive: while performing it, you cannot make any changes to any of the replicated tables. This method best works with major applications, like SAP or Oracle eBusiness Suite, during a planned downtime.



> **Important:** 
The steps mentioned in the following sections do not apply for [trigger-based capture](https://fivetran.com/docs/hvr6/capabilities/610#captrigbased) and [bi-directional replication](http://Replication%20Topologies#bi-directional). For these cases, contact [HVR Technical Support](https://support.fivetran.com/hc/en-us/requests/new) for minimal-impact adapt steps.


The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


## Online Manual Adapt


Online Manual Adapt allows you to adapt an HVR channel without disrupting the replication. To do the Online Adapt, perform the following steps:

- 
Stop the current jobs:

- 
[**Suspend**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsuspend) the current capture jobs.
hvrsuspend hub chn-cap

- 
Wait until the integrate jobs have finished integrating all the changes. In this way, no transaction files will be left in the router directory.
hvrstart -w hub chn-integ

- 
[**Suspend**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsuspend) the current integrate jobs.
hvrsuspend hub chn-integ



- 
Run the SQL script with the DDL statements against both the source and target databases, so that database schemas become identical.

- 
Manually adapt the channel definition so it reflects the DDL changes. This can be done in the HVR user interface or on the command line.

Run the command [**hvradapt**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvradapt) with the following options:
hvradapt -oelj hub chn

- Add tables to the channel in the [**Table Selection**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel) dialog.
- Change the table definition by choosing [**Redefine Table**](https://fivetran.com/docs/hvr6/user-interface/tables/checking-definition-against-source-or-target) [▶](https://fivetran.com/docs/hvr6/user-interface/tables/checking-definition-against-source-or-target) From Actual Source on the **Table** or **Table Details** page.
- [**Delete**](https://fivetran.com/docs/hvr6/user-interface/tables/deleting-tables-from-channel) tables from the channel.


- 
Use [**Check Definition ▶ Against Actual Target**](https://fivetran.com/docs/hvr6/user-interface/tables/checking-definition-against-source-or-target) option on the **Tables** or **Table details** page.

- 
Activate replication with **Jobs**, **Table Enrollment**, and **Supplemental Logging** components.

Run the command [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate#replicationcomponents) with the following options:
hvractivate -ojel hub chn

- In the **Activate Replication** dialog, expand the [**Replication Components**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication#replicationcomponents) section and check **Jobs**, **Table Enrollment**, and DBMS logging (**Supplemental Logging**) for the new tables in the capture database.


- 
Execute [**HVR Refresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) to synchronize only the tables that are affected by DDL statements (except for tables that were only dropped) in the SQL script in step **2**. Tables which were only affected by DML statements in this script do not need to be refreshed. It is also not necessary to refresh tables which have only had columns added or removed.

- 
For the first target location, use the option [**Changes before refresh are skipped by both capture and integrate jobs**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#resilientintegration) ([-qrw](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh#q)) to instruct the capture job to skip changes that occurred before the refresh and the integrate job, and to apply any changes that occurred during the refresh using resilience.

Run the command [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) with the following options:
hvrrefresh -gb -qrw -r src -l tgt1 -t tbl1 hvrhub hvr_demo

For the first target location, use the option [**Changes before refresh are skipped by both capture and integrate jobs**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#resilientintegration)



- 
For any extra target location(s), use the option [**Only integrate job skips changes before refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#resilientintegration) ([–qwo](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh#q)) because the capture job should not skip any changes, but the integrate jobs should apply changes which occurred during the refresh using resilience.

Run the command [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) with the following options:
hvrrefresh -gb -qwo -r src -l tgt2 -t tbl1 hvr_demo

In the Refresh Data dialog, for any extra target location(s), use the **Online Refresh Consistency** option **Only integrate job skips changes before refresh**.


> **Note:** 
For an Ingres target database, performing [bulk **refresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) (option **-gb**) will sometimes disable journaling on affected tables. If [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) had displayed a warning about disabling journaling then it is necessary to execute the Ingres command **ckpdb +j** on each target database to re-enable journaling.




- 
If any fail tables exists in the integrate location(s) ([**OnErrorSaveFailed**](https://fivetran.com/docs/hvr6/action-reference/integrate#onerrorsavefailed)) for the tables which have had columns added or dropped, then these fail tables must be dropped. For this, Activate Replication with [**Change Tables**](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/components-for-activating-replication#changetables) option selected. In the CLI, this corresponds to the command **hvractivate** [**-oc**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate#replicationcomponents):
hvractivate -oc -l int1 -l int2 -t tbl1 -t tbl2 hub chn

- 
Start the capture and integrate [Jobs](https://fivetran.com/docs/hvr6/user-interface/jobs).

- 
If the channel is replicating to a standby machine and that machine has its own hub with an identical channel running in the opposite direction, then that channel must also be adapted by repeating steps **3**, **5** and **7** on the standby machine.



## Offline Manual Adapt


Perform the following steps to manually adapt a channel using Offline Manual Adapt method:

- 
Start downtime. Ensure that users cannot make changes to any of the replicated tables.

> **Important:** 
It is recommended to wait for the capture and integrate jobs to process all outstanding changes before performing [**hvrsuspend**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsuspend) in the next step. If waiting is not feasible (in case long time is required for the capture and integrate jobs to process all outstanding changes), then any out of sync issues can be resolved with the [**HVR Refresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) performed in step **8**.


- 
Suspend all jobs.

Run the command [**hvrsuspend**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsuspend):
hvrsuspend hub chn

Choose the option [Suspend Jobs](https://fivetran.com/docs/hvr6/user-interface/jobs#suspendjobs) on the **Jobs** page.

- 
Deactivate replication with all replication components included.

Run the command [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate#d) with the following option:
hvractivate -d hub chn

Choose the option [Deactivate Replication](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication) on the page of your choice. In the [Replication Components](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication#replicationcomponents) section, select all available replication components.



- 
Run the SQL script with the DDL or DML statements against both the source and target databases.

- 
Manually adapt the channel definition so it reflects the DDL changes. This can be done in the HVR UI or on the command line.

Run the command [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate#replicationcomponents) with the following options:
hvractivate -oelj hub chn

Add tables to the channel in the [**Table Selection**](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel) dialog.

Change the table definition by choosing [**Redefine Table ▶ From Actual Source**](https://fivetran.com/docs/hvr6/user-interface/tables/checking-definition-against-source-or-target) on the **Table** or **Table Details** page.

[**Delete**](https://fivetran.com/docs/hvr6/user-interface/tables/deleting-tables-from-channel) tables from the channel.

- 
Use [**Check Definition ▶ Against Actual Target**](https://fivetran.com/docs/hvr6/user-interface/tables/checking-definition-against-source-or-target) option on the **Tables** or **Table details** page to check that all the tables against target

- 
Activate replication with all replication components selected.

Run the command [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate):
hvractivate hub chn

Select all [Replication Components](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication#replicationcomponents) before activating replication.



- 
Execute [**HVR Refresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) to synchronize all tables that are affected by the SQL script in step **4** (except for the tables that were only dropped). This includes tables that were also affected by DML statements in this script.

Run the command [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh#r) with the following option:
hvrrefresh -r src -t tbl1 -t tbl2 hub chn

The **–t** options can also just be omitted. In this case, all replicated tables will be refreshed.

[Refresh data](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data). Make sure to check that the [source location](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#specifylocations) is picked correctly.

> **Note:** 
For an Ingres target database, performing [**bulk refresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) (option **-gb**) will sometimes disable journaling on affected tables. If [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) had displayed a warning about disabling journaling, then it is necessary to execute the Ingres command **ckpdb +j** on each target database to re-enable journaling.


- 
[**Unsuspend**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsuspend) the capture and integrate jobs:

Run the command [**hvrsuspend**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsuspend#u) with the following option:
hvrsuspend -u hub chn

Choose the option [Unsuspend Job](https://fivetran.com/docs/hvr6/user-interface/jobs#suspendunsuspend) for each job you want to unsuspend.

- 
Finish downtime.

- 
If the channel is replicating to a standby machine and that machine has its own hub with an identical channel running in the opposite direction, then that channel must also be adapted by repeating steps **3**, **5**, **6**, **8** and **9** on the standby machine.



### Trigger-Based Capture


> **Important:** 
The trigger-based capture method ([**Capture_Method**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturemethod)=**DB_TRIGGER**) has been deprecated since 6.2.0/0.


Action [**AdaptDDL**](https://fivetran.com/docs/hvr6/action-reference/adaptddl) cannot be applied with trigger-based capture. In this case, the channel needs to be manually configured to perform trigger-based capture involving DDL statements. Steps defined for the [**Offline Manual Adapt**](#offlinemanualadapt) method above are also applicable to the trigger-based capture with DDL statements involved. Note that while performing the steps for the trigger-based capture, in steps **3** and **7**, all **Replication Components** should be selected.
