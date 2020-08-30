act_1_max_level = 13
act_2_max_level = 23
act_3_max_level = 33
act_4_max_level = 40
act_5_max_level = 45
act_6_max_level = 50
act_7_max_level = 55
act_8_max_level = 60
act_9_max_level = 64
act_10_max_level = 67

weapon_classes = [
        "Claws", "Rune Daggers", "Daggers", "Wands", "One Hand Swords",
        "Two Hand Swords", "Bows", "Warstaves", "Staves",
        "Sceptres", "One Hand Axes", "Two Hand Axes", "One Hand Maces",
        "Two Hand Maces", "Quivers"] # Quivers is debatable

trinket_classes = [
        "Amulets", "Rings", "Belts"]

armour_classes = [
        "Helmets", "Gloves", "Boots", "Body Armours", "Shields"]

equipment_classes = [
        *weapon_classes,
        *armour_classes,
        *trinket_classes]

# item classes that exist in more than one rarity
rarity_classes = [
        *equipment_classes,
        "Maps", "Flasks", "Fishing", "Jewel"] # Not sure where Watchstones go

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

influences = ["Shaper", "Elder", "Warlord", "Crusader", "Hunter", "Redeemer"]

drop_gems = ["Portal", "Enlighten", "Enhance", "Empower"]

# Divination Card Tiers
# =====================

divination_top = [
        "House of Mirrors", "The Demon", "The Cheater", "The Immortal",
        "The Doctor", "The Fiend", "The Greatest Intentions",
        "Beauty Through Death", "Seven Years Bad Luck", "Nook's Crown",
        "Gift of Asenath", "The Damned", "The Hive of Knowledge",
        "Alluring Bounty", "Succor of the Sinless", "The Iron Bard",
        "The Samurai's Eye", "A Familiar Call", "Hunter's Reward",
        "Abandoned Wealth", "Pride of the First Ones", "Immortal Resolve",
        "The Nurse", "Etched in Blood", "The Sustenance", "The Fishmonger",
        "The Progeny of Lunaris", "The Spark and the Flame",
        "The White Knight", "The Long Con", "Wealth and Power"
    ]

divination_higher = [
        "The Mayor", "The Price of Loyalty", "The Eye of Terror", "The Queen",
        "The Life Thief", "Void of the Elements", "Squandered Prosperity",
        "The Artist", "The Strategist", "The Saint's Treasure", "The Bargain",
        "Azyran's Reward", "Council of Cats", "The Tumbleweed",
        "The Dragon's Heart", "Mawr Blaidd", "The Escape", "The Sephirot",
        "The Old Man", "Chaotic Disposition", "The Soul", "The Undaunted",
        "The Celestial Stone", "A Note in the Wind", "The World Eater",
        "The Deep Ones", "The Awakened", "Dark Dreams", "Prometheus' Armoury",
        "Peaceful Moments", "The Hoarder", "The Eldritch Decay"
    ]

divination_high = [
        "Divine Justice", "The Undisputed", "Time-Lost Relic", "The Demoness",
        "The Trial", "Rebirth", "Remembrance", "The Valkyrie", "The Avenger",
        "Deathly Designs", "The Dreamer", "The Last One Standing",
        "The Professor", "The Celestial Justicar", "Blessing of God",
        "The Cartographer", "Arrogance of the Vaal", "Burning Blood",
        "The Enlightened", "The Wolf", "The Landing", "Merciless Armament",
        "Perfection", "The Sacrifice", "The Warlord", "The Hale Heart",
        "The Lord in Black", "The Jester", "The Spoiled Prince",
        "The Thaumaturgist", "The Wolven King's Bite", "Left to Fate",
        "Boon of the First Ones", "The Wolf's Legacy", "Baited Expectations",
        "The Ethereal", "Birth of the Three", "The Craving"
    ]

