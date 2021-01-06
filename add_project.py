import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
import time
import calendar
from time import sleep
import config
import elements


class AddProjectTest(unittest.TestCase):
    name = 'Test'

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(config.test_url)
        wait = WebDriverWait(driver, 10)
        #Login to Application
        wait.until(EC.visibility_of_element_located((By.XPATH, elements.email_box_path))).send_keys(config.test_email)
        wait.until(EC.visibility_of_element_located((By.XPATH, elements.password_box_path))).send_keys(config.test_password)
        wait.until(EC.element_to_be_clickable((By.XPATH, elements.login_button_path))).click()
        sleep(2)

    def test_a_cancel_project(self):
        print('--Test Cancel from Add Project returns to Project List--')
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        expected = '/ Project List'
        #Click on Add Project button
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, elements.add_project_button_path))).click()
        except:
            print('Error: Could not click on Add Project button')
        sleep(2)
        #Click on Cancel button
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, elements.project_cancel_button_path))).click()
        except:
            print('Error: Could not click on Cancel button')
        sleep(2)
        #Verify Project page is shown
        try:
            header = wait.until(EC.visibility_of_element_located((By.XPATH, elements.projects_header_path)))
        except:
            print('Error: Could not locate Projects page')
            self.assertEqual('Not Found', expected)
        else:
            self.assertEqual(header.text, expected)
        sleep(2)

    def test_b_add_project(self):
        print('--Test Project is saved and details page is open with new Project name--') 
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        #Click on Add Project button
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, elements.add_project_button_path))).click()
        except:
            print('Error: Could not click on Add Project button')
        sleep(2)
        ts = calendar.timegm(time.gmtime())
        new_name = "Test" + str(ts)
        self.__class__.name = new_name
        survey_cost = config.survey_cost
        travel_cost = config.travel_cost
        #Enter Project Name
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, elements.new_project_name_path))).send_keys(new_name)
        except:
            print('Error: Project Name input not found')
        #Enter Survey Cost
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, elements.new_project_survey_path))).send_keys(survey_cost)
        except:
            print('Error: Survey Cost input not found')
        #Enter Travel Cost
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, elements.new_project_travel_path))).send_keys(travel_cost)
        except:
            print('Error: Travel Cost input not found')
        #Click on Save button
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, elements.project_save_button_path))).click()
        except:
            print('Error: Could not click on Save button')
        sleep(2)
        #Verify new Project is saved and details shown
        try:
            project=wait.until(EC.visibility_of_element_located((By.XPATH, elements.project_details_header_path)))
        except:
             print('Error: Could not verify project ', new_name, ' is saved')
             self.assertEqual('Not Found', new_name)
        else:
            self.assertEqual(project.text, new_name)
        sleep(2)

    def test_c_verify_project_added(self):
        print('--Test Project List has new Project--')
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        project_name = self.__class__.name
        #Verify new Project is saved and exists in Projects list
        try:
            project=wait.until(EC.visibility_of_element_located((By.XPATH, elements.projects_list_path.format(project_name))))
        except:
             print('Error: Could not locate saved project ', project_name)
             self.assertEqual('Not Found', project_name)
        else:
            self.assertEqual(project.text, project_name)
        sleep(2)

    def tearDown(self):
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main(failfast=True)
