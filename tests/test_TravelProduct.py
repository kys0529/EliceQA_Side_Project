import pytest
from src.pages.TravelProduct import TravelProduct
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from src.utils.helpers import Helpers

@pytest.mark.usefixtures("login_driver")
class TestTP01:
    def test_open(self, login_driver: WebDriver, request):
        helpers = Helpers(login_driver, page_name="TravelProduct")
        screenshot_file = helpers.setup_screenshot(request.node.name)
        
        helpers.logger.info("접속 완료")
        login_driver.save_screenshot(screenshot_file)

    def test_tp_01_01(self, login_driver: WebDriver, request): # 기능/의도 설명
        #travelProduct = TravelProduct() # 클래스에 대한 객체의 변수명은 첫 문자를 소문자로!
        helpers = Helpers(login_driver, page_name="TravelProduct")
        screenshot_file = helpers.setup_screenshot(request.node.name)
        
        helpers.logger.info("2차 접속 완료")
        login_driver.save_screenshot(screenshot_file)
