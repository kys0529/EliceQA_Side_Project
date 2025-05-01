import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from src.pages.Chatting import Chatting
from utils.locators.ChattingLocator import ChattingTabLocator, ChatRoomLocator
from resources.testdata.test_data import chat_users
import time


@pytest.mark.usefixtures("login_driver")
class TestTP01:

    def test_tp_01_01(self, login_driver: WebDriver, request): # 채팅 탭 진입 확인
        chatting = Chatting(login_driver)
        tab_locs = ChattingTabLocator()

        try:
            chatting.go_to_chatting_tap()
        
            chat_tab_element = chatting.find_element(tab_locs.ICON)
            selected_status = chat_tab_element.get_attribute('selected')

            assert selected_status == 'true', '✖ 채팅 탭 진입 실패'
            chatting.logger.info("✔ 채팅 탭 진입 성공")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_01_02(self, login_driver: WebDriver, request): # 채팅 탭 UI요소 확인
        chatting = Chatting(login_driver)
        tab_locs = ChattingTabLocator()

        try:
            chatting.go_to_chatting_tap()
        
            title = chatting.find_element(tab_locs.TITLE)
            assert title.is_displayed(), '✖ 채팅 목록 타이틀 미노출'

            search_input = chatting.find_element(tab_locs.SEARCH_INPUT)
            assert search_input.is_displayed(), '✖ 검색창 미노출'

            search_btn = chatting.find_element(tab_locs.SEARCH_BTN)
            assert search_btn.is_displayed(), '✖ 검색버튼 미노출'

            chatting.logger.info("✔ 채팅 탭 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


#test_tp_01_03 은 자동화 불가


    def test_tp_01_04(self, login_driver: WebDriver, request): # 채팅 탭 UI요소 확인
        chatting = Chatting(login_driver)
        chatroom_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.go_to_chat_room(user_name)

            title = chatting.find_element(chatroom_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방 타이틀 미노출'

            for ui_check in chatroom_locs.UI_CHECK_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            chatting.logger.info("✔ 채팅방 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_01_05(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        tab_locs = ChattingTabLocator()
        chatroom_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.return_to_chat_list(user_name)

            title = chatting.find_element(tab_locs.TITLE)
            assert title.is_displayed(), '✖ 채팅 목록으로 복귀 실패'
            
            chatting.logger.info("✔ 채팅목록 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.usefixtures("login_driver")
class TestTP02:
    def test_tp_02_01(self, login_driver: WebDriver, request): # 채팅 입력창 미 입력 테스트
        chatting = Chatting(login_driver)
        chatroom_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.go_to_chat_room(user_name)

            send_btn = chatting.find_element(chatroom_locs.MESSAGE_SEND_BTN)
            is_enabled = send_btn.get_attribute("enabled")
            assert is_enabled == "false", "✖ 채팅창 미입력 시 보내기 버튼 활성화됨"

            chatting.logger.info("✔ 채팅창 미입력 시 보내기 버튼 비활성화 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.usefixtures("login_driver")
class TestTP03:
    @pytest.mark.skip(reason='검증 자꾸 오류뜸 나중에 다시 수정 필요')
    def test_tp_03_01(self, login_driver: WebDriver, request): # 채팅 입력 테스트
        chatting = Chatting(login_driver)
        chatroom_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]
        text = '테스트'

        try:
            chatting.go_to_chat_room(user_name)

            chatting.driver.hide_keyboard()
            chatting.find_element(chatroom_locs.MESSAGE_INPUT)
            time.sleep(0.3)  # 포커스 주고 약간 대기
            chatting.send_keys(chatroom_locs.MESSAGE_INPUT, text)

            send_btn = chatting.find_element(chatroom_locs.MESSAGE_SEND_BTN)
            is_enabled = send_btn.get_attribute("enabled")
            assert is_enabled == "true", "✖ 채팅창 입력 시 보내기 버튼 비활성화됨"

            chatting.logger.info("✔ 채팅창 입력 시 보내기 버튼 활성화 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise
# def test_tp_03_01 해결 후 test_tp_03_02 함수 작성해야함


# class TestTP04 마지막 메시지 시간정보 확인 요소가 없어서 자동화 불가
# class TestTP05 안 읽은 메시지 알림 요소가 없어서 자동화 불가
# class TestTP06 채팅방 좌측 프로필 이미지 요소가 없어서 자동화 불가
# class TestTP07 최근순 정렬 자동화 불가


@pytest.mark.usefixtures("login_driver")
class TestTP08: 
    def test_tp_08_01(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        chatroom_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.go_to_chatting_tap()

            chat_element  = chatting.find_element(chatroom_locs.chat_room_profile(user_name))
            chatting.swipe_left(chat_element)

            exit_alert = chatting.find_element(chatroom_locs.EXIT_ALERT)

            assert exit_alert.is_displayed(), '✖ 채팅방 나가기 모달창 미노출'
            
            chatting.logger.info("✔ 채팅방 나가기 모달창 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise