# Getting Started - HVR 6 | Fivetran Documentation

> **Source**: https://fivetran.com/docs/hvr6/getting-started
> **Extracted**: June 20, 2026

---

## Overview

Fivetran HVR is a software product for enterprise-level replication of database and file management systems. With its reliable and secure technology, HVR can achieve a combination of light footprint, low latency, and high throughput that cannot be found anywhere else. HVR supports a distributed architecture for database and file replication in between a [large number](/docs/hvr6/supported-platforms) of Database Management Systems (DBMSs). It is a comprehensive software system with various modules for running data replication. This includes:

- **[Refresh](/docs/hvr6/getting-started/concepts/refresh)** mechanism for initial loading of data from source to target;
- **[Capture](/docs/hvr6/action-reference/capture)** process that continuously acquires all the changes in the source location;
- **[Integrate](/docs/hvr6/action-reference/integrate)** process that applies the changes to the target location;
- **[Compare](/docs/hvr6/getting-started/concepts/compare)** feature that compares the source and target locations to ensure that the data is in sync.

---

## STEP 1: Learn

HVR is a large system with numerous capacities. Ensure to learn basic terms and concepts used throughout the HVR service and documentation.

### Learn Topics

- [Architecture](/docs/hvr6/getting-started/concepts/architecture)
- [HVR Agent](/docs/hvr6/getting-started/concepts/agent)
- [Refresh](/docs/hvr6/getting-started/concepts/refresh)
- [Replication Topologies](/docs/hvr6/getting-started/concepts/replication-topologies)
- [Activate Replication](/docs/hvr6/getting-started/concepts/channel/components-for-activating-replication)
- [Compare](/docs/hvr6/getting-started/concepts/compare)

To learn about other HVR concepts, see the [Concepts](/docs/hvr6/getting-started/concepts) section.

Additionally, check our [Quick Start Guide](/docs/hvr6/getting-started/quick-start-guide), a comprehensive resource designed to assist users in gaining a preview and practical understanding of HVR. This guide offers a hands-on experience, directing users through the configuration and execution of the HVR replication channel within a preconfigured environment.

---

## STEP 2: Install and Configure

Learn how to set up and configure your HVR installation.

1. [Installing HVR Hub](/docs/hvr6/install-and-upgrade/install/hub)
2. [Initial Setup of HVR Hub](/docs/hvr6/install-and-upgrade/configure/hub)
3. [Installing HVR Agent](/docs/hvr6/install-and-upgrade/install/agent)
4. [Configuring HVR Agent](/docs/hvr6/install-and-upgrade/configure/agent)

---

## STEP 3: Operate

Learn where to start and how to manage replication using HVR.

1. Create [Channels](/docs/hvr6/user-interface/channels/creating-channel) and [Locations](/docs/hvr6/user-interface/locations/creating-location)
2. [Activate and Run Replication](/docs/hvr6/user-interface/channels/activating-replication)
3. [Perform Initial Load using Refresh](/docs/hvr6/user-interface/channels/refreshing-data)
4. [Verify Replication using Compare](/docs/hvr6/user-interface/channels/comparing-data)

---

# Sub-Section: Document Conventions

> **Source**: https://fivetran.com/docs/hvr6/getting-started/document-conventions

This section explains the conventions used in Fivetran HVR documentation.

## Text Formatting Conventions

| CONVENTION | DESCRIPTION |
|---|---|
| **bold** | Indicates computer terms that are fixed, field or button name in UI, keywords, [action name](/docs/hvr6/action-reference), action parameters, [commands](/docs/hvr6/command-line-interface), command parameters, file names, directory path. |
| *italics* | Indicate computer terms that are variables or placeholders requiring user-supplied values. For example, in a directory path such as `HVR_CONFIG/hubs/myhub`, the word *myhub* is in italics indicating that it is a variable and should be replaced with the appropriate value. |
| `[ ]` | Text inside square brackets indicates optional entries. |
| `\|` | The vertical line or pipe sign separates a mutually exclusive set of options. |
| `SELECT * FROM table1;` | Code examples, syntax, and commands recognized by the system are displayed in code blocks using a monospaced font. |
| `hvrhubserver -acs` | Code examples or SQL statements embedded inside paragraphs are displayed in a monospaced font with a gray background. |

