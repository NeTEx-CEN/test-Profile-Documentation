
# DatedServiceJourney
    
>[!NOTE]
>A particular ServiceJourney of a vehicle on a particular OperatingDay.
>
>Operational details of the DatedServiceJourney is derived from a referenced generic ServiceJourney. The generic Journey cannot specify dayTypes when this is defined by the OperatingDay of the DatedServiceJourney.

        
    
### Normal planned journey 
Referencing a [ServiceJourney](ServiceJourney.md) adding a OperatingDay to the Journey's calender and a unique identifier for this connection

```xml
<DatedServiceJourney version="1" id="ENT:DatedServiceJourney:Planned_example" derivedFromObjectRef="">
    <ServiceJourneyRef ref="ENT:ServiceJourney:Example_1"/>
    <OperatingDayRef ref="ENT:OperatingDay:2025-03-06"/>
</DatedServiceJourney>
```
### A cancellation of a journey

```xml
<DatedServiceJourney version="1" id="ENT:DatedServiceJourney:Cancelled_example">
    <ServiceAlteration>cancellation</ServiceAlteration>
    <ServiceJourneyRef ref="ENT:ServiceJourney:Example_1"/>
    <OperatingDayRef ref="ENT:OperatingDay:2025-03-06"/>
</DatedServiceJourney>
```
### Journey beeing replaced

```xml
<DatedServiceJourney version="1" id="ENT:DatedServiceJourney:Replaced">
    <ServiceAlteration>replaced</ServiceAlteration>
    <ServiceJourneyRef ref="ENT:ServiceJourney:Example_1"/>
    <OperatingDayRef ref="ENT:OperatingDay:2025-03-06"/>
</DatedServiceJourney>
```
### Replacement journey
The replacement service uses DatedServiceJourneyRef to tie together with the original journey

```xml
<DatedServiceJourney version="1" id="ENT:DatedServiceJourney:Replacement_Bus_1">
    <ServiceJourneyRef ref="ENT:ServiceJourney:Example_bus_1"/>
    <replacedJourneys>
        <DatedVehicleJourneyRef ref="ENT:DatedServiceJourney:Replaced"/>
    </replacedJourneys>
    <OperatingDayRef ref="ENT:OperatingDay:2025-03-06"/>
</DatedServiceJourney>
```
