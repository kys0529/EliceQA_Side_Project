from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.webdriver import WebDriver

from appium.webdriver.common.appiumby import AppiumBy

from utils.locators import ChattingLocator
from src.pages.BasePage import BasePage  # 명시적으로 클래스 임포트

class Chatting(BasePage):
    def __init__(self, driver, page_name="Chatting"): # page_name 인자 전달
        super().__init__(driver, page_name)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def into_chatting_tap(self):  # 채팅 탭 진입 함수
        self.click_element(ChattingLocator.CHATTING_TAB_ICON)
