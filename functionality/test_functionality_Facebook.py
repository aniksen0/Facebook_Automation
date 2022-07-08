from Pages.signin_page import SignInPage
from functionality.base_test import BaseTest
from Pages.group_post_page import GroupPost
from Pages.PeopleList import PeopleList
from Pages.friend_request_send import SendingFriendRequest


class TestVerifySignIn(BaseTest):

    def test_signin(self):
        page_signin = SignInPage(self.driver)
        page_signin.signin()
        print("Sign-In Successful")
        # page2 = GroupPost(self.driver)
        # page2.post()
        page3 = PeopleList(self.driver)
        page3.collect()
        function4_friend_request = SendingFriendRequest(self.driver)
        function4_friend_request.send()

# python3 -m unittest functionality.test1
# python3 -m pytest -s functionality/test_functionality_Facebook.py --alluredir=ReportAllure &&  allure serve ReportAllure/
