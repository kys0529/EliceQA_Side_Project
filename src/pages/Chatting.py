from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.webdriver import WebDriver

from appium.webdriver.common.appiumby import AppiumBy

from utils.locators.ChattingLocator import ChattingTabLocator, ChatRoomLocator, BottomSheetLocators
from src.pages.BasePage import BasePage  # 명시적으로 클래스 임포트

# 스와이프 관련 임포트
# from appium.webdriver.common.pointer_input import PointerInput
# from selenium.webdriver.common.actions import ActionBuilder

class Chatting(BasePage):
    def __init__(self, driver, page_name="Chatting"): # page_name 인자 전달
        super().__init__(driver, page_name)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.tab_locs = ChattingTabLocator()
        self.c_room_locs = ChatRoomLocator()
        self.bottom_locs = BottomSheetLocators


    def go_to_chatting_tap(self):  # 채팅 탭 진입
        self.click_element(self.tab_locs.ICON)


    def go_to_chat_room(self, user_name): # 채팅 방 진입
        self.go_to_chatting_tap()
        self.click_element(self.c_room_locs.chat_room_profile(user_name))


    def return_to_chat_list(self, user_name): #채팅방 뒤로가기 터치-> 채팅 목록
        self.go_to_chat_room(user_name)
        self.click_element(self.c_room_locs.BACK_BTN)


    def tap_plus_button(self, user_name):
        self.go_to_chat_room(user_name)
        self.click_element(self.c_room_locs.PLUS_BTN)


    def tap_gallery_icon(self, user_name):
        self.tap_plus_button(user_name)
        self.click_element(self.bottom_locs.GALLERY_ICON)





    #스와이프 관련 함수.. 임포트가 안돼서 작동안함..
    # def swipe_left(self, element):
    #     rect = element.rect

    #     # 스와이프 시작점: 오른쪽 끝 -10, 끝점: 왼쪽 끝 +10 (좌 ← 우)
    #     start_x = rect['x'] + rect['width'] - 10
    #     start_y = rect['y'] + rect['height'] // 2
    #     end_x = rect['x'] + 10
    #     end_y = start_y

    #     # 손가락 포인터 정의
    #     finger = PointerInput(interaction.POINTER_TOUCH, "finger")
    #     actions = ActionBuilder(self.driver)
    #     actions.add_action(finger)

    #     # 제스처 정의
    #     finger.create_pointer_move(duration=0, x=start_x, y=start_y, origin='viewport')
    #     finger.create_pointer_down(button=0)
    #     finger.create_pause(100)
    #     finger.create_pointer_move(duration=300, x=end_x, y=end_y, origin='viewport')
    #     finger.create_pointer_up(button=0)

    #     # 액션 실행
    #     actions.perform()