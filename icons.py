from poefilter import *

# Top 3 tiers have map icons + beams
# Mid tier has temp beam, no icons

class Icons:

    # Currency icons
    # ==============

    currency_color = "Green"
    currency_shape = "Star"

    currency_top = Style(
            play_effect_color=currency_color,
            minimap_icon_color=currency_color,
            minimap_icon_shape=currency_shape,
            minimap_icon_size=0)
    currency_higher = Style(
            play_effect_color=currency_color,
            minimap_icon_color=currency_color,
            minimap_icon_shape=currency_shape,
            minimap_icon_size=1)
    currency_high = Style(
            play_effect_color=currency_color,
            minimap_icon_color=currency_color,
            minimap_icon_shape=currency_shape,
            minimap_icon_size=2)
    currency_mid = Style(
            play_effect_color=currency_color,
            play_effect_temp=True)

    # Unique icons
    # ============

    unique_color = "Orange"
    unique_shape = "Cross"

    unique_top = Style(
            play_effect_color=unique_color,
            minimap_icon_color=unique_color,
            minimap_icon_shape=unique_shape,
            minimap_icon_size=0)
    unique_higher = Style(
            play_effect_color=unique_color,
            minimap_icon_color=unique_color,
            minimap_icon_shape=unique_shape,
            minimap_icon_size=1)
    unique_high = Style(
            play_effect_color=unique_color,
            minimap_icon_color=unique_color,
            minimap_icon_shape=unique_shape,
            minimap_icon_size=2)
    unique_mid = Style(
            play_effect_color=unique_color,
            play_effect_temp=True)

    # Divination icons
    # ================

    divination_color = "Cyan"
    divination_shape = "Square"

    divination_top = Style(
            play_effect_color=divination_color,
            minimap_icon_color=divination_color,
            minimap_icon_shape=divination_shape,
            minimap_icon_size=0)
    divination_higher = Style(
            play_effect_color=divination_color,
            minimap_icon_color=divination_color,
            minimap_icon_shape=divination_shape,
            minimap_icon_size=1)
    divination_high = Style(
            play_effect_color=divination_color,
            minimap_icon_color=divination_color,
            minimap_icon_shape=divination_shape,
            minimap_icon_size=2)
    divination_mid = Style(
            play_effect_color=divination_color,
            play_effect_temp=True)

    # Prophecy icons
    # ==============

    prophecy_color = "Purple"
    prophecy_shape = "Triangle"

    prophecy_top = Style(
            play_effect_color=prophecy_color,
            minimap_icon_color=prophecy_color,
            minimap_icon_shape=prophecy_shape,
            minimap_icon_size=0)
    prophecy_higher = Style(
            play_effect_color=prophecy_color,
            minimap_icon_color=prophecy_color,
            minimap_icon_shape=prophecy_shape,
            minimap_icon_size=1)
    prophecy_high = Style(
            play_effect_color=prophecy_color,
            minimap_icon_color=prophecy_color,
            minimap_icon_shape=prophecy_shape,
            minimap_icon_size=2)
    prophecy_mid = Style(
            play_effect_color=prophecy_color,
            play_effect_temp=True)

    # Map icons
    # =========

    map_shape = "Hexagon"

    map_red = Style(
            play_effect_color="Red",
            minimap_icon_color="Red",
            minimap_icon_shape=map_shape,
            minimap_icon_size=0)
    map_yellow = Style(
            play_effect_color="Yellow",
            minimap_icon_color="Yellow",
            minimap_icon_shape=map_shape,
            minimap_icon_size=1)
    map_white = Style(
            play_effect_color="White",
            minimap_icon_color="White",
            minimap_icon_shape=map_shape,
            minimap_icon_size=2)

    # Fragment icons
    # ==============

    fragment_color = "Brown"
    fragment_shape = "Diamond"

    fragment_top = Style(
            play_effect_color=fragment_color,
            minimap_icon_color=fragment_color,
            minimap_icon_shape=fragment_shape,
            minimap_icon_size=0)
    fragment_higher = Style(
            play_effect_color=fragment_color,
            minimap_icon_color=fragment_color,
            minimap_icon_shape=fragment_shape,
            minimap_icon_size=1)
    fragment_high = Style(
            play_effect_color=fragment_color,
            minimap_icon_color=fragment_color,
            minimap_icon_shape=fragment_shape,
            minimap_icon_size=2)
    fragment_mid = Style(
            play_effect_color=fragment_color,
            play_effect_temp=True)

    # League-specific icons
    # =====================

    league_color = "Grey"
    league_shape = "Raindrop"

    league_top = Style(
            play_effect_color=league_color,
            minimap_icon_color=league_color,
            minimap_icon_shape=league_shape,
            minimap_icon_size=0)
    league_higher = Style(
            play_effect_color=league_color,
            minimap_icon_color=league_color,
            minimap_icon_shape=league_shape,
            minimap_icon_size=1)
    league_high = Style(
            play_effect_color=league_color,
            minimap_icon_color=league_color,
            minimap_icon_shape=league_shape,
            minimap_icon_size=2)
    league_mid = Style(
            play_effect_color=league_color,
            play_effect_temp=True)

    # Other icons
    # ===========

    other_color = "Pink"
    other_shape = "Circle"

    other_top = Style(
            play_effect_color=other_color,
            minimap_icon_color=other_color,
            minimap_icon_shape=other_shape,
            minimap_icon_size=0)
    other_higher = Style(
            play_effect_color=other_color,
            minimap_icon_color=other_color,
            minimap_icon_shape=other_shape,
            minimap_icon_size=1)
    other_high = Style(
            play_effect_color=other_color,
            minimap_icon_color=other_color,
            minimap_icon_shape=other_shape,
            minimap_icon_size=2)
    other_mid = Style(
            play_effect_color=other_color,
            play_effect_temp=True)

