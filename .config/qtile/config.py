# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequi
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Imports
import os
import subprocess

from libqtile import bar, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

# Local imports
import mycolors

# Predefined variables
mod = "mod4"  # super key
terminal = "alacritty"
default_browser = "flatpak run io.gitlab.librewolf-community"
default_media_player = "flatpak run org.videolan.VLC"
screenshot_program = "flameshot"
colors = mycolors.init_colors()
dmenu = "rofi -show run"  # dmenu replacement
calculator = "rofi -show calc -modi calc -no-show-match -no-sort"
shutdown_menu = f"rofi -show power-menu -modi power-menu:{os.path.expanduser('~/.local/bin/rofi-power-menu')}"
alt_tab = "rofi -show window"
wifi_menu = os.path.expanduser("~/.local/bin/rofi-wifi-menu")  # custom shell script
office_suite = "flatpak run org.libreoffice.LibreOffice"
file_manager = "thunar"
volume_manager = f"alacritty -e {os.path.expanduser('~/.local/bin/pulsemixer')}"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    #
    # For these keys, I prefer the control and shift keys to be the other way around:
    # Key(
    #    [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    # ),
    # Key(
    #    [mod, "shift"],
    #    "l",
    #    lazy.layout.shuffle_right(),
    #    desc="Move window to the right",
    # ),
    # Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    # Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    # Key(
    #    [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    # ),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # ----- My custom keys -----
    # My convention is this:
    # mod + letter represents opening an app
    # mod + shift + letter also represents opening an app
    # mod + ctrl + letter represents interacting with system
    # If there are some keys I use from muscle memory (e.g. taking a screnshot), use that instead
    # Interacting with screen
    Key(
        [mod, "control"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move to the previous monitor"),
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod, "control"], "m", lazy.window.toggle_minimize(), desc="Toggle minimize"),
    Key(
        [mod, "control"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"
    ),
    Key(
        [mod, "control"],
        "w",
        lazy.window.toggle_floating(),
        desc="Set/unset floating mode",
    ),
    # Take screenshot
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn(f"{screenshot_program} gui"),
        desc="take screenshot",
    ),
    Key(
        [mod, "shift"],
        "Print",
        lazy.spawn(
            f"{screenshot_program} screen"  # currently only works for primary monitor
        ),
        desc="print screen",
    ),
    # Various apps
    Key([mod], "b", lazy.spawn(default_browser), desc="Librewolf"),
    Key([mod, "shift"], "b", lazy.spawn("flatpak run com.brave.Browser"), desc="Brave"),
    Key([mod], "m", lazy.spawn(default_media_player), desc="Media player"),
    Key([mod], "o", lazy.spawn(office_suite), desc="Run LibreOffice suite"),
    Key([mod], "f", lazy.spawn(file_manager), desc="Run thunar file manager"),
    Key([mod], "v", lazy.spawn(volume_manager), desc="Volume Mixer Control"),
    # Rofi
    Key([mod], "space", lazy.spawn(dmenu), desc="Run dmenu or replacement"),
    Key([mod], "c", lazy.spawn(calculator), desc="Run rofi calculator"),
    Key([mod], "w", lazy.spawn(wifi_menu), desc="Connect to WiFi"),
    Key(
        [mod, "control", "shift"],
        "s",
        lazy.spawn(shutdown_menu),
        desc="Shutdown the system",
    ),
    Key(["mod1"], "tab", lazy.spawn(alt_tab), desc="Alt-tab through the open windows"),
]

# Groups
group_names = "CTRL,WEB1,WEB2,FILE,DEV,GAME,SYS,PROD,SOC".split(
    ","
)  # may change frequently
groups = [Group(name) for name in group_names]
for i, group in enumerate(groups):
    keys.extend(
        [
            Key(
                [mod],
                str(i + 1),
                lazy.group[group.name].toscreen(),
                desc=f"Switch to group {group.name}",
            ),
            Key(
                [mod, "shift"],
                str(i + 1),
                lazy.window.togroup(group.name, switch_group=True),
                desc=f"Switch to & move focused window to group {group.name}",
            ),
            Key(
                [mod, "control"],
                str(i + 1),
                lazy.window.togroup(group.name, switch_group=False),
                desc=f"Move the focused window to group {group.name} but don't switch to it",
            ),
        ]
    )
