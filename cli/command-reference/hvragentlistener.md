# hvragentlistener - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvragentlistener

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvragentlistener/index.md)

# hvragentlistener


## Usage


<b>hvragentlistener</b> [<em>-options</em>]... <em>portnum</em>

## Description


Command **hvragentlistener** allows to start, stop, and manage the HVR Agent Listener service. When the HVR Agent Listener service is started, it will listen for a connection request on the supplied <em>portnum</em>. The mechanism is the same as that of the Linux/Unix daemon (**systemd**, **xinetd**, or **inetd**).

- On Windows, the HVR Agent Listener is a Windows service which is administered with option <b>-a</b>. The account under which it is installed must be a member of the administrator group and must be granted the privilege to act as part of the operating system (**SeTcbPrivilege**). The service can either run as the default system account or (if option <b>-P</b> is used) it can run under the Fivetran account which created the Windows Service.
- On Unix and Linux, the HVR Agent Listener runs as a daemon which can be started with option <b>-d</b> and killed with option <b>-k</b>.


> **Important:** 
- 
For HVR Agent Listener on Linux and Unix, it is more common to start HVR executables using the system process (**systemd**, **xinetd**, or **inetd**). For more information, see [System Configuration for Agent on Linux](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/system-configuration-for-agent-on-linux) or [System Configuration for Agent on Unix](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/agent/system-configuration-for-agent-on-unix).

- 
When the HVR Agent Listener is executed as a Windows Service, the errors are written to the Windows Event Log (**Control Panel ▶ Administrative Tools ▶ Event Viewer ▶ Windows Logs ▶ Application**).




## Options


This section describes the options available for command **hvragentlistener**.

 Parameter | Description |
 `**-a***x*`
`Windows` | 
Administration operations for the HVR Agent Listener service on Windows.

Values of `*x*` can be:

- **c** : Create (register) the service.
- **s** : Start the service.
- **h** : Stop (halt) the service.
- **d** : Destroy (unregister) the service.
- **t** : Test the service.


Several `**-a***x*` operations can be supplied together; allowed combinations are:

- **acs** : Create and start the service
- **ahd** :**** Halt and destroy the service


> **Note:** 
HVR Agent Listener service can also be started and halted from the **Windows Services** console (accessible from **Control Panel ▶ Administrative Tools ▶ Computer Management ▶ Services and Applications ▶ Services**). The shortcut command to access this console is **services.msc**.

 |
 `**-d**``Unix & Linux` | Start**** HVR Agent Listener as a daemon process. |
 
`**-E***name=value*`
 | Set environment variable `*name*` to `*value*` for the HVR processes started by the service. |
 
`**-i**`
 | Interactive invocation. HVR Agent Listener stays attached to the terminal instead of redirecting its output to a log file. |
 `**-k**``Unix & Linux` | Stop a running**** HVR Agent Listener daemon process. |
 
`**-P***pwd*`

`Windows` | 
Configure HVR Agent Listener service to run under the current login Fivetran account using password `*pwd*`, instead of under the default system login account. This option may only be supplied with option `**-ac**`.

Empty passwords are not allowed. The password is kept (hidden) within the Microsoft Windows operating system and must be re-entered if passwords change. |


## Examples


This section provides examples of using the **hvragentlistener** command.

##### Example 1. Run HVR Agent Listener interactively


Command to run **hvragentlistener** interactively in the terminal and listen on port number 4343.
hvragentlistener -i 4343

> **Important:** 
In this method, exiting the shell/terminal will terminate the HVR Agent Listener.


##### Example 2. Run HVR Agent Listener as daemon process in Linux/Unix


Command to run the **hvragentlistener** as daemon process in Linux/Unix and listen on port number 4343.
hvragentlistener -d 4343

##### Example 3. Stop/kill HVR Agent Listener running as daemon process in Linux/Unix


Command to stop/kill the **hvragentlistener** that is running as daemon process and listening on port 4343.
hvragentlistener -k 4343

##### Example 4. Create and start the HVR Agent Listener as a Windows service


Command to create and run/start the **hvragentlistener** as a Windows service and listen on port number 4343.
hvragentlistener -acs 4343

##### Example 5. Stop and destroy the HVR Agent Listener service in Windows


Command to halt and destroy the **hvragentlistener** that is running as a Windows service and listening on port number 4343.
hvragentlistener -ahd 4343

  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
