from src.pages.Login import Login
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

import time
@pytest.mark.usefixtures("driver")
@pytest.mark.skip("아직 작성계획 없음")
class TestLR02:
    def test_lr_02_01(self, driver, request): # 기능/의도 설명
        login = Login(driver)

        login.logger.info("로그인 페이지 접속")
        login.save_screenshot(request.node.name)

    def test_lr_01_02(self, driver): 
        print("login_2")
