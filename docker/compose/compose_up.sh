#!/usr/bin/env bash

# Get dependent parameters
source "$(dirname "$(readlink -f "${0}")")/get_param.sh"

# set -x
# Write docker compose parameters to .env file
cat << EOF >> ${FILE_DIR}/.env
DOCKER_HUB_USER=${DOCKER_HUB_USER}
user=${user}
group=${group}
uid=${uid}
gid=${gid}
hardware=${hardware}
FILE_DIR=${FILE_DIR}
WS_PATH=${WS_PATH}
IMAGE=${IMAGE}
CONTAINER=${CONTAINER}
DOCKERFILE_NAME=${DOCKERFILE_NAME}
ENTRYPOINT_FILE=${ENTRYPOINT_FILE}
COMPOSE_GPU_FLAG=${COMPOSE_GPU_FLAG}
COMPOSE_GPU_CAPABILITIES=${COMPOSE_GPU_CAPABILITIES}
EOF

# TODO: multi docker container up
# Create a new Docker Compose file
cat << EOF > docker-compose.yml
services:
  basic: &basic
    # docker build params
    image: ${DOCKER_HUB_USER}/${IMAGE}
    # image: ${DOCKER_HUB_USER}/${IMAGE}:${tag}
    build:
      context: ${FILE_DIR}
      dockerfile: ${DOCKERFILE_NAME}
      args:
        user: ${user}
        UID: ${uid}
        GROUP: ${group}
        GID: ${gid}
        HARDWARE: ${hardware}
        ENTRYPOINT_FILE: ${ENTRYPOINT_FILE}
    # docker run params
    container_name: ${CONTAINER}
    # tty: true
    # stdin_open: true
    # restart: no
    privileged: true
    network_mode: host
    ipc: host
    environment:
      - XAUTHORITY=/home/${user}/.Xauthority
      - DISPLAY=${DISPLAY}
      - QT_X11_NO_MITSHM=1
    volumes:
      - ${WS_PATH}:/home/${user}/work
      - /dev:/dev
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
      - /tmp/.Xauthority:/home/${user}/.Xauthority:rw
      # - /etc/timezone:/etc/timezone:ro
      # - /etc/localtime:/etc/localtime:ro
    # ports:
    #   - "5000:5000"
EOF

# TODO: confirm nvidia card found, enable gpu functionality
cat << EOF >> docker-compose.yml
    deploy:
      resources:
        reservations:
          devices:
            - driver: ${COMPOSE_GPU_FLAG}
              capabilities: [${COMPOSE_GPU_CAPABILITIES}]
EOF

# TODO: get_parm.sh add docker-compose.yml
# * docker compose up
docker compose \
    -f ${FILE_DIR}/docker-compose.yml \
    --env-file ${FILE_DIR}/.env \
    up --build -d

# * remove docker compose
# docker rm -f ${CONTAINER} >/dev/null && echo "remove '${CONTAINER}' container"
