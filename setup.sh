#!/bin/bash

cd $HOME
mkdir Desktop Documents Downloads Games Pictures Videos

# add all packages
echo "Installing packages..."
sudo pacman -S --needed - < pkglist.txt

sudo systemctl enable lightdm

echo "Adding yay..."
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..

echo "Installing AUR packages..."
yay -S --needed --noconfirm - < foreignpkglist.txt

echo "Installing flatpak applications..."

while read line; do
	remote_name=$(echo $line | awk '{print $1}')
	remote_url=$(echo $line | awk '{print $2}')
	sudo flatpak remote-add --if-not-exists $remote_name $remote_url 
done < flatpak_remotes.txt

while read line; do
	app_id=$(echo $line | awk '{print $1}')
	app_origin=$(echo $line | awk '{print $2}')
	flatpak install $app_origin $app_id -y
done < flatpaks.txt

echo "Installing python packages..."
cat python-pkglist.txt | xargs pipx install


# Customize ZSH
echo "Adding oh-my-zsh..."
mv .zshrc temp
read -p "Enter 'no' when prompted to change default shell. Type 'exit' when done. [OK] "
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
mv .zshrc .zshrc.orig
mv temp .zshrc

echo "Adding zsh plugins..."
cd $HOME/.oh-my-zsh/custom/plugins
git clone https://github.com/marlonrichert/zsh-autocomplete 
git clone https://github.com/zsh-users/zsh-syntax-highlighting 
git clone https://github.com/zsh-users/zsh-autosuggestions 
cd $HOME


echo "Adding NVM..."
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash


# Customize Rofi
echo "Adding rofi plugins..."
local_scripts_dir=$HOME/.local/bin
mkdir -p $local_scripts_dir

wget https://raw.githubusercontent.com/ericmurphyxyz/rofi-wifi-menu/master/rofi-wifi-menu.sh 
mv rofi-wifi-menu.sh $local_scripts_dir/rofi-wifi-menu

wget https://raw.githubusercontent.com/jluttine/rofi-power-menu/master/rofi-power-menu
mv rofi-power-menu $local_scripts_dir/rofi-power-menu

chmod u+x $local_scripts_dir/*


# Customize Neovim
echo "Adding Neovim config..."
nvim_config_dir=$HOME/.config/nvim
git clone https://github.com/AstroNvim/AstroNvim $nvim_config_dir
echo "Adding Neovim plugins..."
git clone https://github.com/WillChamness/astronvim-config $nvim_config_dir/lua/user
echo "Adding nerd font..."
font_dir=$HOME/.local/share/fonts/nerd-fonts
mkdir -p $font_dir
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/BitstreamVeraSansMono.zip
unzip BitstreamVeraSansMono.zip -d $font_dir
mv BitstreamVeraSansMono.zip $HOME/Downloads


echo "Done. Some things to do manually:"
echo 1. Set \'backend = \"xrender\"\' in \'~/.config/picom/picom.conf\'. Otherwise, your system may freeze after reboot. Note that the blurring effect may not work correctly if you do this.
echo "2. Change the monitor settings in '~/.config/qtile/autostart.sh' to match your preferences"
echo "3. If you chose the default options when installing flatpak, you may want to downgrade the package 'xdg-desktop-portal-gnome' to version '43.1-1'"
echo "4. If you have an NVIDIA graphics card, please install the correct drivers if you haven't already done so"
echo "5. Install nodejs with 'nvm install node'. Then do 'npm install -g neovim'. Note that you will need to reload your terminal session to do this."
echo "Please reboot."
