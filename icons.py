from poefilter import *

# TODO: Come up with a consistent color / shape / beam system so that drop
# value is communicated effectively

class Icons:

    # This icon should be filtered out anywhere it is set, so seeing it ingame
    # means something went wrong in the filter
    buggy = Style(
            play_effect_color="Red",
            minimap_icon_size=0,
            minimap_icon_color="Pink",
            minimap_icon_shape="Square")

    extremely_valuable = Style(
            play_effect_color="Red",
            minimap_icon_size=0,
            minimap_icon_color="Red",
            minimap_icon_shape="Star")
    very_valuable = Style(
            play_effect_color="Red",
            minimap_icon_size=1,
            minimap_icon_color="Red",
            minimap_icon_shape="Star")
    valuable = Style(
            play_effect_color="Red",
            play_effect_temp=True,
            minimap_icon_size=2,
            minimap_icon_color="Red",
            minimap_icon_shape="Star")
    chaos = Style(
            play_effect_color="Red",
            minimap_icon_size=2,
            minimap_icon_color="Red",
            minimap_icon_shape="Cross")
    green_circle_beam = Style(
            play_effect_color="Green",
            play_effect_temp=True,
            minimap_icon_size=2,
            minimap_icon_color="Green",
            minimap_icon_shape="Circle")
    blue_circle_beam = Style(
            play_effect_color="Blue",
            minimap_icon_size=2,
            minimap_icon_color="Blue",
            minimap_icon_shape="Circle")
    blue_circle_temp = Style(
            play_effect_color="Blue",
            play_effect_temp=True,
            minimap_icon_size=2,
            minimap_icon_color="Blue",
            minimap_icon_shape="Circle")
    blue_circle = Style(
            minimap_icon_size=2,
            minimap_icon_color="Blue",
            minimap_icon_shape="Circle")
    yellow_circle_beam = Style(
            play_effect_color="Yellow",
            minimap_icon_size=2,
            minimap_icon_color="Yellow",
            minimap_icon_shape="Circle")
    yellow_circle_temp = Style(
            play_effect_color="Yellow",
            play_effect_temp=True,
            minimap_icon_size=2,
            minimap_icon_color="Yellow",
            minimap_icon_shape="Circle")
    yellow_circle = Style(
            minimap_icon_size=2,
            minimap_icon_color="Yellow",
            minimap_icon_shape="Circle")
    cyan_diamond_beam = Style(
            play_effect_color="Cyan",
            minimap_icon_size=2,
            minimap_icon_color="Cyan",
            minimap_icon_shape="Diamond")
    splinter = Style(
            minimap_icon_size=2,
            minimap_icon_color="White",
            minimap_icon_shape="Kite")

    divination_card = Style(
            play_effect_color="Grey",
            minimap_icon_size=2,
            minimap_icon_color="Grey",
            minimap_icon_shape="Square")

    divination_card_temp = Style(
            play_effect_color="Grey",
            play_effect_temp=True,
            minimap_icon_size=2,
            minimap_icon_color="Grey",
            minimap_icon_shape="Square")

    divination_card_temp_no_minimap = Style(
            play_effect_color="Grey",
            play_effect_temp=True)

    prophecy = Style(
            play_effect_color="Purple",
            minimap_icon_size=2,
            minimap_icon_color="Purple",
            minimap_icon_shape="Triangle")

    prophecy_temp = Style(
            play_effect_color="Purple",
            play_effect_temp=True,
            minimap_icon_size=2,
            minimap_icon_color="Purple",
            minimap_icon_shape="Triangle")

    prophecy_temp_no_minimap = Style(
            play_effect_color="Purple",
            play_effect_temp=True)

    unique = Style(
            play_effect_color="Orange",
            minimap_icon_size=1,
            minimap_icon_color="Orange",
            minimap_icon_shape="Diamond")

    unique_temp = Style(
            play_effect_color="Orange",
            play_effect_temp=True,
            minimap_icon_size=2,
            minimap_icon_color="Orange",
            minimap_icon_shape="Diamond")

    unique_temp_no_minimap = Style(
            play_effect_color="Orange",
            play_effect_temp=True)


