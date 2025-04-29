import os
import time
import json
import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from dotenv import load_dotenv

from src.utils.helpers import Helpers

load_dotenv(dotenv_path="src/config/.env")

def make_options():
    # capabilities 설정을 json에서 불러오기
    with open("src/config/capabilities.json", encoding="utf-8") as f:
        caps = json.load(f)

    options = AppiumOptions()
    options.load_capabilities(caps)

    return options

@pytest.fixture(scope="class")
def driver():
    # appium 서버 연결
    driver = webdriver.Remote(os.getenv("APPIUM_SERVER_URL"), options=make_options())
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_driver(driver):
    # 로그인 처리
    login_id = os.getenv("LOGIN_ID")
    login_pw = os.getenv("LOGIN_PW")
    helpers = Helpers(driver)
    helpers.login(login_id, login_pw)
    yield driver

@pytest.fixture(autouse=True)
def reset_app(driver):
    package_name = os.getenv("PACKAGE_NAME")  # .env 파일에서 읽기
    start_time = time.time()
    driver.execute_script('mobile: clearApp', {'appId': package_name})
    driver.activate_app(package_name)
    yield
    driver.terminate_app(package_name)
    end_time = time.time()
    duration = end_time - start_time
    print(f"⌚ 테스트 소요 시간: {duration:.2f}초")