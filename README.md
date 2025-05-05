# 📱 TravelOn App 테스트 자동화 사이드 프로젝트

엘리스 트랙에서 제공한 **TravelOn** 앱을 대상으로 진행한 Appium 기반의 테스트 자동화 사이드 프로젝트입니다.  
직접 제공된 APK 파일을 Android 실기기에서 실행하여 Appium, Pytest, Jenkins를 통해 UI 테스트 자동화 환경을 구축하였습니다.

## 👥 팀 구성
- **스터디장**: 강연수
- **팀원**: 김혜원, 박재윤, 신은영, 양송이

## 🔗 프로젝트 리포지토리 및 앱 정보
- TravelOn 앱 GitHub: [https://github.com/jhdodev/TravelON](https://github.com/jhdodev/TravelON)
- 테스트 대상: `TravelOn` 앱 (제공된 APK 기반)

## 📌 프로젝트 개요
**TravelOn**은 AI 기반의 여행 패키지 및 가이드 서비스를 제공하는 앱입니다.  
본 프로젝트에서는 핵심 탭별 기능을 중심으로 Appium을 활용한 **모바일 UI 테스트 자동화**를 구현하였습니다.

## 🧪 탭별 테스트 영역 담당
| 팀원     | 담당 탭            |
|--------|-----------------|
| 박재윤  | 로그인 / 회원가입     |
| 강연수  | 홈               |
| 양송이  | 마이페이지           |
| 김혜원  | 여행 패키지          |
| 신은영  | 채팅              |

## 🔍 앱 주요 기능 (원 프로젝트 기준)
- **여행 패키지**
  - 패키지 검색, 정렬, 지역/카테고리 필터링, 찜 기능
  - 상세 정보 확인 및 가이드 프로필 기능 (외부 API 연동)
  - 실시간 예약 및 리뷰/평점 등록 시스템
- **가이드 기능**
  - 패키지 등록/관리, 예약 현황, 채팅 상담, 매출 통계 등
- **여행 갤러리**
  - 이미지 업로드, 댓글/좋아요, 위치 기반 후기 공유
- **채팅 시스템**
  - 실시간 1:1 채팅, 이미지 전송, 패키지/지도 정보 공유
- **알림 시스템**
  - 예약/채팅 관련 푸시 알림

## 🛠 사용 기술
- **테스트 자동화**: Appium, Python, Pytest
- **CI/CD**: Jenkins

## ⚙️ 환경 설정
📁 `.env` 예시 (`src/config/.env`)
```env
APPIUM_SERVER_URL="http://127.0.0.1:4723"           # Appium 서버 주소
PACKAGE_NAME="com.example.travel_on_final"          # 패키지 이름
LOGIN_ID="<your_login_email>"                       # 로그인 ID
LOGIN_PW="<your_password>"                          # 로그인 PW
```

📁 `capabilities.json` 예시 (`src/config/capabilities.json`)
```json
{
    "platformName": "Android",
    "appium:deviceName": "<your_device_name>",
    "appium:automationName": "UiAutomator2",
    "app": "<absolute_path_to_apk_file>",
    "appium:appPackage": "com.example.travel_on_final",
    "appium:appActivity": ".MainActivity"
}
```

## 📁 디렉토리 구조
```
project_root/
├── src/                   # 자동화 프레임워크의 소스 코드
│   ├── pages/             # Page Object 클래스 (UI 요소 및 메서드 정의)
│   │   ├── __init__.py
│   │   └── example_page.py
│   ├── utils/             # 공통 유틸리티 함수 및 헬퍼 모듈
│   │   ├── __init__.py
│   │   └── helpers.py
│   │   └── locators/      # 로케이터 관리 디렉토리
│   ├── config/            # 환경 설정 파일
│   │   ├── config.ini
│   │   └── .env
│   │   └── capabilities.json
│   └── resources/         # 테스트 데이터 및 기타 리소스 파일
│       ├── testdata/      # JSON, CSV, XML 형태의 테스트 데이터
│       └── assets/        # 이미지 등 기타 자원 파일
├── tests/                 # 실제 테스트 케이스 구현 디렉토리 (pytest 테스트 코드)
│   ├── conftest.py        # pytest fixture 및 공통 설정 정의
│   ├── test_example.py    # 실제 테스트 스크립트 (test_*.py 형식)
│   └── ...
├── reports/               # 테스트 실행 후 생성된 보고서 및 로그 저장 디렉토리
│   ├── logs/
│   └── screenshots/
├── requirements.txt       # Python 의존성 패키지 목록 (pip install -r requirements.txt)
├── pytest.ini             # pytest 설정 파일 (테스트 옵션 지정)
└── Jenkinsfile            # Jenkins CI/CD 파이프라인 정의 파일
```