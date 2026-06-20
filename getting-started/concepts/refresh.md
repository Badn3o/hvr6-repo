# Refresh - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/concepts/refresh

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/concepts/refresh/index.md)

# Refresh


**Refresh** is a process in Fivetran HVR that initially loads data from source to target location. **Refresh** loads your data from source into the target tables you already have. If the tables are not there, **Refresh** creates them for you. **Refresh** is a function that you use in the context of a **Channel**. In this channel, the source for **Refresh** should be a database location, while the target can be either a database or a file location.

> **Important:** 
For [consumption-based](https://fivetran.com/docs/hvr6/getting-started/licensing#consumptionbased) licensing, Fivetran offers a five-day troubleshooting window per table for performing free **Refreshes** in HVR. This window starts on the day you first perform a **Refresh** on a table in a given month. Any subsequent **Refreshes** done outside this window count towards paid [MAR](https://fivetran.com/docs/hvr6/getting-started/pricing).


Refreshing from a source location is supported only on certain location types. For the list of supported source location types, see section [Refresh and Compare](https://fivetran.com/docs/hvr6/capabilities/610#refreshandcompare) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

> **Note:** 
HVR offers the following methods of executing **Refresh**:

- via **UI** – see [Refreshing Data](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)
- via **CLI** – see [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh)
- via **API** – see **/api/latest/hubs/{hub}/channels/{channel}/refresh** in [Activate, Refresh, and Compare Interface](https://fivetran.com/docs/hvr6/rest-api/rest-api-reference/610/6100/activate-refresh-and-compare).



You can use a HVR channel exclusively for doing a **Refresh** job. In this case, you must also define this channel with [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) and [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) actions, and running [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) is not required.

A **Refresh** job cannot be run simultaneously with the [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) job because it can lead to data inconsistency. Therefore, when a **Refresh** job is started, HVR forces the **Integrate** job into **SUSPEND** [state](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler#jobstates) and creates a control file to block the **Integrate** job from running. When the **Refresh** job is complete, HVR automatically removes the control file and unsuspends the **Integrate** job. Note that the **Integrate** job is restored to its previous [state](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler#jobstates) before the **Refresh** was executed.

The control files are created on the HVR Hub System in the directory **HVR_CONFIG/hubs/***hubname***/channels/***channelname***/control**.

In case the **Refresh** job fails and the block control files are not removed automatically, the **Integrate** job cannot be restarted (or unsuspended). When that happens, an error shows up. To resolve this error, remove the control files with names matching **.ctrl-***channelname***-integ-***targetlocation***-*_block** from the hub directory **HVR_CONFIG/hubs/***hubname***/channels/***channelname***/control** and then manually **Unsuspend** the **Integrate** job.

## Refresh Types


There are two types of **Refresh** you can choose from:

- 
**Bulk Refresh**

- 
**Row-by-row Refresh**



> **Note:** 
You can set a **Refresh** type via:

- the CLI [-g option](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh#g)
- choosing [Bulk](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#bulkloadtablegranularity) or [Row-by-Row Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#repairrowbyrowgranularity) in the UI



### Bulk Refresh


**Bulk Refresh** means that the target object is truncated, and then the bulk copy is used to refresh the data from the read location. On [certain locations](https://fivetran.com/docs/hvr6/capabilities/610#refreshandcompare), during **Bulk Refresh** table indexes and constraints will be temporarily dropped or disabled and will be reset after the refresh is complete.

During **Bulk Refresh**, HVR typically streams data directly over the network into a bulk loading interface (e.g. direct path load in Oracle) of the target database. For [DBMSs](https://fivetran.com/docs/hvr6/capabilities/610#bulkloadrequiresstaging) that do not support a bulk loading interface,HVR streams data into intermediate temporary staging files (in a staging directory) from where the data is loaded into the target database. For more information about staging files/directory, see section "Burst Integrate and Bulk Refresh" in the respective [Source and Target Requirements](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements).

### Row-by-Row Refresh


**Row-by-Row Refresh**, also referred to as **Row-wise Refresh**, compares data on read and write locations and produces a 'diff' result based on which only rows that differ are updated on the write location, each row is refreshed individually. This results in a list of a minimal number of inserts, updates or deletes needed to re-synchronize the tables.

For column-oriented databases (e.g., Redshift, Snowflake, Google BigQuery), **Row-wise Refresh** is best used on small amount of data, e.g., on tables with a small amount of changed data or on small tables. In other cases **Row-wise Refresh** on column-oriented databases takes a lot of time.

## Slicing


Sometimes, the amount of data that the **Refresh** job needs to process is too big. In this case, you can choose to divide the table into a few batches and process them in parallel. In HVR, this is achieved via the [**Slicing**](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing) functionality. By configuring **Slicing**, you can divide your database table into a few pieces that will be processed in parallel saving you a lot of time.

HVR suggests a few types of **Slicing**, each fitting best for a specific business case. To learn more about slicing types and when it's best to use them, see the [**Slicing**](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing) concept page.

## Isolation


In a non-isolated refresh, all relevant integrate jobs are suspended until the refresh is complete. In contrast, an isolated table refresh allows integrate jobs to continue for tables that are not part of the isolated refresh. The integrate jobs for the isolated tables will resume once the refresh is complete.
