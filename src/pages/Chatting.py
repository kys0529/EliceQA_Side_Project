from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.webdriver import WebDriver

from appium.webdriver.common.appiumby import AppiumBy

from utils.locators.ChattingLocator import ChattingTabLocator, ChatRoomLocator
from src.pages.BasePage import BasePage  # 명시적으로 클래스 임포트

class Chatting(BasePage):
    def __init__(self, driver, page_name="Chatting"): # page_name 인자 전달
        super().__init__(driver, page_name)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.tab_locs = ChattingTabLocator()
        self.c_room_locs = ChatRoomLocator()


    def go_to_chatting_tap(self):  # 채팅 탭 진입
        self.click_element(self.tab_locs.ICON)


    def go_to_chat_room(self, user_name): # 채팅 방 진입
        self.go_to_chatting_tap()
        self.click_element(self.c_room_locs.chat_room_profile(user_name))


    def return_to_chat_list(self, user_name): #채팅방 뒤로가기 터치-> 채팅 목록
        self.go_to_chat_room(user_name)
        self.click_element(self.c_room_locs.BACK_BTN)
