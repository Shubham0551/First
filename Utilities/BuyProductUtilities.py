import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from conftest import driver
from Locators.BuyProductLocator import *
from Locators.HomePageLocator import *
from Utilities.CommonUtilities import CommonUtil


class BuyProduct:

    cu = CommonUtil()

    def buy_product(self, search_item: str, select_item: str, size: str):
        """
        This will buy the product
        :param search_item: String
        :param select_item: String
        :param size: String
        :return:
        """
        self.search_product(search_item)
        self.select_product(select_item)
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        self.select_size(size)
        self.buy_now()
        # time.sleep(3)
        # driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        # LoginPageFunction().perform_login(mobile_no=mobile_no)
        # time.sleep(30)
        # self.proceed_to_pay()

    def search_product(self, search_item: str):
        """
        This will search the product
        :param search_item: String
        :return: None
        """
        self.cu.fill_data(search_box, search_item)
        self.cu.fill_data(search_box, Keys.ENTER)

    def select_product(self, select_item):
        """
        It will select the product
        :param select_item:
        :return:
        """
        self.cu.click_element(select_item)

    def select_size(self, size: str):
        """
        It will select the size
        :param size:
        :return:
        """
        time.sleep(2)
        self.cu.click_element(size)

    def buy_now(self):
        """
        This will perform add to bag and checkout option
        :return:
        """
        self.cu.click_element(add_to_bag)
        time.sleep(4)
        self.cu.click_element(view_bag)
        time.sleep(4)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        self.cu.click_element(buy_now)

    def proceed_to_pay(self):
        """
        It will click on final payment option
        :return:
        """
        self.cu.click_element(procced_to_pay)
