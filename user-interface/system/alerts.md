# Alerts - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/user-interface/system/alerts

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/user-interface/system/alerts/index.md)

# Alerts


The **Alerts** tab on the [**System**](https://fivetran.com/docs/hvr6/user-interface/system) page displays a list of all alerts configured on a HVR Hub System.

Under this tab, you can create an alert and manage the existing alerts. Alerts scan the hub server log files and, according to their [configuration properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties), send notifications about any issues encountered (errors, warnings, latency threshold exceeded).

When you create an alert, an alert configuration file (*alert_name***.conf**) is created in the **HVR_CONFIG/hubs/***hub***/alerts** directory. The file contains the [alert configuration properties](https://fivetran.com/docs/hvr6/property-reference/alert-properties) specified when the alert was created, i.e. every alert has a certain set of alert properties. For an alert, you always must specify the type of notification: Email, SNS, Slack, or SNMP. If you want to receive alert notifications of different types, e.g. via email and Slack, separate alerts need to be configured.

The [**hvralertmanager**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertmanager) command is responsible for executing all the alerts configured on the hub server.

> **Note:** 
The **Alerts** dialog corresponds to the [**hvralertconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertconfig) command.


The page provides the following information about alerts.

 Field | Description |
 **Alert** | Alert name. Clicking the alert name opens the **Edit Alert** dialog. |
 **Type** | 
Type of the alert notification that the alerting system will send.

Available options are:

- **EMAIL** - Send notification as email.
- **SNS** - Send notification using Amazon SNS.
- **SNMP** - Send notification as SNMP traps.
- **SLACK** - Send notification as Slack messages.

 |
 **Last Check** | The last time the alert was executed. |
 **Description** | Specific channels and/or locations for which the alert is configured, i.e. only the specified channel(s) and/or location(s) will be checked by the alert. |


> **Important:** 
The [**hvralertmanager**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertmanager) should be [scheduled](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertmanager#schedulinghvralertmanager) to run at certain time intervals for monitoring the status of the HVR Hub System. When an alert is not executed within two hours (provided that the alert is not disabled and the hub is not frozen), warning "**Alert execution is overdue**" is displayed in the **LAST CHECK** column. To prevent resource-intensive scans, alerts that have not run for over 5 hours will only process the most recent log file upon execution, skipping archived logs.




## Managing Alerts


The following options to manage alerts are available at the top right menu, as well as under the **More options** menus  related to each alert.

> **Note:** 
To select multiple alerts in one go, select the first alert, hold the **Shift** key and then select the last alert - all alerts in between the first and the last will be selected.


- 
**Create New Alert**
Create a new alert. For steps to create an alert, see [Creating Alerts](https://fivetran.com/docs/hvr6/user-interface/system/alerts/creating-alerts).

- 
**View Alert Manager Log**
This option opens the **hvralertmanager.out** log file in the [**Log Viewer**](https://fivetran.com/docs/hvr6/user-interface/viewing-log) drawer containing the **Alert** **Manager** runtime information.

- 
**Disable/Enable Alerts**
Disable/enable the selected alert. Once disabled, an alert will not be executed until it is enabled again.

- 
**Send Test Notification**

Test an alert to verify if notification settings (Slack, email, etc) are properly configured.

This applies only when an alert is enabled.

- 
**Perform Alert Check**
Execute an alert. This applies only when an alert is enabled.

- 
**Clear Outstanding Errors**
Disregard any pending errors, so that only new errors will be reported the next time the alert is run. This applies only when an alert is enabled.

- 
**Duplicate Alert**
Create a copy of an existing alert with all its configured properties. When you click **Duplicate Alert**, the **Edit Alert** dialog opens, where you need to specify a unique name of the new alert.

- 
**Delete Alert(s)**
Delete selected alerts.

- 
**View Alert Log**
This option opens the alert's log file in the [**Log Viewer**](https://fivetran.com/docs/hvr6/user-interface/viewing-log) drawer containing the alert runtime information.


