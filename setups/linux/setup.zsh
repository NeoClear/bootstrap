# Setup 1Password keyrings and apt repos
curl -sS https://downloads.1password.com/linux/keys/1password.asc | sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/amd64 stable main' | sudo tee /etc/apt/sources.list.d/1password.list
sudo mkdir -p /etc/debsig/policies/AC2D62742012EA22/
curl -sS https://downloads.1password.com/linux/debian/debsig/1password.pol | sudo tee /etc/debsig/policies/AC2D62742012EA22/1password.pol
sudo mkdir -p /usr/share/debsig/keyrings/AC2D62742012EA22
curl -sS https://downloads.1password.com/linux/keys/1password.asc | sudo gpg --dearmor --output /usr/share/debsig/keyrings/AC2D62742012EA22/debsig.gpg

# Setup Dropbox keyrings and apt repos
echo 'deb [arch=i386,amd64 signed-by=/etc/apt/keyrings/dropbox.gpg] http://linux.dropbox.com/debian bookworm main' | sudo tee /etc/apt/sources.list.d/dropbox.list
TEMP_KEYRING=`mktemp`
gpg --no-default-keyring --keyring $TEMP_KEYRING  --keyserver hkps://keyserver.ubuntu.com --recv-keys 1C61A2656FB57B7E4DE0F4C1FC918B335044912E
sudo gpg --no-default-keyring --keyring $TEMP_KEYRING --output /etc/apt/keyrings/dropbox.gpg --export

# Setup Google Chrome keyrings and apt repos
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo tee /etc/apt/keyrings/google.asc >/dev/null
echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/google.asc] https://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list

# Update apt source
sudo apt update

# Setup prezto
git clone --recursive https://github.com/NeoClear/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"
setopt EXTENDED_GLOB
for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do
    ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"
done
chsh -s /bin/zsh
