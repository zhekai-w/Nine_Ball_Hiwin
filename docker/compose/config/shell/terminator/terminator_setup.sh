#!/usr/bin/env bash

# ${Username}: USER
# ${2}: GROUP

file_dir=$(dirname "$(readlink -f "${0}")")
username=${1:-"$USER"}
usergroup=${2:-"$GROUP"}

mkdir -p /home/"${username}"/.config/terminator
cp -r "${file_dir}"/config /home/"${username}"/.config/terminator/config
chown -R "${username}":"${usergroup}" /home/"${username}"/.config/terminator
