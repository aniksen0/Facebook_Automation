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

