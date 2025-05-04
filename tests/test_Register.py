from src.pages.Register import Register
from src.utils.locators import RegisterLocator
import time
import src.resources.testdata.test_data

class TestLR02: # 회원가입 탭 - 요소 확인

    def test_lr_02_01(self, driver, request): # 로그인 페이지에서 회원가입 버튼 클릭
        try:
            register = Register(driver)
            register.click_element(RegisterLocator.REGISTER_BTN)
            register_tab = register.find_element(RegisterLocator.REGISTER_TAB)
        except Exception as e:
            register.handle_exception(request, e)
        assert register_tab.is_displayed(), f"회원가입 탭이 보이지 않는 상태."
    
    def test_lr_02_02(self, driver, request): # 회원가입 탭 - 상단 UI - 뒤로가기 버튼 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            register_tab = register.find_element(RegisterLocator.REGISTER_TAB)
        except Exception as e:
            register.handle_exception(request, e)
        assert register_tab.is_displayed(), f"회원가입 탭이 보이지 않는 상태."

    def test_lr_02_03(self, driver, request): # 회원가입 탭 - 상단 UI - 타이틀 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            title_text = register.get_attribute(RegisterLocator.TITLE, "content-desc")
        except Exception as e:
            register.handle_exception(request, e)
        assert title_text == "회원가입", f"타이틀 명이 다름. 현재 타이틀 : {title_text}"

    def test_lr_02_04(self, driver, request): # 회원가입 탭 - 입력란 - 닉네임 입력란 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            nickname = register.find_by_hint(RegisterLocator.TEXT_INPUT, "닉네임")
        except Exception as e:
            register.handle_exception(request, e)
        assert nickname.is_displayed(), f"닉네임 입력란이 보이지 않는 상태."

    def test_lr_02_05(self, driver, request): # 회원가입 탭 - 입력란 - 이메일 아이디 입력란 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            email_ID = register.find_by_hint(RegisterLocator.TEXT_INPUT, "이메일 아이디")
        except Exception as e:
            register.handle_exception(request, e)
        assert email_ID.is_displayed(), f"이메일 아이디 입력란이 보이지 않는 상태."
    
    def test_lr_02_06(self, driver, request): # 회원가입 탭 - @ 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            at_mark = register.find_element(RegisterLocator.AT_MARK)
        except Exception as e:
            register.handle_exception(request, e)
        assert at_mark.is_displayed(), f"@가 보이지 않는 상태."

    def test_lr_02_07(self, driver, request): #회원가입 탭 - 입력란 - 비밀번호 입력란 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            password = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호")
        except Exception as e:
            register.handle_exception(request, e)
        assert password.is_displayed(), f"비밀번호 입력란이 보이지 않는 상태."
    
    def test_lr_02_08(self, driver, request): #회원가입 탭 - 비밀번호 보이기 버튼 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            password_visible_btn = register.find_element(RegisterLocator.PASSWORD_VISIBLE_BTN)
        except Exception as e:
            register.handle_exception(request, e)
        assert password_visible_btn.is_displayed(), f"비밀번호 보이기 버튼이 보이지 않는 상태."

    def test_lr_02_09(self, driver, request): #회원가입 탭 - 입력란 - 비밀번호 확인 입력란 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            password_confirm = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호 확인")
        except Exception as e:
            register.handle_exception(request, e)
        assert password_confirm.is_displayed(), f"비밀번호 확인 입력란이 보이지 않는 상태."

    def test_lr_02_10(self, driver, request): #회원가입 탭 - 비밀번호 확인 보이기 버튼 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            password_confirm_visible_btn = register.find_element(RegisterLocator.PASSWORD_CONFIRM_VISIBLE_BTN)
        except Exception as e:
            register.handle_exception(request, e)
        assert password_confirm_visible_btn.is_displayed(), f"비밀번호 확인 보이기 버튼이 보이지 않는 상태."

    def test_lr_02_11(self, driver, request): # 회원가입 탭 - 회원가입 버튼 확인
        try:            
            register = Register(driver)
            register.navigate_to_register(driver)
            register_btn = register.find_element(RegisterLocator.REGISTER_BTN)
        except Exception as e:
            register.handle_exception(request, e)
        assert register_btn.is_displayed(), f"회원가입 버튼이 보이지 않는 상태."

