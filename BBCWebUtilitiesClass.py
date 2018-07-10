######################################
# Utilities to aid testing of web page
# Arguments: browser instance
# JM
# 17/6/18
# v1.0
######################################
from selenium.common.exceptions import NoSuchElementException

class WebUtilitiesObject():

    def __init__(self, browser):
        self.browser = browser
     
    def load_page(self, url):
        return self.browser.get(url)

    def is_page_visible(self, title):
        try:
            assert title in self.browser.title
            return True
        except AssertionError:
            return False

    def click_by_class(self, element_class_name):
        element = self.get_element_by_class(element_class_name)
        if element:            
            element.click()
            return True
        else:
            return False

    def click_by_xpath(self, element_xpath):
        element = self.get_element_by_xpath(element_xpath)
        if element:            
            element.click()
            return True
        else:
            return False
     
    def get_element_by_class(self, element_class_name):
        try:
            element = self.browser.find_element_by_class_name(element_class_name)
            return element
        except NoSuchElementException: 
            return False

    def get_element_by_xpath(self, element_xpath):
        try:
            element = self.browser.find_element_by_xpath(element_xpath)
            return element
        except NoSuchElementException: 
            return False

    def get_element_by_id(self, element_id):
        try:
            element = self.browser.find_element_by_id(element_id)
            return element
        except NoSuchElementException: 
            return False
