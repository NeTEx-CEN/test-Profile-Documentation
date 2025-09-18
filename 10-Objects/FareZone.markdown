# FareZone

## Introduction to FareZones

FareZone is a specialization of TariffZone. FareZone present additional concepts relating to the network that is needed to underpin fare structures.
>[!NOTE] 
>This profile mandates the use of FareZone rather than TariffZone for any use case that aim to provide fare products and prices.

FareZones define the permanent zones of a network, and thus also the geographic areas where a ticket is valid for use. FareZones can be used to calculate the fare in several ways. In this profile the following are described:
- *stage count with zone as unit*: the price between two stops is defined by counting the number of FareZones the journey passes through 
- *zone to zone*: the price is stated based on a pair of origin and destination zones, possibly with restrictions on the route between the start and end zone
- *flat for a group of zones*: see [GroupOfTariffZones](/10-Objects/GroupOfTariffZones.markdown)

>[!NOTE] 
>The number of FareZones a ticket is valid for may differ from the number used in fare calculation.

Each FareZone is managed by a transport authority, referenced in the *authorityRef* field. ~~The valid area for a FareZone is described by a polygon in the `geometry` field. ~~

To calculate the price of a journey across multiple FareZones based on the count of zone traversals, each zone's neighburs must be specified. This is done in the `neighbours` element, which lists all neighbouring FareZones.

#### Relating tariffs to the network

For a trip planner or fare engine to be able to select the available fares, it must be possible to relate the spatial description of a FareZone to stops in a timetabled journey chosen by a traveller. This profile supports the following methods:
- explicitly: membership of stops in a zone is stated by a link
- implicitly by projection: membership is determined by examining if the coordinates of the stop is within the polygon that describes the zone. This method requires the polygon element on the zone. *EFIP draft says explicit only*
Note that spatial containment do not always imply membership in a zone, e.g. a stop used for water transport mode is not automatically a member in a zone used for road based tariffs.

The name and description of a FareZone is mandatory as it is customer facing when used as a fare structure, which describes where the customer may travel.

FareZones can be grouped according to a functional purpose by use of a [GroupOfTariffZones](/10-Objects/GroupOfTariffZones.markdown)



| **Name**|**Type**|**Cardinality**|**Description** |**Example**|
|-|-|-|-|-|
||FareZone inherits from TariffZone|||
|Id| FareZoneIdType | 1:1| Identifier of FareZone | |
|`ValidBetween` | `ValidBetween`| `0:1`| Fromdate and todate for the FareZone, controls when a zone becomes valid or expires `Required in this profile?` ||
|privateCodes| PrivateCode | 0:* | A list of private codes that uniquely identify the FareZone. May be used for inter-operating with other systems (v2.0)| 119|
|`Name`| `MultilingualString`| `1:1` | Name of the FareZone `Required in this profile`| Ål |
|`Description`| `MultilingualString`| `1:1` | Description of the FareZone `Required in this profile` | Ål kommune |
|Polygon|gml:Polygon| 0:1| Geographic area/polygon associated with zone. <br>`Mandatory if `*scopingMethod*` is `*implicitSpatialProjection* <br/> optional if *scopingMethod* is *explicitStops*| |
|publicCode| publicCodeStructure | 0:1 | Additional code identifying the zone to the public as an alternative to a name (v2.0)|B|
|zoneTopology| ZoneTopologyEnum | `1:1` | Topology of the FareZones with regard to other zones. `Required in this profile` Allowed values: nested, tiled, sequence, overlappingSequence Present in NeTEx but not included in this profile: ~~ring, annular, other~~ | |
|scopingMethod| ScopingMethodEnum | 0:1| How stops within the zone are included. Default is *explicitStops*. Allowed values: *explicitStops*, *implicitSpatialProjection*. Present in NeTEx but not included in this profile: ~~explicitPeripheryStops~~ ||
|TransportOrganisationRef| (TransportOrganisationRef) OperatorRef or AuthorityRef| `1:1` |Reference to the organisation that manages the zone `Required in this profile` |BRA:Authority:1| |
|neighbours|FareZoneRef| 0:*| Adjacent FareZones `Required in this profile for stage count using zones as unit`|BRA:FareZone:3; BRA:FareZone:5||


