from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *

class SignInPage(BasePage):
    def __init__(self, driver):
        self.locator = locators.SignInPageLocator
        super(SignInPage, self).__init__(driver)

    def signIn(self, email, password):
        self.find_element2(*self.locator.email).send_keys(email)
        self.find_element2(*self.locator.password).send_keys(password)
        self.find_element2(*self.locator.signInBtn).click()

    def signin(self):
        self.signIn(testcase_data.account, testcase_data.password)
