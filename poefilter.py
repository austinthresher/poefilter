from colorsys import rgb_to_hsv, hsv_to_rgb
from contextlib import contextmanager
from inspect import currentframe

global in_block
in_block = 0

global condition_stack
condition_stack = []

global block_style
block_style = {}

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

def _rgb_float_to_dec(rgb):
    r_in, g_in, b_in = rgb
    r_out = int(r_in * 255)
    g_out = int(g_in * 255)
    b_out = int(b_in * 255)
    return "%d %d %d" % (r_out, g_out, b_out)

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
    global block_style
    assert not in_block
    in_block = True
    for cond in condition_stack:
        _indent()
        print(cond)
    block_style = {}

    

def _exit_block():
    global block_style
    global in_block
    assert in_block
    for k, v in block_style.items():
        _indent()
        print(k + " " + v)
    in_block = False


def _apply(vals, text):
    global block_style
    if vals is None:
        return False
    key = text.split()[0]
    if isinstance(vals, list):
        for v in vals:
            if v is None:
                return False
        block_style[key] = " ".join(str(x) for x in vals)
    else:
        block_style[key] = str(vals)
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
            play_effect_temp=None,
            warn_if_unused=True):
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

        # Print a warning if the style is never used
        if warn_if_unused:
            self.used = False
            self.lineno = currentframe().f_back.f_lineno
        else:
            self.used = True

    def apply(self):
        self.used = True
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

    def __del__(self):
        if not self.used:
            print("# unused style defined on line %d" % (self.lineno))



class ColorSeries:
    def __init__(self, fg_color, bg_color, tiers, min_sat=0.01, min_val=0.1):
        fg_col_str = _hex(fg_color)
        bg_col_str = _hex(bg_color)
        self.fg_color = [(int(x) / 255.0) for x in fg_col_str.split()]
        self.bg_color = [(int(x) / 255.0) for x in bg_col_str.split()]
        self.tiers = tiers
        self.min_sat = min_sat 
        self.min_val = min_val

    def fg(self, tier):
        assert tier >= 0 and tier < self.tiers
        h, s, v = rgb_to_hsv(*self.fg_color)
        # Desaturate lower tiers
        delta = tier / self.tiers 
        s = self.min_sat * (1.0 - delta) + s * delta
        # Lighten higher tiers
        missing_val = 1.0 - v
        v += delta * missing_val
        return _rgb_float_to_dec(hsv_to_rgb(h, s, v))        

    def bg(self, tier):
        assert tier >= 0 and tier < self.tiers
        h, s, v = rgb_to_hsv(*self.bg_color)
        # Darken lower tiers
        delta = tier / self.tiers 
        v = self.min_val * (1.0 - delta) + v * delta
        # Saturate lower tiers
        missing_sat = 1.0 - s
        s += (1.0 - delta) * missing_sat
        # Hue transitions to complementary color for higher tiers
        delta *= delta # Transition is nonlinear
        opposite = h + 0.5
        if opposite >= 1.0:
            opposite -= 1.0
        h = (1.0 - delta) * h + opposite * delta
        return _rgb_float_to_dec(hsv_to_rgb(h, s, v))        

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
def show():
    begin_show()
    try:
        yield None
    finally:
        end()

@contextmanager
def hide():
    begin_hide()
    try:
        yield None
    finally:
        end()

@contextmanager
def show_continue():
    begin_show()
    try:
        yield None
    finally:
        cont()

@contextmanager
def hide_continue():
    begin_hide()
    try:
        yield None
    finally:
        cont()

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