class TestLR03: # 회원가입 탭 - 기능 확인

    email_domain = ['naver.com', 'gmail.com', 'daum.net', '직접 입력'] # 이메일 도메인 리스트
    not_registered = {
        "user_name": "test",
        "email": "eliceqa123@gmail.com",
        "password": "!Elice123"
    }
    registered = {
        "user_name": "test",
        "email": "eliceqamade@gmail.com",
        "password": "123456"
    }
    def test_lr_03_01(self, driver, request): # 회원가입 탭 - 닉네임 입력란에 값 입력
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            nickname = register.find_by_hint(RegisterLocator.TEXT_INPUT, "닉네임")
            register.send_keys(nickname, "aa")
        except Exception as e:
            register.handle_exception(request, e)
        assert nickname.text == "aa", f"닉네임 입력란에 다르게 입력됨. 현재 입력된 값 : {nickname.text}"

    def test_lr_03_02(self, driver, request): # 회원가입 탭 - 이메일 아이디 입력란에 값 입력
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            email_ID = register.find_by_hint(RegisterLocator.TEXT_INPUT, "이메일 아이디")
            register.send_keys(email_ID, "test")
        except Exception as e:
            register.handle_exception(request, e)
        assert email_ID.text == "test", f"이메일 아이디 입력란에 다르게 입력됨. 현재 입력된 값 : {email_ID.text}"

    def test_lr_03_03(self,driver,request): # 회원가입 탭 - 이메일 도메인 기본값 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            naver_text = register.get_attribute(RegisterLocator.NAVER_BTN, "content-desc")
        except Exception as e:
            register.handle_exception(request, e)
        assert naver_text == "naver.com", f"이메일 도메인 기본값이 다르게 노출됨. 현재 입력된 값 : {naver_text}"

    def test_lr_03_04(self,driver,request): #회원가입 탭 - 이메일 도메인 드롭다운 버튼 클릭
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            email_dropdown = register.find_element(RegisterLocator.EMAIL_DROPDOWN_BTN)
            register.click_element(email_dropdown)
            menu_close = register.find_element(RegisterLocator.MENU_CLOSE)
            naver_text = register.get_attribute(RegisterLocator.NAVER_BTN, "content-desc")
            gmail_text = register.get_attribute(RegisterLocator.GMAIL_BTN, "content-desc")
            daum_text = register.get_attribute(RegisterLocator.DAUM_BTN, "content-desc")
            enter_manually_text = register.get_attribute(RegisterLocator.ENTER_MANUALLY_BTN, "content-desc")
            dropdown_elements = [naver_text, gmail_text, daum_text, enter_manually_text]
        except Exception as e:
            register.handle_exception(request, e)
        assert menu_close.is_displayed(), f"이메일 도메인 드롭다운 버튼 클릭 후 메뉴 닫기 요소가 등장하지 않는 상태."
        assert dropdown_elements == self.email_domain, f"이메일 도메인이 다르게 노출됨. 현재 노출된 값 : {dropdown_elements}"

    def test_lr_03_05(self, driver, request): # 회원가입 탭 - 비밀번호 입력란에 값 입력
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            password = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호")
            register.send_keys(password, "123456")
        except Exception as e:
            register.handle_exception(request, e)
        assert password.text == "••••••", f"비밀번호 입력란에 다르게 입력됨. 현재 입력된 값 : {password.text}"

    def test_lr_03_06(self, driver, request): # 회원가입 탭 - 비밀번호 입력란에 값 입력 후 보이기 버튼 클릭
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            password = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호")
            register.send_keys(password, "123456")
            register.click_element(RegisterLocator.PASSWORD_VISIBLE_BTN)
        except Exception as e:
            register.handle_exception(request, e)
        assert password.text == "123456", f"비밀번호 입력란에 다르게 입력됨. 현재 입력된 값 : {password.text}"

    def test_lr_03_07(self, driver, request): # 회원가입 탭 - 비밀번호 확인 입력란에 값 입력
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            password_confirm = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호 확인")
            register.send_keys(password_confirm, "123456")
            register.hide_keyboard()
            password_confirm = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호 확인")
        except Exception as e:
            register.handle_exception(request, e)
        assert password_confirm.text == "••••••", f"비밀번호 확인 입력란에 다르게 입력됨. 현재 입력된 값 : {password_confirm.text}"

    def test_lr_03_08(self, driver, request): # 회원가입 탭 - 비밀번호 입력란에 값 입력 후 보이기 버튼 클릭
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            password_confirm = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호 확인")
            register.send_keys(password_confirm, "123456")
            register.hide_keyboard()
            password_confirm = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호 확인")
            register.click_element(RegisterLocator.PASSWORD_CONFIRM_VISIBLE_BTN)
        except Exception as e:
            register.handle_exception(request, e)
        assert password_confirm.text == "123456", f"비밀번호 확인 입력란에 다르게 입력됨. 현재 입력된 값 : {password_confirm.text}"

    def test_lr_03_09(self, driver, request): # 회원가입 탭 - 이메일 인증 팝업 확인
        try:
            register = Register(driver)
            register.navigate_to_register(driver)
            register.input_register_data(driver,"registered_id")
            email_auth_popup = register.find_element(RegisterLocator.EMAIL_AUTH_POPUP)
        except Exception as e:
            register.handle_exception(request, e)
        assert email_auth_popup.is_displayed(), f"이메일 인증 팝업이 보이지 않는 상태."