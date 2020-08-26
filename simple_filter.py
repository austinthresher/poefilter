from poefilter import *

default = Style(
        background_color="0 0 0",
        text_color="255 0 255",
        font_size=45)

hidden = Style(
        background_color="20 20 20 128",
        text_color="#808080",
        font_size=32)

# (text, bg)
no_rarity_categories = {
        "quest":          Style(text_color="59 192 41",   background_color="0 88 45"),
        "magic_orbs":     Style(text_color="171 232 240", background_color="17 109 130"),
        "rare_orbs":      Style(text_color="255 246 182", background_color="169 104 98"),
        "other_orbs":     Style(text_color="255 216 206", background_color="149 104 71"),
        "quality":        Style(text_color="197 195 147", background_color="52 74 72"),
        "map_currency":   Style(text_color="204 212 191", background_color="62 93 121"),
        "prophecies":     Style(text_color="220 156 208", background_color="126 34 103"),
        "other_currency": Style(text_color="225 211 191", background_color="112 79 44"),
        "frags":          Style(text_color="158 209 239", background_color="145 33 47"),
        #"breachstones":   Style(text_color="208 247 255", background_color="92 109 91"),
        #"emblems":        Style(text_color="24 48 58",    background_color="216 229 220"),
        "shards":         Style(text_color="120 148 170", background_color="90 98 83"),
        "incubators":     Style(text_color="201 192 179", background_color="78 38 13"),
        "essences":       Style(text_color="246 190 196", background_color="17 112 114"),
        "divination":     Style(text_color="111 231 252", background_color="73 27 76"),
        "gems":           Style(text_color="98 201 202",  background_color="60 98 99"),
        "delve":          Style(text_color="249 202 61",  background_color="0 71 64"),
        #"scarabs":        Style(text_color="252 254 217", background_color="105 116 162"),
        "oils":           Style(text_color="229 253 231", background_color="232 113 145"),
        #"delirium":       Style(text_color="232 235 233", background_color="45 81 94"),
        "catalysts":      Style(text_color="255 250 165", background_color="154 170 252"),
        "metamorph":      Style(text_color="225 255 94",  background_color="59 89 65"),
        "vials":          Style(text_color="239 166 172", background_color="225 109 118"),
        "seeds":          Style(text_color="227 214 195", background_color="103 89 71")
    }

rarity_categories = [
        "jewels",
        "abyss",
        "cluster",
        "watchstones",
        "maps",
        "amulets",
        "rings",
        "belts",
        "flasks",
        "str_armour",
        "dex_armour",
        "int_armour",
        "strdex_armour",
        "strint_armour",
        "dexint_armour",
        "str_weapons",
        "dex_weapons",
        "int_weapons",
        "strdex_weapons",
        "strint_weapons",
        "dexint_weapons",
        "quivers",
        "fishing"
]



begin_show()
default.apply()
cont()



# Default colors for rarity

rarity_normal = Style(
        background_color="#202020",
        text_color="#c8c8c8")

rarity_magic = Style(
        background_color="#202020",
        text_color="#8889ff")

rarity_rare = Style(
        background_color="#202020",
        text_color="#feff77")

rarity_unique = Style(
        background_color="#202020",
        text_color="#b45000",
        play_effect_color="Brown",
        minimap_icon_size=1,
        minimap_icon_color="Brown",
        minimap_icon_shape="Diamond")


begin_show()
condition("Rarity Normal")
rarity_normal.apply()
cont()

begin_show()
condition("Rarity Magic")
rarity_magic.apply()
cont()

begin_show()
condition("Rarity Rare")
rarity_rare.apply()
cont()

begin_show()
condition("Rarity Unique")
rarity_unique.apply()
cont()

# Colors for items without rarity

begin_show()
condition("Class", "Quest", "Labyrinth")
no_rarity_categories["quest"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "of Alteration", "of Augmentation", "of Transmutation", "Regal Orb")
no_rarity_categories["magic_orbs"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Chaos Orb", "Orb of Annulment", "Divine Orb", "Exalted Orb")
no_rarity_categories["rare_orbs"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Orb")
no_rarity_categories["other_orbs"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Scrap", "Whetstone", "Prisim", "Bauble")
no_rarity_categories["quality"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Chisel", "Sextant")
no_rarity_categories["map_currency"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Prophecy")
no_rarity_categories["prophecies"].apply()
end()

begin_show()
condition("Class", "Fragment")
no_rarity_categories["frags"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Shard")
no_rarity_categories["shards"].apply()
end()

begin_show()
condition("Class", "Incubator")
no_rarity_categories["incubators"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Essence")
no_rarity_categories["essences"].apply()
end()

begin_show()
condition("Class", "Divination")
no_rarity_categories["divination"].apply()
end()

begin_show()
condition("Class", "Gems")
no_rarity_categories["gems"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Fossil", "Resonator")
no_rarity_categories["delve"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Oil")
no_rarity_categories["oils"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Catalyst")
no_rarity_categories["catalysts"].apply()
end()

begin_show()
condition("Class", "Metamorph")
no_rarity_categories["metamorph"].apply()
end()

begin_show()
condition("Class", "Currency")
condition("BaseType", "Vial")
no_rarity_categories["vials"].apply()
end()

begin_show()
condition("Class", "Seed")
no_rarity_categories["seeds"].apply()
end()

begin_show()
condition("Class", "Currency")
no_rarity_categories["other_currency"].apply()
end()
