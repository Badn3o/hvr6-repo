# Channels - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/user-interface/channels

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/user-interface/channels/index.md)

# Channels


This section describes and illustrates how to create, view, and manage [channels](https://fivetran.com/docs/hvr6/getting-started/concepts/architecture) in HVR.

The **Channels** page displays a list of all channels available in the current HVR Hub and various options to [manage channels](#managingchannels).



The **Channels** page displays the following information about channels:

 Field | Description |
 **CHANNEL** | Indicates the channel name. Clicking on a channel name opens the [Channel Details](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details) page. |
 **DESCRIPTION** | Indicates the description of a channel (optionally specified during [channel creation](https://fivetran.com/docs/hvr6/user-interface/channels/creating-channel)). |
 **REPLICATION STATUS** | Indicates the details on whether the replication is activated, replication status, etc. |
 **LOCATIONS** | Indicates the source and target locations within a channel. Location names are links to the corresponding [Location Details](https://fivetran.com/docs/hvr6/user-interface/locations/location-details) pages. |


## Filtering Channels


By default, the page displays all channels related to a current hub. You can easily find the channels you need using one of the following filters.

- 
The **Locations** selector allows you to display only channels containing the selected location. For this, click **All Locations** and start typing the location name. The location names get filtered based on the characters you type. Select the required location and its name will be pinned in the **Locations** selector field.

- 
The **Search** filter allows you to search channel(s) by name. The channels get filtered as you type.





## Managing Channels


The following options to manage channels are available at the top right menu, as well as under the **More options** menu .

> **Note:** 
To select multiple channels in one go, select the first channel, hold the **Shift** key and then select the last channel - all channels in between the first and the last will be selected.


- 
[**Add Channel**](https://fivetran.com/docs/hvr6/user-interface/channels/creating-channel)
Create a new channel.

- 
[**Import or Export Channel Definitions**](https://fivetran.com/docs/hvr6/user-interface/channels/importing-and-exporting-channel-definition)
Import the definition of one channel or multiple channels at once.

- 
[**View Actions**](https://fivetran.com/docs/hvr6/user-interface/action-list)
View actions defined in a channel in the [**Actions List Drawer**](https://fivetran.com/docs/hvr6/user-interface/action-list).

- 
**Show Start Page**
Open the **Start Page**. This is a landing page that opens when you first access the web UI. This page offers a starting point for new users that helps them build up a channel in HVR.



Every channel also has its own **More Options** menu  with the following set of options:

- [**Delete Channel**](https://fivetran.com/docs/hvr6/user-interface/channels/deleting-channel)
- [**Duplicate Channel**](https://fivetran.com/docs/hvr6/user-interface/channels/duplicating-channel)
- [**Rename Channel**](https://fivetran.com/docs/hvr6/user-interface/channels/renaming-channel)
- [**Export Channel Definitions**](https://fivetran.com/docs/hvr6/user-interface/channels/importing-and-exporting-channel-definition).



