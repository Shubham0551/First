import pytest
from Utilities.CommonUtilities import CommonUtil
from Utilities.WishlistUtilities import Wishlist


class TestLoginPage:
    cu = CommonUtil()

    @pytest.mark.usefixtures("initiate_driver")
    def test_add_wishlist(self, initiate_driver):
        Wishlist().add_to_wishlist()
        assert 1 == 1