divination_mid = [
        "The Fletcher", "The Endless Darkness", "The Mad King", "The Chosen",
        "Underground Forest", "The Easy Stroll", "The Primordial",
        "The Insatiable", "The King's Heart", "The Throne",
        "The One With All", "The Dark Mage", "Echoes of Love",
        "Heterochromia", "Blind Venture", "Rain Tempter", "The Betrayal",
        "The Tyrant", "Treasure Hunter", "The Porcupine", "The Admirer",
        "The Golden Era", "The Siren", "The Void", "The Risk", "The Polymath",
        "Pride Before the Fall", "The Cursed King", "The Dapper Prodigy",
        "The Offering", "The Wretched", "The Master", "The Darkest Dream",
        "The Lord of Celebration", "Akil's Prophecy", "Cameria's Cut",
        "The Tinkerer's Table", "The Dreamland", "Humility",
        "The Road to Power", "Lost Worlds", "The Brittle Emperor",
        "The Wolverine", "The Sigil", "The Price of Protection", "Friendship",
        "The Archmage's Right Hand", "The Stormcaller", "Audacity",
        "Shard of Fate", "The Battle Born", "The Conduit", "The Hunger",
        "The Oath", "The Scavenger", "Lingering Remnants", "The Standoff",
        "The Forsaken", "The Breach", "The Wilted Rose", "Vanity",
        "Buried Treasure", "The Lion", "The Gladiator", "The Penitent",
        "The Body", "A Dab of Ink", "The Valley of Steel Boxes",
        "The Twilight Moon", "The Mercenary", "The Inoculated",
        "Lysah's Respite", "The Cataclysm", "The Garish Power",
        "Glimmer of Hope", "The Skeleton", "The Arena Champion", "Hope",
        "The Wind", "Vile Power", "The Harvester", "The Vast"
    ]

divination_low = [
        "Boon of Justice", "Bowyer's Dream", "Coveted Possession",
        "Demigod's Wager", "Emperor of Purity", "Emperor's Luck",
        "Harmony of Souls", "Imperial Legacy", "Last Hope", "Loyalty",
        "Lucky Connections", "Lucky Deck", "Monochrome",
        "More is Never Enough", "No Traces", "Sambodhi's Vow", "The Cacophony",
        "The Catalyst", "The Chains that Bind", "The Deal", "The Fool",
        "The Gemcutter", "The Heroic Shot", "The Innocent", "The Inventor",
        "The Journey", "The Master Artisan", "The Seeker", "The Side Quest",
        "The Survivalist", "The Union", "The Wrath", "Three Faces in the Dark",
        "The Jeweller's Boon", "Three Voices", "Vinia's Token"
    ]

divination_lower = [
        "The Calling", "Dying Anguish", "A Mother's Parting Gift",
        "Anarchy's Price", "Assassin's Favour", "Boundless Realms", "Death",
        "Dialla's Subjugation", "Doedre's Madness", "Earth Drinker",
        "Gemcutter's Promise", "Gift of the Gemling Queen", "Grave Knowledge",
        "Hubris", "Hunter's Resolve", "Jack in the Box",
        "Lantador's Lost Love", "Light and Truth", "Prosperity", "Rats",
        "Scholar of the Seas", "The Aesthete",
        "The Doppelganger", "The Dragon", "The Drunken Aristocrat",
        "The Encroaching Darkness", "The Endurance", "The Explorer",
        "The Feast", "The Formless Sea", "The Fox", "The Gentleman",
        "The Hermit", "The Incantation",
        "The Metalsmith's Gift", "The Pack Leader", "The Pact", "The Poet",
        "The Rabid Rhoa", "The Scarred Meadow", "The Summoner", "The Sun",
        "The Surveyor", "The Tower", "The Traitor", "The Twins",
        "The Visionary", "The Watcher", "The Web", "The Wolf's Shadow",
        "Tranquillity", "Turn the Other Cheek", "Volatile Power", "Mitts",
        "Call to the First Ones", "The Coming Storm", "Might is Right",
        "Atziri's Arsenal", "The Opulent", "The Blazing Fire",
        "The Ruthless Ceinture", "The Eye of the Dragon", "The Realm",
        "The Obscured", "The Deceiver", "Forbidden Power",
         "The Army of Blood", "The Beast",
        "The Sword King's Salute", "The Fathomless Depths",
        "The Rite of Elements", "The Witch", "Alone in the Darkness",
        "Dark Temptation", "The Messenger", "Thirst for Knowledge",
        "The Mountain", "The Bones", "Struck by Lightning", "The Lich",
        "The Lunaris Priestess", "The Surgeon", "Thunderous Skies",
        "The Lover", "The Warden", "Cartographer's Delight",
        "Destined to Crumble", "Her Mask", "Rain of Chaos", "The Flora's Gift",
        "The Gambler", "The Puzzle", "The Scholar"
        ]

