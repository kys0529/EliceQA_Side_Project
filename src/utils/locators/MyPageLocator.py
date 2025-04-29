from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

"""
스크린샷으로 비교해야 하는 항목 (LOCATOR 추출 불가)
- 프로필 페이지
  └ 프로필 사진
  └ 프로필 배경
  └ 별점 별 갯수

  ※ Class 제거 작업 예정 - 로케이터 선언 시 변수명이 너무 길어짐
"""


class MypageMainLocator:  # 마이페이지 메인 & UI 공통 LOCATOR 모음 - 작업 완료
    # 계정 유형 공통 - 작업 완료
    MYPAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "마이페이지")
    MYPAGE_TAB = (AppiumBy.ACCESSIBILITY_ID, "마이페이지\n탭 4개 중 4번째")
    THEME_TOGGLE_BTN = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(5)',
    )
    MY_RESERVATION_LIST_MENU = (
        AppiumBy.ACCESSIBILITY_ID,
        "내 예약 내역\n예약한 패키지를 확인합니다",
    )
    MY_FAVORITE_PACKAGE_MENU = (
        AppiumBy.ACCESSIBILITY_ID,
        "찜한 패키지\n관심 있는 패키지를 확인합니다",
    )
    LOGOUT_BTN = (AppiumBy.ACCESSIBILITY_ID, "로그아웃")

    @staticmethod
    def get_user_profile_locator(nickname, email):
        USER_PROFILE_MENU = (AppiumBy.ACCESSIBILITY_ID, f"{nickname}\n{email}")
        return USER_PROFILE_MENU

    # 가이드 계정 Only - 작업 완료
    MAKE_MY_PACKAGE_MENU = (
        AppiumBy.ACCESSIBILITY_ID,
        "나만의 패키지 만들기\n새로운 여행 패키지를 등록합니다",
    )
    MY_PACKAGE_RESERVATION_MNG_MENU = (
        AppiumBy.ACCESSIBILITY_ID,
        "내 패키지 예약 관리\n등록한 패키지의 예약을 관리합니다",
    )
    MY_PACKAGE_MNG_MENU = (
        AppiumBy.ACCESSIBILITY_ID,
        "내 패키지 관리\n등록된 패키지 수정하거나 삭제합니다",
    )

    # 일반 계정 Only - 작업 완료
    GUIDE_CERTIFICATON_MENU = (
        AppiumBy.ACCESSIBILITY_ID,
        "가이드 인증\n가이드 인증을 진행하세요",
    )

    # UI 공통 항목 (팝업 공통 버튼, 뒤로가기 등)
    MYPAGE_BACK = (AppiumBy.ACCESSIBILITY_ID, "뒤로")
    MYPAGE_POPUP_CANCEL = (AppiumBy.ACCESSIBILITY_ID, "취소")
    MYPAGE_POPUP_COMFIRM = (AppiumBy.ACCESSIBILITY_ID, "확인")


class MypageProfileLocator:  # 프로필 페이지 LOCATOR 모음 - 작업 완료
    # 계정 공통 - 작업 완료
    @staticmethod
    def get_profile_title_locator(nickname):
        PROFILE_PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, f"{nickname} 님의 프로필")
        return PROFILE_PAGE_TITLE

    @staticmethod
    def get_my_account_type(accountType):
        MY_ACCOUNT_TYPE = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{accountType}")',
        )
        return MY_ACCOUNT_TYPE

    FLOATING_ICON = (  # 접힘 상태 / 펼침 상태 모두 LOCATOR 값 동일
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)',
    )
    FLOATING_MODIFY_INFO_ICON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(2)',
    )
    FLOATING_BACKGROUND_MODI_ICON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(3)',
    )
    FLOATING_BACKGROUND_DEL_ICON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(4)',
    )

    @staticmethod
    def get_profile_nickname(nickname):
        PROFILE_NICKNAME = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{nickname}")',
        )
        return PROFILE_NICKNAME

    @staticmethod
    def get_profile_introduce(introduce):
        PROFILE_INTRODUCE = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().description("{introduce}")',
        )
        return PROFILE_INTRODUCE

    PROFILE_MORE = (  # 가이드 / 일반 계정 모두 '더보기' Locator 동일
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("더보기")',
    )

    # 가이드 계정 ONLY - 작업 완료
    @staticmethod
    def get_star_score(starscore):
        PROFILE_MY_STAR_SCORE = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f"평균 별점 {starscore}점",
        )
        return PROFILE_MY_STAR_SCORE

    @staticmethod
    def get_review_count(reviewcount):
        PROFILE_MY_REVIEW_COUNT = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f"리뷰 {reviewcount}개",
        )
        return PROFILE_MY_REVIEW_COUNT

    PROFILE_GUIDE_PAKAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "가이드 패키지")
    PROFILE_GUIDE_PAKAGE_SECTION = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(13)',
    )

    # 프로필 가이드 각 항목 (CLASS)
    PROFILE_GUIDE_PACKAGE_ITEM = (By.CLASS_NAME, "android.widget.ImageView")
    PROFILE_GUIDE_PACKAGE_SECTION = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(13)',
    )

    # 일반 계정 ONLY - 작업 완료
    PROFILE_RECENT_REVIEW_TITLE = (AppiumBy.ACCESSIBILITY_ID, "최근에 작성한 리뷰")
    PROFILE_RECENT_REVIEW_SECTION = (
        AppiumBy.ACCESSIBILITY_ID,
        'new UiSelector().className("android.view.View").instance(10)',
    )


