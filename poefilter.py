from contextlib import contextmanager

global in_block
in_block = 0

global condition_stack
condition_stack = []

# Private utility functions
# =========================

def _hex(hex_string):
    """
    If the string starts with #, convert it from hex to a PoE color string.
    Otherwise, just let the color string pass through.
    """
    if hex_string is None:
        return None
    if hex_string.startswith("#"):
        # Taken from https://stackoverflow.com/a/29643643
        h = hex_string.lstrip("#")
        t = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        return " ".join(str(x) for x in t)
    return hex_string

def _esc(text):
    t = str(text)
    if not " " in t:
        return t
    return '"' + t + '"'

def _indent():
    global in_block
    if in_block:
        print("    ", end='')


def _enter_block():
    global in_block
    global condition_stack
    assert not in_block
    in_block = True
    for cond in condition_stack:
        _indent()
        print(cond)
    

def _exit_block():
    global in_block
    assert in_block
    in_block = False


def _apply(vals, text):
    if vals is None:
        return False
    if isinstance(vals, list):
        for v in vals:
            if v is None:
                return False
        _indent();
        print(text + " ", end = '')
        print(" ".join(str(x) for x in vals))
    else:
        _indent();
        print(text + " " + str(vals))
    return True

# Public interface
# ================

class Style:
    def __init__(self,
            border_color=None,
            text_color=None,
            background_color=None,
            font_size=None,
            alert_sound_id=None,
            alert_sound_volume=None,
            alert_sound_positional=None,
            disable_drop_sound=None,
            custom_alert_sound=None,
            minimap_icon_size=None,
            minimap_icon_color=None,
            minimap_icon_shape=None,
            play_effect_color=None,
            play_effect_temp=None):
        self.border_color = _hex(border_color)
        self.text_color = _hex(text_color)
        self.background_color = _hex(background_color)
        self.font_size = font_size
        self.alert_sound_id = alert_sound_id
        self.alert_sound_volume = alert_sound_volume
        self.alert_sound_positional = alert_sound_positional
        self.disable_drop_sound = disable_drop_sound
        self.custom_alert_sound = custom_alert_sound
        self.minimap_icon_size = minimap_icon_size
        self.minimap_icon_color = minimap_icon_color
        self.minimap_icon_shape = minimap_icon_shape
        self.play_effect_color = play_effect_color
        self.play_effect_temp = play_effect_temp

    def apply(self):
        _apply(self.border_color, "SetBorderColor")
        _apply(self.text_color, "SetTextColor")
        _apply(self.background_color, "SetBackgroundColor")
        _apply(self.font_size, "SetFontSize")
        if self.alert_sound_positional is not None and self.alert_sound_positional:
            if not _apply([self.alert_sound_id, self.alert_sound_volume], "PlayAlertSoundPositional"):
                _apply(self.alert_sound_id, "PlayAlertSoundPositional")
        else:
            if not _apply([self.alert_sound_id, self.alert_sound_volume], "PlayAlertSound"):
                _apply(self.alert_sound_id, "PlayAlertSound")
        if self.disable_drop_sound is not None and self.disable_drop_sound:
            _indent()
            print("DisableDropSound")
        _apply(self.custom_alert_sound, "CustomAlertSound")
        if not _apply([self.minimap_icon_size, self.minimap_icon_color, self.minimap_icon_shape], "MinimapIcon"):
            if self.minimap_icon_size == "-1":
                _apply("-1", "MinimapIcon")
        if self.play_effect_temp is not None and self.play_effect_temp:
            _apply([self.play_effect_color, "Temp"], "PlayEffect")
        else:
            _apply(self.play_effect_color, "PlayEffect")


def begin_show():
    print("Show")
    _enter_block()

def begin_hide():
    print("Hide")
    _enter_block()

def end():
    _exit_block()
    print("")

def cont():
    _indent()
    print("Continue")
    end()

#def rule(text, arg_list=None):
#    if arg_list is None:
#        return text
#    elif isinstance(arg_list, list):
#        for a in arg_list:
#            text += " " + _esc(a)
#        return text + "\n"
#    else:
#        return text + " " + _esc(arg_list)

def cond(*args):
    assert len(args) > 0
    result = str(args[0])
    if len(args) > 1:
        for a in args[1:]:
            result += " " + _esc(a)
    return result

def condition(*args):
    """Add a condition to the active block"""
    global in_block
    assert in_block
    _indent()
    print(cond(*args))

@contextmanager
def conditions(*args):
    global condition_stack
    global in_block
    assert not in_block
    num_to_pop = len(args)
    condition_stack.extend(args)
    try:
        yield None
    finally:
        assert not in_block
        while num_to_pop:
            condition_stack.pop()
            num_to_pop -= 1
