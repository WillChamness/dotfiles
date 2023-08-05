#!/bin/bash

# list installed packages from arch repos and AUR
pacman -Qqen > pkglist.txt
comm -13 <(pacman -Qqdt | sort) <(pacman -Qqdtt | sort) > optdeplist.txt
pacman -Qqem > foreignpkglist.txt

# list installed flatpaks
flatpak remotes --show-details | awk '{print $1,$3}' > flatpak_remotes.txt
flatpak list --app --columns=application --columns=origin > flatpaks.txt | awk '{print $1,$2}' > flatpaks.txt

