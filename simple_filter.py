from poefilter import *
import tables
import colors
import styles
import hide

# Filter configuration
# ====================
class Config:
    main_socket_groups = ["BBG", "RRG", "GGG"]
    other_socket_groups = ["BG", "RG", "GG"]
    # str, dex, int, strdex, strint, dexint
    armour_types = ["int"]
    # thrusting, bows, wands, axes1, axes2, maces1, maces2, swords1, swords2,
    # sceptres, warstaves, staves, claws, rune daggers, daggers
    weapon_types = ["wands", "rune daggers"]

    highlighted_rings = ["Sapphire"]
    highlighted_belts = ["Leather", "Rustic"]
    highlighted_amulets = ["Jade"]


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
 

class Theme:
    default = Style(
            background="0 0 0",
            text="255 0 255",
            border="255 255 255 0",
            size=45)
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
styles.apply(config=Config, theme=Theme, icons=Icons, sounds=Sounds)

# This section of the filter is where items are actually hidden.
# Up to this point, every block had an implicit Continue.
set_always_continue(False)
hide.apply(config=Config)
