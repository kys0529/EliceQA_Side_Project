FROM jenkins/jenkins:lts

USER root

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    curl unzip git \
    software-properties-common apt-transport-https \
    && apt-get clean

# pip 최신화
RUN python3 -m pip install --upgrade pip --break-system-packages

# Appium + 테스트 도구 설치
RUN pip install pytest Appium-Python-Client --break-system-packages

# Jenkins GitHub 관련 플러그인 설치
RUN jenkins-plugin-cli --plugins \
    git \
    github \
    workflow-aggregator \
    credentials-binding

USER jenkins