import os
import json
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

# Navigate to active user group with > 5 events
driver.get("https://webuildsg.github.io/data/dataset/events-per-group/")

# get search keyword
f = open(dir + "/data/events/events.json")
data = json.load(f)
f.close()

# get the list of programming languages in json file
for obj in data[:]:
    for (k, v) in obj.items():

        # verify events
        if (k == "events"):
            text_link = driver.find_element_by_link_text(v).get_attribute("innerText")
            assert (text_link == v)
            #driver.find_element_by_link_text(v).click()
            #driver.back()

        # verify graph bar
        # apologies - it is imcomplete. not executable for this section
        """
        if (k == "numbers"):   
            print(text_link)
            graph_value = driver.find_element_by_xpath('//p[contains(text(), text_link)]/div[@class="graph-bar"]').get_attribute("innerText")
            assert (graph_value == v)
        """

# verify footer
common.verify_footer(driver)
common.verify_footer_social(driver)

# close the browser window
driver.quit()
