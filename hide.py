from poefilter import *
import tables

hidden = Style(size=28)

# Some show() groups don't need anything additional, so this marks it as complete
def done():
    pass

def apply(config, colors, icons, sounds):

    # Always show Fishing Rods, top tier currency, and 6Ls
    with conditions(("Class", "Fishing")), show():
        done()

    with conditions(("LinkedSockets", "6")), show():
        done()

    with conditions(("BaseType", "Exalted", "Mirror", "Feather")), show():
        done()

    if config.show_5_links:
        with conditions(("LinkedSockets", "5")), show():
            icons.valuable.apply()
            sounds.swish.apply()

    # Always show influenced items
    # TODO: Emphasize top tier bases
    with conditions(("HasInfluence", *tables.influences)), show():
        icons.cyan_diamond_beam.apply()
        sounds.swish.apply()

    # Hide Scrolls of Wisdom after act 5, Portal Scrolls after act 10
    with conditions(
            ("AreaLevel", ">", tables.act_5_max_level),
            ("BaseType", "Scroll of Wisdom")), hide():
        hidden.apply()
    with conditions(
            ("AreaLevel", ">", tables.act_10_max_level),
            ("BaseType", "Portal Scroll")), hide():
        hidden.apply()

    # Show all Magic items until the end of Act 1
    with conditions(
            ("Rarity", "Magic"),
            ("AreaLevel", "<=", tables.act_1_max_level)), show():
        icons.blue_circle.apply()

    # Show all Rare items until the end of Act 4
    with conditions(
            ("Rarity", "Rare"),
            ("AreaLevel", "<=", tables.act_4_max_level)), show():
        icons.yellow_circle.apply()

    # Filter out undesirable armour types
    for tag, armour in [
            ("int", tables.int_armour),
            ("dex", tables.dex_armour),
            ("str", tables.str_armour),
            ("strdex", tables.strdex_armour),
            ("strint", tables.strint_armour),
            ("dexint", tables.dexint_armour)]:
        if tag not in config.armour_types:
            with conditions(("Rarity", "<", "Unique"), ("BaseType", *armour)), hide():
                hidden.apply()

    # Hide all non-unique weapons that we do not care about
    for w in tables.weapon_classes:
        if w not in config.weapon_types:
            with conditions(("Rarity", "<", "Unique"), ("Class", w)), hide():
                hidden.apply()

    # Now that weapon and armour types have been filtered out, show anything
    # matching our socket groups regardless of rarity
    if config.main_socket_groups:
        with conditions(("SocketGroup", *config.main_socket_groups)), show():
            icons.green_circle_beam.apply()
            sounds.echo_light.apply()

    if config.other_socket_groups:
        with conditions(("SocketGroup", *config.other_socket_groups)), show():
            done()

    # Don't show bad corrupts with 0 mods
    with hide():
        condition("Corrupted", "True")
        condition("FracturedItem", "False")
        condition("SynthesisedItem", "False")
        condition("Class",
                "Rings", "Belts", "Quivers", "Mace", "Sword",
                "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
                "Claw", "Gloves", "Helmets", "Body", "Shields")
        condition("CorruptedMods", "==", 0)
        hidden.apply()

    # Filter stuff out based on arealevel
    # ===================================
    # Hide Rare except trinkets and jewels after Act 10
    with conditions(
            ("Rarity", "<=", "Rare"),
            ("AreaLevel", ">", tables.act_10_max_level),
            ("Class", *tables.weapon_classes, *tables.armour_classes, "Flasks"),
            ("Identified", "False")), hide():
        hidden.apply()

    with hide(): # Hide Magic after Act 3, except flasks
        condition("Rarity", "<", "Rare")
        condition("AreaLevel", ">=", tables.act_3_max_level)
        condition("Class",
                "Amulets", "Rings", "Belts", "Quivers", "Mace",
                "Sword", "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
                "Claw", "Gloves", "Helmets", "Body", "Shields", "Boots")
        condition("Identified", "False")
        hidden.apply()

    with hide(): # Hide Normal after Act 2, except flasks
        condition("Rarity", "<", "Magic")
        condition("AreaLevel", ">", tables.act_2_max_level)
        condition("Class",
                "Amulets", "Rings", "Belts", "Quivers", "Mace",
                "Sword", "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
                "Claw", "Gloves", "Helmets", "Body", "Shields", "Boots")
        condition("Identified", "False")
        hidden.apply()

