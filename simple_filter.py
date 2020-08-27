from poefilter import *

default = Style(
        background_color="0 0 0",
        text_color="255 0 255",
        font_size=45)

# Categories without rarity
class Theme:
    # Class Currency
    magic_orbs = Style(
            text_color="171 232 240",
            background_color="17 109 130")
    rare_orbs = Style(
            text_color="255 246 182",
            background_color="169 104 98")
    other_orbs = Style(
            text_color="255 216 206",
            background_color="149 104 71")
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
            background_color="112 79 44")
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
            background_color="0 88 45")
    incubators = Style(
            text_color="201 192 179",
            background_color="78 38 13")
    divination = Style(
            text_color="111 231 252",
            background_color="73 27 76")
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
            text_color="#c8c8c8",
            background_color="#141414")

    rarity_magic = Style(
            text_color="#8889ff",
            background_color="#141414")

    rarity_rare = Style(
            text_color="#feff77",
            background_color="#141414")

    rarity_unique = Style(
            text_color="#b45000",
            background_color="#141414",
            play_effect_color="Brown",
            minimap_icon_size=1,
            minimap_icon_color="Brown",
            minimap_icon_shape="Diamond")

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
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    mana_flasks = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    hybrid_flasks = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    utility_flasks = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    str_armour = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    dex_armour = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    int_armour = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    strdex_armour = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    strint_armour = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    dexint_armour = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    str_weapons = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    dex_weapons = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    int_weapons = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    strdex_weapons = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    strint_weapons = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    dexint_weapons = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    quivers = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]
    fishing = [
            rarity_normal,
            rarity_magic,
            rarity_rare, 
            rarity_unique
        ]


# Apply default filter to everything
# ==================================

with show_continue():
    default.apply()


# Apply default styles for rarity
# ===============================

with show_continue():
    condition("Rarity Normal")
    Theme.rarity_normal.apply()

with show_continue():
    condition("Rarity Magic")
    Theme.rarity_magic.apply()

with show_continue():
    condition("Rarity Rare")
    Theme.rarity_rare.apply()

with show_continue():
    condition("Rarity Unique")
    Theme.rarity_unique.apply()


# Apply styles to items without rarity
# ====================================

with conditions(cond("Class", "Currency")):
    with show():
        condition("BaseType",
                "of Alteration", "of Augmentation",
                "of Transmutation", "Regal Orb")
        Theme.magic_orbs.apply()

    with show():
        condition("BaseType",
                "Chaos Orb", "Orb of Annulment",
                "Divine Orb", "Exalted Orb")
        Theme.rare_orbs.apply()

    with show():
        condition("BaseType",
                "Scrap", "Whetstone", "Prisim", "Bauble")
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
            condition("Class", "Quivers")
            Theme.quivers[idx].apply()

        with show():
            condition("Class", "Fishing")
            Theme.fishing[idx].apply()

        with show():
            condition("Class", "Hand Mace")
            Theme.str_weapons[idx].apply()

        with show():
            condition("Class", "Thrusting", "Bow")
            Theme.dex_weapons[idx].apply()

        with show():
            condition("Class", "Wand")
            Theme.int_weapons[idx].apply()

        with show():
            condition("Class", "Hand Axe", "Hand Sword")
            Theme.strdex_weapons[idx].apply()

        with show():
            condition("Class", "Sceptre", "Staff", "Warstaff")
            Theme.strint_weapons[idx].apply()

        with show():
            condition("Class", "Claw", "Dagger")
            Theme.dexint_weapons[idx].apply()


        with conditions(
                cond("Class",
                    "Gloves", "Boots", "Helmets", "Body", "Shields")
                ):

            with show():
                condition("BaseType",
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
                        "Tower Shield")
                Theme.str_armour[idx].apply()

            with show():
                condition("BaseType",
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
                        "Exquisite Leather", "Zodiak Leather",
                        "Assassin's Garb",
                        # Dex Shields
                        "Buckler")
                Theme.dex_armour[idx].apply()

            with show():
                condition("BaseType",
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
                        "Spirit Shield")
                Theme.int_armour[idx].apply()

                
            with show():
                condition("BaseType",
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
                        "Round Shield")
                Theme.strdex_armour[idx].apply()

            with show():
                condition("BaseType",
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
                        "Kite Shield")
                Theme.strint_armour[idx].apply()

            with show():
                condition("BaseType",
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
                        "Spiked Bundle", "Spiked Shield")
                Theme.dexint_armour[idx].apply()
