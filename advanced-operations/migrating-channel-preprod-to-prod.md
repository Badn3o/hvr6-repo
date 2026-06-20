# Migrating Channel from Pre-Production to Production - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/migrating-channel-from-pre-production-to-production

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/migrating-channel-from-pre-production-to-production/index.md)

# Migrating Channel from Pre-Production to Production


This section describes the requirements and step-by-step instructions on how to migrate a channel from a pre-production environment to a production environment.

## Scenario


A pre-production environment in Fivetran HVR may refer to some kind of staging environment that helps to safely set up, configure, test, and integrate new replication channels. HVR provides a possibility to migrate a replication channel from the pre-production to the production using the channel export and import functionality.

## Prerequisites


For the purposes of this article, it is assumed that:

- the channel to be migrated is already configured on the pre-production
- the production environment is up and running
- the channel and locations to be migrated do not exist on the production environment


## Steps To Migrate Channel


- 
In pre-production, export the channel definition to a file.

a. On the [**Channel Details**](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details) page, click the **More Options** icon  and select **Export Channel Definition**.

b. In the **Export Channel** dialog, if required, include the locations and actions contained in the channel in the exported file.

c. In case locations are included in the export file, choose the way the [classified data](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/classification-of-data) related to the locations will be exported. For more information, see section [Exporting Channel Definition](https://fivetran.com/docs/hvr6/user-interface/channels/importing-and-exporting-channel-definition#classifiedinfo).

c. Click **Export** and save the file.



Use command **hvrdefinitionexport** to export the channel definition. For example, the following command exports channel **mychannel** with its locations and actions to the **chn_export** file.
hvrdefinitionexport -c mychannel -m -a myhub chn_export

> **Important:** 
By default, classified data is exported obfuscated. You can specify how to export the classified data using option **-V** of command [**hvrdefinitionexport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionexport).


For more information about all options of the command, see page [**hvrdefinitionexport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionexport).

- 
In production, import the channel to a hub.

a. On the [**Channels**](https://fivetran.com/docs/hvr6/user-interface/channels) page, click the **More Options** icon  and select **Import Channel Definition**.

b. Browse for the exported file and click **Open**. The **Import Summary** dialog shows the details of the import.

c. Click **Continue**.

> **Important:** 
If the channel was exported with location property values [encrypted with single-use transport key](https://fivetran.com/docs/hvr6/user-interface/channels/importing-and-exporting-channel-definition#classifiedinfo), a warning dialog will be displayed prompting you to enter the appropriate transport key. For more information, see section [Importing Channel With Encrypted Data](https://fivetran.com/docs/hvr6/user-interface/channels/importing-and-exporting-channel-definition#importingchannelwithencrypteddata). If the channel was exported with [redacted](https://fivetran.com/docs/hvr6/user-interface/channels/importing-and-exporting-channel-definition#classifiedinfo) location property values, a warning dialog will be displayed prompting you to proceed with importing the redacted values. For more information, see section [Importing Channel With Redacted Data](https://fivetran.com/docs/hvr6/user-interface/channels/importing-and-exporting-channel-definition#importingchannelwithredacteddata).


Use command **hvrdefinitionimport** to import the channel definition to the hub. For example, the following command adds a channel supplied in the **chn_export** file to the hub.
hvrdefinitionimport myhub chn_export

> **Important:** 
If the channel was exported with location property values [encrypted with a single-use transport key](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionexport#optionv), a warning will be displayed prompting you to enter the appropriate transport key. If the channel was exported with [redacted](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionexport#optionv) location property values, a warning will be displayed saying that the corresponding location properties (e.g. [**Database_Password**](https://fivetran.com/docs/hvr6/property-reference/location-properties#databasepassword)) contain redacted values. For more information, see option [**-V**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionexport#optionv) on page [**hvrdefinitionexport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionexport).


For more information about all options of the command, see page [**hvrdefinitionimport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionimport).

- 
In production, activate replication for the imported channel.

a. On the [**Channel Details**](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details) page, click **Activate Replication** at the top-right menu.

b. In the **Activate Replication** dialog, leave all the options selected by default.

c. Click **Activate**.

For more information about all activation options, see page [Activating Replication](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication).

Use command **hvractivate** to activate replication in the channel. For example, the following command activates replication for channel **mychannel**.
hvractivate -J cap -J integ myhub mychannel

For more information about all options of the command, see page [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate).



## See Also


- [Migrating Channel From HVR Version 5](https://fivetran.com/docs/hvr6/advanced-operations/migrating-channel-from-hvr-version-5)

