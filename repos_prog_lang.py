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

# Navigate to repos per programming language page
driver.get("https://webuildsg.github.io/data/dataset/repos-per-programming-language/")

# get search keyword
f = open(dir + "/data/repos/programming_languages.json")
data = json.load(f)
f.close()

# get the list of programming languages in json file
for obj in data[:]:
    for (k, v) in obj.items():

        # click radio button
        if (k == "programming_language"):
            pl = v.lower()
            driver.find_element_by_xpath('//*[@id="language-'+ pl +'"]').click()

        # verify repos
        if (k == "repos"):
            for (repo, value) in v.items():         
                assert (driver.find_element_by_link_text(repo))
                driver.find_element_by_link_text(repo).click()
                driver.back()


# verify footer
common.verify_footer(driver)
common.verify_footer_social(driver)

# close the browser window
driver.quit()
