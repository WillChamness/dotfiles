#
# ~/.bashrc
#
export PATH=$HOME/.local/bin/:$PATH

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

alias ts-debug="npx tsc && node --inspect-brk"

colorscript -e suckless 

# keep at the end of .bashrc
eval "$(starship init bash)"

# kitty fix for SSH
[[ "$TERM" == "xterm-kitty" ]] && alias ssh="TERM=xterm-256color ssh" 
