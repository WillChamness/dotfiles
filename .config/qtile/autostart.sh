#!/usr/bin/env bash
# run compositor in background
picom -b
# prevent PC from sleeping (sleeps when running emulators)
xset s off
xset -dpms
xset s noblank
# monitor setup
xrandr --output HDMI-A-0 --mode 1920x1080 --rate 60 --primary --output DisplayPort-0 --mode 1920x1080 --rate 60 --right-of HDMI-A-0
# not sure what this is but flatpaks run a lot faster when this is ran
# dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY
systemctl --user import-environment DISPLAY XAUTHORITY
if command -v dbus-update-activation-environment >/dev/null 2>&1; then
    dbus-update-activation-environment DISPLAY XAUTHORITY
fi

# live wallpaper
$HOME/.local/bin/wallpaper-wrap
