# Location Details - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/user-interface/locations/location-details

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/user-interface/locations/location-details/index.md)

# Location Details


The **Location Details** page provides detailed information about a specific location and various options to manage the location. The information displayed on this page are grouped into the following panes:



## Agent


The **Agent** pane displays connection information for the HVR Agent service, if configured for the current location.

Click **Edit** to open the **Agent** dialog where you can modify the agent's connection information or set up a new connection to an agent service. For instructions on how to set the agent connection parameters, see section [Select Agent Connection](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location#step2selectagentconnection) in [Creating Location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location).

> **Note:** 
In the **Agent** dialog, you can also reconfigure the agent service by clicking the **Configure Agent Service** button, which will open the **Agent Service Configuration** dialog. For instructions on how to configure the agent service, see section [Configuring HVR Agent from Browser](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser).


> **Important:** 
If the configuration for an existing agent service is modified/updated, ensure to reflect those changes in all locations that use this agent service. For example, if the password of an agent user is updated, then that user's password must be updated in all locations that use this agent service.




## Database Connection


The **Database Connection** pane displays connection details for the current location, which can be a database or file location. For more information on setting up a connection to each location type, see [Location Connection](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location/location-connection).

> **Important:** 
For file locations, like Azure DLS, the pane will be named **File Connection**.


To modify location connection details:

- 
On the **Database Connection** pane, click **Edit**.

- 
In the **Database Connection** dialog, make the necessary changes.

- 
Click **Save**.

> **Important:** 
Fields in the **Database Connection** dialog will differ depending on the location type you are connected to.






## Source and Target Properties


The **Source and Target Properties** pane displays the location properties defined for the current location. For more information about all location properties available in Fivetran HVR, see section [Location Properties](https://fivetran.com/docs/hvr6/property-reference/location-properties).

To modify location properties:

- 
On the **Source and Target Properties** pane, click **Edit**.

- 
In the **Source and Target Properties** dialog, make the necessary changes.

- 
Click **Save**.





## Channel Membership


The **Channel Membership** pane displays the following information about the channel(s) containing the location.

 Field | Description |
 **CHANNEL** | Channel to which the location belongs. |
 **REPLICATION STATUS** | Defines whether the replication is currently activated or not yet activated, whether jobs are running. Here you can [activate replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication) or replication components that are not activated. |
 **LOCATION GROUP** | Name of the location group to which the location belongs. |
 **TABLES** | Number of tables in the channel. |
 **CHANGES** | Number of capture or integrate changes per the time interval selected on the **[Channels](https://fivetran.com/docs/hvr6/user-interface/channels)** or **[Jobs](https://fivetran.com/docs/hvr6/user-interface/jobs)** pages. |


The **More options** menu  associated with a channel provides additional options to manage the location within that channel:

- [**Change Location Group**](https://fivetran.com/docs/hvr6/user-interface/locations/changing-location-group)
Change the location group of the location in the channel. You can either pick one of the existing location groups or create a new one.
- [**Delete from Channel**](https://fivetran.com/docs/hvr6/user-interface/locations/deleting-location)
Delete the location from the channel.
- [**Activate replication**](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication)
Start replication in the channel. Set or reset replication components as required.
- [**Deactivate replication**](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication)
Stop all replication jobs in the channel. This will drop the replication components created for the channel.
- [**Compare Data**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data)
Compare data in the location between source and target.
- [**Refresh Data**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data)
Copy data in the location from source to target.
- [**Create/Alter Target Table**](https://fivetran.com/docs/hvr6/user-interface/tables/creating-or-altering-target-tables)
Create tables that are missing in a target location or alter/recreate the existing tables.




### Adding Location to an Existing Channel


To add the location to an existing channel:

- On the **Channel Membership** pane, click **Add to an Existing Channel**.
- In the **Add to Channel** dialog, select a required channel from the drop-down list.
- Select the location group for the location or add the location to a new location group by entering the group name in the **New location group** field.
- Click **Save**.



## Managing Location


The following options to manage a location are available at the top-right menu, as well as under the **More options** menu .

- **Test Connection**
Verify the location connection status.
- [**Export Location Definition**](https://fivetran.com/docs/hvr6/user-interface/locations/importing-and-exporting-location-definition)
Export the location definition into a JSON file
- [**Export Agent Connection**](https://fivetran.com/docs/hvr6/user-interface/locations/importing-and-exporting-agent-connection)
Export Agent connection details.
- [**Import Agent Connection**](https://fivetran.com/docs/hvr6/user-interface/locations/importing-and-exporting-agent-connection)
Import Agent connection details.
- [**View Actions**](https://fivetran.com/docs/hvr6/user-interface/action-list)
View actions defined in a channel in the **Actions** panel.
- [**All Location Properties**](https://fivetran.com/docs/hvr6/user-interface/locations/managing-location-properties)
View, modify, add, and delete the properties of the location.
- [**Duplicate Location**](https://fivetran.com/docs/hvr6/user-interface/locations/duplicating-location)
Create a copy of the current location.
- [**Delete Location from Hub**](https://fivetran.com/docs/hvr6/user-interface/locations/deleting-location)
Delete the location from the hub.
- [**Rename Location**](https://fivetran.com/docs/hvr6/user-interface/locations/renaming-location)
Rename the location.

