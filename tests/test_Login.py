#from src.pages.Login import Login
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

import time
@pytest.mark.usefixtures("driver")
class TestLR01:
    def test_lr_01_01(self, driver): # 기능/의도 설명
        #login = Login() # 클래스에 대한 객체의 변수명은 첫 문자를 소문자로!
        locator = 'android.widget.EditText'
        wait = WebDriverWait(driver,10)
        element = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, locator)))
        element.click()
        element.send_keys("test")
        assert element.text == "test", "입력이 안됨 ㅠㅠ"
    def test_lr_01_02(self, driver): 
        locator = 'android.widget.ImageView'
        wait = WebDriverWait(driver,10)
        element = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, locator)))
        assert element.is_displayed(), "안보여용"

'''
임시로 만든용도입니다!
아직 POM 적용되지 않은 테스트용 코드
'''