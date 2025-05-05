import pytest
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from src.pages.Chatting import Chatting
from utils.locators.ChattingLocator import ChattingTabLocator, ChatRoomLocator, BottomSheetLocators
from resources.testdata.test_data import chat_users, data_package, input_text, data_location
import time

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestCP01:

    def test_cp_01_01(self, login_driver: WebDriver, request): # 채팅 탭 진입 확인
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


    def test_cp_01_02(self, login_driver: WebDriver, request): # 채팅 탭 UI요소 확인
        chatting = Chatting(login_driver)
        tab_locs = ChattingTabLocator()

        try:
            chatting.go_to_chatting_tap()

            for ui_check in tab_locs.TAB_CHECK_UI:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            chatting.logger.info("✔ 채팅 탭 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


#test_cp_01_03 은 자동화 불가


    def test_cp_01_04(self, login_driver: WebDriver, request): # 채팅방 UI요소 확인
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


    def test_cp_01_05(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        tab_locs = ChattingTabLocator()

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
class TestCP02:
    def test_cp_02_01(self, login_driver: WebDriver, request): # 채팅 입력창 미 입력 테스트
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
class TestCP03:
    def test_cp_03_01(self, login_driver: WebDriver, request): # 채팅 입력 테스트
        chatting = Chatting(login_driver)
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]
        text = input_text["text"]

        try:
            chatting.go_to_chat_room(user_name)

            chatting.driver.hide_keyboard()
            chatting.find_element(cr_locs.MESSAGE_INPUT)
            time.sleep(5)  # 약간 대기, 안하면 오류메시지 때문에 오류뜸..
            chatting.send_keys(cr_locs.MESSAGE_INPUT, text)

            selected_status = chatting.get_attribute(cr_locs.MESSAGE_SEND_BTN, 'enabled')
            
            assert selected_status == 'true', '✖ 채팅창 입력 시 보내기 버튼 비활성화됨'

            chatting.logger.info("✔ 채팅창 입력 시 보내기 버튼 활성화 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    @pytest.mark.parametrize("text_key", ["text", "long_text"])
    def test_cp_03_02_03(self, login_driver: WebDriver, request, text_key):  # 일반/긴 메시지 전송
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



# class TestCP04 마지막 메시지 시간정보 확인 요소가 없어서 자동화 불가
# class TestCP05 안 읽은 메시지 알림 요소가 없어서 자동화 불가
# class TestCP06 채팅방 좌측 프로필 이미지 요소가 없어서 자동화 불가
# class TestCP07 최근순 정렬 자동화 불가


@pytest.mark.blocked(reason='스와이프 기능 구현해보려했으나 임포트 안됨...')
@pytest.mark.usefixtures("login_driver")
class TestCP08:
    @pytest.mark.skip(reason='자동화 실패')
    def test_cp_08_01(self, login_driver: WebDriver, request): # 채팅방 나가기 스와이프
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
class TestCP09:
    def test_cp_09_01(self, login_driver: WebDriver, request): # 채팅방  '+' 바텀 시트 UI 요소 확인
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


    def test_cp_09_02(self, login_driver: WebDriver, request): # 갤러리 로컬 이미지 전송
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


    def test_cp_09_03(self, login_driver: WebDriver, request): # 갤러리 로컬 이미지 전송취소
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
class TestCP10: 
    def test_cp_10_01(self, login_driver: WebDriver, request): # 카메라 촬영 이미지 전송
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

            chatting.logger.info("✔ 채팅방 화면 노출 확인 - 이미지는 수동 확인 필요")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_cp_10_02(self, login_driver: WebDriver, request): # 카메라 재촬영 이미지 전송
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


    def test_cp_10_03(self, login_driver: WebDriver, request): # 카메라 이미지 전송취소
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
class TestCP11: 
    def test_cp_11_01(self, login_driver: WebDriver, request): # 사용자 화면 UI 요소 확인
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


    def test_cp_11_02(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.USER_ICON)
            chatting.click_element(bottom_locs.BACK_BTN_USER)

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방으로 복귀 실패'
            
            chatting.logger.info("✔ 채팅방 화면 노출 확인")

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
    def test_cp_11_03_04(self, login_driver: WebDriver, search_key: str, search_value: str, request): # 사용자 검색창 입력 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        try:
            chatting.tap_bottom_icon(chat_users["user_name"], bottom_locs.USER_ICON)

            chatting.find_element(bottom_locs.SEARCH_INPUT_USER)
            # time.sleep(0.3)  # 포커스 주고 약간 대기
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
class TestCP12: 
    def test_cp_12_01(self, login_driver: WebDriver, request): # 프로필 정보 미리보기 모달창 확인
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
class TestCP13: 
    def test_cp_13_01(self, login_driver: WebDriver, request): # 사용자 프로필 공유하기 모달창 취소버튼
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


    def test_cp_13_02(self, login_driver: WebDriver, request): # 사용자 프로필 미리보기 모달창 보내기버튼
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
class TestCP14: 
    def test_cp_14_01(self, login_driver: WebDriver, request): # 사용자 공유 후 1:1 채팅하기
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
class TestCP15: 
    def test_cp_15_01(self, login_driver: WebDriver, request): # 사용자 공유 후 프로필 화면으로 이동
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
class TestCP16: 
    def test_cp_16_01(self, login_driver: WebDriver, request): # 패키지 화면 UI 요소 확인
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


    def test_cp_16_02(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.PACKAGE_ICON)
            chatting.click_element(bottom_locs.BACK_BTN_PACKAGE)

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방으로 복귀 실패'
            
            chatting.logger.info("✔ 채팅방 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise

    def test_cp_16_03(self, login_driver: WebDriver, request): # 패키지 검색창-정상이름 입력 테스트
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


    def test_cp_16_04(self, login_driver: WebDriver, request): # 패키지 검색창-의미없는 문자열 입력 테스트
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


#test_cp_16_05~07 자동화 불가


    def test_cp_16_08(self, login_driver: WebDriver, request): # 패키지 공유 버튼 터치시 모달창 노출
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


    def test_cp_16_09(self, login_driver: WebDriver, request): # 패키지 미리보기 모달창 UI 요소 확인
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


    def test_cp_16_10(self, login_driver: WebDriver, request): # 패키지 모달창 취소 버튼 터치
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


    def test_cp_16_11(self, login_driver: WebDriver, request): # 패키지 모달창 보내기 버튼 터치
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
class TestCP17: 
    def test_cp_17_01(self, login_driver: WebDriver, request): # 패키지 상세 정보 화면 이동
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


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestCP18: 
    def test_cp_18_01(self, login_driver: WebDriver, request): # 지도 화면 UI 요소 확인
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


    def test_cp_18_02(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]

        try:
            chatting.tap_bottom_icon(user_name, bottom_locs.MAP_ICON)
            chatting.click_element(bottom_locs.BACK_BTN_MAP)

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방으로 복귀 실패'
            
            chatting.logger.info("✔ 채팅방 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise

    
    def test_cp_18_03(self, login_driver: WebDriver, request): # 존재하지 않는 장소 입력 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        not_exist_name = data_location["not_exist_name"]

        try:
            chatting.search_map_input_and_btn(user_name, bottom_locs.MAP_ICON, location_name=not_exist_name)

            try:
                results = chatting.find_elements(bottom_locs.MAP_LIST)
            except TimeoutException:
                results = []  # 요소가 없으면 빈 리스트로 처리
            
            assert len(results) == 0, f"✖ {not_exist_name} 검색 -> 장소 목록 노출"

            chatting.logger.info(f"✔ {not_exist_name} 검색 -> 장소 목록 미노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_cp_18_04(self, login_driver: WebDriver, request): # 지도 검색창 잘못된 형식 입력 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        invaild_text = data_location["invaild_text"]

        try:
            chatting.search_map_input_and_btn(user_name, bottom_locs.MAP_ICON, location_name=invaild_text)

            toast_message = chatting.find_element(bottom_locs.MAP_SEARCH_ERROR_TOAST)
            
            assert toast_message.is_displayed(), f"✖ {invaild_text} 검색 -> 하단에 오류 안내 Toast 메시지 미노출"

            chatting.logger.info(f"✔ {invaild_text} 검색 -> 하단에 오류 안내 Toast 메시지 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_cp_18_05(self, login_driver: WebDriver, request): # 지도 검색창 정상 이름 입력
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        location_name = data_location["location_name"]

        try:
            chatting.search_map_input_and_btn(user_name, bottom_locs.MAP_ICON, location_name)

            result = chatting.find_element(bottom_locs.searched_map(location_name))
            
            assert result.is_displayed(), f"✖ {location_name} 검색 -> 검색 조건에 맞는 장소 미노출"

            chatting.logger.info(f"✔ {location_name} 검색 -> 검색 조건에 맞는 장소 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_cp_18_06(self, login_driver: WebDriver, request): # 지도 공유하기 모달창
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        location_name = data_location["location_name"]
        location_address = data_location["location_address"]

        try:
            chatting.search_map_input_and_btn(user_name, bottom_locs.MAP_ICON, location_name)

            chatting.click_element(bottom_locs.map_share_btn(location_name, location_address))

            alert = chatting.find_element(bottom_locs.MAP_SHARE_ALERT)
            
            assert alert.is_displayed(), f"✖ 지도 공유하기 모달창 미노출"

            chatting.logger.info(f"✔ 지도 공유하기 모달창 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_cp_18_07(self, login_driver: WebDriver, request): # 장소 공유하기 모달창 UI 요소 확인
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        location_name = data_location["location_name"]
        location_address = data_location["location_address"]

        try:
            chatting.map_share_alert_view(user_name, bottom_locs.MAP_ICON, location_name, location_address)

            for ui_check in bottom_locs.MAP_ALERT_UI_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            name = chatting.find_element(bottom_locs.share_alert_location_name(location_name))
            assert name.is_displayed(), f'✖ 장소 이름 미노출'

            address = chatting.find_element(bottom_locs.share_alert_location_address(location_address))
            assert address.is_displayed(), f'✖ 장소 주소 미노출'

            chatting.logger.info("✔ 장소 공유하기 모달창 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_cp_18_08(self, login_driver: WebDriver, request): # 지도 공유하기 모달창 '취소' 터치
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        location_name = data_location["location_name"]
        location_address = data_location["location_address"]

        try:
            chatting.map_share_alert_view(user_name, bottom_locs.MAP_ICON, location_name, location_address)

            chatting.click_element(bottom_locs.MAP_SHARE_ALERT_CANCEL_BTN)

            title = chatting.find_element(bottom_locs.MAP_TITLE)
            
            assert title.is_displayed(), f"✖ 장소 검색 화면 미노출"

            chatting.logger.info(f"✔ 장소 검색 화면 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_cp_18_09(self, login_driver: WebDriver, request): # 지도 공유하기 모달창 '공유하기' 터치
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        location_name = data_location["location_name"]
        location_address = data_location["location_address"]

        try:
            chatting.map_share_alert_view(user_name, bottom_locs.MAP_ICON, location_name, location_address)

            chatting.click_element(bottom_locs.MAP_SHARE_ALERT_SEND_BTN)

            message = chatting.find_element(bottom_locs.share_map_message(location_name))
            
            assert message.is_displayed(), f"✖ 장소 정보 공유 메시지 미노출"

            chatting.logger.info(f"✔ 장소 정보 공유 메시지 노출")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


#TestCP19는 자동화 불가


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestCP20: 
    def test_cp_20_01(self, login_driver: WebDriver, request): # 위치 상세 정보 화면 UI 요소 확인
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()

        user_name = chat_users["user_name"]
        location_name = data_location["location_name"]
        location_address = data_location["location_address"]

        try:
            chatting.go_to_map_detail(user_name, bottom_locs.MAP_ICON, location_name, location_address)

            for ui_check in bottom_locs.MAP_DETAIL_UI_LOCS:
                assert chatting.find_element(ui_check).is_displayed(), f'✖ {ui_check} 미노출'

            icon = chatting.find_element(bottom_locs.location_name_icon(location_name))
            assert icon.is_displayed(), f'✖ 장소 이름 아이콘 미노출'

            chatting.logger.info("✔ 위치 상세 정보 화면 UI 요소 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise


    def test_cp_20_02(self, login_driver: WebDriver, request): # '←'(뒤로가기) 버튼 테스트
        chatting = Chatting(login_driver)
        bottom_locs = BottomSheetLocators()
        cr_locs = ChatRoomLocator()

        user_name = chat_users["user_name"]
        location_name = data_location["location_name"]
        location_address = data_location["location_address"]

        try:
            chatting.go_to_map_detail(user_name, bottom_locs.MAP_ICON, location_name, location_address)

            chatting.click_element(bottom_locs.BACK_BTN_MAP_DETAIL)

            title = chatting.find_element(cr_locs.chat_room_title(user_name))
            assert title.is_displayed(), '✖ 채팅방으로 복귀 실패'
            
            chatting.logger.info("✔ 채팅방 화면 노출 확인")

        except Exception as e:
            chatting.logger.error(f"✖ 테스트 실패: {e}")
            chatting.save_screenshot(request.node.name)
            raise