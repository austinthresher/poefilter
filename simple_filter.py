from poefilter import *
import tables
import colors

# Filter configuration
# ====================

main_socket_groups = ["BBG", "RRG", "GGG"]
other_socket_groups = ["BG", "RG", "GG"]
# str, dex, int, strdex, strint, dexint
armour_types = ["int"]
# thrusting, bows, wands, axes1, axes2, maces1, maces2, swords1, swords2,
# sceptres, warstaves, staves, claws, rune daggers, daggers
weapon_types = ["wands", "rune daggers"]

always_show_magic_until = 13
always_show_rare_until = 23
always_show_unique_until = 68

highlighted_rings = ["Sapphire"]
highlighted_belts = ["Leather", "Rustic"]
highlighted_amulets = ["Jade"]

# Start of actual filter
# ======================


default = Style(
        background="0 0 0",
        text="255 0 255",
        border="255 255 255 0",
        size=45)

hidden = Style(size=28)

class Icons:
    extremely_valuable = Style(
            play_effect_color="Red",
            minimap_icon_size=0,
            minimap_icon_color="Red",
            minimap_icon_shape="Star")
    very_valuable = Style(
            play_effect_color="Red",
            minimap_icon_size=1,
            minimap_icon_color="Red",
            minimap_icon_shape="Star")
    valuable = Style(
            play_effect_color="Red",
            play_effect_temp=True,
            minimap_icon_size=2,
            minimap_icon_color="Red",
            minimap_icon_shape="Star")

class Sounds:
    exalt = Style(alert_sound_id=1, alert_sound_volume=300)
    divine = Style(alert_sound_id=2, alert_sound_volume=300)
    good_unique = Style(alert_sound_id=3, alert_sound_volume=300)
    something = Style(alert_sound_id=4, alert_sound_volume=300)
    great_unique = Style(alert_sound_id=5, alert_sound_volume=300)
    very_interesting = Style(alert_sound_id=6, alert_sound_volume=300)
    long_wobble = Style(alert_sound_id=7, alert_sound_volume=300)
    medium_wobble = Style(alert_sound_id=8, alert_sound_volume=300)
    shorter_wobble = Style(alert_sound_id=9, alert_sound_volume=300)
    bang = Style(alert_sound_id=10, alert_sound_volume=300)
    chaos = Style(alert_sound_id=11, alert_sound_volume=300)
 
