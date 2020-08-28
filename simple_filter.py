from poefilter import *

main_socket_groups = ["BBG", "RRG", "GGG"]
other_socket_groups = ["BG", "RG", "GG"]
# str, dex, int, strdex, strint, dexint
armour_types = ["int"]
# thrusting, bows, wands, axes, maces, swords, sceptres, warstaves, staves,
# claws, rune daggers, daggers
weapon_types = ["wands", "rune daggers"]

default = Style(
        background_color="0 0 0",
        text_color="255 0 255",
        border_color="255 255 255 0",
        font_size=45)

hidden = Style(font_size=28)

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
            text_color="255 0 0 255",
            background_color="255 255 255 255",
            font_size=45)
    very_valuable = Style(
            text_color="179 36 30 255",
            background_color="255 248 229",
            font_size=45)
    valuable = Style(
            text_color="255 248 229 255",
            background_color="193 43 19 255")
    magic_orbs = Style(
            text_color="171 232 240",
            background_color="17 109 130")
    other_orbs = Style(
            text_color="255 216 206",
            background_color="20 20 20")
    quality = Style(
            text_color="197 195 147",
            background_color="52 74 72")
    map_currency = Style(
            text_color="204 212 191",
            background_color="62 93 121")
    prophecies = Style(
            text_color="220 156 208",
            background_color="126 34 103")
    shards = Style(
            text_color="120 148 170",
            background_color="90 98 83")
    essences = Style(
            text_color="246 190 196",
            background_color="17 112 114")
    other_currency = Style(
            text_color="225 211 191",
            background_color="20 20 20")
    vials = Style(
            text_color="239 166 172",
            background_color="225 109 118")
    delve = Style(
            text_color="249 202 61",
            background_color="0 71 64")
    catalysts = Style(
            text_color="255 250 165",
            background_color="154 170 252")
    oils = Style(
            text_color="229 253 231",
            background_color="232 113 145")
    delirium = Style(
            text_color="232 235 233",
            background_color="45 81 94")
    wisdom = Style(
            text_color="#b7b7a4",
            border_color="#b7b7a4ff",
            background_color="59 12 4")
    portal = Style(
            text_color="#b7b7a4",
            border_color="#b7b7a4ff",
            background_color="8 63 127")
    transmute = Style(
            text_color="171 232 240",
            background_color="17 109 130")

    # Class Fragments
    frags = Style(
            text_color="158 209 239",
            background_color="145 33 47")
    breachstones = Style(
            text_color="208 247 255",
            background_color="92 109 91")
    emblems = Style(
            text_color="24 48 58",
            background_color="216 229 220")
    scarabs = Style(
            text_color="252 254 217",
            background_color="105 116 162")

    # Other classes
    quest = Style(
            text_color="59 192 41",
            background_color="20 20 20")
    incubators = Style(
            text_color="201 192 179",
            background_color="78 38 13")
    divination = Style(
            text_color="100 206 254 255",
            background_color="9 23 70 220")
    awakened_gems = Style(
            text_color="0 0 0 255",
            background_color="240 92 36 255",
            minimap_icon_size=1,
            minimap_icon_color="Cyan",
            minimap_icon_shape="Hexagon",
            play_effect_color="Cyan")
    drop_gems = Style(
            text_color="0 0 0 255",
            background_color="106 212 177 255",
            minimap_icon_size=2,
            minimap_icon_color="Cyan",
            minimap_icon_shape="Hexagon",
            play_effect_color="Cyan")
    gems = Style(
            text_color="98 201 202",
            background_color="60 98 99")
    metamorph = Style(
            text_color="225 255 94",
            background_color="59 89 65")
    seeds = Style(
            text_color="227 214 195",
            background_color="103 89 71")
    # TODO: piece

    # Default colors for rarity
    rarity_normal = Style(
            text_color="200 200 200 220",
            #border_color="200 200 200 128",
            background_color="20 20 20 200",
            font_size=35)

    rarity_magic = Style(
            text_color="56 171 255 255",
            #border_color="56 171 255 192",
            background_color="20 20 20 220",
            font_size=38)

    rarity_rare = Style(
            text_color="255 255 119 255",
            #border_color="255 255 119 220",
            background_color="20 20 20 255",
            font_size=42)

    rarity_unique = Style(
            text_color="239 132 18 255",
            #border_color="239 132 18 255",
            background_color="20 20 20 255",
            font_size=45,
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
            text_color="0 0 0 255",
            background_color="#3c78d8ff",
            border_color="#ffffffff",
            font_size=45)
    elder = Style(
            text_color="0 0 0 255",
            background_color="#8e7cc3ff",
            border_color="#ffffffff",
            font_size=45)
    warlord = Style(
            text_color="0 0 0 255",
            background_color="#ffd966ff",
            border_color="#ffffffff",
            font_size=45)
    hunter = Style(
            text_color="0 0 0 255",
            background_color="#6aa84fff",
            border_color="#ffffffff",
            font_size=45)
    redeemer = Style(
            text_color="0 0 0 255",
            background_color="#9fc5e8ff",
            border_color="#ffffffff",
            font_size=45)
    crusader = Style(
            text_color="0 0 0 255",
            background_color="#cc4125ff",
            border_color="#ffffffff",
            font_size=45)

    # Notable highlights

    corrupted = Style(border_color="210 0 0 255")
    veiled = Style(border_color="70 207 119 255")
    enchanted = Style(border_color="242 205 233 255")
    corrupted_enchanted = Style(border_color="255 0 255 255")

    good_sockets = Style(border_color="0 255 0 255")
    ok_sockets = Style(border_color="0 0 0 255")

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
    amulets = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    rings = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    belts = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    life_flasks = [
            Style(background_color="125 13 53 220"),
            Style(background_color="125 13 53 220"),
            rarity_rare, 
            Style(background_color="125 13 53 255"),
        ]
    mana_flasks = [
            Style(background_color="32 48 126 220"),
            Style(background_color="32 48 126 220"),
            rarity_rare, 
            Style(background_color="32 48 126 255"),
        ]
    hybrid_flasks = [
            Style(background_color="73 27 76 220"),
            Style(background_color="73 27 76 220"),
            rarity_rare, 
            Style(background_color="73 27 76 255"),
        ]
    utility_flasks = [
            Style(background_color="0 77 67 220"),
            Style(background_color="0 77 67 220"),
            rarity_rare, 
            Style(background_color="0 77 67 255"),
        ]
    str_armour = [
            Style(background_color=attr_str[0]),
            Style(background_color=attr_str[1]),
            Style(background_color=attr_str[2]), 
            Style(background_color=attr_str[3]) 
        ]
    dex_armour = [
            Style(background_color=attr_dex[0]),
            Style(background_color=attr_dex[1]),
            Style(background_color=attr_dex[2]), 
            Style(background_color=attr_dex[3]) 
        ]
    int_armour = [
            Style(background_color=attr_int[0]),
            Style(background_color=attr_int[1]),
            Style(background_color=attr_int[2]), 
            Style(background_color=attr_int[3]) 
        ]
    strdex_armour = [
            Style(background_color=attr_strdex[0]),
            Style(background_color=attr_strdex[1]),
            Style(background_color=attr_strdex[2]), 
            Style(background_color=attr_strdex[3]) 
        ]
    strint_armour = [
            Style(background_color=attr_strint[0]),
            Style(background_color=attr_strint[1]),
            Style(background_color=attr_strint[2]), 
            Style(background_color=attr_strint[3]) 
        ]
    dexint_armour = [
            Style(background_color=attr_dexint[0]),
            Style(background_color=attr_dexint[1]),
            Style(background_color=attr_dexint[2]), 
            Style(background_color=attr_dexint[3]) 
        ]
    str_weapons = [
            Style(background_color=attr_str[0]),
            Style(background_color=attr_str[1]),
            Style(background_color=attr_str[2]), 
            Style(background_color=attr_str[3]) 
        ]
    dex_weapons = [
            Style(background_color=attr_dex[0]),
            Style(background_color=attr_dex[1]),
            Style(background_color=attr_dex[2]), 
            Style(background_color=attr_dex[3]) 
        ]
    int_weapons = [
            Style(background_color=attr_int[0]),
            Style(background_color=attr_int[1]),
            Style(background_color=attr_int[2]), 
            Style(background_color=attr_int[3]) 
        ]
    strdex_weapons = [
            Style(background_color=attr_strdex[0]),
            Style(background_color=attr_strdex[1]),
            Style(background_color=attr_strdex[2]), 
            Style(background_color=attr_strdex[3]) 
        ]
    strint_weapons = [
            Style(background_color=attr_strint[0]),
            Style(background_color=attr_strint[1]),
            Style(background_color=attr_strint[2]), 
            Style(background_color=attr_strint[3]) 
        ]
    dexint_weapons = [
            Style(background_color=attr_dexint[0]),
            Style(background_color=attr_dexint[1]),
            Style(background_color=attr_dexint[2]), 
            Style(background_color=attr_dexint[3]) 
        ]
    quivers = [
            Style(background_color=attr_dex[0]),
            Style(background_color=attr_dex[1]),
            Style(background_color=attr_dex[2]), 
            Style(background_color=attr_dex[3]) 
        ]
    fishing = [
            Style(text_color="#ff0000", background_color="#ffffff", font_size=45),
            Style(text_color="#ff0000", background_color="#ffffff", font_size=45),
            Style(text_color="#ff0000", background_color="#ffffff", font_size=45),
            Style(text_color="#ff0000", background_color="#ffffff", font_size=45)
        ]


