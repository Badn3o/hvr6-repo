# Uninstalling HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/install-and-upgrade/uninstall

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/install-and-upgrade/uninstall/index.md)

# Uninstalling HVR


This section describes step-by-step instructions on how to uninstall HVR from Linux, Unix, or Windows machine.

## Uninstalling from Linux or Unix


#### Deactivate channels


Deactivate replications for all channels that are currently activated.

Run the command [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate) with option **-d** to deactivate replication for a specific channel. You have to repeat the command for every activated channel.
hvractivate -d myhub mychannel

Go to the **Channels** page and [deactivate](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication) replication for all currently activated channels.

#### Delete hub system registration


> **Important:** 
This step is only applicable for customers on [Business Critical](https://fivetran.com/docs/hvr6/getting-started/pricing#businesscritical) pricing plan that have [registered the hub system with a Fivetran Account](https://fivetran.com/docs/hvr6/user-interface/system#registeringwithfivetranaccount).

Note that [deleting hub system registration](https://fivetran.com/docs/hvr6/user-interface/system#deletingfivetranaccountregistration) is available only through the [User Interface](https://fivetran.com/docs/hvr6/user-interface).


To delete hub system registration, follow these steps:

- Go to the [**System**](https://fivetran.com/docs/hvr6/user-interface/system) page.
- Click the **More Options** icon  at the top right and select **Licensing**.
- In the **Licensing** dialog, click **Delete Registration**.
- Click **OK** in the confirmation dialog.


> **Important:** 
Deleting a Fivetran account registration only removes the account registration information from the current hub's repository. This will not delete the Fivetran account itself.

However, deleting a Fivetran account registration will immediately stop uploading the [Monthly Active Rows (MAR)](https://fivetran.com/docs/getting-started/consumption-based-pricing#monthlyactiverows) data and the auto-renewal of the license will be stopped (so the license will expire after seven days).


#### Shut down hub and agent


If the HVR Hub and HVR Agent Listener are running, stop/shut them down using the following commands in CLI:

- 
To stop the HVR Hub Server, run command **hvrhubserver** with option [**-k**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserver#k):
hvrhubserver -k

- 
To stop the HVR Agent Listener, run command **hvragentlistener** with option [**-k**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener#k):
hvragentlistener -k



#### Remove the HVR repository user


To remove your repository user, run command **hvruserconfig** with option [**-d**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig#d):
hvruserconfig -d myuser

#### Remove repository tables


To drop the repository tables from the repository database, run command **hvrreposconfig** with option [**-d**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrreposconfig#d):
hvrreposconfig -d

#### Delete the installation


To remove the HVR installation files, delete the following folders:

- **HVR_HOME**. Path: **/home/myhvr/hvr_home**
- **HVR_CONFIG**. Path: **/home/myhvr/hvr_config**
- **HVR_TMP**. Path: **/home/myhvr/hvr_tmp**



## Uninstalling from Windows


#### Deactivate channels


Deactivate replications for all channels that are currently activated.

Run the command [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate) with option **-d** to deactivate replication for a specific channel. You have to repeat the command for every activated channel.
hvractivate -d myhub mychannel

Go to the **Channels** page and [deactivate](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication) replication for all currently activated channels.

#### Delete hub system registration


> **Important:** 
This step is only applicable for customers on [Business Critical](https://fivetran.com/docs/hvr6/getting-started/pricing#businesscritical) pricing plan that have [registered the hub system with a Fivetran Account](https://fivetran.com/docs/hvr6/user-interface/system#registeringwithfivetranaccount).

Note that [deleting hub system registration](https://fivetran.com/docs/hvr6/user-interface/system#deletingfivetranaccountregistration) is available only through the [User Interface](https://fivetran.com/docs/hvr6/user-interface).


To delete hub system registration, perform the following steps:

- Go to the [**System**](https://fivetran.com/docs/hvr6/user-interface/system) page.
- Click the **More Options** icon  at the top right and select **Licensing**.
- In the **Licensing** dialog, click **Delete Registration**.
- Click **OK** in the confirmation dialog.


> **Important:** 
Deleting a Fivetran account registration only removes the account registration information from the current hub's repository. This will not delete the Fivetran account itself.

However, deleting a Fivetran account registration will immediately stop uploading the [Monthly Active Rows (MAR)](https://fivetran.com/docs/getting-started/consumption-based-pricing#monthlyactiverows) data and the auto-renewal of the license will be stopped (so the license will expire after seven days).


#### Shut down hub and agent


If the HVR Hub and HVR Agent Listener are running, stop/shut them down using the following commands in CLI:

- 
To stop the HVR Hub Server, run command **hvrhubserver** with option [**-ah**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserver#a):
hvrhubserver -ah

- 
To stop the HVR Agent Listener, run command **hvragentlistener** with option [**-ah**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener#a):
hvragentlistener -ah



#### Remove the HVR repository user


To remove your repository user, run command **hvruserconfig** with option [**-d**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig#d):
hvruserconfig -d myuser

#### Remove repository tables


To drop the repository tables from the repository database, run command **hvrreposconfig** with option [**-d**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrreposconfig#d):
hvrreposconfig -d

#### Delete the installation


Use Windows Uninstaller to delete the HVR installation.
