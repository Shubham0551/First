import pytest
from Config.configdata import *
from Locators.HomePageLocator import *
from Locators.BuyProductLocator import *
from Utilities.CommonUtilities import CommonUtil
from Utilities.BuyProductUtilities import BuyProduct


class TestLoginPage:
    cu = CommonUtil()

    @pytest.mark.usefixtures("initiate_driver")
    def test_buy_product(self, initiate_driver):
        BuyProduct().buy_product(search_item=item, select_item=shirt_link, size=size_btn)
        view_summary = self.cu.get_element_text(summary)
        assert "Price Summary" == view_summary, "User unable to buy product"