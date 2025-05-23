from appium.webdriver.common.appiumby import AppiumBy


class ChattingTabLocator: # 채팅 탭 관련
  ICON = (AppiumBy.ACCESSIBILITY_ID, '채팅\n탭 4개 중 3번째') # 채팅 탭 아이콘
  TITLE = (AppiumBy.ACCESSIBILITY_ID, '채팅 목록') # 타이틀
  SEARCH_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@hint="검색"]') # 채팅방 검색창
  SEARCH_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button') # 검색 버튼

  TAB_CHECK_UI = [TITLE, SEARCH_INPUT, SEARCH_BTN]


class ChatRoomLocator: # 채팅방 관련
  @staticmethod
  def chat_room_profile(user_name: str): # 채팅방(프로필 이미지, 사용자이름, 마지막 메시지 노출)
    return (AppiumBy.XPATH, f'//android.widget.Button[contains(@content-desc, "{user_name}")]')

  @staticmethod
  def chat_room_title(user_name: str):
    return (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc, "{user_name} 님과의 대화")]')

  #채팅방 UI 요소
  BACK_BTN = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼
  # PLUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)') # + 버튼
  PLUS_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button[1]') # + 버튼


  #MESSAGE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@hint="메시지를 입력하세요..."]') # 메세지 입력창
  MESSAGE_INPUT = (AppiumBy.CLASS_NAME, 'android.widget.EditText') # 메세지 입력창

  MESSAGE_SEND_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button[2]') # 메세지 보내기 버튼

  @staticmethod
  def chat_message_check(text: str): # 전송한 메시지 확인
    return (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc, "{text}")]')
  
  UI_CHECK_LOCS = [BACK_BTN, PLUS_BTN, MESSAGE_INPUT, MESSAGE_SEND_BTN] 


  # 채팅방 나가기
  EXIT_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 나가기 모달창
  EXIT_ALERT_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, '사용자 A님과의 대화방을 나가시겠습니까?') # 모달창 메시지
  EXIT_ALERT_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '취소') # 취소 버튼
  EXIT_ALERT_EXIT_BTN = (AppiumBy.ACCESSIBILITY_ID, '나가기') # 나가기 버튼


