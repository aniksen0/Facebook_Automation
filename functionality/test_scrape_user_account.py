from Pages.signin_page import SignInPage
from functionality.base_test import BaseTest
from Pages.PeopleList import PeopleList


class TestScrapeUser(BaseTest):

    @staticmethod
    def test_signin(self):
        page_signin = SignInPage(self.driver)
        page_signin.signin()
        page3 = PeopleList(self.driver)
        page3.collect()

# python3 -m unittest functionality.test1
# python3 -m pytest -s functionality/test_functionality_Facebook.py --alluredir=ReportAllure &&  allure serve ReportAllure/
