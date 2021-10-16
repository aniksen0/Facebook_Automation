from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("F:\Anik Working Demo Directory\Python-Selenium-Facebook-group-auto-poster\/browser\chromedriver.exe")
driver.get("https://evaly.com.bd/")
driver.maximize_window()
#advertise closing
driver.find_element_by_xpath('//button[@class="absolute top-0 right-0 p-2 text-black"]').click()
# logging in
driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]/span[1]").click()
time.sleep(1)

driver.implicitly_wait(1)
phone = driver.find_element(By.NAME, "phone")
passw = driver.find_element_by_name("password")
phone.send_keys("01630524832")
passw.send_keys("zpxtLwCA6AvA@$*")
driver.find_element_by_xpath("//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()

#clicking speaker
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element_by_xpath('//a[@href="/categories/speaker-2f615cf9a"]').click()
driver.implicitly_wait(5)
time.sleep(5)



#finding all the brand name
list_of_hrefs = []

# for ele in  driver.find_elements_by_xpath('//p[@class="BrandCard___StyledP-sc-1kq2v0k-1 bAWFRI text-sm font-semibold text-center cursor-pointer"]'):
#     print(ele.text)


content_blocks = driver.find_elements(By.CSS_SELECTOR, "div.CategoryBrand__GridCategory-sc-17tjxen-0.PYjFK.my-4")
for block in content_blocks:
    elements = block.find_elements_by_tag_name("p")
    for el in elements:
        list_of_hrefs.append(el.text)
print(list_of_hrefs)
#
for name in list_of_hrefs:

    with open("brandName.txt", "a", encoding="utf-8") as f:
        f.write(str(name)+" ")
print(driver.title)
#2nd task
#clicking MI brand and comparing price
driver.implicitly_wait(5)
time.sleep(5)
link1 = []
name1 = []
price1 = []
driver.find_element_by_xpath('//a[@href="/brands/xiaomi-004a023b8?category=speaker-2f615cf9a"]').click()

product = driver.find_elements_by_xpath('//div[@class="slug__Grid-vcgsbx-0 hPFNJV pb-24 my-4 md:pb-4"]')
for individual in product:
    productlink = individual.find_elements_by_tag_name("a")
    for link in productlink:
        link1.append(link.get_attribute('href'))
        print(link.get_attribute('href'))
        allp = link.find_elements_by_tag_name("p")

productprice=driver.find_elements_by_xpath('//div[@class="p-4 pt-0"]//p')
productname=driver.find_elements_by_xpath('//p[@class="Card___StyledP4-sc-1629dl9-4 fWEsJX text-sm text-gray-800"]')
for price in productprice:
    print(price.text)
    price1.append(price.text)
for name in productname:
    print(name.text)
    name1.append(name.text)

index = 0
highvalue = 0
highvalueindex = 0
for high in price1:
    newhigh=high.replace("৳", "0")
    if highvalue < int(newhigh):
        highvalueindex = index
        highvalue = int(newhigh)
        print(highvalue)
        index = index + 1
url = (link1[highvalueindex])

driver.get(url)
print("this is the url::{0}".format(url))
print("here is the index url::{0} and highest value::{1} ".format(highvalueindex, highvalue))

# driver.find_element_by_xpath('//div[@class="relative flex flex-col justify-center h-full overflow-hidden bg-white rounded-lg cursor-pointer product-card hover:shadow-md"]').click()


#3rd Task

#4th Task

driver.get("https://evaly.com.bd/career/")
option=driver.find_elements_by_xpath('//div[@class="flex items-center justify-between px-4 py-3 mb-4 bg-gray-200 cursor-pointer"]')
for ll in option:
    ll.click()

name = {}
email=[]
# mb-2 font-semibold text-gray-600
content_blocks = driver.find_elements_by_xpath('//p[@class="mb-2 font-semibold text-gray-600"]')
domain="evaly.com.bd"
for block in content_blocks:
    elements = block.find_elements_by_tag_name("a")
    for el in elements:
        if(domain in el.text):
            email.append(el.text)

        else:
            email.append("this is not contain required domain "+el.text)
print("email:{0}".format(email))
time.sleep(6)
driver.quit()