## Menu Selection Conventions

Menu selection sequences are displayed in bold and each menu item is divided by the **▶** symbol. For example, select **Tools ▶ Data ▶ Entity ▶ Organization**.

## Environment Variables

All occurrences of `HVR_HOME`, `HVR_CONFIG`, and `HVR_TMP` in paragraphs should be treated as environment variables:

- **Linux/Unix**: `$hvr_config/logs`
- **Windows**: `%hvr_config%/logs`

## File/Directory Path Conventions

Many path names follow Unix conventions, where a forward slash `/` is used as a file path delimiter. On Microsoft Windows, this corresponds to a backward slash `\`. HVR automatically converts between forward and backward slashes as needed.

## Callouts

The documentation uses the following callouts:

- **Note**: Provides additional information that enhances understanding but is not critical to functionality.
- **Important**: Highlights crucial information that the user must be aware of to avoid errors or issues.
- **Tip**: Offers useful suggestions, best practices, or shortcuts.
- **Warning**: Alerts about potential risks, data loss, security issues, or irreversible actions.

## Labels

- **Applies-to**: Indicates functionality supported only on specific systems (e.g., Oracle, Ingres, SQL Server, Linux, Windows).
- **Available Since**: Indicates the HVR version in which a feature was introduced. Example: Since v6.2.0/10
- **Default**: Indicates the default value for a field, property, or command.

## Icons

| ICON | DESCRIPTION |
|---|---|
|  | Indicates an HVR Agent process or machine. |
|  | Indicates an HVR Agent proxy process or HVR Agent proxy machine or a file proxy. |
|  | Indicates a channel. |
|  | Indicates a database location or location whose type (db/file/kafka) is unknown or hub repository or hive database for external tables. |
|  | Indicates a file location or directory or temporary file. |
|  | Indicates a Kafka location. |
|  | Indicates a location group. |
|  | Indicates a table. |
|  | Indicates a table group. |
|  | Indicates a capture job. |
|  | Indicates an integrate job. |
|  | Indicates the direction of replication. In the HVR UI, the color of this icon changes to blue when the channel is activated and to red if a job fails or the latency threshold is exceeded. |

---

# Sub-Section: Pricing for HVR

> **Source**: https://fivetran.com/docs/hvr6/getting-started/pricing

## Pricing Model

The pricing model is based on usage. You are charged based on the amount of data replicated or consumed by a target (destination). Fivetran calculates consumption based on the number of **monthly active rows (MAR)** across all source and target locations within your HVR Hub System(s). MAR is the number of distinct primary keys synced or replicated from a source location to a target location in a given calendar month.

Once you register your hub system with a Fivetran account, HVR securely sends back metadata to Fivetran regarding your usage. The following pricing rules apply:

- You can register multiple hub systems to your Fivetran account.
- If you are syncing data from one source to multiple destinations, MAR is counted for each destination.
- MAR is calculated the same way across all cloud and on-premise connections.
- You can share a single budget for both Fivetran and HVR.
- All MAR calculations are in the UTC time zone.

## Business Critical Plan

Fivetran offers a single pricing plan for HVR - **Business Critical**. In this plan, Fivetran automatically manages consumption tracking and license renewal.

The Business Critical plan allows HVR to be deployed on-premise. The HVR Hub System must be registered with a Fivetran account and connected to the Fivetran server to automatically send the consumption data and receive licenses. Once registered, HVR automatically transmits encrypted consumption data to Fivetran, where it is securely stored on AWS S3.

If the Fivetran account registration is deleted from a hub system, HVR immediately stops sending consumption data to Fivetran, and the automatic license renewal stops (the license expires after seven days).

## Understand HVR Usage Data

### MAR Data

HVR sends the MAR Data file to Fivetran hourly for usage tracking, and Fivetran returns a new seven-day license key each day.

**Columns in MAR file:**

| COLUMN | DESCRIPTION |
|---|---|
| month | Month and year for which the MAR data is applicable. |
| hub_name | Name of the hub. |
| hub_id | Unique identifier of the HVR Hub System. |
| chn_name | Name of the channel. |
| src_loc_name | Name of the source location. |
| tgt_loc_name | Name of the target location. |
| mar | Total sum of MAR for the month. |
| mar_daily | List of incremental MAR values per day. |
| src_loc_type | Type (e.g. Oracle, SQL Server) of source location. |
| tgt_loc_type | Type (e.g. Oracle, SQL Server) of target location. |
| table_count_estimate | Estimate of the number of tables seen per source-target connection in a channel. |
| integ_mar_signature | Serialized form of the raw internal HLL structure for tracking MAR data. |
| refr_mar_signature | Serialized form of the raw internal HLL structure for tracking MAR data. |

### Hub Snapshot

HVR encrypts and sends a usage snapshot for each hub to Fivetran every 30 days. The hub snapshot file includes:

- One week of events
- One week of statistics
- Channel definitions
- Job state

The snapshot does not contain log files, history, or transaction files.

To manually generate a hub snapshot:

```bash
hvrsnapshotsave -r "Usage snapshot for account_id my_account_id" -e now-1w -s now-1w -l none -t none -V redact hub_name snapshot_filename.zip
```

### Viewing MAR Data

To view the hourly MAR data sent to Fivetran:

```bash
hvrlicense -m marfilename -B now-1h
```

## HVR Connections

An HVR connection is defined by a unique combination of: Registration ID, Hub ID, Source location name, Target location name, Channel name.

Fivetran offers a **14-day free trial** for new connections based on HVR connectors.

## Troubleshooting Window

Fivetran offers a **5-day troubleshooting window** for free table refreshes, starting from the day you first refresh a table in a given month. All subsequent refreshes outside this window count toward paid MAR.

If you have **enhanced re-sync detection** enabled (available since HVR version 6.2.0/13), the 5-day troubleshooting window is not required.

## Storage Requirements for MAR

HVR stores MAR data locally on the Hub machine in hourly buckets per table using HyperLogLog (HLL). Each data structure is approximately **2 KB**. Daily storage needed: **48 KB × number of active tables**.

Original primary keys cannot be retrieved from the HLL data structure - only irreversible hashes are used.

We recommend allocating about a week's worth of storage capacity on the HVR Hub machine. MAR data is automatically purged one day after transmission (configurable via `Metering_Purge_Frequency` repository property).

## Register HVR with Fivetran

### Prerequisites

- Enable outbound access from the web browser to IP address **35.236.237.87** (fivetran.com).
- Enable outbound access from the HVR Hub Server system to the following IP addresses on port **443**:
  - **34.110.137.135**
  - **34.120.211.189**
- Register your HVR Hub System with a Fivetran account (Administrator role).
- If using a proxy server, configure the proxy server setup.
- If you have multiple HVR Hub Systems, register each hub system individually.

### Existing HVR Users

1. Log in to the HVR web UI.
2. On the left navigation pane, click **System**.
3. Click the ellipsis button and select **Licensing**.
4. Click **Register with Fivetran account**.
5. Enter your details and click **Sign up** (or **Sign in here** if you already have an account).
6. Once logged in, click **Continue to HVR**.

### New HVR Users

1. Download HVR from the Fivetran dashboard: Account Settings > Downloads > Fivetran (HVR) Downloads section.
2. See the Getting Started documentation for installation and configuration instructions.

### Manage Fintran License

Licenses are provided during registration and automatically refresh. If you remove registration before your contract ends, HVR loses access after seven days.

## Pricing Plan Updates (April 24, 2025)

- Introduced **enhanced re-sync detection** mechanism for more precise data change identification.
- Moved from account-level tiering to **channel-level usage tiers**. Cost per MAR decreases for a single channel as usage grows.
- Introduced **discounts for annual contracts** based on commitment levels.
- **Deprecated the Private Deployment** pricing plan. All accounts must transition upon contract renewal.
- Updated pricing automatically applied on **May 1, 2025** for pay-as-you-go accounts. Annual plans transition upon renewal.

### Improved Re-sync Detection Upgrade Requirements

To enable re-sync detection:
1. Renew your annual contract
2. Upgrade HVR Hub and Agent:
   - 6.1.0 → 6.1.0/76 or newer
   - 6.2.0 → 6.2.0/14 or newer
   - 6.2.5 → 6.2.5/5 or newer

Re-sync detection stores up to **50 MB** of sample data per replicated table in `HVR_CONFIG/metering/`. Not available for SAP HANA as source.

---

# Sub-Section: Licensing for HVR

> **Source**: https://fivetran.com/docs/hvr6/getting-started/licensing

You must have a valid license to use Fivetran HVR for data replication. The license includes details such as the issue and expiry dates, and the source/target location types that can be used for replication.

Fivetran uses a **consumption-based** licensing model for HVR, available through the **Business Critical** plan. The license is automatically supplied to the HVR Hub System as part of this model.

> **Deprecated**: The **Private Deployment** pricing plan and **Usage-based Subscription** licensing model were deprecated as of March 1, 2025. Accounts must transition to **Business Critical** or other available plans upon contract renewal.

## Consumption-based Licensing

**Available Since**: v6.1.0/3

In this licensing model, you must register the HVR Hub System with the Fivetran server to acquire a license.

- The license is valid for **7 days** and is automatically renewed daily, with issue and expiry dates incremented by one day each time.
- Example: Registered on March 10th → issue date March 10th, expiry March 17th. On March 11th → issue date March 11th, expiry March 18th.

### Registration Methods

**For newly installed HVR Hub System:**

- **Browser-based**: See "Setting up HVR Hub from Browser"
- **CLI-based**: See "Setting up HVR Hub from CLI"

**For existing HVR Hub System:**

- **HVR UI**: Navigate to **System ▶ Licensing**
- **CLI**: Use the `hvrlicense` command

> For information about consumption-based licensing in an HVR High-Availability environment, see the dedicated documentation.

---

# Sub-Section: Release Life Cycle - HVR 6

> **Source**: https://fivetran.com/docs/hvr6/getting-started/release-life-cycle

This page contains detailed information on the support duration for Fivetran HVR 6 releases, version compatibility, supported operating system releases, and supported DBMS releases.

> **HVR 6 is not compatible with HVR 5.**

## Support Duration for HVR 6 Releases

- Major HVR 6 releases (e.g., HVR 6.1.0) are supported for **3 years** from their General Availability (GA) release date.
- Fivetran typically releases a new major version every **12-18 months**.
- Early Adopter (EA) releases (e.g., HVR 6.1.5) and patch releases (e.g., HVR 6.1.0/40 or 6.1.0/43.1) do **not** extend the GA support window.

### Release Support Status

| RELEASE | GA RELEASE DATE | END OF REGULAR SUPPORT | SUPPORT STATUS |
|---|---|---|---|
| 6.1 | 2021-12-03 | 2026-01-31 | Support Ended |
| 6.2 | 2024-09-25 | 2027-09-30 | Regular |
| 6.3 | 2025-12-11 | 2028-12-31 | Regular |

## Version Compatibility

- HVR 6 is **not compatible** with HVR versions 5.x and 4.x.
- HVR versions are 'network compatible' with the two previous major versions but not with versions that have a different initial number. (e.g., HVR 6.1 is network-compatible with 6.2 and 6.3, but not with HVR 5.7.)
- When using a mix of HVR versions, each bug fix or feature is only effective if the correct installation/machine is upgraded. Check release notes at `HVR_HOME/hvr.rel` for details.

## Supported Operating System Releases

- For the list of supported OS versions, see [Supported Platforms](/docs/hvr6/supported-platforms) or the HVR release notes.
- Support for an OS continues until the OS supplier ends its "mainstream support".
- After mainstream support ends: status changes from **Regular** → **Sunset**.
- Customers may request **Extended** support instead of Sunset.
- HVR supports Linux based on a minimal **glibc version of 2.12**.

## Supported DBMS Releases

- For the list of supported DBMS versions, see [Supported Platforms](/docs/hvr6/supported-platforms) or the HVR release notes.
- Subsequent major DBMS versions are not automatically supported but may be recertified after QA testing.
- Patches to a supported DBMS version are automatically supported (no recertification at patch level).
- Support for a DBMS version continues at least until the DBMS supplier ends its "mainstream support".
- After mainstream support ends: **Regular** → **Sunset** (or **Extended** upon request).

---

# Sub-Section: Concepts

> **Source**: https://fivetran.com/docs/hvr6/getting-started/concepts

This section describes essential Fivetran HVR concepts, such as location, channel, hub, agent, scheduler, jobs, events, actions, etc. Here you can find information about the compare and refresh functionality in HVR. The section also describes HVR architecture in terms of the replication process, network connectivity, and security.

## Topics

- Architecture
- Replication Topologies
- Licensing
- Location
- HVR Agent
- Scheduler
- Slicing
- Channel
- Components for Activating Replication
- Keys
- Table Groups
- Table Name and Base Name
- Refresh
- Compare
- Refresh and Compare Contexts
- Jobs
- Events
- Security Architecture
- User Authentication
- User Permissions
- Hub System Encryption Wallet
- Classification of Data
- Environment Variables
- Maintenance and Monitoring

---

# Sub-Section: Quick Start Guide

> **Source**: https://fivetran.com/docs/hvr6/getting-started/quick-start-guide

The aim of this quick start guide is to help you achieve four primary objectives:

1. Gain a preview and hands-on experience with Fivetran HVR.
2. Deploy your first live replication flow using HVR.
3. Validate data to ensure systems are in sync.
4. Learn about efficient, high-volume data replication using log-based Change Data Capture (CDC).

## HVR Distributed Architecture

The architecture of HVR is modular and flexible, leveraging HVR Agent(s) for optimum efficiency. HVR Agent (HVA) is an installation of HVR software that acts on instructions from another HVR installation known as a **hub**.

Three key reasons to use agents:

### Performance
- Low-latency access to data endpoints and transaction log files for log-based CDC.
- Compressed and optimized data transfer methods.
- Minimized bandwidth requirements, reducing sensitivity to high latency (crucial for WAN transfers).

### Scalability
- Agents serve as units of scalability for parallelization.
- A single hub can manage numerous data flows from a unified console.

### Security
- Unified authentication capabilities with rich security features.
- Communication secured through encryption using **TLS 1.3**.

All HVR capabilities (refresh, capture/integrate, compare) fully leverage the distributed architecture.

HVR uses a **hub server** which can host one or more hubs. The hub server must connect to a **repository database** to store metadata. The hub server runs an HTTP(S) listener. Users can interact through:
- Web browser user interface
- Command-line interface (CLI)
- REST APIs

All interactions are recorded as events for change tracking and regulatory compliance.

## Prerequisites

This guide demonstrates replicating data from an **on-premises Oracle system** (source) to a **cloud-hosted Snowflake instance** (target).

### Assumptions completed:

1. Source schema with tables for replication.
2. Access privileges and configuration for Oracle (source) and Snowflake (target).
3. HVR Hub installed, configured, and running.
4. HVR Agent installed and configured on the source machine.

## Setup Steps

This guide primarily focuses on the web UI. The same tasks can be accomplished using the CLI.

### Login
1. Enter user credentials in the login dialog and click **Log in**.

### Create Channel
2. On the Start page, click **Create New Channel**.
3. The channel creation workflow consists of **five steps**:

#### Step 1: Select Channel Type
- Specify the channel name and optionally a description.
- Select **One to One** channel type (topology defining data flow between source and target).

#### Step 2: Select Locations

**Source Location (Oracle):**

1. Click **Create New Location** under Source Location.
2. Click the **Oracle** logo.
3. Select connection type: **Connect via High-Volume Agent**.
4. Enter agent connection details:
   - **AGENT HOST**: Hostname or IP of the HVR Agent server.
   - **AGENT PORT**: Port number (default: 4343).
5. Click **Test Agent Connection**.
6. Click **Confirm Connection Method**.
7. Configure Oracle Location Connection:
   - **ORACLE_HOME**: Directory path where Oracle is installed.
   - **SID**: Unique name identifier of the Oracle instance.
   - **USER**: Username for connecting to Oracle.
   - **PASSWORD**: Password of the USER.
8. Click **Confirm Connection Details**.
9. Configure Capture for Oracle: Select **Direct Redo Access**.
10. Select **Test connection before confirming** and click **Confirm Capture**.
11. Specify name and description, then click **Save Location**.

**Target Location (Snowflake):**

1. Click **Create New Location** under Target Locations.
2. Select **Snowflake**.
3. Select connection: **Connect via High-Volume Agent**.
4. Enter Snowflake connection details:
   - **SERVER**: Hostname or IP address.
   - **PORT**: Port number.
   - **ROLE**: Snowflake role name.
   - **WAREHOUSE**: Snowflake warehouse name.
   - **DATABASE**: Snowflake database name.
   - **SCHEMA**: Default schema name.
   - **USER**: Username.
   - **AUTHENTICATION METHOD**: Password or Key Pair.
   - **PASSWORD** (if Password auth): Database user password.
   - **CLIENT PRIVATE KEY** (if Key Pair): Path to .pem file.
   - **CLIENT PRIVATE KEY PASSWORD**: Password for the private key.
5. Advanced Settings:
   - **LINUX/UNIX ODBC DRIVER MANAGER LIBRARY PATH**: Default `/usr/lib64`.
   - **LINUX/UNIX ODBCSYSINI**: Default `/etc`.
   - **ODBC DRIVER**: Name of installed ODBC driver.
6. Click **Confirm Connection Details**.
7. Unselect **Integrate Staging Directory** for simplicity. Click **Confirm Integrate**.
8. Specify name and description, then click **Save Location**.
9. Click **Confirm Locations**.

#### Step 3: Configure Channel

Replication styles:
- **Standard replica**: Mirrors insert, update, delete operations (recommended for this guide).
- **Soft Delete**: Marks rows as deleted when physically deleted on source.
- **TimeKey**: Captures every change as a new record (creates audit trail).

1. Select **Standard replica**.
2. Click **Save Channel and Continue**.
3. Provide channel name and description, then click **Save**.

#### Step 4: Select Tables to Replicate
1. Click **Select Tables** (HVR auto-discovers table definitions).
2. Select the **NAME** checkbox to select all tables, or select individually.
3. Click **Save** to include tables.
4. Click **Confirm** to add tables to the channel.

#### Step 5: Complete Channel
1. Click **Complete Channel Creation** with default options:
   - Activate Replication
   - Refresh Data (initial bulk-load) into Target
   - Start Replication Jobs
2. Capture and integrate jobs will be running. View integrated changes on the chart.

## Data Validation

The **Compare** feature enables data validation by comparing data and table structures between source and target.

1. In the left navigation, click **Channels**.
2. Select your channel.
3. Click **Compare Data** (top right).
4. **Online Compare** option is selected by default.
5. Click **Compare Data**.
6. View the compare job on the Jobs pane.
7. Click **View Log** → event link → **View Results** on the Event Details page.

## Monitoring

### Topology
- Presents all data replication flows managed by the hub.
- Shows direction of data flows, data volume indicators, latency, and job status.
- Interactive chart with live statistical metrics.
- Access via **TOPOLOGY** in the left navigation.

### Statistics
- Historical time series statistics with fixed intervals.
- Metrics: total changes, min/max latency per interval.
- Access via **STATISTICS** in the left navigation.

### Jobs
- Shows current state of all jobs (capture, refresh, integrate, compare).
- Access via **JOBS** in the left navigation.

### Events
- Records all repository changes (job starts/stops).
- Definition Change events can be **undone**.
- Refresh and Compare events can be **repeated**.
- Access via **EVENTS** in the left navigation.

## Reviewing Metadata Definitions

### Tables
- Access via **TABLES** in left navigation.
- Displays source/target table names, refresh info, compare data.
- Click table name for Table Details (data type, encoding info).

### Locations
- Access via **LOCATIONS** in left navigation.
- Shows agent connection, database connection, source/target properties.

### Channels
- Access via **CHANNELS** in left navigation.
- Channel Details provides multiple management options.

## Preferences
- Access via **PREFERENCES** at bottom of left navigation.
- Customize UI view, switch to dark mode, etc.

## Administration
- Access via **SYSTEM** in left navigation.
- Supports multiple hubs on a single hub server.
- Define users, set permissions, configure alerts.
- **Freeze Hub** option to stop all jobs.
- **SWITCH HUB** to switch between hubs.
- HVR provides its own authentication or integrates with LDAP/Kerberos.

---

*End of Getting Started section content*
*Source: https://fivetran.com/docs/hvr6*
*Extracted: June 20, 2026*
