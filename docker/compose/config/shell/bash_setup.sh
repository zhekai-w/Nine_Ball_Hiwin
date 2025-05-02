#!/usr/bin/env bash

# ${1}: USER
# ${2}: GROUP

# Write Hello and alias to bashrc
cat << 'EOF' >> /home/"${1}"/.bashrc

# Commonly used aliases
alias eb='vim ~/.bashrc'
alias sb='source ~/.bashrc && \
    echo "You source user config!"'
alias wb='source ~/work/devel/setup.bash && \
    echo "You source workspace config!"'

EOF

# Write Color and git branch to bashrc
cat << 'EOF' >> /home/"${1}"/.bashrc
# Color and git branch
force_color_prompt=yes
color_prompt=yes

parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ '
fi

unset color_prompt force_color_prompt
EOF

chown "${1}":"${2}" /home/"${1}"/.bashrc
