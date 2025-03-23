# Common packages could be installed via the default package manager of OS without extra setups
COMMON_PACKAGES = """
neovim
vim
fzf
curl
wget
git
zsh
neofetch
ripgrep
gh
tree
opam
htop
hugo
smartmontools
ncdu
aria2
tmux
nodejs
npm
go
btop
""".split()

# Linux packages could be installed on any Linux distro via default package manager
LINUX_PACKAGES = """
emacs
i3
xcape
alacritty
arandr
xsecurelock
gnome-shell-extension-manager
redshift
debsig-verify debian-keyring
python3-gpg
python3-pip libdrm-dev
pavucontrol
okular
rofi
pahole
emacs
i3
xcape
alacritty
arandr
xsecurelock
gnome-shell-extension-manager
redshift
debsig-verify debian-keyring
python3-gpg
python3-pip
libdrm-dev
pavucontrol
okular
rofi
pahole
""".split()

# Installed via [brew install ...]
DARWIN_CLI_PACKAGES = """
gnu-tar
""".split()

# Installed via [brew install --cask ...]
DARWIN_GUI_PACKAGES = """
emacs
1password
amazon-q
dropbox
iterm2
raycast
google-chrome
rectangle
pdf-expert
zoom
iina
discord
hyperkey
font-jetbrains-mono
zed
balenaetcher
monitorcontrol
tradingview
scroll-reverser
""".split()
