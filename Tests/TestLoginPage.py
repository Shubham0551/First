import pytest
from Config.configdata import *
from Locators.HomePageLocator import *
from Locators.LoginPageLocator import *
from Utilities.CommonUtilities import CommonUtil
from Utilities.LoginPageUtilities import LoginPageFunction


class TestLoginPage:
    cu = CommonUtil()

    @pytest.mark.usefixtures("initiate_driver")
    def test_login_function(self, initiate_driver):
        self.cu.click_element(account_btn)
        self.cu.click_element(login_btn)
        LoginPageFunction().perform_login(mobile_no=mobile_no)
        self.cu.click_element(account_btn)
        login_success = self.cu.get_element_text(hi_user)
        assert "Hi user!" == login_success, "User not able to login with correct mobile number and otp"

    @pytest.mark.parametrize('mobile_field',
                             [("72380302741"), ("7238030274"), (""), ("shubham")])
    def test_login_function_with_invalid_details(self, initiate_driver, mobile_field):
        self.cu.click_element(account_btn)
        LoginPageFunction().perform_login(mobile_no=mobile_field)
        # login_unsuccessful = self.cu.get_element_text(error_msg)
        # assert "Error!" == login_unsuccessful, "User able to login with incorrect details"
