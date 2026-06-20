# Upgrading from HVR 5 to HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/upgrading-from-hvr-5

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/install-and-upgrade/upgrade/upgrading-from-hvr-5/index.md)

# Upgrading from HVR 5


This section describes the steps to upgrade from HVR 5 to HVR 6 without the need to [Refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) tables. These instructions are suitable for scenarios with active replication in place to ensure that the replication continues seamlessly in the upgraded channel, picking up exactly where it left off in HVR 5.

> **Important:** 
Since HVR 6 is not compatible with HVR versions 5.x and 4.x, you must upgrade both the hub machine and agent machine to version 6.x.


> **Note:** 
- For the differences between HVR 5 and HVR 6, see [Important Notes When Upgrading from HVR 5](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade/upgrading-from-hvr-5/important-notes-when-upgrading-from-hvr-5).
- For steps to migrate only channel definitions from HVR 5 to HVR 6, see section [Migrating Channel from HVR Version 5](https://fivetran.com/docs/hvr6/advanced-operations/migrating-channel-from-hvr-version-5)



## Prerequisites


Consider the following general prerequisites when upgrading from HVR 5 to HVR 6:

- 
Do not disable/uninstall HVR 5 before ensuring HVR 6 works properly.

- 
Before disabling HVR 5, it is recommended to take a full backup of the following HVR 5 objects:

- the **HVR_HOME** and **HVR_CONFIG** directories.
- the HVR hub database using the DBMS native backup option.


- 
Perform the upgrade during scheduled downtime, as all HVR running services ([HVR remote listener](https://fivetran.com/docs/hvr5/commands/hvrremotelistener)) must be stopped during the upgrade.



> **Important:** 
The following step-by-step guide uses Oracle source/target/repository databases as an example to demonstrate the upgrade process. However, if you move the HVR repository to another database vendor during the upgrade, ensure you have already installed the database that will serve as the new HVR repository and created a schema/database/user with the same name as the previous HVR repository prior to performing the upgrade.


## Scripts Used During Upgrade


Upgrading from HVR 5 to HVR 6 includes the step of converting one or more channels from an HVR 5 Hub to HVR 6 Hub using the **hvrconvert5to6** script. The script exports HVR 5 channel(s) from the HVR 5 catalog export XML file or HVR 5 hub database to the HVR 6 compatible import JSON file. The JSON file is then used to import the channels to the HVR 6 Hub.

After the channel(s) are converted, the **hvrconvert5to6activate** script must be used to generate the [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate) and [**hvrcontrol**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcontrol) commands that will activate the HVR 6 channel to capture from the point where the HVR 5 channel stopped. The **hvrconvert5to6activate** script inspects the HVR 5 *.**cap_state** file for capture status (such as the transaction log’s position of the beginning of the oldest open transaction) to generate the correct values for activation of replication in the HVR 6 channel(s).

The scripts come prepackaged with the HVR 6 distribution and can be found in the **HVR_HOME/script/** directory.

> **Important:** 
- HVR version 5.3 or above is required to run the **hvrconvert5to6** and **hvrconvert5to6activate** scripts.
- The **hvrconvert5to6** and **hvrconvert5to6activate** scripts must be executed on the HVR 5 system because the HVR 5 command [**hvr**](https://fivetran.com/docs/hvr5/commands/hvr) is used to run the scripts.



- 
**hvrconvert5to6 **
Click here to see more information about hvrconvert5to6
**NAME**

**hvrconvert5to6** - HVR 5 to HVR 6 channel migration

**USAGE**

<b>hvr hvrconvert5to6</b> <b>-f</b> <em>xmlfile</em> [<b>-c</b> <em>chn</em>]... <em>hub output.json</em>

<b>hvr hvrconvert5to6</b> [<b>-c</b> <em>chn</em>]... [<b>-h</b> <em>class</em>] [<b>-u</b> <em>user</em>] <em>hub output.json</em>

**DESCRIPTION**

Exports one or more HVR 5 channels to a HVR 6 compatible import file, from either an HVR 5 catalog export file, or an HVR 5 hub database.

**OPTIONS**

 Parameter | Description |
 `**-c***chn*` | Channel name. This is to convert a specific channel. |
 `**-f***xmlfile*` | HVR 5 catalog export output file |
 `**-h***class*` | HVR 5 hub class |
 `**-u***user[/pass]*` | Hub database username and password for relevant hubs |


- 
**hvrconvert5to6activate **
Click here to see more information about hvrconvert5to6activate
> **Important:** 
The **hvrconvert5to6activate** script is supported in HVR versions up to 5.7.5.


**NAME**

**hvrconvert5to6activate** - HVR 5 to HVR 6 migration of capture state

**USAGE**
<b>hvr hvrconvert5to6activate</b> [<b>-c</b> <em>chn</em>]... [<b>-r</b>] [<b>-h</b> <em>class</em>] [<b>-u</b> <em>user</em>] <em>hub</em> 

**DESCRIPTION**
Inspects the HVR 5 ***.cap_state** file and generates the [**hvractivate**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate) and [**hvrcontrol**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcontrol) commands to run in the HVR 6 system. This allows for a refresh-less upgrade from HVR 5 to HVR 6.

**OPTIONS**

 Parameter | Description |
 `**-c***chn *` | Channel name. |
 **`-r`** | HVR child process to service remote HVR connections |
 `**-h***class*` | HVR 5 hub class |
 `**-u***user*[/*pass*]` | Database username and password for relevant hubs |




## Notes for Upgrading from HVR 5 to HVR 6


For the following location types certain changes need to be made for operating HVR 6 smoothly. For more information, click on the required location type below:

- [SAP HANA](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements#notesformigratingfromhvr5xto6x)


## Upgrading to HVR 6


The upgrade process includes three main phases:

### Phase 1. Upgrading Test System


This phase involves the steps of upgrading the HVR 5 system running in the test system (equivalent to the HVR 5 system in the production system). In this phase, HVR 6 should be installed and configured to run independently of the HVR 5 system. After completing Phase 1 and ensuring that the replication runs smoothly in the HVR 6 system, proceed to Phase 2.



Perform the following steps to implement Phase 1 of the upgrade process:

- 
If the HVR 5 system includes an HVR 5 Agent running on a remote location, install the HVR 6 Agent on the HVR 5 Agent machine to a new directory different from the HVR 5 installation directory. HVR 6 Agent should be installed on all HVR 5 Agent machines. For the steps to install the HVR 6 Agent, see section [Installing HVR Agent](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent).

> **Important:** 
Start the HVR 6 Agent on a port other than the HVR 5 Agent is currently running on. For example, if the HVR 5 Agent listens on port 4343, start the HVR 6 Agent on port 4340.


- 
Create a new empty repository database for HVR 6. For the list of databases supported as repository databases, see section [Repository Database](https://fivetran.com/docs/hvr6/capabilities/610#repositorydatabase) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

- 
Install HVR Hub System. If you are installing HVR Hub System on the same machine where HVR 5 is installed, the HVR Hub System must be installed as a separate system: to a directory other than the HVR 5 **HVR_HOME** and **HVR_CONFIG** directories. For the steps to install HVR Hub System, see section [Installing HVR Hub](https://fivetran.com/docs/hvr6/install-and-upgrade/install/hub).

- 
After the installation is complete, set up the HVR Hub System, which requires connecting it to its repository database and initializing that database's repository tables. For the steps to set up the HVR Hub System, see section [Setting up HVR Hub](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub).

- 
After completing the HVR Hub System setup, the [**Start**](https://fivetran.com/docs/hvr6/user-interface/user-interface-overview#startpage) page will open. Click **Skip channel or location creation** option available at the bottom of the page.

- 
Export the HVR 5 channels to the HVR 6 compatible import file (JSON) using the **hvrconvert5to6** script, which is available in the **HVR_HOME/script/** directory of the HVR 6 distribution. The generated file will be used to import the channel definition to the HVR 6 Hub.

There are two ways to do this:

- 
**Method 1:** Generate HVR 5 channel export file (XML) and convert it to HVR 6 compatible import file (JSON).

- 
Use the HVR 5 command [**hvrcatalogexport**](https://fivetran.com/docs/hvr5/commands/hvrcatalogexport-hvrcatalogimport) or the **Export Catalogs** option in HVR 5 GUI to generate the HVR 5 channel export file (XML).

- 
Run the **hvrconvert5to6** script to convert the HVR 5 channel export file (XML) to HVR 6 compatible import file (JSON):
hvr <em>hvrconvert5to6_script_path</em>/hvrconvert5to6 -f <em>hvr5_export</em>.xml <em>hvrhub</em> <em>export_channel</em>.json

To migrate a specific channel (e.g. **mychannel**) only, use option <b>-c</b>:
hvr <em>hvrconvert5to6_script_path</em>/hvrconvert5to6 -c mychannel -f <em>hvr5_export</em>.xml <em>hvrhub</em> <em>export_channel</em>.json



- 
**Method 2:** Generate the HVR 6 compatible import file (JSON) by directly fetching data from the HVR 5 hub database.

- 
Run the **hvrconvert5to6** script:
hvr <em>hvrconvert5to6_script_path</em>/hvrconvert5to6 -h oracle -u <em>hvruser/hvr</em> <em>hvrhub</em> <em>export_channel</em>.json

> **Note:** 
For more information about using option <b>-h</b> for other location types (class), see [Calling HVR on the Command Line](https://fivetran.com/docs/hvr5/commands/calling-hvr-on-the-command-line) (HVR 5).






- 
In the HVR 6 system, import the channel from the HVR 6 compatible import file (JSON) generated in the previous step:

- 
On the left sidebar, click **CHANNELS**.

- 
On the **Channels** page, click **Import Channel Definitions**.


- 
In the file browser, select the HVR 6 compatible import file (e.g. **export-channel.json**) that was generated on step 6 and click **Open**.

- 
The **Import Summary** dialog shows the details of the import. Click **Continue**.



- 
The channel will be added to the **Channels** page.




Run command [**hvrdefinitionimport**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrdefinitionimport) to import the channel definition:
hvrdefinitionimport <em>hvrhub</em> <em>path_to_export_channel</em>.json

- 
If the channel contains remote locations with an HVR 5 Agent configured on them, change the agent port to the port used to start the HVR 6 Agent.

> **Important:** 
Repeat the agent configuration steps (a-f) for all locations in the channel that use an HVR Agent for connection.


- 
On the left sidebar, click **LOCATIONS**.

- 
Click the location name to open its **Location Details** page.

- 
In the **Agent** pane, click **Edit**.

- 
In the **Agent** dialog, specify the port of the HVR 6 Agent and click **Test Agent Connection**.

- 
Click **Save**.

> **Important:** 
To configure the agent, click **Configure Agent Service**. For more information about [configuring the agent](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent), see section [Configuring HVR Agent from Browser](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser).






Run command [**hvrlocationconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlocationconfig) to change the port number:
hvrlocationconfig <em>hvrhub</em> <em>location</em> Agent_Port=<em>portnumber</em>

> **Important:** 
To configure the HVR 6 Agent, use command [**hvragentconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig). For more information about [configuring the agent](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent), see section [Configuring HVR Agent from CLI](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-cli).


- 
In the HVR 5 system, perform the following steps:

- 
Run [**Compare**](https://fivetran.com/docs/hvr5/commands/hvrcompare) to ensure that all tables in the test source location are in sync with those on the test target location.

In HVR 5 GUI:

- In the navigation tree pane, right-click the channel name and select **HVR Compare**.
- Select the source location on the left side and the target location on the right side.
- Select **Row by Row Granularity** in the **Options** tab.
- Click **Compare**.



Run HVR 5 command [**hvrcompare**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcompare) to compare tables between source and target locations:
hvrcompare -r<em>src</em> -l<em>tgt</em> <em>hub/hubpasswd channel</em>

- 
Stop the capture job using command [**Hvrcontrol**](https://fivetran.com/docs/hvr5/commands/hvrcontrol). Option **-F** stops the capture job at the end of the next replication cycle.
hvrcontrol -c -F <em>hub</em> <em>channel</em>

> **Important:** 
Ensure that the latency of the capture and integrate jobs drops to zero (e.g. using the [Statistics](https://fivetran.com/docs/hvr6/user-interface/statistics) graph or checking the capture and integrate jobs' log files), so that all the router files are processed before continuing.


- 
Run the [**hvrconvert5to6activate**](#hvrconvert5to6activate) script to generate appropriate commands that must be run in HVR 6 system for performing a refresh-less upgrade from HVR 5 to HVR 6:
hvr /hvr_home/script/hvrconvert5to6activate -c <em>chn</em> -h oracle <em>hub</em>/<em>pwd</em>

> **Note:** 
For more information about using option <b>-h</b> for other location types (class), see [Calling HVR on the Command Line](https://fivetran.com/docs/hvr5/commands/calling-hvr-on-the-command-line) (HVR 5).


Sample output:
hvrconvert5to6activate: HVR 5.7.0/18 (linux_glibc2.17-x64-64bit)
hvrconvert5to6activate: All generated commands have to be executed in the HVR 6 system. Please correct the hub and/or channel names manually if they are different in the HVR 6 system.

# Commands for channel 'mychannel':
# Activate entire channel and emit changes starting from Oracle SCN 1286643358.
hvractivate -i 2021-08-20T15:03:04+02:00 -I scn=1286643358 myhub mychannel



- 
In the HVR 6 system, activate the HVR 6 channel using the command output in the previous step and start the [Capture](https://fivetran.com/docs/hvr6/action-reference/capture) and [Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate) jobs in HVR 6. The jobs will catch up from where the channel was stopped in HVR 5.

- On the left sidebar, click **CHANNELS**.
- On the **Channels** page, click the imported channel name to open its **Channel Details** page.
- On the **Channel Details** page, click **Activate Replication** at the top right.
- In the **Activate Replication** dialog, select option **Custom Rewind Time** and specify the required time from the output of the **hvrconvert5to6activate** command in the previous step. For Oracle, select option **Delay Emission Unit Oracle SCN** and specify the required SCN number.
- Click **Activate Replication**.
****


Run command **hvractivate** to activate the channel and start the capture and integrate jobs:
hvractivate -i 2021-08-20T15:03:04+02:00 -I scn=1286643358 -Jcap -Jinteg <em>hub channel</em>



### Phase 2. Setting Up Replication from HVR 5 Source Database to HVR 6 Target Database


This phase involves installing an HVR 6 Agent on the HVR 5 production source location and directing data flow from HVR 5 production source database via HVR Hub to HVR 6 test target database.



Perform the following steps to implement Phase 2 of the upgrade process:

- 
In the HVR 5 production system: if the HVR 5 Agent is running on a remote source location, install HVR 6 Agent on the HVR 5 Agent machine to a new directory that is different from the HVR 5 installation directory. HVR 6 Agent should be installed on all HVR 5 Agent machines. For the steps to install the HVR Agent, see section [Installing HVR Agent](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent).

> **Important:** 
Start the HVR 6 Agent on a port other than that the HVR 5 Agent is currently running on. For example, if the HVR 5 Agent listens on port 4343, start the HVR 6 Agent on port 4340.


- 
Export the HVR 5 channels to the HVR 6 compatible import file (JSON) using the **hvrconvert5to6** script. The generated file will be used to import the channels to the HVR 6 Hub.

> **Important:** 
Repeat steps 2-8 for all of the HVR 5 production channels until they are all converted and run in the HVR 6 test hub.


There are two ways to do this:

- 
**Method 1:** Generate HVR 5 channel export file (XML) and convert it to HVR 6 compatible import file (JSON).

- 
Use the HVR 5 command [**hvrcatalogexport**](https://fivetran.com/docs/hvr5/commands/hvrcatalogexport-hvrcatalogimport) or the **Export Catalogs** option in HVR 5 GUI to generate the HVR 5 channel export file (XML).

- 
Run the **hvrconvert5to6** script to convert the HVR 5 channel export file (XML) to HVR 6 compatible import file (JSON):
hvr <em>hvrconvert5to6_script_path</em>/hvrconvert5to6 -f <em>hvr5_export</em>.xml <em>hvrhub</em> <em>export_channel</em>.json

To migrate a specific channel (e.g. **mychannel**) only, use option <b>-c</b>:
hvr <em>hvrconvert5to6_script_path</em>/hvrconvert5to6 -c mychannel -f <em>hvr5_export</em>.xml <em>hvrhub</em> <em>export_channel</em>.json



- 
**Method 2:** Generate the HVR 6 compatible import file (JSON) by directly fetching data from the HVR 5 hub database.

- 
Run the **hvrconvert5to6** script:
hvr <em>hvrconvert5to6_script_path</em>/hvrconvert5to6 -h oracle -u hvruser/hvr <em>hvrhub</em> <em>export_channel</em>.json

> **Note:** 
For more information about using option <b>-h</b> for other location types (class), see [Calling HVR on the Command Line](https://fivetran.com/docs/hvr5/commands/calling-hvr-on-the-command-line) (HVR 5).






- 
In the HVR 6 test system, go to the HVR [user interface](https://fivetran.com/docs/hvr6/user-interface) in the browser.

- 
On the HVR 6 test hub, import the channel from the file generated on step 2 of [Phase 2](#phase2) (for instructions on how to import channels to HVR 6 Hub, see step 8 of [Phase 1](#phase1upgradingtestenvironment)).

- 
If the channel contains remote source locations with an HVR 5 Agent configured on them, change the agent port to the port used for the HVR 6 Agent on the HVR 5 production source machine:

> **Important:** 
Repeat the agent configuration steps (a-d) for all locations in the channel that use an HVR Agent for connection.


- 
On the left sidebar, click **LOCATIONS**.

- 
Click the location name to open its **Location Details** page.

- 
In the **Agent** pane, click **Edit**.

- 
In the **Agent** dialog, specify the port of the HVR 6 Agent and click **Test Agent Connection**.

- 
Click **Save**.

> **Important:** 
To configure the agent, click **Configure Agent Service**. For more information about [configuring the agent](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent), see section [Configuring HVR Agent from Browser](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser).






Run command **hvrlocationconfig** to change the port number:
hvrlocationconfig <em>hvrhub </em><em>location</em> Agent_Port=<em>portnumber</em>

> **Important:** 
To configure the HVR 6 Agent, use command **hvragentconfig**. For more information about [configuring the agent](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent), see section [Configuring HVR Agent from CLI](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-cli).


- 
For the target location, modify the agent connection details to point to the port of the HVR 6 Agent running on the test target machine.

- 
Once everything is configured, activate the imported channel:

- On the left sidebar, click **CHANNELS**.
- On the **Channels** page, click the imported channel name to open its **Channel Details** page.
- On the **Channel Details** page, click **Activate Replication** at the top right.
- In the **Activate Replication** dialog, select option **Refresh Data into Target After Activation** and then option **Create Missing Target Tables and Alter or Recreate Tables with Incorrect Layout**.




- 
Compare data between the tables in the HVR 5 production source database and the HVR 6 test target database:

- 
On the **Channel Details** page, click **Compare Data** at the top right.

- 
In the **Compare Data** dialog, click **Compare Data**.



- 
To view the results of the compare job, click **show...inactive** on the **Jobs** pane: this will display all inactive events in the channel.

- 
Click the **More Options** icon  related to the compare job and select **Go to Event**: this will open the [**Event Details**](https://fivetran.com/docs/hvr6/user-interface/events/event-details) page with the details about the compare event.







### Phase 3. Upgrading Production System


This phase involves installing HVR 6 on the HVR 5 production hub machine and routing the data coming from the production source database to the production target database through the HVR 6 system.



Perform the following steps to implement Phase 3 of the upgrade process:

- 
Create a new empty repository database for the HVR Hub Server in the production system. For the list of databases supported as repository databases, see section [Repository Database](https://fivetran.com/docs/hvr6/capabilities/610#repositorydatabase) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).

- 
On the production hub machine, install HVR 6. If you are installing HVR 6 on the same machine where HVR 5 is installed, the HVR 6 must be installed as a separate system: to a directory other than the HVR 5 **HVR_HOME** and **HVR_CONFIG** directories. For the steps to install HVR Hub, see section [Installing HVR Hub](https://fivetran.com/docs/hvr6/install-and-upgrade/install/hub).

- 
After the installation is complete, set up the HVR Hub System, which requires connecting it to the repository database (created on step 1) and initializing that database's repository tables. For the steps to set up the hub server, see section [Setting up HVR Hub](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub).

- 
Follow steps 6-11 in [Phase 1](#phase1upgradingtestenvironment) until all channels are migrated and activated to the HVR 6 production hub.

- 
Once all channels are running in the HVR 6 production hub, stop all channels in the HVR 5 system and ensure that the latency of the capture and integrate jobs in HVR 5 system drops to zero (e.g. using the [**Statistics**](https://fivetran.com/docs/hvr5/hvr-insights/statistics) graph or checking the capture and integrate jobs' log files).

- 
Run [**Compare**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data) in the HVR 6 system to check if tables in the source location are in sync with those in the target location.

- 
On the left sidebar, click **CHANNELS**.

- 
On the **Channels** page, click the required channel name to open its **Channel Details** page.

- 
On the **Channel Details** page, click **Compare Data** at the top right.

- 
In the **Compare Data** dialog, click **Compare Data**.





- 
Stop the HVR 5 Agents.

For example, to stop/kill the **hvrremotelistener** that is running as a daemon process and listening on port 4343, execute the following command:
hvrremotelistener -k 4343

To halt and destroy the **hvrremotelistener** that is running as a Windows service and listening on port number 4343, execute the following command:
hvrremotelistener -ahd 4343


