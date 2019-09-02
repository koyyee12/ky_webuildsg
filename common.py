import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def verify_footer(driver):
    txt_suggestion = driver.find_element_by_xpath('//p[contains(text(), "We welcome your")]').get_attribute("innerText")
    assert (txt_suggestion == "We welcome your suggestions")
    driver.find_element_by_link_text("suggestions").click()
    assert (driver.find_element_by_id("search-query").get_attribute("placeholder"))
    driver.back()

    txt_bugs_pr = driver.find_element_by_xpath('//p[contains(text(), "Feel free to")]').get_attribute("innerText")
    assert (txt_bugs_pr == "Feel free to report bugs / send pull requests")
    driver.find_element_by_link_text("report bugs / send pull requests").click()
    assert ("github" in driver.page_source)
    driver.back()

def verify_footer_social(driver):
    # twitter
    assert (driver.find_element_by_class_name ("footer-twitter"))
    driver.find_element_by_class_name ("footer-twitter").click()
    driver.back()
    # facebook
    assert (driver.find_element_by_class_name ("footer-facebook"))
    driver.find_element_by_class_name ("footer-facebook").click()
    driver.back()
    # github
    assert (driver.find_element_by_class_name ("footer-github"))
    driver.find_element_by_class_name ("footer-github").click()
    driver.back()
    # rss
    assert (driver.find_element_by_class_name ("footer-rss"))
    driver.find_element_by_class_name ("footer-rss").click()
    driver.back()
    # calendar
    assert (driver.find_element_by_class_name ("footer-calendar"))
    # i-tunes
    assert (driver.find_element_by_class_name ("footer-itunes"))
    driver.find_element_by_class_name ("footer-itunes").click()
    driver.back()


