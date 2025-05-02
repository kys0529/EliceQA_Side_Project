from appium.webdriver.common.appiumby import AppiumBy

# 📌 탭
HOME_TAB = (AppiumBy.ACCESSIBILITY_ID, "홈")
TRAVEL_PRODUCT_TAB = (AppiumBy.ACCESSIBILITY_ID, "여행상품")
CHATTING_TAB = (AppiumBy.ACCESSIBILITY_ID, "채팅")
MYPAGE_TAB = (AppiumBy.ACCESSIBILITY_ID, "마이페이지")

# 📌 홈 탭
TRAVELON_LOGO = (AppiumBy.XPATH, "//android.widget.ImageView")
NOTIFICATION_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button")

DDAY_WIDGET_USER_NAME = (AppiumBy.XPATH, "(//android.widget.ScrollView//android.view.View)[1]")
DDAY_WIDGET_TITLE = (AppiumBy.XPATH, "(//android.widget.ScrollView//android.view.View)[2]")

WEATHER_WIDGET_REGION = (AppiumBy.XPATH, "(//android.widget.ScrollView//android.view.View)[3]")
WEATHER_WIDGET_TEMP = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '°')]")
WEATHER_WIDGET_WIND = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'm/s')]")

TRAVEL_RECOMM_BTN = (AppiumBy.ACCESSIBILITY_ID, "여행추천")
GUIDE_RANK_BTN = (AppiumBy.ACCESSIBILITY_ID, "가이드랭킹")
REGION_TOUR_BTN = (AppiumBy.ACCESSIBILITY_ID, "지역탐방")
TRAVEL_GALLERY_BTN = (AppiumBy.ACCESSIBILITY_ID, "여행갤러리")

CONGESTION_TITLE = (AppiumBy.ACCESSIBILITY_ID, "인기 관광지 혼잡도")
CONGESTION_REFRESH_BTN = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.Button[1]")
CONGESTION_REGIONS_BAR = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[8]/android.view.View")
CONGESTION_ALL_BTN = (AppiumBy.ACCESSIBILITY_ID, "전체")
CONGESTION_SEOUL_BTN = (AppiumBy.ACCESSIBILITY_ID, "서울")
CONGESTION_BUSAN_BTN = (AppiumBy.ACCESSIBILITY_ID, "부산")
CONGESTION_DAEGU_BTN = (AppiumBy.ACCESSIBILITY_ID, "대구")
CONGESTION_INCHEON_BTN = (AppiumBy.ACCESSIBILITY_ID, "인천")
CONGESTION_GWANGJU_BTN = (AppiumBy.ACCESSIBILITY_ID, "광주")
CONGESTION_DAEJEON_BTN = (AppiumBy.ACCESSIBILITY_ID, "대전")
CONGESTION_ULSAN_BTN = (AppiumBy.ACCESSIBILITY_ID, "울산")
CONGESTION_GYEONGGI_BTN = (AppiumBy.ACCESSIBILITY_ID, "경기")
CONGESTION_GANGWON_BTN = (AppiumBy.ACCESSIBILITY_ID, "강원")
CONGESTION_JEJU_BTN = (AppiumBy.ACCESSIBILITY_ID, "제주")
CONGESTION_RESULTS_BAR = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[9]/android.view.View")
CONGESTION_FIRST_RESULT = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[9]/android.view.View/android.view.View[1]")

POPULAR_COURSE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "지금 인기있는 여행코스는?")
POPULAR_COURSE_MORE = (AppiumBy.ACCESSIBILITY_ID, "더보기")
POPULAR_COURSE_RESULTS_BAR = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[9]/android.view.View")

# 📌 맞춤 여행 추천 페이지
TRAVEL_RECOMM_TITLE = (AppiumBy.ACCESSIBILITY_ID, "맞춤 여행 추천")
TRAVEL_RECOMM_RESULTS = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View")
TRAVEL_RECOMM_FIRST_RESULT = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")

# 📌 가이드 랭킹 페이지
GUIDE_RANK_TITLE = (AppiumBy.ACCESSIBILITY_ID, "가이드 랭킹")
GUIDE_RANK_RESULTS = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View")

