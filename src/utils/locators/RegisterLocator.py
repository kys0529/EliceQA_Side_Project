from appium.webdriver.common.appiumby import AppiumBy


# 📌 로그인 탭 - Register버튼
REGISTER_BTN = (AppiumBy.ACCESSIBILITY_ID, "회원가입")

# 📌 회원가입 탭
REGISTER_TAB = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View')


# 📌 회원가입 탭 - 상단 UI
BACK_BTN = (AppiumBy.ACCESSIBILITY_ID, "뒤로")
TITLE = (AppiumBy.ACCESSIBILITY_ID, "회원가입")

# 📌 회원가입 탭 - 입력란
TEXT_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")

# 📌 회원가입 탭 - 골뱅이
AT_MARK = (AppiumBy.ACCESSIBILITY_ID, "@")

# 📌 회원가입 탭 - 이메일 도메인
EMAIL_DOMAIN = (AppiumBy.ACCESSIBILITY_ID, "@")
NAVER = (AppiumBy.ACCESSIBILITY_ID, "naver.com")
GMAIL = (AppiumBy.ACCESSIBILITY_ID, "gmail.com")
DAUM = (AppiumBy.ACCESSIBILITY_ID, "daum.net")