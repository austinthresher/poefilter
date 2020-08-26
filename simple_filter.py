from poefilter import *

default = Style(
        background_color="#000000",
        text_color="#ff0000",
        font_size=45)

hidden = Style(
        background_color="20 20 20 128",
        text_color="#808080")

currency_0 = Style(
        background_color="#433633",
        text_color="#b7b7b7")

currency_1 = Style(
        background_color="#464e5b",
        text_color="#a7b7b7")

currency_2 = Style(
        background_color="#304c78",
        text_color="#cccccc")

currency_3 = Style(
        background_color="#403195",
        text_color="#d9d9d0")

currency_4 = Style(
        background_color="#990043",
        text_color="#efefef")

currency_5 = Style(
        background_color="#ff0000",
        text_color="#ffffff")

currency_6 = Style(
        background_color="#f4cccc",
        text_color="#5b0f00")

currency_7 = Style(
        background_color="#ffe7e7",
        text_color="#990000")

currency_8 = Style(
        background_color="#ffffff",
        text_color="#ff0000")

begin_show()
default.apply()
cont()

early_hide = []
early_show = [
        ("Scroll of Wisdom", currency_0),
        ("Portal Scroll", currency_1),
        ("Orb of Transmutation", currency_2),
        ("Orb of Alteration", currency_3),
        ("Orb of Chance", currency_4),
        ("Orb of Alchemy", currency_5),
        ("Chaos Orb", currency_6)
    ]

midgame_hide = [
        ("Scroll of Wisdom", hidden)
    ]
midgame_show = [
        ("Portal Scroll", currency_0),
        ("Orb of Transmutation", currency_1),
        ("Orb of Alteration", currency_2),
        ("Orb of Chance", currency_3),
        ("Orb of Alchemy", currency_4),
        ("Chaos Orb", currency_5),
        ("Orb of Annulment", currency_6),
        ("Divine Orb", currency_7),
        ("Exalted Orb", currency_8)
    ]

endgame_hide = [
        ("Scroll of Wisdom", hidden),
        ("Portal Scroll", hidden)
    ]
endgame_show = midgame_show[1:]

area_levels = [
        (early_hide, early_show, ["AreaLevel < 24"]),
        (midgame_hide, midgame_show, ["AreaLevel < 68"]),
        (endgame_hide, endgame_show, ["AreaLevel >= 69"])
    ]

with conditions(cond("Class Currency")):
    for hide, show, rules in area_levels:
        with conditions(cond(*rules)):
            for bt, style in hide:
                begin_hide()
                condition("BaseType", bt)
                style.apply()
                end()
            for bt, style in show:
                begin_show()
                condition("BaseType", bt)
                style.apply()
                end()

    # Any currency we missed
    begin_show()
    currency_4.apply()
    end()