# 📌 지역탐방 페이지
REGION_TOUR_TITLE = (AppiumBy.ACCESSIBILITY_ID, "지역탐방")
REGION_TOUR_CITY_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "시/도 선택")
REGION_TOUR_CITY_DAEGU = (AppiumBy.ACCESSIBILITY_ID, "대구광역시")
REGION_TOUR_DISTRICT_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "시/군/구 선택")
REGION_TOUR_DISTRICT_JUNGGU = (AppiumBy.ACCESSIBILITY_ID, "중구")
REGION_TOUR_DISTRICT_DONGGU = (AppiumBy.ACCESSIBILITY_ID, "동구")
REGION_TOUR_DISTRICT_SEOGU = (AppiumBy.ACCESSIBILITY_ID, "서구")
REGION_TOUR_DISTRICT_NAMGU = (AppiumBy.ACCESSIBILITY_ID, "남구")
REGION_TOUR_DISTRICT_BUKGU = (AppiumBy.ACCESSIBILITY_ID, "북구")
REGION_TOUR_DISTRICT_SUSEONGGU = (AppiumBy.ACCESSIBILITY_ID, "수성구")
REGION_TOUR_DISTRICT_DALSEOGU = (AppiumBy.ACCESSIBILITY_ID, "달서구")
REGION_TOUR_DISTRICT_DALSEONGGUN = (AppiumBy.ACCESSIBILITY_ID, "달성군")
REGION_TOUR_ALL_BTN = (AppiumBy.ACCESSIBILITY_ID, "전체")
REGION_TOUR_ATTRACTION_BTN = (AppiumBy.ACCESSIBILITY_ID, "관광지")
REGION_TOUR_FOOD_BTN = (AppiumBy.ACCESSIBILITY_ID, "음식")
REGION_TOUR_STAY_BTN = (AppiumBy.ACCESSIBILITY_ID, "숙박")
REGION_TOUR_RESULTS = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View")

# 📌 여행갤러리 페이지
TRAVEL_GALLERY_TITLE = (AppiumBy.ACCESSIBILITY_ID, "여행갤러리")
TRAVEL_GALLERY_SEARCH_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]")
TRAVEL_GALLERY_BOOKMARK_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[3]")
TRAVEL_GALLERY_ADD_POST_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[4]")
TRAVEL_GALLERY_RESULTS = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View")
TRAVEL_GALLERY_FIRST_RESULT = (AppiumBy.XPATH, "(//android.view.View[contains(@content-desc, '좋아요')])[1]")
TRAVEL_GALLERY_FIRST_RESULT_LIKE_BTN = (AppiumBy.XPATH, "(//android.view.View[contains(@content-desc, '좋아요')])[1]//android.widget.Button[1]")
TRAVEL_GALLERY_FIRST_RESULT_COMMENT_BTN = (AppiumBy.XPATH, "(//android.view.View[contains(@content-desc, '좋아요')])[1]//android.widget.Button[2]")
TRAVEL_GALLERY_FIRST_RESULT_BOOKMARK_BTN = (AppiumBy.XPATH, "(//android.view.View[contains(@content-desc, '좋아요')])[1]//android.widget.Button[3]")
TRAVEL_GALLERY_FIRST_RESULT_ALL_COMMENT_BTN = (AppiumBy.XPATH, "(//android.view.View[contains(@content-desc, '좋아요')])[1]//android.widget.Button[4]")

TRAVEL_GALLERY_COMMENT_AREA = (AppiumBy.ACCESSIBILITY_ID, "댓글")
TRAVEL_GALLERY_COMMENT_AREA_CLOSE_BTN = (AppiumBy.XPATH, "//android.view.View[@content-desc='댓글']/android.widget.Button[1]")
TRAVEL_GALLERY_COMMENT_RESULTS = (AppiumBy.XPATH, "//android.view.View[@content-desc='댓글']/android.view.View")
TRAVEL_GALLERY_COMMENT_FIRST_RESULT = (AppiumBy.XPATH, "//android.view.View[@content-desc='댓글']/android.view.View/android.view.View/android.view.View")
TRAVEL_GALLERY_COMMENT_INPUT = (AppiumBy.XPATH, "//android.widget.EditText")
TRAVEL_GALLERY_COMMENT_SEND_BTN = (AppiumBy.XPATH, "//android.view.View[@content-desc='댓글']/android.widget.Button[2]")

TRAVEL_GALLERY_BOOKMARK_TITLE = (AppiumBy.ACCESSIBILITY_ID, "스크랩한 게시글")

