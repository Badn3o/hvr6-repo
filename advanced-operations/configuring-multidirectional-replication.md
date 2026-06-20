# Configuring Multidirectional Replication - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/configuring-multidirectional-replication

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/configuring-multidirectional-replication/index.md)

# Configuring Multidirectional Replication


Multidirectional replication assumes that data is replicated between two (bi-directional) or more locations in both directions, and end users (applications) modify data on both sides. For more information on different Fivetran HVR replication types, see [Replication Topologies](https://fivetran.com/docs/hvr6/getting-started/concepts/replication-topologies).

For the list of locations, on which bi-directional replication is supported, refer to the [relevant section](https://fivetran.com/docs/hvr6/capabilities/610#bidirectionalreplication) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

## Channel Setup for Multi-Directional Replication


> **Important:** 
The steps described in this section are applicable for both bi-directional and multidirectional replication.


By default, all locations in a multidirectional channel will be added to a single location group named **SOURCE_TARGET** with the [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) and [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) actions defined on that group. Any changes made to any of the locations will be propagated to all the other locations within the channel.

The following steps include configuring multi-directional replication with three Oracle locations in the HVR [user interface](https://fivetran.com/docs/hvr6/user-interface).

- 
Create three Oracle locations **app1**, **app2**, and **app3**. Follow the procedure described on the page [Creating Location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) for each of the locations.

- 
Define a channel for the replication: right-click **Channel Definitions** and select **New Channel** and enter the name of the channel **chn**. Click **OK**.

- Navigate to the left sidebar and click **CHANNELS**.
- On the **Channels** page, click **Create Channel** at the top right.
- On the **Create New Channel** page, under **Select Channel Type**, click **Multidirectional**.

- Under **Select Locations**, select locations **app1**, **app2**, and **app3**. Click **Confirm Locations**. 

- Click **Save Channel and Continue**.
- Specify the channel name and, optionally, the description of the channel.

- Click **Select Tables** to add tables to the channel.

- In the table selection dialog, select the required tables and click **Save**. For more information on different options and filters for selecting tables, see section [Adding Tables to a Channel](https://fivetran.com/docs/hvr6/user-interface/tables/adding-tables-to-a-channel).



- 
Confirm table selection.


- 
Click **Complete Channel Creation**. This will activate replication, lunch the [refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh), and start [capture](https://fivetran.com/docs/hvr6/action-reference/capture) and [integrate](https://fivetran.com/docs/hvr6/action-reference/integrate) jobs in the channel.

> **Important:** 
- To manually configure custom activation components, click **Replication Activation Options**. This will open the **Replication Activation Options dialog**, in which you can set up the activation parameter as required. For detailed information about each activation component, see section [Components for Activating Replication](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/components-for-activating-replication).
- To define additional [actions](https://fivetran.com/docs/hvr6/action-reference) for the channel, unselect the **Activate replication** option. See section [Additional Configuration for Multidirectional Channel](#additionalconfigurationformultidirectionalchannel).
- To suspend the start of capture and integrate jobs, unselect the **Start Replication Jobs**.


You can [activate the replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication), run the [refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), and start the replication jobs manually later.






### Additional Configuration for Multidirectional Channel


- 
Parameter [**OnErrorSaveFailed**](https://fivetran.com/docs/hvr6/action-reference/integrate#onerrorsavefailed) of action [**Integrate**](https://fivetran.com/docs/hvr6/action-reference/integrate) allows HVR to continue replication when errors occur. The error message including the row causing the failure is stored in the fail table *tbl*_**f** and can be investigated afterwards (see command [**hvrretryfailed**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrretryfailed)). The errors will also be written to the log file.

- 
There can be collisions in a multidirectional replication environment. For example, users in different databases may update the same row at the same time, or a row may be updated in one database and deleted in another database. If collisions happen, then the end result may be that your databases get out of sync. HVR provides a sophisticated collision detection capability (action [**CollisionDetect**](https://fivetran.com/docs/hvr6/action-reference/collisiondetect)) that will ensure that the most recent change to a row always wins and systems remain in sync. In the [**CollisionDetect**](https://fivetran.com/docs/hvr6/action-reference/collisiondetect) dialog select option [**TimestampColumn**](https://fivetran.com/docs/hvr6/action-reference/collisiondetect#timestampcolumn) and select the timestamp column in the replicated tables for collision detection. A timestamp column should be manually added beforehand to each replicated table in the multi-directional channel. Consider using action [**CollisionDetect**](https://fivetran.com/docs/hvr6/action-reference/collisiondetect) only on tables with a reliable timestamp column that accurately indicates when the data was last updated.

> **Important:** 
In some multi-directional replication environments, the collisions may be prevented at the application level (using customers' own application partitioning), thus avoiding the need to use action [**CollisionDetect**](https://fivetran.com/docs/hvr6/action-reference/collisiondetect).



