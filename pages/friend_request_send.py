import os
import pathlib
from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
from time import sleep
from datetime import datetime


class SendingFriendRequest(BasePage):
    def __init__(self, driver):
        self.locator = locators.SendingFriendRequest

        super(SendingFriendRequest, self).__init__(driver)

    def accept_alert_message(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            print("No alert found")

    def go_to_profile_page(self, link):
        self.driver.get(link)

    def click_send_request(self):
        try:
            self.click(*self.locator.friend_request)
            message = "Friend Request Button Found and clicked"
            self.accept_alert_message()
        except:
            message = "Friend Request Button Not Found"
        print(message)

    def checking_status(self):
        try:
            self.find_element2(*self.locator.send_message)
            message = "Friend Request send Successfully"
        except:
            message = "Not send"
        print(message)
        return message

    def totalPeopleList(self):
        countstart = read(testcase_data.counter_path)
        countend = readWriteBy20(testcase_data.counter_path)
        people_list = read_portion_col_data(testcase_data.People_list_file_path, testcase_data.People_list, countstart,
                                            countend, 2)
        return people_list

    def send(self):
        totalpeople = getRowCount(testcase_data.People_list_file_path, testcase_data.People_list)
        loop = int(totalpeople / 20)
        for i in range(loop):
            print("*" * 80)
            peoples = self.totalPeopleList()
            print(peoples)
            for people in peoples:
                print(people)
                self.go_to_profile_page(people)
                self.click_send_request()
                sleep(5)
                status = self.checking_status()
                if status == "Friend Request send Successfully":
                    data = ["send"]
                    writecolautomatic(testcase_data.People_list_file_path, testcase_data.log,data)
