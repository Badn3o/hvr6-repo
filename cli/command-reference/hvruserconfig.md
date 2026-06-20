# hvruserconfig - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvruserconfig/index.md)

# hvruserconfig


## Usage


- <b>hvruserconfig</b> [<b>-R</b><em>url</em>] List all the users in the repository database.
- <b>hvruserconfig</b> [<b>-R</b><em>url</em>] <em>user</em> List the [user properties](https://fivetran.com/docs/hvr6/property-reference/user-properties) of the *user*.
- <b>hvruserconfig</b> [<b>-R</b><em>url</em>] [<b>-o</b><em>jsonfile</em>] [<b>-h</b><em>hub</em>] <em>user</em> [<em>property</em>]... Print the specified property(ies) (*property...*), ** or all if none are specified.
- <b>hvruserconfig</b> [<b>-R</b><em>url</em>] [<b>-i</b><em>jsonfile</em>] [<b>-h</b><em>hub</em>] <em>user</em> [<em>property</em>=[<em>value</em>]]<em>...</em> Set or unset the specific user properties supplied in the *jsonfile* or directly on the command line.
- <b>hvruserconfig</b> [<b>-R</b><em>url</em>] <b>-a</b> [<b>-i</b><em>jsonfile</em>] [<b>-h</b><em>hub</em>] <em>user</em> [<em>property</em>=<em>value</em>]... Replace all the existing user properties with a new set of properties supplied in the *jsonfile* or set directly on the command line (*property=value...*).
- <b>hvruserconfig</b> [<b>-R</b><em>url</em>] <b>-c</b> [<b>-A</b><em>auth</em>] <em>user</em> [<em>property=</em>[<em>value</em>]]... Create a *user* with the local authentication method and the specified user properties (*property=value...*).
- <b>hvruserconfig</b> [<b>-R</b><em>url</em>] <b>-d</b> <em>user</em> Delete the *user*.
- <b>hvruserconfig</b> [<b>-R</b><em>url</em>] <b>-r</b> <em>user</em> Reset the password of the repository-authenticated (local) *user*.


## Description


Command **hvruserconfig** allows you to configure the hub user properties. Argument *property* specifies the configuration properties of a hub user. For more information, see section [User Properties](https://fivetran.com/docs/hvr6/property-reference/user-properties).

## Options


This section describes the options available for command **hvruserconfig**.

 Parameter | Description |
 
`**-A***auth*`
 | 
Set an authentication method for the hub user.

Valid values for `*auth*` are:

- **local**: The user is authenticated using the username and password of a local user. In this authentication method, the user account is created locally in the HVR Hub System and stores it in the repository database of the hub server.
- 
**pam**: The user is authenticated using the username and password of a user available in the Pluggable Authentication Module (PAM). To use this authentication method, PAM must be already configured in the user machine/network. In this authentication method, the PAM authentication service is used to authenticate a user on Linux and Unix systems. PAM is a login/password authentication service used to validate user credentials on Linux and Unix systems as an alternative to regular username/password authentication, e.g. checking the **/etc/passwd** file.

The `default` PAM authentication service used is **login**. To use a different PAM service, you must set the repository property [**PAM_Service**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#pamservice) using the command **[hvrreposconfig](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrreposconfig)**.


> **Important:** 
This authentication method is applicable only for authenticating the hub user on Linux system.


- 
**plugin**: The user is authenticated using a custom authentication plugin.

You can supply your own plugin for authenticating users. The custom plugin file must be named as **hvrauth** and saved in the **HVR_CONFIG/plugin/authentication/** directory. An example of the custom authentication plugin can be found in the **HVR_HOME/plugin_examples/authentication/** directory.

> **Important:** 
The plugin must follow the simple call conventions:

- It should read a two-line input that contains a username and password.
- It should exit with code 0 if the username and password are valid. Otherwise, it should exit with code 1.



- 
**windows**
`Windows`
The user is authenticated using a username and password of the Windows user available in the Active Directory (AD). In this authentication method, a Windows user account is used for authentication.


> **Important:** 
This authentication method is applicable only for authenticating the hub user on Windows system.


- **saml**`**Since** v6.2.5/2`: The user is authenticated by a third-party identity provider using SAML 2.0. 
.
To use this authentication method, you must [configure SSO for the HVR Hub](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/configuring-sso-for-hvr-hub).


This option must be used in combination with option `**-c**`.


For example, the following command creates new user **myuser** with the **windows** authentication:
`hvruserconfig -c -A windows myuser` |
 
`**-a**`
 | 
Replace (delete) all the existing user properties with a new set of user properties. The new set of user properties may be supplied directly in the command line ([*property*=[*value*]]...) and/or from a JSON file *jsonfile* using parameter **`-i`**.

The following syntaxes are applicable:

- 
The following command replaces the current user properties with the properties supplied in *jsonfile*.
`hvruserconfig -a -i *jsonfile user*`
- 
The following command replaces the current user properties with the properties supplied on the command line.
`hvruserconfig -a *user property=value1 property=value2 property=value3*`
- 
The following command replaces the current user properties with the properties supplied in the *jsonfile* and on the command line.
`hvruserconfig -a -i *jsonfile property1=value1 property2=value2 property3=value3*`
> **Important:** 
The properties supplied directly on the command line will override the relevant properties in *jsonfile*.




For specific examples, see [Replace user properties](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig). |
 
`**-c**`
 | 
Create a hub user.

To set the [authentication method](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/user-authentication), this option must be used in combination with option `**-A**`. If option `**-A**` is not supplied, the user will be created with the **local** authentication method.

User will be prompted for a password if the authentication method is **local**.

For example, the following command creates a new user **myuser** (with **local** authentication):
`hvruserconfig -c myuser`
You can also create a new user using a JSON file **user_props.json**:
`hvruserconfig -i user_props.json -c myuser` |
 
**`-d`**
 | 
Delete a hub user.

For example, the following command deletes user **myuser**:
`hvruserconfig -d myuser` |
 
`**-E***x*`
 | 
Override automatic encoding/decoding of string properties when reading a property from file using `*property=@file_name*` or when writing a property to file using `*property>@file_name*`. This option may be required only while setting the [property](https://fivetran.com/docs/hvr6/property-reference) whose argument is **base64**.

When this option is not used, the `default` encoding is **base64**.

Valid values of `*x*` are:

- **none**: no encoding/decoding will be applied.
- **base64**: encode a property in the base64 format.

 |
 
`**-h***hub*`
 | 
Hub name *hub* for configuring hub user properties, not general user properties (for all hubs).

For example, the following command replaces the current [user properties](https://fivetran.com/docs/hvr6/property-reference/user-properties) of user **myuser** on hub **hvr6_hub** with a new user property **Latency_Manual_Limit**:
`hvruserconfig -a -h hvr6_hub myuser Latency_Manual_Limit=10` |
 
`**-i***jsonfile*`
 | 
Read property values from JSON file *jsonfile*.

For example, the following command replaces all the existing properties of user **myuser** with the new properties supplied in file **user_props.json**:
`hvruserconfig -a -i user_props.json myuser` |
 
`**-o***jsonfile*`
 | 
Write properties to JSON file *jsonfile*. If no properties are specified on the command line, then all properties are fetched from a repository.

For example, the following command creates a JSON file **user_props.json** with the existing user properties of user **myuser**:
`hvruserconfig -o user_props.json myuser` |
 
`**-P**`
 | 
Prompt for the current password of the hub user. For example, the following command prompts for the current password for the user **myuser**:
`hvruserconfig -P myuser`
This option must be used in combination with option `**-r**`. |
 
`**-R***url*`
 | 
Remote hub server. Access the hub server running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

This option is required for [remote CLI access](https://fivetran.com/docs/hvr6/command-line-interface). When using this option, command **[hvrlogin](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)** should be run first, for authentication.

For example, the following command creates a new user named **myuser1** on a remote hub server:
`hvruserconfig -R http://node:port -c myuser1` |
 
`**-r**`
 | 
Reset the password of a hub user. This option is applicable only for a user whose authentication method is set to **Local**.

For example, the following command resets the password of user **myuser**:
`hvruserconfig -r myuser` |


## Examples


This section provides examples of using the **hvruserconfig** command.

##### Example 1. Get user properties


The following command prints the values of properties **Topology_Animation** and **Topology_Preferences** of **hvruser**.
hvruserconfig hvruser Topology_Animation Topology_Preferences

##### Example 2. Set user properties


- 
The following command sets property **Latency_Manual_Limit** to value **10** for **hvruser**. This will override the current value of property **Latency_Manual_Limit** (if set) with value **10**.
hvruserconfig hvruser Latency_Manual_Limit=10

- 
The following command sets the properties specified in the **user_props.json** file for **hvruser**.
hvruserconfig hvruser -i user_props.json

- 
The following command sets properties specified in the **user_props.json** file as well as the properties specified on the command line for **hvruser**.
hvruserconfig hvruser -i user_props.json hvruser Num_Events_Initially=50

> **Important:** 
If the **user_props.json** file contains properties that are already set for the user, option <b>-i</b> will override these properties.

For example, the following properties are currently set: **Full_Name**, **Show_Internal_Jobs**, and **Num_Events_Initially**. The **user_props.json** file contains properties **Full_Name** and **Show_Internal_Jobs**. Option <b>-i</b> will override the current values of properties **Full_Name** and **Show_Internal_Jobs**.




##### Example 3. Unset user properties


The following command unsets property **Topology_Animation** of **hvruser**.
hvruserconfig hvruser Topology_Animation=

##### Example 4. Replace user properties 


- 
The following command replaces the current properties of **hvruser** with the properties supplied in the **user_props.json** file.
hvruserconfig -a -i user_props.json hvruser

- 
The following command replaces the current properties of **hvruser** with the [**Latency_Manual_Limit**](https://fivetran.com/docs/hvr6/property-reference/user-properties#latencymanuallimit), [**Full_Name**](https://fivetran.com/docs/hvr6/property-reference/user-properties#fullname), [**Show_Inactive_Jobs**](https://fivetran.com/docs/hvr6/property-reference/user-properties#showinactivejobs), and [**Topology_Animation**](https://fivetran.com/docs/hvr6/property-reference/user-properties#topologyanimation) properties.
hvruserconfig -a hvruser Full_Name="HVR User" Show_Inactive_Jobs=true Topology_Animation=true

- 
The following command replaces the current properties of **hvruser** with the properties supplied in the **user_props.json** file and the [**Show_Inactive_Jobs**](https://fivetran.com/docs/hvr6/property-reference/user-properties#showinactivejobs) property.
hvruserconfig -a -i user_props.json hvruser Show_Inactive_Jobs=false

> **Important:** 
The properties supplied directly on the command line will override the relevant properties in the **user_props.json** file.




##### Example 5. Show deprecated features


The following command displays deprecated options in the user interface, such as the **Database Triggers** capture method (on **Step 4. Configure Capture/Integrate** of the [location creation](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) workflow).
hvruserconfig myuser Show_Deprecated_Features=true

  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
