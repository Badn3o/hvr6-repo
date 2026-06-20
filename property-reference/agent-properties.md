# Agent Properties - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/property-reference/agent-properties

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/property-reference/agent-properties/index.md)

# Agent Properties


An agent property specifies the characteristics/attributes of an HVR Agent. This can include agent connection parameters, user access levels, authentication mode, etc. In the Command Line interface (CLI), the repository properties can be set using the command [**hvragentconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig).

> **Note:** 
An array property and map property can store multiple values. The syntax for updating them from the [Command Line Interface (CLI)](https://fivetran.com/docs/hvr6/command-line-interface/managing-properties-in-cli) varies.


---

### Agent_Server_Kerberos_Keytab


**Argument:** *keytabfile*

**Description:** Full path to the user specified Kerberos keytab file that contains a security key for identifying the agent to the hub during authentication (when connecting hub to the agent). If defined, this keytab file will be used instead of the operating system defaults.

---

### Agent_Server_Kerberos_Principal


**Argument:** *principal*

**Description:** User specified Kerberos principal name for identifying the agent to the hub during authentication (when connecting hub to the agent). If defined, this principal name will be used instead of the operating system defaults.

---

### Agent_Server_Private_Key


**Argument:** *base64*

**Description:** Private key for the HVR Agent.

This property is generated when agent starts for the first time.

---

### Agent_Server_Private_Key_Password


**Argument:** *password*

**Description:** Password for the **Agent_Server_Private_Key**

---

### Agent_Server_Public_Certificate


**Argument:** *base64*

**Description:** Public certificate for the HVR Agent.

This property is generated when agent starts for the first time.

See also, [**Agent_Server_Public_Certificate**](https://fivetran.com/docs/hvr6/property-reference/location-properties#agentserverpubliccertificate) in location properties.

---

### All_User_Access


**Argument:** *accesslevel*

**Description:** Enables you to set the HVR Agent administration permissions for all agent users configuring the agent. This property supports only the following access level:

- **AgentAdmin**: An agent user with this permission level can only [configure the agent service](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser) from HVR UI or using remote CLI.


Example JSON:
{"level":"AgentAdmin"}

This is a map property that can store multiple values.

---

### Anonymous_Access


**Argument:** true

**Description:** Anonymous access to HVR Agent. If set to **true**, the HVR Hub System can connect anonymously to HVR Agent without supplying a username and password. This requires the agent property [**Only_From_Client_Public_Certificates**](#onlyfromclientpubliccertificates).

Example JSON to enable anonymous access:
{"allow": true}

This is a map property that can store multiple values.

---

### Only_From_Client_Public_Certificates


**Argument:** *base64*

**Description:** The SSL public certificate of the client (HVR Hub System). When this property is set, only the client that has the specified certificate is allowed to connect to the HVR Agent. Note that multiple certificates can be defined, and the incoming connection can use one of them.

This is a map property that can store multiple values.

See also, [**Agent_Client_Public_Certificate**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#agentclientpubliccertificate) in repository property.

---

### PAM_Service


**Argument:** *service*

**Description:** The name of the PAM service used for authenticating the agent users with PAM authentication. This defaults to the **login** service.

---

### PAM_Sudo_User


**Argument:** *username*

**Description:** Name of the user for running the PAM authenticator instead of the operating system user under which the HVR Agent is running.

This user must have privilege to run the following command:
sudo -n -u PAM_Sudo_User -- $HVR_HOME/lib/hvrauthpam PAM_Service

If this property is set then **sudo** is used to elevate privileges to verify the agent users with PAM authentication.

---

### Remote_Keepalive


<strong>Since</strong> v6.1.5/7

**Argument:** *seconds*

**Description:** Set the timeout for HVR protocol keepalive messages between the HVR hub and HVR agent. This helps prevent network devices such as load balancers from terminating idle connections, ensuring continuous communication even when no data is being transferred.

Note that defining this property may introduce a minor performance overhead.

The value specified for this property is in *seconds*. For example, to set a timeout of 2 minutes and 20 seconds, you need to set the value to **140**.

---

### Setup_Mode_Timed_Until


**Argument:** *time*

**Description:** When this property is set, the agent is in setup mode until the *time* specified. This property can be used with the [**Setup_Mode_Token_Value**](#setupmodetokenvalue).

Valid date formats are:

- **now**[**+**|**-**]*NUM***s** - indicates the number of seconds from now
- **now**[**+**|**-**]*NUM***m** - indicates the number of minutes from now
- **now**[**+**|**-**]*NUM***h** - indicates the number of hours from now
- **now**[**+**|**-**]*NUM***d** - indicates the number of days from now
- **now**[**+**|**-**]*NUM***w** - indicates the number of weeks from now
- **today** indicates the current day
- *YYYY-MM-DD*[**T**| ]*HH:MM:SS*[*.MSECS*]*+TZD -* indicates the precise date and time with time zone information
- *YYYY-MM-DD*[*HH:MM:SS*] - indicates the precise date and time without time zone information
- an integer - indicates seconds since 1970-01-01 00:00:00 UTC


Example:
Setup_Mode_Timed_Until=now+1h

---

### Setup_Mode_Token_Name


**Argument:** *tokenname*

**Description:** User friendly name/description of the setup token.

---

### Setup_Mode_Token_Value


**Argument:** *tokenvalue*

**Description:** When this property is set, the agent is in setup mode, and only allows access when the token value is provided. This property can be used with the [**Setup_Mode_Timed_Until**](https://fivetran.com/docs/hvr6/property-reference/agent-properties).

---

### User_Access


**Argument:** *accesslevel*

**Description:** Enables you to set the HVR Agent administration permissions for a specific agent user configuring the agent. This property supports only the following access level:

- **AgentAdmin**: An agent user with this permission level can only [configure the agent service](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser) from UI or using remote CLI.


Example JSON:
User_Access={"user1":{"level":"AgentAdmin"},"user2":{"level":"AgentAdmin"}}

This is a map property that can store multiple values.

.actparam {
    padding-left: 20px;
}
