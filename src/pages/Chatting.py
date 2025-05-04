from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.webdriver import WebDriver
import time

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


    def go_to_chatting_tap(self):
        """채팅 탭 진입"""
        self.click_element(self.tab_locs.ICON)


    def go_to_chat_room(self, user_name): 
        """채팅 방 진입"""
        self.go_to_chatting_tap()
        self.click_element(self.c_room_locs.chat_room_profile(user_name))


    def return_to_chat_list(self, user_name):
        """채팅방 뒤로가기 터치-> 채팅 목록"""
        self.go_to_chat_room(user_name)
        self.click_element(self.c_room_locs.BACK_BTN)


    def tap_plus_button(self, user_name):
        """채팅방 하단 '+' 버튼 터치"""
        self.go_to_chat_room(user_name)
        self.driver.hide_keyboard()
        time.sleep(1) # 오류로 인해 설정
        self.click_element(self.c_room_locs.PLUS_BTN)


    def tap_bottom_icon(self, user_name, icon_locator):
        """+ 버튼 바텀시트 아이콘 터치"""
        self.tap_plus_button(user_name)
        self.click_element(icon_locator)


    def take_photo(self):
        self.click_element(self.bottom_locs.TAKE_PHOTO_BTN)  # 촬영
        self.click_element(self.bottom_locs.TAKE_PHOTO_CONFIRM_BTN)  # 확인 버튼


    def take_and_send_photo_with_retry(self):
        """카메라로 사진을 촬영하고, 재촬영 후 전송"""
        self.click_element(self.bottom_locs.TAKE_PHOTO_BTN)  # 첫 촬영
        self.click_element(self.bottom_locs.TAKE_PHOTO_RETRY_BTN)  # 다시시도 버튼
        self.click_element(self.bottom_locs.TAKE_PHOTO_BTN)  # 재촬영
        self.click_element(self.bottom_locs.TAKE_PHOTO_CONFIRM_BTN)  # 확인 버튼


    def image_alert_yes_tap(self):
        """사진 보내기 모달창에서 '예' 터치"""
        self.find_element(self.bottom_locs.IMAGE_ALERT) # 모달창 확인
        self.find_element(self.bottom_locs.IMAGE_ALERT_TITLE) # 사진보내기 타이틀 확인
        self.click_element(self.bottom_locs.IMAGE_ALERT_YES_BTN) # 예 버튼 터치


    def image_alert_no_tap(self):
        """사진 보내기 모달창에서 '아니오' 터치"""
        self.find_element(self.bottom_locs.IMAGE_ALERT)
        self.find_element(self.bottom_locs.IMAGE_ALERT_TITLE)
        self.click_element(self.bottom_locs.IMAGE_ALERT_NO_BTN) # 아니오 버튼 터치


    def search_user_input_and_btn(self, user_name, icon_locator, input_locator, btn_locator):
        """바텀시트 아이콘 선택-> 사용자 검색창 입력-> 검색버튼 터치"""
        self.tap_bottom_icon(user_name, icon_locator)
        self.send_keys(input_locator, user_name)
        self.click_element(btn_locator)


    def share_user_profile_dm(self, user_name, icon_locator, btn_locator):
        """사용자 프로필 공유-> 1:1 채팅하기 터치"""
        self.search_user_input_and_btn(user_name, icon_locator, btn_locator)
        self.click_element(self.bottom_locs.FROFILE_SHARE_ALERT_SEND_BTN)
        self.click_element(self.bottom_locs.PROFILE_DM_BTN)


    def share_user_profile_view(self, user_name, icon_locator, btn_locator):
        """사용자 프로필 공유-> 프로필 보기 터치"""
        self.search_user_input_and_btn(user_name, icon_locator, btn_locator)
        self.click_element(self.bottom_locs.FROFILE_SHARE_ALERT_SEND_BTN)
        self.click_element(self.bottom_locs.VIEW_PROFILE_BTN)


    def search_package_input_and_btn(self, user_name, icon_locator, input_locator, text, btn_locator):
        """바텀시트 아이콘 선택-> 패키지 검색창 입력-> 검색버튼 터치"""
        self.tap_bottom_icon(user_name, icon_locator)
        self.send_keys(input_locator, text)
        self.click_element(btn_locator)


    def package_share_alert_view(self, user_name, icon_locator, input_locator, text, btn_locator):
        self.search_package_input_and_btn(self, user_name, icon_locator, input_locator, text, btn_locator)
        self.click_element(self.bottom_locs.package_share_btn(text))
        self.find_element(self.bottom_locs.PACKAGE_SHARE_ALERT)


    def package_alert_send_tap(self, user_name, icon_locator, text, btn_locator):
        """패키지 공유하기 모달창에서 '보내기' 터치"""
        self.search_package_input_and_btn(user_name, user_name, icon_locator, text, btn_locator)
        self.click_element(self.bottom_locs.package_share_btn(text))
        self.click_element(self.bottom_locs.PACKAGE_SHARE_ALERT_SEND_BTN) # 보내기 버튼 터치


    def package_alert_cancle_tap(self, user_name, icon_locator, text, btn_locator):
        """패키지 공유하기 모달창에서 '취소' 터치"""
        self.search_package_input_and_btn(user_name, user_name, icon_locator, text, btn_locator)
        self.click_element(self.bottom_locs.package_share_btn(text))
        self.click_element(self.bottom_locs.PACKAGE_SHARE_ALERT_SEND_BTN) # 보내기 버튼 터치


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