# hvrlicense - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlicense

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/command-line-interface/command-reference/hvrlicense/index.md)

# hvrlicense


## Usage


- <b>hvrlicense</b> [<b>-R</b><em>url</em>] List all licenses in the repository, with properties.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-a</b> Upload the monthly active rows (MAR) data and snapshots of your hub system to the Fivetran server to renew the license for the consumption-based pricing.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-A</b> Force acquire a license for the consumption-based pricing.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-d</b><em> licname </em> Delete a license from the repository.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] [<b>-l</b><em>licname</em>] [<b>-f</b>] <em>licfile</em> Add a license from a file into the repository.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] [<b>-l</b><em>licname</em>] <b>-o</b> <em>licfile</em> Export a license from the repository into a file.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-m</b><em>marfile</em> [<b>-B</b><em>period_begin</em>] [<b>-E</b><em>period_end</em>] Save the MAR data of the hub system to file *marfile*, optionally specify the begin period and end period, for which the data should be downloaded.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-M</b><em>marfile</em> [<b>-B</b><em>period_begin</em>] [<b>-E</b><em>period_end</em>] Save the monthly aggregate of the hub system's MAR data to a CSV file, optionally specify the begin period and end period, for which the data should be downloaded.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-P</b><em>purge_before</em> Force-purge the MAR data.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-r</b> Register the hub system with the Fivetran Account.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-s</b> Print the status of licensing.
- <b>hvrlicense</b> [<b>-R</b><em>url</em>] <b>-t</b> Test consumption-based pricing registration and print the status.


## Description


