# HVR 6 - 12 Rest Api

**Source:** https://fivetran.com/docs/hvr6/rest-api

---

# HVR REST API

This section describes the Fivetran HVR REST API functionality.

The REST APIs are provided for advanced users who want to script HVR interactions and for developers who want to integrate HVR into their applications.

Representational State Transfer (REST) API is a simple, stateless architecture style (not a protocol) that uses the HTTP/HTTPS method (such as`GET`,`PUT`,`POST`,`DELETE`) to retrieve the management information from the database. The main advantage is that it has a simple interface and can be modified even when HVR is running.

## Interfaces

HVR has close to 200 REST API end-points and these are grouped into 'interfaces'. Most REST end-points return a JSON response and many also accept a JSON request.

Following are the REST interfaces in HVR:

- Activate, Refresh, and Compare Interface

- Agent Configuration Interface

- Alert Interface

- Authentication Interface

- Control Message Interface

- Definition Interface

- Encryption Interface

- Event Interface

- File and DB Browse Interface

- Hub Config Interface

- HubServer Interface

- Job Interface

- License Interface

- Logfile Tailing Interface

- Miscellaneous Interface

- Query Interface

- Repository Config Interface

- Statistics Interface

- Table Adapt Interface

- User Config Interface

The specification for each REST end-point defines the structure of this JSON using a syntax called**HVR prototype**. For more information about HVR prototype, see[Prototype Specification](https://fivetran.com/docs/hvr6/rest-api/prototype-specification).

An example for how to use REST API is available in section[REST API Examples](https://fivetran.com/docs/hvr6/rest-api/rest-api-examples).

## Versioning

The REST API for HVR is version independent but is closely related to the HVR version. A single HVR Hub Server can serve multiple version of the REST API, so that older Command Line Interface (CLI) clients and user written API clients continue to work, even if the HVR Hub Server was upgraded with a new version of the REST API.

A new API version is released only when there is a change in the API. The REST API version is defined as the HVR version that released the specific version of the API. Therefore, the API version looks similar to the HVR version.

Note that the string representation in API version contains only '**.**' instead of the '**/**'. For example, when HVR version 6.1.0/1 got released with changes in API, it then serves**/api/v6.1.0.1**. Later, when HVR version 6.1.0/2 is released but does not have any API changes, then it still serves**/api/v6.1.0.1**.

HVR[properties](https://fivetran.com/docs/hvr6/property-reference)and[actions](https://fivetran.com/docs/hvr6/action-reference)are not dependent on API version, which means you can inspect or changes values of newer HVR properties or actions using an older version of API. For example, a new property or action parameter introduced in HVR version 6.1.0 can still be inspected and changed using an older API version like**/api/v6.0.5**.

### Version in the REST Request URL

This section describes about the version number to be used in the REST request URL.

- For authentication request (
- Login
- ), irrespective of the HVR version,
- /v1
- must be used.

- For HVR versions 6.0.5/0 and above,
- /latest
- may be used instead of the actual version (e.g.
- /v6.0.5
- ).
- /latest
- will be automatically converted to the highest known version by the HVR Hub Server.

- For HVR versions prior to 6.0.5/0,
- /latest
- or
- /v6.0.5
- must be replaced with
- /v0
- .

### Supported API Versions

To list the HVR API versions supported by your hub server, use the following cURL statement:

`curl -H "Authorization: bearer``access_token``"``hub_server_url``/api`

**Example Request:**

`curl -H "Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6pXVCJ9.eyJpc3MiOiJodHRwOi8vbWFsdGE6NTY5MDAiLCJzdWIiOiJW5l2w1bRxU" http://localhost:4340/api`

**Example Response:**

`["v0","v6.0.5","v6.0.5.1"]`

## Supplying Data

Normally, the data (**-d**or**--data**) is supplied directly on the command line. To send large amount of data or to avoid escaping of special characters in the Windows command prompt, you can use a data file to supply data from the command line.

### Supplying Data Directly on Command Line

Example for supplying data directly on the command line:

`curl \
-X POST \
-d '{"loc":"mylocation", "props": {"Class":"oracle", "Oracle_Home":"/oracle/1900", "Oracle_SID":"ORA1900", "Database_User":"mydb", "Database_Password":"mydbpassword", "Capture_Method":"DIRECT"}}' \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwOi8vbWFsdGE6NTY5MDAiLCJzdWIiOiJodnIiLCJleHAiOjE2NDIxNjI3MTh9.Fd5x4uGzRimvj8Ykq867lXQTWuIQBVELzhvn3mfPv8U" \
-H "Content-Type: application/json" \
http://localhost:4340/api/latest/hubs/myhub/definition/locs`

### Supplying Data from File

Following is the procedure to supply data from a file:

1. Create a JSON file with the required data.

2. For example, to create an Oracle location:

3. {"loc":"myloc_file", "props": {"Capture_Method":"DIRECT","Oracle_Home":"/oracle/1220","Oracle_SID":"ORA1220","Database_User":"mytestdb","Database_Password":"testdbpass", "Class":"oracle"}}

4. Save the JSON file (e.g.
5. mydata.json
6. ).

7. Run the cURL command.

8. For example:

9. Linux
10. Windows

11. curl \
-X POST \
-d @mydata.json \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwOi8vbWFsdGE6NTY5MDAiLCJzdWIiOiJodnIiLCJleHAiOjE2NDI0MTcwNTF9.mmYpa_It9Mj5p0I_HBceHTdu_4-HJj_yqWyYMVgLyhg" \
-H "Content-Type: application/json" \
http://localhost:4340/api/latest/hubs/myhub/definition/locs

12. curl ^
-X POST ^
-d @mydata.json ^
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwOi8vbWFsdGE6NTY5MDAiLCJzdWIiOiJodnIiLCJleHAiOjE2NDI0MTcwNTF9.mmYpa_It9Mj5p0I_HBceHTdu_4-HJj_yqWyYMVgLyhg" ^
-H "Content-Type: application/json" ^
http://localhost:4340/api/latest/hubs/myhub/definition/locs

## Status Codes

| Code | Name | Description |
|---|---|---|
| 200 | OK | Indicates that the request has succeeded. |
| 201 | Created | Indicates that the request has succeeded and a new resource has been created as a result. |
| 400 | Bad Request | Indicates that the request could not be understood by the server, probably due to incorrect syntax. |
| 403 | Forbidden | Indicates that the user does not have execution access rights. |

## Related Articles

- REST API Examples

- Prototype Specification

- REST API Reference