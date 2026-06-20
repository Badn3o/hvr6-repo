# Pricing for HVR

**Source:** https://fivetran.com/docs/hvr6/getting-started/pricing

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/pricing/index.md)

# Pricing for HVR


Our pricing model is based on usage. You are charged based on the amount of data replicated or consumed by a target (destination). Fivetran calculates your consumption (usage) based on the number of [monthly active rows (MAR)](https://fivetran.com/docs/core-concepts/usage-based-pricing#monthlyactiverows) across all source and target locations within your HVR Hub System(s). MAR is the number of distinct primary keys synced or replicated from a source location to a target location in a given calendar month. For more information, see our [pricing documentation](https://fivetran.com/docs/core-concepts/usage-based-pricing).

Once you [register your hub system](https://fivetran.com/docs/hvr6/getting-started/pricing#registerhvrwithfivetran) with a Fivetran account, HVR securely sends back metadata to Fivetran regarding your usage. Fivetran calculates MAR for your HVR Hub System(s) based on this metadata. The following pricing rules apply:

- You can register multiple hub systems to your Fivetran account.
- If you are syncing data from one source to multiple destinations, we count MAR for each destination.
- We calculate MAR the same way across all cloud and on-premise connections.
- You can share a single budget for both Fivetran and HVR.
- All our MAR calculations are in the UTC time zone.


> **Note:** 
Fivetran offers a single pricing plan for HVR - [Business Critical](#businesscritical). In this plan, Fivetran automatically manages consumption tracking and license renewal.


---

## Business Critical


The [Business Critical](https://fivetran.com/docs/core-concepts/usage-based-pricing) plan allows HVR to be deployed on-premise. In this plan, the HVR Hub System must be registered with a Fivetran account and connected to the Fivetran server to automatically send the consumption data and receive licenses. Once registered, HVR automatically transmits encrypted consumption data to Fivetran, where it is securely stored on AWS S3.

> **Important:** 
If the Fivetran account registration is deleted from a hub system, HVR immediately stops sending consumption data to Fivetran, and the automatic license renewal stops (the license expires after seven days).


---

## Understand HVR Usage Data


Each month, your consumption/usage is calculated based on the number of MAR across all source (connector) and target (destination) locations in your account. The consumption data (metadata) used to calculate MAR for your HVR Hub System(s) is sent to Fivetran in two files:

- [**MAR Data**](#mardata)
- [**Hub Snapshot**](#hubsnapshot)


HVR sends the **MAR Data** file to Fivetran hourly for usage tracking, and Fivetran returns a new seven-day license key each day. In addition, HVR sends the **Hub Snapshot** file every 30 days.

> **Note:** 
The MAR data or snapshot file sent to Fivetran does not contain any data from replicated tables or any [confidential or secret](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/classification-of-data) data.



### MAR Data


The MAR data that HVR sends to Fivetran contains information such as Hub Name, Hub ID, Hub Description, Hub Server URL, Channel Name, Location Name, Location Description, Location Type, Table Name, Base Name, Refresh Events (including the timestamp and metadata), hashes of primary keys changed, and HLL records for [Integrate](https://fivetran.com/docs/hvr6/action-reference/integrate) and [Refresh](https://fivetran.com/docs/hvr6/getting-started/concepts/refresh) jobs.
 Column in MAR File | Description |
 **month** | Month and year for which the MAR data is applicable. |
 **hub_name** | Name of the hub. |
 **hub_id** | Unique identifier of the HVR Hub System. |
 **chn_name** | Name of the channel. |
 **src_loc_name** | Name of the source location. |
 **tgt_loc_name** | Name of the target location. |
 **mar** | Total sum of MAR for the month. |
 **mar_daily** | List of incremental MAR values per day. |
 **src_loc_type** | Type (e.g. Oracle, SQL Server) of source location. |
 **tgt_loc_type** | Type (e.g. Oracle, SQL Server) of target location. |
 **table_count_estimate** | Estimate of the number of tables seen per source-target connection in a channel. The estimate has the same error rate as regular MAR, so usually +- 2%. |
 **integ_mar_signature** | Serialized form of the raw internal HLL structure which is used to track MAR data. |
 **refr_mar_signature** | Serialized form of the raw internal HLL structure which is used to track MAR data. |

#### HVR Connections


An HVR connection is defined by a unique combination of the following:

- Registration ID
- Hub ID
- Source location name
- Target location name
- Channel name


Fivetran offers a [14-day free trial](https://fivetran.com/docs/getting-started/free-trials#connectiontrial) for new connections based on HVR connectors. Fivetran starts a free trial for every new HVR connection with the same hub ID, source location name, and target location name.

#### Troubleshooting Window


Fivetran offers a troubleshooting window for free table refreshes. This window lasts 5 days, starting from the day you first refresh a table in a given month. All subsequent refreshes outside this window count toward paid MAR.

> **Note:** 
If you have [enhanced re-sync detection](#improvedresyncdetection) enabled (available since HVR version 6.2.0/13), the 5-day troubleshooting window is not required. Re-sync detection more precisely identifies data changes and eliminates the need to limit free refreshes.


#### Storage Requirements for MAR


HVR stores MAR data locally on the Hub machine in hourly buckets per table before sending it to Fivetran. These files use a data structure called HyperLogLog (HLL) to track MAR. HVR uses hash values from primary keys to update these structures, which are retained for up to one month.

> **Important:** 
Original primary keys cannot be retrieved from the HLL data structure. HVR does not store the primary keys directly, but instead uses their hashes to update this structure. The hashes are irreversible and can not be retrieved.


Each data structure is approximately 2 KB. The amount of data stored daily is **24 (hours) * 2 (KB) * number of active tables**, so the disk space needed per day is **48 (KB) * number of active tables**. The total storage required for MAR data depends on the number of active tables being replicated.

We recommend allocating about a week's worth of storage capacity on the HVR Hub machine for storing MAR data. Typically, only one or two days of data is stored because HVR automatically purges MAR data one day after transmission. If required, you can disable automatic purging using the repository property [**Metering_Purge_Frequency**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#meteringpurgefrequency).

#### Viewing MAR Data


To view the hourly MAR data sent to Fivetran:

- 
Execute the [**hvrlicense**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlicense) command in the CLI:
hvrlicense -m <em>marfilename</em> -B now-1h

- 
Open the file in a text editor to view the data.



### Hub Snapshot


The hub snapshot includes information about the system configuration or usage such as Channel definitions, Events, Statistics, and Job state.

HVR encrypts and sends a usage snapshot for each hub to Fivetran every 30 days. Before transmission, the snapshot file is temporarily stored on the disk of the hub machine. HVR automatically purges it a day after it is sent to Fivetran.

The hub snapshot file includes:

- one week of events
- one week of statistics
- channel definitions
- job state


> **Important:** 
The snapshot does not contain log files, history, or transaction files.


To manually generate a hub snapshot (in ZIP file format), use the [**hvrsnapshotsave**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrsnapshotsave) command in the CLI:
hvrsnapshotsave -r "Usage snapshot for account_id <em>my_account_id</em>" -e now-1w -s now-1w -l none -t none -V redact <em>hub_name</em> <em>snapshot_filename</em>.zip

---

## Register HVR with Fivetran


Follow these instructions to integrate your HVR Hub System with Fivetran so that you can use Fivetran's pricing.

### Prerequisites


To integrate each of your HVR Hub System with Fivetran, you must:

- Enable outbound access from the web browser that you will use to register the HVR Hub System to the IP address 35.236.237.87 ([fivetran.com](https://www.fivetran.com/)).
- Enable outbound access from the system running the HVR Hub Server to the following IP addresses on port **443** (required for sending consumption data to the Fivetran server):
- 34.110.137.135
- 34.120.211.189


- Register your HVR Hub System. You must create a Fivetran account or log in to [fivetran.com](https://www.fivetran.com/) with an account Administrator role.
- If you are using proxy server to connect HVR Hub System with Fivetran, then ensure to configure the [proxy server setup](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/configuring-connection-via-proxy-server).


> **Important:** 
If you have multiple HVR Hub Systems, you must register each hub system individually.



The registration process differs for existing and new HVR users.

### Existing HVR Users


To start using the Fivetran pricing model on your HVR Hub System:

- 
Log in to the [HVR web UI](https://fivetran.com/docs/hvr6/user-interface).

- 
On the left navigation pane, click **System**.

- 
Click the ellipsis button and select [**Licensing**](https://fivetran.com/docs/hvr6/user-interface/system#licensing).

- 
Click **Register with Fivetran account**.

- 
On the Fivetran account setup form, enter your details and click **Sign up**.

> **Note:** 
If you already have a Fivetran account, click **Sign in here**.


- 
Once you log in to your Fivetran account, click **Continue to HVR**.

The registration process is complete, and you are redirected to the HVR UI.



> **Note:** 
Once you complete the registration, the HVR Licensing section displays the new Fivetran account with a VALID status. To view the HVR registration logs, click **Registration ID**.


### New HVR Users


If you are a new HVR user or a Fivetran user on the [Business Critical plan](https://www.fivetran.com/pricing/features):

- Download HVR from the [Fivetran dashboard](https://fivetran.com/dashboard/account/general/account): go to **Account Settings** > **Downloads**, scroll down to the **Fivetran (HVR) Downloads** section, and click the required version to begin downloading.
- To get started with HVR, see the [Getting Started](https://fivetran.com/docs/hvr6/getting-started) documentation for installation and configuration instructions.


---

## Manage Fivetran License


Licenses are provided during the registration process. You can manage your license from the **Licensing** page of your HVR deployment, where you can delete the license or remove the Fivetran registration.

The Fivetran registration provides access to HVR via an automatically refreshing license key. If you remove your Fivetran registration before your contract ends, HVR loses access after seven days. Your access to HVR ends at the end of your subscription term.

For more information, see [Licensing](https://fivetran.com/docs/hvr6/getting-started/licensing).

---

## Pricing Plan Updates


We introduced the following pricing updates as of April 24, 2025:

- Introduced an enhanced re-sync detection mechanism that more precisely determines data changes. For more information, see [Improved Re-sync Detection](#improvedresyncdetection).
- Moved away from account-level tiering to channel-level usage tiers. The cost of HVR per monthly active row decreases for a single channel as your usage grows for that particular channel. Previously, usage was calculated on an account level.
- Introduced discounts for annual contracts based on commitment levels. Once you have upgraded your HVR Hub and Agent to version 6.2.0/14 or newer and we have one month of usage data, see the [Pricing Estimator](https://fivetran.com/pricing-estimator) for an estimate of your annual discount. The discount applies once you renew your contract.
- Deprecated the **Private Deployment** pricing plan. All HVR accounts on the **Private Deployment** plan must transition to the **Business Critical** or other plans upon contract renewal.


We automatically applied the updated pricing to HVR accounts on a pay-as-you-go plan on May 1, 2025. HVR accounts on annual plans transition to the updated pricing upon contract renewal.

### Improved Re-sync Detection


The enhanced re-sync detection mechanism more accurately identifies data changes, eliminating the need for free refreshes within the five-day troubleshooting window. You are charged only for changed rows, regardless of when the change occurs.

To enable re-sync detection on your account:

- Renew your annual contract
- [Upgrade your HVR Hub and HVR Agent](https://fivetran.com/docs/hvr6/install-and-upgrade/upgrade) to the version applicable to your current release:
- If you are using 6.1.0, upgrade to 6.1.0/76 or newer.
- If you are using 6.2.0, upgrade to 6.2.0/14 or newer.
- If you are using 6.2.5, upgrade to 6.2.5/5 or newer.




You must complete both actions to benefit from re-sync detection.

You can transition to the updated pricing without upgrading your Hub and Agent, but the improved re-sync detection mechanism won't be enabled. Without re-sync detection, you will have to rely on the five-day troubleshooting window for free refreshes.

If you have an active contract, you can upgrade your HVR Hub and Agent without transitioning to the updated pricing. After the upgrade, once Fivetran has collected one month of usage data, our [Pricing Estimator](https://fivetran.com/pricing-estimator) shows your estimated usage with re-sync detection, helping you make an informed renewal decision.

Re-sync detection stores up to 50 MB of sample data per replicated table on the system hosting the HVR Hub System. Samples are stored in the **HVR_CONFIG/metering** directory for every channel containing the table, per source/target location pair.

> **Important:** 
Re-sync detection is not available for HVR when using [SAP HANA as the Source](https://fivetran.com/docs/hvr6/requirements/source-and-target-requirements/sap-hana-requirements/sap-hana-as-source).


