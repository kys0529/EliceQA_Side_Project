from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver

from appium.options.common.base import AppiumOptions

from src.pages.Chatting import Chatting
from utils.locators import ChattingLocator


class BaseTest:
    def setUp(self):
        options = AppiumOptions()

        options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2"
        })
        
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        print("Class test 시작.")
        
    def tearDown(self):
        if self.driver:
            self.driver.quit()

class TestCP01(BaseTest):
    def test_cp_01_01(): # 기능/의도 설명
        try:
            chatting = Chatting() # 클래스에 대한 객체의 변수명은 첫 문자를 소문자로!
            chatting.into_chatting_tap()

            title = chatting.get_element(ChattingLocator.CHATTING_TAB_TITLE)

            assert title.text == '채팅 목록'
            print('✅ 채팅 탭 진입 성공')

        except Exception as e:
            print(e)
            raise


#우선 대충 틀만 적어놓기!!!