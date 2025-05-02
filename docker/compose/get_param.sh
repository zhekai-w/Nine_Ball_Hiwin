#!/usr/bin/env bash

# Function to set the Docker image name based on the directory path
#
# Parameters:
#    ${1}: the directory path to search for the Dockerfile
#
# Returns:
#    IMAGE: The name of the Docker image to be used
#
# This function first checks if the `docker` folder has a suffix, such as `docker_xxx`, and extracts the suffix
# and store it in the `IMAGE` variable. If the `docker` folder has no suffix, it checks if the workspace folder
# has a prefix, such as `xxx_ws`, and extracts the prefix and store it in the `IMAGE` variable. If the workspace
# folder has no prefix/suffix, the image name is set to `unknown`. The function then returns the image name.
#
# If no Dockerfile is found in the directory, the function will not work correctly and will return an incorrect
# image name.
#
function set_image_name() {
    # Check if the `docker` folder has a suffix, such as `docker_xxx`
    # If yes, extract the suffix and store it in the `IMAGE` variable
    IMAGE=$(echo "${1}" | awk -F/ '{
            for (i=NF; i>0; i--) {
                if ($i ~ /^docker_/) {
                    sub(/^docker_/,"",$i);
                    print $i;
                    exit;
                }
            }
        }')

    # If the `docker` folder has no suffix, check if the workspace folder has a prefix, such as `xxx_ws`
    # If yes, extract the prefix and store it in the `IMAGE` variable, and update the `WS_PATH` variable accordingly
    if [[ -z "${IMAGE}" ]]; then
        IMAGE=$(echo "${1}" | awk -F/ '{
                for (i=NF; i>0; i--) {
                    if ($i ~ /_ws$/) {
                        sub(/_ws$/,"",$i);
                        print $i;
                        exit;
                    }
                }
            }')
    fi

    # If the workspace folder has no prefix/suffix, set the image name to `unknown`
    # and the workspace path to the current directory
    IMAGE="${IMAGE:-unknown}"

    # echo the values of IMAGE
    echo "${IMAGE}"
}

# Function to extract the path of the workspace folder
# and store it in the `WS_PATH` variable
#
# Parameters:
#    ${1}: the directory path to extract the workspace folder from
#
# Returns:
#    WS_PATH: the path to the workspace folder
#
# If a workspace folder with the given prefix is found,
# its path is stored in the `WS_PATH` variable.
# Otherwise, the `WS_PATH` variable is set to the parent directory
# of the given directory path.
#
function get_workdir() {
    WS_NAME=$(echo "${1}" | awk -F/ '{
            for (i=NF; i>0; i--) {
                if ($i ~ /_ws$/) {
                    print $i;
                    exit;
                }
            }
        }')

    if [[ -n "${WS_NAME}" ]]; then
        # Extract the path of the workspace folder and store it in the `WS_PATH` variable
        WS_PATH=$(echo "${1}" | awk -v ws="${WS_NAME}" -v found=0 -F/ '{
                for (i=1; i<=NF; i++) {
                    if ($i ~ /_ws$/){
                        found=1;
                        break;
                    }
                    printf "%s/", $i
                }
                if (found) printf "%s", ws
            }')
    else
        # If no workspace folder is found based on the provided prefix, extract the path to the parent directory
        WS_PATH="$(echo "${1}" | rev | cut -d '/' -f 2- | rev)"
    fi

    # echo the values of WS_PATH
    echo "${WS_PATH}"
}

# Function to check if GraphicsCard is NVIDIA and nvidia-docker2 or nvidia-container-runtime is installed
#
# Parameters:
#    None
#
# Returns:
#    GPU_FLAG: if NVIDIA graphics card and nvidia-docker2 or nvidia-container-runtime is installed, empty string otherwise
#
function check_nvidia() {
    # if (lspci | grep -q VGA ||
    #     lspci | grep -iq NVIDIA ||
    #     lsmod | grep -q nvidia ||
    #     nvidia-smi -L >/dev/null 2>&1 | grep -iq nvidia) &&
    #     (command -v nvidia-smi >/dev/null 2>&1) &&
    #     (command -v nvidia-docker >/dev/null 2>&1 ||
    #         dpkg -l | grep -q nvidia-container-toolkit); then
    if (dpkg -l | grep -q nvidia-docker || dpkg -l | grep -q nvidia-container-toolkit); then
        # Used in Docker run shell script
        GPU_FLAG="--gpus all"

        # Used in Docker compose shell script
        COMPOSE_GPU_FLAG="nvidia"
        COMPOSE_GPU_CAPABILITIES="gpu, utility"

    else
        # Used in Docker run shell script
        GPU_FLAG=""

        # Used in Docker compose shell script
        NVIDIA_FLAG=""
        GPU_CAPABILITIES=""
    fi

    # echo the values of GPU_FLAG
    printf "%s.%s.%s" "${GPU_FLAG}" "${COMPOSE_GPU_FLAG}" "${COMPOSE_GPU_CAPABILITIES}"
}

