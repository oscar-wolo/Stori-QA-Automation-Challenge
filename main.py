# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
import sys
import time

from selenium.webdriver.common.by import By
from Browser import Browser
from locators.AutomationPractice import AutomationPractice
from locators.QAClickAcademy import QAClickAcademy
from locators.RahulShettyAcademy import RahulShettyAcademy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def print_help():
    print("Usage: python main.py --browser <browserName>\n")
    print("Where valid <browserName> are: chrome, firefox\n")
    pass


def main():
    # Check right number of parameters
    if (len(sys.argv) != 3):
        print_help()
        quit()
    if (sys.argv[1] != "--browser" and sys.argv[1] != "-b"):
        print_help()
        quit()
    else:
        #Call the browser class and initialize a browser..
        browser = Browser(sys.argv[2].lower());
        driver = browser.get_driver()
        page = AutomationPractice()

        #Open browser
        print("Step 1:")
        driver.get(page.base_uri)
        original_window_handle = driver.current_window_handle



        """"2. In the Suggestion Class Example, enter the word “Me” and select Mexico. (Bonus: use only xpath)"""
        print("Step 2:")

        element = driver.find_element(By.XPATH, page.input_type_to_select_countries_xpath)
        element.send_keys("Me")
        elements = driver.find_elements(By.XPATH, page.input_type_to_select_countries_suggestions_xpath)
        while len(elements) == 0:
            elements = driver.find_elements(By.XPATH, page.input_type_to_select_countries_suggestions_xpath)
        for e in elements:
            if e.get_attribute('textContent') == 'Mexico':
                e.click()
                print("Mexico was found and click")
                break
        assert element.get_attribute('value') == 'Mexico', 'value should be Mexico, ' + element.get_attribute('value') + ' found instead'

        """ 3. In the Dropdown Example, select option 2 and then option 3. The user should be able to see the changes"""
        element = driver.find_element(By.XPATH, page.drop_down_class_example_xpath)
        print(element.get_attribute('name'))
        element.click()
        elements = driver.find_elements(By.XPATH, page.drop_down_class_example_options_xpath)
        for e in elements:
            #print("e.get_attribute('value'): " + e.get_attribute('value'))
            if(e.get_attribute('value') == 'option2'):
                print("Click on Option2")
                e.click()
                break
                #The user should be able to see the changes.
                assert element.get_attribute('value') == 'option2', 'Option2 should be visibly selected, found'

        #And then option 3.

        print("Step 3:")

        element.click()
        elements = driver.find_elements(By.XPATH, page.drop_down_class_example_options_xpath)
        for e in elements:
            #print("e.get_attribute('value'): " + e.get_attribute('value'))
            if(e.get_attribute('value') == 'option3'):
                print("Click on Option3")
                e.click()
                break
                #The user should be able to see the changes.
                assert element.get_attribute('value') == 'option3', 'Option3 should be visibly selected, found'

        #4. In the Switch Window Example, click the Open Window button
        element = driver.find_element(By.XPATH, page.button_switch_window_example_open_window_xpath)
        element.click()

        print("Step 4:")

        #switch windows (basically an alt+tab)
        print("driver.title: " + driver.title)
        print("driver.current_url: " + driver.current_url)
        print("switch windows...")
        current_window = driver.current_window_handle
        for h in driver.window_handles:
            if current_window != h:
                driver.switch_to.window(h)
                break;

        print("driver.title: " + driver.title)
        print("driver.current_url: " + driver.current_url)

        qapage = QAClickAcademy();
        driver.implicitly_wait(5)
        element = driver.find_element(By.XPATH, qapage.button_no_thanks_xpath)
        element.click()

        #review 30 day money guarantee
        element = driver.find_element(By.XPATH, qapage.header_thirty_day_money_back_guarantee_xpath)
        print(element.get_attribute('textContent'))
        element = driver.find_element(By.XPATH, qapage.paragraph_thirty_day_money_back_guarantee_xpath)
        print(element.get_attribute('textContent'))

        #review lifetime
        element = driver.find_element(By.XPATH, qapage.header_life_time_xpath)
        print(element.get_attribute('textContent'))
        element = driver.find_element(By.XPATH, qapage.paragraph_life_time_xpath)
        print(element.get_attribute('textContent'))

        #review selfpaced
        element = driver.find_element(By.XPATH, qapage.header_self_paced_online_training_xpath)
        print(element.get_attribute('textContent'))
        element = driver.find_element(By.XPATH, qapage.paragraph_self_paced_online_traning_xpath)
        print(element.get_attribute('textContent'))

        #review in depth material
        element = driver.find_element(By.XPATH, qapage.header_in_depth_material_xpath)
        print(element.get_attribute('textContent'))
        element = driver.find_element(By.XPATH, qapage.paragraph_in_depth_material_xpath)
        print(element.get_attribute('textContent'))

        #review resume preparation
        element = driver.find_element(By.XPATH, qapage.header_resume_preparation_xpath)
        print(element.get_attribute('textContent'))
        element = driver.find_element(By.XPATH, qapage.paragraph_resume_preparation_xpath)
        print(element.get_attribute('textContent'))
        # review the other texts

        # switch windows (basically an alt+tab)
        # go back to AutomationPractice page.
        print("driver.title: " + driver.title)
        print("driver.current_url: " + driver.current_url)
        print("close and switch windows...")

        driver.close()
        driver.switch_to.window(original_window_handle)

        print("driver.current_url: " + driver.current_window_handle)
        print("driver.title: " + driver.title)
        print("driver.current_url: " + driver.current_url)

        """5. In the Switch Tab Example, click the Open Tab button. Scroll on the new tab until you
        #see the button below. Then take a screenshot that includes the button and save it with
        #the name of the test case that you gave in the RTM. Don't close the window. Return to
        #the first window."""

        print("Step 5:")

        actions = ActionChains(driver)
        rsa_page = RahulShettyAcademy()
        element = driver.find_element(By.XPATH, page.button_switch_tab_example_open_tab_xpath)
        element.click()

        #switch windows (basically an alt+tab)
        print("driver.title: " + driver.title)
        print("driver.current_url: " + driver.current_url)
        print("switch windows...")
        current_window = driver.current_window_handle
        for h in driver.window_handles:
            if current_window != h:
                driver.switch_to.window(h)
                break;

        print("driver.title: " + driver.title)
        print("driver.current_url: " + driver.current_url)

        element = driver.find_element(By.XPATH, rsa_page.button_view_all_courses_xpath);
        print("Xpath Button found: " + element.text)
        time.sleep(2)
        print("Attempting a scroll...")
        print("Value: " + str(int(driver.get_window_size()['height']) * 0.5))
        driver.execute_script("arguments[0].scrollIntoView();", element);
        actions.scroll_by_amount(0, -int(driver.get_window_size()['height'] * 0.5)).perform()
        #find by CSS
        element = driver.find_element(By.CSS_SELECTOR, rsa_page.button_view_all_courses_css);
        print("CSS Button found: " + element.text)
        #take screenshot
        driver.save_screenshot("test5.png")
        #Don't close the window. Return to the first window.
        driver.switch_to.window(original_window_handle)

        """6.In the Switch To Alert Example, type this string “Stori Card” and click the Alert button.
        Print the text in the alert and click on OK. Then type the same string and click on the
        Confirm button and print the text. Make sure that the string shown equals this “Hello
        Stori Card, Are you sure you want to confirm?” then click on OK."""

        print("Step 6:")

        element = driver.find_element(By.XPATH, page.input_enter_your_name_xpath)
        element.send_keys("Stori Card")
        element = driver.find_element(By.XPATH, page.button_alert_xpath)
        element.click()
        #time.sleep(3)
        alert = Alert(driver)
        print(alert.text)
        alert.accept()
        element = driver.find_element(By.XPATH, page.input_enter_your_name_xpath)
        element.send_keys("Stori Card")
        element = driver.find_element(By.CSS_SELECTOR, page.button_confirm_css)
        element.click()
        #time.sleep(3)
        print(alert.text)
        alert.accept()

        """7. In the Web Table Example, print the number of courses that are $25. Then print their
        course names."""

        print("Step 7:")
        table = driver.find_element(By.CSS_SELECTOR, page.table_courses_css)
        body = table.find_element(By.TAG_NAME, 'tbody')
        rows = body.find_elements(By.TAG_NAME, 'tr')

        #Iterate through each row and check if the price is 25. If true, print the course name.
        numberOfCourses = 0
        coursesName = []
        for r in rows:
            #print("Full Row: " + r.text)
            #print(r.find_element(By.XPATH, " ./child::*[3]").text)
            if r.find_element(By.XPATH, " ./child::*[3]").text == '25':
                numberOfCourses += 1
                coursesName.append(r.find_element(By.XPATH, "./child::*[2]").text)

        print("Number of courses priced at 25: " + str(numberOfCourses))
        print("Title of courses priced at 25: ")
        for c in coursesName:
            print(c)

        """8. Print the names of all the Engineers in the Web Table Fixed header."""
        print("Step 8:")
        elements = driver.find_elements(By.XPATH, page.table_webtable_fixed_rows_xpath)
        for e in elements:
            #print(e.text)
            #print(e.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text)
            if e.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text == 'Engineer':
                print(e.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text + " is an Engineer.")


        print("Step 9:")

        element = driver.find_element(By.XPATH, page.legend_iframe_example_xpath)
        actions.scroll_to_element(element).perform()
        driver.switch_to.frame("courses-iframe")
        element = driver.find_element(By.XPATH, page.legend_mentorship_program_xpath)
        print(element.text)

        oddChars = []
        i = 0
        for c in element.text:
            if i % 2 != 0:
                oddChars.append(c);
            i += 1

        print(str(str(oddChars)))


        print("Finishing tests...")
        time.sleep(5)

    pass

if __name__ == "__main__":
    main()
