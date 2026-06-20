# User Properties - HVR 6 | Fivetran Documentation

**Source:** https://fivetran.com/docs/hvr6/property-reference/user-properties

---


[Edit on GitHub](https://github.com/fivetran/engineering/blob/main/docs/hvr6/property-reference/user-properties/index.md)

# User and User Hub Properties


This section lists and describes the Fivetran HVR user properties and user hub properties. These properties can only be changed by the user (for whom the property is assigned to), or a user who has **SysAdmin** permission, using the command [**hvruserconfig**](https://fivetran.com/docs/hvr6/command-line-interface/command-reference/hvruserconfig).

> **Note:** 
An array property and map property can store multiple values. The syntax for updating them from the [Command Line Interface (CLI)](https://fivetran.com/docs/hvr6/command-line-interface/managing-properties-in-cli) varies.


---

## User Properties


User properties define the characteristics or attributes of an HVR user that apply across all hubs the user can access. They store the user's [UI preferences](https://fivetran.com/docs/hvr6/user-interface/user-preferences).

---

### Avatar


**Description:** Stores the user's profile image, which is displayed in the HVR UI.

---

### Column_Visibility_Channels


**Description:** Stores the user's HVR UI preferences for column visibility.

This is a map property that can store multiple values.

---

### Column_Visibility_Event_Results


**Description:** Stores the user's HVR UI preferences for column visibility.

This is a map property that can store multiple values.

---

### Column_Visibility_Events


**Description:** Stores the user's HVR UI preferences for column visibility.

This is a map property that can store multiple values.

---

### Column_Visibility_Jobs


**Description:** Stores the user's HVR UI preferences for column visibility.

This is a map property that can store multiple values.

---

### Column_Visibility_Locations


**Description:** Stores the user's HVR UI preferences for column visibility.

This is a map property that can store multiple values.

---

### Column_Visibility_Tables


**Description:** Stores the user's HVR UI preferences for column visibility.

This is a map property that can store multiple values.

---

### Compact_Mode


**Description:** Stores the user's HVR UI layout preference - **true** indicates the Compact layout, and **false** indicates the default (expanded) layout.

---

### Full_Name


**Argument:** *name*

**Description:** Name of the user.

---

### Num_Events_Initially


**Description:** Stores the user's HVR UI preferences for the number of events initially shown in the [Events](https://fivetran.com/docs/hvr6/user-interface/events) page.

---

### Previous_Hub


**Description:** Stores the user's HVR UI preferences.

---

### Show_Alpha_Features


**Description:** Stores the user's HVR UI preferences for alpha feature visibility.

---

### Show_Deprecated_Features


**Argument:**

**Description:** Stores the user's HVR UI preferences for deprecated feature visibility.

---

### Show_Inactive_Jobs


**Description:** Stores the user's HVR UI preferences for showing inactive [jobs](https://fivetran.com/docs/hvr6/user-interface/jobs) in the UI.

---

### Show_Internal_Jobs


**Description:** Stores the user's HVR UI preferences for showing internal [jobs](https://fivetran.com/docs/hvr6/user-interface/jobs) in the UI.

---

### Suggested_Rows_Per_Slice


**Description:** Stores the user's HVR UI preferences regarding [slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing).

---

### Suggested_Slices_Per_Table


**Description:** Stores the user's HVR UI preferences regarding [slicing](https://fivetran.com/docs/hvr6/getting-started/concepts/slicing).

---

### Theme


**Description:** Stores the user's HVR UI preferences for the color theme.

---

### TimeSeries_Metrics


**Description:** Stores the user's HVR UI preferences.

This is an array property that can store multiple values.

---

### Topology_Animation


**Description:** Stores the user's HVR UI preferences for animation in the [Topology](https://fivetran.com/docs/hvr6/user-interface/topology) page.

---

### Topology_Preferences


**Description:** Stores the user's HVR UI preferences for the location properties and metrics displayed on the [Topology](https://fivetran.com/docs/hvr6/user-interface/topology) page.

---

## User Hub Properties


User hub properties define the characteristics or attributes of an HVR user that apply only to a specific hub the user can access. They store the user's [UI preferences](https://fivetran.com/docs/hvr6/user-interface/user-preferences) for that hub.

---

### Graph_Range_Period


**Description:** Stores the user's HVR UI preferences regarding the graph range period displayed on the [Statistics](https://fivetran.com/docs/hvr6/user-interface/statistics) or [Topology](https://fivetran.com/docs/hvr6/user-interface/topology) page.

---

### Ignored_Warnings


**Description:** Stores the user's HVR UI preferences.

This is a map property that can store multiple values.

---

### Latency_Colors


**Description:** Stores the user's HVR UI preferences regarding the latency colors displayed on the [Topology](https://fivetran.com/docs/hvr6/user-interface/topology) page.

---

### Latency_Manual_Limit


**Description:** Stores the user's HVR UI preferences.

---

### Recent_Errors_Seen


**Description:** Stores the user's HVR UI preferences.

This is a map property that can store multiple values.

.actparam {
    padding-left: 20px;
}
