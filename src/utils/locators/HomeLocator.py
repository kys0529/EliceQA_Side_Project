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
DDAY_WIDGET_TXT = (AppiumBy.XPATH, "(//android.widget.ScrollView//android.view.View)[2]")

WEATHER_WIDGET_REGION = (AppiumBy.XPATH, "(//android.widget.ScrollView//android.view.View)[3]")
WEATHER_WIDGET_TEMP = (AppiumBy.XPATH, "(//android.widget.ScrollView//android.view.View)[4]")
WEATHER_WIDGET_WIND = (AppiumBy.XPATH, "(//android.widget.ScrollView//android.view.View)[5]")

TRAVEL_RECOMM_BTN = (AppiumBy.ACCESSIBILITY_ID, "여행추천")
GUIDE_RANK_BTN = (AppiumBy.ACCESSIBILITY_ID, "가이드랭킹")
REGION_TOUR_BTN = (AppiumBy.ACCESSIBILITY_ID, "지역탐방")
TRAVEL_GALLERY_BTN = (AppiumBy.ACCESSIBILITY_ID, "여행갤러리")

CONGESTION_TXT = (AppiumBy.ACCESSIBILITY_ID, "인기 관광지 혼잡도")
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

POPULAR_COURSE_TXT = (AppiumBy.ACCESSIBILITY_ID, "지금 인기있는 여행코스는?")
POPULAR_COURSE_MORE = (AppiumBy.ACCESSIBILITY_ID, "더보기")
POPULAR_COURSE_RESULTS_BAR = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.View[9]/android.view.View")

# 📌 맞춤 여행 추천 페이지
TRAVEL_RECOMM_TXT = (AppiumBy.ACCESSIBILITY_ID, "맞춤 여행 추천")
TRAVEL_RECOMM_RESULTS = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View")
TRAVEL_RECOMM_FIRST_RESULT = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")

# 📌 가이드 랭킹 페이지
GUIDE_RANK_TXT = (AppiumBy.ACCESSIBILITY_ID, "가이드 랭킹")
GUIDE_RANK_RESULTS = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View")

# 📌 지역탐방 페이지
REGION_TOUR_TXT = (AppiumBy.ACCESSIBILITY_ID, "지역탐방")
REGION_TOUR_CITY_BTN = (AppiumBy.ACCESSIBILITY_ID, "시/도 선택")
REGION_TOUR_DISTRICT_BTN = (AppiumBy.ACCESSIBILITY_ID, "시/군/구 선택")
REGION_TOUR_ALL_BTN = (AppiumBy.ACCESSIBILITY_ID, "전체")
REGION_TOUR_ATTRACTION_BTN = (AppiumBy.ACCESSIBILITY_ID, "관광지")
REGION_TOUR_FOOD_BTN = (AppiumBy.ACCESSIBILITY_ID, "음식")
REGION_TOUR_STAY_BTN = (AppiumBy.ACCESSIBILITY_ID, "숙박")
REGION_TOUR_RESULTS = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View")

# 📌 여행갤러리 페이지
TRAVEL_GALLERY_TXT = (AppiumBy.ACCESSIBILITY_ID, "여행갤러리")
TRAVEL_GALLERY_SEARCH_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]")
TRAVEL_GALLERY_BOOKMARK_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[3]")
TRAVEL_GALLERY_ADD_POST_BTN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[4]")
TRAVEL_GALLERY_RESULTS = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View")

# 📂 주요 UI 요소 확인을 위한 요소 리스트
HOME_TAB_KEY_UI_ELEMENTS = [
    TRAVELON_LOGO, 
    DDAY_WIDGET_USER_NAME, DDAY_WIDGET_TXT,
    WEATHER_WIDGET_REGION, WEATHER_WIDGET_TEMP, WEATHER_WIDGET_WIND,
    TRAVEL_RECOMM_BTN, GUIDE_RANK_BTN, REGION_TOUR_BTN, TRAVEL_GALLERY_BTN,
    CONGESTION_TXT, CONGESTION_REFRESH_BTN, CONGESTION_REGIONS_BAR, CONGESTION_RESULTS_BAR,
    POPULAR_COURSE_TXT, POPULAR_COURSE_RESULTS_BAR, POPULAR_COURSE_MORE
]

TRAVEL_RECOMM_UI_ELEMENTS = [
    TRAVEL_RECOMM_TXT,
    TRAVEL_RECOMM_RESULTS
]

GUIDE_RANK_UI_ELEMENTS = [
    GUIDE_RANK_TXT,
    GUIDE_RANK_RESULTS
]