# Function to get system parameter, including user, group, UID, GID, hardware architecture
#
# Parameters:
#    None
#
# Returns:
#    DOCKER_HUB_USER: If you have logged in to docker, it is the user name of docker hub
#    user: the user of the current Docker environment or the user of the current system
#    group: the group of the current user
#    uid: the UID of the current user
#    gid: the GID of the current user
#    hardware: the hardware architecture of the current system
#
function get_system_info() {
    # Try to retrieve the current user from Docker using the `docker info`
    # command and store it in the `DOCKER_HUB_USER` variable
    # If that fails, fall back to using the `id` command to get the current user
    DOCKER_INFO_NAME=$(docker info 2>/dev/null | grep Username | cut -d ' ' -f 3)
    if [[ -z "${DOCKER_INFO_NAME}" ]]; then
        DOCKER_HUB_USER="$(id -un)"
    else
        DOCKER_HUB_USER="${DOCKER_INFO_NAME}"
    fi

    user="$(id -un)"
    group="$(id -gn)"

    # Retrieve the UID of the current user using the `id` command and store it in the `uid` variable
    uid="$(id -u)"

    # Retrieve the GID of the current user using the `id` command and store it in the `gid` variable
    gid="$(id -g)"

    # Retrieve the hardware architecture of the current system using the `uname` command and store it in the `hardware` variable
    hardware="$(uname -m)"

    # Print out the values of user, group, uid, gid and hardware
    printf "%s %s %s %d %d %s" "${DOCKER_HUB_USER}" "${user}" "${group}" "${uid}" "${gid}" "${hardware}"
}