Command **hvrlicense** allows you to manage Fivetran HVR licenses. For more information on licenses, see section [Licensing](https://fivetran.com/docs/hvr6/getting-started/licensing).

## Options


This section describes the options available for command **hvrlicense**.

 Parameter | Description |
 `**-a**`
`**Since** v6.1.0/3` | 
Automatic license renewal for consumption-based pricing. Uploads the MAR data and snapshots of your hub system to the Fivetran server for license renewal. The hub server runs this hourly to keep licensing up to date.

> **Important:** 
A user should never run this command, except for debugging or testing purposes.

 |
 `**-A**`
`**Since** v6.1.0/3` | Force acquire a license for consumption-based pricing. This will force the download of the license using the credentials from the [Fivetran account registration](https://fivetran.com/docs/hvr6/user-interface/system#fivetranaccountregistration). This option is needed as part of the CLI workflow for registering a license with a Fivetran account. It can also be used in cases of license errors or by technical support. |
 `**-B***period_begin*`
`**Since** v6.1.0/3` | 
Begin of the period, for which MAR data is downloaded. This option must be used in combination with option `**-m**` or `**-M**`.

If used with option `**-m**`, the period is always rounded down to the start of an hour. For example, if you use '**2022-01-01T10:30:13Z**', it will be rounded down to '**2022-01-01T10:00:00Z**'. If you use '**now**', it will be rounded down to **2022-03-17T11:00:00Z** provided that it is 11:20 now in GMT.

If used with option `**-M**`, the period is always rounded down to the beginning of a month. For example, if you use '**2022-01-09T00:00:00Z**', it will be rounded down to '**2022-01-01T00:00:00Z**'.


Valid formats for *period_begin******* are:

- 
*YYYY-MM-DD* [*HH:MM:SS*] (in local time).

- 
*YYYY-MM-DD***T***HH:MM:SS+TZD*

- 
*YYYY-MM-DD***T***HH:MM:SSZ*

- 
**today**

- 
**now***[±SECS]*

- 
an integer (seconds since **1970-01-01 00:00:00 UTC**)



See section [Examples](#examples) for specific usage examples. |
 `**-d***licname*` | Delete license `*licname*` from the repository. |
 `**-E***period_end*`
`**Since** v6.1.0/3` | 
End of the period, for which the MAR data is downloaded. This option must be used in combination with option `**-m**` or `**-M**`.

If used with option `**-m**`, the period is always rounded up to the next hour. For example, if you use '**2022-01-01T10:30:13Z**', it will be rounded up to '**2022-01-01T11:00:00Z**'. If you use '**now**', it will be rounded up to **2022-03-17T12:00:00Z** provided that it is 11:20 now in GMT. 

If used with option `**-M**`, the period is always rounded up to the next month. For example, if you use '**2022-01-15T00:00:00Z**', it will be rounded up to '**2022-02-01T00:00:00Z**'.


Valid formats for *period_end******* are:

- 
*YYYY-MM-DD [HH:MM:SS]* (in local time)

- 
*YYYY-MM-DD***T***HH:MM:SS+TZD*

- 
*YYYY-MM-DD***T***HH:MM:SSZ*

- 
**today**

- 
**now***[±SECS]*

- 
an integer (seconds since **1970-01-01 00:00:00 UTC**).


 |
 `**-f**` | Replace the existing license with a new license being added from a file if the name of the new license already exists in the repository (instead of displaying an error). |
 `**-l***licname*` | 
License name in the repository. If the license name `*licname*` is not supplied, then the basename of the license file (`*licfile*`) is used instead.

This option can be used when adding a license from a file, or when exporting (`**-o**`) a license to a file. In the first case, it defines the name for the license in the repository. If this option is not supplied when adding the license, then the basename of the license file (`*licfile*`) is used instead. If used when exporting the license, it matches the license name in the repository and exports that license into a file. |
 `**-m***marfile*`
`**Since** v6.1.0/3` | Save the MAR data of the hub system to file `*marfile*`. 

The option can be used with options `**-B**` and/or `**-E**`to specify the period, for which the data must be saved to the file. If option `**-m**` is used without options `**-B**` and `**-E**`, then all the stored MAR data will be saved to the file. |
 `**-M***mmarfile*`
`**Since** v6.1.0/26` | Save the monthly aggregate of the hub system's MAR data to a CSV file. The value of `*mmarfile*` can be a name for the generated file or it can be a directory path for saving the file. If a directory path is specified, then a dynamic file name is assigned using the date for which the generated MAR applies to (e.g. Compact_MAR_2023-02_to_2023-04.csv). 

The option can be used with options `**-B**` and/or `**-E**`to specify the period, for which the data must be saved to the file. If option `**-M**` is used without options `**-B**` and `**-E**`, then it generates a file with last three whole months data.
 |
 `**-o**` | Export the license from the repository to a text file. |
 `**-P***purge_before*`
`**Since** v6.1.0/3` | Force purge of stored MAR data older than the specified time `*purge_before*`. By default, MAR data is purged automatically after 30 days for unregistered hub systems, and after 24 hours for registered hub systems. |
 `**-r**`
`**Since** v6.1.0/3` | Register the hub system with the Fivetran Account. |
 `**-R***url*` | 
Remote hub server. Access the hub server running on a remote machine, via the [REST interface](https://fivetran.com/docs/hvr6/rest-api).

This option is required for [remote CLI access](https://fivetran.com/docs/hvr6/command-line-interface). When using this option, command **[hvrlogin](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlogin)** should be run first, for authentication.
 |
 `**-s**`
`**Since** v6.1.0/3` | Print the status of licensing. |
 `**-t**`
`**Since** v6.1.0/3` | Test consumption-based pricing registration and print the status. |


## Examples


This section provides examples of using the **hvrlicense** command.

##### Example 1. Add license to repository from file


- 
The following command adds license **hvrlic** from file **lic.file** into the repository.
hvrlicense -l hvrlic lic.file



- 
If the license name is not supplied with option <b>-l</b>, then the basename (**lic.file**) of the license file is used instead.
hvrlicense lic.file



##### Example 2. Replace existing license


- 
The following command will add a new license from the **lic** file to the repository and replace the existing license with name **lic**.
hvrlicense -f lic

- 
The following command will add a new license **hvrlic** to the repository and replace the existing license with name **hvrlic**.
hvrlicense -l hvrlic -f lic.file



##### Example 3. Delete license from repository


The following command deletes license **lic_hvr**.
hvrlicense -d lic_hvr

##### Example 4. Export license from repository to file


The following command retrieves license **hvr.lic** from the repository into file **lic.file**.
hvrlicense -l hvr.lic -o lic.file

##### Example 5. Save MAR data to file


The following command saves the MAR data for the period from **March 20, 2022 6 p.m.** till **March 21, 2022 10 a.m.** to file **marfile**.
hvrlicense -B'2022-03-20 18:00:00' -E'2022-03-21 10:00:00' -m marfile

##### Example 6. Save monthly aggregate of MAR data to a CSV file


The following command saves the monthly aggregate of MAR data for the last three months. The dot (**.**) indicates the current directory path where the CSV file is to be saved. The file name will be generated dynamically, which corresponds to the period for which the MAR data applies to.
hvrlicense -M .

##### Example 7. Save monthly aggregate of MAR data to a CSV file with custom name


The following command saves the monthly aggregate of MAR data for the last three months into a CSV file named **mymar**. The file is saved into the current directory path from where the command is executed.
hvrlicense -M mymar.csv

##### Example 8. Save monthly aggregate of MAR data to a CSV file with begin and end period


The following command saves the monthly aggregate of MAR data for specified period into a CSV file named **mymar**. The file is saved into the current directory path from where the command is executed.
hvrlicense -B'2022-03-20 18:00:00' -E'2022-04-21 10:00:00' -M mymar.csv

> **Important:** 
The value for begin and end period will be rounded, the MAR data will be generated for the whole month of March and April (from '2022-03-01 00:00:00' to '2022-05-01 00:00:00').


  table td:first-child {
    white-space: nowrap;
  }

th {
     position: sticky !important;
     top: 0 !important;
     z-index: 5;
     border-top: none !important;
 }
