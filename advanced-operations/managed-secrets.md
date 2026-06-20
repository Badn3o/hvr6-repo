# Managed Secrets - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/managed-secrets

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/managed-secrets/index.md)

# Managed Secrets


<b>Since</b> v6.1.5/0

The 'Managed Secrets' feature offers a secure and efficient method for handling secrets such as passwords, key IDs, and secret keys in Fivetran HVR. By utilizing an external password manager and the **hvrmanagedpassword** script, you can keep secrets in a safe environment while ensuring that HVR always has access to the latest password. The **hvrmanagedpassword** script is user-created and facilitates interaction with the external password manager. Instead of directly entering the actual secret in the User Interface (UI), users can provide a token. This token identifies the secret stored in an external password manager. When HVR needs the secret, it communicates with the password manager via the **hvrmanagedpassword** script, accepting the token to retrieve the current secret.

This approach enhances security by keeping secrets in a secure environment external to HVR. Additionally, it eliminates the need for manual intervention during password rotations. HVR automatically receives the latest password from the password manager based on the stored token.

## Configuration to Enable Managed Secrets


To enable and use this feature:

- Create a directory named **authentication** in **HVR_CONFIG/plugin/**.
- Create a script file named **hvrmanagedpassword** (for Linux/Unix) or **hvrmanagedpassword.bat** (for Windows, supported since 6.2.0/0) in the **HVR_CONFIG/plugin/authentication** directory. This script should contain the logic to retrieve passwords from an external password manager using the token as an input argument.
> **Note:** 
The **HVR_HOME/plugin_examples/authentication** directory contains example script files - **hvrmanagedpassword** (for Linux/Unix) and **hvrmanagedpassword.bat** (for Windows). The usage instructions are included within these files.


- Log in to HVR UI or refresh the UI window (if already open).


When HVR detects the **hvrmanagedpassword** script in the **HVR_CONFIG/plugin/authentication** directory,  the hub server property [**Hub_Server_Password_Manager_Configured**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#hubserverpasswordmanagerconfigured) is automatically set to **true** and option **USE TOKEN INSTEAD** is displayed in all UI fields designated for entering secrets.



To use managed secrets in the web user interface (UI), click **USE TOKEN INSTEAD** option and enter the token in the **PASSWORD MANAGER TOKEN** field. Click **Use** and then click **Ok** to confirm. This informs HVR to fetch the secrets from the external password manager when needed, based on the tokens stored in the repository.

To use managed secrets in the command line interface (CLI), execute the [**hvrcrypt**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrcrypt) command with **-m** option along with the token.
hvrcrypt -m <em>token</em>

The command will output the encrypted secret in the !{m:<em>encryptedtext</em>}! format, which can then be used in the location creation commands [**hvrlocationconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlocationconfig) or [**hvrdefinitionimport**](https://fivetran.com/docs/hvr6/command-line-interface/creating-and-activating-channels-from-cli#createasourcelocation).
