from poefilter import *
import tables

hidden = Style(size=30, disable_drop_sound=True)

# Some show() groups don't need anything additional, so this marks it as complete
def done():
    pass

def apply(config):

    # Always show Fishing Rods, top tier currency, and 6Ls
    with conditions(("Class", "Fishing")), show():
        done()

    with conditions(("LinkedSockets", "6")), show():
        done()

    with conditions(("BaseType", "Exalted", "Mirror of", "Mirror Shard", "Feather")), show():
        done()

    if config.show_5_links:
        with conditions(("LinkedSockets", "5")), show():
            done()

    # Always show influenced items
    # TODO: Emphasize top tier bases
    with conditions(("HasInfluence", *tables.influences)), show():
        done()

    with conditions(("HasExplicitMod", "Veil")), show():
        done()

    # Hide Scrolls of Wisdom after act 5, Portal Scrolls after act 10
    with conditions(
            ("AreaLevel", ">", tables.act_5_max_level),
            ("BaseType", "Scroll of Wisdom")), hide():
        hidden.apply()
    with conditions(
            ("AreaLevel", ">", tables.act_10_max_level),
            ("BaseType", "Portal Scroll")), hide():
        hidden.apply()

    # Jeweller's Orb recipe
    with conditions(("Sockets", "6"), ("LinkedSockets", "<", 5)), show():
        done()

    # Chromatic Orb recipe
    with conditions(
            ("SocketGroup", "RGB"),
            ("AreaLevel", "<=", tables.act_10_max_level)), show():
        done()

    # Hide non-quality gems in endgame
    with conditions(("Class", "Gems"), ("AreaLevel", ">=", tables.act_10_max_level)):
        with conditions(("BaseType", *tables.drop_gems)), show():
            done()

        with conditions(("Quality", ">", 0)), show():
            done()

        with conditions(("Corrupted", "True")), show():
            done()

        with conditions(("BaseType", "Awakened")), show():
            done()

        # Show high level gems that could reduce leveling time / make easy 20% recipe
        with conditions(("GemLevel", ">=", 15)), show():
            done()

        with hide():
            hidden.apply()

    # Show all Magic items until the end of Act 1
    with conditions(
            ("Rarity", "Magic"),
            ("AreaLevel", "<=", tables.act_1_max_level)), show():
        done()

    # Show all Rare items until the end of Act 4
    with conditions(
            ("Rarity", "Rare"),
            ("AreaLevel", "<=", tables.act_4_max_level)), show():
        done()

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
        with conditions(
                ("Rarity", "<", "Unique"),
                ("Class", w),
                ("AreaLevel", ">", tables.act_10_max_level)), hide():
            hidden.apply()

    # Now that weapon and armour types have been filtered out, show anything
    # matching our socket groups regardless of rarity
    if config.main_socket_groups:
        with conditions(
                ("SocketGroup", *config.main_socket_groups),
                ("AreaLevel", "<=", tables.act_10_max_level)), show():
            done()

    if config.other_socket_groups:
        with conditions(
                ("SocketGroup", *config.other_socket_groups),
                ("AreaLevel", "<=", tables.act_10_max_level)), show():
            done()

    # Don't show bad corrupts with 0 mods
    with hide():
        condition("Corrupted", "True")
        condition("FracturedItem", "False")
        condition("SynthesisedItem", "False")
        condition("Rarity", "<=", "Rare")
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
            ("Class", *(tables.weapon_classes + tables.armour_classes), "Flasks"),
            ("Identified", "False")), hide():
        hidden.apply()

    with hide(): # Hide Magic after Act 3, except flasks
        condition("Rarity", "<", "Rare")
        condition("AreaLevel", ">=", tables.act_3_max_level)
        condition("Class",
                "Amulets", "Rings", "Belts", "Quivers", "Mace",
                "Sword", "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
                "Claw", "Gloves", "Helmets", "Body", "Shields", "Boots", "Jewel")
        condition("Identified", "False")
        hidden.apply()

    with hide(): # Hide Normal after Act 2, except flasks
        condition("Rarity", "<", "Magic")
        condition("AreaLevel", ">", tables.act_2_max_level)
        condition("Class",
                "Amulets", "Rings", "Belts", "Quivers", "Mace",
                "Sword", "Axe", "Bow", "Wand", "Sceptre", "taves", "Dagger",
                "Claw", "Gloves", "Helmets", "Body", "Shield", "Boots")
        condition("Identified", "False")
        hidden.apply()

    # Filter Uniques by tier

    with conditions(("Rarity", "Unique")):
        if tables.unique_bottom:
            if config.hide_unique_tier >= 0:
                with conditions(("BaseType", *tables.unique_bottom)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.unique_bottom)), show():
                    done()
        
        if tables.unique_lower:
            if config.hide_unique_tier >= 1:
                with conditions(("BaseType", *tables.unique_lower)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.unique_lower)), show():
                    done()

        if tables.unique_low:
            if config.hide_unique_tier >= 2:
                with conditions(("BaseType", *tables.unique_low)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.unique_low)), show():
                    done()

        if tables.unique_mid:
            if config.hide_unique_tier >= 3:
                with conditions(("BaseType", *tables.unique_mid)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.unique_mid)), show():
                    done()

        if tables.unique_high:
            if config.hide_unique_tier >= 4:
                with conditions(("BaseType", *tables.unique_high)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.unique_high)), show():
                    done()

        if tables.unique_higher:
            if config.hide_unique_tier >= 5:
                with conditions(("BaseType", *tables.unique_higher)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.unique_higher)), show():
                    done()

        if tables.unique_top:
            with conditions(("BaseType", *tables.unique_top)), show():
                done()

    # Filter Divination cards by tier

    with conditions(("Class", "Divination")):
        if tables.divination_bottom and config.hide_div_tier >= 0:
            with conditions(("BaseType", *tables.divination_bottom)), hide():
                hidden.apply()
        
        if tables.divination_lower and config.hide_div_tier >= 1:
            with conditions(("BaseType", *tables.divination_lower)), hide():
                hidden.apply()

        if tables.divination_low and config.hide_div_tier >= 2:
            with conditions(("BaseType", *tables.divination_low)), hide():
                hidden.apply()

        if tables.divination_mid:
            if config.hide_div_tier >= 3:
                with conditions(("BaseType", *tables.divination_mid)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.divination_mid)), show():
                    done()

        if tables.divination_high:
            if config.hide_div_tier >= 4:
                with conditions(("BaseType", *tables.divination_high)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.divination_high)), show():
                    done()

        if tables.divination_higher:
            if config.hide_div_tier >= 5:
                with conditions(("BaseType", *tables.divination_higher)), hide():
                    hidden.apply()
            else:
                with conditions(("BaseType", *tables.divination_higher)), show():
                    done()

        if tables.divination_top:
            with conditions(("BaseType", *tables.divination_top)), show():
                done()

    # Filter Prophecies by tier

    with conditions(("BaseType", "Prophecy")):
        if tables.prophecy_bottom and config.hide_proph_tier >= 0:
            with conditions(("Prophecy", *tables.prophecy_bottom)), hide():
                hidden.apply()
        
        if tables.prophecy_lower and config.hide_proph_tier >= 1:
            with conditions(("Prophecy", *tables.prophecy_lower)), hide():
                hidden.apply()

        if tables.prophecy_low and config.hide_proph_tier >= 2:
            with conditions(("Prophecy", *tables.prophecy_low)), hide():
                hidden.apply()

        if tables.prophecy_mid:
            if config.hide_proph_tier >= 3:
                with conditions(("Prophecy", *tables.prophecy_mid)), hide():
                    hidden.apply()
            else:
                with conditions(("Prophecy", *tables.prophecy_mid)), show():
                    done()

        if tables.prophecy_high:
            if config.hide_proph_tier >= 4:
                with conditions(("Prophecy", *tables.prophecy_high)), hide():
                    hidden.apply()
            else:
                with conditions(("Prophecy", *tables.prophecy_high)), show():
                    done()

        if tables.prophecy_higher:
            if config.hide_proph_tier >= 5:
                with conditions(("Prophecy", *tables.prophecy_higher)), hide():
                    hidden.apply()
            else:
                with conditions(("Prophecy", *tables.prophecy_higher)), show():
                    done()

        if tables.prophecy_top:
            with conditions(("Prophecy", *tables.prophecy_top)), show():
                done()
