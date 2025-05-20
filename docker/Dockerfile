FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
############################## SYSTEM PARAMETERS ##############################
# * Arguments
ARG USER=initial
ARG GROUP=initial
ARG UID=1000
ARG GID="${UID}"
ARG SHELL=/bin/bash
ARG HARDWARE=x86_64
ARG ENTRYPOINT_FILE=entrypint.sh

# * Env vars for the nvidia-container-runtime.
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES all
# ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility,compute

# * Setup users and groups
RUN groupadd --gid "${GID}" "${GROUP}" \
    && useradd --gid "${GID}" --uid "${UID}" -ms "${SHELL}" "${USER}" \
    && mkdir -p /etc/sudoers.d \
    && echo "${USER}:x:${UID}:${UID}:${USER},,,:/home/${USER}:${SHELL}" >> /etc/passwd \
    && echo "${USER}:x:${UID}:" >> /etc/group \
    && echo "${USER} ALL=(ALL) NOPASSWD: ALL" > "/etc/sudoers.d/${USER}" \
    && chmod 0440 "/etc/sudoers.d/${USER}"

# * Replace apt urls
# ? Change to tku
RUN sed -i 's@archive.ubuntu.com@ftp.tku.edu.tw@g' /etc/apt/sources.list
# ? Change to Taiwan
# RUN sed -i 's@archive.ubuntu.com@tw.archive.ubuntu.com@g' /etc/apt/sources.list

# * Time zone
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/"${TZ}" /etc/localtime && echo "${TZ}" > /etc/timezone

# * Copy custom configuration
# ? Requires docker version >= 17.09
COPY --chmod=0775 ./${ENTRYPOINT_FILE} /entrypoint.sh
COPY --chown="${USER}":"${GROUP}" --chmod=0775 config config
# ? docker version < 17.09
# COPY ./${ENTRYPOINT_FILE} /entrypoint.sh
# COPY config config
# RUN sudo chmod 0775 /entrypoint.sh && \
    # sudo chown -R "${USER}":"${GROUP}" config \
    # && sudo chmod -R 0775 config

# * Install packages
RUN apt update \
    && apt install -y --no-install-recommends \
        sudo \
        git \
        htop \
        wget \
        curl \
        psmisc \
        # * Shell
        tmux \
        udev \
        terminator \
        # * base tools
        python3-pip \
        python3-dev \
        python3-setuptools \
        software-properties-common \
        lsb-release \
        # * Work tools
        xvfb \
        ffmpeg \ 
        freeglut3-dev \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

#in terminal can see cudnn version -> major 8 minor 6
#cat /usr/include/cudnn_version.h | grep CUDNN_MAJOR -A 2

ENV DEBIAN_FRONTEND=noninteractive
RUN add-apt-repository universe \
    && apt update \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null \
    && apt update \
    && DEBIAN_FRONTEND=noninteractive apt install -y ros-humble-desktop \
    && apt install -y ros-humble-rmw-cyclonedds-cpp \
    && apt install -y python3-colcon-common-extensions

############################### LIBREALSENSE #######################################
# RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
# RUN sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u
# RUN sudo apt update && apt install -y --no-install-recommends \
#   #Realsense SDK depend
#   librealsense2-dkms \
#   librealsense2-utils \
#   librealsense2-dev \
#   librealsense2-dbg \
#   ros-humble-librealsense2* \
#   ros-humble-diagnostic-updater \
#   ros-humble-vision-msgs \
#   ros-humble-dynamixel-sdk* \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists
RUN sudo mkdir -p /etc/apt/keyrings 
RUN curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | sudo tee /etc/apt/keyrings/librealsense.pgp > /dev/null 
RUN echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo `lsb_release -cs` main" | \
    sudo tee /etc/apt/sources.list.d/librealsense.list 
RUN sudo apt-get update 
RUN sudo apt-get install -y --no-install-recommends \
    librealsense2-utils \
    librealsense2-dev \
    librealsense2-dbg \
    ros-humble-librealsense2* \
    ros-humble-diagnostic-updater \
    ros-humble-vision-msgs \
    ros-humble-visp \
    ros-humble-camera-calibration-parsers \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


############################### PtTorch #######################################
RUN pip3 install --ignore-install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

RUN ./config/pip/pip_setup.sh
RUN pip3 install opencv-python
############################## USER CONFIG ####################################
# * Switch user to ${USER}
USER ${USER}

RUN ./config/shell/bash_setup.sh "${USER}" "${GROUP}" \
    && ./config/shell/terminator/terminator_setup.sh "${USER}" "${GROUP}" \
    && ./config/shell/tmux/tmux_setup.sh "${USER}" "${GROUP}" \
    && sudo rm -rf /config
RUN export CXX=g++
RUN export MAKEFLAGS="-j nproc"
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
RUN echo "set-option -g mouse on" >  ~/.tmux.conf


# * Switch workspace to ~/work
RUN sudo mkdir -p /home/"${USER}"/work
WORKDIR /home/"${USER}"/work

# * Make SSH available
EXPOSE 22

ENTRYPOINT [ "/entrypoint.sh", "terminator" ]
# ENTRYPOINT [ "/entrypoint.sh", "tmux" ]
# ENTRYPOINT [ "/entrypoint.sh", "bash" ]
# ENTRYPOINT [ "/entrypoint.sh" ]
