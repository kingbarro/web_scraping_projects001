#!Purposely put here

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By


def interact_with_page():
    #open browser and type in it
    browser = webdriver.Chrome()
    #type(browser)
    browser.get('https://www.wikipedia.com')

    # Finding an element of the page 
    try:
        #element = browser.find_element(By.TAG_NAME, "")
        #element = browser.find_element(By.XPATH, "")
        #element = browser.find_element(By.CSS_SELECTOR, "")
       #element = browser.find_element(By.CLASS_NAME, "banner__topbar" )
       element = browser.find_element(By.ID, "js-link-box-en")
       print('found <%s> element with that class name' % (element.tag_name))

    except Exception as ex:
        print('not able to find the element with that name.')

    # Clicking the page


interact_with_page()

