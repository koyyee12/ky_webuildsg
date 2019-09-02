import os
import json
import time
import pytest
import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# using ChromeDriver
# get path of ChromeDriverServer
print (__file__)
dir = os.path.dirname(os.path.realpath(__file__))

# only runnable in Mac or Linux
chrome_driver_path = dir + "/chromedriver/chromedriver"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to main page
driver.get("https://webuildsg.github.io/data/")

# get search keyword
f = open(dir + "/data/main/search/search_keyword.json")
data = json.load(f)
f.close()

# get the list of search keywords in json file
for obj in data[:]:
    for (k, v) in obj.items():
        # enter search keyword
        if (k == "keyword"):
            # get the search textbox
            search_txtbox = driver.find_element_by_id("search")
            search_txtbox.send_keys(v)
            search_txtbox.clear()
        # verify results
        if (k == "results"):
            for r in v:
                assert (r in driver.page_source)
                driver.find_element_by_xpath('//p[contains(text(), "' + r + '")]').click()
                driver.back()
        
# verify the contents
f_main_contents = open(dir + "/data/main/main_contents.json")
main_contents = json.load(f_main_contents)
f_main_contents.close()


list_ui_text = []
list_elm_text = []
# get the list of main contents in json file
for data in main_contents[:]:
    for (k, v) in data.items():
        # get element id
        if (k == "id"):
            numbers = driver.find_element_by_id(v).text
        if (k == "info"):
            list_ui_text.append(v)
            #assert (txt_info == v)
        if (k == "numbers"):
            assert (numbers == v)

# get list of innerText for main contents
for elm in driver.find_elements_by_class_name("sm"):
    list_elm_text.append(elm.text)

assert (list_elm_text == list_ui_text)

# verify footer
common.verify_footer(driver)
common.verify_footer_social(driver)

# close the browser window
driver.quit()
