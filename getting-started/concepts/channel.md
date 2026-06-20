# Channel - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/concepts/channel

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/concepts/channel/index.md)

# Channel


In Fivetran HVR, a **Channel** is a logical unit that connects source and target [**Locations**](https://fivetran.com/docs/hvr6/getting-started/concepts/location) in a series of [**actions**](https://fivetran.com/docs/hvr6/action-reference). Data replication and comparison, scheduling, error handling, performance tuning, and other actions happen within **Channels**.

HVR moves the data within a **Channel** from source to target [**Location Groups**](https://fivetran.com/docs/hvr6/getting-started/concepts/location). Every source **Location Group** within a channel must contain at least one source **Location**, and every target **Location Group** must contain at least one target **Location**.

In most cases, a **Channel** has two **Location Groups**: one source group and one target group. In [cascading replication scenario](https://fivetran.com/docs/hvr6/getting-started/concepts/replication-topologies#cascading), a **Channel** will include multiple **Location Groups**, with the first target group acting as a source for multiple **Locations**.

## Channel Structure


The following image shows a **Channel** scheme. It includes:

- Source **Location Group**. It can contain files, directories, data warehouses, or any of the locations for which HVR supports [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture). To see the list of all **Locations** that HVR supports as source, navigate to your preferred version of HVR in [Supported Platforms](https://fivetran.com/docs/hvr6/supported-platforms).
- **Actions**, which take place in the HVR **Hub**.
- Target **Location Group**. It can contain files, directories, data warehouses, or any of the locations for which HVR supports [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate). To see the list of all **Locations** that HVR supports as target, navigate to your preferred version of HVR in [Supported Platforms](https://fivetran.com/docs/hvr6/supported-platforms) (HVR supports all locations as target besides [SAP NetWeaver](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-netweaver-requirements)).




## Replication Scenarios


HVR channels support multiple replication scenarios:

- between one source location and one target location;
- from one source to multiple target locations;
- from multiple source locations to one target location;
- between multiple source and target locations.


All these options are described in detail on the [Replication Topologies](https://fivetran.com/docs/hvr6/getting-started/concepts/replication-topologies) page.

## Replication Styles


Replication styles dictate how HVR handles data changes when replicating data from the source to the target location.

HVR offers the following replication styles:

- **Standard replica**: Processes each insert, update, and delete by mirroring these operations on the target, ensuring synchronization between the source and the target.
- **Soft Delete**: Marks rows on the target as deleted when they are physically deleted on the source. This style is particularly useful in scenarios where downstream processing relies on information about deleted rows.
- **TimeKey**: Captures every change to a row on the source as a new record on the target, with metadata like the type and order of change. This style creates an audit trail of changes, making it well-suited for data lakes and streaming data use cases (e.g. Kafka).

