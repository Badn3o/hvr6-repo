# Performance Metrics - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/performance-metrics

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/performance-metrics/index.md)

# Performance Metrics


<b>Since</b> v6.1.0/31 Linux

The **Performance Metrics** feature collects and reports system-level performance data such as CPU usage, disk activity, and network I/O from machines running the HVR Hub and HVR Agent. These metrics are averaged on a minute-by-minute basis.

They are supported for both [Capture](https://fivetran.com/docs/hvr6/action-reference/capture) and [Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate) jobs. Performance metrics can be viewed in the [Statistics](https://fivetran.com/docs/hvr6/user-interface/statistics) page.

> **Important:** 
The **Performance Metrics** feature is available only on Linux.


The following performance metrics are generated when this feature is enabled:
 Performance Metric | Description |
 **CPU Usage** | Average CPU usage of a hub or agent machine per minute, represented in percentage. |
 **IO Wait** | The time spent by CPU of a hub or agent machine waiting for IO, represented in percentage. |
 **Network Dropped Incoming/Outgoing Packages** | The number of dropped incoming/outgoing network packages of a hub or agent machine. |
 **Network Incoming/Outgoing Errors** | The number of incoming/outgoing network errors of a hub or agent machine. |
 **Config/Temp/HVR_HOME Disk Time Spent Reading/Writing** | The time the disk spent reading/writing to the **HVR_HOME**, **HVR_CONFIG**, and **TEMP** directories on a hub or agent machine, measured in milliseconds. |
 **Config/Temp/HVR_HOME Disk Time Spent doing IO** | The time the disk spent on IO operations for the **HVR_HOME**, **HVR_CONFIG**, and **TEMP** directories on a hub or agent machine, measured in milliseconds. |
 **Config/Temp/HVR_HOME Disk Weighted Time Spent doing IO** | The weighted time the disk spent on IO operations for the **HVR_HOME**, **HVR_CONFIG**, and **TEMP** directories on a hub or agent machine in milliseconds. |
 **Config/Temp/HVR_HOME Disk IO Operations In Progress** | The number of in-progress disk IO operations for the **HVR_HOME**, **HVR_CONFIG**, and **TEMP** directories on a hub or agent machine. |

## Enabling Performance Metrics


The **Performance Metrics** feature is disabled by default. You can enable it on the HVR Hub, the HVR Agent, or both - depending on the machine from which you want to collect system-level performance data.

To enable the feature, you must set the environment variable **HVR_PERFORMANCE_METRIC_ENABLE** to **1** on the machine running the respective HVR process (Hub or Agent).

- 
To enable on the HVR Hub:

- 
In HVR UI, use the [**Job System Environment Variable**](https://fivetran.com/docs/hvr6/user-interface/jobs#jobsystemenvvar) option to set the environment variable.

- 
In the CLI, use the [**hvrjobconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrjobconfig) command.
hvrjobconfig -E HVR_PERFORMANCE_METRIC_ENABLE=1 <em>hub</em> SYSTEM



- 
To enable on the HVR Agent (for the source/target location):

- 
In HVR UI, define the [**Environment**](https://fivetran.com/docs/hvr6/action-reference/environment) action on the source and/or target locations to set the environment variable.

- 
In the CLI, use the [**hvragentlistener**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener) command.
hvragentlistener -E HVR_PERFORMANCE_METRIC_ENABLE=1





Alternatively, you can set the environment variable using the Linux export command:
export HVR_PERFORMANCE_METRIC_ENABLE=1

## Disabling Performance Metrics


To disable the **Performance Metrics** feature, you must set the environment variable **HVR_PERFORMANCE_METRIC_ENABLE** to **0** on the HVR Hub and/or HVR Agent, depending on where it was previously enabled.

You can update the environment variable using the same method you used to enable it - via the HVR UI or CLI.

## Limitations


When HVR Hub or HVR Agent runs inside a "container" whose file system uses an overlay storage driver (such as Docker), disk I/O performance metrics are not collected. As a result, the following metrics are absent:

- **Config/Temp/HVR_HOME Disk Time Spent Reading/Writing**
- **Config/Temp/HVR_HOME Disk Time Spent doing I/O**
- **Config/Temp/HVR_HOME Disk Weighted Time Spent doing I/O**
- **Config/Temp/HVR_HOME Disk I/O Operations In Progress**


## Performance Metrics Log Examples


When Performance Metrics are enabled, the measures are represented in the logs for each category as follows. Logs from the hub are prefixed with  **<Hub>**, and logs from the agent are prefixed with  **<Agent>**.

- 
**CPU Usage**

In the following example, the average **CPU Usage** of machine running the hub 5%.
<Hub> Average CPU usage of machine 'demo' for the last minute is 5%.

- 
**I/O Wait**

In the following example, the time spent by the CPU of the agent machine waiting for IO is 4.40%.
<Agent> Time spent by the CPU waiting for a IO on machine 'demo' is 4.40%.

- 
**Network Incoming/Outgoing Errors**

In the following example, the machine running the agent reported a number of dropped incoming packets, dropped outgoing packets, incoming errors, and outgoing errors.
<Agent> Network interface em1 in machine 'demo' dropped 1 incoming packet and 5 outgoing packets. It also had 3 incoming errors and 6 outgoing errors.

- 
**Config/Temp/HVR_HOME Disk IO Operations In Progress**

In this example, the machine running the hub reported the time spent in the **HVR_CONFIG** directory.
<Hub> Disk config partition dm-2 (used by directory /home/user1/dev/hvr_observability/hvr_config) in machine 'demo' spent 118742472 ms reading, 2834220646 ms writing and 52780841 ms doing IO (weighted: 2953464018 ms). With 0 IO operations in progress.


