# Hub Properties - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/property-reference/hub-properties

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/property-reference/hub-properties/index.md)

# Hub Properties


This section lists and describes the HVR Hub properties.

A hub property specifies the characteristics/attributes of HVR Hub. In the Command Line interface (CLI), the hub properties can be set using the command [**hvrhubconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubconfig).

> **Note:** 
A property that is automatically discovered by HVR when it connects to a database/location is called discovered property. A user cannot specify/input value into a discovered property.

An array property and map property can store multiple values. The syntax for updating them from the [Command Line Interface (CLI)](https://fivetran.com/docs/hvr6/command-line-interface/managing-properties-in-cli) varies.


---

## Access_List


<strong>Deprecated in</strong> v6.1.5/2

**Argument:** *accesslevel*

**Description:** Enables you to set read/write permissions for HVR users connecting to HVR Hub System. HVR allows different access levels for the authenticated users based on their username and the hub database name.

The following access levels are supported by HVR:

- **ReadOnly**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables).
- **ReadExec**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and start/stop jobs.
- **ReadExecRefresh**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), and start/stop jobs.
- **ReadWrite**: User can view job status and modify information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), [**Activate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate), and start/stop jobs.
- **HubOwner**: User can view job status and modify information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), [**Activate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate), start/stop jobs, freeze/unfreeze hub, change hub properties, and delete hub.


This is an array property that can store multiple values.

---

## All_User_Access


<strong>Since</strong> v6.1.5/2

**Argument:** *accesslevel*

**Description:** Enables you to set read/write permissions for all HVR users connecting to HVR Hub System.

The following access levels are supported by HVR:

- **read**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables).
- **exec_jobs**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and start/stop jobs.
- **exec_refresh**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), and start/stop jobs.
- **write_locs**: User can view job status and modify location information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables).
- **write_channels**: User can view job status and modify channel information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), [**Activate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate), and start/stop jobs.
- **hubowner**: User can view job status and modify information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), [**Activate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate), start/stop jobs, freeze/unfreeze hub, change hub properties, and delete hub.


Example JSON:
All_User_Access={"read":true}

This is a map property that can store multiple values.

---

## Created


**Argument:** *moment*

**Description:** Moment (date and time) at which the hub was created.

---

## Creator


**Argument:** *name*

**Description:** Name of the user who created the hub

---

## Description


**Argument:** *description*

**Description:** Description for hub.

---

## Encrypt_Transaction_Files


**Argument:** true

**Description:** If set to **true**, enables encryption of the [**Confidential**](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/classification-of-data) data using the Software or KMS wallet.

