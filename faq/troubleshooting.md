# Troubleshooting Access to Hub System - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/faq/troubleshooting/troubleshooting-access-to-hub-system

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/faq/troubleshooting/troubleshooting-access-to-hub-system/index.md)

# Troubleshooting Hub System Access Issues


This section covers various access challenges you may encounter with the HVR Hub System and provides workarounds to resolve them.

> **Important:** 
Direct Command Line Interface (CLI) access is required - all commands listed on this page should be executed directly on the machine where the HVR Hub System is installed. Only a user who has install privileges on the machine (e.g. system administrator) may execute these commands.


---

## Unable to Log in


### Issue


User is not able to log in because of forgotten/wrong username or password. In the HVR UI, the following message is displayed in this scenario:



### Resolution


To resolve this problem, you can use either of the following methods:
Reset User Password
### Reset User Password


A user's password can be reset from HVR UI or CLI.

To reset a user's password from HVR UI, perform the following step as a user with **SysAdmin** permission:

- On the [**System**](https://fivetran.com/docs/hvr6/user-interface/system) page, select [**Users**](https://fivetran.com/docs/hvr6/user-interface/system/users) tab.
- Click **More Options** menu  of the user for whom the password needs to be reset and select **Show Preferences**.

- Click **Reset Password**.



To reset a user's password from CLI, use the command [**hvruserconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig):
hvruserconfig -r <em>username</em>

> **Tip:** 
To list all existing users, execute command [**hvruserconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig) without any options.

Create New User from CLI
### Create New User from CLI


Create a new user and assign the required privilege.

- 
Create a new user using the command [**hvruserconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig):
hvruserconfig -c <em>new_user</em>

> **Important:** 
To set the authentication mechanism for this user, supply option **-A**. If option **-A** is not supplied, then by default the user is created with **local** authentication.


- 
Grant the required permission to the new user using the command [**hvrreposconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrreposconfig):

For example, to grant **SysAdmin** permission to the new user named **myuser**:
hvrreposconfig -A user:myuser=SysAdmin

Since 6.1.5/2, the following command should be used, as -A option is deprecated.
hvrreposconfig User_Access.myuser.sysadmin=true


Reset User Password Using Setup Mode
### Reset User Password Using Setup Mode


Initiate the HVR Hub System setup mode and then reset the user's password from the [**System Setup**](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub/setting-up-hub-from-browser) page.

> **Warning:** 
Initiating setup mode for a HVR Hub System with live hub(s) will stop all replication activities.

In setup mode, the HVR Hub Server will be stopped, which means all replication activities will be terminated.


- 
Initiate the setup mode using the command [**hvrhubserverconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserverconfig):
hvrhubserverconfig Setup_Mode=true

- 
Launch HVR UI in a browser and perform the following steps:

> **Note:** 
If the HVR UI is already open in a browser, just relaunch/refresh the page.


- On the [**System Setup**](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub/setting-up-hub-from-browser) page, click **Proceed with System Setup**.
- In the section **Complete the System Setup**, click **More Options** menu  of the user (for whom the password needs to be reset) and select **Reset Password**.

- Click **Complete System Setup** to save the changes and exit setup mode.




---

## Hub User Has Insufficient Privileges


### Issue


The hub user does not have sufficient privileges/permissions to perform certain operations (e.g. [**Refresh**](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data)) on a hub.

### Resolution


To resolve this problem, you can use either of the following methods:
Grant Permission to User
### Grant Permission to User


A user's permissions can be managed from HVR UI and CLI.

To manage a user's permissions from HVR UI, perform the following step as a user with **SysAdmin** or **HubOwner** permission:

- On the [**System**](https://fivetran.com/docs/hvr6/user-interface/system) page, select **Permissions** tab.
- Click **Add Access**.

- Select the **User** to be granted the permission.
- Select the required permission available under **CURRENT HUB**.

- Click **Save**.


To manage a user's permissions from CLI, use the command [**hvrhubconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubconfig). For example, the following command will add or update the permissions for user **myuser** to be set as **HubOwner** on hub **myhub**:
 hvrhubconfig -A user:myuser=HubOwner myhub

Since 6.1.5/2, the following command should be used, as -A option is deprecated.
 hvrhubconfig User_Access.myuser.hubowner=true myhub
Grant SysAdmin Permission Using Setup Mode
### Grant SysAdmin Permission Using Setup Mode


Initiate the hub system setup mode and then grant the user **SysAdmin** permission from the [**System Setup**](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub/setting-up-hub-from-browser) page.

> **Warning:** 
Initiating setup mode for a HVR Hub System with live hub(s) will stop all replication activities.

In setup mode, the HVR Hub Server will be stopped, which means all replication activities will be terminated.


- 
Initiate the setup mode using the command [**hvrhubserverconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserverconfig):
hvrhubserverconfig Setup_Mode=true

- 
Launch HVR UI in a browser and perform the following steps:

> **Note:** 
If the HVR UI is already open in a browser, just relaunch/refresh the page.


- On the [**System Setup**](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub/setting-up-hub-from-browser) page, click **Proceed with System Setup**.
- In the section **Complete the System Setup**, click **More Options** menu of the user that require **SysAdmin** permission and select **Assign as SysAdmin**.

- Click **Complete System Setup** to save the changes and exit setup mode.




---

## Hub Server Repository Connectivity Error


### Issue


The hub server is not able to connect to the hub repository due to a changed repository connection property (e.g. password for the repository database has changed).

### Resolution


To resolve this problem, you can use either of the following methods:
Update Repository Properties Using Setup Mode
### Update Repository Properties Using Setup Mode


Initiate the HVR Hub System setup mode and then reconfigure/update the hub repository connection properties from the [**System Setup**](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub/setting-up-hub-from-browser) page.

- 
Initiate the setup mode using the command [**hvrhubserverconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserverconfig):
hvrhubserverconfig Setup_Mode=true

- 
Launch HVR UI in the browser and perform the following steps in System Setup page:

> **Note:** 
If the HVR UI is already open in a browser, just relaunch/refresh the page.


- On the [**System Setup**](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub/setting-up-hub-from-browser) page, click **Proceed with System Setup**.
- In the section **Connection to Repository Database**, click **Edit** to update the hub repository connection properties.
- Click **Complete System Setup** to save the changes and exit setup mode.



Update Repository Properties from CLI
### Update Repository Properties from CLI


Reconfigure/update the [hub repository connection properties](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties) directly from CLI using the command [**hvrhubserverconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserverconfig):
hvrhubserverconfig <em>hub_server_property</em>=<em>property_value</em>

For example, if the username and password for the repository database has changed, execute:
hvrhubserverconfig Database_User=mynewrepodb Database_Password=mynewrepodbpassword
