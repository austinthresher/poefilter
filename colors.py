from poefilter import *
import munsell

# Color constants (probably should be in CAPS)
white = "255 255 255 255"
black = "0 0 0 255"
transparent = "0 0 0 0"
error = "255 0 0 255"


# Text sizes
class Font:
    LARGE = 45
    REGULAR = 43
    REDUCED = 41
    SMALL = 38
    TINY = 32

# Many items are grouped into 7 tiers of rarity. These
# functions define a consistent theme across item types.
# pal is a 3-tuple of space separated RGB colors (no alpha)
def series_top(pal):
    return Style(
            text=pal[0] + " 255",
            border=pal[2] + " 255",
            background=white,
            size=Font.LARGE)

def series_higher(pal):
    return Style(
            text=white,
            border=pal[1] + " 255",
            background=pal[2] + " 255",
            size=Font.LARGE)

def series_high(pal):
    return Style(
            text=white,
            border=pal[2] + " 255",
            background=pal[1] + " 255")

def series_mid(pal):
    return Style(
            text=pal[0] + " 255",
            border=pal[2] + " 255",
            background=pal[1] + " 255")

def series_low(pal):
    return Style(
            text=pal[2] + " 255",
            border=pal[2] + " 255",
            background=pal[0] + " 220")

def series_lower(pal):
    return Style(
            text=pal[2] + " 255",
            border=pal[2] + " 128",
            background=pal[0] + " 220",
            size=Font.REDUCED)

def series_bottom(pal):
    return Style(
            text=pal[2] + " 255",
            border=pal[2] + " 128",
            background=pal[0] + " 192",
            size=Font.REDUCED)


