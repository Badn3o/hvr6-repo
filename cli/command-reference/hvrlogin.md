# hvrlogin - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvrlogin/index.md)

# hvrlogin


## Usage


- <b>hvrlogin</b> <b>-R</b><em>url</em> [<b>-u</b><em>user</em>]
- <b>hvrlogin -R</b><em>url</em> [<b>-u</b><em>user</em>] <b>-s</b> [<b>-a</b>]
- <b>hvrlogin -R</b><em>url</em> [<b>-u</b><em>user</em>] <b>-c</b> [<b>-a</b>]
- <b>hvrlogin -R</b><em>url</em> [<b>-u</b><em>user</em>] <b>-L</b>
- <b>hvrlogin -R</b><em>url</em> [<b>-u</b><em>user</em>] <b>-l</b><em>login-token</em> <b>-s</b> [<b>-a</b>]
- <b>hvrlogin -R</b><em>url</em> [<b>-u</b><em>user</em>] <b>-l</b><em>login-token</em> <b>-c</b> [<b>-a</b>]


## Description


Command **hvrlogin** authenticates a user to the HVR Hub System via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

> **Note:** 
The [**Hub_Server_Login_Expiration**](https://fivetran.com/docs/hvr6/property-reference/repository-properties#hubserverloginexpiration) repository property allows you to change the default (one week) login session expiration time. The login session will expire (time-out) after the configured time, regardless of whether a user is active or inactive (idle).


> **Note:** 
`**Since** v6.1.5/8` the [**Authentication_Method**](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#authenticationmethod) hub server property can be used to explicitly enable or disable specific authentication methods (the default is **password** authentication)


## Options


This section describes the options available for command **hvrlogin**.

 Parameter | Description |
 `**-a**` | 
Export a short-lived (15-minute) access token instead of a long-lived refresh token.

The following command exports a short-lived access token.
`hvrlogin -R http(s)://myserver:4343 -u admin -s -a`

Option `**-a**` must be combined with either option `**-c**` or option `**-s**`. |
 `**-c**` | 
Output a one-week refresh token to a C shell environment variable for use by other HVR commands for authentication. This option is used for command line scripting, e.g. to put in a (Unix) shell script, instead of storing it on a disk.

The following command exports a refresh token.
`hvrlogin -R http(s)://myserver:4343 -u admin -c` |
 `**-L**`
`**Since** v6.1.5/8` | 
Generate a short-lived (15-minute) one-time login token. This token allows a user to authenticate and log in to the HVR hub system without requiring a password.

The following command generates a short-lived one-time login token to log in as user **admin**.
`hvrlogin -R http(s)://myserver:4343 -u admin -L`

Option `**-L**` requires the hub server property **[Authentication_Method](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#authenticationmethod)** to contain **"login_token":true**.
 |
 `**-l***login_token*`
`**Since** v6.1.5/8` | 
Login using a login token

The following command allows you to log in using a login token.
`hvrlogin -R http(s)://myserver:4343 -l xxxxxxxxxxxxxxxx -s`

Option `**-l**` requires the hub server property **[Authentication_Method](https://fivetran.com/docs/hvr6/property-reference/hub-server-properties#authenticationmethod)** to contain **"login_token":true**.

Option `**-l**` must be combined with either option `**-c**` or option `**-s**`.
 |
 `**-S**` | 
Get remote setup mode credentials. Entering the setup mode lets you configure hub server properties. This option can be used only when the hub server is in setup mode.

The following command allows you to log in to a remote hub server that is in setup mode.
`hvrlogin -R http(s)://myserver:4343 -S` |
 `**-s**` | 
Output a one-week refresh token to a Bourne shell environment variable for use by other HVR commands for authentication. This option is used for command line scripting, e.g. to put in a (Unix) shell script, instead of storing it on a disk.

The following command exports a refresh token.
`hvrlogin -R http(s)://myserver:4343 -u admin -s` |
 `**-u***user*` | 
User to log in to the HVR Hub System.

The following command allows you to log in to a remote hub server with user **admin**.
`hvrlogin -R http(s)://myserver:4343 -u admin` |
 `**-R***url*` | Remote hub server. The command accesses a hub server, which could be running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api). This option is required for remote CLI access. |


## Examples


The following is an example of a bash script (<b>-s</b>) getting a 15-minute access token (<b>-a</b>) and using it with curl.
#!/bin/bash
R="http://hostname:4340/"
user=myuser
pass=myuser
hub=myhub




# This puts a 15-minute access token in the environment variable of this process
eval $(echo $pass | hvrlogin -R$R -u$user -s -a)




# API call: you need the Authorization header for all calls to API
curl -i -H"Authorization: Bearer $HVR_LOGIN_ACCESS_TOKEN" \
    -XGET $R/api/v0/hubs/$hub

  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
