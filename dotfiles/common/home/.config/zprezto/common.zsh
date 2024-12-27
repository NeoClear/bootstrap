[[ ! -r ~/.opam/opam-init/init.zsh ]] || source ~/.opam/opam-init/init.zsh  > /dev/null 2> /dev/null
[ -f "$HOME/.cargo/env" ] && source "$HOME/.cargo/env"
eval "$(zoxide init zsh)"

# Check if the ~/.zshrc.d directory exists
if [[ -d $HOME/.zshrc.d ]]; then
    # Loop through all files in the directory
    for config_file in $HOME/.zshrc.d/*.zsh(N); do
        # Check if the file is readable
        if [[ -r $config_file ]]; then
            # Source the file
            source $config_file
        fi
    done
fi
