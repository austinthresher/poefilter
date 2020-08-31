from poefilter import *

class Sounds:
    currency_most = Style(alert_sound_id=1, alert_sound_volume=300)
    currency_more = Style(alert_sound_id=10, alert_sound_volume=250)
    currency = Style(alert_sound_id=11, alert_sound_volume=200)

    pong = Style(alert_sound_id=12, alert_sound_volume=200)

    vroom = Style(alert_sound_id=6, alert_sound_volume=200)

    boom = Style(alert_sound_id=16, alert_sound_volume=200)

    heavy_more = Style(alert_sound_id=3, alert_sound_volume=300)
    heavy = Style(alert_sound_id=2, alert_sound_volume=250)

    unique_most = Style(alert_sound_id=5, alert_sound_volume=300)
    unique_more = Style(alert_sound_id=4, alert_sound_volume=250)
    unique = Style(alert_sound_id=13, alert_sound_volume=200)

    maps_most = Style(alert_sound_id=7, alert_sound_volume=200, disable_drop_sound=True)
    maps_more = Style(alert_sound_id=8, alert_sound_volume=200, disable_drop_sound=True)
    maps = Style(alert_sound_id=9, alert_sound_volume=200, disable_drop_sound=True)

    bang_more = Style(alert_sound_id=10, alert_sound_volume=300)
    bang = Style(alert_sound_id=11, alert_sound_volume=200)

    stutter_more = Style(alert_sound_id=15, alert_sound_volume=300)
    stutter = Style(alert_sound_id=14, alert_sound_volume=200)
