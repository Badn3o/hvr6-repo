# HVR Agent - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/concepts/agent

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/concepts/agent/index.md)

# HVR Agent


HVR Agent is an installation of Fivetran HVR that typically resides on the same machine as a source or target data store (database or file system) to perform the task of capturing or integrating data. In the HVR distributed architecture, the agent acts as a child process for the hub server that entirely controls the replication process.

[HVR Agent service configuration](#agentconfiguration) allows to establish a secure network connection to the agent and configure the agent properties. Every HVR Agent has its own set of [agent properties](https://fivetran.com/docs/hvr6/property-reference/agent-properties) that define various agent characteristics/attributes, including agent connection parameters, user access levels, authentication mode, etc. HVR Agent service can be configured both from the HVR [user interface](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser) or using the [command line](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-cli).

> **Note:** 
Even though we recommend using the HVR Agent with the distributed setup, HVR can also support an agent-less architecture. HVR can connect directly (without using agent) to a remote database location using a DBMS protocol such as Oracle TNS.


## Benefits of Using HVR Agents


Even though HVR fully supports agent-less operations, however, the distributed architecture with agents provides security benefits and multiple performance and scalability advantages.

- 
HVR Agent reduces network cost, distributes CPU load, and allows capture of changes directly from DBMS logging system.

- 
Standardized communication between remote agents enables consistent and secure connections using encryption and key-based authentication as needed.

- 
HVR Agent offloads some resource-intensive processing work that would otherwise have to be performed by the hub. Distributing work through agents results in a scalable setup.

- 
HVR Agent compresses data before sending it. Sending compressed data across the wire requires less bandwidth and/or fewer data packets. HVR commonly achieves 10x or higher compression ratios. Data is only decompressed when it reaches the target agent. Compressing data before sending it magnifies the available bandwidth. Always use an agent for communication over a Wide Area Network (WAN), for example, between on-premises and the cloud, to leverage compression.

- 
HVR Agent is sometimes unavoidable in order for HVR to access database transaction logs with sufficient performance. High volume environments may generate such large volumes of transaction logs that access to a database stored procedure or function is simply not fast enough to read the logs over a database connection.

- 
HVR Agent on a source machine filters data before sending it down the data pipeline. Databases always write more information to the transaction log than should be replicated, and in many cases, only a subset of the application tables is replicated to another system. Filtering data close to the source improves efficiency.



## HVR Agent Connection


The HVR Agent listener service allows the hub server to communicate with the HVR Agent. The hub server connects to the agent using a specified TCP/IP port number.

The connection between the agent and the hub server is always secure. By default, the connection is established using TLS. In addition to this secure connection, HVR also allows you to configure [certificate based authentication](#agentconnectiontohubserver) and user based authentication.

> **Note:** 
Separate configuration is not required for enabling the secure TLS connection.


- 
On Unix and Linux, the HVR Agent listener runs as the system process (daemon). For more information, see [System Configuration for HVR Agent on Linux](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/system-configuration-for-agent-on-linux).

- 
On Windows, the HVR Agent listener is a Windows service. The service is started automatically after [installing the HVR Agent on Windows using the installer](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent/installing-agent-on-windows-using-installer). When [installing the HVR Agent on Windows using zip file](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent/installing-agent-on-windows-using-zip-file), the service must be created and started manually.



Command [**hvragentlistener**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener) can be used to start, stop, and manage the HVR Agent listener process/service.

### HVR Agent Connection to Location


When the HVR Agent service is started for the first time, the agent server's public certificate and private key are created automatically and are stored in the HVR Agent properties [**Agent_Server_Public_Certificate**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#agentserverpubliccertificate) and [**Agent_Server_Private_Key**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#agentserverprivatekey) on the HVR Agent machine.

When a location first connects to the HVR Agent, it gets the agent server public certificate (HVR Agent property [**Agent_Server_Public_Certificate**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#agentserverpubliccertificate)) and stores a copy of it (location property [**Agent_Server_Public_Certificate**](https://fivetran.com/docs/hvr6/property-reference/location-properties#agentserverpubliccertificate)) in the repository database. The next time the location connects to the HVR Agent, the HVR Hub System verifies the certificate on the agent side to match the certificate on the location side to establish the connection.

### HVR Agent Connection to Hub Server


The hub server's client public certificate and private key are generated when hub server repository tables are created and are used to verify all incoming connections to the agents. The public certificate and private key are stored in the repository properties [**Agent_Client_Public_Certificate**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#agentclientpubliccertificate) and [**Agent_Client_Private_Key**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#agentclientprivatekey) in the repository database. If the agent is configured to accept connections only from a specific hub server(s) (HVR Agent property [**Only_From_Client_Public_Certificates**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#onlyfromclientpubliccertificates)), the hub server's client public certificate and private key are verified to accept only those that are allowed. This provides an easy and secure way to accept [anonymous connections](#agentauthentication) to the agent from trusted hub servers.

## HVR Agent Configuration


After [installation](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent), the HVR Agent must be configured to implement secure agent service authentication and authorization. HVR Agent service configuration can be done remotely from the [user interface](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser) or the [command line](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-cli) or directly on the agent machine using the command line. Configuration steps include creating HVR Agent users and defining the authentication and authorization policies for accessing the HVR Agent service.

The HVR Agent service can be configured using the following methods:

- 
Enabling the setup mode for the agent. For more information, see [HVR Agent Setup Mode](#agentsetupmode).

> **Important:** 
By default, after the first start of the HVR Agent service, it will enter a 60-minute setup mode, during which the HVR Agent may be configured.


- 
Using the command line on the agent machine. In this case, the setup mode is not required.

- 
Using the HVR Agent user with the administrator (**AgentAdmin)** permissions that can remotely configure the HVR Agent service (e.g. from the [user interface](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser) or [command line](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-cli)). In this case, the setup mode is not required.



### HVR Agent Setup Mode


Setup mode is a special state intended only for HVR Agent configuration, in which the agent does not accept any connections and is not available for any other activities, such as replication. In the setup mode, you can configure the HVR Agent remotely (using the [user interface](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser) or command [**hvragentconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig) with option <b>-R</b>). It is also possible to reinitiate the HVR Agent setup mode using the [**hvragentconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig) command (see section [Examples](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig#examples)).

There are two types of HVR Agent setup mode:

- **Time-based setup mode**: This is a timed setup mode that expires in a certain period of time, after which the HVR Agent becomes completely unavailable unless it is terminated by a user before the expiration. By default, after starting the HVR Agent for the first time after its [installation](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent), it will automatically go into the timed setup mode for the next 60 minutes for the HVR Agent to be configured within this time period. The time-based setup mode can be enabled using command [**hvragentconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig) by setting up the HVR Agent property [**Setup_Mode_Timed_Until**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#setupmodetimeduntil).
- **Token-based setup mode**: This mode is protected with a token name and token value pair. To enable this setup mode, the user needs to define a token name and value (HVR Agent properties [**Setup_Mode_Token_Name**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#setupmodetokenname) and [**Setup_Mode_Token_Value**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#setupmodetokenvalue)). To configure the HVR Agent using the token-based setup mode, the user then needs to supply the token value.


## HVR Agent Connection Modes


The following modes are available for connecting hub to HVR Agent service:

- 
**All connections require an agent user**. This mode requires agent user's credentials to access the HVR Agent service. The HVR Agent user credentials are defined by location properties [**Agent_User**](https://fivetran.com/docs/hvr6/property-reference/location-properties#agentuser) and [**Agent_Password**](https://fivetran.com/docs/hvr6/property-reference/location-properties#agentpassword).

- 
**Anonymous connections only**. This mode allows the HVR Agent service to accept anonymous connection (as opposed to connections with the agent's user credentials) provided that the HVR Agent access is limited to only hubs with specific hub certificates (the HVR Agent property [**Only_From_Client_Public_Certificate**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#onlyfromclientpubliccertificates)). No HVR Agent user account (username and password) is required for this type of authentication. This authentication mode is defined by the HVR Agent property [**Anonymous_Access**](https://fivetran.com/docs/hvr6/property-reference/agent-properties#anonymousaccess).

- 
**Allow both anonymous connections and ones with an agent user**. This mode allows anonymous connections from the trusted hubs and also to define a user with administrator permissions (**AgentAdmin** user) for the purpose of remote HVR Agent configuration.



## HVR Agent Users


HVR Agent user is a special type of HVR user that can access the HVR Agent service. Just like the [hub server user accounts](https://fivetran.com/docs/hvr6/user-interface/system/users) are used to authenticate users on the HVR Hub System, the HVR Agent service has its own set of user accounts. HVR Agent users can also be assigned administrator (**AgentAdmin**) permissions. Only the HVR Agent users with this permission (access level) can [configure the agent service](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser) remotely when the HVR Agent is not in the setup mode. The administrator can either access the **Agent Service Configuration** dialog in the UI or use CLI commands [**hvragentconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig) and [**hvragentuserconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentuserconfig) for configuring the HVR Agent service.

HVR Agent users can access the HVR Agent service using different types of authentication mechanisms. For more information, see section [User Authentication](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/user-authentication).
