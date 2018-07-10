###################################################
# Utilities to adi tersting of BBC iPlayer radionav
# 
# JM
# 17/6/18
# v1.0
###################################################
from BBCWebUtilitiesClass import WebUtilitiesObject
from selenium import webdriver

class BBCRadionavObject():

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.web_utils = WebUtilitiesObject(self.browser)

    def close_browser(self):
        self.browser.close()

    def load_page(self, url):
        return self.web_utils.load_page(url)

    def is_page_visible(self, page):
        return self.web_utils.is_page_visible(page)

    def open_a_drawer(self, section):
        drawer_class = self.construct_section_class_name(section)
        return self.web_utils.click_by_class(drawer_class)

    def is_drawer_open(self, drawer):
        drawer_xpath = self.construct_drawer_xpath(drawer)
        self.web_utils.get_element_by_xpath(drawer_xpath)

    def is_radionav_visible(self):
        return self.web_utils.get_element_by_class('radionav')

    def return_to_homepage(self):   #this doesn't reliably work
        iplayer_homepage_xpath = "//*[@id='orb-modules']/section[1]/div[1]/section[1]/a"
        return self.web_utils.click_by_xpath(iplayer_homepage_xpath)
        
    def get_categories_link(self, index):   #this was the only way I could figure to do this
        categories_link_xpath = self.construct_category_xpath(index)
        return self.web_utils.get_element_by_xpath(categories_link_xpath)
    
    def click_on_a_link(self, link_xpath):
        return self.web_utils.click_by_xpath(link_xpath)

        
    # Constructs the class name for a section
    def construct_section_class_name(self, section_name):
        return "radionav__" + section_name.lower() + "-link"

    # Constructs the xpath name for a drawer
    def construct_drawer_xpath(self, drawer_name):
        drawer_panel = drawer_name.lower() + "-panel"
        return "//*[@id='" + drawer_panel + "']/ul"

    # Constructs the xpath from a list index
    def construct_category_xpath(self, index):
        return "//*[@id='categories-panel']/ul/li[" + str(index + 1) + "]"
