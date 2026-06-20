# Using Contexts Variables for Comparing Data Based on Datetime Column - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/advanced-operations/using-contexts-variables-for-comparing-data-based-on-datetime-column

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/advanced-operations/using-contexts-variables-for-comparing-data-based-on-datetime-column/index.md)

# Using Contexts Variables for Comparing Data Based on Datetime Column


> **Important:** 
It is assumed that a channel is already created with source and target locations residing on Oracle databases.


This section describes the steps for configuring the channel for comparing a manageable subset of data in two Oracle tables based on a DateTime column. Fivetran HVR allows you to implement this behavior using action [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) with the **CompareCondition** and **Context** parameters using context variables.

To set up [**HVR Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) based on a DateTime column using context variables, you need to define action [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) with parameters **CompareCondition** and **Context** for both source and target locations. The **CompareCondition** allows comparing only rows that satisfy a certain condition. The condition may be defined using the following pattern **{hvr_var_***xxx***}**, where *xxx* is a value of the context variable. The **Context** parameter allows to activate the **Restrict** action only if the context is enabled. For more information, see sections [**CompareCondition**](https://fivetran.com/docs/hvr6/action-reference/restrict#comparecondition) and [**Context**](https://fivetran.com/docs/hvr6/action-reference/restrict#context) on the [**Restrict**](https://fivetran.com/docs/hvr6/action-reference/restrict) page.

- 
In the [**Channel Details**](https://fivetran.com/docs/hvr6/user-interface/channels/channel-details) page, click the **More Options**  icon at the top right menu and select **View Actions**.

- 
In the [**Actions**](https://fivetran.com/docs/hvr6/user-interface/action-list) dialog, click [**Add Action**](https://fivetran.com/docs/hvr6/user-interface/action-list/adding-action) and select **Restrict** from the list of actions.

- 
In the **New Action: Restrict** dialog, ensure that the **All Locations** option is selected in the location scope selector.

- 
Select table **product** in the table scope selector.

- 
Specify the following condition in the **CompareCondition** field: **last_update>{hvr_var_last_modified}**, where **last_modified** is a variable, the value for which will be defined in the **Contexts** tab of the **Compare Data** dialog (see step 10 below). By defining different values/expressions for the variable, you can manage the subsets of data to be compared.



- 
Enter the context name, (e.g. **update_date**) in the **Context** field. Click **OK**.

> **Important:** 
[**HVR Compare**](https://fivetran.com/docs/hvr6/getting-started/concepts/compare) is effective only when the context is enabled. The context can be enabled in the **Contexts** tab of the **Compare Data** dialog (see the steps below).




The resulting configuration for the channel is as follows: 

- 
At the top right menu of the **Channel Details** page, click **Compare Data**.

- 
In the **Compare Data** dialog, click **Tables** and leave only table **Product** selected. 

- 
Under the **Contexts** tab, select context **update_date** (defined in step 6).

- 
Under **Variables**, specify value **sysdate-4** for variable **last_modified** defined on the source and target locations. Expression **sysdate-4** selects only data which is 4 days old. Click **Compare**.

> **Important:** 
SYSDATE is an Oracle function that returns the current date and time set for the operating system on which the database resides. For other DBMSs, the appropriate date/time functions should be used.




- 
Click **Compare Data**. Click the [**View Compare event**](https://fivetran.com/docs/hvr6/user-interface/channels/comparing-data#viewingcompareresults) link to open the **Event Details** page displaying detailed information about the compare event.



You can change the date range for which you want to compare data in locations by specifying different values/expressions for the context variable. For example, if you want to compare data modified on a particular date, you can define the **CompareCondition** for source and target as **last_update>{hvr_var_last_modified} and last_update<{hvr_var_last_modified_n}**.



In this case, the context expressions are defined as follows:


