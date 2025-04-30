import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from src.pages.Chatting import Chatting
from utils.locators import ChattingLocator


@pytest.mark.usefixtures("login_driver")
class TestTP01:
    @pytest.mark.skip()
    def test_tp_01_01(self, login_driver: WebDriver, request): # 채팅 탭 진입

        chatting = Chatting(login_driver)
        chatting.into_chatting_tap()
    
        chat_tab_element = chatting.find_element(ChattingLocator.CHATTING_TAB_ICON)
        selected_status = chat_tab_element.get_attribute('selected')
        assert selected_status == 'true', '❌ 채팅 탭 진입 실패'

        chatting.logger.info("✅ 채팅 탭 진입 성공")
        chatting.save_screenshot(request.node.name)


    # @pytest.mark.skip()
    def test_tp_01_02(self, login_driver: WebDriver, request): # 채팅 탭 UI요소 확인

        chatting = Chatting(login_driver)
        chatting.into_chatting_tap()
    
        title_element = chatting.find_element(ChattingLocator.CHATTING_TAB_TITLE)
        title = title_element.get_attribute('content-desc')
        assert title == '채팅 목록', '❌ 채팅 목록 타이틀이 보이지 않음'

        search_input = chatting.find_element(ChattingLocator.SEARCH_INPUT_CHAT)
        assert search_input.is_displayed(), '❌ 검색창 보이지 않음'

        search_btn = chatting.find_element(ChattingLocator.SEARCH_BTN_CHAT)
        assert search_btn.is_displayed(), '❌ 검색버튼이 보이지 않음'

        chatting.logger.info("✅ 채팅 탭 UI요소 확인")
        chatting.save_screenshot(request.node.name)