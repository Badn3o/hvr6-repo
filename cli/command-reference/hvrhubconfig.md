# hvrhubconfig - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubconfig

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvrhubconfig/index.md)

# hvrhubconfig


## Usage


- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] List all the hubs on the hub server.
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] <em>hub</em> List the [hub properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties) of the *hub*.
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] [<b>-o</b><em>jsonfile</em>] <em>hub</em> [<em>properties</em>]... Print the specified [hub properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties) (*property...*), or all if none are specified.
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] [<b>-i</b><em>jsonfile</em>] <em>hub</em> [<em>property</em>=[<em>value</em>]]... Set or unset the specific [hub properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties) supplied in the *jsonfile* and/or directly on the command line.
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] <b>-a</b> [<b>-i</b><em>jsonfile</em>] <em>hub</em> [<em>property</em>=<em>value</em>]... Replace all the existing [properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties) of the *hub* with a new set of properties supplied in the *jsonfile* and/or directly set on the command line (*property=value...*).
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] <b>-c</b> [<b>-i</b><em>jsonfile</em>] <em>hub</em> [<em>property</em>=[<em>value</em>]]... Create a *hub* with the specified [properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties) in the *jsonfile* and/or the properties specified in the command line (*property=*[*value*]*...*).
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] <b>-d</b> <em>hub</em> Drop the *hub*.
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] <b>-f</b> <em>hub</em> Freeze the *hub*.
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] <b>-u</b> <em>hub</em> Unfreeze the *hub*.
- <b>hvrhubconfig</b> [<b>-R</b><em>url</em>] <b>-A</b><em>type</em>[:<em>name</em>]=[<em>access</em>]... <em>hub</em> Add or delete **[Access_List](https://fivetran.com/docs/hvr6/property-reference/hub-properties)** property to the *hub* (`**Deprecated in** v6.1.5/2`).


## Description


Command **hvrhubconfig** allows you to create and drop a hub, as well as configure [hub properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties). If this command is executed without supplying any of the options, it will list all the hubs available on a hub server.

Argument <em>properties</em> or <em>property</em> specifies the properties that define the hub configuration. For more information, see section [Hub Properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties).

## Options


This section describes the options available for command **hvrhubconfig**.

 Parameter | Description |
 `**-A***type[:name]=[access]*` | 
> **Important:** 
`**Deprecated in** v6.1.5/2`. Use **[User_Access](https://fivetran.com/docs/hvr6/property-reference/hub-properties#useraccess)** and/or **[All_User_Access](https://fivetran.com/docs/hvr6/property-reference/hub-properties#alluseraccess)** hub properties instead.


Add or delete **[Access_List](https://fivetran.com/docs/hvr6/property-reference/hub-properties)** property entry.

- Value `*type*` can be **all** or **user**. If value `type` is **all**, then `*name*` is omitted.
- Value `*access*` can be **HubOwner**, **ReadWrite**, **ReadExecRefresh**, **ReadExec**, **ReadOnly**.


> **Important:** 
Omitting *access* causes all matching access elements to be removed/unset.


The following command will add or update the permissions for user **hvruser** to be **HubOwner** on hub **myhub**:
`hvrhubconfig -A user:hvruser=HubOwner myhub`
The following command will remove all permissions explicitly set for user **hvruser** on the hub level:
`hvrhubconfig -A user:hvruser= myhub` |
 `**-a**` | 
Replace (delete) all the existing [hub properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties) with a new set of properties. The new set of properties may be supplied directly in the command line ([*property*=[*value*]]...) and/or from file *jsonfile* using parameter **`-i`**.

The following syntaxes are applicable:

- 
Replace the properties of the current hub with the properties supplied in *jsonfile*.
`hvrhubconfig -a -i *jsonfile**hub*`
- 
Replace the current hub properties**** with the properties supplied on the command line.
`hvrhubconfig -a *hub**property1=value1**property2=value2**property3=value3...*`
- 
Replace the current hub properties with the properties supplied in *jsonfile* and on the command line.
`hvrhubconfig -a -i *jsonfile**hub**property1=value1 property2=value2 property3=value3...*`
> **Important:** 
The properties supplied directly on the command line will override the relevant properties in *jsonfile*.




For specific examples, see [Replace hub properties](#replacehubproperties). |
 `**-c**` | 
Create a hub. Before creating a hub, you must stop the hub server using command **[hvrhubserver](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserver)**`**-k**`.

For example, the following command will create hub **myhub**:
`hvrhubconfig -c myhub`
You can also create a new hub **myhub** using a JSON file **hub_props.json**:
`hvrhubconfig -i hub_props.json -c myhub` |
 `**-d**` | 
Delete a hub.

Deleting a hub will delete everything associated with that hub. That includes all definition objects, jobs, events, statistics data, files on the disk (**$HVR_CONFIG/hubs/***hub*/ is removed). The hub will be frozen automatically before it is deleted. Deactivating a channel(s) is not required. Exporting hub definition is a good optional step for backup.

For example, the following command will drop hub **myhub**:
`hvrhubconfig -d myhub` |
 `**-E***x*` | 
Override automatic encoding/decoding of string properties when reading a property from file using `*property=@file_name*` or when writing a property to file using `*property>@file_name*`. This option may be required only while setting the [property](https://fivetran.com/docs/hvr6/property-reference) whose argument is **base64**.

When this option is not used, the `default` encoding is **base64**.

Valid values of `*x*` are:

- **none**: no encoding/decoding will be applied.
- **base64**: encode a property in the base64 format.

 |
 `**-f**` | 
Freeze a hub.

When you freeze a hub, the hub's [scheduler](https://fivetran.com/docs/hvr6/getting-started/concepts/scheduler) and all running jobs are stopped. In a frozen hub, you cannot run any jobs such as [compare](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data), [refresh](https://fivetran.com/docs/hvr6/user-interface/channels/refreshing-data), [activate](https://fivetran.com/docs/hvr6/user-interface/channels/activating-replication), [deactivate](https://fivetran.com/docs/hvr6/user-interface/channels/deactivating-replication).

You can freeze a hub when you no longer need it. The main benefit of freezing a hub is to stop resource consumption on the [hub server](https://fivetran.com/docs/hvr6/user-interface/system/hub-server) while saving the state, history, and configuration of the hub. |
 `**-i***jsonfile*` | 
Read property values from JSON file `*jsonfile*`.

For example, the following command will replace all the existing properties of hub **myhub** with the new properties supplied in the **hub_props.json** file:
`hvrhubconfig -a -i hub_props.json myhub` |
 `**-o***jsonfile*` | 
Write properties to JSON file `*jsonfile*`. If no properties are specified on the command line, then all properties are fetched from the repository.

For example, the following command will create the **hub_props.json** file with the current hub properties:
`hvrhubconfig -o hub_props.json *myhub*` |
 `**-R***url*` | 
Remote hub server. Access the hub server running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

This option is required for [remote CLI access](https://fivetran.com/docs/hvr6/command-line-interface). When using this option, command **[hvrlogin](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)** should be run first, for authentication.

For example, the following command will create hub **myhub** on a remote hub server:
`hvrhubconfig -R http://*node*:*port* -c myhub` |
 `**-u**` | 
Unfreeze a hub.

When you unfreeze a hub, the jobs will return to the state they were at the moment of freezing. It is important to note that if the hub is frozen for an extended period of time, a capture job(s) may not be able to resume from the moment the hub is frozen since the log files were most likely cleared up a while ago.
 |


## Examples


This section provides an example of using the **hvrhubconfig** command.

##### Example 1. Get hub properties


The following command prints the value of property **Hub_Server_URL** of hub **myhub**.
hvrhubconfig myhub Hub_Server_URL

##### Example 2. Set hub properties


The following command sets property **Hub_State** to value **FROZEN** for hub **myhub**.
hvrhubconfig myhub Hub_State=FROZEN

##### Example 3. Unset hub properties


The following command unsets property **Description** of hub **myhub**.
hvrhubconfig myhub Description=

##### Example 4. Replace hub properties 


- 
The following command replaces the current properties of hub **myhub** with the properties supplied in the **hub_props.json** file.
hvrhubconfig -a -i hub_props.json myhub

- 
The following command replaces the current properties of hub **myhub** with the properties supplied in the **hub_props.json** file and property **Description**.
hvrhubconfig -a -i hub_props.json myhub Description=My_old_hub

> **Important:** 
The properties supplied directly on the command line will override the relevant properties in the **hub_props.json** file.




  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