# Apply default filter to everything
# ==================================

with show():
    default.apply()
    cont()



# Apply styles to items without rarity
# ====================================

with conditions(cond("Class", "Currency")):
    # Filter out low tier currency based on AreaLevel
    with conditions(cond("BaseType", "Scroll of Wisdom")):
        with show():
            condition("AreaLevel <= 23")
            Theme.wisdom.apply()

        with hide():
            condition("AreaLevel > 23")
            Theme.wisdom.apply()
            hidden.apply()

    with conditions(cond("BaseType", "Portal Scroll")):
        with show():
            condition("AreaLevel <= 40")
            Theme.portal.apply()

        with hide():
            condition("AreaLevel > 40")
            Theme.portal.apply()
            hidden.apply()

    with show():
        condition("BaseType",
                "Exalted Orb", "Mirror of Kalandra", "Albino Rhoa Feather")
        Icons.extremely_valuable.apply()
        Theme.extremely_valuable.apply()
        Sounds.exalt.apply()

    with show():
        condition("BaseType",
                "Ancient Orb", "Divine Orb")
        Icons.very_valuable.apply()
        Theme.very_valuable.apply()

    with show():
        condition("BaseType", "of Transmutation")
        Theme.transmute.apply()

    with show():
        condition("BaseType",
                "of Alteration", "of Augmentation", "Regal Orb")
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
    

