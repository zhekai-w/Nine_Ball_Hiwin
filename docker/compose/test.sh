#!/usr/bin/env bash

function
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
        USER: ${user}
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
