from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os.path
import time


def createDriver():  # Creates Driver that's easily configurable
    options = webdriver.FirefoxOptions()
    PATH = r'/home/louis/path/geckodriver'  # Locates the browser driver
    return webdriver.Firefox(executable_path=PATH, options=options)  # Starts the browser


def idExists(elemid, driver):  # Checks if an element exists based off if its ID
    try:
        driver.find_element_by_id(elemid)
    except NoSuchElementException:
        return False
    return True


def textExists(elemtext, driver):  # Checks if an element exists based off of its Text
    try:
        driver.find_element_by_partial_link_text(elemtext)
    except NoSuchElementException:
        return False
    return True


def xpathExists(elemxpath, driver):  # Checks if an element exists based off of its xPath
    try:
        driver.find_element_by_xpath(elemxpath)
    except NoSuchElementException:
        return False
    return True


def classExists(elemclass, driver):  # Checks if an element exists based off of its xPath
    try:
        driver.find_element_by_class_name(elemclass)
    except NoSuchElementException:
        return False
    return True

