FROM jenkins/jenkins:lts

USER root

# 필수 패키지 + OpenCV 의존성(libGL)
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    curl unzip git \
    libgl1-mesa-glx \
    software-properties-common apt-transport-https \
    && apt-get clean

# pip 최신화
RUN python3 -m pip install --upgrade pip --break-system-packages

# Jenkins GitHub 관련 플러그인만 설치
RUN jenkins-plugin-cli --plugins \
    git \
    github \
    workflow-aggregator \
    credentials-binding

USER jenkins