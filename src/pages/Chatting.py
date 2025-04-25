from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver

from appium.options.common.base import AppiumOptions

from appium.webdriver.common.appiumby import AppiumBy

from utils.locators import ChattingLocator

class Chatting:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator): 
        return self.wait.until(EC.presence_of_element_located(locator))

    def element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def into_chatting_tap(self): # 채팅 탭 진입 함수
        self.element_clickable(ChattingLocator.CHATTING_TAB)