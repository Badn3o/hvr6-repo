# Repository Tables - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/internal-objects/repository-tables

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/internal-objects/repository-tables/index.md)

# Repository Tables


## Introduction


Repository tables are created automatically in HVR. They are for reference only and cannot be altered manually.

HVR uses its repository database to store the replication definitions (which tables must be replicated between which 'locations') as well as run-time status (which jobs are currently running). In a repository database the information is stored in the repository tables, which are divided into the following three categories:

- [**Configuration Tables**](#configurationtables)
- [**Definition Tables**](#definitiontables)
- [**Run-Time Tables**](#runtimetables)


> **Warning:** 
Do not <b>INSERT</b>/<b>UPDATE</b>/<b>DELETE</b> values from repository tables using SQL commands. It will lead to data loss and corruption.


## Entity Relationship Diagram




## Tables in Repository Database


This section describes all tables and columns available in the repository database.

### Configuration Tables


This group of repository tables contains information that is managed by the system administrators and the owners of the hub using the User Interface or the commands - [**hvrreposconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrreposconfig), [**hvrhubconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubconfig), and [**hvruserconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig).

Following are the configuration tables:

#### HVR_HUB


Table containing row for each hub in the repository database.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Unique name for the hub. It must be a lowercase identifier containing only alphanumerics and underscores. |


#### HVR_REPOS_PROPERTY


Table containing values for the [repository properties](https://fivetran.com/docs/hvr6/property-reference/repository-properties). The properties in this table can only be changed by a user with **SysAdmin** permission.

 Column | Data type | Description |
 **prop_name** | String 64 characters | Name of the repository property. |
 **prop_value** | Long string object | Value of the repository property. |
 **last_updated** | Datetime with microsecond precision | The moment this row was inserted or last updated. |


#### HVR_USER


Table containing the list of users that may access HVR Hub Server. The properties in this table can only be changed by a user with **SysAdmin** permission.

 Column | Data type | Description |
 **user_name** | String 128 characters | Login name or account name of user. |
 **user_authen** | String 16 characters | System used by the HVR Hub Server to authenticate the user. Currently, only value **local** is allowed, this indicates the user's password is checked against the password hash held locally in this repository table. |
 **user_pwd** | String 128 characters | Hash of password for user with **local** authentication. |
 **last_updated** | Datetime with microsecond precision | The moment this row was inserted or last updated. |


#### HVR_USER_PROPERTY


Table containing values for [user properties](https://fivetran.com/docs/hvr6/property-reference/user-properties) which are effective for all hubs. The properties in this table can only be changed by the user who the property is for or a user who has **SysAdmin** permission.

 Column | Data type | Description |
 **user_name** | String 128 characters | Login name or account name of user. |
 **prop_name** | String 64 characters | Name of the user property. |
 **prop_value** | Long string object | Value of the user property. |
 **last_updated** | Datetime with microsecond precision | The moment this row was inserted or last updated. |


#### HVR_USER_HUB_PROPERTY


Table containing values for [user hub properties](https://fivetran.com/docs/hvr6/property-reference/user-properties#userhubproperties): only effective for a specific hub. The properties in this table can only be changed by the user who the property is for or a user who has **SysAdmin** permission.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **user_name** | String 128 characters | Login name or account name of user. |
 **prop_name** | String 64 characters | Name of the user hub property. |
 **prop_value** | Long string object | Value of the user hub property. |
 **last_updated** | Datetime with microsecond precision | The moment this row was inserted or last updated. |


#### HVR_HUB_PROPERTY


Table containing values for the [hub properties](https://fivetran.com/docs/hvr6/property-reference/hub-properties). The properties in this table can only be changed by a user with **SysAdmin** or **HubOwner** permission.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **prop_name** | String 64 characters | Name of the hub property. |
 **prop_value** | Long string object | Value of the hub property. |
 **last_updated** | Datetime with microsecond precision | The moment this row was inserted or last updated. |


### Definition Tables


This group of repository tables contains information that defines various replication components such as locations, channels, tables, actions, etc. All definition tables have an **insert_tstamp** and **delete_tstamp** column which allows the definition states to be queried as it was at a previous point in time. The definitions can only be updated by a user with **SysAdmin**, **HubOwner**, or **ReadWrite** permission.

Following are the definition tables:

#### HVR_CHANNEL


Table containing the list of channels.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **chn_name** | String 12 characters | 
Unique name for the channel. It must be a lowercase identifier containing only alphanumerics and underscores. Because this value occurs so often in every logfile, program, database etc. it is recommended that this name be kept as small and concise as possible. Values **hvr_*** and **system** are reserved.

Channel name is used as a parameter in most of our commands, and also as a component for naming jobs, database objects, and files. For example, a capture job is named '*chn*–**cap**–*loc'* (*chn* indicates channel name). |
 **insert_tstamp** | Datetime with microsecond precision | The moment this row was inserted or the moment that an update was done (the previous row has this same value assigned into its **delete_tstamp** column). |
 **chn_description** | String 200 characters | Description for the channel. |
 **delete_tstamp** | Datetime with microsecond precision | The moment this row was deleted or the moment that an update was done (the new version of the row is inserted with the same value in its **insert_tstamp** column).
 |


#### HVR_LOCATION


Table containing the list of locations in the hub.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **loc_name** | String 12 characters | 
Name of the location. It must be a lowercase identifier containing only alphanumerics and underscores.

This name is used as a part of the name for the generated HVR objects, and also used as an argument in various commands. For example, the location database in Amsterdam could be named **amsterdam**. |
 **insert_tstamp** | Datetime with microsecond precision | The moment this row was inserted or the moment that an update was done (the previous row has this same value assigned into its **delete_tstamp** column). |
 **delete_tstamp** | Datetime with microsecond precision | The moment this row was deleted or the moment that an update was done (the new version of the row is inserted with the same value in its **insert_tstamp** column). |


#### HVR_LOCATION_PROPERTY


Table containing the list of [location properties](https://fivetran.com/docs/hvr6/property-reference/location-properties).

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **loc_name** | String 12 characters | Name of the location. |
 **prop_name** | String 64 characters | Name of the location property. |
 **insert_tstamp** | Datetime with microsecond precision | The moment this row was inserted or the moment that an update was done (the previous row has this same value assigned into its **delete_tstamp** column). |
 **prop_value** | Long string object | Value of the location property. |
 **delete_tstamp** | Datetime with microsecond precision | The moment this row was deleted or the moment that an update was done (the new version of the row is inserted with the same value in its **insert_tstamp** column). |


#### HVR_LOC_GROUP


Table containing the list of location group for each channel.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **chn_name** | String 12 characters | Name of the channel to which this location group belongs. |
 **grp_name** | String 24 characters | Unique UPPERCASE identifiers used as name of location group. Should begin with an alphabetic and contain only alphanumerics and underscores. |
 **insert_tstamp** | Datetime with microsecond precision | The moment this row was inserted or the moment that an update was done (the previous row has this same value assigned into its **delete_tstamp** column). |
 **delete_tstamp** | Datetime with microsecond precision | The moment this row was deleted or the moment that an update was done (the new version of the row is inserted with the same value in its **insert_tstamp** column). |


#### HVR_LOC_GROUP_MEMBER


Table contains channel membership information. A location can only be a member of one location group for any channel.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **chn_name** | String 12 characters | Channel name for location group. |
 **loc_name** | String 12 characters | Location belonging to this location group. |
 **insert_tstamp** | Datetime with microsecond precision | The moment this row was inserted or the moment that an update was done (the previous row has this same value assigned into its **delete_tstamp** column). |
 **grp_name** | String 24 characters | Name of location group defined in table **[HVR_LOC_GROUP](#hvrlocgroup)**. |
 **delete_tstamp** | Datetime with microsecond precision | The moment this row was deleted or the moment that an update was done (the new version of the row is inserted with the same value in its **insert_tstamp** column). |


#### HVR_TABLE


Table containing a row for each table entity replicated for each channel. For more information about table name and table groups, see concept pages - [Table Name and Base Name](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/table-name-and-base-name), and [Table Groups](https://fivetran.com/docs/hvr6/getting-started/concepts/channel/table-groups).

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **chn_name** | String 12 characters | Name of channel to which this table belongs. Each table name therefore belongs to a single channel. |
 **tbl_name** | String 124 characters | Replication name for table. Typically this is the same as the name of the table in the database location, but it could differ. For example if the table's database name is too long or is not an identifier. It must be a lowercase identifier; an alphabetic followed by alphanumerics and underscores. |
 **insert_tstamp** | Datetime with microsecond precision | The moment this row was inserted or the moment that an update was done (the previous row has this same value assigned into its **delete_tstamp** column). |
 **tbl_base_name** | String 128 characters | Name of database table to which this replication table refers. If the table has different names in different databases then the specific value can also be set using parameter **[BaseName](https://fivetran.com/docs/hvr6/action-reference/tableproperties#basename)** in action **[TableProperties](https://fivetran.com/docs/hvr6/action-reference/tableproperties)**. |
 **tbl_group** | String 24 characters | Unique UPPERCASE identifiers used as name of table group. It must begin with an alphabetic character, and contain only alphanumerics and underscores. |
 **delete_tstamp** | Datetime with microsecond precision | The moment this row was deleted or the moment that an update was done (the new version of the row is inserted with the same value in its **insert_tstamp** column). |


#### HVR_COLUMN


Table containing all the columns in each replicated tables.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **chn_name** | String 12 characters | Name of the channel. |
 **tbl_name** | String 124 characters | Name of the table. |
 **col_name** | String 128 characters | If the column has a different name in different databases, this value can be overridden with parameter **[BaseName](https://fivetran.com/docs/hvr6/action-reference/columnproperties#basename)** in**** action **[ColumnProperties](https://fivetran.com/docs/hvr6/action-reference/columnproperties)**. |
 **insert_tstamp** | Datetime with microsecond precision | The moment this row was inserted or the moment that an update was done (the previous row has this same value assigned into its **delete_tstamp** column). |
 **col_sequence** | number | Sequence of column in the table. |
 **col_key** | number | 
Value **0** indicates column not in the replication key. Other (higher) values indicate the order of this column in the replication key.

If no columns are explicitly marked as replication key columns, then either the table is assumed to allow duplicate rows, or (if action **[TableProperties](https://fivetran.com/docs/hvr6/action-reference/tableproperties)** with parameter **[NoDuplicateRows](https://fivetran.com/docs/hvr6/action-reference/tableproperties#noduplicaterows)** is defined) all columns of the table form the implicit replication key. |
 **col_distrib_key** | number | Value **0** indicates column not in the distribution key. Other (higher) values indicate the order of this column in the distribution key. |
 **col_datatype** | String 128 characters | Data type of column. Any data type such as **varchar**, **char**, **integer**, **number**, **date**, etc. can be used here. |
 **col_attributes** | String 256 characters | JSON column containing data type attributes such as nullability and string length. |
 **delete_tstamp** | Datetime with microsecond precision | The moment this row was deleted or the moment that an update was done (the new version of the row is inserted with the same value in its **insert_tstamp** column). |


#### HVR_ACTION


Table containing the list of replication actions and their parameters.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **chn_name** | String 12 characters | 
Name of the channel(s) affected by this action.

- ***** (asterisk) indicates all channels are affected.

 |
 **loc_scope** | String 24 characters | 
Location scope for the action. Indicates which locations are affected by this action.

Possible values are:

- ***** (asterisk) indicates all locations
- The name of a location group in the channel. This will always be an UPPERCASE identifier.
- The name of a specific location in the channel. This will always be a lowercase identifier.

 |
 **tbl_scope** | String 124 characters | 
Table scope for the action. Indicates which tables in the channel are affected by this action.

Possible values are:

- ***** (asterisk) indicates all tables in the channel.
- The name of a table group in the channel. This will always be an UPPERCASE identifier.
- The name of a specific table in the channel. This will always be a lowercase identifier.

 |
 **act_name** | String 24 characters | Action name. See also section [Action Reference](https://fivetran.com/docs/hvr6/action-reference) for available actions and their parameters. |
 **act_parameters_hash** | String 40 characters | Internal column used to index the rows of this **HVR_ACTION** table. Many rows may differ only by their value in the **act_parameters** column, which cannot be indexed because it is a long string object. |
 **insert_tstamp** | Datetime with microsecond precision | The moment this row was inserted or the moment that an update was done (the previous row has this same value assigned into its **delete_tstamp** column). |
 **act_parameters** | Long string object | JSON column containing action parameters. |
 **delete_tstamp** | Datetime with microsecond precision | The moment this row was deleted or the moment that an update was done (the new version of the row is inserted with the same value in its **insert_tstamp** column). |


### Run-Time Tables


This group of repository tables contains information that is generated during runtime, which includes events, jobs, statistics etc.

Following are the runtime tables:

#### HVR_EVENT


Table containing events. Each change made in the replication system is recorded as an event. For more information about events, see section [Events](https://fivetran.com/docs/hvr6/getting-started/concepts/events).

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **ev_id_tstamp** | Datetime with microsecond precision | Unique ID of this event. This is the moment when the event was created. This timestamp is generated using **[HVR_COUNTER](#hvrcounter)**. |
 **user_name** | String 128 characters | Name of the user that created this event. |
 **ev_type** | String 64 characters | Name of this event. Some events are just audit records of system changes (e.g. **Catalog Change**) while other events (e.g. **Refresh** or **Compare**) are activities which could run for some time. |
 **ev_descrip** | String 1024 characters | Description of this event. |
 **chn_name** | String 12 characters | Name of the channel affected by this event. |
 **loc_name** | String 12 characters | Name of location associated to this result. |
 **loc_name_2** | String 12 characters | Name of second location associated to this result. |
 **job_name** | String 64 characters | Name of the job associated to this event. |
 **ev_state** | String 10 characters | State of this event, either **PENDING**, **DONE** or **FAILED**. |
 **ev_num_retries** | number | Number of times event has been restarted. |
 **ev_response** | String 128 characters | Summary of the activity in this event; either written when the event finishes successfully or containing the error that caused it to fail or be cancelled. |
 **ev_start_tstamp** | Datetime with microsecond precision | The moment when event was last started (updated on each retry). |
 **ev_finish_tstamp** | Datetime with microsecond precision | The moment when event finished. |
 **ev_body** | Long string object | Event body string in JSON. Contains arguments for this event. |
 **last_updated** | Datetime with microsecond precision | The moment this row was inserted (indicates the time when event was updated). |


#### HVR_EVENT_RESULT


Table containing results from job events such as activate event, refresh event, and compare event.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **ev_id_tstamp** | Datetime with microsecond precision | Event ID of parent event (from **[HVR_EVENT](#hvrevent)**). |
 **tbl_name** | String 128 characters | Name of table associated to this result. |
 **res_name** | String 64 characters | Name of this result. |
 **res_value** | Long string object | Value of this result. |
 **last_updated** | Datetime with microsecond precision | The moment this row was inserted (indicates the time when event result was updated). |


#### HVR_JOB


Table containing jobs. For more information about jobs, see [Jobs](https://fivetran.com/docs/hvr6/getting-started/concepts/jobs).

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **job_name** | String 64 characters | Unique name of job. Case sensitive and conventionally composed of lowercase identifiers (alphanumerics and underscores) separated by hyphens. Examples: **foo** and **foo–bar**. |
 **pos_x** | number | X coordinate of job in job space. The coordinates of a job determines within which job groups it is contained and therefore which attributes apply. |
 **pos_y** | number | Y coordinate of job in job space. The coordinates of a job determines within which job groups it is contained and therefore which attributes apply. |
 **obj_owner** | String 24 characters | Used for authorization: only the Scheduler administrator and a job's owner may change a jobs attributes or attributes. |
 **job_state** | String 10 characters | Valid values for cyclic jobs are **PENDING**, **RUNNING**, **HANGING**, **ALERTING**, **FAILED**, **RETRY** and **SUSPEND** are also allowed. |
 **job_period** | String 10 characters | Mandatory column indicating the period in which the job is currently operating. The job's period affects which job group attributes are effective. The typical value is **normal**. |
 **job_trigger** | number | 0 indicates job is not triggered, 1 means it may run if successful, and 2 means it may run even if it is unsuccessful. |
 **job_cyclic** | number | 0 indicates job is acyclic, and will disappear after running; 1 indicates job is cyclic. |
 **job_touched_user** | Datetime with microsecond precision | Last time user or **[hvractivate](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvractivate)** changed job tuple. |
 **job_touched_server** | Datetime with microsecond precision | Last time Scheduler changed job tuple. |
 **job_last_run_begin** | Datetime with microsecond precision | Last time job was started. |
 **job_last_run_end** | Datetime with microsecond precision | Last time job finished running. |
 **job_num_runs** | number | Number of times job has successfully run. |
 **job_num_retries** | number | Number of retries job has performed since last time job successfully ran. Reset to zero after job runs successfully. |


#### HVR_JOB_ATTRIBUTE


Table containing scheduler attributes for specific job. For more information, see section Scheduler Attributes in Scheduler.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **job_name** | String 64 characters | Name of object on which attribute is defined. |
 **attr_name** | String 24 characters | Type of attribute. Case insensitive. |
 **attr_arg1** | String 200 characters | Some attribute types require one or more arguments, which is supplied in this column. |
 **attr_arg2** | String 200 characters | Some attribute types require one or more arguments, which is supplied in this column. |


#### HVR_JOB_GROUP


Table containing groups of jobs, which are associated with individual jobs using abstract X, Y coordinate system. The purpose of job groups is to associate scheduler attributes efficiently.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **jobgrp_name** | String 64 characters | Job group name. Case sensitive and conventionally composed of UPPERCASE identifiers (alphanumerics and underscores) separated by hyphens. Examples: **MYCHANNEL** and **MYCHANNEL-CAP**. |
 **pos_x_min** | number | This forms coordinates of the job group's box in job space. Objects such as jobs, resources and other job groups whose coordinates fall within this box are contained by this job group and are affected by its attributes. |
 **pos_x_max** | number | This forms coordinates of the job group's box in job space. Objects such as jobs, resources and other job groups whose coordinates fall within this box are contained by this job group and are affected by its attributes. |
 **pos_y_min** | number | This forms coordinates of the job group's box in job space. Objects such as jobs, resources and other job groups whose coordinates fall within this box are contained by this job group and are affected by its attributes. |
 **pos_y_max** | number | This forms coordinates of the job group's box in job space. Objects such as jobs, resources and other job groups whose coordinates fall within this box are contained by this job group and are affected by its attributes. |
 **obj_owner** | String 24 characters | Owner of a job group. Only a job group's owner and the Scheduler administrator can make changes its coordinates or attributes. |


#### HVR_JOB_GROUP_ATTRIBUTE


Table containing scheduler attributes for specific job group. For more information, see section Scheduler Attributes in Scheduler.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **jobgrp_name** | String 64 characters | Name of the job group on which attribute is defined. This also affect objects contained in job group. |
 **attr_name** | String 24 characters | Name of the attribute, which also indicate its type. Case insensitive. |
 **attr_arg1** | String 200 characters | Some attribute types require one or more arguments, which is supplied in this column. |
 **attr_arg2** | String 200 characters | Some attribute types require one or more arguments, which is supplied in this column. |
 **attr_period** | String 10 characters | Period for which this attribute is applicable. It must be a lowercase identifier or an asterisks '*'. |


#### HVR_STATS


Table containing statistics gathered by special job [hvrstats](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrstats) from the replication log files and from the contents of the HVR_CONFIG directory.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **hist_time_gran** | number | 
Granularity in minutes. Possible values are:

- **0** : Current granularity (not historical).
- **1** : Minute time granularity.
- **10** : Ten (10) minutes granularity.
- **60** : Hour granularity.
- **1440** : Day granularity.

 |
 **hist_time** | Timestamp in number | Start time of measurement period as seconds since 1 Jan 1970. The length of the measurement period is equal to the value of **hist_time_gran** in minutes. |
 **chn_name** | String 12 characters | Name of the channel. An asterisk '*' means the value (sum, average, min or max) for all channels. |
 **loc_name** | String 12 characters | Name of the location. An asterisk '*' means the value (sum, average, min or max) for all locations. |
 **tbl_name** | String 124 characters | Name of the table. An asterisk '*' means the value (sum, average, min or max) for all tables. |
 **metric_name** | String 64 characters | Name of the metric collected during a capture or integrate cycle. Min and Max values are provided for some metrics to denote the variance of a metric during a cycle. |
 **metric_value** | String 1024 characters | Value of metric. |
 **metric_gatherer** | String 4 characters | Name of the subsystem that gathered the metric. Values can be **logs** (metric was gathered from the HVR log files) or **glob** (metric was gathered from inspecting the router files). |
 **metric_scope** | String 3 characters | 
Scope of the current metric.

First letter is '*****' if **chn_name** is '*****' and '**c**' otherwise.

Second letter is '*****' if **loc_name** is '*****' and '**l**' otherwise.

Third letter is '*****' if **tbl_name** is '*****' and '**t**' otherwise. |
 **last_updated** | Timestamp in number | The moment this row was inserted or last updated. The value is in seconds since 1 Jan 1970. |


### Other Tables


This group of repository tables contains information about other internal tables of HVR.

#### HVR_COUNTER


Internal table containing counters used to perform locking, track caching, and time dimensions of other tables.

 Column | Data type | Description |
 **hub_name** | String 32 characters | Name of the hub. |
 **counter_name** | String 64 characters | Name of the internal time counter. |
 **counter_tstamp** | Datetime with microsecond precision | Value of the internal time counter. |
 **counter_last_node** | String 128 characters | Name of the host on which the process which last changed this counter was running. |

