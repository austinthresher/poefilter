from poefilter import *
import munsell

class Colors:

    # Color constants (probably should be in CAPS)
    white = "255 255 255 255"
    black = "0 0 0 255"
    transparent = "0 0 0 0"

    # Text sizes

    class Font:
        LARGE = 45
        REGULAR = 40
        REDUCED = 35
        SMALL = 30
        TINY = 25
            

    default = Style(
            background="0 0 0",
            text="255 0 255",
            border="255 255 255 0",
            size=Font.REGULAR)


    # Class Currency
    extremely_valuable = Style(
            text="255 0 0 255",
            background="255 255 255 255",
            size=45)
    very_valuable = Style(
            text="179 36 30 255",
            background="255 248 229 255",
            size=45)
    valuable = Style(
            text="255 248 229 255",
            background="193 43 19 255")
    other_orbs = Style(
            text="255 216 206",
            background="20 20 20")
    quality = Style(
            text="197 195 147",
            background="52 74 72")
    map_currency = Style(
            text="204 212 191",
            background="62 93 121")

    prophecy_unknown = Style(
            text="255 0 0 255",
            background=black)

    prophecy_top = Style(
            text="51 27 67 255",
            border="181 71 254 255",
            background=white,
            size=Font.LARGE)
    prophecy_higher = Style(
            text=white,
            border="65 1 97 255",
            background="181 71 254 255",
            size=Font.LARGE)
    prophecy_high = Style(
            text=white,
            border="181 71 254 255",
            background="65 1 97 255")
    prophecy_mid = Style(
            text="181 71 254 255",
            border="181 71 254 255",
            background="65 1 97 255")
    prophecy_low = Style(
            text="181 71 254 255",
            border="181 71 254 255",
            background="30 13 41 220")
    prophecy_lower = Style(
            text="181 71 254 255",
            border=transparent,
            background="30 13 41 220",
            size=Font.REDUCED)
    prophecy_bottom = Style(
            text="181 71 254 255",
            border=transparent,
            background="30 13 41 192",
            size=Font.SMALL)

    shards = Style(
            text=munsell.get("10G", 8, 2),
            background=munsell.get("10R", 1, 2))
    essences = Style(
            text=munsell.get("5R", 9, 4),
            background=munsell.get("10R", 6, 14))
    remnant = Style(
            text=munsell.get("5B", 9, 4),
            background=munsell.get("10RP", 6, 14))
    other_currency = Style(
            text="225 211 191",
            background="20 20 20")
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

    # Individual currencies
    wisdom = Style(
            text=munsell.get("5R", 7, 2),
            background=munsell.get("5R", 2, 4))
    portal = Style(
            text=munsell.get("10B", 7, 2),
            background=munsell.get("10B", 2, 4))
    transmute = Style(
            text=munsell.get("7.5B", 8, 2),
            background=munsell.get("7.5B", 2, 4))
    augmentation = Style(
            text=munsell.get("2.5BG", 8, 2),
            background=munsell.get("2.5BG", 2, 4))
    alteration = Style(
            text=munsell.get("5PB", 8, 2),
            background=munsell.get("5PB", 3, 4))
    chance = Style(
            text=munsell.get("10BG", 8, 2),
            background=munsell.get("10BG", 2, 2))
    binding = Style(
            text=munsell.get("10GY", 8, 2),
            background=munsell.get("10GY", 2, 2))
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
            background=munsell.get("10Y", 2, 2))
    jewelers = Style(
            text=munsell.get("10B", 8, 2),
            background=munsell.get("10B", 4, 4))
    fuse = Style(
            text=munsell.get("2.5RP", 8, 2),
            background=munsell.get("2.5RP", 3, 6))
    chromatic = Style(
            text=munsell.get("5G", 8, 2),
            background=munsell.get("5G", 2, 4))
    scouring = Style(
            text=munsell.get("2.5GY", 8, 2),
            background=munsell.get("2.5GY", 4, 4))
    regret = Style(
            text=munsell.get("5YR", 8, 2),
            background=munsell.get("5YR", 4, 4))
    scrap = Style(
            text=munsell.get("7.5YR", 7, 2),
            background=munsell.get("7.5YR", 2, 2))
    whetstone = Style(
            text=munsell.get("7.5YR", 8, 2),
            background=munsell.get("7.5YR", 2, 4))
    bauble = Style(
            text=munsell.get("7.5YR", 9, 2),
            background=munsell.get("7.5YR", 3, 6))
    engineer = Style(
            text=munsell.get("7.5YR", 9, 2),
            background=munsell.get("7.5YR", 4, 8))
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
    perandus = Style(
            text=munsell.get("2.5Y", 4, 4),
            background=munsell.get("5Y", 8, 10))
    horizons = Style(
            text=munsell.get("7.5BG", 8, 2),
            background=munsell.get("2.5BG", 4, 2))
    harbingers = Style(
            text=munsell.get("2.5BG", 2, 4),
            background=munsell.get("5B", 7, 8))
    stacked_deck = Style(
            text=munsell.get("2.5PB", 2, 4),
            background=munsell.get("2.5PB", 7, 10))

    # Fragments
    sacrifice = Style(
            text=munsell.get("5R", 9, 4),
            background=munsell.get("5R", 3, 4))
    mortal = Style(
            text=munsell.get("5G", 9, 4),
            background=munsell.get("5G", 3, 4))
    shaper_frags = Style(
            text=munsell.get("5B", 3, 4),
            background=munsell.get("5B", 9, 4))
    elder_frags = Style(
            text=munsell.get("7.5GY", 3, 4),
            background=munsell.get("7.5GY", 9, 4))
    uber = Style(
            text=munsell.get("10G", 1, 2),
            background=munsell.get("10G", 9, 2))
    pale = Style(
            text=munsell.get("2.5P", 3, 4),
            background=munsell.get("2.5P", 9, 4))
    frags = Style(
            text=munsell.get("10RP", 9, 4),
            background=munsell.get("5P", 3, 4))
    breachstones = Style(
            text=munsell.get("10R", 9, 4),
            background=munsell.get("10R", 1, 2))
    emblems = Style(
            text=munsell.get("10R", 9, 4),
            background=munsell.get("10R", 2, 2))
    breach_splinter = Style(
            text=munsell.get("10GY", 2, 6),
            background=munsell.get("10P", 7, 4))
    timeless_splinter = Style(
            text=munsell.get("10RP", 1, 6),
            background=munsell.get("10G", 7, 4))
    rusted_scarabs = Style(
            text=munsell.get("2.5YR", 7, 4),
            background=munsell.get("2.5Y", 2, 2))
    polished_scarabs = Style(
            text=munsell.get("5YR", 8, 4),
            background=munsell.get("2.5Y", 2, 4))
    gilded_scarabs = Style(
            text=munsell.get("10YR", 9, 4),
            background=munsell.get("5Y", 4, 6))
    winged_scarabs = Style(
            text=munsell.get("5Y", 4, 6),
            background=munsell.get("10YR", 9, 4))
    simulacrum_splinter = Style(
            text=munsell.get("10YR", 3, 6),
            background=munsell.get("10B", 9, 2))
    delirium_orb = Style(
            text=munsell.get("10YR", 4, 6),
            background=munsell.get("10B", 9, 2))

    # Other classes
    quest = Style(
            text="59 192 41",
            background="20 20 20")
    incubators = Style(
            text="201 192 179",
            background="78 38 13")

    # For cards that aren't listed in the tier table
    divination_unknown = Style(
            text="255 0 0 255",
            border="14 186 255 255",
            background="1 44 139 220")

    divination_top = Style(
            text="1 4 35 255",
            border="14 186 255 255",
            background=white,
            size=Font.LARGE)
    divination_higher = Style(
            text=white,
            border="1 44 139 255",
            background="14 186 255 255",
            size=Font.LARGE)
    divination_high = Style(
            text=white,
            border="14 186 255 255",
            background="1 44 139 255")
    divination_mid = Style(
            text="14 186 255 255",
            border="14 186 255 255",
            background="1 44 139 255")
    divination_low = Style(
            text="14 186 255 255",
            border="14 186 255 255",
            background="1 4 35 220")
    divination_lower = Style(
            text="14 186 255 255",
            border=transparent,
            background="1 4 35 220",
            size=Font.REDUCED)
    divination_bottom = Style(
            text="14 186 255 255",
            border=transparent,
            background="1 4 35 192",
            size=Font.SMALL)

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
    quality_gems = Style(
            text=munsell.get("5BG", 8, 8),
            background=munsell.get("2.5BG", 4, 4))
    gems = Style(
            text=munsell.get("2.5BG", 5, 6),
            background=munsell.get("2.5BG", 1, 2))
    metamorph = Style(
            text=munsell.get("7.5Y", 9, 8),
            background=munsell.get("7.5GY", 4, 6))
    seeds = Style(
            text="227 214 195",
            background="103 89 71")
    # TODO: pieces, lures

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
            border="239 132 18 255",
            background="20 20 20 255",
            size=45,
            play_effect_color="Brown",
            minimap_icon_size=1,
            minimap_icon_color="Brown",
            minimap_icon_shape="Diamond")

    # Colors for attribute gear

    attr_str = [
            "40 0 0 192",
            "40 0 0 220",
            "40 0 0 255",
            "40 0 0 255"]
    attr_dex = [
            "0 40 0 192",
            "0 40 0 220",
            "0 40 0 255",
            "0 40 0 255"]
    attr_int = [
            "0 0 40 192",
            "0 0 40 220",
            "0 0 40 255",
            "0 0 40 255"]
    attr_strdex = [
            "25 25 0 192",
            "25 25 0 220",
            "25 25 0 255",
            "25 25 0 255"]
    attr_strint = [
            "25 0 25 192",
            "25 0 25 220",
            "25 0 25 255",
            "25 0 25 255"]
    attr_dexint = [
            "0 25 25 192",
            "0 25 25 220",
            "0 25 25 255", 
            "0 25 25 255"]

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
    good_sockets = Style(border="0 255 0 255")
    ok_sockets = Style(border="30 128 30 255")
    chrome_recipe = Style(border="200 200 200 255")
    jewellers_recipe = Style(border="200 200 255 255")

    ring_color = munsell.get("7.5PB", 1, 2) + " 255"
    belt_color = munsell.get("7.5BG", 1, 2) + " 255"
    amulet_color = munsell.get("7.5RP", 1, 2) + " 255"

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
    # TODO: Map tiers
    maps = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    highlighted_amulets = [
            Style(text=white, background=amulet_color, border=white),
            Style(text=white, background=amulet_color, border=white),
            Style(text=white, background=amulet_color, border=white),
            Style(text=white, background=amulet_color, border=white),
        ]
    amulets = [
            Style(background=amulet_color),
            Style(background=amulet_color),
            Style(background=amulet_color),
            Style(background=amulet_color),
        ]
    highlighted_rings = [
            Style(text=white, background=ring_color, border=white),
            Style(text=white, background=ring_color, border=white),
            Style(text=white, background=ring_color, border=white),
            Style(text=white, background=ring_color, border=white),
        ]
    rings = [
            Style(background=ring_color),
            Style(background=ring_color),
            Style(background=ring_color),
            Style(background=ring_color),
        ]
    highlighted_belts = [
            Style(text=white, background=belt_color, border=white),
            Style(text=white, background=belt_color, border=white),
            Style(text=white, background=belt_color, border=white),
            Style(text=white, background=belt_color, border=white),
        ]
    belts = [
            Style(background=belt_color),
            Style(background=belt_color),
            Style(background=belt_color),
            Style(background=belt_color),
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
