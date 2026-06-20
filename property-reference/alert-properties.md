# Alert Properties - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/property-reference/alert-properties

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/property-reference/alert-properties/index.md)

# Alert Properties


This section lists and describes the Fivetran HVR alert properties.

An alert property specifies the characteristics/attributes of various alerts generated in HVR. These properties are set when creating/modifying alerts from the ([Alerts](https://fivetran.com/docs/hvr6/user-interface/system/alerts)) tab in UI or using the command [**hvralertconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertconfig).

> **Note:** 
An array property and map property can store multiple values. The syntax for updating them from the [Command Line Interface (CLI)](https://fivetran.com/docs/hvr6/command-line-interface/managing-properties-in-cli) varies.


---

### Add_HVR_Event


**Argument:** true

**Description:** If set to **true**, HVR creates an [event](https://fivetran.com/docs/hvr6/getting-started/concepts/events) every time an alert notification is sent.

This event can be viewed on the [Events](https://fivetran.com/docs/hvr6/user-interface/events) page.

---

### Email_From_Address


**Argument:** *address*

**Description:** Email address of the sender in the notification email header.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **EMAIL**.

---

### Email_Recipients


**Argument:** *address1* [,*address2*]

**Description:** Email address(es) to which HVR will send an email notification. This property can be defined only if [**Notification_Type**](#notificationtype) is set to **EMAIL**.

Multiple email addresses can be specified with values separated by a comma.

This property requires [**Email_SMTP_Server**](#emailsmtpserver).

This is an array property that can store multiple values.

---

### Email_SMTP_Password


**Argument:** *password*

**Description:** Password for the SMTP user ([**Email_SMTP_User**](#emailsmtpuser)).

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **EMAIL**.

---

### Email_SMTP_Port


**Argument:** *port*

**Description:** SMTP *port* to use when sending an email notification. If this property is not defined, the **default** SMTP port is **25**. If [**Email_SMTP_Starttls**](#emailsmtpstarttls) is set to **true**, the **default** SMTP port is **465**.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **EMAIL**.

---

### Email_SMTP_Server


**Argument:** *server*

**Description:** SMTP *server* to use when sending an email notification to the recipient(s) defined in [**Email_Recipients**](#emailrecipients). Value *server* can be either a node name or IP address.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **EMAIL**.

---

### Email_SMTP_Starttls


**Argument:** true

**Description:** If set to **true**, use the STARTTLS method to communicate with the SMTP server.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **EMAIL**.

---

### Email_SMTP_User


**Argument:** *user*

**Description:** Username for authenticating SMTP server, if needed.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **EMAIL**.

---

### Ignore_Patterns


**Argument:** *pattern*

**Description:** Pattern to match error/warning records in the **hvr.out** file.

If defined, HVR alert system will ignore the matching error/warning records, which means alert notification will not be sent for these errors/warnings.

For example, if pattern **F_JT.*|W_JD.*** is defined, alert notification will not be sent for all errors starting with **F_JT** or warnings starting with **W_JD**.

---

### Ignore_Warnings


**Argument:** true

**Description:** If set to **true**, notifications are sent only for errors. HVR will **not** send alert notifications when the alert system encounter a warning while scanning the **hvr.out** log file or when the latency limit is exceeded.

---

### Max_Channel_Idle_Minutes


<strong>Since</strong> v6.1.5/2

**Argument:** *minutes*

**Description:** Send notifications when the channel has empty [**Capture**](https://fivetran.com/docs/hvr6/action-reference/capture) cycles (no data captured) for a duration that exceeds the time (in *minutes*) specified in this parameter.

---

### Max_Hub_Idle_Minutes


<strong>Since</strong> v6.1.5/2

**Argument:** *minutes*

**Description:** Send notifications when there is no activity in the HVR Hub for a duration that exceeds the time (in *minutes*) specified in this parameter.

---

### Message_Error_Limit


**Argument:** *limit*

**Description:** Maximum number (*limit*) of errors reported in HVR alert. This option prevents the generated notification (email, SNS, or Slack) from becoming too large.

If this property is not defined, the **default** *limit* for email and SNS notification is **1000**. For Slack notification, the **default** and maximum *limit* is **40**.

---

### Notification_Type


**Argument:** *type*

**Description:** Type of the alert notification that the HVR alert system will send.

Available options for *type* are:

- **EMAIL** - Send notification as email.
- **SNS** - Send notification using Amazon SNS.
- **SNMP** - Send notification as SNMP traps.
- **SLACK** - Send notification as Slack messages.


---

### Repeat_Interval


**Argument:** *secs*

**Description:** Send alert for the same error/warning only after the specified duration in seconds *secs*.

By default, each time when HVR alert system encounters an error itself or detects an HVR error or warning while scanning **hvr.out** or the latency limit is exceeded, the alerting system sends out an alert until the issue is fixed. The number of alerts sent depends on the frequency at which the [**hvralertmanager**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvralertmanager) is configured to run. As long as the issue is not resolved or the error/warning has not changed, the alerting system will repeatedly send alerts for the same issue.

To avoid repeatedly sending alerts for the same issue, this option forces HVR alerting system to remain silent for the specified duration after the first alert is sent out.

---

### Slack_Channel


**Argument:** *channel*

**Description:** Slack user (@*username*) or *channel* to which HVR will send Slack message notifications. This optional property can be used to override the value defined in the [**Slack_Webhook_URL**](#slackwebhookurl).

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SLACK**.

---

### Slack_Webhook_URL


**Argument:** *url*

**Description:** Incoming webhook URL for the Slack channel to which HVR will send Slack message notifications.

To generate a Slack incoming webhook, see [Slack documentation](https://api.slack.com/messaging/webhooks).

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SLACK**.

---

### SNMP_Community


**Argument:** *str*

**Description:** Community string *str* for SNMP agent to receive traps.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SNMP**.

---

### SNMP_Heartbeat


**Argument:** true

**Description:** If set to **true**, send a **hvrMaintNotifySummary** notification, even if there was nothing to report.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SNMP**.

---

### SNMP_Hostname


**Argument:** *host*

**Description:** Host name of the SNMP agent. The **Default** host is **localhost**.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SNMP**.

---

### SNMP_Port


**Argument:** *port*

**Description:** Port number for the SNMP agent to receive traps. The **Default** port is **162**.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SNMP**.

---

### SNMP_Version


**Argument:** *version*

**Description:** SNMP version.

Available options for *version* are:

- **V1**
- **V2C**


This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SNMP**.

---

### SNS_Access_Key_Id


**Argument:** *keyid*

**Description:** Access key ID of the AWS IAM user. For more information about the access key, refer to [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in [AWS documentation](https://docs.aws.amazon.com/).

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SNS**.

---

### SNS_Destination


**Argument:** *arn*

**Description:** Amazon Resource Name (ARN) of the [SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-create-topic.html) to which HVR will send alert notification.

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SNS**.

---

### SNS_Secret_Access_Key


**Argument:** *key*

**Description:** Secret access key of the AWS IAM user.

For more information about the secret key, refer to [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in [AWS documentation](https://docs.aws.amazon.com/).

This property can be defined only if [**Notification_Type**](#notificationtype) is set to **SNS**.

---

### Specific_Channels


**Argument:** *chn*

**Description:** Only scan the specified channel(s) *chn* for errors and warnings.

This is an array property that can store multiple values.

---

### Specific_Locations


**Argument:** *loc*

**Description:** Only scan the specified locations(s) *loc* for errors and warnings.

This is an array property that can store multiple values.

.actparam {
    padding-left: 20px;
}
