# Command Line Interface - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/index.md)

# Command Line Interface


This section describes the Fivetran HVR commands and their parameters. You can use these commands in the command line interface (CLI) to configure, manage, and monitor the replication process in HVR. The command line interface can be accessed using either of the two methods - Direct CLI or Remote CLI.

## Direct CLI


In this method, the HVR commands are executed directly/locally on the hub machine. The authentication to the HVR Hub System is done using the credentials of the user logged in to a hub machine. In this case, only the hub name is needed to run a command (e.g. <b>hvractivate</b> <em>myhub mychn</em>).

## Remote CLI


In this method, the HVR commands are executed from a remote machine, provided that the HVR is installed on the remote machine. When executing the commands remotely, authentication to the HVR Hub System is required. Otherwise, you can encounter the error **F_JW0555: Refresh token invalid or expired**. The authentication is done via the HVR REST interface. To access a remote hub system, you need to use the command [**hvrlogin**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)**-R**, the authentication token is stored for a certain period of time in **~/.config/hvr**.

For example, to access a remote hub system with the **hvradmin** user, use the following command:
hvrlogin -R http://myhost:12345 -u hvradmin

When using remote CLI, option **-R** must be used to run all commands (except for [**hvrhubserver**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrhubserver)).

## Topics


- [Command Help](https://fivetran.com/docs/hvr6/command-line-interface/command-help)
- [Command Reference](https://fivetran.com/docs/hvr6/command-line-interface/command-reference)
- [Managing Properties in CLI](https://fivetran.com/docs/hvr6/command-line-interface/managing-properties-in-cli)
- [Creating and Activating Channels from CLI](https://fivetran.com/docs/hvr6/command-line-interface/creating-and-activating-channels-from-cli)