# This function sets the Dockerfile name based on the directory path and hardware architecture
#
# Parameters:
#    ${1}: the directory path to search for the Dockerfile
#    ${2}: the hardware architecture
#
# Returns:
#    DOCKERFILE_NAME: The name of the Dockerfile to be used
#
# Exit codes:
#    1: Dockerfile file not found
#    2: Incorrect naming format of Dockerfile file
#
# If no Dockerfile is found in the directory, an error message is displayed and the script exits.
# If only one Dockerfile is found, it is returned.
# If a Dockerfile with the architecture suffix is found, it is returned.
# Otherwise, the default Dockerfile is returned.
#
function set_dockerfile() {
    readarray -t file_list < <(find "${1}" -maxdepth 1 -type f -name "Dockerfile*" -printf "%f\n")

    # Check if there is no Dockerfile file
    if [[ ${#file_list[@]} -eq 0 ]]; then
        exit 1
    else
        for file in "${file_list[@]}"; do
            # Make sure the Dockerfile is in the current directory
            if [[ ${file} == "Dockerfile" ]]; then
                DOCKERFILE_NAME="Dockerfile"
                break
            # Make sure the Dockerfile with the architecture suffix is in the current directory
            elif [[ ${file} == "Dockerfile_${2}" ]]; then
                DOCKERFILE_NAME="Dockerfile_${2}"
                break
            fi
        done
    fi

    # If none of the above conditions are true, print an error message and exit
    if [[ -z ${DOCKERFILE_NAME} ]]; then exit 2; fi

    # echo the values of DOCKERFILE_NAME
    echo "${DOCKERFILE_NAME}"
}


# This function sets the entrypoint.sh name based on the directory path and hardware architecture
#
# Parameters:
#    ${1}: the directory path to search for the entrypoint.sh
#    ${2}: the hardware architecture
#
# Returns:
#    ENTRYPOINT_FILE: The name of the entrypoint.sh to be used
# Exit codes:
#    1: entrypoint.sh file not found
#    2: Incorrect naming format of entrypoint.sh file
#
# If no entrypoint.sh is found in the directory, an error message is displayed and the script exits.
# If only one entrypoint.sh is found, it is returned.
# If a entrypoint.sh with the architecture suffix is found, it is returned.
# Otherwise, the default entrypoint.sh is returned.
#
function set_entrypoint() {
    readarray -t file_list < <(find "${1}" -maxdepth 1 -type f -name "entrypoint*" -printf "%f\n")

    # Check if there is no entrypoint file
    if [[ ${#file_list[@]} -eq 0 ]]; then
        exit 1
    else
        for file in "${file_list[@]}"; do
            # Make sure the entrypoint.sh is in the current directory
            if [[ ${file} == "entrypoint.sh" ]]; then
                ENTRYPOINT_FILE="entrypoint.sh"
                break
            # Make sure the entrypoint.sh with the architecture suffix is in the current directory
            elif [[ ${file} == "entrypoint_${2}.sh" ]]; then
                ENTRYPOINT_FILE="entrypoint_${2}.sh"
                break
            fi
        done
    fi

    # If none of the above conditions are true, print an error message and exit
    if [[ -z ${ENTRYPOINT_FILE} ]]; then exit 2; fi

    # echo the values of ENTRYPOINT_FILE
    echo "${ENTRYPOINT_FILE}"
}
################################ MAIN ##########################################
# Analyze the user input parameters to make thecorresponding action
ARGS=$(getopt \
    -o h \
    --long debug,help \
    -- "$@")
eval set -- "${ARGS}"

while true; do
    case "${1}" in
    --debug)
        DEBUG=true
        shift
        ;;
    -h | --help)
        echo "Usage: ${0} [OPTION]"
        echo " Options:"
        echo "     --debug    Enable debug mode"
        echo " -h, --help     Show this help massage and exit"
        exit 0
        ;;
    --)
        shift
        break
        ;;
    *)
        echo "Unknown option: ${1}"
        exit 1
        ;;
    esac
done

# $DEBUG && set -x

# TODO: wait check
# Start sharing xhost
# xhost +local:root

FILE_DIR=$(dirname "$(readlink -f "${0}")")

IFS='.' read -r GPU_FLAG COMPOSE_GPU_FLAG COMPOSE_GPU_CAPABILITIES <<< "$(check_nvidia)"
read -r DOCKER_HUB_USER user group uid gid hardware <<<"$(get_system_info)"
IMAGE="$(set_image_name "${FILE_DIR}")"
WS_PATH="$(get_workdir "${FILE_DIR}" "${IMAGE}")"
DOCKERFILE_NAME=$(set_dockerfile "${FILE_DIR}" "${hardware}")
set_dockerfile_exit_status=$?

ENTRYPOINT_FILE=$(set_entrypoint "${FILE_DIR}" "${hardware}")
set_entrypoint_exit_status=$?

# Set the container name to be the same as the image name
CONTAINER="${IMAGE}"

if [ "${DEBUG}" = true ]; then
    echo "DOCKER_HUB_USER=${DOCKER_HUB_USER}"
    echo "user=${user}"
    echo "group=${group}"
    echo "uid=${uid}"
    echo "gid=${gid}"
    echo -e "hardware=${hardware}\n"

    echo "FILE_DIR=${FILE_DIR}"
    echo "WS_PATH=${WS_PATH}"
    echo "IMAGE=${IMAGE}"
    echo -e "CONTAINER=${CONTAINER}\n"

    echo "DOCKERFILE_NAME=${DOCKERFILE_NAME}"
    echo -e "ENTRYPOINT_FILE=${ENTRYPOINT_FILE}"

    echo "GPU_FLAG=${GPU_FLAG}"
    echo "COMPOSE_GPU_FLAG=${COMPOSE_GPU_FLAG}"
    echo "COMPOSE_GPU_CAPABILITIES=${COMPOSE_GPU_CAPABILITIES}"
fi

# Check if the Dockerfile and entrypoint.sh files are found and set correctly
if [ "${set_dockerfile_exit_status}" != 0 ] || [ "${set_entrypoint_exit_status}" != 0 ]; then
    case "${set_dockerfile_exit_status}" in
    1)
        echo "Dockerfile file not found"
        ;;
    2)
        echo "Incorrect naming format of Dockerfile file"
        ;;
    esac

    case "${set_entrypoint_exit_status}" in
    1)
        echo "entrypoint.sh file not found"
        ;;
    2)
        echo "Incorrect naming format of entrypoint.sh file"
        ;;
    esac

    exit 1
fi
