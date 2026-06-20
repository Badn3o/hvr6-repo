# Migrating Channel from HVR Version 5 to HVR Version 6 - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/migrating-channel-from-hvr-version-5

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/migrating-channel-from-hvr-version-5/index.md)

# Migrating Channel from HVR Version 5


This section describes the steps to migrate channel definitions from HVR 5 to HVR 6 using the **hvrconvert5to6** script. This script is suitable for migrating channel definitions only. It *does not* manage the capture status (e.g., transaction log position) in the HVR 5 channel. Therefore, it is not suited for situations that require replication to resume in HVR 6 from where it was stopped in the HVR 5. For such cases, see section [Upgrading From HVR 5](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/upgrading-from-hvr-5).

You can find the script in the **HVR_HOME/script/** directory of the HVR 6 distribution. It exports one or more HVR 5 channels to an HVR 6 compatible import file (JSON) from either an HVR 5 catalog export file (XML) or HVR 5 hub database. The resulting JSON file is then used to import the channels to the HVR 6 Hub.

The exported channel definition includes:

- Locations
- Location group membership
- Tables
- Actions, including configuration actions


> **Important:** 
- HVR version 5.3 or above is required to run the **hvrconvert5to6** script.
- The **hvrconvert5to6** script must be executed on the HVR 5 system because the HVR 5 command [**hvr**](https://fivetran.com/docs/hvr5/commands/hvr) is used to run the script.



> **Note:** 
- For differences between HVR 5 and HVR 6, see section [Important Notes When Upgrading from HVR 5](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/upgrading-from-hvr-5/important-notes-when-upgrading-from-hvr-5).



## Prerequisites


Ensure the following requirements are met before migrating from HVR 5 to HVR 6:

- 
HVR 6 is already installed and configured.

> **Important:** 
HVR 6 must be installed as a separate system, to a directory other than the HVR 5 **HVR_HOME** and **HVR_CONFIG** directories.


- 
Do not disable/uninstall HVR 5 before ensuring HVR 6 works properly.

- 
Before disabling HVR 5, it is recommended to take a full backup of the following HVR 5 objects:

- the **HVR_HOME** and **HVR_CONFIG** directories.
- the Hub database using the DBMS native backup option.


- 
Perform the migration during scheduled downtime, as all HVR running services ([HVR Agent Listener](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener)) must be stopped during the migration.



## hvrconvert5to6


**NAME**

**hvrconvert5to6** - HVR 5 to HVR 6 channel migration

**USAGE**

<b>hvr hvrconvert5to6</b> <b>-f</b> <em>xmlfile</em> [<b>-c</b> <em>chn</em>]... <em>hub output.json</em> <b>hvr hvrconvert5to6</b> [<b>-c</b> <em>chn</em>]... [<b>-h</b> <em>class</em>] [<b>-u</b> <em>user</em>[<em>/pass</em>]] <em>hub output.json</em>

**DESCRIPTION**

Exports one or more HVR 5 channels to an HVR 6 compatible import file, from either an HVR 5 catalog export file or an HVR 5 hub database.

**OPTIONS**

 Parameter | Description |
 `**-c***chn*` | Channel name |
 `**-f***xmlfile*` | HVR 5 catalog export output file |
 `**-h***class*` | HVR 5 hub class |
 `**-u***user[/pass]*` | Database username and password for relevant hubs |


## Migration Steps


Follow these steps to migrate HVR 5 channels to the HVR 6 Hub:

- 
If the HVR 5 and HVR 6 systems are installed on separate machines, copy the **hvrconvert5to6** script (available in **HVR_CONFIG/script** directory) from HVR 6 to HVR 5 machine.

- 
Export HVR 5 channels to an HVR 6 compatible import file (JSON). There are two ways to do this:

> **Note:** 
The **hvrconvert5to6** script must be run in the HVR 5 system.


- 
**Method 1:** Generate HVR 5 channel export file (XML) and convert it to HVR 6 compatible import file (JSON).

- 
Use the HVR 5 command [**hvrcatalogexport**](https://fivetran.com/docs/hvr5/commands/hvrcatalogcreate-hvrcatalogdrop) or the **Export Catalogs** option in HVR 5 graphical user interface to generate the HVR 5 channel export file (XML).

- 
Run the **hvrconvert5to6** script to convert the HVR 5 channel export file (XML) to HVR 6 compatible import file (JSON):
hvr <em>hvrconvert5to6_script_path</em>/hvrconvert5to6 -f <em>hvr5_export</em>.xml <em>hvr5_hub output</em>.json

To migrate a specific channel (e.g. **mychannel**) only, use option <b>-c</b>:
hvr <em>hvrconvert5to6_script_path</em>/hvrconvert5to6 -c mychannel -f <em>hvr5_export</em>.xml <em>hvr5_hub output</em>.json



- 
**Method 2:** Connect directly to HVR 5 hub database and generate the HVR 6 compatible import file (JSON) using the **hvrconvert5to6** script:
hvr <em>hvrconvert5to6_script_path</em>/script/hvrconvert5to6 -h oracle -u <em>hvruser</em>/<em>password </em><em>hvr5_hub output</em>.json

> **Note:** 
For more information about using option <b>-h</b> for other location types (class), see [Calling HVR on the Command Line](https://fivetran.com/docs/hvr5/commands/calling-hvr-on-the-command-line) (HVR 5).




- 
In the HVR 6 system, use the [**hvrdefinitionimport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionimport) command to import the contents of the JSON file to the HVR 6 Hub.
hvrdefinitionimport <em>hvr6_hub output</em>.json

Alternatively, use the [Import Channel Definition](https://fivetran.com/docs/hvr6/user-interface/channels/importing-and-exporting-channel-definition) option in the HVR 6 [User Interface](https://fivetran.com/docs/hvr6/user-interface).



## See Also


- [Migrating Channel from Pre-Production to Production](https://fivetran.com/docs/hvr6/advanced-operations/migrating-channel-from-pre-production-to-production)

