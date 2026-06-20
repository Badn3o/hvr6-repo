# Jobs - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/user-interface/jobs

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/user-interface/jobs/index.md)

# Jobs


This section describes and illustrates how to monitor and manage [jobs](https://fivetran.com/docs/hvr6/getting-started/concepts/jobs). A job is a process that performs a certain task, such as capturing changes, refreshing data, integrating changes, comparing data. At any moment a job has a certain state. Jobs are managed by the [Scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler). Jobs running through the [Scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) have their output appended to the hub log, and in case of a job failure, the hub will automatically retry the job.



The **Jobs** page displays a list of all jobs managed by a hub, as well as various options to manage jobs. It also displays the following information about each job:

 Field | Description |
 **TYPE** | A job type (**Activate**, **Capture**, **Refresh**, **Integrate**, **Compare**, **Statistics gather**) |
 **CHANNEL** | The name of a channel, to which a job belongs. |
 **LOCATIONS** | The name of a location, to which a job belongs. |
 **STATE** | A job state:

- **ALERTING** - if a job fails to run successfully, the [Scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) will change its state first to **ALERTING**, then **RETRY** and will eventually run again.
- **DISABLED** - if the job is disabled, it cannot be resumed, as opposed to **SUSPENDED**.
- **DONE** - for **Activate**, **Refresh** and **Compare** jobs, this state indicates that the most recent event of the corresponding type has been completed.
- **ERROR** - error(s) occurred during job execution.
- 
**FAILED** - the job execution is canceled.

- **HANGING** - If a job stays in state **RUNNING** for too long, it may be marked with state **HANGING**; if it finishes successfully, it will become **PENDING**.
- **PENDING** - the job is yet to be executed.
- **READY** - the job execution is completed.
- **RETRYING** - that the job failed and is restarted at least once during the job processing.****

- **RUNNING** - the job execution is in progress.
- **SUSPENDED** - the job execution is paused and can be unsuspended, which means that it will go into **PENDING** or **RUNNING** state.
- **WAITING** - the job will run at a scheduled time.

 |
 **RECENT ERRORS** | 
The time when the most [recent error](https://fivetran.com/docs/hvr6/property-reference/user-properties#recenterrorsseen) occurred. If there are any job errors or warnings, the following notification is displayed at the top of the page. Click the **View Scheduler Log** button to open the [**Log Viewer**](https://fivetran.com/docs/hvr6/user-interface/viewing-log) dialog displaying information about all the job errors on the hub. Click the **Clear All** button to hide all the current errors and warnings from the page. After clearing the errors and warnings, only new ones will be displayed in the **RECENT ERRORS** column from now on.



You can hide a specific error by clicking the cross icon next to it.
 |
 **LATENCY** | The time taken for a transaction committed on a source system to be replicated (captured and integrated) to a target system. This value allows you to analyze the delay in data replication. The graph is a link to the **Statistics** page of the corresponding channel. |
 **VOLUME** | An average number of integrated changes per the time range selected in the **Graph Range** filter. |
 **CHANGES QUEUED** | The number of captured changes queued on a hub to be integrated into a target location. |
 **CAPTURE REWIND** | Capture rewind shows you which period the job covered/captured since the last activation. It is only available for capture jobs. For example, if capture rewind is 6 days, that means that this capture job captured all changes that happened in the last 6 days. For a frozen hub, this time interval ends when the hub was frozen. |


## Filtering Jobs


By default, the page displays data about all jobs in the current hub. The top panel with multiple filtering options will help you to narrow down the data to view only the information you need.

- 
**Channels** selector allows you to display only jobs related to a selected channel.

- 
**Locations** selector allows you to display only jobs related to a selected location

- 
**Type** selector allows you to display only jobs of a selected type(s).

- 
**Graph Range** selector allows you to select the time range for the graphs displayed in the **Latency** and **Changes Processed** columns. The graphs will automatically update to show only that chosen period of time. Note that the **Graph Range** selector is not displayed when the two columns (**LATENCY** and **CHANGES PROCESSED**) are set to be hidden in the **Columns** menu.

- 
**Search** field provides a full-text search across all records in the **Jobs** table to quickly find all occurrences of a word/number you type.



The panel also shows the total number of jobs currently displayed on the page including inactive jobs (jobs that have no events to process and no pending errors).



## Managing Jobs


The following options to manage jobs are available at the top-right menu, as well as under the **More options** menu .

> **Note:** 
To select multiple jobs in one go, select the first job, hold the **Shift** key and then select the last job - all jobs in between the first and the last will be selected.




 Option | Description |
 **View Hub Log** | View the runtime information and errors related to the entire hub in the **[Log Viewer](https://fivetran.com/docs/hvr6/user-interface/viewing-log)** dialog. |
 
**Suspend Jobs**
**** | 
Suspend a job or multiple jobs at once.

`**Since** v6.1.0/3` When you suspend capture and/or integrate jobs in the **RUNNING** state, HVR enables a so-called 'graceful suspension' - a process that waits until the replication job cycle is completed before moving the job into the **SUSPEND** state. This ensures that no pending transactions are left as the job stops at the end of a cycle. During graceful suspension, the following dialog appears. Once the safe suspension is done, the dialog is closed automatically. There is also an option to do force suspend which will suspend the job immediately by killing the job process. However, note that the force suspension may leave the job in the **PENDING** state. For more information about job states, see section [Scheduler - Job States](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler#jobstates).


 |
 
**Start Jobs**
**** | Start a job or multiple jobs at once. The job's current status will change to **RUNNING**. |
 
**Delete Jobs**
**** | Delete a job or multiple jobs at once. |
 
**Show Stats Job**
**** | Displays the statistics gathering job (**hvrstats**) in the **Jobs** list. By default, this job is hidden and appears only when this option is enabled or when errors occur. It runs continuously in the background. For more information about this job, see [Stats Job](https://fivetran.com/docs/hvr6/user-interface/statistics#statsjob). |
 
**Hide Stats Job (unless errors)**
**** | Hide the **Stats Gathering** job from the list of jobs unless there are errors on the hub. This option is displayed when the **Show Stats Job** option is enabled. |
 
**Freeze Hub**
**** | This will stop the [Scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) and stop all the jobs running on the hub. For more information, see [Hub States](https://fivetran.com/docs/hvr6/user-interface/switch-hub#hubstates). |
 
**Job System Attributes**
**** | 
Set a [job attribute](https://fivetran.com/docs/hvr6/internal-objects/job-attributes) for **SYSTEM** job group. This opens the **Job System Attributes** dialog, where you can set default attributes for all jobs in the hub.
 |
 
**Job System Environment Variables**
**** | 
Set an [environment variable](https://fivetran.com/docs/hvr6/getting-started/concepts/environment-variables) for **SYSTEM** job group. This opens the **Job System Environment Variables** dialog, where you can set default environment variables for all jobs in the hub.
 |
 
**Show Start Page**
**** | Open the **Start Page**. This is a landing page that opens when you first access HVR web user interface. This page offers a starting point for new users that helps them build up a channel in the HVR Hub. |


Every job has its own **View Log** button that opens the [**Log Viewer**](https://fivetran.com/docs/hvr6/user-interface/viewing-log) dialog showing the job's runtime information and errors, and also the **More Options** menu  allowing you to manage every job separately.



 Option | Description |
 **Start Job** | Changes the job state to **RUNNING**. |
 
**Suspend/Unsuspend Jobs**
**** | 
Suspend or unsuspend the job.

`**Since** v6.1.0/3` When you suspend capture and/or integrate jobs in the **RUNNING** state, HVR enables a so-called 'graceful suspension' - a process that waits until the replication job cycle is completed before moving the job into the **SUSPEND** state. This ensures that no pending transactions are left as the job stops at the end of a cycle. During graceful suspension, the following dialog appears. Once the safe suspension is done, the dialog is closed automatically. There is also an option to do force suspend which will suspend the job immediately by killing the job process. However, note that the force suspension may leave the job in the **PENDING** state. For more information about job states, see section [Scheduler - Job States](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler#jobstates).


 |
 **Delete Job** | Delete a job from the channel. |
 **Go to Event** | Open the **[Event Details](https://fivetran.com/docs/hvr6/user-interface/events/event-details)** page for the recent event associated with the job (applies only to the **[Activate](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication)**, **[Compare](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data)**, and **[Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)** jobs if they have **DONE** or **RUNNING** state). |
 **Cancel Event** | 
If the event is executed by the corresponding job, this execution is stopped. The event is canceled by setting the event status to **CANCELED**. Only events in the **ACTIVE** state can be canceled (e.g. activate, refresh or compare events). A canceled event will not be executed anymore.
 |
 **Job Attributes** | This opens the **Job Attributes** dialog, where you can set [attributes](https://fivetran.com/docs/hvr6/internal-objects/job-attributes) for a specific job. |
 **Environment Variables** | This opens the **Job Environment Variables** dialog, where you can set environment variables for a specific job. |
 **New Refresh** | Start the refresh job once again. This applies only to a **[Refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)** job. |
 **New Compare** | Start the compare job once again. This applies only to a **[Compare](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data)** job. |

