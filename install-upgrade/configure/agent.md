# Configuring HVR Agent - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/install-and-upgrade/configure/agent/index.md)

# Configuring HVR Agent


This section describes the configuration required (network security and authentication properties) for [HVR Agent](https://fivetran.com/docs/hvr6/getting-started/concepts/agent) . The configuration steps include creating agent users, and defining the authentication and authorization policies for accessing the agent service.

> **Note:** 
Before configuring the HVR Agent service, it is recommended to read sections [HVR Agent](https://fivetran.com/docs/hvr6/getting-started/concepts/agent) and [User Authentication](https://fivetran.com/docs/hvr6/getting-started/concepts/security-architecture/user-authentication) for detailed information about the HVR Agent, agent users, and user authentication methods.


The agent service can be configured by using either of the following methods:

- 
By initiating the agent 'setup mode' and remotely configure the agent service (e.g. from the UI).

> **Important:** 
- By default, after [installing](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent) and starting the HVR Agent for the first time, it will automatically go into the 'setup mode' for the next 60 minutes for configuration purposes.
- When in 'setup mode', the agent does not accept any connections and is not available for any other activities except for agent configuration.
- In the 'setup mode', you can configure the agent remotely using the user interface or command [**hvragentconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig) with option <b>-R</b>.
- For the command examples to initiate or terminate the HVR Agent 'setup mode', see section [Examples for Starting and Terminating Setup Mode](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig#examplesforstartingandterminatingsetupmode) in [**hvragentconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentconfig).



- 
By using the [agent user](https://fivetran.com/docs/hvr6/getting-started/concepts/agent#agentusers) with the **AgentAdmin** privilege. An agent user with administration privilege can remotely configure the agent service (e.g. from the UI). In this case, the agent 'setup mode' initiation is not required to configure the agent.

- 
By directly accessing the Command Line Interface (CLI) on the agent machine. In this case, the agent 'setup mode' initiation is not required to configure the agent.



The agent service configuration is normally done after the agent has been [installed](https://fivetran.com/docs/hvr6/install-and-upgrade/install/agent) on an agent machine. You can remotely configure the agent service from a browser (UI) while [creating a location](https://fivetran.com/docs/hvr6/user-interface/locations/creating-location) using the **Agent Service Configuration** dialog (provided that the agent service is in the 'setup mode') or for an existing location, the agent service can also be configured/edited from the **Agent** pane available on the [Location Details](https://fivetran.com/docs/hvr6/user-interface/locations/location-details) page. Alternatively, you can also perform the configuration from the command line (CLI). For more information, see [Configuring HVR Agent from CLI](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-cli).

## Topics


- [Configuring HVR Agent from Browser](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-browser)
- [Configuring HVR Agent from CLI](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/configuring-agent-from-cli)
- [System Configuration for HVR Agent on Linux](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/system-configuration-for-agent-on-linux)
- [System Configuration for HVR Agent on Unix](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/system-configuration-for-agent-on-unix)

