from src.pages.BasePage import BasePage
from src.utils.locators import MyPageLocator


class MyPage(BasePage):
    def __init__(self, driver, page_name="MyPage"):
        super().__init__(driver, page_name)

    def get_nickname(self):  # 로그인 후 닉네임 값 받아오기
        current_user_nickname = self.get_attribute(
            MyPageLocator.MypageMain.LOGIN_TOAST, "content-desc"
        ).replace(
            "님 환영합니다!", ""
        )  # 토스트 내용에서 닉네임 영역만 남김
        return current_user_nickname

    def into_mypage(self):  # 마이페이지 탭 진입
        self.click_element(MyPageLocator.MypageMain.MYPAGE_TAB)

    def into_profile_page(self):  # 프로필 페이지 진입
        self.click_element(MyPageLocator.MypageMain.PROFILE_PHOTO)
