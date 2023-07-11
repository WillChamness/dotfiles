#!/bin/bash
picom -b
xset s off
xset -dpms
xset s noblank
xrandr --output HDMI-A-0 --mode 1920x1080 --output DisplayPort-0 --mode 1920x1080 --right-of HDMI-A-0
# does something with xdg-desktop-portal to allow flatpaks to initially load faster
# dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY
systemctl --user import-environment DISPLAY XAUTHORITY
if command -v dbus-update-activation-environment >/dev/null 2>&1; then
    dbus-update-activation-environment DISPLAY XAUTHORITY
fi
