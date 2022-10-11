from typing import cast

from selenium import webdriver
from selenium.webdriver.common.by import By


# This class is intended to contain all the pertinent locator elements
# for the test runner to use.

class AutomationPractice:

    def __init__(self):
        self.base_uri = 'https://rahulshettyacademy.com/AutomationPractice/'
        #Dropdown example
        self.drop_down_class_example_xpath = "//select[@id='dropdown-class-example']"
        self.drop_down_class_example_options_xpath = "//select[@id='dropdown-class-example']/option"

        #Suggestion Class Example (Type to Select Countries)
        self.input_type_to_select_countries_xpath = "//input[@id='autocomplete' and @placeholder='Type to Select Countries']"
        self.input_type_to_select_countries_suggestions_xpath = "//li[@class='ui-menu-item']/*"

        #Switch Window Example Button
        self.button_switch_window_example_open_window_xpath = "//button[@id='openwindow']"

        #Switch tab example
        self.button_switch_tab_example_open_tab_xpath = "//legend[@class='switch-tab']/following-sibling::a[@id='opentab']"

        #Switch to Alert Example
        self.legend_switch_to_alert_xpath = "//legend[text() = 'Switch To Alert Example']"
        self.input_enter_your_name_xpath = "//legend[text()= 'Switch To Alert Example']/following-sibling::input[@type='text']"
        #Alert button
        self.button_alert_xpath = "//legend[text()= 'Switch To Alert Example']/following-sibling::input[@id='alertbtn']"
        self.button_alert_css = "input#alertbtn[type='submit']"
        #Confirm Button
        self.button_confirm_xpath = "//legend[text()= 'Switch To Alert Example']/following-sibling::input[@id='confirmbtn']"
        self.button_confirm_css = "input#confirmbtn[type='submit']"

        #Web Table Example
        self.table_courses_xpath = "//table[@name = 'courses']"
        self.table_courses_css = "table#product"

        #Web Table Fixed header
        self.table_webtable_fixed_xpath = "//div[@class = 'tableFixHead']"
        self.table_webtable_fixed_rows_xpath = "//div[@class = 'tableFixHead']//tbody/tr"

        #iframe example
        self.legend_iframe_example_xpath = "//legend[text() = 'iFrame Example']"

        self.legend_mentorship_program_xpath = "//li[contains(text(), 'His mentorship program')]"