import os
from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
from time import sleep
from datetime import datetime
from pathlib import Path


class GroupPost(BasePage):
    def __init__(self, driver):
        self.locator = locators.PostingLocators
        super(GroupPost, self).__init__(driver)

    def accept_alert_message(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            print("No alert found")

    def group_posting(self, message):
        # all the variable which you have to change according to your need
        sheetpath = Path(__file__).parent.parent / "utils/grouplist.xlsx"
        print("*" * 80)
        print(sheetpath)
        imagepath = os.getcwd() + "\image\hire.png"
        datacounterpath = Path(__file__).parent.parent / "utils/datacounter.txt"
        allsheetname = allsheetName(sheetpath)
        images_list = [imagepath]

        datacounter = readWrite(datacounterpath)
        sheetcount = len(allsheetname)
        for i in range(8, sheetcount + 1):
            sheetname = allsheetname[i]
            groups_links_list = readallsheetdata(sheetpath, sheetname, 1, 3)
            print("this is a group list {0}".format(groups_links_list))
            # Post on each group
            for group in groups_links_list:
                print("this is group link{0}".format(group))
                i = readWrite(datacounterpath) + 1
                self.driver.get(group)
                sleep(2)
                self.accept_alert_message()
                try:
                    for photo in images_list:
                        photo_element = self.driver.find_element(*self.locator.imageInput)
                        photo_element.send_keys(photo)

                    sleep(2)
                    try:
                        post_box = self.driver.find_element(*self.locator.postbox)
                        post_box.click()
                        sleep(2)
                        message2 = message + "\n" + "Post Id:" + str(i) + "\n"
                        post_box.send_keys(message2)
                        sleep(2)
                        post_button = self.driver.find_element(*self.locator.postbutton)
                        post_button.click()
                        sleep(5)
                        errorData = [i, f"Posted->Done grouplink: {group}", str(datetime.now()), "No issues"]
                        writecol(sheetpath, testcase_data.log, i, errorData)
                    except:

                        # garbage1placeholder
                        # clicking Post button
                        errorData = [i, f"grouplink: {group} couldn't post ", str(datetime.now()), "Post Blocking off"]
                        writecol(sheetpath, testcase_data.log, i, errorData)
                except:
                    print("No input field found.")
                    errorData = [str(i), f"grouplink: {group}not posted due to blocked issue", str(datetime.now()),
                                 "not posted"]
                    writecol(sheetpath, testcase_data.log, i, errorData)

    def post(self):
        self.group_posting(testcase_data.group_post_message)
