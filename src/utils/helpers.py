from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.BasePage import BasePage

from appium.webdriver.common.appiumby import AppiumBy   # TODO: 추후 login 요소 정의 후 수정 시 삭제
#from utils.locators import LoginLocator                # TODO: 추후 login 요소 정의 후 수정 시 추가

class Helpers(BasePage):
    def __init__(self, driver, page_name = "Helpers"):
        super().__init__(driver, page_name)

    def login(self, login_id, login_pw):
        screenshot_file = self.save_screenshot("login")

        # TODO: login 요소 하드코딩 -> 추후 login 요소 정의 후 수정 필요
        INPUT_ID = (AppiumBy.XPATH, "//android.widget.EditText[1]")
        INPUT_PW = (AppiumBy.XPATH, "//android.widget.EditText[2]")
        BTN_LOGIN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='로그인']")
        BTN_ALLOW_PUSH = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        HOME_LOGO = (AppiumBy.XPATH, "//android.widget.ImageView")

        try:
            input_id = self.click_element(INPUT_ID)
            input_id.send_keys(login_id)
            self.logger.info("✔ ID 입력 확인")

            input_pw = self.click_element(INPUT_PW)
            input_pw.send_keys(login_pw)
            self.logger.info("✔ PW 입력 확인")

            self.driver.hide_keyboard() # 키보드 창이 요소를 가리는 문제 방지

            self.click_element(BTN_LOGIN)
            self.logger.info("✔ 로그인 버튼 클릭 확인")

            try: # 알림 허용 팝업이 뜨는 경우와 뜨지 않는 경우를 모두 고려하여 예외 처리
                self.click_element(BTN_ALLOW_PUSH)
                self.logger.info("✔ 알림 허용 클릭 확인")
            except TimeoutException:
                self.logger.info("✔ 알림 허용 버튼 안 뜸, 넘어감")

            assert self.find_element(HOME_LOGO).is_displayed()
            self.logger.info("✔ 홈 화면 진입 확인")

        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"✖ 요소를 찾지 못하거나 대기 시간 초과: {e}")
            self.driver.save_screenshot(screenshot_file)
            raise

        except Exception as e:
            self.logger.error(f"✖ 예외 발생: {e}")
            self.driver.save_screenshot(screenshot_file)
            raise
