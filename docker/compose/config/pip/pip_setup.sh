#!/usr/bin/env bash

# python3 -m pip install --upgrade --force-reinstall pip \
# && pip3 install -r ./pip/requirements.txt
file_dir=$(dirname "$(readlink -f "${0}")")

pip install --upgrade --force-reinstall pip \
&& pip install -r "${file_dir}"/requirements.txt
