TOWN_LIST = [
    "Nuvema Town",
    "Accumula Town",
    "Striaton City",
    "Nacrene City",
    "Castelia City",
    "Nimbasa City",
    "Driftveil City",
    "Mistralton City",
    "Icirrus City",
    "Opelucid City",
    "Lacunosa Town",
    "Undella Town",
]

DEFAULT_STARTING_TOWN = "Nuvema Town"

STARTING_HOUSES = {
    #                      outside_zone, outside_warp, inside_zone, inside_warp
    "Nuvema Town":        (389,   0,   390,   0),
    "Accumula Town":      (397,   4,   405,   0),
    "Striaton City":      (  6,   3,    13,   0),
    "Nacrene City":       ( 16,   1,    21,   0),
    "Castelia City":      ( 28,  12,    42,   0),
    "Nimbasa City":       ( 62,  11,    93,   0),
    "Driftveil City":     ( 96,   3,   102,   0),
    "Mistralton City":    (107,   1,   112,   1),
    "Icirrus City":       (113,   2,   116,   0),
    "Opelucid City":      (120,   5,   127,   0),
    "Lacunosa Town":      (406,   1,   408,   0),
    "Undella Town":       (412,   3,   416,   0),
}

#  Warp helpers
def _warp_offset(zone_file: bytearray, warp_id: int) -> int:
    """Byte offset of warp `warp_id` inside a a/1/2/5 zone file."""
    return 8 + 20 * zone_file[4] + 36 * zone_file[5] + 20 * warp_id


def _set_warp_target(zone_file: bytearray, warp_id: int,
                     dest_zone: int, dest_warp: int) -> None:
    """Point a warp at (dest_zone, dest_warp), leaving its other 16 bytes alone."""
    off = _warp_offset(zone_file, warp_id)
    if off + 4 > len(zone_file):
        raise IndexError(
            "warp %d does not exist in this zone file (only %d bytes)"
            % (warp_id, len(zone_file))
        )
    zone_file[off:off + 4] = (dest_zone.to_bytes(2, "little")
                              + dest_warp.to_bytes(2, "little"))



#   The Mistralton City house has three 1-tile warps for some reason
EXTRA_INTERIOR_EXITS = {
    "Mistralton City": (0, 2),
}
