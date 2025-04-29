from src.pages.Register import Register
from src.utils.locators import RegisterLocator
import time
import pytest

class TestLR02:
    def test_lr_02_01(self, driver, request): # 로그인 페이지에서 회원가입 버튼 클릭
        try:
            register = Register(driver)
            register.click_element(RegisterLocator.REGISTER_BTN)
            register_tab = register.find_element(RegisterLocator.REGISTER_TAB)
        except Exception as e:
            register.logger.info(f"테스트 실패: {e}")
            register.save_screenshot(request.node.name)
            assert False, f"테스트 실패"
        assert register_tab.is_displayed(), f"회원가입 탭이 보이지 않는 상태."
    
    def test_lr_02_02(self, driver, request): # 회원가입 탭 - 상단 UI - 뒤로가기 버튼 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            register_tab = register.find_element(RegisterLocator.REGISTER_TAB)
        except Exception as e:
            register.logger.info(f"테스트 실패: {e}")
            register.save_screenshot(request.node.name)
            assert False, f"테스트 실패"
        assert register_tab.is_displayed(), f"회원가입 탭이 보이지 않는 상태."

    def test_lr_02_03(self, driver, request): # 회원가입 탭 - 상단 UI - 타이틀 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            title_element = register.find_element(RegisterLocator.TITLE)
            title_text = title_element.get_attribute("content-desc")
        except Exception as e:
            register.logger.info(f"테스트 실패: {e}")
            register.save_screenshot(request.node.name)
            raise
        assert title_text == "회원가입", f"타이틀 명이 다름. 현재 타이틀 : {title_text}"

    def test_lr_02_04(self, driver, request): # 회원가입 탭 - 입력란 - 닉네임 입력란 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            a = register.find_by_hint(RegisterLocator.TEXT_INPUT, "닉네임")
        except Exception as e:
            register.logger.info(f"테스트 실패: {e}")
            register.save_screenshot(request.node.name)
            raise

    def test_lr_02_05(self, driver, request): # 회원가입 탭 - 입력란 - 이메일 아이디 입력란 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            a = register.find_by_hint(RegisterLocator.TEXT_INPUT, "이메일 아이디")
        except Exception as e:
            register.logger.info(f"테스트 실패: {e}")
            register.save_screenshot(request.node.name)
            raise