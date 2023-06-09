#!/bin/bash
# run compositor in background
picom -b
# prevent PC from sleeping (sleeps when running emulators)
xset s off
xset -dpms
xset s noblank
# monitor setup
xrandr --output HDMI-A-0 --mode 1920x1080 --rate 60 --output DisplayPort-0 --mode 1920x1080 --rate 60 --right-of HDMI-A-0
# not sure what this is but flatpaks run a lot faster when this is ran
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY
