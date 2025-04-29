from appium.webdriver.common.appiumby import AppiumBy

# 채팅 탭
CHATTING_TAB = (AppiumBy.ACCESSIBILITY_ID, '채팅\n탭 4개 중 3번째') # 채팅 탭 아이콘
CHATTING_TAB_TITLE = (AppiumBy.ACCESSIBILITY_ID, '채팅 목록') # 타이틀
SEARCH_INPUT = (AppiumBy.CLASS_NAME, 'android.widget.EditText') # 검색창