#conftest.py
import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
import time
import subprocess

App_Path = 'app/app-release.apk' # 앱 경로, gitignore에 추가한다?
PackageName = "com.example.travel_on_final" # 패키지명
Device_ID = "27ba2494de0d7ece" # 디바이스 ID, 보안을 위해 가리는 방법이 필요. user_info.py에 넣고 gitignore 하는 방식?

# option
def make_options():
    opts = AppiumOptions()
    opts.load_capabilities({
        "platformName":    "Android",
        "appium:deviceName": Device_ID,
        "appium:automationName": "UiAutomator2"
    })
    return opts


@pytest.fixture(scope="session", autouse=True) # 전체 세션에서 실행 시 앱 설치 여부를 확인하고, 없으면 설치합니다.
def is_app_installed():
    driver = webdriver.Remote("http://127.0.0.1:4723", options=make_options())
    try:
        is_app_installed = driver.is_app_installed(PackageName) # 앱 깔려있는지 확인, True면 이 함수 종료됨
        if is_app_installed== False: #앱이 안깔려있으면 이 조건 진입
            print("\n앱이 설치되지 않아서 앱 설치 중...")
            driver.install_app(App_Path) # 앱 설치시키기
            print("앱 설치 완료!")
    except Exception as e: # 앱설치중 오류가 발생한다면
        pytest.exit("앱 설치되지 않은 오류 발생, 테스트 종료") # pytest 종료
    finally:
        driver.quit() #세션단위로 실행된 드라이버종료함

@pytest.fixture(scope="class") # 클래스 단위로 드라이버를 실행하고, 종료함
def driver():
    driver = webdriver.Remote("http://127.0.0.1:4723", options=make_options()) # 드라이버 실행
    yield driver #드라이버 넘김
    driver.quit() #클래스가 끝나면 드라이버 종료

@pytest.fixture(autouse=True)
def reset_app(driver): #드라이버를 function 단위로 받음
    start_time = time.time()  #시간 측정용, 디버깅용으로 만든 용도
    driver.execute_script('mobile: clearApp',{'appId': PackageName}) # 앱 실행 전 앱 메모리, 캐시 삭제
    driver.activate_app(PackageName) # 패키지 실행
    yield
    driver.terminate_app(PackageName) # 패키지 종료
    end_time = time.time() #시간 측정용 2
    duration = end_time - start_time
    print(f"⌚{duration:.2f}초") # 몇초동안 테스트가 진행되었는지 디버깅용으로 만듬


'''
부가설명
초안으로는, 이전 셀레니움 과제에서 사용했듯이 fixture을 이용해 function 단위로 드라이버를 실행하고 종료했습니다.
하지만.. 각 드라이버가 한번 켜지고 꺼지는데에 제 컴퓨터 기준 11초가 걸리더라구요. (driver 시작부터 driver quit까지)
그래서,
1. 이 전체 세션이 시작될때 앱이 설치되었는지 확인하고, 없으면 설치한다.
2. 클래스 단위로 driver fixture로 드라이버를 실행한다.
3. 각 테스트 함수에서 테스트가 시작될 때 앱의 캐시와 메모리를 삭제한다. (테스트 독립성 유지를 위해) (reset_app fixture 이용)
4. 각 테스트 함수가 시작되면 activate_app을 통해 앱을 켠다.
5. 각 테스트 함수가 종료되면 terminate_app을 통해 앱을 종료한다.
6. 모든 테스트 함수가 종료되면 driver fixture을 통해 드라이버가 종료된다.
의 느낌으로 conftest.py를 작성해봤습니다.
즉 간단히 말하자면!
세션 시작 시 우선 앱이 설치되어 있는지 확인하고 없으면 설치부터 합니다.
다음 클래스 단위로 드라이버가 켜지고 클래스가 끝나면 드라이버가 꺼집니다. (이게 한번에 11초정도 걸림)
함수 단위로 앱이 초기화된 후 앱이 켜지고 함수가 끝나면 앱이 꺼집니다.
이 코드를 사용하려면 app-release.apk 파일을 app 폴더에 넣고 시작해보면 됩니다!
추천 명령어 : 
pytest -s -q .\tests\test_Login.py
'''

