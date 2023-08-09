# dotfiles
My Linux Dotfiles

![My Arch Linux Desktop](./.github/my-archlinux-desktop.jpg)

|My Setup|
|-------|
|**OS:** Arch Linux|
|**Window Manager:** Qtile (X11)|
|**Terminal Emulator:** Alacritty|
|**Shell:** ZSH (oh-my-zsh)|
|**Compositor:** Picom|
|**Dmenu Replacement:** Rofi|
|**Text Editor:** Vim|
|**Code Editor:** Neovim|
|**GUI File Manager:** Thunar|
|**CLI File Manager:** Ranger|
|**Screenshot Program:** Scrot|

Feel free to use whatever you want in your own dotfiles. If you want my exact configuration from scatch, follow the install instructions.

# Installation
First, do a minimal Arch Linux installation with the multilib repo enabled. Then, run these commands:
```
cd /home
sudo mv $USER $USER.orig
sudo mkdir $USER
sudo chown $USER:$USER $USER
git clone https://github.com/WillChamness/dotfiles $USER
cd $USER
chmod u+x setup.sh
./setup.sh
```

This will install all packages that I use, including AUR packages and flatapks. Note that there are some things that will need to be done manually. See `setup.sh` for more details.
