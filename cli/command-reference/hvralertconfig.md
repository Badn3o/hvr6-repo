# hvralertconfig - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertconfig

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvralertconfig/index.md)

# hvralertconfig


## Usage


- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <em>hub</em> List all the alerts configured on the *hub*.
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <em>hub alert</em> List the [properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties) of the *alert* configured on the *hub*.
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] [<b>-o</b><em>jsonfile</em>] <em>hub alert</em> [<em>property</em>]... Print the specified [alert properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties) (*property...*) configured on the *hub*, or all if none are specified.
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] [<b>-i</b><em>jsonfile</em>] <em>hub alert</em> [<em>property</em>=[<em>value</em>]]... Set or unset the specific [alert properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties) supplied in the *jsonfile* and/or directly on the command line.
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <b>-a</b> [<b>-i</b><em>jsonfile</em>] <em>hub alert</em> [<em>property</em>=<em>value</em>]... Replace all the existing [properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties) of the *alert* configured on the *hub* with a new set of properties supplied in the *jsonfile* and/or directly set on the command line (*property=**value*...).
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <b>-c</b> <em>hub alert</em> <em>property</em>=<em>value</em>... Create an *alert* on the *hub* with specified [properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties) and set values for the properties (*property=value...*).
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <b>-d</b> <em>hub alert</em> Delete the *alert* configured on the *hub*.
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <b>-D</b> <em>hub alert</em> Disable the *alert* configured on the *hub*.
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <b>-C</b> <em>hub alert</em> Clear the *alert* configured on the *hub*.
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <b>-t</b><em> hub alert</em> Test the *alert* configured on the *hub*.
- <b>hvralertconfig</b> [<b>-R</b><em>url</em>] <b>-e</b><em> hub alert</em> Execute the *alert* configured on the *hub*.


## Description


The **hvralertconfig** command allows you to create an alert and manage the existing alerts. HVR alerts scan the hub server log files and, according to their [configuration properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties), send notifications about any issues encountered (errors, warnings, latency threshold exceeded).

Argument <em>hub</em> specifies the name of a hub on which an alert(s) are configured. Argument <em>alert</em> specifies the name of an alert.

When you create an alert (using option <b>-c</b>), an alert configuration file (*alert_name***.conf**) is created in the **HVR_CONFIG/hubs/***hub***/alerts** directory. The file contains the [alert configuration properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties) specified when the alert was created, i.e. every alert has a certain set of alert properties. For an alert, you always must specify the type of notification: Email, SNS, Slack, or SNMP. If you want to receive alert notifications of different types, e.g. via email and Slack, separate alerts need to be configured.

The [**hvralertmanager**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertmanager) command is responsible for executing all the alerts configured on the hub server.

For the alert properties that can be configured using this command, see section [Alert Properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties).

