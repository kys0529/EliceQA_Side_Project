from appium.webdriver.common.appiumby import AppiumBy

''' 공통 로케이터 모음 '''
class TravelProductUtilLocator:
    TEXT = (AppiumBy.XPATH, "//android.view.View")                # 텍스트 요소
    IMAGES = (AppiumBy.XPATH, "//android.widget.ImageView")     # 이미지 요소
    BUTTON = (AppiumBy.XPATH, "//android.widget.Button")        # 버튼 기능
    INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")    # 입력 기능

    @staticmethod
    def get_image(text):            # 텍스트 기반 이미지 요소 반환
        return (AppiumBy.XPATH, f"//android.widget.ImageView[contains(@content-desc,'{text}')]")
    
    @staticmethod
    def get_text(text):             # 텍스트 기반 텍스트 요소 반환
        return (AppiumBy.XPATH, f"//android.view.View[contains(@content-desc,'{text}')]")

    @staticmethod   
    def get_button(text):           # 텍스트 기반 버튼 요소 반환
        return (AppiumBy.XPATH, f"//android.widget.Button[contains(@content-desc,'{text}')]")

    @staticmethod
    def get_accessibility_id(text): # 텍스트 기반 접근성 ID 요소 반환
        return (AppiumBy.ACCESSIBILITY_ID, f"{text}")


''' 여행 패키지 화면 '''
class TravelProductListLocator: 
    PAGE_NAVIGATION = (AppiumBy.ACCESSIBILITY_ID, "여행상품\n탭 4개 중 2번째")  # 탭 내비게이션 위치 (화면 진입 확인용)
    PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "여행 패키지") # 페이지 타이틀 텍스트
    SEARCH_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[1]")  # 검색 버튼
    FILTER_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[2]")  # 필터 버튼
    SORT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "기본순") # 정렬 옵션 버튼
    PACKAGE_LIST_CONTAINER = (AppiumBy.XPATH, "//android.widget.FrameLayout//android.view.View[3]/android.view.View")   # 패키지 리스트 영역
    UI_CHECK_ELEMENTS = [SEARCH_BUTTON, FILTER_BUTTON, SORT_BUTTON, PACKAGE_LIST_CONTAINER]     # 리스트 화면 주요 UI 요소들
    FILTER_NO_RESULTS = TravelProductUtilLocator.get_text("등록된 패키지가 없습니다.")  # 필터 결과 없음 텍스트
    SEARCH_NO_RESULTS = [
        (AppiumBy.ACCESSIBILITY_ID, "검색 결과: 0개"),  # 검색 결과 없음 텍스트
        (AppiumBy.ACCESSIBILITY_ID, "등록된 패키지가 없습니다.")    # 등록된 패키지 없음 안내 문구
    ]

    @staticmethod
    def get_selected_filter(text):
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='선택된 지역: {text}']")    # 선택된 필터(지역 등) 요소


''' 여행 패키지 상세 화면 '''
class TravelProductDetailLocator:   
    DETAIL_TITLE = (AppiumBy.ACCESSIBILITY_ID, "패키지 상세")   # 화면 진입 확인 타이틀
    REVIEW = TravelProductUtilLocator.get_button("리뷰")    # 리뷰 버튼
    GUIDE_BUTTON = TravelProductUtilLocator.get_button("가이드")    # 가이드 프로필 버튼
    PARTICIPANTS = TravelProductUtilLocator.get_text("예약 가능 인원")  # 예약 가능 인원 텍스트
    DETAILED_DESCRIPTION = (AppiumBy.ACCESSIBILITY_ID, "상세 설명") # 상세 설명 타이틀
    RESERVATION_BUTTON = TravelProductUtilLocator.get_button("예약하기")    # 예약하기 버튼
    TRAVEL_COURSE = (AppiumBy.ACCESSIBILITY_ID, "여행 코스")    # 여행 코스 타이틀
    UI_CHECK_ELEMENTS = [REVIEW, GUIDE_BUTTON, PARTICIPANTS, DETAILED_DESCRIPTION, RESERVATION_BUTTON]  # 상세화면 주요 UI 요소
    GUIDE_CHATTING_BUTTON = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.Button[4]")    # 가이드 채팅 버튼
    GUIDE_EMOJI_BUTTON = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.Button[2]")   # 가이드 이모지 버튼
    TRAVEL_COURSE_BUTTON = TravelProductUtilLocator.get_button("1.")    # 첫 번째 여행 코스 버튼 
    TRAVEL_COURSE_BOTTOM_SHEET = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View\
                                  /android.view.View/android.view.View[2]/android.view.View")  # 여행 코스 하단 시트