# Further details

## Naming Conventions 

(updated according to https://github.com/NeTEx-CEN/NeTEx/pull/849)

The name of the zone is essential to convey to travellers where they can travel and so it is considered mandatory in this profile. The name must be given in the local language, and should include translated names if neccessary. 
In Norway, all names including FareZone names should be present in Bokmål, Nynorsk and English. 

- Names should not be abbreviated.
- Avoid special characters.
- Names should be identical or clearly recognizable to customers compared to naming used in other information channels.
- If the *publicCode* element is included, the zone name must **not** contain a code.

Example: 
```
 <FareZone version="1" id="TRO:FareZone:1">
    <Name>
        <Text lang="nob">Storfjord og Kåfjord</Text>
        <Text lang="nno">Storfjord og Kåfjord</Text>
        <Text lang="en">Storfjord and Kåfjord</Text>
    </Name>
</FareZone>
```


## TransportOrganisationRef restricted to AuthorityRef Reference (Norway)

The `TransportOrganisationRef` element is ecpected to be an AuthorityRef, and to an ID from the route data that is associated with the zone. <font color="red"> TBD If other authorities need to use the same zone, a new zone must be created for that purpose. This new zone can be identical to the previous one but must have a unique ID and a different `authorityRef`</font>.

## ScopingMethod

The `ScopingMethod` is a technical marker indicating how stops within the zone's polygon are handled. There are two valid values:

- `explicitStops`: All stops to be included must be explicitly listed.
- `implicitSpatialProjection`: All stops within the polygon are implicitly part of the zone and can be used with a zone ticket.

Stops included in a zone using `explicitStops` must be listed under `members` to be associated with the zone. Use `StopPlace` IDs (e.g., `NSR:StopPlace:1234`).

## ZoneTopology

The `zoneTopology` field describes how the zones are laid out. The most common value in Norway is:

- `tiled`: Zones are drawn edge-to-edge without gaps.

Another value is:

- `sequence`: Zones are still adjacent and travel is allowed between them, but in FareZones this should be handled using the `neighbours` field.

## Neighbouring Zones

Neighbouring zones allow travel between them on the same ticket. Even if zones are adjacent on the map, the terrain may prevent actual travel (e.g., mountains or forests). Therefore, only zones that are **actually reachable** should be listed in the `neighbours` field using their IDs. 

Zones should point to each other, but one-way references are also permitted.

## Separate Zone Structures

It is possible to create overlapping or duplicated zones for different purposes. These must still have unique IDs within the `codespace`, but may have different `authorityRef` values and/or belong to different `GroupOfTariffZones`.


# Example FareZone
>[!NOTE]: This example is part of a delivery of FareZones within a PublicationDelivery where the FareZones is part of the SiteFram

      <tariffZones>
        <FareZone version="1" id="VOT:FareZone:19">
            <ValidBetween>
                <FromDate>2021-03-09T00:00:00</FromDate>
            </ValidBetween>
            <Name lang="nor">Kongsberg</Name>
            <PrivateCode>630</PrivateCode>
            <members>
                <ScheduledStopPointRef ref="NSR:StopPlace:16845"/>
                <ScheduledStopPointRef ref="NSR:StopPlace:16848"/>
            </members>
            <ns2:Polygon ns2:id="GEN-PolygonType-10673396">
                <ns2:exterior>
                    <ns2:LinearRing>
                        <ns2:posList>59.69729474436 9.56136557616  59.58258879394 9.91558959938 59.46601814332 9.97880295769 59.46843265215 9.82246394625 59.69729474436 9.56136557616</ns2:posList>
                    </ns2:LinearRing>
                </ns2:exterior>
            </ns2:Polygon>
            <ZoneTopology>tiled</ZoneTopology>
            <ScopingMethod>explicitStops</ScopingMethod>
            <AuthorityRef ref="VOT:Authority:VTFK_ID"/>
            <neighbours>
                <FareZoneRef ref="VOT:FareZone:17"/>
                <FareZoneRef ref="VOT:FareZone:14"/>
            </neighbours>
        </FareZone>
      </tariffZones>