> **Note:** 
Command **hvralertconfig** corresponds to the [**Alerts**](https://fivetran.com/docs/hvr6/user-interface/system/alerts) dialog in the [User Interface](https://fivetran.com/docs/hvr6/user-interface).


## Options


This section describes the options available for the **hvralertconfig** command.

 Parameter | Description |
 `**-a**` | 
Replace the existing alert properties with a new set of alert properties. The new set of alert properties may be supplied directly in the command line or from a JSON file using option `**-i**`.

The following syntaxes are applicable:

- 
The following command replaces the current alert properties with the properties supplied in *jsonfile*.
`hvralertconfig -a -i *jsonfile hub alert*`
- 
The following command replaces the current alert properties with the properties supplied on the command line.
`hvralertconfig -a *hub alert**property1=value1 property2=value2 property3=value3*`
- 
The following command replaces the current alert properties with the properties supplied in *jsonfile* and on the command line.

`hvralertconfig -a -i *jsonfile hub alert property1=value1 property2=value2 property3=value3*`
> **Important:** 
The properties supplied directly on the command line will override the relevant properties in *jsonfile*.




For specific examples, see [Replace alert properties](#replacealertproperties). |
 `**-c**` | 
Create an alert. This option requires alert property **[Notification_Type](https://fivetran.com/docs/hvr6/property-reference/alert-properties)** to be specified, and other properties depending on the notification type you specify.

For specific examples, see [Create Email alert](#createemailalert), [Create SNS alert](#createsnsalert), [Create SNMP alert](#createsnmpalert).

In the User Interface, this option corresponds to the [New Alert](https://fivetran.com/docs/hvr6/user-interface/system/alerts/creating-alerts) dialog. |
 `**-C**` | 
Clear and enable an alert. This option enables an alert (if disabled) and disregards any pending errors, so that only new errors will be reported the next time the alert is run. If an alert is already enabled, it just disregards pending errors.

> **Important:** 
There can be multiple alerts configured on a hub (for example for different notification types: Email, Slack. etc), but some of them could be disabled. When [**hvralertmanager**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertmanager) runs, it will not execute the disabled alerts.


For example, the following command enables alert **myalert**.
`hvralertconfig -C myhub myalert` |
 `**-d**` | 
Delete an alert.

For example, the following command deletes alert **myalert**:
`hvralertconfig -d myhub myalert`
In the User Interface, this option corresponds to the **Delete Alert(s)** option in the **[More options](https://fivetran.com/docs/hvr6/user-interface/system/alerts#managingalerts)** menus  |
 `**-D**` | 
Disable an alert. It will not be executed until it is enabled again.

For example, the following command disables alert **myalert**:
`hvralertconfig -D myhub myalert`
In the User Interface, this option corresponds to the **Disable/Enable Alerts** option in the **[More options](https://fivetran.com/docs/hvr6/user-interface/system/alerts#managingalerts)** menus  |
 `-e` | 
Execute an alert.

For example, the following command executes alert **myalert**:
`hvralertconfig -e myhub myalert` |
 `**-E***x*` | 
Override automatic encoding/decoding of string properties when reading a property from file using `*property=@file_name*` or when writing a property to file using `*property>@file_name*`. This option may be required only while setting the [property](https://fivetran.com/docs/hvr6/property-reference) whose argument is **base64**.

When this option is not used, the `default` encoding is **base64**.

Valid values of `*x*` are:

- **none**: no encoding/decoding will be applied.
- **base64**: encode a property in the base64 format.

 |
 `**-i***jsonfile*` | 
Read property values from a JSON file *`jsonfile`.*

For example, the following command creates alert **myalert** using the alert properties file **alert_props.json**:
`hvralertconfig -i alert_props.json -c myhub myalert` |
 `**-o***jsonfile*` | 
Write the specified properties to a JSON file `*jsonfile*`.

For example, the following command writes the listed properties into the **alert_props.json** file (this should be a single line without wrapping).
`hvralertconfig -o alert_props.json myhub myalert Notification_Type=EMAIL Email_SMTP_Server=smtp.mycorp.com Email_SMTP_Starttls=true`
If no properties are specified on the command line, then all properties are fetched from the alert configuration file (*alert_name*.**conf**).
For example, the following command writes the properties of alert **myalert** from the **myalert.conf** file**** to the **myalert_props.json** file:
`hvralertconfig -o myalert_props.json myhub myalert` |
 `**-R***url*` | 
Remote hub server. Access the hub server running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

This option is required for [remote CLI access](https://fivetran.com/docs/hvr6/command-line-interface). When using this option, command **[hvrlogin](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)** should be run first, for authentication.

For example, the following command deletes alert **myalert** on a remote hub server:
`hvralertconfig -R http://node:port -d myhub myalert ` |
 `**-t**` | 
Test an alert to verify if notification settings (Slack, email, etc) are properly configured.

For example, the following command sends a test notification defined in alert **myalert**:
`hvralertconfig -t myhub myalert`
In the User Interface, this option corresponds to the **Send Test Notification** option in the **[More options](https://fivetran.com/docs/hvr6/user-interface/system/alerts#managingalerts)** menus  |
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


This section provides examples of using the **hvralertconfig** command.

##### Example 1. Get alert properties


The following command prints the value of property **Repeat_Interval** of alert **myalert**.
hvralertconfig myhub myalert Repeat_Interval

##### Example 2. Set alert properties


- 
The following command sets property **Repeat_Interval** to value **500** for alert **myalert**.
hvralertconfig myhub myalert Repeat_Interval=500

- 
The following command sets the properties specified in the **alert_props.json** file for alert **myalert**.
hvralertconfig -i alert_props.json myhub myalert

- 
The following command sets properties specified in the **alert_props.json** file and property **Repeat_Interval** for alert **myalert**.
hvralertconfig -i alert_props.json myhub myalert Repeat_Interval=500

> **Important:** 
If the **agent_props.json** file contains properties that are already set for alert, option <b>-i</b> will override these properties.

For example, the following properties are currently set: **Notification_Type**, **SNS_Destination**, **SNS_Access_Key_Id**, **SNS_Secret_Access_Key**, and **Repeat_Interval**. The **agent_props.json** file contains property **Repeat_Interval**. Option <b>-i</b> will override the current value of property **Repeat_Interval** only.




##### Example 3. Unset alert properties


The following command unsets property **Repeat_Interval** of alert **myalert**.
hvralertconfig myhub myalert Repeat_Interval=

##### Example 4. Replace alert properties 


- 
The following command replaces the properties of alert **myalert** with the properties supplied in the **alert_props.json** file.
hvralertconfig -a -i alert_props.json myhub myalert

- 
The following command replaces the current email recipient with a new recipient **joe@mycorp.com** (this should be a single line without wrapping).
hvralertconfig -a myhub myalert Notification_Type=EMAIL Email_SMTP_Server=smtp.mycorp.com Email_Recipients[0]=joe@mycorp.com

- 
The following command replaces the properties of alert **myalert** with the properties supplied in the **alert_props.json** file and property **Repeat_Interval**.
hvralertconfig -a -i alert_props.json myhub myalert Repeat_Interval=500

> **Important:** 
The properties supplied directly on the command line will override the relevant properties in the **alert_props.json** file.




##### Example 5. Create Email alert 


The following command creates an Email alert **myalert** with multiple properties that sends email notifications to **joe@mycorp.com** and **jane@mycorp.com** (this should be a single line without wrapping).
hvralertconfig -c myhub myalert Notification_Type=EMAIL Email_Recipients[++]=joe@mycorp.com Email_Recipients[++]=jane@mycorp.com Email_SMTP_Server=smtp.mycorp.com Email_SMTP_Starttls=true Ignore_Patterns=F_JT* Message_Error_Limit=10 Add_HVR_Event=true Repeat_Interval=10 Specific_Locations[++]=myloc Specific_Channels[++]=mychannel

##### Example 6. Create SNS alert 


The following command creates an SNS alert (this should be a single line without wrapping).
hvralertconfig -c myhub sns_alert Notification_Type=SNS SNS_Destination=arn:aws:sns:eu-west-1:6675700182:test SNS_Access_Key_Id=KNDTMY7FTX0KSDRRNTPV SNS_Secret_Access_Key=K9D7G6mm6ZOi9DReodELDmLNC/1Fc

##### Example 7. Create SNMP alert 


The following command creates an SNMP alert (this should be a single line without wrapping).
hvralertconfig -c myhub snmp_alert Notification_Type=SNMP SNMP_Hostname=localhost SNMP_Port=189 SNMP_Community=public SNMP_Heartbeat=true SNMP_Version=V2C

  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
