import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from src.pages.Chatting import Chatting
from utils.locators.ChattingLocator import ChattingTabLocator, ChatRoomLocator, BottomSheetLocators
from resources.testdata.test_data import chat_users, data_package, input_text, data_location
import time

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP01:

    def test_tp_01_01(self, login_driver: WebDriver, request): # 채팅 탭 진입 확인
        chatting = Chatting(login_driver)
        tab_locs = ChattingTabLocator()

        try:
            chatting.go_to_chatting_tap()
        
            selected_status = chatting.get_attribute(tab_locs.ICON, 'selected')
            
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
            chatting.go_to_chat_room()
        
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
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.go_to_chat_room(user_name)

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방 타이틀 미노출'

            for ui_check in cr_locs.UI_CHECK_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            chatting.logger.info("✔ 채팅방 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_01_05(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        tab_locs = ChattingTabLocator()
        cr_locs = ChatRoomLocator()

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

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP02:
    def test_tp_02_01(self, login_driver: WebDriver, request): # 채팅 입력창 미 입력 테스트
        chatting = Chatting(login_driver)
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.go_to_chat_room(user_name)

            send_btn = chatting.find_element(cr_locs.MESSAGE_SEND_BTN)
            is_enabled = send_btn.get_attribute("enabled")
            assert is_enabled == "false", "✖ 채팅창 미입력 시 보내기 버튼 활성화됨"

            chatting.logger.info("✔ 채팅창 미입력 시 보내기 버튼 비활성화 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise

@pytest.mark.blocked
@pytest.mark.usefixtures("login_driver")
class TestTP03:
    def test_tp_03_01(self, login_driver: WebDriver, request): # 채팅 입력 테스트
        chatting = Chatting(login_driver)
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]
        text = input_text["text"]

        try:
            chatting.go_to_chat_room(user_name)

            chatting.driver.hide_keyboard()
            # chatting.find_element(cr_locs.MESSAGE_INPUT)
            time.sleep(1)  # 포커스 주고 약간 대기, 안하면 오류뜸..
            chatting.send_keys(cr_locs.MESSAGE_INPUT, text)

            selected_status = chatting.get_attribute(cr_locs.MESSAGE_SEND_BTN, 'enabled')
            
            assert selected_status == 'true', '✖ 채팅창 입력 시 보내기 버튼 비활성화됨'

            chatting.logger.info("✔ 채팅창 입력 시 보내기 버튼 활성화 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    @pytest.mark.parametrize("text_key", ["text", "long_text"])
    def test_tp_03_02_03(self, login_driver: WebDriver, request, text_key):  # 일반/긴 메시지 전송
        chatting = Chatting(login_driver)
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]
        text = input_text[text_key]

        try:
            chatting.go_to_chat_room(user_name)

            chatting.driver.hide_keyboard()
            chatting.find_element(cr_locs.MESSAGE_INPUT)
            time.sleep(1)  # 포커스 대기

            chatting.send_keys(cr_locs.MESSAGE_INPUT, text)

            selected_status = chatting.get_attribute(cr_locs.MESSAGE_SEND_BTN, 'enabled')
            assert selected_status == 'true', f'✖ "{text_key}" 입력 시 보내기 버튼 비활성화됨'
            chatting.logger.info(f'✔ "{text_key}" 입력 시 보내기 버튼 활성화 확인')

            chatting.click_element(cr_locs.MESSAGE_SEND_BTN)

            message_check = chatting.find_element(cr_locs.chat_message_check(text))
            assert message_check.is_displayed(), f'✖ "{text_key}" 메시지 전송 실패'
            chatting.logger.info(f'✔ "{text_key}" 메시지 전송 확인')

        except Exception as e:
            chatting.logger.error(f'✖ 테스트 실패 ({text_key}): {e}')
            chatting.save_screenshot(request.node.name)
            raise



# class TestTP04 마지막 메시지 시간정보 확인 요소가 없어서 자동화 불가
# class TestTP05 안 읽은 메시지 알림 요소가 없어서 자동화 불가
# class TestTP06 채팅방 좌측 프로필 이미지 요소가 없어서 자동화 불가
# class TestTP07 최근순 정렬 자동화 불가


@pytest.mark.blocked(reason='스와이프 기능 구현해보려했으나 임포트 안됨...')
@pytest.mark.usefixtures("login_driver")
class TestTP08: 
    def test_tp_08_01(self, login_driver: WebDriver, request): # 채팅방 나가기 스와이프
        chatting = Chatting(login_driver)
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.go_to_chatting_tap()

            chat_element  = chatting.find_element(cr_locs.chat_room_profile(user_name))
            chatting.swipe_left(chat_element)

            exit_alert = chatting.find_element(cr_locs.EXIT_ALERT)

            assert exit_alert.is_displayed(), '✖ 채팅방 나가기 모달창 미노출'
            
            chatting.logger.info("✔ 채팅방 나가기 모달창 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP09:
    def test_tp_09_01(self, login_driver: WebDriver, request): # 채팅방  '+' 바텀 시트 UI 요소 확인
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        try:
            chatting.tap_plus_button(user_name)

            for ui_check in bottom_locs.UI_CHECK_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 아이콘 미노출'

            chatting.logger.info("✔ 바텀시트 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_09_02(self, login_driver: WebDriver, request): # 갤러리 로컬 이미지 전송
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.GALLERY_ICON)

            chatting.click_element(bottom_locs.LOCAL_IMAGE)

            chatting.image_alert_yes_tap()

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방 타이틀 미노출'

            chatting.logger.info("✔ 갤러리-사진전송 후 채팅방 복귀 성공 - 이미지는 수동 확인 필요")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_09_03(self, login_driver: WebDriver, request): # 갤러리 로컬 이미지 전송취소
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.GALLERY_ICON)

            chatting.click_element(bottom_locs.LOCAL_IMAGE)

            chatting.image_alert_no_tap()

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방 화면 미노출'

            chatting.logger.info("✔ 채팅방 화면 노출 확인 ")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP10: 
    def test_tp_10_01(self, login_driver: WebDriver, request): # 카메라 촬영 이미지 전송
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.CAMERA_ICON)

            chatting.take_photo()

            chatting.image_alert_yes_tap()

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방 화면 미노출'

            chatting.logger.info("✔ 채팅방 화면 노출 확인 ")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_10_02(self, login_driver: WebDriver, request): # 카메라 재촬영 이미지 전송
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.CAMERA_ICON)

            chatting.take_and_send_photo_with_retry()

            chatting.image_alert_yes_tap()

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방 타이틀 미노출'

            chatting.logger.info("✔ 카메라-재촬영 사진전송 후 채팅방 복귀 성공 - 이미지는 수동 확인 필요")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_10_03(self, login_driver: WebDriver, request): # 카메라 이미지 전송취소
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.CAMERA_ICON)

            chatting.take_photo()

            chatting.image_alert_no_tap()

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방 화면 미노출'

            chatting.logger.info("✔ 채팅방 화면 노출 확인 ")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP11: 
    def test_tp_11_01(self, login_driver: WebDriver, request): # 사용자 화면 UI 요소 확인
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.USER_ICON)

            for ui_check in bottom_locs.USER_UI_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            chatting.logger.info("✔ 시용자 화면 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_11_02(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.USER_ICON)
            chatting.click_element(bottom_locs.BACK_BTN_USER)

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅 목록으로 복귀 실패'
            
            chatting.logger.info("✔ 채팅목록 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    @pytest.mark.parametrize(
    "search_key, search_value",
    [
        ("user_name", chat_users["user_name"]),
        ("email", chat_users["email"])
    ])
    def test_tp_11_03_04(self, login_driver: WebDriver, search_key: str, search_value: str, request): # 사용자 검색창 입력 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        try:
            chatting.tap_bottom_icon(chat_users["user_name"], bottom_locs.USER_ICON)

            chatting.find_element(bottom_locs.SEARCH_INPUT_USER)
            time.sleep(0.3)  # 포커스 주고 약간 대기
            chatting.send_keys(bottom_locs.SEARCH_INPUT_USER, search_value)

            chatting.click_element(bottom_locs.SEARCH_BTN_USER)

            profile = chatting.find_element(bottom_locs.search_user_profile(search_value))
            assert profile.is_displayed(), f"✖ {search_key} 검색 실패"

            chatting.logger.info(f"✔ {search_key} 검색 -> 사용자 프로필 카드 노출 성공")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP12: 
    def test_tp_12_01(self, login_driver: WebDriver, request): # 프로필 정보 미리보기 모달창 확인
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        email = chat_users["email"]

        try:
            chatting.search_user_input_and_btn(user_name, bottom_locs.USER_ICON)

            chatting.click_element(bottom_locs.search_user_profile_share_btn(user_name, email))

            for ui_check in bottom_locs.USER_SHARE_ALERT_UI_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            profile_user_name = chatting.find_element(bottom_locs.share_alert_user_name(user_name))
            assert profile_user_name.is_displayed(), f'✖ 사용자 이름 미노출'

            profile_email = chatting.find_element(bottom_locs.share_alert_email(email))
            assert profile_email.is_displayed(), f'✖ 사용자 이메일 미노출'

            chatting.logger.info("✔ 프로필 정보 미리보기 모달창 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP13: 
    def test_tp_13_01(self, login_driver: WebDriver, request): # 사용자 프로필 공유하기 모달창 취소버튼
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        email = chat_users["email"]

        try:
            chatting.user_alert_cancle_tap(user_name, bottom_locs.USER_ICON, email)

            title = chatting.find_element(bottom_locs.USER_TITLE)
            assert title.is_displayed(), '✖ 사용자 검색 화면 미노출'
            
            chatting.logger.info("✔ 사용자 검색 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_13_02(self, login_driver: WebDriver, request): # 사용자 프로필 미리보기 모달창 보내기버튼
        chatting = Chatting(login_driver)
        cr_locs = ChatRoomLocator()
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        email = chat_users["email"]

        try:
            chatting.user_alert_send_tap(user_name, bottom_locs.USER_ICON, email)

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방 화면 미노출'

            message = chatting.find_element(bottom_locs.share_user_message_check(user_name, email))
            assert message.is_displayed(), '✖ 공유한 사용자 프로필 메시지 미노출'
            
            chatting.logger.info("✔ 공유한 사용자 프로필 메시지 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP14: 
    def test_tp_14_01(self, login_driver: WebDriver, request): # 사용자 공유 후 1:1 채팅하기
        chatting = Chatting(login_driver)
        cr_locs = ChatRoomLocator()
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        email = chat_users["email"]

        try:
            chatting.user_alert_send_tap(user_name, bottom_locs.USER_ICON, email)

            chatting.click_element(bottom_locs.PROFILE_DM_BTN)

            title = chatting.click_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), f'✖ {user_name} 1:1 채팅방 미노출'
            
            chatting.logger.info(f"✔ {user_name} 1:1 채팅방 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP15: 
    def test_tp_15_01(self, login_driver: WebDriver, request): # 사용자 공유 후 프로필 화면으로 이동
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        email = chat_users["email"]

        try:
            chatting.user_alert_send_tap(user_name, bottom_locs.USER_ICON, email)

            chatting.click_element(bottom_locs.VIEW_PROFILE_BTN)

            title = chatting.find_element(bottom_locs.view_profile_title(user_name))
            assert title.is_displayed(), f'✖ {user_name}의 프로필 화면 미노출'
            
            chatting.logger.info(f"✔ {user_name}의 프로필 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP16: 
    def test_tp_16_01(self, login_driver: WebDriver, request): # 패키지 화면 UI 요소 확인
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.PACKAGE_ICON)

            for ui_check in bottom_locs.PACKAGE_UI_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            chatting.logger.info("✔ 패키지 화면 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_16_02(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.PACKAGE_ICON)
            chatting.click_element(bottom_locs.BACK_BTN_PACKAGE)

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅 목록으로 복귀 실패'
            
            chatting.logger.info("✔ 채팅목록 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise

    def test_tp_16_03(self, login_driver: WebDriver, request): # 패키지 검색창 정상이름 입력 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        package_name = data_package["package_name"]

        try:
            chatting.search_package_input_and_btn(user_name, bottom_locs.PACKAGE_ICON, package_name)

            results = chatting.find_elements(bottom_locs.PACKAGE_LIST)
            
            assert len(results) > 0, f"✖ {package_name} 검색 -> 패키지 목록 미노출"

            chatting.logger.info(f"✔ {package_name} 검색 -> 패키지 목록 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_16_04(self, login_driver: WebDriver, request): # 패키지 검색창 의미없는 문자열 입력 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        invaild_text = data_package["invaild_text"]

        try:
            chatting.search_package_input_and_btn(user_name, bottom_locs.PACKAGE_ICON, package_name=invaild_text)

            try:
                results = chatting.find_elements(bottom_locs.PACKAGE_LIST)
            except TimeoutException:
                results = []  # 요소가 없으면 빈 리스트로 처리

            assert len(results) == 0, f"✖ {invaild_text} 검색 -> 패키지 목록 노출"
            chatting.logger.info(f"✔ 유효하지않은 {invaild_text} 검색 -> 패키지 목록 미노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            
            chatting.save_screenshot(request.node.name)
            raise


#16_05~07 자동화 불가


    def test_tp_16_08(self, login_driver: WebDriver, request): # 패키지 공유 버튼 터치시 모달창 노출
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        package_name = data_package["package_name"]

        try:
            chatting.package_share_alert_view(user_name, bottom_locs.PACKAGE_ICON, package_name)

            alert = chatting.find_element(bottom_locs.PACKAGE_SHARE_ALERT)
            
            assert alert.is_displayed(), f"✖ 패키지 미리보기 모달창 미노출"

            chatting.logger.info(f"✔ 패키지 미리보기 모달창 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_16_09(self, login_driver: WebDriver, request): # 패키지 미리보기 모달창 UI 요소 확인
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        package_name = data_package["package_name"]

        try:
            chatting.package_share_alert_view(user_name, bottom_locs.PACKAGE_ICON, package_name)

            for ui_check in bottom_locs.PACKAGE_ALERT_UI_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            chatting.logger.info("✔ 패키지 공유하기 모달창 UI 요소 노출 확인")
            
        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_16_10(self, login_driver: WebDriver, request): # 패키지 모달창 취소 버튼 터치
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        package_name = data_package["package_name"]

        try:
            chatting.package_share_alert_view(user_name, bottom_locs.PACKAGE_ICON, package_name)

            chatting.click_element(bottom_locs.PACKAGE_SHARE_ALERT_CANCEL_BTN)

            title = chatting.find_element(bottom_locs.PACKAGE_TITLE)
            
            assert title.is_displayed(), f"✖ 패키지 찾기 화면 미노출"

            chatting.logger.info(f"✔ 패키지 찾기 화면 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_16_11(self, login_driver: WebDriver, request): # 패키지 모달창 보내기 버튼 터치
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        package_name = data_package["package_name"]

        try:
            chatting.package_share_alert_view(user_name, bottom_locs.PACKAGE_ICON, package_name)

            chatting.click_element(bottom_locs.PACKAGE_SHARE_ALERT_SEND_BTN)

            message = chatting.find_element(bottom_locs.share_package_message(package_name))
            
            assert message.is_displayed(), f"✖ 패키지 요약정보 메시지 미노출"

            chatting.logger.info(f"✔ 패키지 요약정보 메시지 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP17: 
    def test_tp_17_01(self, login_driver: WebDriver, request): # 패키지 상세 정보 화면 이동
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        package_name = data_package["package_name"]

        try:
            chatting.go_to_package_detail(user_name, bottom_locs.PACKAGE_ICON, package_name)

            title = chatting.click_element(bottom_locs.VIEW_PACKAGE_DETAIL_TITLE)
            
            assert title.is_displayed(), f"✖ 패키지 상세 정보 화면 미노출"

            chatting.logger.info(f"✔ 패키지 상세 정보 화면 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


@pytest.mark.wip
@pytest.mark.usefixtures("login_driver")
class TestTP18: 
    def test_tp_18_01(self, login_driver: WebDriver, request): # 지도 화면 UI 요소 확인
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.MAP_ICON)

            for ui_check in bottom_locs.MAP_UI_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            chatting.logger.info("✔ 지도 화면 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_18_02(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.MAP_ICON)
            chatting.click_element(bottom_locs.BACK_BTN_MAP)

            title = chatting.find_element(cr_locs.chat_room_title)
            assert title.is_displayed(), '✖ 채팅 목록으로 복귀 실패'
            
            chatting.logger.info("✔ 채팅목록 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_tp_18_03(self, login_driver: WebDriver, request): # 지도 검색창 입력 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        location = data_package["location_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.MAP_ICON)

            chatting.send_keys(bottom_locs.SEARCH_INPUT_MAP, location)
            chatting.click_element(bottom_locs.SEARCH_BTN_MAP)

            results = chatting.find_elements(bottom_locs.MAP_EMPTY_LIST)
            
            assert len(results) < 1, f"✖ {location} 검색 -> 장소 목록 노출"

            chatting.logger.info(f"✔ {location} 검색 -> 장소 목록 미노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise