import time

from Locators.LoginPageLocator import *
from Utilities.CommonUtilities import CommonUtil


class LoginPageFunction:
    cu = CommonUtil()

    def perform_login(self, mobile_no: int):
        """
        This function perform login with the given mobile number
        :param mobile_no: Integer
        :return: None
        """
        self.fill_number(mobile_no)
        self.cu.click_element(submit_btn)
        time.sleep(30)

    def fill_number(self, mobile_no: int):
        """
        This function fill the given mobile number
        :param mobile_no: Integer
        :return: None
        """
        self.cu.fill_data(mobile_no_field, mobile_no)
