from typing import cast

from selenium import webdriver
from selenium.webdriver.common.by import By


# This class is intended to contain all the pertinent locator elements
# for the test runner to use.

class QAClickAcademy:

    def __init__(self):
        self.base_uri = 'http://www.qaclickacademy.com/'

        #No thanks button
        self.button_no_thanks_xpath= "//button[text()='NO THANKS']"

        #header 30 Day Money Back Guarantee
        self.header_thirty_day_money_back_guarantee_xpath = "//h3[text()='30 day Money Back Guarantee']"
        #text
        self.paragraph_thirty_day_money_back_guarantee_xpath = "//h3[text()='30 day Money Back Guarantee']/following-sibling::p"

        #header Life time instructor support
        self.header_life_time_xpath = "//h3[text()='Life time instructor support']"
        self.paragraph_life_time_xpath = "//h3[text()='Life time instructor support']/following-sibling::p"

        #header Self Paced online Training
        self.header_self_paced_online_training_xpath = "//h3[text()='Self Paced online Training']"
        self.paragraph_self_paced_online_traning_xpath = "//h3[text()='Self Paced online Training']/following-sibling::p"

        #header In Depth Material
        self.header_in_depth_material_xpath = "//h3[text()='In Depth Material']"
        self.paragraph_in_depth_material_xpath = "//h3[text()='In Depth Material']/following-sibling::p"

        #header Resume Prepartion & Interview Questions
        self.header_resume_preparation_xpath = "//h3[text()='Resume Prepartion & Interview Questions']"
        self.paragraph_resume_preparation_xpath = "//h3[text()='Resume Prepartion & Interview Questions']/following-sibling::p"

