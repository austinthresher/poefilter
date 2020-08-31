from poefilter import *
import tables

# Map the style options defined in colors / icons / sounds
# to actual Path of Exile item classes and base types

def apply(config, colors, icons, sounds):

    # Apply default filter to everything
    with show():
        colors.default.apply()

    # Apply styles to items without rarity
    with conditions(("Class", "Currency")):
        with show():
            colors.other_currency.apply()

        with conditions(("BaseType", "Orb")), show():
            colors.other_orbs.apply()

        with conditions(("BaseType", "Scroll of Wisdom", "Scroll Fragment")), show():
            colors.wisdom.apply()

        with conditions(("BaseType", "Portal Scroll")), show():
            colors.portal.apply()

        with conditions((
                "BaseType", "Exalted Orb", "Mirror of Kalandra",
                "Albino Rhoa Feather"
                )), show():
            icons.currency_top.apply()
            colors.extremely_valuable.apply()
            sounds.currency_most.apply()

        with conditions((
                "BaseType", "Ancient Orb", "Divine Orb"
                )), show():
            icons.currency_higher.apply()
            colors.very_valuable.apply()
            sounds.currency_more.apply()

        with conditions(("BaseType", "of Transmutation")), show():
            colors.transmute.apply()

        with conditions(("BaseType", "of Augmentation")), show():
            colors.augmentation.apply()

        with conditions(("BaseType", "of Alteration")), show():
            colors.alteration.apply()

        with conditions(("BaseType", "Orb of Chance")), show():
            colors.chance.apply()

        with conditions(("BaseType", "Orb of Alchemy")), show():
            colors.alchemy.apply()

        with conditions(("BaseType", "Regal Orb")), show():
            colors.regal.apply()

        with conditions(("BaseType", "Chaos Orb")), show():
            icons.currency_high.apply()
            colors.chaos.apply()
            sounds.bang.apply()

        with conditions(("BaseType", "Vaal Orb")), show():
            icons.currency_high.apply()
            colors.vaal.apply()
            sounds.currency.apply()

        with conditions(("BaseType", "Orb of Annulment")), show():
            icons.currency_higher.apply()
            colors.valuable.apply()
            sounds.currency.apply()

        with conditions(("BaseType", "Jeweller's Orb")), show():
            colors.jewelers.apply()

        with conditions(("BaseType", "Orb of Fusing")), show():
            colors.fuse.apply()

        with conditions(("BaseType", "Chromatic Orb")), show():
            colors.chromatic.apply()

        with conditions(("BaseType", "Orb of Scouring")), show():
            colors.scouring.apply()

        with conditions(("BaseType", "Orb of Regret")), show():
            colors.regret.apply()

        with conditions(("BaseType", "Scrap")), show():
            colors.scrap.apply()

        with conditions(("BaseType", "Whetstone")), show():
            colors.whetstone.apply()

        with conditions(("BaseType", "Prism")), show():
            colors.prism.apply()

        with conditions(("BaseType", "Bauble")), show():
            colors.bauble.apply()

        with conditions(("BaseType", "Engineer's")), show():
            colors.engineer.apply()

        with conditions(("BaseType", "Chisel")), show():
            colors.chisel.apply()

        with conditions(("BaseType", "Simple Sextant")), show():
            colors.white_sextant.apply()

        with conditions(("BaseType", "Prime Sextant")), show():
            colors.yellow_sextant.apply()

        with conditions(("BaseType", "Awakened Sextant")), show():
            colors.red_sextant.apply()

        with conditions(("BaseType", "Prophecy")):
            with show():
                colors.prophecy_unknown.apply()

            if tables.prophecy_bottom:
                with conditions(("Prophecy", *tables.prophecy_bottom)), show():
                    colors.prophecy_bottom.apply()
            
            if tables.prophecy_lower:
                with conditions(("Prophecy", *tables.prophecy_lower)), show():
                    colors.prophecy_lower.apply()

            if tables.prophecy_low:
                with conditions(("Prophecy", *tables.prophecy_low)), show():
                    colors.prophecy_low.apply()

            if tables.prophecy_mid:
                with conditions(("Prophecy", *tables.prophecy_mid)), show():
                    colors.prophecy_mid.apply()

            if tables.prophecy_high:
                with conditions(("Prophecy", *tables.prophecy_high)), show():
                    colors.prophecy_high.apply()

            if tables.prophecy_higher:
                with conditions(("Prophecy", *tables.prophecy_higher)), show():
                    colors.prophecy_higher.apply()

            if tables.prophecy_top:
                with conditions(("Prophecy", *tables.prophecy_top)), show():
                    colors.prophecy_top.apply()

        # TODO: Shard types
        with conditions(("BaseType", "Shard")), show():
            colors.shards.apply()

        with conditions(("BaseType", "Whispering Essence")), show():
            colors.essence_bottom.apply()
        with conditions(("BaseType", "Muttering Essence")), show():
            colors.essence_lower.apply()
        with conditions(("BaseType", "Weeping Essence")), show():
            colors.essence_low.apply()
        with conditions(("BaseType", "Wailing Essence")), show():
            colors.essence_mid.apply()
        with conditions(("BaseType", "Screaming Essence")), show():
            colors.essence_high.apply()
        with conditions(("BaseType", "Shrieking Essence")), show():
            colors.essence_higher.apply()
        with conditions(
                ("BaseType",
                    "Deafening Essence", "Essence of Hysteria",
                    "Essence of Insanity", "Essence of Horror",
                    "Essence of Delirium")), show():
            colors.essence_top.apply()

        with conditions(("BaseType", "Remnant of Corruption")), show():
            colors.remnant.apply()

        with conditions(("BaseType", "Fossil")), show():
            colors.fossil.apply()

        with conditions(("BaseType", "Resonator")), show():
            colors.resonator.apply()

        # TODO: Oil tiers
        with conditions(("BaseType", "Oil")), show():
            colors.oils.apply()

        # TODO: Catalyst tiers
        with conditions(("BaseType", "Catalyst")), show():
            colors.catalysts.apply()

        with conditions(("BaseType", "Vial")), show():
            colors.vials.apply()

        with conditions(("BaseType", "Delirium Orb")), show():
            colors.delirium_orb.apply()

        with conditions(("BaseType", "Simulacrum Splinter")), show():
            icons.fragment_high.apply()
            colors.simulacrum_splinter.apply()

        with conditions(("BaseType", "Silver Coin")), show():
            colors.silver_coin.apply()

        with conditions(("BaseType", "Perandus Coin")), show():
            colors.perandus.apply()

        with conditions(("BaseType", "Harbinger")), show():
            colors.harbingers.apply()
        
        with conditions(("BaseType", "Orb of Horizons")), show():
            colors.horizons.apply()

        with conditions(("BaseType", "Stacked Deck")), show():
            colors.stacked_deck.apply()

        with conditions(("BaseType", "Blessed Orb")), show():
            colors.blessed.apply()

        with conditions(("BaseType", "Orb of Binding")), show():
            colors.binding.apply()

        # Splinters
        with conditions((
                "BaseType", "Esh", "Tul", "Chayula", "Xoph", "Netol"
                )), show():
            colors.breach_splinter.apply()
            icons.fragment_high.apply()

        with conditions(("BaseType", "Timeless")), show():
            colors.timeless_splinter.apply()
            icons.fragment_high.apply()
        

    with conditions(("Class", "Fragment")):
        # Other fragments
        with show():
            colors.frags.apply()

        with conditions((
                "BaseType", "Esh", "Tul", "Chayula", "Xoph", "Netol"
                )), show():
            colors.breachstones.apply()

        with conditions(("BaseType", "Sacrifice at")), show():
            colors.sacrifice.apply()

        with conditions(("BaseType", "Mortal ")), show():
            colors.mortal.apply()

        with conditions(("BaseType", "Hydra", "Phoenix", "Chimera", "Minotaur")), show():
            colors.shaper_frags.apply()

        with conditions(("BaseType", "Purification", "Constriction", "Eradication", "Enslavement")), show():
            colors.elder_frags.apply()

        with conditions(("BaseType", "Knowledge", "Shape", "Emptiness", "Terror")), show():
            colors.uber.apply()

        with conditions(("BaseType", "'s Key")), show():
            colors.pale.apply()

        with conditions(("BaseType", "Timeless")), show():
            colors.emblems.apply()

        with conditions(("BaseType", "Rusted")), show():
            colors.rusted_scarabs.apply()

        with conditions(("BaseType", "Polished")), show():
            colors.polished_scarabs.apply()

        with conditions(("BaseType", "Gilded")), show():
            colors.gilded_scarabs.apply()

        with conditions(("BaseType", "Winged")), show():
            colors.winged_scarabs.apply()

    with conditions(("Class", "Quest", "Labyrinth")), show():
        colors.quest.apply()

    with conditions(("Class", "Incubator")), show():
        colors.incubators.apply()

    with conditions(("Class", "Divination")):
        with show():
            colors.divination_unknown.apply()

        if tables.divination_bottom:
            with conditions(("BaseType", *tables.divination_bottom)), show():
                colors.divination_bottom.apply()
        
        if tables.divination_lower:
            with conditions(("BaseType", *tables.divination_lower)), show():
                colors.divination_lower.apply()

        if tables.divination_low:
            with conditions(("BaseType", *tables.divination_low)), show():
                colors.divination_low.apply()

        if tables.divination_mid:
            with conditions(("BaseType", *tables.divination_mid)), show():
                colors.divination_mid.apply()

        if tables.divination_high:
            with conditions(("BaseType", *tables.divination_high)), show():
                colors.divination_high.apply()

        if tables.divination_higher:
            with conditions(("BaseType", *tables.divination_higher)), show():
                colors.divination_higher.apply()

        if tables.divination_top:
            with conditions(("BaseType", *tables.divination_top)), show():
                colors.divination_top.apply()

    with conditions(("Class", "Gems")):
        with show():
            colors.gems.apply()

        with conditions(("Quality", ">", 0)), show():
            colors.quality_gems.apply()

        with conditions(("Corrupted", "True")), show():
            colors.corrupted.apply()

        with conditions(("BaseType", "Awakened")), show():
            colors.awakened_gems.apply()
            icons.other_top.apply()
            sounds.boom.apply()

        with conditions(("BaseType", *tables.drop_gems)), show():
            icons.other_higher.apply()
            colors.drop_gems.apply()
            sounds.pong.apply()


    with conditions(("Class", "Metamorph")), show():
        colors.metamorph.apply()

    with conditions(("Class", "Seed")), show():
        colors.seeds.apply()


    # Apply styles to items with rarity
    # =================================

    with conditions(("Class", *tables.rarity_classes)):
        # Apply default styles for rarity
        with conditions(("Rarity", "Normal")), show():
            colors.rarity_normal.apply()

        with conditions(("Rarity", "Magic")), show():
            colors.rarity_magic.apply()

        with conditions(("Rarity", "Rare")), show():
            colors.rarity_rare.apply()

        with conditions(("Rarity", "Unique")), show():
            colors.rarity_unique.apply()


        # Apply specific styles to each class / basetype
        for idx, rarity in enumerate(["Normal", "Magic", "Rare", "Unique"]):
            with conditions(("Rarity", rarity)):
                with conditions(("Class", "Abyss")), show():
                    colors.abyss[idx].apply()

                with conditions(("Class", "Jewel")):
                    with conditions(("BaseType", "Cluster")), show():
                        colors.cluster[idx].apply()

                    with show():
                        colors.jewels[idx].apply()

                with conditions(("Class", "Atlas")), show():
                    colors.watchstones[idx].apply()

                # TODO: Map tiers
                with conditions(("Class", "Maps")):
                    with conditions(("MapTier", "<=", 5)), show():
                        colors.maps_white[idx].apply()
                    with conditions(("MapTier", ">=", 6), ("MapTier", "<=", 10)), show():
                        colors.maps_yellow[idx].apply()
                    with conditions(("MapTier", ">=", 11)), show():
                        colors.maps_red[idx].apply()

                with conditions(("Class", "Amulets")):
                    if config.highlighted_amulets:
                        with conditions(("BaseType", *config.highlighted_amulets),
                                ("Rarity", "<", "Unique")), show():
                            colors.highlighted_amulets[idx].apply()
                    with show():
                        colors.amulets[idx].apply()

                with conditions(("Class", "Rings")):
                    if config.highlighted_rings:
                        with conditions(
                                ("BaseType", *config.highlighted_rings),
                                ("Rarity", "<", "Unique")), show():
                            colors.highlighted_rings[idx].apply()
                    with show():
                        colors.rings[idx].apply()

                with conditions(("Class", "Belts")):
                    if config.highlighted_belts:
                        with conditions(("BaseType", *config.highlighted_belts),
                                ("Rarity", "<", "Unique")), show():
                            colors.highlighted_belts[idx].apply()
                    with show():
                        colors.belts[idx].apply()

                with conditions(("Class", "Life Flasks")), show():
                    colors.life_flasks[idx].apply()

                with conditions(("Class", "Mana Flasks")), show():
                    colors.mana_flasks[idx].apply()

                with conditions(("Class", "Utility Flasks")), show():
                    colors.utility_flasks[idx].apply()

                with conditions(("Class", "Hybrid Flasks")), show():
                    colors.hybrid_flasks[idx].apply()

                with conditions(("Class", "Fishing")), show():
                    colors.fishing[idx].apply()

                with conditions(("Class", "Thrusting", "Bow")), show():
                    colors.dex_weapons[idx].apply()

                with conditions(("Class", "Quivers")), show():
                    colors.quivers[idx].apply()

                with conditions(("Class", "Wand")), show():
                    colors.int_weapons[idx].apply()

                with conditions(("Class", "Hand Axes", "Hand Swords")), show():
                    colors.strdex_weapons[idx].apply()

                with conditions(("Class", "Hand Maces")), show():
                    colors.str_weapons[idx].apply()

                with conditions(("Class", "Sceptre", "Warstaves", "Staves")), show():
                    colors.strint_weapons[idx].apply()

                with conditions(("Class", "Claw", "Dagger")), show():
                    colors.dexint_weapons[idx].apply()

                with conditions(("Class", *tables.armour_classes)):
                    with conditions(("BaseType", *tables.str_armour)), show():
                        colors.str_armour[idx].apply()

                    with conditions(("BaseType", *tables.dex_armour)), show():
                        colors.dex_armour[idx].apply()

                    with conditions(("BaseType", *tables.int_armour)), show():
                        colors.int_armour[idx].apply()
                        
                    with conditions(("BaseType", *tables.strdex_armour)), show():
                        colors.strdex_armour[idx].apply()

                    with conditions(("BaseType", *tables.strint_armour)), show():
                        colors.strint_armour[idx].apply()

                    with conditions(("BaseType", *tables.dexint_armour)), show():
                        colors.dexint_armour[idx].apply()
        
        # Unique tiers
        # ============

        # TODO: Highlight 6L uniques

        with conditions(("Rarity", "Unique")):
            with show():
                colors.unique_unknown.apply()

            if tables.unique_bottom:
                with conditions(("BaseType", *tables.unique_bottom)), show():
                    colors.unique_bottom.apply()
            
            if tables.unique_lower:
                with conditions(("BaseType", *tables.unique_lower)), show():
                    colors.unique_lower.apply()

            if tables.unique_low:
                with conditions(("BaseType", *tables.unique_low)), show():
                    colors.unique_low.apply()

            if tables.unique_mid:
                with conditions(("BaseType", *tables.unique_mid)), show():
                    colors.unique_mid.apply()

            if tables.unique_high:
                with conditions(("BaseType", *tables.unique_high)), show():
                    colors.unique_high.apply()

            if tables.unique_higher:
                with conditions(("BaseType", *tables.unique_higher)), show():
                    colors.unique_higher.apply()

            if tables.unique_top:
                with conditions(("BaseType", *tables.unique_top)), show():
                    colors.unique_top.apply()


        # Misc highlights / emphasis
        # ==========================

        # Chromatic Orb Recipe
        with conditions(("SocketGroup", "RGB")), show():
            colors.chrome_recipe.apply()

        # Jeweller's recipe
        with conditions(("Sockets", "6"), ("LinkedSockets", "<", 5)), show():
            colors.jewellers_recipe.apply()

        # Leveling socket types
        with conditions(
                ("Rarity", "<", "Unique"),
                ("AreaLevel", "<=", tables.act_10_max_level),
                ("SocketGroup", *config.other_socket_groups)), show():
            colors.ok_sockets.apply()

        with conditions(
                ("Rarity", "<", "Unique"),
                ("AreaLevel", "<=", tables.act_10_max_level),
                ("SocketGroup", *config.main_socket_groups)), show():
            colors.good_sockets.apply()

        # 5 & 6 links
        with conditions(("LinkedSockets", "5")), show():
            colors.valuable.apply()
            icons.other_mid.apply()

        with conditions(("LinkedSockets", "6")):
            with conditions(("Rarity", "<", "Unique")), show():
                colors.very_valuable.apply()
                icons.other_top.apply()
                sounds.bang_more.apply()

            with conditions( # Tabula
                    ("Rarity", "=", "Unique"),
                    ("SocketGroup", "WWWWWW")), show():
                colors.unique_high.apply()
                sounds.unique_more.apply()

            with conditions(
                    ("Rarity", "=", "Unique"),
                    ("SocketGroup", "6R", "6G", "6B")), show():
                colors.extremely_valuable.apply()
                sounds.unique_most.apply()


        with conditions(("Class", "Fishing")), show():
            icons.other_top.apply()
            colors.very_valuable.apply()
            sounds.unique_most.apply()

        # Influences
        # TODO: Different colors for top tier bases
        with conditions(("HasInfluence", "Shaper")), show():
            colors.shaper.apply()
            icons.other_higher.apply()
            sounds.vroom.apply()

        with conditions(("HasInfluence", "Elder")), show():
            colors.elder.apply()
            icons.other_higher.apply()
            sounds.vroom.apply()

        with conditions(("HasInfluence", "Warlord")), show():
            colors.warlord.apply()
            icons.other_higher.apply()
            sounds.vroom.apply()

        with conditions(("HasInfluence", "Hunter")), show():
            colors.hunter.apply()
            icons.other_higher.apply()
            sounds.vroom.apply()

        with conditions(("HasInfluence", "Redeemer")), show():
            colors.redeemer.apply()
            icons.other_higher.apply()
            sounds.vroom.apply()

        with conditions(("HasInfluence", "Crusader")), show():
            colors.crusader.apply()
            icons.other_higher.apply()
            sounds.vroom.apply()

        # Corruptions and Enchantments
        with conditions(
                    ("Corrupted", "True"),
                    ("AnyEnchantment", "False")), show():
            colors.corrupted.apply()

        with conditions(
                    ("Corrupted", "False"),
                    ("AnyEnchantment", "True")), show():
            colors.enchanted.apply()

        with conditions(
                    ("Corrupted", "True"),
                    ("AnyEnchantment", "True")), show():
            colors.corrupted_enchanted.apply()

        with conditions(("HasExplicitMod", "Veil")), show():
            colors.veiled.apply()
            sounds.pong.apply()

    with conditions(("Class", "Maps")):
        with conditions(("MapTier", "<=", 5)), show():
            icons.map_white.apply()
            sounds.maps.apply()

        with conditions(("MapTier", ">=", 6), ("MapTier", "<=", 10)), show():
            icons.map_yellow.apply()
            sounds.maps_more.apply()

        with conditions(("MapTier", ">=", 11)), show():
            icons.map_red.apply()
            sounds.maps_most.apply()
