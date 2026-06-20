# Licensing for HVR

**Source:** https://fivetran.com/docs/hvr6/getting-started/licensing

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/getting-started/licensing/index.md)

# Licensing


You must have a valid license to use Fivetran HVR for data replication. The license includes details such as the issue and expiry dates, the source/target location types that can be used for replication.

Fivetran uses a [consumption-based](#consumptionbased) licensing model for HVR, available through the [Business Critical](https://fivetran.com/docs/hvr6/getting-started/pricing#businesscritical) plan. The license is automatically supplied to the HVR Hub System as part of this model.

> **Important:** 
We've deprecated the **Private Deployment** pricing plan and **Usage-based Subscription** licensing model as of March 1, 2025. HVR accounts on the **Private Deployment** plan must transition to the **Business Critical** or other available plans upon contract renewal. See [Pricing Plan Updates](https://fivetran.com/docs/hvr6/getting-started/pricing#pricingplanupdates) for more information.



## Consumption-based


`**Since** v6.1.0/3`
In this licensing model, you must register the HVR Hub System with the Fivetran server to acquire a license.

The license is valid for 7 days. It is automatically renewed daily, with the issue and expiry dates incremented by one day each time. For example, if you registered on March 10th, the license issue and expiry dates would be March 10th and March 17th, respectively. On March 11th, the license would be auto-renewed, resulting in the issue date updated to March 11th, and the expiry date updated to March 18th.

> **Note:** 
To register the HVR Hub System with the Fivetran server, you must have access to **fivetran.com** (35.236.237.87) from your web browser.


To register a newly installed HVR Hub System with the Fivetran server, use one of the following methods:

- For browser-based setup, see [Setting up HVR Hub from Browser](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub/setting-up-hub-from-browser).
- For CLI-based setup, see [Setting up HVR Hub from CLI](https://fivetran.com/docs/hvr6/install-and-upgrade/configure/hub/setting-up-hub-from-cli).


To register an existing HVR Hub System with the Fivetran server, use one of the following methods:

- In the HVR UI, navigate to [**System**](https://fivetran.com/docs/hvr6/user-interface/system) **▶** [**Licensing**](https://fivetran.com/docs/hvr6/user-interface/system#licensing).
- In the CLI, use the [**hvrlicense**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvrlicense) command.


For more information about how the consumption-based licensing model works in an HVR High-Availability environment, see our [How Does Consumption-Based Licensing Model Work in HVR High-Availability Environment documentation](https://fivetran.com/docs/hvr6/faq/expert-notes-best-practices/cbp-high-availability-hub).
