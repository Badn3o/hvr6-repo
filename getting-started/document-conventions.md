# Document Conventions - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/document-conventions

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/document-conventions/index.md)

# Document Conventions


This section explains the conventions used in Fivetran HVR documentation.

 Convention | Description |
 **bold** | Indicates computer terms that are fixed, field or button name in UI, keywords, [action name](https://fivetran.com/docs/hvr6/action-reference), action parameters, [commands](https://fivetran.com/docs/hvr6/command-line-interface/command-reference), command parameters, file names, directory path. |
 *italics* | Indicate computer terms that are variables or placeholders requiring user-supplied values. For example, in a directory path such as **HVR_CONFIG/hubs/***myhub*, the word 'myhub' is in italics indicating that it is a variable and should be replaced with the appropriate value. |
 [ ] | Text inside square brackets [ ] indicates optional entries. |
 | | The vertical line or pipe sign ( | ) separates a mutually exclusive set of options. |
 `SELECT * FROM table1;` | Code examples, syntax, and commands recognized by the system are displayed in code blocks using a monospaced font. 
`hvrhubserver -acs`
Code examples or SQL statements embedded inside paragraphs are displayed in a monospaced font with  a gray background. For example, "The HVR database user must be granted the `CREATE TABLE` privilege". |


---

## Menu


Menu selection sequences are displayed in **bold** and each menu item is divided by the **▶** symbol. For example, select **Tools ▶ Data ▶ Entity ▶ Organization**. This means select the **Tools** option in the menu bar, then select the **Data** option in the **Tools** menu, then select the **Entity** option in the **Data** sub-menu and finally click the **Organization** option in the **Entity** sub-menu.

---

## Environment Variables


All occurrences of **HVR_HOME**, **HVR_CONFIG**, and **HVR_TMP** in paragraphs should be treated as environment variables. Linux/Unix users need to add a dollar sign (**$**) and Windows users need to add percent signs (**%**) when setting variables in their operating system.

For example, if a paragraph mentions something about **HVR_CONFIG/logs/**, it should be interpreted as:

- In Linux/Unix - **$hvr_config/logs**
- In Windows - **%hvr_config%/logs**


---

## File/Directory Path


Many path names follow the Unix conventions, where a forward slash '/' is used as a file path delimiter. On the Microsoft Windows platform, this corresponds to a backward slash '\'. Generally, HVR automatically converts between the forward and backward slashes as needed, allowing them to be used interchangeably.

---

## Callouts


We use the following callouts in our documentation to highlight key information:

- 
**Note**

> **Note:** 
Provides additional information that enhances understanding but is not critical to functionality.


- 
**Important**

> **Important:** 
Highlights crucial information that the user must be aware of to avoid errors or issues.


- 
**Tip**

> **Tip:** 
Offers useful suggestions, best practices, or shortcuts.


- 
**Warning**

> **Warning:** 
Alerts about potential risks, data loss, security issues, or irreversible actions.




---

## Labels


We use the following labels in our documentation to convey long messages concisely.

- 
**Applies-to**
Indicates functionality supported only on specific systems, such as a location type or operating system. Example: Oracle, Ingres, SQL Server, Linux, Windows.

- 
**Available Since**
Indicates the HVR version in which a feature was introduced.
Example: <b>Since</b> v6.2.0/10

- 
**Default**
Indicates the default value for a field, property, or command.
Example: default



---

## Icons


We use the following icons in this documentation:

 Icon | Description |
  | Indicates an HVR Agent process or machine. |
  | Indicates an HVR Agent proxy process or HVR Agent proxy machine or a file proxy. |
  | Indicates a channel. |
  | Indicates a database location or location whose type (db/file/kafka) is unknown or hub repository or hive database for external tables. |
  | Indicates a file location or directory or temporary file. |
  | Indicates a Kafka location. |
  | Indicates a location group. |
  | Indicates a table. |
  | Indicates a table group. |
  | Indicates a capture job. |
  | Indicates an integrate job. |
  | Indicates the direction of replication.
In the HVR UI, the color of this icon changes to blue when the channel is activated and to red if a job fails or the latency threshold is exceeded.
 |

