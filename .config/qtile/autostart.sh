#!/bin/bash
picom -b
xset s off
xset -dpms
xset s noblank
xrandr --output HDMI-A-0 --mode 1920x1080 --output DisplayPort-0 --mode 1920x1080 --right-of HDMI-A-0