class BottomSheetLocators: # 바텀시트 관련 로케이터
  
  # 갤러리
  GALLERY_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)') # 갤러리 아이콘
  LOCAL_IMAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)') # 로컬 이미지 중 첫번째
  IMAGE_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 사진 보내기 모달창
  IMAGE_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, '사진 보내기') # 사진 보내기 모달창 타이틀
  IMAGE_ALERT_YES_BTN = (AppiumBy.ACCESSIBILITY_ID, '예') # 예 버튼
  IMAGE_ALERT_NO_BTN = (AppiumBy.ACCESSIBILITY_ID, '아니오') # 아니오 버튼


  # 카메라
  CAMERA_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(6)')
  TAKE_PHOTO_BTN = (AppiumBy.ID, 'com.sec.android.app.camera:id/bottom_background') # 카메라 촬영 버튼 체크필요
  TAKE_PHOTO_CONFIRM_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.sec.android.app.camera:id/navigation_bar_item_small_label_view" and @text="확인"]') # 카메라 촬영 후 확인 버튼 체크필요
  TAKE_PHOTO_RETRY_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.sec.android.app.camera:id/navigation_bar_item_small_label_view" and @text="다시 시도"]') # 카메라 촬영 후 다시시도 버튼 체크필요
  ## 사진보내기 모달창과 똑같


  # 사용자
  USER_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(7)')
  BACK_BTN_USER = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼
  USER_TITLE = (AppiumBy.ACCESSIBILITY_ID, '사용자 검색') # 사용자 검색 타이틀
  SEARCH_INPUT_USER = (AppiumBy.XPATH, '//android.widget.EditText[@hint="검색"]') # 사용자 검색창

  SEARCH_BTN_USER = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button') # 사용자 검색 버튼

  USER_UI_LOCS = [BACK_BTN_USER, USER_TITLE, SEARCH_INPUT_USER, SEARCH_BTN_USER]

  @staticmethod
  def search_user_profile(text: str):
    return (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc, "{text}")]')

  @staticmethod
  def search_user_profile_share_btn(user_name: str, email: str):
    escaped_user_name = user_name.replace("'", "\\'").replace('"', '\\"')
    escaped_email = email.replace("'", "\\'").replace('"', '\\"')
    xpath = f'//android.view.View[@content-desc="{escaped_user_name}\n{escaped_email}"]/android.widget.Button'
    return (AppiumBy.XPATH, xpath)
  
  PROFILE_SHARE_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 공유하기 모달창
  SHARE_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, '공유하기') # 공유하기 모달창 타이틀

  @staticmethod
  def share_alert_user_name(user_name: str):
    return (AppiumBy.ACCESSIBILITY_ID, f'{user_name}')
  
  @staticmethod
  def share_alert_email(email: str):
    return (AppiumBy.ACCESSIBILITY_ID, f'{email}')

  SHARE_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, '공유하기') # 공유하기 모달창 타이틀
  FROFILE_SHARE_ALERT_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '취소') # 취소 버튼
  FROFILE_SHARE_ALERT_SEND_BTN = (AppiumBy.ACCESSIBILITY_ID, '보내기') # 보내기 버튼

  #사용자 공유-채팅방
  @staticmethod
  def share_user_message_check(user_name: str, email: str): # 공유한 사용자 프로필 메시지 확인
    escaped_user_name = user_name.replace("'", "\\'").replace('"', '\\"')
    escaped_email = email.replace("'", "\\'").replace('"', '\\"')
    xpath = f'//android.view.View[@content-desc="{escaped_user_name}\n{escaped_email}"]'
    return (AppiumBy.XPATH, xpath)

  PROFILE_DM_BTN = (AppiumBy.ACCESSIBILITY_ID, '1:1 채팅') # 1:1 채팅 버튼
  VIEW_PROFILE_BTN = (AppiumBy.ACCESSIBILITY_ID, '프로필 보기') # 프로필 보기 버튼

  USER_SHARE_ALERT_UI_LOCS = [SHARE_ALERT_TITLE, FROFILE_SHARE_ALERT_CANCEL_BTN, FROFILE_SHARE_ALERT_SEND_BTN]


  @staticmethod
  def view_profile_title(user_name: str):
    return (AppiumBy.ACCESSIBILITY_ID, f'{user_name} 님의 프로필')


  # 패키지
  PACKAGE_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)')
  BACK_BTN_PACKAGE = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼
  PACKAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, '패키지 찾기') # 패키지 검색창 타이틀
  SEARCH_INPUT_PACKAGE = (AppiumBy.XPATH, '//android.widget.EditText[@hint="패키지 이름, 지역 또는 가이드 이름 검색"]') # 패키지 검색창
  SEARCH_BTN_PACKAGE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button') #검색 버튼

  PACKAGE_UI_LOCS = [BACK_BTN_PACKAGE, PACKAGE_TITLE, SEARCH_INPUT_PACKAGE, SEARCH_BTN_PACKAGE]

  PACKAGE_LIST = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View') #패키지 리스트


  @staticmethod
  def package_share_btn(package_name: str = None, price: str = None, guide_name: str = None):
    """
    공유 버튼을 찾기 위한 XPath 생성 함수 (패키지명, 가격, 가이드명 중 아무거나 조합 가능)

    :param package_name: 패키지 이름 (선택)
    :param price: 가격 (선택)
    :param guide_name: 가이드 이름 (선택)
    :return: (By 전략, XPath 문자열)
    :raises ValueError: 조건이 하나도 없을 경우
    """
    conditions = []

    if package_name:
        conditions.append(f'contains(@content-desc, "{package_name}")')
    if price:
        conditions.append(f'contains(@content-desc, "가격: {price}")')
    if guide_name:
        conditions.append(f'contains(@content-desc, "가이드: {guide_name}")')

    if not conditions:
        raise ValueError("XPath를 생성하려면 최소한 하나 이상의 인자를 입력해야 합니다.")

    xpath = f'//android.widget.ImageView[{" and ".join(conditions)}]/android.widget.Button'
    return (AppiumBy.XPATH, xpath)

  PACKAGE_SHARE_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 공유하기 모달창
  PACKAGE_SHARE_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, '공유하기') # 공유하기 모달창 타이틀
  ALERT_VIEW_PACKAGE_DETAIL_BTN = (AppiumBy.ACCESSIBILITY_ID, '패키지 상세 정보 보기') # 공유하기 모달창 상세보기 버튼
  PACKAGE_SHARE_ALERT_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '취소') # 취소 버튼
  PACKAGE_SHARE_ALERT_SEND_BTN = (AppiumBy.ACCESSIBILITY_ID, '보내기') # 보내기 버튼

  PACKAGE_ALERT_UI_LOCS = [PACKAGE_SHARE_ALERT_TITLE, ALERT_VIEW_PACKAGE_DETAIL_BTN, PACKAGE_SHARE_ALERT_CANCEL_BTN, PACKAGE_SHARE_ALERT_SEND_BTN]

  # 패키지-채팅방
  @staticmethod
  def share_package_message(text: str):
    return (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc, "{text}")]')
  
  VIEW_PACKAGE_DETAIL_BTN = (AppiumBy.ACCESSIBILITY_ID, '패키지 상세 정보 보기') # 패키지 상세보기 버튼
  VIEW_PACKAGE_DETAIL_TITLE = (AppiumBy.ACCESSIBILITY_ID, '패키지 상세') # 패키지 상세 페이지 타이틀


  # 지도
  MAP_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(9)')
  BACK_BTN_MAP = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼
  MAP_TITLE = (AppiumBy.ACCESSIBILITY_ID, '장소 검색') # 장소 검색 타이틀
  SEARCH_INPUT_MAP = (AppiumBy.XPATH, '//android.widget.EditText[@hint="장소 이름으로 검색..."]') # 장소 검색창
  SEARCH_BTN_MAP = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button') #검색 버튼

  MAP_UI_LOCS = [BACK_BTN_MAP, MAP_TITLE, SEARCH_INPUT_MAP, SEARCH_BTN_MAP]

  MAP_LIST = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View') # 검색 장소 리스트
  MAP_SEARCH_ERROR_TOAST = (AppiumBy.ACCESSIBILITY_ID, '검색 중 오류가 발생했습니다: Exception: 위치 정보를 불러오지 못했습니다. 상태 코드: 400') # 장소 검색 오류 토스트 메시지

  @staticmethod
  def map_share_btn(location_name: str, location_address: str): #장소 공유하기 버튼
    escaped_location_name = location_name.replace("'", "\\'").replace('"', '\\"')
    escaped_location_address = location_address.replace("'", "\\'").replace('"', '\\"')
    xpath = f'//android.view.View[@content-desc="{escaped_location_name}\n{escaped_location_address}"]/android.widget.Button'
    return (AppiumBy.XPATH, xpath)
  
  @staticmethod
  def searched_map(location_name: str): # 검색한 장소 목록 카드
    return (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc, "{location_name}")]')
  

  MAP_SHARE_ALERT = (AppiumBy.XPATH, '//android.view.View[@content-desc="닫기"]/android.view.View/android.view.View') # 공유하기 모달창
  SHARE_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, '장소 공유하기') # 장소 공유하기 모달창 타이틀

  @staticmethod
  def share_alert_location_name(location_name: str):
    return (AppiumBy.ACCESSIBILITY_ID, f'{location_name}')
  
  @staticmethod
  def share_alert_location_address(location_address: str):
    return (AppiumBy.ACCESSIBILITY_ID, f'{location_address}')

  MAP_SHARE_ALERT_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '취소') # 취소 버튼
  MAP_SHARE_ALERT_SEND_BTN = (AppiumBy.ACCESSIBILITY_ID, '공유하기') # 공유하기 버튼

  MAP_ALERT_UI_LOCS = [SHARE_ALERT_TITLE, MAP_SHARE_ALERT_CANCEL_BTN, MAP_SHARE_ALERT_SEND_BTN]

  #지도-채팅방
  @staticmethod
  def share_map_message(text: str):
    return (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc, "{text}")]')
  
  VIEW_MAP_DETAIL_BTN = (AppiumBy.ACCESSIBILITY_ID, '자세히 보기') # 자세히 보기 버튼
  VIEW_MAP_DETAIL_TITLE = (AppiumBy.ACCESSIBILITY_ID, '위치 상세') # 위치 상세 페이지 타이틀
  VIEW_MAP_DETAIL_INFO_TITLE = (AppiumBy.ACCESSIBILITY_ID, '위치 상세 정보') # 위치 상세 정보 타이틀

  MAP_DETAIL_UI_LOCS = [VIEW_MAP_DETAIL_TITLE, VIEW_MAP_DETAIL_INFO_TITLE]

  @staticmethod
  def location_name_icon(location_name: str):
    return (AppiumBy.ACCESSIBILITY_ID, f'{location_name}')
  
  BACK_BTN_MAP_DETAIL = (AppiumBy.ACCESSIBILITY_ID, '뒤로') # 뒤로가기 버튼

  UI_CHECK_LOCS = [GALLERY_ICON, CAMERA_ICON, USER_ICON, PACKAGE_ICON, MAP_ICON]

#로케이터들이 사용자 닉네임이나, 장소 이름 등에 따라서 바뀌는게 많아서 자동화 가능할지 한번 코드 작성해봐야할듯!