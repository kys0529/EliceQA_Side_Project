pipeline {
    agent any

    environment {
        ENV_FILE = credentials('env-file')                  // .env 파일
        CAP_FILE = credentials('capabilities-file')         // capabilities.json 파일
    }

    stages {
        stage('Run Appium Tests') {
            steps {
                sh '''
                    # 기존 파일이 이미 존재할 경우 삭제
                    rm -f src/config/.env
                    rm -f src/config/capabilities.json

                    # Credentials로부터 복사
                    cp "$ENV_FILE" src/config/.env
                    cp "$CAP_FILE" src/config/capabilities.json

                    # 가상환경 설정 및 테스트 실행
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest tests/test_Home.py
                '''
            }
        }
    }
}
