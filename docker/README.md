# Steps for usage
<!-- TODO: change to asciidoc -->
<!-- BUG: container name = image -->
## English version

1. Install Docker Engine.
    - [Docker Engine](https://docs.docker.com/engine/install/)
    - [linux post-installation](https://docs.docker.com/engine/install/linux-postinstall/)

2. Download this github repository.

    ```shell
    git clone https://github.com/errrr0501/docker_20.04_cuda12_tf1.15
    ```

3. Copy to your project directory.
    - `<workspace_path>`: replace with real project folder path.

        ```shell
        cp -r docker_template <workspace_path>
        # or
        cp -r docker_template <workspace_path>/docker
        ```

    - Example:

        ```shell
        # ROS format workspace
        cp -r docker_template ~/test_ws/src
        ```

4. Adjust Dockerfile to suit your needs
5. Build Docker image (run `build.sh`).
    - `<docker_path>` replace with real to docker location.

    ```shell
    ./<docker_path>/build.sh
    ```

6. Run Docker container (run `run.sh`).
    - `<docker_path>` replace with real to docker location.

    ```shell
    ./<docker_path>/run.sh
    ```

7. Enjoy Docker support.

### Pay attention to the following points when using

1. Docker image name wil be named based on the follwing order:
    - Dockerfile name (suffix), ex: **Dockerfile_DuckDuckGo**, the image name will be **DuckDuckGo**.
    - Workspace folder name (prefix), ex: **Microsoft_ws**, the image name will be **Microsoft**.
    - If neither exists, the image name will be **unknown**.

2. Docker container name will be named in the format of `<user>/<container>` and named based on the following order:
    - `<user>`:
        - Docker login username.
        - system username.
        - if neither exists, `<user>` will be named initial.
    - `<container>`:
        - Workspace folder name (prefix), ex: **chrome_ws**, the container name will be **chrome**.
        - Dockerfile name (suffix), ex: **Dockerfile_Firefox**, the container name will be **Firefox**.
        - If neither exists, the container name will be **unknown**.


3. Dockerfile and entrypoint.sh notes:
    - It is possible to add hardware architecture as a suffix to the file name.
       - ex: **Dockerfile_x86_64** or **Dockerfile_aarch64**.
       - ex: **entrypoint_x86_64.sh** or **entrypoint_aarch64.sh**.
    - If there are multiple Dockerfile or entrypoint.sh file in the docker folder, the script will use the one that matches the current hardware architecture.

---

## 中文版本

1. 安裝 Docker Engine。
    - [Docker Engine](https://docs.docker.com/engine/install/)
    - [linux post-installation](https://docs.docker.com/engine/install/linux-postinstall/)

2. 下載這個 Github 儲存庫。

    ```shell
    git clone https://github.com/ycpss91255/docker_template
    ```

3. 複製到你的專案目錄中。

    - `<workspace_path>`: 替換為真實的專案資料夾位置。

        ```shell
        cp -r docker_template <workspace_path>
        # or
        cp -r docker_template <workspace_path>/docker
        ```

    - 例如:

        ```shell
        # ROS format workspace
        cp -r docker_template ~/test_ws/src
        ```

4. 調整 Dockerfile 以符合你的需求。
5. 建構 Docker image (執行 `build.sh`)。
    - `<docker_path>`: 替換為真實的 docker 資料夾位置。

    ```shell
    ./<docker_path>/build.sh
    ```

6. 執行 Docker container (執行 `run.sh`)。
    - `<docker_path>`: 替換為真實的 docker 資料夾位置。

    ```shell
    ./<docker_path>/run.sh
    ```

7. 享受 Docker 支援。

### 使用時需要注意以下幾點

1. Docker image 名稱會使用以下的順序進行命名：
    - Docker 資料夾名稱 (後綴)，例如：**Docker_resistor**，image 名稱就是 **resistor**。
    - 工作區資料夾名稱 (前綴)，例如：**capacitor_ws**，image 名稱就是 **capacitor**。
    - 以上都沒有，image 名稱為 **unknown**。

2. Docker container 名稱會以 `<user>/<container>` 的格式並且搭配以下順序進行命名：
    - `<user>`：
        - Docker 登入的使用者名稱。
        - 系統的使用者名稱。
        - 以上都沒有，`<user>` 名稱就是 **initial**。
    - `<container>`：
        - 工作區資料夾名稱 (前綴)，例如：**inductor_ws**，container 名稱就是 **inductor**。
        - Docker 資料夾名稱 (後綴)，例如：**Docker_antennas**，container 名稱就是 **antennas**。
        - 以上都沒有，container 名稱為 **unknown**。

3. Dockerfile 與 entrypoint.sh 注意事項：
    - 可允許增加硬體系統架構作為檔案名稱的後綴。
        - 例如：**Dockerfile_x86_64** 或 **Dockerfile_aarch64**。
        - 例如：**entrypoint_x86_64.sh** 或 **entrypoint_arrch64.sh**。
    - 如果在 docker 資料夾底下有多個 Dockerfile 或 entrypoint.sh 會使用與當前電腦系統架構相同檔案。
