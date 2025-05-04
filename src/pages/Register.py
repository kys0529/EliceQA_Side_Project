from src.pages.BasePage import BasePage
from src.utils.locators import RegisterLocator
from src.resources.testdata.test_data import not_registered_id, registered_id

class Register(BasePage):
    def __init__(self, driver, page_name="Register"):
        super().__init__(driver, page_name)

    def navigate_to_register(self, driver):
        try:
            register = Register(driver)
            register.click_element(RegisterLocator.REGISTER_BTN)
        except Exception as e:
            register.logger.error(f"테스트 실패 - navigate_to_register")
            register.save_screenshot("failed_navigate_to_register")
            raise
    
    def input_register_data(self, driver, id_info):
        try:
            if id_info == "registered_id":
                nickname = registered_id["nickname"]
                email_id = registered_id["email_id"]
                email_domain = registered_id["email_domain"]
                password = registered_id["password"]
            elif id_info == "not_registered_id":
                nickname = not_registered_id["nickname"]
                email_id = not_registered_id["email_id"]
                email_domain = not_registered_id["email_domain"]
                password = not_registered_id["password"]
            register = Register(driver)
            nickname_input = register.find_by_hint(RegisterLocator.TEXT_INPUT, "닉네임")
            register.send_keys(nickname_input, nickname)
            email_id_input = register.find_by_hint(RegisterLocator.TEXT_INPUT, "이메일 아이디")
            register.send_keys(email_id_input, email_id)
            email_dropdown = register.find_element(RegisterLocator.EMAIL_DROPDOWN_BTN)
            register.click_element(email_dropdown)
            if email_domain == "naver":
                register.click_element(RegisterLocator.NAVER_BTN)
            elif email_domain == "gmail":
                register.click_element(RegisterLocator.GMAIL_BTN)
            elif email_domain == "daum":
                register.click_element(RegisterLocator.DAUM_BTN)
            else:
                register.click_element(RegisterLocator.ENTER_MANUALLY_BTN)
            password_input = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호")
            register.send_keys(password_input, password)
            password_confirm_input = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호 확인")
            register.send_keys(password_confirm_input, password)
            self.hide_keyboard()
            register.click_element(RegisterLocator.REGISTER_BTN)
        except Exception as e:
            register.logger.error(f"테스트 실패 - input_register_data")
            register.save_screenshot("failed_input_register_data")
            

    def find_by_hint(self, locator, hint):
        try:
            for element in self.driver.find_elements(*locator): # *locator = 언패킹을 해야한다
                if element.get_attribute("hint") == hint:
                    self.logger.info(f"{hint} 힌트 확인")
                    return element
        except Exception as e:
            self.logger.error(f"테스트 실패 - find_by_hint")
            self.save_screenshot("failed_to_navigate_to_register")            

    def handle_exception(self, request, e):
        self.logger.error(f"테스트 실패")
        self.save_screenshot(request.node.name)
        assert False, "테스트 실패"

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
            self.logger.info("키보드 숨김")
        except Exception as e:
            self.logger.error(f"키보드 숨기기 실패: {e}")
            self.save_screenshot("hide_keyboard_fail")