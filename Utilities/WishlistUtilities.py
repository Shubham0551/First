from selenium.webdriver.common.by import By

from Locators.LoginPageLocator import login_btn
import time
from conftest import driver
from Locators.WishlistLocators import *
from Utilities.BuyProductUtilities import BuyProduct
from Locators.HomePageLocator import *
from Utilities.LoginPageUtilities import LoginPageFunction
from Utilities.CommonUtilities import CommonUtil
from Locators.BuyProductLocator import *
from Config.configdata import *


class Wishlist:

    cu = CommonUtil()

    def add_to_wishlist(self):
        """
        This function will perform add to wish list option
        :return:
        """
        self.cu.click_element(account_btn)
        self.cu.click_element(login_btn)
        LoginPageFunction().perform_login(mobile_no)
        BuyProduct().search_product(wish_item)
        BuyProduct().select_product(wishlist_item)
        tabs = driver.window_handles
        # print(tabs)
        driver.switch_to.window(tabs[1])
        time.sleep(5)
        self.cu.click_element(add_to_bag)
        time.sleep(4)
        self.cu.click_element(view_bag)
        time.sleep(4)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        self.cu.click_element(move_wishlist)
        driver.switch_to.window(tabs[1])
        self.cu.click_element(wishlist_btn)
        tabs2 = driver.window_handles
        print(tabs2)
