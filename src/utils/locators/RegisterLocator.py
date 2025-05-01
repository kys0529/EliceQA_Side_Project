from appium.webdriver.common.appiumby import AppiumBy


# 📌 로그인 탭 - Register버튼
REGISTER_BTN = (AppiumBy.ACCESSIBILITY_ID, "회원가입")

# 📌 회원가입 탭
REGISTER_TAB = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View')


# 📌 회원가입 탭 - 상단 UI
BACK_BTN = (AppiumBy.ACCESSIBILITY_ID, "뒤로")
TITLE = (AppiumBy.XPATH, '//android.view.View[@content-desc="회원가입"]')

# 📌 회원가입 탭 - 입력란
TEXT_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
# 닉네임, 이메일 아이디, 비밀번호, 비밀번호 확인 입력란

# 📌 회원가입 탭 - 골뱅이
AT_MARK = (AppiumBy.ACCESSIBILITY_ID, "@")

# 📌 회원가입 탭 - 이메일 도메인
EMAIL_DROPDOWN_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.Button\").instance(1)')
NAVER_BTN = (AppiumBy.ACCESSIBILITY_ID, "naver.com")
GMAIL_BTN = (AppiumBy.ACCESSIBILITY_ID, "gmail.com")
DAUM_BTN = (AppiumBy.ACCESSIBILITY_ID, "daum.net")
#ENTER_MANUALY_BTN = find_by_hint(RegisterLocator.TEXT_INPUT, "직접 입력")
ENTER_MANUALLY_BTN = (AppiumBy.ACCESSIBILITY_ID, "직접 입력")
MENU_CLOSE = (AppiumBy.ACCESSIBILITY_ID, "메뉴 닫기")

# 📌 회원가입 탭 - 비밀번호 보이기 버튼
PASSWORD_VISIBLE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className(\"android.widget.Button\").instance(2)')

# 📌 회원가입 탭 - 비밀번호 확인 보이기 버튼
PASSWORD_CONFIRM_VISIBLE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.Button\").instance(3)')

# 📌 회원가입 탭 - 회원가입 버튼
REGISTER_BTN = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="회원가입"]')