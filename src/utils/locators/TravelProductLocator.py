from appium.webdriver.common.appiumby import AppiumBy

''' 공통 로케이터 모음 '''
class TravelProductUtilLocator:
    IMAGES = (AppiumBy.XPATH, "//android.widget.ImageView")     # 이미지 요소
    BUTTON = (AppiumBy.XPATH, "//android.widget.Button")        # 버튼 기능
    INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")    # 입력 기능

    # 텍스트 기반 이미지 요소 반환
    @staticmethod
    def get_image(text): 
        return (AppiumBy.XPATH, f"//android.widget.ImageView[contains(@content-desc,'{text}')]")
    
    # 텍스트 기반 텍스트 요소 반환
    @staticmethod
    def get_text(text): 
        return (AppiumBy.XPATH, f"//android.view.View[contains(@content-desc,'{text}')]")

    # 텍스트 기반 버튼 요소 반환
    @staticmethod
    def get_button(text):    # 정렬 이름을 기반으로 정렬 옵션 로케이터 반환
        return (AppiumBy.XPATH, f"//android.widget.Button[contains(@content-desc,'{text}')]")
    
    # 텍스트 기반 접근성 ID 요소 반환
    @staticmethod
    def get_accessibility_id(text):
        return (AppiumBy.ACCESSIBILITY_ID, f"{text}")


''' 여행 패키지 화면 '''
class TravelProductListLocator: 
    # 화면 진입 확인 요소
    PAGE_NAVIGATION = TravelProductUtilLocator.get_accessibility_id("여행상품\n탭 4개 중 2번째")
    PAGE_TITLE = TravelProductUtilLocator.get_accessibility_id("여행 패키지") 
    
    # 주요 UI 요소
    SEARCH_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[1]")
    FILTER_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[2]")
    SORT_BUTTON = TravelProductUtilLocator.get_accessibility_id("기본순")
    PACKAGE_LIST_CONTAINER = (AppiumBy.XPATH, "//android.widget.FrameLayout//android.view.View[3]/android.view.View")
    UI_CHECK_ELEMENTS = [SEARCH_BUTTON, FILTER_BUTTON, SORT_BUTTON, PACKAGE_LIST_CONTAINER]     # UI 구성 요소 리스트

    # 검색 결과 없음 처리
    SEARCH_NO_RESULTS = [
        TravelProductUtilLocator.get_accessibility_id("검색 결과: 0개"),
        TravelProductUtilLocator.get_accessibility_id("등록된 패키지가 없습니다.")
    ]

    # 선택된 필터 로케이터 반환 (지역 등)
    @staticmethod
    def get_selected_filter(filter_name):
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='선택된 지역: {filter_name}']")
    
    # 필터 결과 없음
    FILTER_NO_RESULTS = TravelProductUtilLocator.get_text("등록된 패키지가 없습니다.")


''' 여행 패키지 상세 화면 '''
class TravelProductDetailLocator:   
    # 화면 진입 확인 요소
    DETAIL_TITLE = TravelProductUtilLocator.get_accessibility_id("패키지 상세")
    
    # 상세 화면 UI 요소
    REVIEW = TravelProductUtilLocator.get_button("리뷰")
    GUIDE = TravelProductUtilLocator.get_button("가이드")
    PARTICIPANTS = TravelProductUtilLocator.get_text("예약 가능 인원")
    DETAILED_DESCRIPTION = TravelProductUtilLocator.get_accessibility_id("상세 설명")
    RESERVATION = TravelProductUtilLocator.get_button("예약하기")
    TRAVEL_COURSE = TravelProductUtilLocator.get_accessibility_id("여행 코스")
    UI_CHECK_ELEMENTS = [REVIEW, GUIDE, PARTICIPANTS, DETAILED_DESCRIPTION, RESERVATION]    # UI 구성 요소 리스트

    # 가이드 채팅 기능
    GUIDE_CHATTING_BUTTON = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.Button[4]")

    # 여행 코스 기능
    TRAVEL_COURSE_BUTTON = TravelProductUtilLocator.get_button("1.")
    TRAVEL_COURSE_BOTTOM_SHEET = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View")


''' 여행 패키지 리뷰 화면 '''
class TravelProductReviewLocator:   
    pass

''' 가이드 프로필 화면 '''
class GuideProfileLocator:  
    pass

''' 여행 패키지 예약 화면 '''
class ReservationLocator:   
    pass