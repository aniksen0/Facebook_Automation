#DISCLAIMER
Any actions and or activities related to the material contained within this repo is solely your responsibility. The misuse of the information in this repo can result in criminal charges brought against the company in question. The author will not be held responsible in the event any criminal charges be brought against any individuals misusing the information in this repo to break the law.

As written in Facebook User Agreement: you agree you will not use

bots or other automated methods to access the Services, add or download contacts, send or redirect messages.
###Terms And Conditions:
I do not promote, encourage, support or excite any illegal activity or hacking without written permission in general. The repo and author of the repo is no way responsible for any misuse of the information.
"Python-selenium-facebook-group-auto-poster" is just a terms that represents the name of the repo and is not a repo that provides any illegal information.
This repo is totally meant for providing information on Computer Software, Computer Programming and other related topics.
The Software's and Scripts provided by the repo should only be used for education purposes. The repo or the author can not be held responsible for the misuse of them by the users.
I am not responsible for any direct or indirect damage caused due to the usage of the code provided on this site. All the information provided on this repo are for educational purposes only.


# Facebook automation tools

## Installation
##### Use the package manager pip to install project dependency

    $ cd to the directory where requirements.txt is located
    $ run: pip3 install -r requirements.txt


## Run Project

    $ cd to the "Test/ui" directory
    $ run: python3 testconf/runtest.py


## Run individual testcase

 ##### run test using unittest

    $ cd to the "Test" directory
    $ python3 -m unittest TestCase.TC_file_name (without.py)
    
##### run test with allure report

    $ cd to the "Test" directory
    $ python -m pytest -s TestCase/TC_file_name.py --alluredir=ReportAllure &&  allure serve ReportAllure/

# Python-Selenium-Facebook-group-auto-poster
A Python script use Selenium to achieve automatically posting images with text on multiple Facebook groups that you are the member of.

Setup
----------
 - First of all, install [Python 3](https://www.python.org/downloads/) into your machine
 
 - Then insall selenium:
   ```
   pip install selenium
   ```
 - Download the [Chrome Driver](http://chromedriver.chromium.org/downloads) and place it in the same directory with the script.
 
Configure the script
----------
You need to edit the script to provide your Facebook account name and password, the message you want to post, whether you want to attach an image, along with its path and the links of the Facebook groups you are the member of:
``` 
def main():
    # Set up Facebook login account name and password
    account = "sample@gmail.com"
    password = "sample"

    # Set up Facebook groups to post, you must be a member of the group
    groups_links_list = [
        "https://www.facebook.com/groups/sample1", "https://www.facebook.com/groups/sample2"
    ]

    # Set up text content to post
    message = "Checkout an amazing selenium script for posting automaticaaly on Facebook groups! https://github.com/ethanXWL/Python-Selenium-Facebook-group-poster"

    # Set up paths of images to post
    images_list = ['C:/Users/OEM/Pictures/sample1.jpg','C:/Users/OEM/Pictures/sample2.jpg']
 ```
 
After that, run the script by double click on it. Enjoy!

extended configuration
You have to update the xlsx file(excel file) name grouplist.xlsx where you can add the group link.
and after adding credential you if run the code it will automatically generate log file in excel and also it will post if you joined or the group let you post the discussion.

Here is the some limitation:
This bot can't detect the previous post and can't detect if you are joined in the group. If it didn't find any input field it will simply generate a log history where it will say "due to blocking it couldn't post the discussion".
It also lack some of the visualization. it doesn't generate any message whether you have already posted on the group or not also it didn't automatically join you in the group.
please use cautiously. If your account get blocked, developer isn't responsible for that.

