#
# ~/.bashrc
#
export PATH=$HOME/.local/bin/:$PATH

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

colorscript -e suckless 

# keep at the end of .bashrc
eval "$(starship init bash)"