''' 리뷰작성 화면 '''
class TravelProductReviewLocator:
    REVIEW = (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc, '리뷰') and contains(@content-desc, '개')]")
    TO_WRITE_REVIEW = (AppiumBy.ACCESSIBILITY_ID, "리뷰 작성하기")
    REVIEW_WRITE = (AppiumBy.ACCESSIBILITY_ID, "리뷰 작성")
    SEND_REVIEW = (AppiumBy.ACCESSIBILITY_ID, "리뷰 등록")
    NO_INPUT_REVIEW = (AppiumBy.ACCESSIBILITY_ID, "리뷰 내용을 입력해주세요")
    VERIFIED_REVIEW_SECTION_VISIBLE = (AppiumBy.XPATH, "//android.view.View[4]/android.view.View/android.view.View")
    UNVERIFIED_REVIEW_SECTION_VISIBLE = (AppiumBy.XPATH, "//android.view.View[5]/android.view.View/android.view.View")
    INVISIBLE_REVIEW = (AppiumBy.ACCESSIBILITY_ID, "아직 작성된 리뷰가 없습니다")
    UNVERIFIED_REVIEW = (AppiumBy.ACCESSIBILITY_ID, "예약 승인된 사용자만 리뷰를 작성할 수 있습니다")

    @staticmethod
    def select_review_star(text):
        return (AppiumBy.XPATH, f"//android.view.View[2]//android.widget.Button[{text}]")

    @staticmethod
    def get_review_count(text): # 리뷰 개수
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='리뷰 {text}개']")


''' 가이드 프로필 화면 '''
class GuideProfileLocator:
    GUIDE_ICON = (AppiumBy.ACCESSIBILITY_ID, "가이드")  # 가이드 아이콘
    AVERAGE_RATING = TravelProductUtilLocator.get_text("평균 별점") # 평균 별점 텍스트
    REVIEW = TravelProductUtilLocator.get_text("리뷰")  # 리뷰 텍스트
    GUIDE_PACKAGE = (AppiumBy.ACCESSIBILITY_ID, "가이드 패키지")    # 가이드 패키지 타이틀
    GUIDE_PACKAGE_PREVIEW = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[6]")
    UI_CHECK_ELEMENTS = [GUIDE_ICON, AVERAGE_RATING, REVIEW, GUIDE_PACKAGE, GUIDE_PACKAGE_PREVIEW] # 프로필 화면 주요 UI 요소
    GUIDE_CHATTING_BUTTON = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.Button[1]")    # 가이드 채팅 버튼
    PACKAGE_MORE_BUTTON = TravelProductUtilLocator.get_button("더보기") # 더보기 버튼
    
    @staticmethod
    def guide_name_to_email(text):  # 가이드 이름 클릭 시 이메일 변경
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='{text}']")
    
    @staticmethod
    def guide_package_title(text):  # 가이드 패키지 화면 타이틀
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='{text} 님의 패키지 목록']")    
    
    
''' 예약하기 화면 '''
class ReservationLocator:
    RESERVATION_TITLE = (AppiumBy.ACCESSIBILITY_ID, "예약 날짜 선택")   # 예약 화면 진입 확인 타이틀
    CALENDAR = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']//android.view.View[2]//android.view.View[4]//android.view.View")   # 캘린더 뷰
    SELECT_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, "인원 선택")
    SELECTED_DATE = TravelProductUtilLocator.get_text("선택한 날짜")
    PACKAGE_NAME = TravelProductUtilLocator.get_text("패키지")
    SCHEDULE = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '박') and contains(@content-desc, '일')]")
    PRICE = TravelProductUtilLocator.get_text("가격")
    UI_CHECK_ELEMENTS = [SELECTED_DATE, PACKAGE_NAME, SCHEDULE, PRICE, SELECT_PERSONNEL]
    ADD_PERSONNEL = (AppiumBy.XPATH, "//android.view.View[2]//android.widget.Button[2]")
    MINUS_PERSONNEL = (AppiumBy.XPATH, "//android.view.View[2]//android.widget.Button[1]")

    @staticmethod
    def get_selected_date(text):
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='선택한 날짜: {text}']")    # 선택된 예약 날짜 요소
    
    @staticmethod
    def get_select_personnel(text):
        return (AppiumBy.XPATH, f"//android.view.View[@content-desc='{text}명']")    # 선택된 예약 날짜 요소