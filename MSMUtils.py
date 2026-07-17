from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from . import MSMWorld


courts_by_sport = {
    "Basketball": [
        "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle", "DK Dock",
        "Luigi's Mansion", "Western Junction", "Daisy Garden", "Wario Factory",
        "Bowser Jr. Blvd.", "Bowser's Castle", "Ghoulish Galleon", "Star Ship"
    ],
    "Dodgeball": [
        "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle", "DK Dock",
        "Toad Park", "Western Junction", "Daisy Garden", "Wario Factory",
        "Bowser's Castle", "Waluigi Pinball", "Ghoulish Galleon", "Star Ship"
    ],
    "Volleyball": [
        "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle", "DK Dock",
        "Luigi's Mansion", "Western Junction", "Wario Factory", "Bowser Jr. Blvd.",
        "Bowser's Castle", "Waluigi Pinball", "Ghoulish Galleon", "Star Ship"
    ],
    "Hockey": [
        "Mario Stadium", "Koopa Troopa Beach", "Peach's Castle", "Toad Park",
        "Western Junction", "Daisy Garden", "Wario Factory", "Bowser Jr. Blvd.",
        "Bowser's Castle", "Waluigi Pinball", "Ghoulish Galleon", "Star Ship"
    ]
}

courts_list = ["Mario Stadium", "Koopa Troopa Beach", "Toad Park", "DK Dock", "Peach's Castle","Daisy Garden",
               "Luigi's Mansion", "Wario Factory", "Bowser Jr. Blvd.", "Bowser's Castle", "Waluigi Pinball",
               "Western Junction", "Ghoulish Galleon", "Star Ship"]

def find_num_exhibition_locs(enabled_sports, exhibition_difficulty):
    """Return the number of exhibition checks that this configuration creates.

    Sports Mix is a selectable sport but has no exhibition locations. Counting
    the generated names rather than applying a formula prevents it (and any
    future non-exhibition sport) from inflating the Exhibition Tour goal.
    """
    return len(generate_exhibition_locations(enabled_sports, exhibition_difficulty))


def generate_exhibition_locations(sports, difficulties):
    locations = []

    for diff in difficulties:
        for sport in sports:
            if sport != "Sports Mix":
                courts = courts_by_sport.get(sport, [])

                for court in courts:
                    locations.append(f"{sport} Ex: Beat {court} ({diff})")

    return locations