from src.pages.Login import Login
import pytest
import time

@pytest.mark.usefixtures("login_driver")
class TestLR01:
    def test_lr_01_01(driver):
        print("test_1")
        time.sleep(2)
    def test_lr_01_02(driver):
        print("test_2")
        time.sleep(2)