TRAVEL_GALLERY_ADD_POST_TITLE = (AppiumBy.ACCESSIBILITY_ID, "새 게시물")
TRAVEL_GALLERY_ADD_POST_SHARE_BTN = (AppiumBy.ACCESSIBILITY_ID, "공유")
TRAVEL_GALLERY_ADD_POST_IMG_BTN = (AppiumBy.ACCESSIBILITY_ID, "이미지 추가")
TRAVEL_GALLERY_ADD_POST_LOCATION_INPUT = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
TRAVEL_GALLERY_ADD_POST_LOCATION_WARNING = (AppiumBy.ACCESSIBILITY_ID, "위치를 입력해주세요")
TRAVEL_GALLERY_ADD_POST_DESCRIPTION_INPUT = (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
TRAVEL_GALLERY_ADD_POST_DESCRIPTION_WARNING = (AppiumBy.ACCESSIBILITY_ID, "설명을 입력해주세요")

TRAVEL_GALLERY_SEARCH_INPUT =(AppiumBy.XPATH, "//android.widget.EditText")
TRAVEL_GALLERY_SEARCH_FIRST_RESULT = (AppiumBy.XPATH, "(//android.view.View[contains(@content-desc, '좋아요')])[1]")

# 📂 주요 UI 요소 확인을 위한 요소 리스트
# 📌 홈 탭 주요 UI 요소 리스트
HOME_TAB_KEY_UI_ELEMENTS = [
    TRAVELON_LOGO, 
    DDAY_WIDGET_USER_NAME, DDAY_WIDGET_TITLE,
    WEATHER_WIDGET_REGION, WEATHER_WIDGET_TEMP, WEATHER_WIDGET_WIND,
    TRAVEL_RECOMM_BTN, GUIDE_RANK_BTN, REGION_TOUR_BTN, TRAVEL_GALLERY_BTN,
    CONGESTION_TITLE, CONGESTION_REFRESH_BTN, CONGESTION_REGIONS_BAR, CONGESTION_RESULTS_BAR,
    POPULAR_COURSE_TITLE, POPULAR_COURSE_RESULTS_BAR, POPULAR_COURSE_MORE
]

# 📌 맞춤 여행 추천 페이지 주요 UI 요소 리스트
TRAVEL_RECOMM_UI_ELEMENTS = [
    TRAVEL_RECOMM_TITLE,
    TRAVEL_RECOMM_RESULTS
]

# 📌 가이드 랭킹 페이지 주요 UI 요소 리스트
GUIDE_RANK_UI_ELEMENTS = [
    GUIDE_RANK_TITLE,
    GUIDE_RANK_RESULTS
]

# 📌 지역탐방 페이지 주요 UI 요소 리스트
REGION_TOUR_UI_ELEMENTS = [
    REGION_TOUR_TITLE,
    REGION_TOUR_CITY_DROPDOWN,
    REGION_TOUR_ALL_BTN,
    REGION_TOUR_ATTRACTION_BTN,
    REGION_TOUR_FOOD_BTN,
    REGION_TOUR_STAY_BTN
]

# 📌 여행갤러리 페이지 주요 UI 요소 리스트
TRAVEL_GALLERY_UI_ELEMENTS = [
    TRAVEL_GALLERY_TITLE,
    TRAVEL_GALLERY_SEARCH_BTN,
    TRAVEL_GALLERY_BOOKMARK_BTN,
    TRAVEL_GALLERY_ADD_POST_BTN,
    TRAVEL_GALLERY_RESULTS
]

# 📌 여행갤러리 페이지 - 댓글 창 주요 UI 요소 리스트
TRAVEL_GALLERY_COMMENT_AREA_UI_ELEMENTS = [
    TRAVEL_GALLERY_COMMENT_AREA,
    TRAVEL_GALLERY_COMMENT_AREA_CLOSE_BTN,
    TRAVEL_GALLERY_COMMENT_RESULTS,
    TRAVEL_GALLERY_COMMENT_INPUT,
    TRAVEL_GALLERY_COMMENT_SEND_BTN
]

# 📌 여행갤러리 페이지 - 스크랩한 게시글 페이지 주요 UI 요소 리스트
TRAVEL_GALLERY_BOOKMARK_LIST_UI_ELEMENTS = [
    TRAVEL_GALLERY_BOOKMARK_TITLE,
    TRAVEL_GALLERY_FIRST_RESULT,
    TRAVEL_GALLERY_FIRST_RESULT_LIKE_BTN,
    TRAVEL_GALLERY_FIRST_RESULT_COMMENT_BTN,
    TRAVEL_GALLERY_FIRST_RESULT_BOOKMARK_BTN,
    TRAVEL_GALLERY_FIRST_RESULT_ALL_COMMENT_BTN
]

# 📌 여행갤러리 페이지 - 새 게시글 페이지 주요 UI 요소 리스트
TRAVEL_GALLERY_ADD_POST_UI_ELEMENTS = [
    TRAVEL_GALLERY_ADD_POST_TITLE,
    TRAVEL_GALLERY_ADD_POST_SHARE_BTN,
    TRAVEL_GALLERY_ADD_POST_IMG_BTN,
    TRAVEL_GALLERY_ADD_POST_LOCATION_INPUT,
    TRAVEL_GALLERY_ADD_POST_DESCRIPTION_INPUT
]