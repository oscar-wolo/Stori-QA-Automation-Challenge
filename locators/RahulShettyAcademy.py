from typing import cast

from selenium import webdriver
from selenium.webdriver.common.by import By


# This class is intended to contain all the pertinent locator elements
# for the test runner to use.

class RahulShettyAcademy:

    def __init__(self):
        self.base_uri = "https://www.rahulshettyacademy.com/"
        self.button_view_all_courses_xpath = "//*[contains(text(), 'VIEW ALL COURSES')]"
        self.button_view_all_courses_css = "a[class*='btn-primary'][href$='/courses']"
