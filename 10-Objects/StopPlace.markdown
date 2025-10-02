# StopPlace
>[!NOTE]
>A place comprising one or more locations where vehicles may stop and where passengers may board or leave vehicles or prepare their trip. A STOP PLACE will usually have one or more well-known names.

| Name                 | Type                                | Cardinality | Description |
|----------------------|-------------------------------------|--------------|-------------|
| modification         | ModificationEnumeration             | 0:1         | Type of change (specified as "delete" when the stop is decommissioned). |
| Description          | normalizedString                    | 0:1         | Used only if additional explanatory text is necessary. For example, to describe the status after decommissioning: "physically removed", "signage removed", "untouched", etc. |
| TransportMode        | VehicleModeEnumeration              | 1:1         | Main transport mode available at the stop. See Transport Modes for valid values. |
| AirSubmode           | AirSubmodeEnumeration               | 0:1         | Subcategory for air transport. See Transport Modes for valid values. |
| BusSubmode           | BusSubmodeEnumeration               | 0:1         | Subcategory for bus. See Transport Modes for valid values. |
| FunicularSubmode     | FunicularSubmodeEnumeration         | 0:1         | Subcategory for funicular. See Transport Modes for valid values. |
| MetroSubmode         | MetroSubmodeEnumeration             | 0:1         | Subcategory for metro. See Transport Modes for valid values. |
| TramSubmode          | TramSubmodeEnumeration              | 0:1         | Subcategory for tram. See Transport Modes for valid values. |
| TelecabinSubmode     | TelecabinSubmodeEnumeration         | 0:1         | Subcategory for cable car. See Transport Modes for valid values. |
| RailSubmode          | RailSubmodeEnumeration              | 0:1         | Subcategory for rail. See Transport Modes for valid values. |
| WaterSubmode         | WaterSubmodeEnumeration             | 0:1         | Subcategory for water transport. See Transport Modes for valid values. |
| OtherTransportModes  | VehicleModeListOfEnumerations       | 0:*         | List of other available transport modes (same valid values as the main transport mode). See Transport Modes for valid values. |
| tariffZones          | TariffZoneRef                       | 0:*         | References to fare zones (TariffZone) applicable at the stop. |
| StopPlaceType        | StopTypeEnumeration                 | 1:1         | Classification of the stop: onstreetBus (bus stop), onstreetTram (tram stop), taxiStand (taxi stand), airport (airport), railStation (train station), metroStation (metro station), busStation (bus terminal), harbourPort (car ferry terminal), ferryStop (passenger ferry terminal), liftStation (cable car station). Required when the StopPlace has underlying Quay(s). Not required for multimodal StopPlace. |
| BorderCrossing       | xsd:boolean                         | 0:1         | Indicates whether the stop is a border crossing. |
| Weighting            | InterchangeWeightingEnumeration     | 0:1         | Relative weighting for interchange at the stop: preferredInterchange, recommendedInterchange, interchangeAllowed, noInterchange. Corresponds to interchange priority. |
| quays                | [Quay](Quay.markdown/)                                | 1:* or 0     | List of Quays available at the stop. One or more for standard stops. Always zero for multimodal StopPlaces. |
| accessSpaces         | AccessSpace                         | 0:*         | List of waiting areas at the stop. |
| pathLinks            | PathLink                            | 0:*         | Describes a segment of a walking link. |
| pathJunctions        | PathJunction                        | 0:*         | Point in a walking link where one or more PathLinks connect. |
| navigationPaths      | NavigationPath                      | 0:*         | Description of walking paths at or near the stop. Used only when pathLinks should be overridden or are not applicable. |
