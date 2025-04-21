import time
from pages.loginpage import LoginPage
from config import config
from utility import utility

class Test_Class_Login:

    def test_01(self, setup_teardown):
        driver = setup_teardown
        login_page = LoginPage(driver)

        home_page = login_page.do_login(config.username_value, config.password_value)

        time.sleep(2)

        assert utility.get_page_title(driver) == "ParaBank | Accounts Overview", "Page title does not match"

        print(utility.get_page_title(driver))