class MypagePWDConfirm:  # 비밀번호 확인 팝업 LOCATOR 모음 - 작업 완료
    PWD_CONFIRM_POPUP_SECTION = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(3)',
    )
    PWD_CONFIRM_POPUP_TITLE = (AppiumBy.ACCESSIBILITY_ID, "비밀번호 확인")
    PWD_CONFIRM_POPUP_INPUT = (
        By.CLASS_NAME,
        "android.widget.EditText",
    )  # Placeholder나 입력 문구 확인 시 hint 속성 확인하기


class MypageModifyPage:  # 회원 정보 수정 페이지 LOCATOR 모음 - 작업 필요
    MYPAGE_MODI_TITLE = (AppiumBy.ACCESSIBILITY_ID, "회원 정보 수정")
    MYPAGE_MODI_PROFILE_IMG = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(6)',
    )

    @staticmethod
    def get_modify_nickname_input(nickname):
        MYPAGE_MODI_NICKNAME_INPUT = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{nickname}")',
        )
        return MYPAGE_MODI_NICKNAME_INPUT

    @staticmethod
    def get_modify_email_textview(email):
        MYPAGE_MODI_EMAIL_TEXTVIEW = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{email}")',
        )
        return MYPAGE_MODI_EMAIL_TEXTVIEW

    @staticmethod
    def get_modify_introduce_input(introduce):
        MYPAGE_MODI_INTRODUCE_INPUT = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{introduce}")',
        )
        return MYPAGE_MODI_INTRODUCE_INPUT

    MYPAGE_MODI_GENDER_MAN = (AppiumBy.ACCESSIBILITY_ID, "남성")
    MYPAGE_MODI_GENDER_WOMAN = (AppiumBy.ACCESSIBILITY_ID, "여성")
    MYPAGE_MODI_BIRTH_ICON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(3)',
    )
    MYPAGE_MODI_BIRTH_CAL_POPUP = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(3)',
    )
    # 날짜 직접 입력 / 캘린더 뷰 모드 전환 아이콘
    MYPAGE_MODI_BIRTH_CAL_MODE_ICON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(0)',
    )

    @staticmethod
    # 생일 캘린더 날짜 직접 입력 모드 전환 시 나오는 input
    def get_modi_birth_cal_date_input(birthdate):
        MYPAGE_MODI_BIRTH_CAL_DATE_INPUT = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{birthdate}")',
        )
        return MYPAGE_MODI_BIRTH_CAL_DATE_INPUT

    # 달력 날짜 선택은 일단 직접 입력 모드로만 우선 확인해보는걸로.. 캘린더뷰 선택 완전 난감..

    MYPAGE_MODI_SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, "저장")
    MYPAGE_MODI_WITHDRAW = (AppiumBy.ACCESSIBILITY_ID, "회원 탈퇴")


class MypageMyRes:  # 내 예약 내역 페이지 LOCATOR 모음 - 작업 필요
    MY_RESERVATION_TITLE = (AppiumBy.ACCESSIBILITY_ID, "내 예약 내역")


class MypageMyFavorPkg:  # 찜한 패키지 페이지 LOCATOR 모음 - 작업 필요
    MY_FAVOR_PACKAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "찜한 패키지")


class MypageMakeMyPkg:  # 가이드 계정 - 나만의 패키지 만들기 페이지 LOCATOR 모음 - 작업 필요
    MAKE_MY_PKG_TITLE = (AppiumBy.ACCESSIBILITY_ID, "새 패키지 등록")


class MypagePkgRes:  # 가이드 계정 - 내 패키지 예약 관리 페이지 LOCATOR 모음 - 작업 필요
    MY_PKG_RES_TITLE = (AppiumBy.ACCESSIBILITY_ID, "예약 관리")


class MypageManageMyPkg:  # 가이드 계정 - 내 패키지 관리 페이지 LOCATOR 모음 - 작업 필요
    MANAGE_MY_PKG_TITLE = (AppiumBy.ACCESSIBILITY_ID, "내 패키지 관리")


class MypageReviewspage:  # 일반 계정 - 작성한 리뷰 페이지 LOCATOR 모음 - 작업 필요
    def get_reviews_title_nickname(nickname):
        MY_REVIEWS_TITLE = (AppiumBy.ACCESSIBILITY_ID, f"{nickname} 님이 작성한 리뷰")
        return MY_REVIEWS_TITLE


class MypageGuideCertPage:  # 일반 계정 - 가이드 인증 페이지 LOCATOR 모음 - 작업 필요
    GUIDE_CERTIFICATION_TITLE = (AppiumBy.ACCESSIBILITY_ID, "가이드 인증")
