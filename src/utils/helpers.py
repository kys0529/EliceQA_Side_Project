from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy   # TODO: 추후 login 요소 정의 후 수정 시 삭제
#from utils.locators import LoginLocator                # TODO: 추후 login 요소 정의 후 수정 시 추가

def login(driver, login_id, login_pw):
    # TODO: login 요소 하드코딩 -> 추후 login 요소 정의 후 수정 필요
    INPUT_ID = (AppiumBy.XPATH, "//android.widget.EditText[1]")
    INPUT_PW = (AppiumBy.XPATH, "//android.widget.EditText[2]")
    BTN_LOGIN = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='로그인']")
    BTN_ALLOW_PUSH = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")

    wait = WebDriverWait(driver, 2)
    input_id = wait.until(EC.element_to_be_clickable(INPUT_ID))
    input_pw = wait.until(EC.element_to_be_clickable(INPUT_PW))

    input_id.click()
    input_id.send_keys(login_id)
    input_pw.click()
    input_pw.send_keys(login_pw)

    driver.hide_keyboard() # 키보드 창이 요소를 가리는 문제 방지

    try: # 알림 허용 팝업이 뜨는 경우와 뜨지 않는 경우를 모두 고려하여 예외 처리
        wait.until(EC.element_to_be_clickable(BTN_ALLOW_PUSH)).click()
    except:
        pass
    
    wait.until(EC.element_to_be_clickable(BTN_LOGIN)).click()