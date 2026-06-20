# Upgrading HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/install-and-upgrade/upgrade/index.md)

# Upgrading HVR 6


This section describes the requirements and steps for upgrading HVR Hub and HVR Agent.

> **Note:** 
In the case of a distributed setup, along with the HVR Hub installation, there may be one or more HVR Agent installations on the source and target machines. Since HVR versions 6.1.0 and higher are fully compatible with each other, upgrading all installations may not be required.

Each HVR release contains new features and/or fixes for certain bugs. Each feature or fix is only effective if the correct machine is upgraded. Typically, the release notes (available in **HVR_HOME/hvr.rel**) contain information about which features and fixes have been added, and which machines must be upgraded for each feature and fix to be effective. New features should not be used until all machines that are specified for that feature are upgraded, otherwise, errors may occur.

For example, if a new release fixes an integrate bug, then that release must be installed on the HVR Agent machine(s) which perform integrate. If only the HVR Hub is upgraded using that release, there will be no benefit.


## Topics


- [Upgrading HVR Hub](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/hub)
- [Upgrading HVR Hub on Linux](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/hub/upgrading-hub-on-linux)
- [Upgrading HVR Hub on Windows](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/hub/upgrading-hub-on-windows)


- [Upgrading HVR Agent](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/agent)
- [Upgrading HVR Agent on Linux](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/agent/upgrading-agent-on-linux)
- [Upgrading HVR Agent on Unix](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/agent/upgrading-agent-on-unix)
- [Upgrading HVR Agent on Windows](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/agent/upgrading-agent-on-windows)


- [Upgrading from HVR 5](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/upgrading-from-hvr-5)
- [Important Notes When Upgrading from HVR 5](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/upgrading-from-hvr-5/important-notes-when-upgrading-from-hvr-5)



