# test-Profile-Documentation
This is a test for collaborative profile documentation
Notes / Ideas for structure:
- **TODO:** Review and harmonize naming conventions with the Transmodel and NeTEx standards.
- Align the structure with Transmodel and NeTEx.
# Table of Contents
- [Foreword](#foreword)
- [MMTIS Requirments](#mmtis-requrements)
- [Glossary](#glossary)
- [Frames](#frames)
- [Common](#common)
- [Reference Data](#reference-data)
- [Publishing Data](#publish-data)
- [Use Cases](#use-case)
# Foreword
**TODO:** Write a foreword to NeTEx, explaining how to understand its parts and profiles. Suggested content structure:
<details>
<summary>Introduction to NeTEx</summary>

## NeTEx

**NeTEx** (Network Timetable Exchange) is a European CEN standard for exchanging public transport data. It defines a comprehensive and flexible XML-based format for:

- Transport networks (routes, stops, operators)
- Timetables and schedules
- Fare structures
- Accessibility
- Operational data

NeTEx is **modular**, meaning it has different parts (frames) for different types of data. It’s designed to support **national and international data exchange**, especially for **multimodal journey planning** and **passenger information systems**.
	
</details>
<details>
<summary>Profiles</summary>

 ## Profiles

Profiles are subsets or specializations of NeTEx. They define **which parts of NeTEx to use**, and **how to use them**, for specific purposes or use cases. Profiles help ensure **interoperability** and **consistency** across systems and countries.

### 🔹 EPIP – European Passenger Information Profile
- A profile of NeTEx focused on **passenger information**.
- Defines a **minimum set of data** needed for journey planning and real-time information.
- Used in systems like **National Access Points (NAPs)** across Europe.

### 🔹 EPIAP – European Passenger Information Accessibility Profile
- Builds on EPIP, but adds **accessibility data** for persons with reduced mobility.
- Includes data about **stop accessibility**, **vehicle features**, and **boarding/alighting conditions**.
- Supports compliance with **PRM TSI** (Technical Specifications for Interoperability).

	
	
</details>
<details>
<summary>Standard (NeTEx) vs Profile</summary>

	
	
## NeTEx vs Profiles

| **Feature**   | **NeTEx**                                      | **Profiles (EPIP, EPIAP, etc.)**                      |
|---------------|------------------------------------------------|--------------------------------------------------------|
| **Scope**     | Full standard with all data structures         | Subset tailored for specific use cases                |
| **Flexibility** | Very flexible and comprehensive              | Restrictive to ensure interoperability                |
| **Use**       | National/international data exchange           | Harmonized implementation across systems              |
| **Complexity**| High – requires configuration                  | Lower – predefined structure                          |
| **Examples**  | All NeTEx frames                               | EPIP, EPIAP, Nordic Profile, DELFI+                   |

</details>
<br/>

# MMTIS Requrements
**TODO:** Determine whether this section is necessary.
# Glossary
**TODO:** Create a glossary of terms, possibly as a table of definitions.
# Frames
**TODO:** Add a short introduction to frames—what they are and what they contain.
- [CompositFrame](/01-Frames/01-CompositFrame.markdown)
- [ResourceFrame](/01-Frames/02-ResourceFrame.markdown)
- [SiteFrame](/01-Frames/03-SiteFrame.markdown)
- [ServiceFrame](/01-Frames/04-ServiceFrame.markdown)
- [ServiceCalendarFrame](/01-Frames/05-ServiceCalendarFrame.markdown)
- [TimetableFrame](/01-Frames/06-TimetableFrame.markdown)
- [VehicleScheduleFrame](/01-Frames/07-VehicleScheduleFrame.markdown)
- [DriverScheduleFrame](/01-Frames/08-DriverScheduleFrame.markdown)
- [FareFrame](/01-Frames/09-FareFrame.markdown)
# Common
**TODO:** Add a short introduction to the "Common" section.
- [DateFormats](/02-Common/01-DateFormats.markdown)
- [Calendars](/02-Common/02-Calendars.markdown)
# Reference Data
**TODO:** Add a short introduction to reference data.
- [Stops](/03-ReferrenceData/01-Stops.markdown)
- [Organisations](/03-ReferrenceData/02-Organisations.markdown)
- [VehicleType](/03-ReferrenceData/03-VehicleType.markdown)
- [Vehicle](/03-ReferrenceData/04-Vehicle.markdown)
# Publish Data
**TODO:** Add a short introduction to this section. It should describe how data is published in different scenarios and use cases.
- [How to publish FareZone](/04-PublishData/40-PublishFareZone.markdown)
# Use Case
**TODO:** Add a short introduction explaining the purpose of use cases—when and why they are used, and how they help describe the application of profiles.
Each use case should include:
- Required fields and frames
- Relevant objects
- Real-world examples

Use Cases and descriptions


**Proposed Use Cases (to be modeled in examples and separate documentation files):**
- **Stops**
	- Accesibility (with images, as Johan is doing with stops)
- **Organisations**
- **Timetables**
- **Timetables with booking**
- **FareZones**
- **Fares**
	- Documentation of relevant objects and fields 
