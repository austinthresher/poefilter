from poefilter import *
import tables
import colors
import styles
import visibility

from sounds import Sounds
from icons import Icons
from colors import Colors


# Notes:
# Different color for 4link + desired sockets
# Don't overwrite the 4link color with desired socket color
# Filter out more normal gear without good links
# TODO: Highlight high ilvl items
# FIXME: everything with a custom drop sound should have an icon
# FIXME: Incursion Stone of Passage doesn't get highlighted

# Filter configuration
# ====================
class Config:
    highlighted_3L = [ "RRG", "GGR" ] #["BBG", "BBB", "GGB"]
    highlighted_4L = [ "RRR", "GGG", "RRG", "GGR" ] #["BBG", "BBB", "GGB", "GGG"]
    # str, dex, int, strdex, strint, dexint
    armour_types = ["dex", "strdex", "str"]
    # List of weapon item classes to show. Strings must be the exact item class.
    weapon_types = ["One Hand Axes"]
    # Trinket BaseTypes to add highlights to
    highlighted_rings = ["Ruby", "Sapphire", "Topaz", "Iron"]
    highlighted_belts = ["Rustic"]
    highlighted_amulets = ["Lapis"]
    # Other options
    show_5_links = True
    # -1:none, 0:bottom, 1:lower, 2:low, 3:mid, 4:high, 5:higher
    hide_div_tier = 0
    hide_proph_tier = 0
    hide_unique_tier = -1

# The first section of the filter is styling ONLY. There should be no
# hide() statements here. After all styling is applied, items can then
# be hidden by the second portion of the filter.
set_always_continue(True)
styles.apply(config=Config, colors=Colors, icons=Icons, sounds=Sounds)

# This section of the filter is where items are actually hidden.
# Up to this point, every block had an implicit Continue.
set_always_continue(False)
visibility.apply(config=Config)
