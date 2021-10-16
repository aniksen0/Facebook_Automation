import os
from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
from time import sleep
from datetime import datetime
from pathlib import Path


class PeopleList(BasePage):
    def __init__(self, driver):
        self.locator = locators.PeopleList
        super(PeopleList, self).__init__(driver)

    def accept_alert_message(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            print("No alert found")

    def search_facebook(self,searchkeyword):
        self.click(*self.locator.searchField)
        sleep(5)
        self.send_data(searchkeyword, *self.locator.searchField)
        sleep(5)
        self.press_enter_key(*self.locator.searchField)
        sleep(5)

    def click_people_menu(self):
        self.click(*self.locator.people_menu)

    def scrolling(self):
        for i in range(0, 100):
            try:
                self.find_element2(*self.locator.end_of_result)
                break
            except:
                self.goto_bottom()
            sleep(4)

    def scrapping_data(self):
        try:
            allpeople = self.find_elements(*self.locator.allpeople)
            for people in allpeople:
                name = people.find_element(*self.locator.name).text
                id_link = people.find_element(*self.locator.id_link).get_attribute("href")
                data = [name, id_link]
                writecolautomatic(testcase_data.People_list_file_path, testcase_data.People_list, data)
        except:
            data = ["NONE"]
            writecolautomatic(testcase_data.People_list_file_path, testcase_data.People_list, data)

    def totalKeyword(self):
        allkey = readallsheetdata(testcase_data.filepath, testcase_data.SearchKeyword_sheet, 6, 3)
        return allkey

    def collect(self):
        keyword = self.totalKeyword()
        totalkey = len(keyword)
        for i in range(0, totalkey+1):
            self.search_facebook(keyword[i])
            sleep(4)
            self.click_people_menu()
            sleep(4)
            self.scrolling()
            sleep(4)
            self.scrapping_data()
