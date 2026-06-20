# Event Details - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/user-interface/events/event-details

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/user-interface/events/event-details/index.md)

# Event Details


The **Event Details** page contains three main panes that display various information about the selected event.

> **Important:** 
The number of panes and the set of parameters on each of the panes may differ depending on the type of event.


- 
**Top pane**: displays the following information about an event: the channel and location(s) where the event occurred, the event state at the current moment, the job associated with the event, when the event was started, its duration, etc.
For certain event types, such as **Activate**, **Deactivate**, **Compare**, and **Refresh**, you can view the event-specific log information by clicking [**View Log**](https://fivetran.com/docs/hvr6/user-interface/viewing-log). For **Compare** and **Refresh** events, you can repeat the event (buttons **Repeat** **Compare** and **Repeat Refresh**), start a new event (buttons **New Compare** and **New Refresh** under the **More Options** menu icon ), and cancel the event (button **Cancel Event** under the **More Options** menu icon ).

The following event states are available:

- 
**CURRENT** - The event is not completed yet.

- 
**CANCELED** - The event was canceled by a user.

- 
**DONE** - The event is completed successfully.

- 
**FAILED** - The event failed to complete due to an error.

- 
**WAITING** - The event will run at a scheduled time.



- 
**Middle pane**: displays additional details specific to each event.

- 
**Bottom pane**: is displayed only for the **Compare** and **Refresh** events. It contains in-depth information about compare/refresh results. For more information on each column displayed on this pane, see [Refresh and Compare Results](#refreshandcompareresults) below.



The following screenshot displays the **Compare** event.



## Refresh and Compare Results


The **Results** pane (see the image above) is displayed for the **Refresh** and **Compare** events. Following are the fields/columns displayed in the results:

 Field | Description |
 **COMPRESSED BYTES** | Indicates the number of bytes the HVR Hub transferred (after compression) |
 **COMPRESSION RATIO (BY MEMORY)** | Indicates the number of compressed bytes transmitted over the network compared with the HVR representation of that row in memory. |
 **DIFF FILE** | 
(Applicable only for **Compare** and **Refresh**). Opens the **View Diff File** dialog allowing to [inspect a binary file](https://fivetran.com/docs/hvr6/advanced-operations/analyzing-diff-file) that contains the list of differences detected. This file can be viewed both in the user interface and dumped as XML using the **[hvrrouterview](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrouterview)** command.

> **Important:** 
In the **[Refresh Data into Target](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)** dialog, this column is displayed only if option [**Repair - Row by Row Granularity**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data#repairrowbyrowgranularity) is selected.

 |
 **DURATION** | Indicates the time taken to compare the specific table. |
 **EVENT DURATION** | (Applicable only for **Compare**) Indicates the time taken to finish the compare operation. |
 **EVENT SPEED** | (Applicable only for **Compare**) Indicates the speed of compare operation in rows per second. |
 **NUMBER OF DIFFERENT TABLES** | (Applicable only for **Compare**) Indicates the number of tables that are not identical. |
 **NUMBER OF TABLES** | Indicates the total number of tables compared. |
 **NUMBER OF INCONCLUSIVE TABLES** | (Applicable only for **Online Compare**) indicates the total number of inconclusive tables. |
 **ROWS IN MOTION IDENTICAL** | (Applicable only for **Online****Compare**) indicates the number of "in-flight" differences that are about to be replicated from source to target. |
 **ROWS IN MOTION INCONCLUSIVE** | (Applicable only for **Online****Compare**) indicates the number of rows that are changing and are not identified as real differences or "in-flight" differences. |
 **ROWS ONLY ON SOURCE** | (Applicable only for **Compare**) Indicates the total number of rows available only in a source location(s) that need to be inserted into a target. |
 **ROWS ONLY ON TARGET** | (Applicable only for **Compare**) Indicates the total number of rows available only in a target location(s) that need to be deleted from a target. |
 **ROWS PROCESSED DURING EVENT** | (Applicable only for **Compare**) Indicates the total number of rows compared. |
 **ROWS WHICH DIFFERS** | (Applicable only for **Compare**) Indicates the total number of rows that need to be updated on target. |
 **SOURCE ROWS SELECTED** | Indicates the total number of rows selected in the source table(s). |
 **TARGET ROWS SELECTED** | (Applicable only for **Compare**) Indicates the total number of rows selected in the target table(s). |
 **SOURCE ROWS USED** | Indicates the total number of rows that were actually compared in the source. |
 **TARGET ROWS USED** | Indicates the total number of rows that were actually compared in the target. |
 **SPEED** | Indicates the speed of compare operation while comparing the specific table in rows/secs. |
 **START TIME** | Indicated the time when the compare operation started. |
 **STATE** | 
Indicates the table state.

The following table states are available:

- 
**BUSY** - The event is busy with subtasks for this table.

- **BUSY/DIFFERENT** - The event is busy with subtasks for this table. A compare difference was detected already.
- **DONE** - The event has completed all subtasks for this table.
- 
**DONE/DIFFERENT** - The event has completed all subtasks for this table. A compare difference was detected: the tables are NOT identical in source and target locations.

- 
**DONE/IDENTICAL** - The event has completed all subtasks for this table. No compare difference was detected: tables are identical in source and target locations.

- 
**DONE/INCONCLUSIVE** - (applicable only for **Online Compare**). The event has completed all subtasks for this table. Compare differences were encountered, but it cannot be determined whether these are persistent or due to online/live change.

- **PENDING** - The event has not yet started subtasks for this table.

 |
 **SUBTASKS DONE(BUSY)/TOTAL** | Indicates the number of subtasks that are done(busy) and the total number of them. |
 **TABLE** | Indicates a table name in a channel. |

