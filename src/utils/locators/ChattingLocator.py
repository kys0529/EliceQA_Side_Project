from appium.webdriver.common.appiumby import AppiumBy


class ChattingTabLocator: # 채팅 탭 관련
  ICON = (AppiumBy.ACCESSIBILITY_ID, '채팅\n탭 4개 중 3번째') # 채팅 탭 아이콘
  TITLE = (AppiumBy.ACCESSIBILITY_ID, '채팅 목록') # 타이틀
  SEARCH_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@hint="검색"]') # 채팅방 검색창
  SEARCH_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button') # 검색 버튼


class ChatRoomLocator: # 채팅방 관련
  @staticmethod
  def chat_room_profile(user_name: str): # 채팅방 진입
    return (AppiumBy.XPATH, f'//android.widget.Button[contains(@content-desc, "{user_name}")]')

  @staticmethod
  def chat_room_title(user_name: str):
    return (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc, "{user_name} 님과의 대화")]')

  #채팅방 UI 요소
  BACK_BTN = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼
  PLUS_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button[1]') # + 버튼
  MESSAGE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@hint="메시지를 입력하세요..."]') # 메세지 입력창
  MESSAGE_SEND_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button[2]') # 메세지 보내기 버튼

  UI_CHECK_LOCS = [BACK_BTN, PLUS_BTN, MESSAGE_INPUT, MESSAGE_SEND_BTN] 






# 채팅방 나가기
EXIT_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 나가기 모달창
EXIT_ALERT_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, '사용자 A님과의 대화방을 나가시겠습니까?') # 모달창 메시지
EXIT_ALERT_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '취소') # 취소 버튼
EXIT_ALERT_EXIT_BTN = (AppiumBy.ACCESSIBILITY_ID, '나가기') # 나가기 버튼


# 갤러리
GALLERY_ICON = (AppiumBy.XPATH, '//android.view.View[@content-desc="갤위치카메라 사용자 위치 지도"]/android.view.View[1]') # 갤러리 아이콘
GALLERY_IMAGE = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[2]') # 로컬 이미지 랜덤 선택되는지 체크필요
IMAGE_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 사진 보내기 모달창
IMAGE_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, '사진 보내기') # 사진 보내기 모달창 타이틀
IMAGE_ALERT_YES_BTN = (AppiumBy.ACCESSIBILITY_ID, '예') # 예 버튼
IMAGE_ALERT_NO_BTN = (AppiumBy.ACCESSIBILITY_ID, '아니오') # 아니오 버튼


# 카메라
CAMERA_ICON = (AppiumBy.XPATH, '//android.view.View[@content-desc="갤러리 카메라 사용자 패키지 지도"]/android.view.View[2]')
TAKE_PHOTO_BTN = (AppiumBy.ID, 'com.sec.android.app.camera:id/bottom_background') # 카메라 촬영 버튼 체크필요
TAKE_PHOTO_CONFIRM_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.sec.android.app.camera:id/navigation_bar_item_small_label_view" and @text="확인"]') # 카메라 촬영 후 확인 버튼 체크필요
TAKE_PHOTO_RETRY_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.sec.android.app.camera:id/navigation_bar_item_small_label_view" and @text="다시 시도"]') # 카메라 촬영 후 다시시도 버튼 체크필요
## 사진보내기 모달창과 똑같


# 사용자
USER_ICON = (AppiumBy.XPATH, '//android.view.View[@content-desc="갤러리 카메라 사용자 패키지 지도"]/android.view.View[3]')
BACK_BTN_USER = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼
USER_TITLE = (AppiumBy.ACCESSIBILITY_ID, '사용자 검색') # 사용자 검색 타이틀
SEARCH_INPUT_USER = (AppiumBy.XPATH, '//android.widget.EditText[@hint="검색"]') # 사용자 검색창
SEARCH_BTN_USER = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button') # 사용자 검색 버튼
USER_PROFILE_CARD = (AppiumBy.ACCESSIBILITY_ID, '사용자 A\ntrouffeubavilleu-2112@yopmail.com') # 사용자 카드 재사용가능할지 체크
PROFILE_SHARE_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="사용자 A trouffeubavilleu-2112@yopmail.com"]/android.widget.Button') #프로필 공유 버튼 재사용 가능한지 체크
PROFILE_SHARE_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 공유하기 모달창
SHARE_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, '공유하기') # 공유하기 모달창 타이틀
SHARE_ALERT_PROFILE_PREVIEW = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View/android.view.View[2]') # 프로필 미리보기 모달창
FROFILE_SHARE_ALERT_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '취소') # 취소 버튼
FROFILE_SHARE_ALERT_SEND_BTN = (AppiumBy.ACCESSIBILITY_ID, '보내기') # 보내기 버튼

