# Architecture - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/concepts/architecture

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/concepts/architecture/index.md)

# Architecture


Fivetran HVR may be installed on the most commonly used [operating systems](https://fivetran.com/docs/hvr6/supported-platforms/platform-support-matrix-610). HVR reads the transaction logs of the source location(s) in real time. That data is then compressed, optionally encrypted, and sent to a 'hub machine'. The hub system then routes the data and integrates (applies) the data into the target location(s).



## Location


A **location** is a storage place (for example, database or file storage) from where HVR captures changes (**source location**) and/or integrates changes (**target location**).

## HVR Hub System


The HVR Hub System is an installation of HVR on a server, which orchestrates replication in logical entities called [channels](https://fivetran.com/docs/hvr6/getting-started/concepts/channel). The HVR Hub Server is supported or can be installed only on Linux and Windows machines (physical, virtual or containerized).

The HVR Hub System comprises the following elements:

- **HVR Hub Server**
This is the main HVR process that runs on the hub machine. Its main two purposes are to run a light-weight web server to enable access to the REST API, and it is responsible for managing the Scheduler. When required the hub server process spawns child processes like the Scheduler and HVR worker (executable). The hub server can serve one or more **Hubs** (logical hub). The HVR Hub Server is also the access point for any remote connection to the HVR Hub System.
- **Repository Database**
The repository database consists of a set of tables storing metadata definitions for the replication between source and target locations. The repository database contains HVR [repository tables](https://fivetran.com/docs/hvr6/internal-objects/repository-tables) that hold all specifications of replication such as the name of replicated databases, replication direction, and the list of tables to be replicated. For the list of databases that HVR supports as a repository database, see section [Repository Database](https://fivetran.com/docs/hvr6/capabilities/610#hubdatabase) in [Capabilities](https://fivetran.com/docs/hvr6/capabilities/610).
- **Hub**
This is a logical entity that is created inside the HVR Hub System. If multiple hubs are created inside the HVR Hub System, then the Hub server will spawn separate Schedulers for each hub created.
- **Jobs**
In HVR, a job is a process that performs a certain task such as capturing changes, refreshing data, integrating changes, comparing data. For more information about HVR jobs, see the concept page [Jobs](https://fivetran.com/docs/hvr6/getting-started/concepts/jobs).
- **Scheduler**
The HVR Hub Server runs a Scheduler service to manage replication jobs (like **Capture**, **Integrate**, **Refresh**, and **Compare** jobs) that move data between source location(s) and target location(s). To either capture or integrate changes, the Scheduler on the hub machine starts the capture and integrate jobs that connect out to source and target locations. For each logical hub, the HVR Hub Server creates and runs separate Scheduler.
- **Log Files**
The log files contain messages from the scheduled jobs like **Capture**, **Integrate**, **Refresh**, and **Compare** jobs. It provides details about the activities like transport, routing, and integration. The HVR Hub Server logs information about the hub server itself. For each logical hub, HVR Hub Server creates and maintains separate set of log files.
- **Router Files**
Router files are the files that HVR Hub Server creates internally to store a history of what HVR had captured and submitted for integration, including the information about timestamps, states of the capture and integrate jobs, transactions, channels, locations, tables, instructions for a replication job, etc. For each logical hub, HVR Hub Server creates and maintains a separate set of router files.


> **Important:** 
The HVR Hub System can also be configured to work as a HVR Agent to capture or integrate changes.


## HVR Agent


The HVR Agent is an installation on a remote source and/or target machine that allows to implement a distributed setup. The HVR Agent acts as a child process for the hub system/machine. To access a remote location, the HVR Hub System normally connects securely (using TLS) to the HVR Agent using a special TCP/IP port number. The HVR Agent is supported or can be installed only on Linux, Unix (Solaris, AIX), and Windows machines.

> **Note:** 
Even though we recommend using the HVR Agent with the distributed setup, HVR can also support an agent-less architecture. HVR can connect directly (without using agent) to a remote database location using a DBMS protocol such as Oracle TNS.


For more information about HVR Agent, see the concept page [HVR Agent](https://fivetran.com/docs/hvr6/getting-started/concepts/agent).

## Interface for Operating HVR


A user can operate or interact with HVR using either of the following interfaces:

### Web UI


The web UI is an intuitive and responsive graphical user experience for configuring/operating HVR. It also provides a comprehensive visualization of replication (capture and integrate) along with dashboard and event log viewer. It can be used on both computer and tablet screens. HVR web UI is commonly referred to as 'UI' in this documentation.

For more information about HVR web UI, see [User Interface](https://fivetran.com/docs/hvr6/user-interface).

### Command Line Interface (CLI)


HVR can be configured/operated from the command line (e.g. Linux shell or Windows command prompt) using HVR commands. HVR CLI can be accessed directly on the hub machine or from a remote machine (provided a HVR installation is available on the remote machine). Without a HVR installation, the client can still make REST calls (e.g. using CURL or some other utility/tools).

For more information about HVR CLI, see [Command Line Interface](https://fivetran.com/docs/hvr6/command-line-interface).

### REST API


The REST APIs are provided for advanced users who want to script HVR interactions, and for developers who want to integrate HVR into their application. For more information about HVR REST interface, see [REST API](https://fivetran.com/docs/hvr6/rest-api).
