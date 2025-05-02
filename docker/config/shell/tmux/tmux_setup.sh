#!/usr/bin/env bash

file_dir=$(dirname "$(readlink -f "${0}")")
username=${1:-"$USER"}

git clone https://github.com/tmux-plugins/tpm /home/"${username}"/.tmux/plugins/tpm \
&& sed "s|~|/home/${username}|g" "${file_dir}"/tmux.conf > /home/"${username}"/.tmux.conf \
&& /home/"${username}"/.tmux/plugins/tpm/scripts/install_plugins.sh
