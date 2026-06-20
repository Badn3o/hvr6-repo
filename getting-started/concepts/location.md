# Location - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/concepts/location

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/concepts/location/index.md)

# Location


In Fivetran HVR, a **Location** is an endpoint in a replication process. It can be a file, database, data warehouse, or any other system [supported](https://fivetran.com/docs/hvr6/supported-platforms) by HVR. **Locations** can be local (i.e. residing on the same machine as the HVR Hub System) or remote (residing on a remote machine, other than the HVR **Hub** system).

Every **Location** that participates in the replication process is a member of a source or target **Location Group**. It is a logical group that includes all the source or all the target endpoints, between which the data is replicated. Unless a **Location** is added to a source or target **Location Group** (i.e., defined as a source or a target), it cannot participate in the replication process.`

**Location Groups** and all the [**actions**](https://fivetran.com/docs/hvr6/action-reference) that HVR can perform (comparison, scheduling, error handling, performance tuning, etc.) together make a [**Channel**](https://fivetran.com/docs/hvr6/getting-started/concepts/channel) – a logical unit which connects the source and target **Locations**.

Any **Location Group** can contain multiple **Locations**. Within a specific [**Channel**](https://fivetran.com/docs/hvr6/getting-started/concepts/channel), a **Location** can only be added to one **Location Group** (i.e., in a single **Channel**, it can only be either a source or a target).

## Location's Place within the Channel Structure


The following image shows a **Channel** scheme. It includes:

- Source **Location Group**. It can contain files, directories, data warehouses, or any of the locations for which HVR supports [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture). To see the list of all **Locations** that HVR supports as source, navigate to your preferred version of HVR in [Supported Platforms](https://fivetran.com/docs/hvr6/supported-platforms).
- **Actions**, which take place in the HVR Hub.
- Target **Location Group**. It can contain files, directories, data warehouses, or any of the locations for which HVR supports [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate). To see the list of all **Locations** that HVR supports as target, navigate to your preferred version of HVR in [Supported Platforms](https://fivetran.com/docs/hvr6/supported-platforms) (HVR supports all locations as target besides [SAP NetWeaver](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements)).



