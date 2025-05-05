from src.utils.locators import HomeLocator

# 📌 인기 관광지 혼잡도
# test_hp_05_04 (인기 관광지 혼잡도의 지역 필터 중 '전체' 필터 확인)
expected_regions = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기", "강원", "제주"]

# test_hp_05_05 ~ test_hp_05_14 (인기 관광지 혼잡도의 지역 필터 중 '서울/부산/대구/인천/광주/대전/울산/경기/강원/제주' 필터 확인)
locator__region_name = [ 
    (HomeLocator.CONGESTION_SEOUL_BTN, "서울"), # test_hp_05_05
    (HomeLocator.CONGESTION_BUSAN_BTN, "부산"), # test_hp_05_06
    (HomeLocator.CONGESTION_DAEGU_BTN, "대구"), # test_hp_05_07
    (HomeLocator.CONGESTION_INCHEON_BTN, "인천"), # test_hp_05_08
    (HomeLocator.CONGESTION_GWANGJU_BTN, "광주"), # test_hp_05_09
    (HomeLocator.CONGESTION_DAEJEON_BTN, "대전"), # test_hp_05_10
    (HomeLocator.CONGESTION_ULSAN_BTN, "울산"), # test_hp_05_11
    (HomeLocator.CONGESTION_GYEONGGI_BTN, "경기"), # test_hp_05_12
    (HomeLocator.CONGESTION_GANGWON_BTN, "강원"), # test_hp_05_13
    (HomeLocator.CONGESTION_JEJU_BTN, "제주") # test_hp_05_14
]

# 📌 지역 탐방
# test_hp_13_02 (선택된 시/도, 시/군/구, 장소 유형과 관련된 장소 리스트 노출 확인)
expected_types = ["관광지", "음식", "숙박"]

# test_hp_13_02 (선택된 시/도, 시/군/구, 장소 유형과 관련된 장소 리스트 노출 확인)
city__district__filter__expected_values = [
    (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_ALL_BTN, "대구", "북구", "전체"), # test_hp_13_02
    (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_ATTRACTION_BTN, "대구", "북구", "관광지"), # test_hp_13_03
    (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_FOOD_BTN, "대구", "북구", "음식"), # test_hp_13_04
    (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_STAY_BTN, "대구", "북구", "숙박") # test_hp_13_05
]

# test_hp_14_01 (선택된 시/도, 시/군/구, 장소 유형과 관련된 장소 리스트 중 가장 상단에 위치한 장소 선택 시, 네이버 지도로 이동)
city__district__filter = [ 
    (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_ALL_BTN), 
]

# 📌 여행 갤러리
# test_hp_16_05 (입력한 댓글이 댓글 리스트에 정상적으로 추가되는지 확인)
comment = [
    ["이것은 댓글 테스트", "댓글 작성 테스트"]
]

# test_hp_18_03 (이미지도 필수 항목이므로, [공유] 버튼이 정상 동작하지 않음)
# test_hp_18_04 (작성한 게시글이 피드 글 리스트에 정상적으로 추가됨)
location__description = [
    ("대구 루시드 카페", "푸딩 빙수 존맛탱") 
]

# test_hp_19_02 (입력한 키워드와 관련된 글이 검색 영역에 정상적으로 노출)
keyword__content = [
    ("위치", "대구 루시드 카페"), # test_hp_19_02
    ("내용", "푸딩 빙수 존맛탱"), # test_hp_19_03
    ("패키지", "알찬") # test_hp_19_04
]