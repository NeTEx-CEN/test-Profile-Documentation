## ScopingMethodEnumeration

Allowed values for FARE ZONE scoping method. The scoping method indicates how FARE ZONES are reletad to stops.

| **Allowed values** | **Description** |
|-|-|
| explicitStops | Stops that are members of the zone are explicitly listed. |
| implicitSpatialProjection | Any stop that is spatially contained within the zone is assumed to be a  member. |
| ~~explicitPeripheryStops~~ | ~~The extent of the zone is indicated by a set of stops marking the border points on the periphery of the FARE ZONE. Any stop that is spatially contained within the indicated zone is assumed to be a  member.~~  Present in NeTEx but not included in this profile |