with conditions(cond("Class", "Fragment")):
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

with conditions(cond("Class", "Gems")):
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
        condition("GemLevel > 15")
        Theme.gems.apply()

    with hide():
        Theme.gems.apply()
        hidden.apply()


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
with show():
    condition("AreaLevel <= 68")
    condition("SocketGroup", *main_socket_groups)
    Theme.good_sockets.apply()

with show():
    condition("AreaLevel <= 68")
    condition("SocketGroup", *other_socket_groups)
    Theme.ok_sockets.apply()

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

# Apply specific styles to each class / basetype
for idx, rarity in enumerate(["Normal", "Magic", "Rare", "Unique"]):
    with conditions(cond("Rarity", rarity)):
        
        with show():
            condition("Class", "Abyss")
            Theme.abyss[idx].apply()

        with conditions(cond("Class", "Jewel")):
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

        with show():
            condition("Class", "Rings")
            Theme.rings[idx].apply()

        with show():
            condition("Class", "Belts")
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

        # TODO: Make magic / rare / unique items outside the selected weapon types
        # still show for certain arealevels

        with (show if "thrusting" in weapon_types else hide)():
            condition("Class", "Thrusting")
            Theme.dex_weapons[idx].apply()

        with (show if "bows" in weapon_types else hide)():
            condition("Class", "Bow")
            Theme.dex_weapons[idx].apply()

        with (show if "bows" in weapon_types else hide)():
            condition("Class", "Quivers")
            Theme.quivers[idx].apply()

        with (show if "wands" in weapon_types else hide)():
            condition("Class", "Wand")
            Theme.int_weapons[idx].apply()

        # TODO: Separate one / two hand axe, maces, and swords
        with (show if "axes" in weapon_types else hide)():
            condition("Class", "Hand Axe")
            Theme.strdex_weapons[idx].apply()

        with (show if "maces" in weapon_types else hide)():
            condition("Class", "Hand Mace")
            Theme.str_weapons[idx].apply()

        with (show if "swords" in weapon_types else hide)():
            condition("Class", "Hand Sword")
            Theme.strdex_weapons[idx].apply()

        with (show if "sceptres" in weapon_types else hide)():
            condition("Class", "Sceptre")
            Theme.strint_weapons[idx].apply()

        with (show if "warstaves" in weapon_types else hide)():
            condition("Class", "Warstaves")
            Theme.strint_weapons[idx].apply()

        with (show if "staves" in weapon_types else hide)():
            condition("Class", "Staves")
            Theme.strint_weapons[idx].apply()

        with (show if "claws" in weapon_types else hide)():
            condition("Class", "Claw")
            Theme.dexint_weapons[idx].apply()

        with (show if "rune daggers" in weapon_types else hide)():
            condition("Class", "Rune Dagger")
            Theme.dexint_weapons[idx].apply()

        with (show if "daggers" in weapon_types else hide)():
            condition("Class", "Dagger")
            Theme.dexint_weapons[idx].apply()


        str_armour = [
                # Str Gloves
                "Iron Gauntlets", "Plated Gauntlets",
                "Bronze Gauntlets", "Steel Gauntlets",
                "Antique Gauntlets", "Ancient Gauntlets",
                "Goliath Gauntlets", "Vaal Gauntlets",
                "Titan Gauntlets", "Spiked Gloves",
                # Str Boots
                "Iron Greaves", "Steel Greaves",
                "Plated Greaves", "Reinforced Greaves",
                "Antique Greaves", "Ancient Greaves",
                "Goliath Greaves", "Vaal Greaves",
                "Titan Greaves",
                # Str Helmets
                "Iron Hat", "Cone Helmet",
                "Barbute Helmet", "Close Helmet",
                "Gladiator Helmet", "Reaver Helmet",
                "Siege Helmet", "Samite Helmet",
                "Ezomyte Burgonet", "Royal Burgonet",
                "Eternal Burgonet",
                # Str Body Armour
                "Plate Vest", "Chestplate",
                "Copper Plate", "War Plate",
                "Full Plate", "Arena Plate",
                "Lordly Plate", "Bronze Plate",
                "Battle Plate", "Sun Plate",
                "Colosseum Plate", "Majestic Plate",
                "Golden Plate", "Crusader Plate",
                "Astral Plate", "Gladiator Plate",
                "Glorious Plate",
                # Str Shields
                "Tower Shield"
            ]
        dex_armour = [
                # Dex Gloves
                "Rawhide Gloves", "Goathide Gloves",
                "Deerskin Gloves", "Nubuck Gloves",
                "Eelskin Gloves", "Sharkskin Gloves",
                "Shagreen Gloves", "Stealth Gloves",
                "Gripped Gloves", "Slink Gloves",
                # Dex Boots
                "Rawhide Boots", "Goathide Boots",
                "Deerskin Boots", "Nubuck Boots",
                "Eelskin Boots", "Sharkskin Boots",
                "Shagreen Boots", "Stealth Boots",
                "Slink Boots",
                # Dex Helmets
                "Leather Cap", "Tricorne",
                "Leather Hood", "Wolf Pelt",
                "Hunter Hood", "Noble Tricorne",
                "Ursine Pelt", "Silken Hood",
                "Sinner Tricorne", "Lion Pelt",
                # Dex Body Armour
                "Shabby Jerkin", "Strapped Leather",
                "Buckskin Tunic", "Wild Leather",
                "Full Leather", "Sun Leather",
                "Thief's Garb", "Eelskin Tunic",
                "Frontier Leather", "Glorious Leather",
                "Coronal Leather", "Cutthroat's Garb",
                "Sharkskin Tunic", "Destiny Leather",
                "Exquisite Leather", "Zodiac Leather",
                "Assassin's Garb",
                # Dex Shields
                "Buckler"
            ]
        int_armour = [
                # Int Gloves
                "Wool Gloves", "Velvet Gloves",
                "Silk Gloves", "Embroidered Gloves",
                "Satin Gloves", "Samite Gloves",
                "Conjurer Gloves", "Arcanist Gloves",
                "Sorcerer Gloves", "Fingerless Silk Gloves",
                # Int Boots
                "Wool Shoes", "Velvet Slippers",
                "Silk Slippers", "Scholar Boots",
                "Satin Slippers", "Samite Slippers",
                "Conjurer Boots", "Arcanist Slippers",
                "Sorcerer Boots",
                # Int Helmets
                "Vine Circlet", "Iron Circlet",
                "Torture Cage", "Tribal Circlet",
                "Bone Circlet", "Lunaris Circlet",
                "Steel Circlet", "Necromancer Circlet",
                "Solaris Circlet", "Mind Cage",
                "Hubris Circlet",
                # Int Body Armour
                "Simple Robe", "Silken Vest",
                "Scholar's Robe", "Silken Garb",
                "Mage's Vestment", "Silk Robe",
                "Cabalist Regalia", "Sage's Robe",
                "Silken Wrap", "Conjurer's Vestment",
                "Spidersilk Robe", "Destroyer Regalia",
                "Savant's Robe", "Necromancer Silks",
                "Occultist's Vestment", "Widowsilk Robe",
                "Vaal Regalia",
                # Int Shields
                "Spirit Shield"
            ]
        strdex_armour = [
                # Str + Dex Gloves
                "Fishscale Gauntlets", "Ironscale Gauntlets",
                "Bronzescale Gauntlets", "Steelscale Gauntlets",
                "Serpentscale Gauntlets", "Wyrmscale Gauntlets",
                "Hydrascale Gauntlets", "Dragonscale Gauntlets",
                # Str + Dex Boots
                "Leatherscale Boots", "Ironscale Boots",
                "Bronzescale Boots", "Steelscale Boots",
                "Serpentscale Boots", "Wyrmscale Boots",
                "Hydrascale Boots", "Dragonscale Boots",
                # TODO: Two Toned Boots
                # Str + Dex Helmets
                "Battered Helm", "Sallet",
                "Visored Sallet", "Gilded Sallet",
                "Secutor Helm", "Fencer Helm",
                "Lacquered Helmet", "Fluted Bascinet",
                "Pig-Faced Bascinet", "Nightmare Bascinet",
                # Str + Dex Body Armour
                "Scale Vest", "Light Brigandine",
                "Scale Doublet", "Infantry Brigandine",
                "Full Scale Armour", "Soldier's Brigandine",
                "Field Lamellar", "Wyrmscale Doublet",
                "Hussar Brigandine", "Full Wyrmscale",
                "Commander's Brigandine", "Battle Lamellar",
                "Dragonscale Doublet", "Desert Brigandine",
                "Full Dragonscale", "General's Brigandine",
                "Triumphant Lamellar",
                # Str + Dex Shields
                "Round Shield"
            ]
        strint_armour = [
                # Str + Int Gloves
                "Chain Gloves", "Ringmail Gloves",
                "Mesh Gloves", "Riveted Gloves",
                "Zealot Gloves", "Soldier Gloves",
                "Legion Gloves", "Crusader Gloves",
                # Str + Int Boots
                "Chain Boots", "Ringmail Boots",
                "Mesh Boots", "Riveted Boots",
                "Zealot Boots", "Soldier Boots",
                "Legion Boots", "Crusader Boots",
                # TODO: Two Toned Boots
                # Str + Int Helmets
                "Rusted Coif", "Soldier Helmet",
                "Great Helmet", "Crusader Helmet",
                "Aventail Helmet", "Zealot Helmet",
                "Great Crown", "Magistrate Crown",
                "Prophet Crown", "Praetor Crown",
                "Bone Helmet",
                # Str + Int Body Armour
                "Chainmail Vest", "Chainmail Tunic",
                "Ringmail Coat", "Chainmail Doublet",
                "Full Ringmail", "Full Chainmail",
                "Holy Chainmail", "Latticed Ringmail",
                "Crusader Chainmail", "Ornate Ringmail",
                "Chain Hauberk", "Devout Chainmail",
                "Loricated Ringmail", "Conquest Chainmail",
                "Elegant Ringmail", "Saint's Hauberk",
                "Saintly Chainmail",
                # Str + Int Shields
                "Kite Shield"
            ]
        dexint_armour = [
                # Dex + Int Gloves
                "Wrapped Mitts", "Strapped Mitts",
                "Clasped Mitts", "Trapper Mitts",
                "Ambush Mitts", "Carnal Mitts",
                "Assassin's Mitts", "Murder Mitts",
                # Dex + Int Boots
                "Wrapped Boots", "Strapped Boots",
                "Clasped Boots", "Shackled Boots",
                "Trapper Boots", "Ambush Boots",
                "Carnal Boots", "Assassin's Boots",
                "Murder Boots",
                # TODO: Two Toned Boots
                # Dex + Int Helmets
                "Scare Mask", "Plague Mask",
                "Iron Mask", "Festival Mask",
                "Golden Mask", "Raven Mask",
                "Callous Mask", "Regicide Mask",
                "Harlequin Mask", "Vaal Mask",
                "Deicide Mask",
                # Dex + Int Body Armour
                "Padded Vest", "Oiled Vest",
                "Padded Jacket", "Oiled Coat",
                "Scarlet Raiment", "Waxed Garb",
                "Bone Armour", "Quilted Jacket",
                "Sleek Coat", "Crimson Raiment",
                "Lacquered Garb", "Crypt Armour",
                "Sentinel Jacket", "Varnished Coat",
                "Blood Raiment", "Sadist Garb",
                "Carnal Armour",
                # Dex + Int Shields
                "Spiked Bundle", "Spiked Shield"
            ]

        with conditions(cond("Class",
                    "Gloves", "Boots", "Helmets", "Body", "Shields")):

            # Below these levels, show that rarity regardless of base type
            arealevels = {
                    "Normal": 1,
                    "Magic": 13,
                    "Rare": 23,
                    "Unique": 68
                }

            with conditions(cond("AreaLevel", "<=", arealevels[rarity])):
                with show():
                    condition("BaseType", *str_armour)
                    Theme.str_armour[idx].apply()

                with show():
                    condition("BaseType", *dex_armour)
                    Theme.dex_armour[idx].apply()

                with show():
                    condition("BaseType", *int_armour)
                    Theme.int_armour[idx].apply()
                    
                with show():
                    condition("BaseType", *strdex_armour)
                    Theme.strdex_armour[idx].apply()

                with show():
                    condition("BaseType", *strint_armour)
                    Theme.strint_armour[idx].apply()

                with show():
                    condition("BaseType", *dexint_armour)
                    Theme.dexint_armour[idx].apply()

            with (show if "str" in armour_types else hide)():
                condition("BaseType", *str_armour)
                Theme.str_armour[idx].apply()

            with (show if "dex" in armour_types else hide)():
                condition("BaseType", *dex_armour)
                Theme.dex_armour[idx].apply()

            with (show if "int" in armour_types else hide)():
                condition("BaseType", *int_armour)
                Theme.int_armour[idx].apply()
                
            with (show if "strdex" in armour_types else hide)():
                condition("BaseType", *strdex_armour)
                Theme.strdex_armour[idx].apply()

            with (show if "strint" in armour_types else hide)():
                condition("BaseType", *strint_armour)
                Theme.strint_armour[idx].apply()

            with (show if "dexint" in armour_types else hide)():
                condition("BaseType", *dexint_armour)
                Theme.dexint_armour[idx].apply()
