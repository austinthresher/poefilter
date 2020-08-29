from poefilter import *
import tables
import colors
import styles
import hide

from sounds import Sounds
from icons import Icons
from colors import Colors

# Filter configuration
# ====================
class Config:
    main_socket_groups = ["BBG", "RRG", "GGG", "BBB"]
    other_socket_groups = ["BG", "RG", "GG"]
    # str, dex, int, strdex, strint, dexint
    armour_types = ["int"]
    # List of weapon item classes to show. Strings must be the exact item class.
    weapon_types = ["Wands", "Rune Daggers"]
    # Trinket BaseTypes to add highlights to
    highlighted_rings = ["Sapphire"]
    highlighted_belts = ["Leather", "Rustic"]
    highlighted_amulets = ["Jade"]
    # Other options
    show_5_links = True

# The first section of the filter is styling ONLY. There should be no
# hide() statements here. After all styling is applied, items can then
# be hidden by the second portion of the filter.
set_always_continue(True)
styles.apply(config=Config, colors=Colors, icons=Icons, sounds=Sounds)

# This section of the filter is where items are actually hidden.
# Up to this point, every block had an implicit Continue.
set_always_continue(False)
hide.apply(config=Config, colors=Colors, icons=Icons, sounds=Sounds)
