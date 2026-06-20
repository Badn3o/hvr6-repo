# Getting Started - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/index.md)

# Getting Started


Fivetran HVR is a software product for enterprise-level replication of database and file management systems. With its reliable and secure technology, HVR can achieve a combination of light footprint, low latency, and high throughput that cannot be found anywhere else. HVR supports a distributed architecture for database and file replication in between a [large number](https://fivetran.com/docs/hvr6/supported-platforms) of Database Management Systems (DBMSs). It is a comprehensive software system with various modules for running data replication. This includes:

- [**Refresh**](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) mechanism for initial loading of data from source to target;
- [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) process that continuously acquires all the changes in the source location;
- [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) process that applies the changes to the target location;
- [**Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) feature that compares the source and target locations to ensure that the data is in sync.


## Learn


HVR is a large system with numerous capacities. Ensure to learn basic terms and concepts used throughout the HVR service and documentation.

- 
[Architecture](https://fivetran.com/docs/hvr6/getting-started/concepts/architecture)

- 
[HVR Agent](https://fivetran.com/docs/hvr6/getting-started/concepts/agent)

- 
[Refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh)

- 
[Replication Topologies](https://fivetran.com/docs/hvr6/getting-started/concepts/replication-topologies)

- 
[Activate Replication](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/components-for-activating-replication)

- 
[Compare](https://fivetran.com/docs/hvr6/getting-started/concepts/compare)



To learn about other HVR concepts, see the [Concepts](https://fivetran.com/docs/hvr6/getting-started/concepts) section.

Additionally, check our [Quick Start Guide](https://fivetran.com/docs/hvr6/getting-started/quick-start-guide), a comprehensive resource designed to assist users in gaining a preview and practical understanding of HVR. This guide offers a hands-on experience, directing users through the configuration and execution of the HVR replication channel within a preconfigured environment.

## Install and Configure


Learn how to set up and configure your HVR installation.

- [Installing HVR Hub](https://fivetran.com/docs/hvr6/install-and-upgrade/install/hub)
- [Initial Setup of HVR Hub](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub)
- [Installing HVR Agent](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent)
- [Configuring HVR Agent](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent)


## Operate


Learn where to start and how to manage replication using HVR.

- Create [Channels](https://fivetran.com/docs/hvr6/user-interface/channels/creating-channel) and [Locations](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location)
- [Activate and Run Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication)
- [Perform Initial Load using Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)
- [Verify Replication using Compare](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data)