class Colors:

    default = Style(
            background="0 0 0",
            text="255 0 255",
            border="255 255 255 0",
            size=Font.REGULAR)

    # Class Currency
    extremely_valuable = Style(
            text="255 0 0 255",
            background="255 255 255 255",
            size=Font.LARGE)
    very_valuable = Style(
            text="179 36 30 255",
            background="255 248 229 255",
            size=Font.LARGE)
    valuable = Style(
            text="255 248 229 255",
            background="193 43 19 255")
    other_orbs = Style(
            text="255 216 206",
            background="20 20 20")

    # Prophecy tiers
    prophecy_pal = ("30 13 41", "65 1 97", "181 71 254")
    prophecy_unknown = Style(text=error, border=error, background=black)

    prophecy_top = series_top(prophecy_pal)
    prophecy_higher = series_higher(prophecy_pal)
    prophecy_high = series_high(prophecy_pal)
    prophecy_mid = series_mid(prophecy_pal)
    prophecy_low = series_low(prophecy_pal)
    prophecy_lower = series_lower(prophecy_pal)
    prophecy_bottom = series_bottom(prophecy_pal)

    shards = Style(
            text=munsell.get("10G", 8, 2),
            background=munsell.get("10R", 1, 2))
    remnant = Style(
            text=munsell.get("5B", 9, 4),
            background=munsell.get("10RP", 6, 14))
    other_currency = Style(
            text="225 211 191",
            background="20 20 20")

    # Individual currencies
    wisdom = Style(
            text=munsell.get("5R", 7, 2),
            background=munsell.get("5R", 2, 4),
            size=Font.SMALL)
    portal = Style(
            text=munsell.get("10B", 7, 2),
            background=munsell.get("10B", 2, 4),
            size=Font.SMALL)
    transmute = Style(
            text=munsell.get("7.5B", 8, 2),
            background=munsell.get("7.5B", 2, 4),
            size=Font.SMALL)
    augmentation = Style(
            text=munsell.get("2.5BG", 8, 2),
            background=munsell.get("2.5BG", 2, 4),
            size=Font.SMALL)
    alteration = Style(
            text=munsell.get("5PB", 8, 2),
            background=munsell.get("5PB", 3, 4),
            size=Font.REDUCED)
    chance = Style(
            text=munsell.get("10BG", 8, 2),
            background=munsell.get("10BG", 2, 2),
            size=Font.REDUCED)
    binding = Style(
            text=munsell.get("10GY", 8, 2),
            background=munsell.get("10GY", 2, 2),
            size=Font.REDUCED)
    chaos = Style(
            text=munsell.get("5R", 9, 2),
            background=munsell.get("5R", 2, 8))
    regal = Style(
            text=munsell.get("5P", 8, 2),
            background=munsell.get("5P", 2, 4))
    vaal = Style(
            text=munsell.get("7.5R", 9, 2),
            background=munsell.get("7.5R", 3, 10))
    alchemy = Style(
            text=munsell.get("2.5Y", 9, 2),
            background=munsell.get("2.5Y", 5, 8))
    blessed = Style(
            text=munsell.get("10Y", 8, 2),
            background=munsell.get("10Y", 2, 2),
            size=Font.REDUCED)
    jewelers = Style(
            text=munsell.get("10B", 8, 2),
            background=munsell.get("10B", 4, 4),
            size=Font.REDUCED)
    fuse = Style(
            text=munsell.get("2.5RP", 8, 2),
            background=munsell.get("2.5RP", 3, 6))
    chromatic = Style(
            text=munsell.get("5G", 8, 2),
            background=munsell.get("5G", 2, 4),
            size=Font.REDUCED)
    scouring = Style(
            text=munsell.get("2.5GY", 8, 2),
            background=munsell.get("2.5GY", 4, 4),
            size=Font.REDUCED)
    regret = Style(
            text=munsell.get("5YR", 8, 2),
            background=munsell.get("5YR", 4, 4))
    scrap = Style(
            text=munsell.get("7.5YR", 7, 2),
            background=munsell.get("7.5YR", 2, 2),
            size=Font.SMALL)
    whetstone = Style(
            text=munsell.get("7.5YR", 8, 2),
            background=munsell.get("7.5YR", 2, 4),
            size=Font.SMALL)
    bauble = Style(
            text=munsell.get("7.5YR", 9, 2),
            background=munsell.get("7.5YR", 3, 6),
            size=Font.REDUCED)
    engineer = Style(
            text=munsell.get("7.5YR", 9, 2),
            background=munsell.get("7.5YR", 4, 8),
            size=Font.REDUCED)
    prism = Style(
            text=munsell.get("10YR", 9, 2),
            background=munsell.get("10YR", 5, 8))
    chisel = Style(
            text=munsell.get("10YR", 9, 4),
            background=munsell.get("10YR", 6, 10))
    white_sextant = Style(
            text=munsell.get("10YR", 1, 2),
            background=munsell.get("10YR", 8, 2))
    yellow_sextant = Style(
            text=munsell.get("5YR", 1, 2),
            background=munsell.get("5YR", 8, 6))
    red_sextant = Style(
            text=munsell.get("10R", 1, 2),
            background=munsell.get("10R", 8, 8))
    silver_coin = Style(
            text=munsell.get("2.5P", 2, 4),
            background=munsell.get("5P", 8, 10))
    horizons = Style(
            text=munsell.get("7.5BG", 8, 2),
            background=munsell.get("2.5BG", 4, 2),
            size=Font.REDUCED)
    harbingers = Style(
            text=munsell.get("2.5BG", 2, 4),
            background=munsell.get("5B", 7, 8))
    stacked_deck = Style(
            text=munsell.get("2.5PB", 2, 4),
            background=munsell.get("2.5PB", 7, 10))

    # Fragments
    sacrifice = Style(
            text=munsell.get("5R", 9, 4),
            background=munsell.get("5R", 3, 4),
            size=Font.REDUCED)
    mortal = Style(
            text=munsell.get("5G", 9, 4),
            background=munsell.get("5G", 3, 4))
    shaper_frags = Style(
            text=munsell.get("5B", 3, 4),
            background=munsell.get("5B", 9, 4),
            size=Font.LARGE)
    elder_frags = Style(
            text=munsell.get("7.5GY", 3, 4),
            background=munsell.get("7.5GY", 9, 4),
            size=Font.LARGE)
    uber = Style(
            text=munsell.get("10G", 1, 2),
            background=munsell.get("10G", 9, 2),
            size=Font.LARGE)
    pale = Style(
            text=munsell.get("2.5P", 3, 4),
            background=munsell.get("2.5P", 9, 4),
            size=Font.LARGE)
    frags = Style(
            text=munsell.get("10RP", 9, 4),
            background=munsell.get("5P", 3, 4))
    rusted_scarabs = Style(
            text=munsell.get("2.5YR", 7, 4),
            background=munsell.get("2.5Y", 2, 2),
            size=Font.REDUCED)
    polished_scarabs = Style(
            text=munsell.get("5YR", 8, 4),
            background=munsell.get("2.5Y", 2, 4))
    gilded_scarabs = Style(
            text=munsell.get("10YR", 9, 4),
            background=munsell.get("5Y", 4, 6),
            size=Font.LARGE)
    winged_scarabs = Style(
            text=munsell.get("5Y", 4, 6),
            background=munsell.get("10YR", 9, 4),
            size=Font.LARGE)

    # Other classes
    quest = Style(
            text="59 192 41",
            border="59 192 41 255",
            background="20 20 20")

    # Divination tiers
    divination_pal = ("1 4 35", "1 44 139", "14 186 255")
    divination_unknown = Style(text=error, border=error, background=black)

    divination_top = series_top(divination_pal)
    divination_higher = series_higher(divination_pal)
    divination_high = series_high(divination_pal)
    divination_mid = series_mid(divination_pal)
    divination_low = series_low(divination_pal)
    divination_lower = series_lower(divination_pal)
    divination_bottom = series_bottom(divination_pal)

    awakened_gems = Style(
            text="0 0 0 255",
            border="255 0 0 255",
            background="240 92 36 255",
            minimap_icon_size=1,
            minimap_icon_color="Cyan",
            minimap_icon_shape="Hexagon",
            play_effect_color="Cyan")
    alt_gems = Style(
            text="0 0 0 255",
            border="0 255 0 255",
            background="106 212 177 255",
            minimap_icon_size=2,
            minimap_icon_color="Cyan",
            minimap_icon_shape="Hexagon",
            play_effect_color="Cyan")
    drop_gems = Style(
            text="0 0 0 255",
            border="0 0 0 255",
            background="106 212 177 255",
            minimap_icon_size=2,
            minimap_icon_color="Cyan",
            minimap_icon_shape="Hexagon",
            play_effect_color="Cyan")
    divergent_gems = Style(
            text=munsell.get("5Y", 8, 8),
            border=munsell.get("5Y", 8, 8) + " 200",
            background=munsell.get("2.5BG", 4, 4))
    anomalous_gems = Style(
            text=munsell.get("5R", 8, 8),
            border=munsell.get("5R", 8, 8) + " 200",
            background=munsell.get("2.5BG", 4, 4))
    phantasmal_gems = Style(
            text=munsell.get("5P", 8, 8),
            border=munsell.get("5P", 8, 8) + " 200",
            background=munsell.get("2.5BG", 4, 4))
    superior_gems = Style(
            text=munsell.get("5BG", 8, 8),
            border=munsell.get("5BG", 8, 8) + " 200",
            background=munsell.get("2.5BG", 4, 4))
    gems = Style(
            text=munsell.get("2.5BG", 5, 6),
            background=munsell.get("2.5BG", 1, 2))

    # League stuff
    perandus = Style(
            text=munsell.get("2.5Y", 4, 4),
            background=munsell.get("5Y", 8, 10),
            size=Font.SMALL)
    vials = Style(
            text="239 166 172",
            background="225 109 118")
    resonator = Style(
            text=munsell.get("7.5YR", 7, 10),
            background=munsell.get("7.5YR", 1, 2))
    fossil = Style(
            text=munsell.get("7.5YR", 1, 2),
            background=munsell.get("7.5YR", 7, 10))
    catalysts = Style(
            text="255 250 165",
            background="154 170 252")
    oils = Style(
            text=munsell.get("5YR", 2, 2),
            background=munsell.get("5YR", 7, 10))
    metamorph = Style(
            text=munsell.get("7.5Y", 9, 8),
            background=munsell.get("7.5GY", 4, 6))
    seeds = Style(
            text="227 214 195",
            background="103 89 71")
    simulacrum_splinter = Style(
            text=munsell.get("10YR", 3, 6),
            background=munsell.get("10B", 9, 2))
    delirium_orb = Style(
            text=munsell.get("10YR", 4, 6),
            background=munsell.get("10B", 9, 2))
    breachstones = Style(
            text=munsell.get("10R", 9, 4),
            background=munsell.get("10R", 1, 2),
            size=Font.LARGE)
    emblems = Style(
            text=munsell.get("10R", 9, 4),
            background=munsell.get("10R", 2, 2),
            size=Font.LARGE)
    breach_splinter = Style(
            text=munsell.get("10GY", 2, 6),
            background=munsell.get("10P", 7, 4))
    timeless_splinter = Style(
            text=munsell.get("10RP", 1, 6),
            background=munsell.get("10G", 7, 4))
    incubators = Style(
            text="201 192 179",
            background="78 38 13")
    # Heist stuff, WIP:
    rogue_marker = Style(
            text="200 251 232 255",
            border="126 168 154 255",
            background="68 62 50 255",
            size=Font.REDUCED)
    tailoring_orb = Style(
            text="164 252 107",
            border="164 252 107 255",
            background="90 73 89 220")
    tempering_orb = Style(
            text="246 206 207",
            border="246 206 207 255",
            background="90 73 89 220")
    prime_regrading_lens = Style(
            text="47 60 33",
            border=white,
            background="204 228 175 240")
    secondary_regrading_lens = Style(
            text="47 60 33",
            background="204 228 175 220")
    trinket = Style(
            text="254 224 234",
            background="120 25 54 240")
    contract = Style(
            text="255 246 182",
            border="255 246 182 220",
            background="74 54 43 240")
    quest_contract = Style(
            text="74 54 43",
            border="74 54 43 200",
            background="255 246 182 220")
    blueprint = Style(
            text="27 34 62 255",
            border="204 232 207 255",
            background="149 176 232 240",
            size=Font.LARGE)
    heist_target = Style(
            text="250 223 152",
            border=white,
            background="104 14 57 255",
            size=Font.LARGE)
    heist_cloak = Style(
            text="248 193 132",
            border="152 101 45 255",
            background="20 60 30 240")
    heist_brooch = Style(
            text="226 152 129",
            border="124 62 42 255",
            background="20 60 30 240")
    heist_gear = Style(
            text="236 220 147",
            border="156 138 59 255",
            background="20 60 30 240")
    heist_tool = Style(
            text="244 233 189",
            border="139 129 90 255",
            background="20 60 30 240")

    # TODO: pieces, lures

    # Default colors for rarity
    rarity_normal = Style(
            text="200 200 200 220",
            background="20 20 20 200",
            size=35)

    rarity_magic = Style(
            text="56 171 255 255",
            background="20 20 20 220",
            size=38)

    rarity_rare = Style(
            text="255 255 119 255",
            background="20 20 20 255",
            size=42)

    rarity_unique = Style(
            text="239 132 18 255",
            border="239 132 18 255",
            background="20 20 20 255",
            size=45,
            play_effect_color="Brown",
            minimap_icon_size=1,
            minimap_icon_color="Brown",
            minimap_icon_shape="Diamond")

    # Unique tiers
    unique_pal = ("73 33 0", "175 96 37", "254 170 56")
    unique_unknown = Style(text=error, border=error, background=black)

    unique_top = series_top(unique_pal)
    unique_higher = series_higher(unique_pal)
    unique_high = series_high(unique_pal)
    unique_mid = series_mid(unique_pal)
    unique_low = series_low(unique_pal)
    unique_lower = series_lower(unique_pal)
    unique_bottom = series_bottom(unique_pal)

    # Essence tiers
    essence_pal = ("65 23 26", "157 55 50", "208 109 89")
    essence_unknown = Style(text=error, border=error, background=black)

    essence_top = series_top(essence_pal)
    essence_higher = series_higher(essence_pal)
    essence_high = series_high(essence_pal)
    essence_mid = series_mid(essence_pal)
    essence_low = series_low(essence_pal)
    essence_lower = series_lower(essence_pal)
    essence_bottom = series_bottom(essence_pal)

    # Colors for attribute gear

    attr_str = [
            "60 0 0 192",
            "60 0 0 220",
            "60 0 0 255",
            "60 0 0 255"]
    attr_dex = [
            "0 60 0 192",
            "0 60 0 220",
            "0 60 0 255",
            "0 60 0 255"]
    attr_int = [
            "0 0 60 192",
            "0 0 60 220",
            "0 0 60 255",
            "0 0 60 255"]
    attr_strdex = [
            "33 33 0 192",
            "33 33 0 220",
            "33 33 0 255",
            "33 33 0 255"]
    attr_strint = [
            "33 0 33 192",
            "33 0 33 220",
            "33 0 33 255",
            "33 0 33 255"]
    attr_dexint = [
            "0 33 33 192",
            "0 33 33 220",
            "0 33 33 255", 
            "0 33 33 255"]

    # Influences
    shaper = Style(
            text=black,
            background="#3c78d8ff",
            border=white,
            size=45)
    elder = Style(
            text=black,
            background="#8e7cc3ff",
            border=white,
            size=45)
    warlord = Style(
            text=black,
            background="#ffd966ff",
            border=white,
            size=45)
    hunter = Style(
            text=black,
            background="#6aa84fff",
            border=white,
            size=45)
    redeemer = Style(
            text=black,
            background="#9fc5e8ff",
            border=white,
            size=45)
    crusader = Style(
            text=black,
            background="#cc4125ff",
            border=white,
            size=45)

    # Border highlights
    corrupted = Style(border="210 0 0 255")
    veiled = Style(border="70 207 119 255")
    enchanted = Style(border="242 205 233 255")
    corrupted_enchanted = Style(border="255 0 255 255")
    three_link_highlighted = Style(border="0 200 0 200")
    highlighted = Style(border=white, size=Font.LARGE)
    four_link = Style(border="0 0 255 255")
    five_link = Style(border="0 255 255 255")
    chrome_recipe = Style(border="100 100 100 255", background="50 50 50 200")
    jewellers_recipe = Style(border="200 200 200 200", background="100 100 100 255")
    replica_unique = Style(border="255 255 0 255")

    ring_color = munsell.get("7.5PB", 1, 2) + " 255"
    belt_color = munsell.get("7.5BG", 1, 2) + " 255"
    amulet_color = munsell.get("7.5RP", 1, 2) + " 255"

    experimented_base = Style(
            text="174 219 138",
            border="255 137 45 255",
            background="19 57 46 255")

    map_white_bg = "57 62 58 250"
    map_yellow_bg = "97 92 11 250"
    map_red_bg = "96 30 6 250"

    maps_white = Style(background=map_white_bg, size=Font.REDUCED)
    maps_yellow = Style(background=map_yellow_bg, size=Font.REGULAR)
    maps_red = Style(background=map_red_bg, size=Font.LARGE)

    highlighted_amulets = Style(background=amulet_color, border=white)
    amulets = Style(background=amulet_color)
    highlighted_rings = Style(background=ring_color, border=white)
    rings = Style(background=ring_color)
    highlighted_belts = Style(background=belt_color, border=white)
    belts = Style(background=belt_color)

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
    life_flasks = [
            Style(background="125 13 53 128"),
            Style(background="125 13 53 220"),
            rarity_rare, 
            Style(background="125 13 53 255"),
        ]
    mana_flasks = [
            Style(background="32 48 126 128"),
            Style(background="32 48 126 220"),
            rarity_rare, 
            Style(background="32 48 126 255"),
        ]
    hybrid_flasks = [
            Style(background="74 27 76 128"),
            Style(background="73 27 76 220"),
            rarity_rare, 
            Style(background="73 27 76 255"),
        ]
    utility_flasks = [
            Style(background="0 77 67 255"),
            Style(background="0 77 67 255"),
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
