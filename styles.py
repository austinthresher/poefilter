from poefilter import *
import tables

def apply(config, theme, icons, sounds):
    # Apply default filter to everything
    # ==================================

    with show():
        theme.default.apply()


    # Apply styles to items without rarity
    # ====================================

    with conditions(("Class", "Currency")):
        with conditions(("BaseType", "Scroll of Wisdom")), show():
            theme.wisdom.apply()

        with conditions(("BaseType", "Portal Scroll")), show():
            theme.portal.apply()

        with conditions((
                "BaseType", "Exalted Orb", "Mirror of Kalandra",
                "Albino Rhoa Feather"
                )), show():
            icons.extremely_valuable.apply()
            theme.extremely_valuable.apply()
            sounds.exalt.apply()

        with conditions((
                "BaseType", "Ancient Orb", "Divine Orb"
                )), show():
            icons.very_valuable.apply()
            theme.very_valuable.apply()

        with conditions(("BaseType", "of Transmutation")), show():
            theme.transmute.apply()

        with conditions((
                "BaseType", "of Alteration", "of Augmentation", "Regal Orb"
                )), show():
            theme.magic_orbs.apply()

        with conditions(("BaseType", "Chaos Orb", "Orb of Annulment")), show():
            icons.valuable.apply()
            theme.valuable.apply()
            sounds.chaos.apply()

        with conditions((
                "BaseType", "Scrap", "Whetstone", "Prism", "Bauble"
                )), show():
            theme.quality.apply()

        with conditions(("BaseType", "Chisel", "Sextant")), show():
            theme.map_currency.apply()

        with conditions(("BaseType", "Prophecy")), show():
            theme.prophecies.apply()

        with conditions(("BaseType", "Shard")), show():
            theme.shards.apply()

        with conditions(("BaseType", "Essence")), show():
            theme.essences.apply()

        with conditions(("BaseType", "Fossil", "Resonator")), show():
            theme.delve.apply()

        with conditions(("BaseType", "Oil")), show():
            theme.oils.apply()

        with conditions(("BaseType", "Catalyst")), show():
            theme.catalysts.apply()

        with conditions(("BaseType", "Vial")), show():
            theme.vials.apply()

        with conditions(("BaseType", "Delirium")), show():
            theme.delirium.apply()
        
        with conditions(("BaseType", "Orb")), show():
            theme.other_orbs.apply()
        
        with show():
            theme.other_currency.apply()
        

    with conditions(("Class", "Fragment")):
        with conditions((
                "BaseType", "Esh", "Tul", "Chayula", "Xoph", "Netol"
                )), show():
            theme.breachstones.apply()

        with conditions(("BaseType", "Timeless")), show():
            theme.emblems.apply()

        with conditions(("BaseType", "Scarab")), show():
            theme.scarabs.apply()

        # Other fragments
        with show():
            theme.frags.apply()


    with conditions(("Class", "Quest", "Labyrinth")), show():
        theme.quest.apply()

    with conditions(("Class", "Incubator")), show():
        theme.incubators.apply()

    with conditions(("Class", "Divination")), show():
        theme.divination.apply()

    with conditions(("Class", "Gems")):
        with conditions(("Corrupted", "True")), show():
            theme.corrupted.apply()

        with conditions(("BaseType", "Awakened")), show():
            theme.awakened_gems.apply()

        with conditions(("BaseType", "Enlighten", "Enhance", "Empower")), show():
            theme.drop_gems.apply()

        with show():
            theme.gems.apply()

    with conditions(("Class", "Metamorph")), show():
        theme.metamorph.apply()

    with conditions(("Class", "Seed")), show():
        theme.seeds.apply()


    # Apply styles to items with rarity
    # =================================

    # Apply default styles for rarity
    with conditions(("Rarity", "Normal")), show():
        theme.rarity_normal.apply()

    with conditions(("Rarity", "Magic")), show():
        theme.rarity_magic.apply()

    with conditions(("Rarity", "Rare")), show():
        theme.rarity_rare.apply()

    with conditions(("Rarity", "Unique")), show():
        theme.rarity_unique.apply()

    # Misc highlights / emphasis
    # ==========================

    # Leveling socket types
    with conditions(
                ("AreaLevel", "<=", "68"),
                ("SocketGroup", *config.other_socket_groups)), show():
        theme.ok_sockets.apply()

    with conditions(
                ("AreaLevel", "<=", "68"),
                ("SocketGroup", *config.main_socket_groups)), show():
        theme.good_sockets.apply()

    # 5 & 6 links
    with conditions(("LinkedSockets", "5")), show():
        icons.valuable.apply()
        theme.valuable.apply()

    with conditions(("LinkedSockets", "6")), show():
        icons.very_valuable.apply()
        theme.very_valuable.apply()

    # Influences
    # TODO: Different colors for top tier bases
    with conditions(("HasInfluence", "Shaper")), show():
        theme.shaper.apply()
        icons.valuable.apply()

    with conditions(("HasInfluence", "Elder")), show():
        theme.elder.apply()
        icons.valuable.apply()

    with conditions(("HasInfluence", "Warlord")), show():
        theme.warlord.apply()
        icons.valuable.apply()

    with conditions(("HasInfluence", "Hunter")), show():
        theme.hunter.apply()
        icons.valuable.apply()

    with conditions(("HasInfluence", "Redeemer")), show():
        theme.redeemer.apply()
        icons.valuable.apply()

    with conditions(("HasInfluence", "Crusader")), show():
        theme.crusader.apply()
        icons.valuable.apply()

    # Corruptions and Enchantments
    with conditions(
                ("Corrupted", "True"),
                ("AnyEnchantment", "False")), show():
        theme.corrupted.apply()

    with conditions(
                ("Corrupted", "False"),
                ("AnyEnchantment", "True")), show():
        theme.enchanted.apply()

    with conditions(
                ("Corrupted", "True"),
                ("AnyEnchantment", "True")), show():
        theme.corrupted_enchanted.apply()

    with conditions(("HasExplicitMod", "Veil")), show():
        theme.veiled.apply()

    # Apply specific styles to each class / basetype
    for idx, rarity in enumerate(["Normal", "Magic", "Rare", "Unique"]):
        with conditions(("Rarity", rarity)):
            with conditions(("Class", "Abyss")), show():
                theme.abyss[idx].apply()

            with conditions(("Class", "Jewel")):
                with conditions(("BaseType", "Cluster")), show():
                    theme.cluster[idx].apply()

                with show():
                    theme.jewels[idx].apply()

            with conditions(("Class", "Atlas")), show():
                theme.watchstones[idx].apply()

            with conditions(("Class", "Maps")), show():
                theme.maps[idx].apply()

            with conditions(("Class", "Amulets")):
                if config.highlighted_amulets:
                    with conditions(("BaseType", *config.highlighted_amulets)), show():
                        theme.highlighted_amulets[idx].apply()
                with show():
                    theme.amulets[idx].apply()

            with conditions(("Class", "Rings")):
                if config.highlighted_rings:
                    with conditions(("BaseType", *config.highlighted_rings)), show():
                        theme.highlighted_rings[idx].apply()
                with show():
                    theme.rings[idx].apply()

            with conditions(("Class", "Belts")):
                if config.highlighted_belts:
                    with conditions(("BaseType", *config.highlighted_belts)), show():
                        theme.highlighted_belts[idx].apply()
                with show():
                    theme.belts[idx].apply()

            with conditions(("Class", "Life Flasks")), show():
                theme.life_flasks[idx].apply()

            with conditions(("Class", "Mana Flasks")), show():
                theme.mana_flasks[idx].apply()

            with conditions(("Class", "Utility Flasks")), show():
                theme.utility_flasks[idx].apply()

            with conditions(("Class", "Hybrid Flasks")), show():
                theme.hybrid_flasks[idx].apply()

            with conditions(("Class", "Fishing")), show():
                theme.fishing[idx].apply()

            with conditions(("Class", "Thrusting", "Bow")), show():
                theme.dex_weapons[idx].apply()

            with conditions(("Class", "Quivers")), show():
                theme.quivers[idx].apply()

            with conditions(("Class", "Wand")), show():
                theme.int_weapons[idx].apply()

            with conditions(("Class", "Hand Axes", "Hand Swords")), show():
                theme.strdex_weapons[idx].apply()

            with conditions(("Class", "Hand Maces")), show():
                theme.str_weapons[idx].apply()

            with conditions(("Class", "Sceptre", "Warstaves", "Staves")), show():
                theme.strint_weapons[idx].apply()

            with conditions(("Class", "Claw", "Dagger")), show():
                theme.dexint_weapons[idx].apply()

            with conditions(("Class",
                        "Gloves", "Boots", "Helmets", "Body", "Shields")):
                with conditions(("BaseType", *tables.str_armour)), show():
                    theme.str_armour[idx].apply()

                with conditions(("BaseType", *tables.dex_armour)), show():
                    theme.dex_armour[idx].apply()

                with conditions(("BaseType", *tables.int_armour)), show():
                    theme.int_armour[idx].apply()
                    
                with conditions(("BaseType", *tables.strdex_armour)), show():
                    theme.strdex_armour[idx].apply()

                with conditions(("BaseType", *tables.strint_armour)), show():
                    theme.strint_armour[idx].apply()

                with conditions(("BaseType", *tables.dexint_armour)), show():
                    theme.dexint_armour[idx].apply()

