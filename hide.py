from poefilter import *

hidden = Style(size=28)

def apply(config):
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

