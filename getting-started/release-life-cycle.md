# Release Life Cycle - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/getting-started/release-life-cycle

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/release-life-cycle/index.md)

# HVR 6 Release Life Cycle


The page contains detailed information on the support duration for Fivetran HVR 6 releases, version compatibility, supported operating system releases, and supported DBMS releases.

> **Important:** 
HVR 6 is not compatible with HVR 5.


## Support Duration for HVR 6 Releases


- Major HVR 6 releases (e.g., HVR 6.1.0) are supported for 3 years from their General Availability (GA) release date.
- Fivetran typically releases a new major version every 12-18 months.
- Early Adopter (EA) releases (e.g., HVR 6.1.5) and patch releases (e.g., HVR 6.1.0/40 or 6.1.0/43.1) do not extend the GA support window. For example, if support for HVR 6.1.0 ends on 2026-01-31, that date does not change even if HVR 6.1.5/0 is released a year later.


The following table shows the release and support dates for the most recent major releases of HVR:
 RELEASE | GA RELEASE DATE | END OF REGULAR SUPPORT | SUPPORT STATUS |
 **6.1** | 2021-12-03 | 2026-01-31 | Support Ended |
 **6.2** | 2024-09-25 | 2027-09-30 | Regular |
 **6.3** | 2025-12-11 | 2028-12-31 | Regular |

### Version Compatibility


- HVR 6 is not compatible with the HVR versions 5.x and 4.x. So, ensure that version 6.x is installed on the Hub machine and Agent machine.
- HVR versions are 'network compatible' with the two previous major versions but not with versions that have a different initial number. For example, HVR 6.1 is network-compatible with 6.2 and 6.3, but not with HVR 5.7.
- When using a mix of HVR versions, note that each bug fix or feature is only effective if the correct installation/machine is upgraded. For example, if a new release fixes an **Integrate** bug, then that release must be installed on the machine(s) that performs **Integrate**. So if only the hub machine(s) is(are) upgraded, then there will be no benefit. To decide whether each installation needs to be upgraded, see the descriptions in the [release notes](https://fivetran.com/docs/hvr6/release-notes) (also available in the directory path **HVR_HOME/hvr.rel**). Each description ends with a line saying which machine(s) must be upgraded for that specific bug fix or feature to be effective.


## Supported Operating System Releases


- For the list of operating system (OS) versions supported by HVR, see [Supported Platforms](https://fivetran.com/docs/hvr6/supported-platforms) or refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (also available in the directory **HVR_HOME/hvr.rel** or on the [Downloads](https://fivetran.com/dashboard/account/downloads) page of the Fivetran [dashboard](https://fivetran.com/docs/getting-started/fivetran-dashboard)).
- Once an OS version is supported by HVR, support for that platform will continue until the OS supplier ends its "mainstream support". After that date, the support for HVR goes from "Regular" to "Sunset", which means that our support continues (including the new HVR versions), but eventually, it may be withdrawn without notice.
- A customer may request that Fivetran makes support for an OS version "Extended" instead of "Sunset", which means that our support will not be withdrawn as long as the customer continues to share information about the production status of that OS version for the customer, and Fivetran can reasonably continue to support the platform.
- A consequence of the end of Fivetran support is that we are no longer able to supply patches for that OS version.
- HVR supports Linux based on a minimal glibc version of 2.12 which is not limited to the Enterprise products below. As long as the version of Linux is compatible with glibc it should work.


> **Tip:** 
For the support status of OS versions, refer to the respective vendor or community site.


## Supported DBMS Releases


- For the list of DBMS versions (such as "Oracle: version 12.2, 18c, and 19c") supported by HVR, see [Supported Platforms](https://fivetran.com/docs/hvr6/supported-platforms) or refer to the HVR [release notes](https://fivetran.com/docs/hvr6/release-notes) (also available in the directory **HVR_HOME/hvr.rel** or on the [Downloads](https://fivetran.com/dashboard/account/downloads) page of the Fivetran [dashboard](https://fivetran.com/docs/getting-started/fivetran-dashboard)).
- Subsequent major versions of the DBMS (such as "Oracle 23ai") are not automatically supported but may be recertified by Fivetran after QA testing. But patches to a supported DBMS version are automatically supported by HVR (no recertification is done at the patch level).
- Once a DBMS version is supported by HVR on a given OS platform, support for that DBMS version will continue at least until the DBMS supplier ends its "mainstream support". After that date, Fivetran support goes from "Regular" to "Sunset", which means that our support continues (including new HVR versions), but eventually, it will be withdrawn without notice.
- A customer may request that Fivetran makes support for a DBMS version "Extended" instead of "Sunset", which means that our support will not be withdrawn as long as the customer continues to share information about the production status of that DBMS version for the customer, and Fivetran can reasonably continue to support the platform.
- A consequence of the end of Fivetran support is that we are no longer able to supply patches for that DBMS.


> **Tip:** 
For the support status of DBMS versions, refer to the respective vendor or community site.

