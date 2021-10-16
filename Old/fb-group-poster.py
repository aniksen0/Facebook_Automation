from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import pyautogui
import openpyxl
from openpyxlfunction import *
import os
import data

sheetpath = os.getcwd() + "\grouplist.xlsx"
sheetforlog = data.log
datacounterpath = os.getcwd() + "\datacounter.txt"
message2 = 'QUPS (Quality Up Services) is looking for Intern Software Engineer (JAVA/Python/JS Track)||' \
          'Program Name : 1000 USD Internship Program' \
          'Application Subject : Intern Software Engineer (Part Time/Full Time)' \
          'Interested Applicants, please apply at ( "hr.qups@gmail.com " CC "qups.xyz@gmail.com" )'


def group_posting():
    # Set up Facebook login account name and password
    account = "hexibo6791@0ranges.com"
    password = "yamin787898"
    # Set up Facebook groups to post, you must be a member of the group
    # Set up text content to post
    message = message2
    # Set up paths of images to post
    images_path1 = os.getcwd() + "/logo.png"
    images_list = [images_path1]
    # Login Facebook
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.facebook.com')
    driver.maximize_window()
    emailelement = driver.find_element(By.XPATH, '//*[@id="email"]')
    emailelement.send_keys(account)
    passelement = driver.find_element(By.XPATH, '//*[@id="pass"]')
    passelement.send_keys(password)
    loginelement = driver.find_element(By.XPATH, '//button[@data-testid="royal_login_button"]')
    loginelement.click()
    time.sleep(5)
    #getting allsheetname
    allsheet = allsheetName(sheetpath)
    sheetcount = totalsheetcount(sheetpath)
    for i in range(18,sheetcount+1):
        sheetname = allsheet[i]
        groups_links_list = readallsheetdata(sheetpath, sheetname, 3)
        print("this is a group list {0}".format(groups_links_list))
        # Post on each group
        for group in groups_links_list:
            print("this is group link{0}".format(group))
            i = readWrite(datacounterpath) + 1
            driver.get(group)
            try:
                alert = driver.switch_to.alert
                alert.accept()
            except:
                print("No alert found")
            time.sleep(1)
            try:
                for photo in images_list:
                    photo_element = driver.find_element(By.XPATH, '//input[@type="file"]')
                    photo_element.send_keys(photo)
                    time.sleep(1)
                time.sleep(5)
                try:
                    post_box = driver.find_element_by_xpath(
                        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
                    post_box.click()
                    time.sleep(2)
                    post_box.send_keys(message)
                    time.sleep(2)
                    driver.find_element_by_css_selector(
                        "body._6s5d._71pn._-kb.segoe:nth-child(2) div.rq0escxv.l9j0dhe7.du4w35lb div.__fb-light-mode.l9j0dhe7.tkr6xdv7 div.rq0escxv.l9j0dhe7.du4w35lb:nth-child(1) div.j83agx80.cbu4d94t.h3gjbzrl.l9j0dhe7 div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p:nth-child(2) div.gs1a9yip.rq0escxv.j83agx80.cbu4d94t.kb5gq1qc.taijpn5t.h3gjbzrl div.ll8tlv6m.rq0escxv.j83agx80.taijpn5t.pnzxbu4t.hpfvmrgz.hzruof5a.dflh9lhu.scb9dxdr.q5pvgw0d.l7iv3u6u.f59ohtjy.aw1xchsf div.cjfnh4rs.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.lzcic4wl.ni8dbmo4.stjgntxs.oqq733wu.cwj9ozl2.io0zqebd.m5lcvass.fbipl8qg.nwvqtn77.nwpbqux9.iy3k6uwz.e9a99x49.g8p4j16d.bv25afu3.d2edcug0 div.idiwt2bm.lzcic4wl.ni8dbmo4.stjgntxs.l9j0dhe7.dbpd2lw6 div.rq0escxv.pmk7jnqg.du4w35lb.pedkr2u6.oqq733wu.ms05siws.pnx7fd3z.b7h9ocf4.j9ispegn.kr520xx4:nth-child(1) div.idiwt2bm.lzcic4wl.ni8dbmo4.stjgntxs.l9j0dhe7.dbpd2lw6:nth-child(1) div.rq0escxv.pmk7jnqg.du4w35lb.pedkr2u6.oqq733wu.ms05siws.pnx7fd3z.b7h9ocf4.j9ispegn.kr520xx4:nth-child(1) div.k4urcfbm.l9j0dhe7.datstx6m.rq0escxv div.l9j0dhe7 div.j83agx80.btwxx1t3 div.j83agx80.cbu4d94t.f0kvp8a6.mfofr4af.l9j0dhe7.ij1vhnid.smbo3krw.oh7imozk div.ihqw7lf3.discj3wi.l9j0dhe7:nth-child(3) div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.hv4rvrfc.dati1w0a.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.p8fzw8mz.pcp91wgn.iuny7tx3.ipjc6fyt > div.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.pq6dq46d.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.l9j0dhe7.abiwlrkh.p8dawk7l.cbu4d94t.taijpn5t.k4urcfbm").click()
                    errorData = [i, "Posted->Done", str(datetime.now()), "No issues"]
                    writecol(sheetpath, sheetforlog, i, errorData)
                except:

                    # garbage1placeholder
                    # clicking Post button
                    errorData = [i, "couldn't post", str(datetime.now()), "Post Blocking off"]
                    writecol(sheetpath, sheetforlog, i, errorData)

                time.sleep(5)
            except:
                print("No input field found.")
                errorData = [str(i), "not posted due to blocked issue", str(datetime.now()), "not posted"]
                writecol(sheetpath, sheetforlog, i, errorData)
            # except:
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("TAB")
            #     # pyautogui.press("ENTER")
            #     time.sleep(5)
    driver.quit()


# Close driver
group_posting()
