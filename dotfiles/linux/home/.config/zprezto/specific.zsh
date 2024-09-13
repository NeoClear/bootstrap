setxkbmap -option ctrl:nocaps
xcape -e 'Control_L=Escape'

source /usr/share/doc/fzf/examples/key-bindings.zsh
source /usr/share/doc/fzf/examples/completion.zsh

alias pbcopy='xclip -selection clipboard'

export XSECURELOCK_COMPOSITE_OBSCURER=0