divination_bottom = ["The Carrion Crow", "The King's Blade"]

# Prophecy Tiers
# ==============

prophecy_top = [
        "Trash to Treasure", "The Queen's Sacrifice", "The Forgotten Garrison",
        "Fated Connections", "The Lady in Black", "From Death Springs Life",
        "Darktongue's Shriek", "The Petrified", "A Dishonourable Death"
    ]

prophecy_higher = [
        "Storm on the Horizon", "The Bowstring's Music", "Song of the Sekhema",
        "Living Fires", "The King's Path", "Blind Faith", "Monstrous Treasure",
        "Fire and Brimstone", "Twice Enchanted",
        "The Great Leader of the North", "The Prison Key"
    ]

prophecy_high = [
        "Cleanser of Sins", "The Jeweller's Touch", "A Whispered Prayer",
        "The Mentor", "The Ward's Ward", "Roth's Legacy", "The Prison Guard",
        "Echoes of Witchcraft", "The Feral Lord V", "The Plaguemaw V",
        "The Unbreathing Queen V", "Unbearable Whispers V"
    ]

prophecy_mid = [
        "A Master Seeks Help", "Anarchy's End III", "Anarchy's End IV",
        "Beyond Sight III", "Beyond Sight IV", "Bountiful Traps",
        "Crushing Squall", "Deadly Rivalry IV", "Deadly Rivalry V",
        "Deadly Twins", "Fire from the Sky", "Hidden Reinforcements",
        "Hidden Vaal Pathways", "Ice from Above", "Lightning Falls",
        "Mysterious Invaders", "Overflowing Riches", "Plague of Frogs",
        "Plague of Rats", "Possessed Foe", "Reforged Bonds",
        "The Beautiful Guide", "The Cursed Choir", "The Dreamer's Dream",
        "The Fortune Teller's Collection", "The Four Feral Exiles",
        "The Hungering Swarm", "The Trembling Earth", "The Twins",
        "The Undead Storm", "The Warmongers III", "The Warmongers IV",
        "Vaal Winds", "Waiting in Ambush"
    ]

prophecy_low = [
        "A Forest of False Idols", "Agony at Dusk", "Battle Hardened",
        "Black Devotion", "Blinding Light", "Burning Dread",
        "Cold Blooded Fury", "Cold Greed", "Crimson Hues", "Dance of Steel",
        "Dark Instincts", "End of the Light", "Faith Exhumed", "From The Void",
        "Greed's Folly", "Mouth of Horrors", "Nature's Resilience",
        "Pleasure and Pain", "Power Magnified", "Sun's Punishment",
        "The Beginning and the End", "The Bishop's Legacy",
        "The Bloody Flowers Redux", "The Dreaded Rhoa",
        "The Fall of an Empire", "The Flow of Energy",
        "The King and the Brambles", "The Malevolent Witch",
        "The Nightmare Awakens", "The Snuffed Flame", "The Storm Spire",
        "Trapped in the Tower", "Winter's Mournful Melodies"
    ]

