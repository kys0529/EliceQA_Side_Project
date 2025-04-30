from appium.webdriver.common.appiumby import AppiumBy

class TravelProductListLocator: # 여행 패키지 페이지 LOCATOR 모음
    PAGE_NAVI = (AppiumBy.ACCESSIBILITY_ID, "여행상품\n탭 4개 중 2번째")
    PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "여행 패키지")

    SEARCH_ICON = (AppiumBy.XPATH, "//android.widget.Button[1]")
    FILTER_ICON = (AppiumBy.XPATH, "//android.widget.Button[2]")
    SORT_BTN = (AppiumBy.ACCESSIBILITY_ID, "기본순")
    PACKAGE_LIST = (AppiumBy.XPATH, "//android.widget.FrameLayout//android.view.View[3]/android.view.View")

    UI_CHECK_ELEMENT = [SEARCH_ICON, FILTER_ICON, SORT_BTN, PACKAGE_LIST]

    SEARCH_BAR = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    SEARCH_NONE_RESULT_CHECK = [
        (AppiumBy.ACCESSIBILITY_ID, "검색 결과: 0개"), 
        (AppiumBy.ACCESSIBILITY_ID, "등록된 패키지가 없습니다.")
    ]
    
    @staticmethod
    def filter_dropdown(text):
        return (AppiumBy.ACCESSIBILITY_ID, f"{text}")
    @staticmethod
    def filter_select(filter_name):
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='선택된 지역: {filter_name}']")


    # 아래는 아직 미사용
    FILTER_NONE_RESULT_CHECK = (AppiumBy.XPATH, "//android.view.View[@content-desc='등록된 패키지가 없습니다.']")
    FILTERED_PACKAGE_LIST = (AppiumBy.XPATH, "//android.widget.FrameLayout//android.view.View[4]/android.view.View")

    PACKAGE_IMAGE = (AppiumBy.XPATH, "//android.widget.ImageView")
    
    PACKAGE_WISH_BTN = (AppiumBy.XPATH, "//android.widget.Button")

    @staticmethod
    def sort_dropdown(text):
        return (AppiumBy.XPATH, f"//android.widget.Button[@content-desc='{text}']")

    @staticmethod
    def package_select(text):
        return (AppiumBy.XPATH, f"//android.widget.ImageView[contains(@content-desc, '{text}')]")

class TravelProductDetailLocator:   # 패키지 상세 페이지 LOCATOR 모음
    pass

class TravelProductReviewLocator:   # 리뷰 페이지 LOCATOR 모음
    pass

class GuideProfileLocator:  # 가이드 프로필 페이지 LOCATOR 모음
    pass

class ReservationLocator:   # 예약하기 페이지 LOCATOR 모음
    pass