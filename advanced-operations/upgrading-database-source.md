# Upgrading Database on Source Location - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/upgrading-database-on-source-location

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/upgrading-database-on-source-location/index.md)

# Upgrading Database on Source Location


This section provides step-by-step instructions for upgrading a source database in a channel with activated replication to ensure that no data is lost during the upgrade.

> **Important:** 
These are the recommended steps that may vary depending on the database being upgraded.


## Upgrade Steps


- 
Stop your application that is making changes to the database.

- 
Ensure all changes made by the application are captured, and wait for the replication latency to reach zero. For more information on monitoring the replication latency, refer to the [Statistics](https://fivetran.com/docs/hvr6/user-interface/statistics#graphsandmetrics) page.

- 
Suspend the capture and integrate jobs running in a channel.

- Go to the [**Channel Details**](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details) page.
- Under the **Jobs** pane, select the capture and integrate jobs.
- Click **Suspend Jobs** at the top right of the **Jobs** pane.




Run the [**hvrsuspend**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsuspend) command. For example:
hvrsuspend myhub mychannel

- 
Upgrade the source database.

- 
[Activate](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate) replication in the channel to capture changes from the beginning of the oldest current (not closed) transaction, and regenerate the jobs, state tables, and enroll information for the tables.

- Go to the [**Channel Details**](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details) page and click [**Activate Replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication).
- In the **Activate Replication** dialog, under [**Replication Components**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication#replicationcomponents), select all options except **Supplemental Logging**.
- Click **Activate Replication**.




Run the command [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate) with options **-J**, **-E**, **-i**, **-ojesr**. For example:
hvractivate -J cap -J integ -E -i oldest_tx -ojesr myhub mychannel

- 
Start your application.


