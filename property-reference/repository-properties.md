# Repository Properties - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/property-reference/repository-properties

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/property-reference/repository-properties/index.md)

# Repository Properties


This section lists and describes the repository properties.

A repository property specifies the characteristics/attributes of Fivetran HVR repository. In the Command Line interface (CLI), the repository properties can be set using the command [**hvrreposconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrreposconfig).

> **Note:** 
A property that is automatically discovered by HVR when it connects to a database/location is called discovered property. A user cannot specify/input value into a discovered property.

An array property and map property can store multiple values. The syntax for updating them from the [Command Line Interface (CLI)](https://fivetran.com/docs/hvr6/command-line-interface/managing-properties-in-cli) varies.


---

### Access_List


<strong>Deprecated in</strong> v6.1.5/2

**Argument:** *access*

**Description:** Enables you to control what tasks a user can perform or access on HVR repository, in some cases user may need administrative rights to perform some tasks or to use some features.

Following are the *access* types available:

- **SysAdmin**: User has full access to all hubs in the repository.
- **HubCreation**: User can create hub.
- **ReadMetering**: Extract Monthly Active Rows (MAR) consumption/metered usage data of the HVR Hub System.


This is an array property that can store multiple values.

---

### Account_Id


<strong>Since</strong> v6.1.0/3

**Argument:** *id*

**Description:** ID of the Fivetran account that was used to register the hub system. This is auto generated when registering a hub system with a Fivetran account.

> **Important:** 
This property is applicable only for the hub system that is registered with the Fivetran account for Consumption-Based Pricing.


---

### Account_Name


<strong>Since</strong> v6.1.0/3

**Description:** This is a discovered property that stores the name of the Fivetran account that was used to register the hub system.

> **Important:** 
This property is applicable only for the hub system that is registered with the Fivetran account for Consumption-Based Pricing.


---

### Agent_Client_Private_Key


**Argument:** *base64*

**Description:** Private key for the HVR Hub System when connecting to an HVR Agent.

---

### Agent_Client_Private_Key_Password


**Argument:** *password*

**Description:** Password for the **Agent_Client_Private_Key**.

---

### Agent_Client_Public_Certificate


**Argument:** *base64*

**Description:** Public certificate for the HVR Hub System when connecting to an HVR Agent.

---

### All_User_Access


<strong>Since</strong> v6.1.5/2

**Argument:** *accesslevel*

**Description:** Enables you to control what tasks all users can perform or access on HVR repository.

The following *access levels* are supported:

- **sysadmin**: User has full access to all hubs in the repository.
- **hubcreator**: User can create hub.
- **readmetering**: Extract Monthly Active Rows (MAR) consumption/metered usage data of the HVR Hub System.


Example JSON:
All_User_Access={"hubcreator": true}

This is a map property that can store multiple values.

---

### Hub_Server_Login_Expiration


**Argument:** *secs*

**Description:** Time duration in seconds (*secs*) after which the HVR login session expires. A login session may end when, for example, an authentication token expires due to a password reset.

The default session expiration time is **604800** seconds (1 week).

---

### Hub_Switch_Bookmarks


**Argument:** *urldesc*

**Description:** This property stores the URL and Description for a bookmark. A bookmark is a shortcut created for easily accessing (frequently accessed) another hub or webpage.

This is an array property that can store multiple values.

Related topics - [Manage Hub Bookmarks in UI](https://fivetran.com/docs/hvr6/user-interface/system/current-hub#managehubbookmarks), [Manage Hub Bookmarks in CLI](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrreposconfig#examples).

---

### Licenses


**Argument:** *license*

**Description:** Details of the HVR license registered/added for the hub system.

This is a map property that can store multiple values.

---

### Metering_License_Acquire_State


<strong>Since</strong> v6.1.0/3

**Argument:** *state*

**Description:** Result of the last time a license was attempted to be acquired.

> **Important:** 
This property is applicable only for the hub system that is registered with the Fivetran account for Consumption-Based Pricing.


This is a map property that can store multiple values.

---

### Metering_Purge_Frequency


<strong>Since</strong> v6.1.0/3

**Description:** Frequency of purging the Monthly Active Rows (MAR) data.

By default, no value is set for this property, which means:

- If you are using Consumption-Based Pricing (CBP), purge all MAR data that is older than one day after it is uploaded.
- If you are using a Subscription-based license, purge all MAR data after 30 days.


If value **0** is set, disable purging; MAR data is never purged.

---

### Metering_Upload_State


<strong>Since</strong> v6.1.0/3

**Argument:** *state*

**Description:** Result of the last time metering/MAR data or usage snapshots were uploaded to Fivetran.

> **Important:** 
This property is applicable only for the hub system that is registered with the Fivetran account for Consumption-Based Pricing.


This is a map property that can store multiple values.

---

### PAM_Service


**Argument:** *service*

**Description:** Name of the PAM service used for authenticating the repository users with PAM authentication. The default is **login** service.

---

### PAM_Sudo_User


**Argument:** *user*

**Description:** If this property is set, then **sudo** is used to elevate privileges to verify the repository users with PAM authentication.

This user must be able to run the following command:
$ sudo -n -u <em>PAM_Sudo_User</em> -- $HVR_HOME/lib/hvrauthpam <em>PAM_Service</em>

---

### Registration_Access_Key


<strong>Since</strong> v6.1.0/3

**Argument:** *key*

**Description:** Access key of the Fivetran registration ID (**Registration_Id**). This is auto generated when registering a hub system with a Fivetran account.

> **Important:** 
This property is applicable only for the hub system that is registered with the Fivetran account for Consumption-Based Pricing.


---

### Registration_Id


<strong>Since</strong> v6.1.0/3

**Argument:** *id*

**Description:** ID of the hub system's registration with the Fivetran account. This is auto generated when registering a hub system with a Fivetran account.

> **Important:** 
This property is applicable only for the hub system that is registered with the Fivetran account for Consumption-Based Pricing.


---

### User_Access


<strong>Since</strong> v6.1.5/2

**Argument:** *accesslevel*

**Description:** Enables you to control what tasks different users can perform or access on HVR repository, per user.

The following access levels are supported:

- **sysadmin**: User has full access to all hubs in the repository.
- **hubcreator**: User can create hub.
- **readmetering**: Extract Monthly Active Rows (MAR) consumption/metered usage data of the HVR Hub System.
- **viewfulluserlist**: Allows a user to view the list of all users and their permissions for any hub in the repository (available since 6.2.0/35, 6.3.0/5, and 6.3.5/1). By default, only the **hubowner** for the hub and the repository **sysadmin** can view this information.


Example JSON:
User_Access={"user1":{"sysadmin":true},"user2":{"readmetering":true}}

This is a map property that can store multiple values.

---

### User_Auto_Create


<strong>Since</strong> v6.2.5/3

**Argument:** *authenticationmethod*

**Description:** Enables automatic addition of users to the HVR Hub System upon successful login using a specified external *authentication method*, if the user does not already exist in the HVR Hub System. For more information, see the [User Provisioning](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/user-provisioning) section.

Valid values for *authenticationmethod* are:

- **pam**: Authenticates the user using the username and password of a user available in the Pluggable Authentication Module (PAM).
- **plugin**: Authenticates the user using a custom authentication plugin.
- **saml**: Authenticates the user using a third-party identity provider using SAML 2.0. To use this authentication method, you must [**configure SSO for the HVR Hub**](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/configuring-sso-for-hvr-hub).
- **windows**: Authenticates the user using a username and password of the Windows user available in the Active Directory (AD).


For more information about these authentication methods, see the [User Authentication](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/user-authentication) section.

---

### Wallet


**Description:** Stores the current wallet configuration in JSON format.

> **Note:** 
This property is automatically defined by HVR and cannot be manually configured by a user.


.actparam {
    padding-left: 20px;
}
