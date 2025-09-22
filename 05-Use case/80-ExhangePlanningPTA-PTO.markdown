
# Planning of Timetable – Exchange of Data Between Actors in Public Transport

In public transport planning, the exchange of data between involved actors must be **standardised** and allow for the **exchange of smaller parts** of the dataset. This sub-profile outlines the data exchange process through the following steps:

## Process Overview

1. **PTA plans the route offer**
2. **PTA sends the route offer to the PTO** for further planning
3. **PTO may suggest changes** to improve efficiency
4. **PTO performs vehicle planning**, including Dead Runs and Blocks
5. **PTO sends Dead Runs and Blocks back to the PTA**
6. **PTA merges the data** and publishes:
   - To the **NAP** (National Access Point)
   - To **PTO Fleet Management**
   - **Note:** Dead Runs and Blocks are *not* published to the NAP due to being business-sensitive information
7. **Travel planners** and other systems use **NAP data** for travel information
8. **Real-time systems**:
   - Use the full dataset (including Dead Runs, Blocks, and PTO fleet data)
   - Estimate and inform about the status of service production
9. **Real-time systems** publish estimates via **SIRI messages** to travel planners and customer interfaces

> **Note:** This profile describes the exchange of data related to **Blocks and Dead Runs**. Other data types are described in separate profile documents.  
> *(TODO: Include links to related documents)*

---

## PTA Planning

Once the PTA has completed its planning for the **Route Offer**, it sends this to PTOs using **NeTEx standards** in accordance with this profile.  
*(TODO: Add link to the relevant profile)*

[!TODO: Insert image illustrating PTA planning process]

---

## PTO Planning

After receiving the Route Offer, the PTO creates an **operational plan** by defining:

- **Blocks**
- **Dead Runs**

Once the planning is completed, the PTO returns the newly created or updated data to the PTA.

[!TODO: Insert image illustrating PTO planning process]

---

## Example XML Exchange

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Publication from PTO to PTA after the PTO has done the planning of DeadRuns and Blocks - how they think the operation will be
      The PTO has added DeadRuns, DatedVehicleJourneys and Blocks -->

<PublicationDelivery xmlns="http://www.netex.org.uk/netex">
    <PublicationTimestamp>2025-07-03T10:45:00</PublicationTimestamp>
    <ParticipantRef>ENT</ParticipantRef>
    <dataObjects>
        <TimetableFrame version="1" id="ENT:TimeTableFrame:Example">
            <vehicleJourneys>
                <DeadRun version="1" id="ENT:DeadRun:Example" >
                    <!-- DeadRun Data -->
                </DeadRun>
                    <!-- Rest of DeadRuns -->
                <DatedVehicleJourney version="1" id="ENT:DatedVehicleJourney:Example-2025-07-03">
                    <VehicleTypeRef ref="ENT:VehicleType:Example"></VehicleTypeRef>
                    <OperatingDayRef ref="ENTU:OperatingDayRef:Example-2025-07-03"></OperatingDayRef>
                    <!-- DeadRunRef or ServiceJourneyRef -->
                </DatedVehicleJourney>
                <!-- Rest of DatedVehicleJourneys -->
            </vehicleJourneys>
        </TimetableFrame>
        
        <VehicleScheduleFrame version ="1" id="ENT:VehicleScheduleFrame:Example">
            <blocks>
                <Block version="1" id="ENT:Block:Example">
                    <journeys>
                        <!-- Need only ref to DatedVehicleJourney -->
                        <DatedVehicleJourneyRef ref="ENT:DatedVehicleJourney:Example-2025-07-03"></DatedVehicleJourneyRef>
                        <!-- Rest of DatedVehicleJourneyRefs-->
                    </journeys>
                </Block>
            </blocks>
        </VehicleScheduleFrame>
    </dataObjects>
</PublicationDelivery>

```
---

## PTA Merge and Publication
Once planning is finalized, the PTA merges data from all PTOs into a complete dataset and publishes it to:

- NAP for use in travel planner or other customer informaton, following the relevant profile (TODO: Add link to profile)
- To operational systems, including Dead Runs and Blocks

## Object Description

| Exchange | Object Type
|-|-
| PTO → PTA | VehicleScheduleFrame
| PTO → PTA | Block
| PTO → PTA | TimetableFrame
| PTO → PTA | DeadRun
| PTO → PTA | DatedVehicleJourney