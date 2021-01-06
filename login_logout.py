import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import config
import elements

class LoginPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(config.test_url)
 
    def test_login (self):
        print('--Test Login to application--')
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        expected = '/ Project List'
        #Enter Enmail
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, elements.email_box_path))).send_keys(config.test_email)
        except:
            print('Error: Email input not found')
        #Enter Password
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, elements.password_box_path))).send_keys(config.test_password)
        except:
            print('Error: Password input not found')
        #Click on Login button
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, elements.login_button_path))).click()
        except:
            print('Error: Could not click Login')
        sleep(2)
        #Verify Projects page is shown
        try:
            header = wait.until(EC.visibility_of_element_located((By.XPATH, elements.projects_header_path)))
        except:
            print('Error: Could not locate Projects page')
            self.assertEqual('Not Found', expected)
        else:
            self.assertEqual(header.text, expected)
        sleep(2)

    def test_logout (self):
        print('--Test Logout from application--')
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        expected = '/ Login'
        #Login to Apllication
        wait.until(EC.visibility_of_element_located((By.XPATH, elements.email_box_path))).send_keys(config.test_email)
        wait.until(EC.visibility_of_element_located((By.XPATH, elements.password_box_path))).send_keys(config.test_password)
        wait.until(EC.element_to_be_clickable((By.XPATH, elements.login_button_path))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, elements.projects_header_path)))
        #Click on Logout button
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, elements.logout_button_path))).click()
        except:
             print('Error: Could not click Logout')
        sleep(2)
        #Verify Login page is shown
        try:
            header = wait.until(EC.visibility_of_element_located((By.XPATH, elements.login_header_path)))
        except:
            print('Error: Could not locate Login page')
            self.assertEqual('Not Found', expected)
        else:
            self.assertEqual(header.text, expected)
        sleep(2)
        
    def tearDown(self):
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main(failfast=True)