prophecy_lower = [
        "A Prodigious Hand", "The Silverwood", "The Sword King's Passion",
        "The Hollow Pledge", "The Misunderstood Queen",
        "Custodians of Silence", "The Great Mind of the North", "Fire and Ice",
        "Undead Uprising", "The Last Watch", "Flesh of the Beast",
        "The Brutal Enforcer", "Visions of the Drowned", "Last of the Wildmen",
        "A Rift in Time", "Wind and Thunder", "A Call into the Void",
        "Touched by the Wind", "Against the Tide", "Resistant to Change",
        "A Vision of Ice and Fire", "The Apex Predator",
        "Fire, Wood and Stone", "Beyond Sight II", "The Karui Rebellion",
        "The Dream Trial", "The Soulless Beast", "Anarchy's End I",
        "Notched Flesh", "The Watcher's Watcher", "Blood in the Eyes",
        "Deadly Rivalry I", "Day of Sacrifice III", "The Mysterious Gift",
        "Lost in the Pages", "The Vanguard", "Weeping Death", "The Nest",
        "Nemesis of Greed", "The Lost Undying", "The Flayed Man",
        "The Walking Mountain", "Day of Sacrifice I",
        "In the Grasp of Corruption", "Kalandra's Craft", "Baptism by Death",
        "Fear's Wide Reach", "Storm on the Reef", "The Eagle's Cry"
    ]

prophecy_bottom = [
        "Heart of the Fire", "Strong as a Bull", "Day of Sacrifice IV",
        "Abnormal Effulgence", "Blood of the Betrayed", "Dying Cry",
        "The Ambitious Bandit I", "Thaumaturgical History IV",
        "A Firm Foothold", "A Regal Death", "An Unseen Peril",
        "Anarchy's End II", "Ancient Doom", "Beyond Sight I",
        "Day of Sacrifice II", "Deadly Rivalry II", "Deadly Rivalry III",
        "Ending the Torment", "Erased from Memory", "Erasmus' Gift",
        "Forceful Exorcism", "Gilded Within", "Golden Touch", "Heavy Blows",
        "Hunter's Lesson", "Lasting Impressions", "Pools of Wealth", "Rebirth",
        "Risen Blood", "Severed Limbs", "Smothering Tendrils",
        "Soil, Worms and Blood", "Thaumaturgical History I",
        "Thaumaturgical History II", "Thaumaturgical History III",
        "The Alchemist", "The Ambitious Bandit II", "The Ambitious Bandit III",
        "The Brothers of Necromancy", "The Corrupt", "The Feral Lord II",
        "The Feral Lord IV", "The God of Misfortune", "The Hardened Armour",
        "The Lost Maps", "The Plaguemaw I", "The Plaguemaw II",
        "The Plaguemaw III", "The Plaguemaw IV", "The Queen's Vaults",
        "The Scout", "The Servant's Heart", "The Sharpened Blade",
        "The Singular Spirit", "The Sinner's Stone", "The Stockkeeper",
        "The Unbreathing Queen I", "The Unbreathing Queen II",
        "The Unbreathing Queen III", "The Unbreathing Queen IV",
        "The Undead Brutes", "The Warmongers I", "The Warmongers II",
        "The Wealthy Exile", "Unbearable Whispers I", "Unbearable Whispers II",
        "Unbearable Whispers III", "Unbearable Whispers IV",
        "Vital Transformation", "The Invader", "The Feral Lord III",
        "Graceful Flames", "The Feral Lord I", "A Valuable Combination",
        "Defiled in the Sceptre", "Fallow At Last", "Holding the Bridge",
        "Path of Betrayal", "The Child of Lunaris", "The Forgotten Soldiers",
        "Unnatural Energy", "Vaal Invasion"
    ]

# Unique Tiers
# ============

# TODO
unique_top = [

    ]

unique_higher = [

    ]

unique_high = [

    ]

unique_mid = [

    ]

unique_low = [

    ]

unique_lower = [

    ]

unique_bottom = [

    ]

# Essence Tiers
# ============

# TODO
essence_top = [

    ]

essence_higher = [

    ]

essence_high = [

    ]

essence_mid = [

    ]

essence_low = [

    ]

essence_lower = [

    ]

essence_bottom = [

    ]