# Categories without rarity
class Theme:
    # Class Currency
    extremely_valuable = Style(
            text="255 0 0 255",
            background="255 255 255 255",
            size=45)
    very_valuable = Style(
            text="179 36 30 255",
            background="255 248 229",
            size=45)
    valuable = Style(
            text="255 248 229 255",
            background="193 43 19 255")
    magic_orbs = Style(
            text="171 232 240",
            background="17 109 130")
    other_orbs = Style(
            text="255 216 206",
            background="20 20 20")
    quality = Style(
            text="197 195 147",
            background="52 74 72")
    map_currency = Style(
            text="204 212 191",
            background="62 93 121")
    prophecies = Style(
            text="220 156 208",
            background="126 34 103")
    shards = Style(
            text="120 148 170",
            background="90 98 83")
    essences = Style(
            text="192 0 0",
            background="20 20 20")
    other_currency = Style(
            text="225 211 191",
            background="20 20 20")
    vials = Style(
            text="239 166 172",
            background="225 109 118")
    delve = Style(
            text="249 202 61",
            background="0 71 64")
    catalysts = Style(
            text="255 250 165",
            background="154 170 252")
    oils = Style(
            text="229 253 231",
            background="232 113 145")
    delirium = Style(
            text="232 235 233",
            background="45 81 94")
    wisdom = Style(
            text="#b7b7a4",
            border="#b7b7a4ff",
            background="59 12 4")
    portal = Style(
            text="#b7b7a4",
            border="#b7b7a4ff",
            background="8 63 127")
    transmute = Style(
            text="171 232 240",
            background="17 109 130")

    # Class Fragments
    frags = Style(
            text="158 209 239",
            background="145 33 47")
    breachstones = Style(
            text="208 247 255",
            background="92 109 91")
    emblems = Style(
            text="24 48 58",
            background="216 229 220")
    scarabs = Style(
            text="252 254 217",
            background="105 116 162")

    # Other classes
    quest = Style(
            text="59 192 41",
            background="20 20 20")
    incubators = Style(
            text="201 192 179",
            background="78 38 13")
    divination = Style(
            text="100 206 254 255",
            background="9 23 70 220")
    awakened_gems = Style(
            text="0 0 0 255",
            background="240 92 36 255",
            minimap_icon_size=1,
            minimap_icon_color="Cyan",
            minimap_icon_shape="Hexagon",
            play_effect_color="Cyan")
    drop_gems = Style(
            text="0 0 0 255",
            background="106 212 177 255",
            minimap_icon_size=2,
            minimap_icon_color="Cyan",
            minimap_icon_shape="Hexagon",
            play_effect_color="Cyan")
    gems = Style(
            text="98 201 202",
            background="60 98 99")
    metamorph = Style(
            text="225 255 94",
            background="59 89 65")
    seeds = Style(
            text="227 214 195",
            background="103 89 71")
    # TODO: piece

    # Default colors for rarity
    rarity_normal = Style(
            text="200 200 200 220",
            #border="200 200 200 128",
            background="20 20 20 200",
            size=35)

    rarity_magic = Style(
            text="56 171 255 255",
            #border="56 171 255 192",
            background="20 20 20 220",
            size=38)

    rarity_rare = Style(
            text="255 255 119 255",
            #border="255 255 119 220",
            background="20 20 20 255",
            size=42)

    rarity_unique = Style(
            text="239 132 18 255",
            #border="239 132 18 255",
            background="20 20 20 255",
            size=45,
            play_effect_color="Brown",
            minimap_icon_size=1,
            minimap_icon_color="Brown",
            minimap_icon_shape="Diamond")

    # Colors for attribute gear

    attr_str = [
            "40 0 0 160",
            "40 0 0 192",
            "40 0 0 220",
            "40 0 0 255"]
    attr_dex = [
            "0 40 0 160",
            "0 40 0 192",
            "0 40 0 220",
            "0 40 0 255"]
    attr_int = [
            "0 0 40 160",
            "0 0 40 192",
            "0 0 40 220",
            "0 0 40 255"]
    attr_strdex = [
            "25 25 0 160",
            "25 25 0 192",
            "25 25 0 220",
            "25 25 0 255"]
    attr_strint = [
            "25 0 25 160",
            "25 0 25 192",
            "25 0 25 220",
            "25 0 25 255"]
    attr_dexint = [
            "0 25 25 160",
            "0 25 25 192",
            "0 25 25 220", 
            "0 25 25 255"]

    # Influences
    shaper = Style(
            text="0 0 0 255",
            background="#3c78d8ff",
            border="#ffffffff",
            size=45)
    elder = Style(
            text="0 0 0 255",
            background="#8e7cc3ff",
            border="#ffffffff",
            size=45)
    warlord = Style(
            text="0 0 0 255",
            background="#ffd966ff",
            border="#ffffffff",
            size=45)
    hunter = Style(
            text="0 0 0 255",
            background="#6aa84fff",
            border="#ffffffff",
            size=45)
    redeemer = Style(
            text="0 0 0 255",
            background="#9fc5e8ff",
            border="#ffffffff",
            size=45)
    crusader = Style(
            text="0 0 0 255",
            background="#cc4125ff",
            border="#ffffffff",
            size=45)

    # Notable highlights

    corrupted = Style(border="210 0 0 255")
    veiled = Style(border="70 207 119 255")
    enchanted = Style(border="242 205 233 255")
    corrupted_enchanted = Style(border="255 0 255 255")

    good_sockets = Style(border="0 255 0 255")
    ok_sockets = Style(border="30 100 30 255")

    # Styles applied for each rarity
    abyss = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    jewels = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    cluster = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    watchstones = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    maps = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    highlighted_amulets = [
            Style(text="255 255 255 255", background="62 86 81 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="62 86 81 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="62 86 81 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="62 86 81 255", border="255 255 255 255"),
        ]
    amulets = [
            Style(background="62 86 81 255"),
            Style(background="62 86 81 255"),
            Style(background="62 86 81 255"),
            Style(background="62 86 81 255"),
        ]
    highlighted_rings = [
            Style(text="255 255 255 255", background="44 51 62 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="44 51 62 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="44 51 62 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="44 51 62 255", border="255 255 255 255"),
        ]
    rings = [
            Style(background="44 51 62 255"),
            Style(background="44 51 62 255"),
            Style(background="44 51 62 255"),
            Style(background="44 51 62 255"),
        ]
    highlighted_belts = [
            Style(text="255 255 255 255", background="95 79 82 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="95 79 82 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="95 79 82 255", border="255 255 255 255"),
            Style(text="255 255 255 255", background="95 79 82 255", border="255 255 255 255"),
        ]
    belts = [
            Style(background="95 79 82 220"),
            Style(background="95 79 82 220"),
            Style(background="95 79 82 220"),
            Style(background="95 79 82 220"),
        ]
    life_flasks = [
            Style(background="125 13 53 220"),
            Style(background="125 13 53 220"),
            rarity_rare, 
            Style(background="125 13 53 255"),
        ]
    mana_flasks = [
            Style(background="32 48 126 220"),
            Style(background="32 48 126 220"),
            rarity_rare, 
            Style(background="32 48 126 255"),
        ]
    hybrid_flasks = [
            Style(background="73 27 76 220"),
            Style(background="73 27 76 220"),
            rarity_rare, 
            Style(background="73 27 76 255"),
        ]
    utility_flasks = [
            Style(background="0 77 67 220"),
            Style(background="0 77 67 220"),
            rarity_rare, 
            Style(background="0 77 67 255"),
        ]
    str_armour = [
            Style(background=attr_str[0]),
            Style(background=attr_str[1]),
            Style(background=attr_str[2]), 
            Style(background=attr_str[3]) 
        ]
    dex_armour = [
            Style(background=attr_dex[0]),
            Style(background=attr_dex[1]),
            Style(background=attr_dex[2]), 
            Style(background=attr_dex[3]) 
        ]
    int_armour = [
            Style(background=attr_int[0]),
            Style(background=attr_int[1]),
            Style(background=attr_int[2]), 
            Style(background=attr_int[3]) 
        ]
    strdex_armour = [
            Style(background=attr_strdex[0]),
            Style(background=attr_strdex[1]),
            Style(background=attr_strdex[2]), 
            Style(background=attr_strdex[3]) 
        ]
    strint_armour = [
            Style(background=attr_strint[0]),
            Style(background=attr_strint[1]),
            Style(background=attr_strint[2]), 
            Style(background=attr_strint[3]) 
        ]
    dexint_armour = [
            Style(background=attr_dexint[0]),
            Style(background=attr_dexint[1]),
            Style(background=attr_dexint[2]), 
            Style(background=attr_dexint[3]) 
        ]
    str_weapons = [
            Style(background=attr_str[0]),
            Style(background=attr_str[1]),
            Style(background=attr_str[2]), 
            Style(background=attr_str[3]) 
        ]
    dex_weapons = [
            Style(background=attr_dex[0]),
            Style(background=attr_dex[1]),
            Style(background=attr_dex[2]), 
            Style(background=attr_dex[3]) 
        ]
    int_weapons = [
            Style(background=attr_int[0]),
            Style(background=attr_int[1]),
            Style(background=attr_int[2]), 
            Style(background=attr_int[3]) 
        ]
    strdex_weapons = [
            Style(background=attr_strdex[0]),
            Style(background=attr_strdex[1]),
            Style(background=attr_strdex[2]), 
            Style(background=attr_strdex[3]) 
        ]
    strint_weapons = [
            Style(background=attr_strint[0]),
            Style(background=attr_strint[1]),
            Style(background=attr_strint[2]), 
            Style(background=attr_strint[3]) 
        ]
    dexint_weapons = [
            Style(background=attr_dexint[0]),
            Style(background=attr_dexint[1]),
            Style(background=attr_dexint[2]), 
            Style(background=attr_dexint[3]) 
        ]
    quivers = [
            Style(background=attr_dex[0]),
            Style(background=attr_dex[1]),
            Style(background=attr_dex[2]), 
            Style(background=attr_dex[3]) 
        ]
    fishing = [
            Style(text="#ff0000", background="#ffffff", size=45),
            Style(text="#ff0000", background="#ffffff", size=45),
            Style(text="#ff0000", background="#ffffff", size=45),
            Style(text="#ff0000", background="#ffffff", size=45)
        ]

# The first section of the filter is styling ONLY. There should be no
# hide() statements here. After all styling is applied, items can then
# be hidden by the second portion of the filter.
set_always_continue(True)

# Apply default filter to everything
# ==================================

with show():
    default.apply()


# Apply styles to items without rarity
# ====================================

with conditions(("Class", "Currency")):
    with conditions(("BaseType", "Scroll of Wisdom")), show():
        Theme.wisdom.apply()

    with conditions(("BaseType", "Portal Scroll")), show():
        Theme.portal.apply()

    with conditions(("BaseType",
                "Exalted Orb", "Mirror of Kalandra", "Albino Rhoa Feather")), show():
        Icons.extremely_valuable.apply()
        Theme.extremely_valuable.apply()
        Sounds.exalt.apply()

    with conditions(("BaseType",
                "Ancient Orb", "Divine Orb")), show():
        Icons.very_valuable.apply()
        Theme.very_valuable.apply()

    with conditions(("BaseType", "of Transmutation")), show():
        Theme.transmute.apply()

    with conditions(("BaseType",
                "of Alteration", "of Augmentation", "Regal Orb")), show():
        Theme.magic_orbs.apply()

    with show():
        condition("BaseType",
                "Chaos Orb", "Orb of Annulment")
        Icons.valuable.apply()
        Theme.valuable.apply()
        Sounds.chaos.apply()

    with show():
        condition("BaseType",
                "Scrap", "Whetstone", "Prism", "Bauble")
        Theme.quality.apply()

    with show():
        condition("BaseType", "Chisel", "Sextant")
        Theme.map_currency.apply()

    with show():
        condition("BaseType", "Prophecy")
        Theme.prophecies.apply()

    with show():
        condition("BaseType", "Shard")
        Theme.shards.apply()

    with show():
        condition("BaseType", "Essence")
        Theme.essences.apply()

    with show():
        condition("BaseType", "Fossil", "Resonator")
        Theme.delve.apply()

    with show():
        condition("BaseType", "Oil")
        Theme.oils.apply()

    with show():
        condition("BaseType", "Catalyst")
        Theme.catalysts.apply()

    with show():
        condition("BaseType", "Vial")
        Theme.vials.apply()

    with show():
        condition("BaseType", "Delirium")
        Theme.delirium.apply()
    
    with show():
        condition("BaseType", "Orb")
        Theme.other_orbs.apply()
    
    with show():
        Theme.other_currency.apply()
    

with conditions(("Class", "Fragment")):
    with show():
        condition("BaseType", "Esh", "Tul", "Chayula", "Xoph", "Netol")
        Theme.breachstones.apply()

    with show():
        condition("BaseType", "Timeless")
        Theme.emblems.apply()

    with show():
        condition("BaseType", "Scarab")
        Theme.scarabs.apply()

    # Other fragments
    with show():
        Theme.frags.apply()


with show():
    condition("Class", "Quest", "Labyrinth")
    Theme.quest.apply()

with show():
    condition("Class", "Incubator")
    Theme.incubators.apply()

with show():
    condition("Class", "Divination")
    Theme.divination.apply()

with conditions(("Class", "Gems")):
    with show():
        condition("Corrupted", "True")
        Theme.corrupted.apply()
        cont()

    with show():
        condition("BaseType", "Awakened")
        Theme.awakened_gems.apply()

    with show():
        condition("BaseType", "Enlighten", "Enhance", "Empower")
        Theme.drop_gems.apply()

    with show():
        condition("Quality > 0")
        Theme.gems.apply()

    with show():
        Theme.gems.apply()


with show():
    condition("Class", "Gems")
    Theme.gems.apply()

with show():
    condition("Class", "Metamorph")
    Theme.metamorph.apply()

with show():
    condition("Class", "Seed")
    Theme.seeds.apply()


# Apply styles to items with rarity
# =================================

# Apply default styles for rarity
with show():
    condition("Rarity Normal")
    Theme.rarity_normal.apply()
    cont()

with show():
    condition("Rarity Magic")
    Theme.rarity_magic.apply()
    cont()

with show():
    condition("Rarity Rare")
    Theme.rarity_rare.apply()
    cont()

with show():
    condition("Rarity Unique")
    Theme.rarity_unique.apply()
    cont()

# Conditions that bypass hides
# ============================

# Leveling socket types
# Note: these will still be hidden by later blocks if
# it isn't one of the listed weapon / armour types.
# Remove cont() to show anything that matches.
with show():
    condition("AreaLevel <= 68")
    condition("SocketGroup", *other_socket_groups)
    Theme.ok_sockets.apply()
    cont()

with show():
    condition("AreaLevel <= 68")
    condition("SocketGroup", *main_socket_groups)
    Theme.good_sockets.apply()
    cont()

# 5 & 6 links
with show():
    condition("LinkedSockets 5")
    Icons.valuable.apply()
    Theme.valuable.apply()

with show():
    condition("LinkedSockets 6")
    Icons.very_valuable.apply()
    Theme.very_valuable.apply()

# Influences
# TODO: Different colors for top tier bases
with show():
    condition("HasInfluence", "Shaper")
    Theme.shaper.apply()
    Icons.valuable.apply()

with show():
    condition("HasInfluence", "Elder")
    Theme.elder.apply()
    Icons.valuable.apply()

with show():
    condition("HasInfluence", "Warlord")
    Theme.warlord.apply()
    Icons.valuable.apply()

with show():
    condition("HasInfluence", "Hunter")
    Theme.hunter.apply()
    Icons.valuable.apply()

with show():
    condition("HasInfluence", "Redeemer")
    Theme.redeemer.apply()
    Icons.valuable.apply()

with show():
    condition("HasInfluence", "Crusader")
    Theme.crusader.apply()
    Icons.valuable.apply()


with show():
    condition("Corrupted", "True")
    condition("AnyEnchantment", "False")
    Theme.corrupted.apply()

with show():
    condition("Corrupted", "False")
    condition("AnyEnchantment", "True")
    Theme.enchanted.apply()

with show():
    condition("Corrupted", "True")
    condition("AnyEnchantment", "True")
    Theme.corrupted_enchanted.apply()

with show():
    condition("HasExplicitMod", "Veil")
    Theme.veiled.apply()

# Below these levels, show that rarity regardless of base type
arealevels = {
        "Normal": 1,
        "Magic": always_show_magic_until,
        "Rare": always_show_rare_until,
        "Unique": always_show_unique_until
    }

# Apply specific styles to each class / basetype
for idx, rarity in enumerate(["Normal", "Magic", "Rare", "Unique"]):
    with conditions(("Rarity", rarity)):
        
        with show():
            condition("Class", "Abyss")
            Theme.abyss[idx].apply()

        with conditions(("Class", "Jewel")):
            with show():
                condition("BaseType", "Cluster")
                Theme.cluster[idx].apply()

            with show():
                Theme.jewels[idx].apply()

        with show():
            condition("Class", "Atlas")
            Theme.watchstones[idx].apply()

        with show():
            condition("Class", "Maps")
            Theme.maps[idx].apply()

        with show():
            condition("Class", "Amulets")
            Theme.amulets[idx].apply()

        with conditions(("Class", "Rings")):
            if highlighted_rings:
                with show():
                    condition("BaseType", *highlighted_rings)
                    Theme.highlighted_rings[idx].apply()

            with show():
                Theme.rings[idx].apply()

        with conditions(("Class", "Belts")):
            if highlighted_belts:
                with show():
                    condition("BaseType", *highlighted_belts)
                    Theme.highlighted_belts[idx].apply()

            with show():
                Theme.belts[idx].apply()

        with show():
            condition("Class", "Life Flasks")
            Theme.life_flasks[idx].apply()

        with show():
            condition("Class", "Mana Flasks")
            Theme.mana_flasks[idx].apply()

        with show():
            condition("Class", "Utility Flasks")
            Theme.utility_flasks[idx].apply()

        with show():
            condition("Class", "Hybrid Flasks")
            Theme.hybrid_flasks[idx].apply()

        with show():
            condition("Class", "Fishing")
            Theme.fishing[idx].apply()

        with show():
            condition("Class", "Thrusting")
            Theme.dex_weapons[idx].apply()

        with show():
            condition("Class", "Bow")
            Theme.dex_weapons[idx].apply()

        with show():
            condition("Class", "Quivers")
            Theme.quivers[idx].apply()

        with show():
            condition("Class", "Wand")
            Theme.int_weapons[idx].apply()

        with show():
            condition("Class", "One Hand Axes")
            Theme.strdex_weapons[idx].apply()

        with show():
            condition("Class", "Two Hand Axes")
            Theme.strdex_weapons[idx].apply()

        with show():
            condition("Class", "One Hand Maces")
            Theme.str_weapons[idx].apply()

        with show():
            condition("Class", "Two Hand Maces")
            Theme.str_weapons[idx].apply()

        with show():
            condition("Class", "One Hand Swords")
            Theme.strdex_weapons[idx].apply()

        with show():
            condition("Class", "Two Hand Swords")
            Theme.strdex_weapons[idx].apply()

        with show():
            condition("Class", "Sceptre")
            Theme.strint_weapons[idx].apply()

        with show():
            condition("Class", "Warstaves")
            Theme.strint_weapons[idx].apply()

        with show():
            condition("Class", "Staves")
            Theme.strint_weapons[idx].apply()

        with show():
            condition("Class", "Claw")
            Theme.dexint_weapons[idx].apply()

        with show():
            condition("Class", "Rune Dagger")
            Theme.dexint_weapons[idx].apply()

        with show():
            condition("Class", "Dagger")
            Theme.dexint_weapons[idx].apply()

        with conditions(("Class",
                    "Gloves", "Boots", "Helmets", "Body", "Shields")):
            with conditions(("AreaLevel", "<=", arealevels[rarity])):
                with show():
                    condition("BaseType", *tables.str_armour)
                    Theme.str_armour[idx].apply()

                with show():
                    condition("BaseType", *tables.dex_armour)
                    Theme.dex_armour[idx].apply()

                with show():
                    condition("BaseType", *tables.int_armour)
                    Theme.int_armour[idx].apply()
                    
                with show():
                    condition("BaseType", *tables.strdex_armour)
                    Theme.strdex_armour[idx].apply()

                with show():
                    condition("BaseType", *tables.strint_armour)
                    Theme.strint_armour[idx].apply()

                with show():
                    condition("BaseType", *tables.dexint_armour)
                    Theme.dexint_armour[idx].apply()

# This section of the filter is where items are actually hidden.
# Up to this point, every block had an implicit Continue.

set_always_continue(False)


# Don't show bad corrupts with 0 mods
with hide():
    condition("Corrupted", "True")
    condition("FracturedItem", "False")
    condition("SynthesisedItem", "False")
    condition("Class",
            "Rings", "Belts", "Quivers", "Mace", "Sword",
            "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
            "Claw", "Gloves", "Helmets", "Body", "Shields")
    condition("CorruptedMods == 0")
    hidden.apply()

# Filter stuff out based on arealevel
with hide():
    condition("Rarity <= Rare") # Hide Rare except Jewelry after Act 10
    condition("AreaLevel > 68")
    condition("Class",
            "Flasks", "Quivers", "Mace",
            "Sword", "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
            "Claw", "Gloves", "Helmets", "Body", "Shields", "Boots")
    condition("Identified", "False")
    hidden.apply()

with hide(): # Hide Magic after Act 3, except flasks
    condition("Rarity < Rare")
    condition("AreaLevel >= 33")
    condition("Class",
            "Amulets", "Rings", "Belts", "Quivers", "Mace",
            "Sword", "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
            "Claw", "Gloves", "Helmets", "Body", "Shields", "Boots")
    condition("Identified", "False")
    hidden.apply()

with hide(): # Hide Normal after Act 2, except flasks
    condition("Rarity < Magic")
    condition("AreaLevel > 23")
    condition("Class",
            "Amulets", "Rings", "Belts", "Quivers", "Mace",
            "Sword", "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
            "Claw", "Gloves", "Helmets", "Body", "Shields", "Boots")
    condition("Identified", "False")
    hidden.apply()

