## ZoneTopologyEnumeration

Allowed values for Fare Zone Topology. Describes how FareZones are positioned with regard to other zones.
The topology is essential for fare engines to be able to deduce how many zones to base the fare on in zone counting scenarios.

| **Allowed values** | **Description** |
|-|-|
|overlapping|Zones are of arbitrary shape and may overlap. |
|honeycomb|Zones are arranged as a tiled honeycomb of regular polygons (e.g. Hexagons, squares etc. The zones are contiguous and do not overlap. |
|~~ring~~|Zones are arranged in rings . The nested inner zones are included in any containing  outer zones. Present in NeTEx but not included in this profile|
|~~annular~~|Zones are arranged in tiled hollow rings. The area of any  immediately nested zone  is excluded from the  containing  outer zone. Present in NeTEx but not included in this profile|
|nested|Zones are nested, that is some zones are fully contained within other zones and are automatically included if the outer zone is selected. They may also overlap their neighbours. |
|tiled| Zones are arranged as adjacent tiles or arbitrary shapes that do not overlap. |
|sequence| Zones are arranged as adjacent tiles in sequence that touch at either or both ends. They do not overlap. |
|overlappingSequence|Zones are arranged as adjacent tiles in sequence that touch at either or both ends. They may partially overlap such that some stops are in both zones. |