This requires the **Wallet Property** - [**Type**](https://fivetran.com/docs/hvr6/property-reference/wallet-properties#type) set to **SOFTWARE** or **KMS**.

---

## Freeze_Time


**Argument:** *moment*

**Description:** Moment (date and time) at which the hub was **FROZEN**.

---

## Hub_ID


**Description:** Unique identifier of the HVR Hub Server.

---

## Hub_Server_HVR_CONFIG


**Description:** This is a discovered property that stores the directory path of **HVR_CONFIG** for the HVR Hub Server.

---

## Hub_Server_HVR_HOME


**Description:** This is a discovered property that stores the directory path of **HVR_HOME** for the HVR Hub Server.

---

## Hub_Server_HVR_License_Hash


**Description:** This is a discovered property that stores the list of license identification hashes installed in the HVR Hub Server.

---

## Hub_Server_HVR_Version


**Description:** This is a discovered property that stores the version of the HVR installed in the HVR Hub Server.

---

## Hub_Server_Operating_System


**Description:** This is a discovered property that stores the name of the operating system on which the HVR Hub Server is installed/running.

---

## Hub_Server_OS_Fingerprint


**Description:** This is a discovered property that stores the unique identifier (fingerprint) of the server on which the HVR Hub Server is installed.

---

## Hub_Server_Platform


**Description:** This is a discovered property that stores the name of the HVR platform used for installing the HVR Hub Server.

---

## Hub_Server_URL


**Argument:** *url*

**Description:** Base URL for the HVR Hub Server. This is the URL via which users can access the HVR Hub Server.

This URL is supplied in (most) commands using option **-R**.

---

## Hub_State


**Argument:** *state*

**Description:** State of the HVR Hub Server.

Valid values for *state* are:

- **FROZEN**: Indicates [scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) is stopped and no jobs can be running in the hub.
- **LIVE**: Indicates [scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) is running (and replication may be running, activated or deactivated).
- **RESTARTING**: Indicates a [scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) failure and the hub server is restarting it.


---

## Statistics_Cycle_Delay


**Description:** Specifies the delay between gather cycles of **hvrstats** job from the HVR log files. The default cycle delay is **60** seconds.

If the value of this property is changed, the **hvrstats** job must be restarted for the change to become effective.

---

## Statistics_Metrics_Set


**Description:** Set of metrics gathered by the **hvrstats** job.

---

## Statistics_Retention_Policy


**Argument:** *policy*

**Description:** Specifies the size of history maintained by **hvrstats** job, before it purges its own rows.

Available options for *policy* are:

- **NONE**: History is not maintained by **hvrstats** job. Does not add history rows to [**HVR_STATS**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrstats).
- **SMALL**: History rows for per-table measurements at 1min/10min/1hour/1day granularity are purged after 1hour/4hours/1day/7days respectively. History rows for all tables (table=*) at 1min/10 min/1hour/1 day granularity are purged after 4hours/1day/7days/30days respectively.
- **MEDIUM** default: History rows for per-table measurements at 1min/10min/1hour/1day granularity are purged after 4hours/1day/7days/30days respectively. History rows for all tables (table=*) at 1min/10min/1hour/1day granularity are purged after 1day/7days/30days/never respectively.
- **LARGE**: History rows for per-table measurements at 1min/10min/1hour/1day granularity are purged after 1day/7days/30days/never respectively. History rows for all tables (table=*) at 1min/10min/1hour/1day granularity are purged after 7days/30days/never/never respectively.
- **UNBOUNDED**: Never purge history rows. Rows continue to grow in [**HVR_STATS**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrstats).


A smaller policy will reduce the amount of disk space needed for the hub database. For example, if a hub has 2 channels with same locations (1 capture and 2 targets) and each has 15 busy tables measured using 10 status measurements, then the following is the approximate number of rows in [**HVR_STATS**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrstats) after 1 year:

- **SMALL**: 207K rows
- **MEDIUM**: 1222K rows
- **LARGE**: 7M rows
- **UNBOUNDED**: 75M rows


In the HVR UI, this property corresponds to the **RETENTION POLICY** option in [**Statistics Tuning**](https://fivetran.com/docs/hvr6/user-interface/system/current-hub#statistictuning).

> **Note:** 
To purge the statistics data immediately (as a one-time purge) from the [**HVR_STATS**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrstats) table, use the command [**hvrstats** (with option **-p**)](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrstats).


---

## Statistics_Second_Location


**Argument:** *path*

**Description:** Secondary location (directory *path*) to store the statistics data in CSV format files. For more information about using this property, see [Secondary Storage for Statistics](https://fivetran.com/docs/hvr6/user-interface/statistics#secondarystorageforstatistics).

---

## Statistics_Time_Granularity_Base


**Description:** Specifies the lowest time granularity that the **hvrstats** job gathers metrics. The default granularity is **1 min**.

If the value of this property is changed, the **hvrstats** job must be restarted for the change to become effective.

---

## User_Access


<strong>Since</strong> v6.1.5/2

**Argument:** *accesslevel*

**Description:** Enables you to set different read/write permissions for HVR users connecting to HVR Hub System, per user.

The following access levels are supported:

- **read**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables).
- **exec_jobs**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) and start/stop jobs.
- **exec_refresh**: User can view job status and information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), and start/stop jobs.
- **write_locs**: User can view job status and modify location information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables).
- **write_channels**: User can view job status and modify channel information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), [**Activate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate), and start/stop jobs.
- **hubowner**: User can view job status and modify information in [Repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables). They can also execute [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare), [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), [**Activate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate), start/stop jobs, freeze/unfreeze hub, change hub properties, and delete hub.


Example JSON:
User_Access={"user1":{"hubowner": true},"user2":{"write_locs":true}}

This is a map property that can store multiple values.

.actparam {
    padding-left: 20px;
}
