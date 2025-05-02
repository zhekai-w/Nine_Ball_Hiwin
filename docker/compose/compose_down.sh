#!/usr/bin/env bash

# Get dependent parameters
source "$(dirname "$(readlink -f "${0}")")/get_param.sh"

docker compose down

# rm -f ${FILE_DIR}/docker-compose.yml ${FILE_DIR}/.env

# * remove docker compose
# docker rm -f ${CONTAINER} >/dev/null && echo "remove '${CONTAINER}' container"
