import pytest
import json
import os
from appium import webdriver
from appium.options.common.base import AppiumOptions
from dotenv import load_dotenv

from src.utils.helpers import Helpers

load_dotenv(dotenv_path="src/config/.env")

@pytest.fixture(scope="function")
def login_driver():
    # capabilities 설정을 json에서 불러오기
    with open("src/config/capabilities.json") as f:   
        caps = json.load(f)

    options = AppiumOptions()
    options.load_capabilities(caps)

    # appium 서버 연결
    driver = webdriver.Remote(os.getenv("APPIUM_SERVER_URL"), options=options)

    # 로그인 처리
    login_id = os.getenv("LOGIN_ID")
    login_pw = os.getenv("LOGIN_PW")

    helpers = Helpers(driver)

    helpers.login(login_id, login_pw)

    yield driver

    driver.quit()
