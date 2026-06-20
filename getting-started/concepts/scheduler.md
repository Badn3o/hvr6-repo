# Scheduler for HVR

**Source:** https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/concepts/scheduler/index.md)

# Scheduler


The **Scheduler** is an internal process managed by the HVR Hub Server. It manages jobs and job groups for each channel and job types. All jobs and job groups are contained within the **SYSTEM** job group.

The jobs are generated using commands [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate), [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) and [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare) or from the corresponding [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication), [**Refresh Data**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), and [**Compare Data**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) dialogs in the [User Interface](https://fivetran.com/docs/hvr6/user-interface). After they are generated, these jobs can be controlled by attributes defined by the jobs themselves and on the job groups to which they belong. These attributes control when the jobs get scheduled.

## Job States


The **Scheduler** schedules jobs. Each job performs a certain task. At any moment a job is in a certain state. For instance, when a job is waiting to be run, it is in state **PENDING**; when a job is running, it is in state **RUNNING**.

Jobs can be either acyclic or cyclic. Acyclic jobs will only run once, whereas cyclic jobs will rerun repeatedly. When a cyclic job runs, it goes from state **PENDING** to **RUNNING** and then back to state **PENDING**. In this state, it waits to receive a signal (trigger) in order to run again. When an acyclic job runs, it goes from state **PENDING** to **RUNNING** and then disappears.

If for some reason a job fails to run successfully, the **Scheduler** will change its state first to **ALERTING**, then **RETRY** and will eventually run again. If a job stays in state **RUNNING** for too long, it may be marked with state **HANGING**; if it finishes successfully it will just become **PENDING**.

For more information about HVR jobs and their states, see [Jobs](https://fivetran.com/docs/hvr6/getting-started/concepts/jobs) section.
