from appium.webdriver.common.appiumby import AppiumBy

# 여행 패키지 페이지의 로케이터 모음
class TravelProductListLocator: 
    # 공통 요소
    PAGE_NAVIGATION = (AppiumBy.ACCESSIBILITY_ID, "여행상품\n탭 4개 중 2번째")
    PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "여행 패키지")
    PACKAGE_IMAGES = (AppiumBy.XPATH, "//android.widget.ImageView")

    @staticmethod
    def get_package_by_text(package_name):  # 패키지의 이름 또는 설명을 기반으로 패키지 로케이터 반환
        return (AppiumBy.XPATH, f"//android.widget.ImageView[contains(@content-desc,'{package_name}')]")
    
    # UI 요소
    SEARCH_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[1]")
    FILTER_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[2]")
    SORT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "기본순")
    PACKAGE_LIST_CONTAINER = (AppiumBy.XPATH, "//android.widget.FrameLayout//android.view.View[3]/android.view.View")
    UI_CHECK_ELEMENTS = [SEARCH_BUTTON, FILTER_BUTTON, SORT_BUTTON, PACKAGE_LIST_CONTAINER]

    # 검색 기능
    SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    SEARCH_NO_RESULTS = [
        (AppiumBy.ACCESSIBILITY_ID, "검색 결과: 0개"), 
        (AppiumBy.ACCESSIBILITY_ID, "등록된 패키지가 없습니다.")
    ]
    
    # 필터 기능
    @staticmethod
    def get_filter_option(filter_name):  # 필터 이름을 기반으로 필터 옵션 로케이터 반환
        return (AppiumBy.ACCESSIBILITY_ID, f"{filter_name}")
    
    @staticmethod
    def get_selected_filter(filter_name):   # 필터 이름을 기반으로 선택된 지역 로케이터 반환
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='선택된 지역: {filter_name}']")
    
    FILTER_NO_RESULTS = (AppiumBy.XPATH, "//android.view.View[@content-desc='등록된 패키지가 없습니다.']")

    # 정렬 기능
    @staticmethod
    def get_sort_option(sort_name):    # 정렬 이름을 기반으로 정렬 옵션 로케이터 반환
        return (AppiumBy.XPATH, f"//android.widget.Button[@content-desc='{sort_name}']")
    
    # 찜 기능
    WISHLIST_BUTTON = (AppiumBy.XPATH, "//android.widget.Button")


# 여행 패키지 상세 페이지의 로케이터 모음
class TravelProductDetailLocator:   
    pass


# 여행 패키지 리뷰 페이지의 로케이터 모음
class TravelProductReviewLocator:   
    pass


# 가이드 프로필 페이지의 로케이터 모음
class GuideProfileLocator:  
    pass


# 예약 페이지의 로케이터 모음
class ReservationLocator:   
    pass