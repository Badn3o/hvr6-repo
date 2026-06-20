# Tuning Capture Checkpoints - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/tuning-capture-checkpoints

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/tuning-capture-checkpoints/index.md)

# Tuning Capture Checkpoints


Defining the **Capture Checkpoint Tuning** option enables storing of uncommitted long running transactions into checkpoint files so that if capture is interrupted, the uncommitted changes will be read from the checkpoint file when replication resumes. This prevents rereading the DBMS transaction logs from the beginning of the uncommitted transaction.

Fivetran HVR's capture job periodically saves its open transactions, so it can recover quickly on restart. In the HVR UI, you can also define the frequency at which the checkpoints are created using the option **Perform Checkpointing** (equivalent location property [**Capture_Checkpoint_Frequency**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturecheckpointfrequency)). Additionally, the storage location for the capture checkpoint files can be configured using the option **Disk Storage** (equivalent location property [**Capture_Checkpoint_Storage**](https://fivetran.com/docs/hvr6/property-reference/location-properties#capturecheckpointstorage)). You can also define a retention period for the checkpoint files using the option **Retain Checkpoints** (equivalent location property [**Capture_Checkpoint_Retention**](https://fivetran.com/docs/hvr6/property-reference/location-properties)).

Capture check-pointing is supported only for certain location types. For the list of supported location types, see [Log-based capture checkpointing](https://fivetran.com/docs/hvr6/capabilities/610#capabilitiescapcheckpoint) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

## Perform Checkpointing


Checkpointing frequency is set in seconds for long-running transactions, so the capture job can recover quickly when it restarts. Value *secs* is the interval (in seconds) at which the capture job creates checkpoints.

Thedefaultcheckpoint frequency is **300** seconds (5 minutes). If value **0** is set, checkpoints are not written.

Without checkpoints, capture jobs must rewind back to the start of the oldest open transaction, which can take a long time and may require access too many old DBMS log files (e.g. archive files).

The checkpoints are written into **HVR_CONFIG/hubs/***hub***/channels/***channel***/locs/***location***/capckp** directory. If a transaction continues to make changes for a long period then successive checkpoints will not rewrite its same changes each time; instead the checkpoint will only write new changes for that transaction; for older changes it will reuse files written by earlier checkpoints.

Checkpoints are written only for long-running transactions. For example, if the checkpoint frequency is each 5 minutes but users always do an SQL commit within 4 minutes then checkpoints will never be written. However, if users keep transactions open for 10 minutes, then those transactions will be saved but shorter-lived ones in the same period will not.

The frequency with which capture checkpoints are written is relative to the capture jobs own clock, but it decides whether a transaction has been running long enough to be checkpointed by comparing the timestamps in its DBMS logging records. As a consequence, the maximum (worst-case) time that an interrupted capture job would need to recover (rewind back over all its open transactions) is its checkpoint frequency plus the amount of time it takes to reread the amount of changes that the DBMS can write in that period of time.

When a capture job is recovering it will only use checkpoints which were written before the 'capture cycle' was completed. This means that very frequent capture checkpointing (say every 10 seconds) is wasteful and will not speed up capture job recovery time.

## Disk Storage


Storage location of capture checkpoint files for quick capture recovery.

> **Note:** 
In HVR UI, the option **Disk Storage** is displayed only when an HVR Agent is used for connecting to the location. If an agent is not used, the checkpoint files are saved in a directory on the capture location.


Available options are:

- 
**Agent machine**default: Checkpoint files are saved in a directory on capture location.

- 
**Hub machine**: Checkpoint files are saved in a directory on the hub server. Writing checkpoints to the hub is more resource-intensive because extra data must be sent across the network.

> **Important:** 
When capturing changes from an Oracle RAC, the checkpoint files should be stored on the hub server. This is necessary because the directory on the remote location, where the capture job would typically write checkpoints, may not be shared across the RAC cluster, so it may not be available when the capture job restarts.




For both the storage locations, the checkpoint files are saved in **HVR_CONFIG/hubs/***hub***/channels/***channel***/locs/***location***/capckp** directory.

When the capture job is restarted and if it cannot find the most recent checkpoint files (perhaps the contents of that directory have been lost during a failover), it will issue a warning and rewind to the start of the oldest open transaction.

## Retain Checkpoints


When this field/property is defined, it retains capture checkpoint files up to the specified period (in seconds).

The retained checkpoint files are saved in **HVR_CONFIG/hubs/***hub***/channels/***channel***/locs/***location***/capckpretain** directory.

> **Important:** 
By default, the checkpoint files are deleted as soon as the [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) does not require it anymore.