# manually add the 0-th group to the end of the groups to be consistent with keyboard
final_group = "ETC"
groups.append(Group(final_group))
keys.extend(
    [
        Key(
            [mod],
            "0",
            lazy.group[final_group].toscreen(),
            desc="Switch to group 0 (the last group)",
        ),
        Key(
            [mod, "shift"],
            "0",
            lazy.window.togroup(final_group, switch_group=True),
            desc="Switch to & move focused window to group 0 (the last group)",
        ),
        Key(
            [mod, "control"],
            "0",
            lazy.window.togroup(final_group, switch_group=False),
            desc="Move focused window to group 0 (the last group) but don't switch to it",
        ),
    ]
)

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.MonadTall(border_width=2, border_focus=colors["purple"], margin=6),
    # layout.MonadWide(border_width=2, border_focus=colors["purple"], margin=6),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND"],
        section_fontsize=11,
        active_bg=colors["purple"],
        active_fg=colors["white"],
        inactive_fg=colors["aqua"],
        padding_y=5,
        section_top=10,
        panel_width=320,
        border_width=2,
        border_focus=colors["purple"],
        margin=6,
        pannel_width=240,
    ),
]

widget_defaults = dict(
    font="Ubuntu Bold", fontsize=12, padding=5, background=colors["bg"]
)

extension_defaults = widget_defaults.copy()  # auto generated by qtile

powerline = {"decorations": [PowerLineDecoration(path="arrow_right")]}

screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpapers/person-looking-over-city-1920x1080.jpg",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="block",
                    rounded=False,
                    active=colors["active-groups"],  # window open in group ==> active
                    this_current_screen_border=colors["purple"],
                    background=colors["bg"],
                ),
                widget.Prompt(),
                widget.WindowName(foreground=colors["purple"]),
                widget.Systray(),  # can only have one on primary monitor
                widget.Sep(foreground=colors["white"]),
                widget.WidgetBox(
                    widgets=[
                        widget.Bluetooth(hci="/dev_74_F8_DB_95_36_94", padding=10),
                        widget.CurrentLayout(),
                    ],
                ),
                widget.Sep(foreground=colors["white"]),
                widget.TextBox(background=colors["bg"], **powerline),
                widget.CPU(
                    foreground=colors["black"],
                    background=colors["light-blue"],
                ),
                widget.ThermalSensor(
                    tag_sensor="Tctl",
                    threshold=90,
                    format="{temp:.0f}{unit}",
                    foreground=colors["black"],
                    background=colors["light-blue"],
                    **powerline,
                ),
                widget.TextBox(
                    "Memory",
                    foreground=colors["black"],
                    padding=2,
                    background=colors["light-green"],
                ),
                widget.Memory(
                    foreground=colors["black"],
                    background=colors["light-green"],
                    measure_mem="G",
                    padding=2,
                    **powerline,
                ),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Wlan(
                    foreground=colors["black"],
                    background=colors["blue"],
                    padding=10,
                    **powerline,
                ),
                widget.Clock(
                    format="%a %m-%d-%Y | %I:%M %p",
                    foreground=colors["black"],
                    background=colors["light-purple"],
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        wallpaper="~/.config/qtile/wallpapers/person-looking-over-city-1920x1080.jpg",
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="block",
                    rounded=False,
                    active=colors["active-groups"],  # window open in group ==> active
                    this_current_screen_border=colors["purple"],
                    background=colors["bg"],
                ),
                widget.Prompt(),
                widget.WindowName(foreground=colors["purple"]),
                widget.Sep(foreground=colors["white"]),
                widget.WidgetBox(
                    widgets=[
                        widget.CurrentLayout(),
                    ],
                ),
                widget.Sep(foreground=colors["white"]),
                widget.TextBox(background=colors["bg"], **powerline),
                widget.CPU(
                    foreground=colors["black"],
                    background=colors["light-blue"],
                ),
                widget.ThermalSensor(
                    tag_sensor="Tctl",
                    threshold=90,
                    format="{temp:.0f}{unit}",
                    foreground=colors["black"],
                    background=colors["light-blue"],
                    **powerline,
                ),
                widget.TextBox(
                    "Memory",
                    foreground=colors["black"],
                    padding=2,
                    background=colors["light-green"],
                ),
                widget.Memory(
                    foreground=colors["black"],
                    background=colors["light-green"],
                    measure_mem="G",
                    padding=2,
                    **powerline,
                ),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Wlan(
                    foreground=colors["black"],
                    background=colors["blue"],
                    padding=10,
                    **powerline,
                ),
                widget.Clock(
                    format="%a %m-%d-%Y | %I:%M %p",
                    foreground=colors["black"],
                    background=colors["light-purple"],
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


# Drag floating layouts.
mouse = [
    # Drag the window to set it to floating mode
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),  # drag with right click to resize the window in floating mode
    ),
    Click(
        [mod], "Button2", lazy.window.bring_to_front()
    ),  # middle mouse button to bring floating window to the front
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors["purple"],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
