from poefilter import *

# From StupidFatHobbit's Sovereign Filter
#1 - clashgong - levelling 4L's, 5L
#2 - stone drop - mid tier currency / div card
#3 - sour stone drop -  currency / div card
#4 - rising wind - variable value or multiple basetype unique, divine vessels
#5 - rising metal - high value unique
#6 - sharper rising metal? - top tier currency / div card / unique
#7 - ALIENS - unique jewel, unique map
#8 - dadadadada - red tier map
#9 - quieter #8 - all other maps
#10 - hard metal drop - high tier special items
#11 - soft metal drop - mid tier special items
#12 - crystal drop - quality gems
#13 - synth metal reverb? -  generic high value (rare atlas basetypes, high ilvl abyss jewels)
#14 - metal echo - levelling flasks
#15 - rapid metal echo - max tier maps
#16 - muffled drop - shaped/elder items

class Sounds:
    exalt = Style(alert_sound_id=1, alert_sound_volume=300)
    divine = Style(alert_sound_id=2, alert_sound_volume=300)
    good_unique = Style(alert_sound_id=3, alert_sound_volume=300)
    deep_gust = Style(alert_sound_id=4, alert_sound_volume=300)
    great_unique = Style(alert_sound_id=5, alert_sound_volume=300)
    very_interesting = Style(alert_sound_id=6, alert_sound_volume=300)
    long_wobble = Style(alert_sound_id=7, alert_sound_volume=300)
    medium_wobble = Style(alert_sound_id=8, alert_sound_volume=300)
    shorter_wobble = Style(alert_sound_id=9, alert_sound_volume=300)
    bang = Style(alert_sound_id=10, alert_sound_volume=300)
    chaos = Style(alert_sound_id=11, alert_sound_volume=300)
    gong = Style(alert_sound_id=12, alert_sound_volume=300)
    swish = Style(alert_sound_id=13, alert_sound_volume=300)
    echo_light = Style(alert_sound_id=14, alert_sound_volume=300)
    echo_heavy = Style(alert_sound_id=15, alert_sound_volume=300)
    boom = Style(alert_sound_id=16, alert_sound_volume=300)