#사용자-채팅방
PROFILE_DM_BTN = (AppiumBy.ACCESSIBILITY_ID, '1:1 채팅') # 1:1 채팅 버튼
DM_ROOM_TITLE = (AppiumBy.ACCESSIBILITY_ID, '사용자 B 님과의 대화') # 타이틀 재사용 체크필요
VIEW_PROFILE_BTN = (AppiumBy.ACCESSIBILITY_ID, '프로필 보기') # 프로필 보기 버튼
VIEW_PROFILE_TITLE = (AppiumBy.ACCESSIBILITY_ID, '사용자 A 님의 프로필') # 타이틀 재사용 체크필요


# 패키지
PACKAGE_ICON = (AppiumBy.XPATH, '//android.view.View[@content-desc="갤러리 카메라 사용자 패키지 지도"]/android.view.View[4]')
BACK_BTN_PACKAGE = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼
PACKAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, '패키지 찾기') # 패키지 검색창 타이틀
SEARCH_INPUT_PACKAGE = (AppiumBy.XPATH, '//android.widget.EditText[@hint="패키지 이름, 지역 또는 가이드 이름 검색"]') # 패키지 검색창
SEARCH_BTN_PACKAGE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button') #검색 버튼
PACKAGE_LIST_ITEM = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View') #패키지 리스트 인데 하나 뽑아올수있을지 체크
PACKAGE_LIST = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]') #패키지 빈 리스트 체크 필요
PACKAGE_SHARE_BTN = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="빵덕후 가격: 5580.0원 가이드: 사용자 A"]/android.widget.Button') # 패키지 공유 버튼 재사용 가능한지 체크
PACKAGE_SHARE_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 공유하기 모달창
ALERT_VIEW_PACKAGE_DETAIL_BTN = (AppiumBy.ACCESSIBILITY_ID, '패키지 상세 정보 보기') # 공유하기 모달창 상세보기 버튼
PACKAGE_SHARE_ALERT_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '취소') # 취소 버튼
PACKAGE_SHARE_ALERT_SEND_BTN = (AppiumBy.ACCESSIBILITY_ID, '보내기') # 보내기 버튼

# 패키지-채팅방
VIEW_PACKAGE_DETAIL_BTN = (AppiumBy.ACCESSIBILITY_ID, '패키지 상세 정보 보기') # 패키지 상세보기 버튼
VIEW_PACKAGE_DETAIL_TITLE = (AppiumBy.ACCESSIBILITY_ID, '패키지 상세') # 패키지 상세 페이지 타이틀


# 지도
MAP_ICON = (AppiumBy.XPATH, '//android.view.View[@content-desc="갤러리 카메라 사용자 패키지 지도"]/android.view.View[5]')
BACK_BTN_MAP = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼
MAP_TITLE = (AppiumBy.ACCESSIBILITY_ID, '장소 검색') # 장소 검색 타이틀
SEARCH_INPUT_MAP = (AppiumBy.XPATH, '//android.widget.EditText[@hint="장소 이름으로 검색..."]') # 장소 검색창
SEARCH_BTN_MAP = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button') #검색 버튼
MAP_LIST = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]') # 장소 빈 리스트 체크 필요
MAP_SEARCH_ERROR_TOAST = (AppiumBy.ACCESSIBILITY_ID, '검색 중 오류가 발생했습니다: Exception: 위치 정보를 불러오지 못했습니다. 상태 코드: 400') # 장소 검색 오류 토스트 메시지
MAP_SHARE_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="광교신도시 경기도 수원시 영통구 이의동"]/android.widget.Button') # 장소 공유 버튼 재사용 가능한지 체크

MAP_SHARE_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 공유하기 모달창
SHARE_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, '장소 공유하기') # 장소 공유하기 모달창 타이틀
SHARE_ALERT_MAP_PREVIEW = (AppiumBy.ID, 'com.example.travel_on_final:id/navermap_map_controls') # 지도 미리보기 모달창
MAP_SHARE_ALERT_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '취소') # 취소 버튼
MAP_SHARE_ALERT_SEND_BTN = (AppiumBy.ACCESSIBILITY_ID, '공유하기') # 공유하기 버튼

#지도-채팅방
VIEW_MAP_DETAIL_BTN = (AppiumBy.ACCESSIBILITY_ID, '자세히 보기') # 자세히 보기 버튼
VIEW_MAP_DETAIL_TITLE = (AppiumBy.ACCESSIBILITY_ID, '위치 상세') # 위치 상세 페이지 타이틀
VIEW_MAP_DETAIL_INFO_TITLE = (AppiumBy.ACCESSIBILITY_ID, '위치 상세 정보') # 위치 상세 정보 타이틀
LOCATION_NAME_ICON = (AppiumBy.ACCESSIBILITY_ID, '광교신도시') # 장소 이름 아이콘 재사용 될지?..
NAVER_MAP_WEB = (AppiumBy.ID, 'com.sec.android.app.sbrowser:id/sparkle_view') # 네이버맵 웹 연결
NAVER_MAP_APP = (AppiumBy.ID, 'com.nhn.android.nmap:id/v_web_view') # 네이버맵 앱 연결


#로케이터들이 사용자 닉네임이나, 장소 이름 등에 따라서 바뀌는게 많아서 자동화 가능할지 한번 코드 작성해봐야할듯!