# Events - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/concepts/events

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/concepts/events/index.md)

# Events


The event system maintains records for certain changes that a user makes in Fivetran HVR. These records are called events and are stored in the [**HVR_EVENT**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrevent) and [**HVR_EVENT_RESULT**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvreventresult) repository tables. An event is identified by a micro-second timestamp stored in the **ev_id_tstamp** column.

The key purposes of using the HVR event system are:

The **first** purpose is to maintain the audit trail of user activities that make certain changes in the HVR system. Event records contain details that include the event type, date and time, the user associated with the event, the event scope, and other information. This lets you track and analyze all user activities to see what events occurred and who performed them at a certain point in time.

The following activities create events in HVR:

- Command Line: Executing commands like [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate), [**hvrrefresh**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh), [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare), [**hvrstart**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrstart), [**hvrsuspend**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsuspend), [**hvrstats**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrstats), [**hvradapt**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvradapt), [**hvrcontrol**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcontrol), [**hvralertconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertconfig), and [**hvrdefinitionimport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionimport), [**hvrhubconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubconfig).
- User Interface: Changing a channel definition, starting or stopping any jobs, creating a hub, freezing/unfreezing a hub, and other operations.


The following activities do not create events in HVR:

- Automated occurrences inside HVR, e.g. activity of replication jobs. This is logged in the job's log files already.
- Read-only activities, such as executing commands like [**hvrrouterview**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrouterview) or [**hvrdefinitionexport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionexport).
- Operations on remote HVR machine, such as starting [**hvragentlistener**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener).


The **second** purpose is to hold the state for long-running operations and store the results of each [compare](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare) and [refresh](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrrefresh) operation.

The event-driven compare operation is driven by the state of an HVR event (**PENDING**, **DONE**, **FAILED**) in the HVR event system. HVR creates a compare job in the [Scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) and the compare operation is started under a compare event. If the compare operation is restarted, it will continue where it was interrupted rather than starting from the beginning. When performing an event-driven compare operation, if there is an existing compare event with the same job name in the **PENDING** state, then it is canceled (**FAILED**) by the new compare event. The same applies to the refresh operation.

## Event Scope


Events are typically associated with a hub, however, certain events my apply to the whole repository. Events can also be created with a scope, specifying which channel and locations were affected by the event. This scope is stored in the **chn_name**, **loc_name**, and **loc_name_2** columns of the [**HVR_EVENT**](https://fivetran.com/docs/hvr6/internal-objects/repository-tables#hvrevent) repository table.

## Event States


At any moment an event has a certain state. Audit logging events are created with a **DONE** state, so the state is not of interest in this case. For events of event-driven jobs, however, the state is important. The events are created in the **ACTIVE** state. Once the associated job executed the task of the event, the state is updated to **DONE**. It is also possible to cancel events, which sets the state to **CANCELED**. Some events can end up in the **FAILED** state due to an error.

An event can be in one of the following states:

- **CURRENT**: Event is not completed yet
- **CANCELED**: Event was canceled by a user
- **DONE**: Event is completed successfully
- **FAILED**: Event failed to complete due to an error
- **WAITING**: The event will run at a scheduled time


## Viewing and Managing Events


HVR offers the following methods for viewing and managing events:

- via **UI** - see [Events](https://fivetran.com/docs/hvr6/user-interface/events) and [Event Details](https://fivetran.com/docs/hvr6/user-interface/events/event-details)
- via **CLI** - see [**hvreventtool**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvreventtool)
- via **API** - see [**Event Interface**](https://fivetran.com/docs/hvr6/rest-api/rest-api-reference/610/6100/event)

