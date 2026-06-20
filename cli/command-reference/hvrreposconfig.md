# hvrreposconfig - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrreposconfig

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvrreposconfig/index.md)

# hvrreposconfig


## Usage


- <b>hvrreposconfig</b> [<b>-R</b><em>url</em>] [<b>-o</b><em>jsonfile</em>] [<em>property</em>]... Print specific [repository properties](https://fivetran.com/docs/hvr6/property-reference/repository-properties) (*property...*), or all if none are specified.
- <b>hvrreposconfig</b> [<b>-R</b><em>url</em>] [<b>-i</b><em>jsonfile</em>] [<em>property</em>=[<em>value</em>]]... Set or unset the specific repository properties supplied in the *jsonfile* and/or directly on the command line.
- <b>hvrreposconfig</b> [<b>-R</b><em>url</em>] <b>-a</b> [<b>-i</b><em>jsonfile</em>] [<em>property=</em><em>value</em>]... Replace all the existing repository properties with a new set of properties supplied in the *jsonfile* and/or directly set on the command line (*property=value...*).
- <b>hvrreposconfig</b> [<b>-R</b><em>url</em>] <b>-c</b> Create repository tables in the repository database.
- <b>hvrreposconfig</b> [<b>-R</b><em>url</em>] <b>-d</b> Drop all repository tables from the repository database.
- <b>hvrreposconfig</b> [<b>-R</b><em>url</em>] <b>-A</b><em>type</em>[:<em>name</em>]=[<em>access</em>] Add or delete [repository-level access permissions](https://fivetran.com/docs/hvr6/property-reference/repository-properties) to a user(s) (`**Deprecated in** v6.1.5/2`).


## Description


Command **hvrreposconfig** allows you to create and drop [repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables) and a hub database, as well as manage the properties of a repository database. If this command is executed without supplying any of the *options*, it will list all the repository properties.

Argument *properties* specifies the properties that define the configuration of a repository database. For more information, see section [Repository Properties](https://fivetran.com/docs/hvr6/property-reference/repository-properties).

## Options


This section describes the options available for command **hvrreposconfig**.

 Parameter | Description |
 `**-A***type[:name]=[access]*` | 
> **Important:** 
`**Deprecated in** v6.1.5/2`. Use **[User_Access](https://fivetran.com/docs/hvr6/property-reference/repository-properties#useraccess)** and/or **[All_User_Access](https://fivetran.com/docs/hvr6/property-reference/repository-properties#alluseraccess)** repository properties instead.


Add or delete **[Access_List](https://fivetran.com/docs/hvr6/property-reference/repository-properties#accesslist)** property entry.

- Value *type* can be **all**, **role**, or **user**. If value *type* is **all**, then name is omitted.
- Value *access* can be **SysAdmin** or **HubCreation**.

Omitting *access* causes all matching access elements to be removed.


For example, the following command will add or update the permissions for the user **hvruser**:
`hvrreposconfig -A user:hvruser=SysAdmin`
The following command will remove all permissions set for user **hvruser **** on the repository level:
`hvrreposconfig -A user:hvruser=` |
 `**-a**` | 
Replace (delete) all the existing repository properties with a new set of properties. The new set of properties may be supplied directly in the command line ([*property*=[*value*]]...) or from file *jsonfile* using parameter `**-i**`.

The following syntaxes are applicable:

- 
The following command replaces the current repository properties with the properties supplied in *jsonfile*.
`hvrreposconfig -a -i *jsonfile*`
- 
The following command will replace all the existing properties with the new properties supplied in the command line.
`hvrreposconfig -a *property1=value1 property2=value2 property3=value3*`
- 
The following command replaces the current repository properties with the properties supplied in *jsonfile* and on the command line.

`hvrreposconfig -a -i *jsonfile property1=value1 property2=value2 property3=value3*`
> **Important:** 
The properties supplied directly on the command line will override the relevant properties in *jsonfile*.




For specific examples, see [Replace repository properties](#examplereplacerepositoryproperties). |
 `**-c**` | 
Create all repository tables in a repository database.

For example, the following command will create repository tables:
`hvrreposconfig -c` |
 
`**-d**`
 | 
Drop all repository tables from a repository database. Executing this command removes all locations, channels (including table groups and tables), and all actions defined on the channel or location. It is recommended to backup the tables (using [**hvrdefinitionexport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionexport)) before executing this command.

For example, the following command will drop all repository tables:
`hvrreposconfig -d` |
 `**-E***x*` | 
Override automatic encoding/decoding of string properties when reading a property from file using `*property=@file_name*` or when writing a property to file using `*property>@file_name*`. This option may be required only while setting the [property](https://fivetran.com/docs/hvr6/property-reference) whose argument is **base64**.

When this option is not used, the `default` encoding is **base64**.

Valid values of `*x*` are:

- **none**: no encoding/decoding will be applied.
- **base64**: encode a property in the base64 format.

 |
 `**-i***jsonfile*` | 
Read the values of repository properties from JSON file *jsonfile*.

For example, the following command will replace all the existing repository properties with the new properties supplied in *repos_props.json*:
`hvrreposconfig -a -i repos_props.json` |
 `**-o***jsonfile*` | 
Write properties to JSON file *jsonfile*. If no properties are specified on the command line, then all properties are fetched from the repository.

For example, the following command will create JSON file **repos_props.json** with the existing repository properties:
`hvrreposconfig -o repos_props.json ` |
 
`**-R***url*`
 | 
Remote hub server. Access the hub server running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

This option is required for [remote CLI access](https://fivetran.com/docs/hvr6/command-line-interface). When using this option, command **[hvrlogin](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)** should be run first, for authentication.

For example, the following command will list the repository properties of the hub server supplied:
`hvrreposconfig -R https://node:port` |
 `**-V***accessmeth*` | 
Handle [classified](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/classification-of-data) data.

- 
**redact**: Redact classified data.

- 
**storage `default`**: Save classified data as they are stored in the hub system.

- 
**@***outputfile*: Apply transport encryption, save key to file *outputfile*.

- 
**@print**: Apply transport encryption using the transport encryption key and display the key in command terminal.

- 
@*inputfile*: Read transport encryption key stored in a *inputfile*. This can also be a path (relative or absolute) to this file.

- 
**@prompt**: Prompt a user to enter the transport key via keyboard.


 |


## Examples


This section provides examples of using the **hvrreposconfig** command.

##### Example 1. Get repository properties


The following command prints the value of property [**Access_List**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#accesslist), which is containing access privileges.
hvrreposconfig Access_List

Since 6.1.5/2, the [**User_Access**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#useraccess) and [**All_User_Access**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#alluseraccess) should be used.
hvrreposconfig User_Access All_User_Access

##### Example 2. Set repository properties


The following command sets property [**Access_List**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#accesslist), namely, it assigns the **SysAdmin** access privilege to users **hvruser1** and **hvruser2**.
hvrreposconfig Access_List[0].user=hvruser1 Access_List[0].level=SysAdmin Access_List[1].user=hvruser2 Access_List[1].level=SysAdmin

Since 6.1.5/2, the [**User_Access**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#useraccess) property should be used.
hvrreposconfig User_Access.hvruser1.sysadmin=true User_Access.hvruser2.sysadmin=true

> **Important:** 
The property [**Access_List**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#accesslist) is an array, hence it is required to specify the array position in square brackets **[***number***]** while setting this property.


##### Example 3. Unset repository properties


The following command unsets property [**Access_List**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#accesslist), which is containing access privileges.
hvrreposconfig Access_List=

Since 6.1.5/2, the [**User_Access**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#useraccess) and [**All_User_Access**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#alluseraccess) should be used.
hvrreposconfig User_Access= All_User_Access=

##### Example 4. Replace repository properties 


- 
The following command replaces the current repository properties with the properties supplied in the **repos_props.json** file.
hvrreposconfig -a -i repos_props.json

- 
The following command replaces the current repository properties with the properties supplied in the **repos_props.json** file and property [**Licenses**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#licenses).
hvrreposconfig -a -i repos_props.json Licenses=<em>licenses</em>

> **Important:** 
The properties supplied directly on the command line will override the relevant properties in the **repos_props.json** file.




##### Example 5. Create hub bookmarks


The following command creates a hub bookmark.
hvrreposconfig Hub_Switch_Bookmarks='[{"url":"https://myserver:4341/#/hubs/myprodhub/","description":"Production Hub"}]'
hvrreposconfig Hub_Switch_Bookmarks="[{"url":"https://myserver:4341/#/hubs/myprodhub/","description":"Production Hub"}]"

  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
