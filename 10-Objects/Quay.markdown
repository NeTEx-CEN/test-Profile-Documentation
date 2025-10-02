# Quay
>[!NOTE]
>A part of a [StopPlace](StopPlace.markdown) where passengers can board and alight vehicles (e.g., bus bay, train platform, or airport gate).

>### Important:
> - A name should **not** be set per Quay (it is inherited from the parent StopPlace.
>- `QuayType` should **not** be specified, but instead derived from `TransportMode` / `StopPlaceType` (as the NeTEx profile does not allow modelling of multimodal Quays under the same StopPlace).


| Name              | Type                        | Cardinality | Description |
|-------------------|-----------------------------|-------------|-------------|
| PrivateCode       | xsd:normalizedString        | 0:1         | Internal code not used in public services. |
| PublicCode        | xsd:normalizedString        | 0:1         | Public code for the Quay (e.g., code displayed on signage). |
| modification      | xs:ModificationEnumeration  | 0:1         | Type of change (specified as "delete" when a single Quay at a stop is decommissioned). |
| CompassBearing    | AbsoluteBearingType         | 0:1         | Orientation in degrees. |
| boardingPositions | BoardingPosition            | 0:*         | List of boarding/alighting points along the Quay (typically A, B, C, D, etc.). Used only for trains. |
