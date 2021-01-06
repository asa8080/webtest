import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import config
import elements

class LoginElementsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(config.test_url)
 
    def test_email_field_dimensions(self):
        print("--Test Email input box is present with proper dimensions--")
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        expected = (config.email_box_height, config.email_box_width)
        try:
            email_box = wait.until(EC.visibility_of_element_located((By.XPATH, elements.email_box_path)))
        except:
            print('Error: Email input not found')
            self.assertEqual('Not Found', expected)
        else:
            actual = (email_box.size['height'], email_box.size['width'])
            self.assertEqual(actual, expected)
        sleep(2)

    def test_password_field_dimensions (self):
        print("--Test Password input box is present with proper dimensions--")
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        expected = (config.password_box_height, config.password_box_width)
        try:
            password_box = wait.until(EC.visibility_of_element_located((By.XPATH, elements.password_box_path)))
        except:
            print('Error: Password input not found')
            self.assertEqual('Not Found', expected)
        else:
            actual = (password_box.size['height'], password_box.size['width'])
            self.assertEqual (actual, expected)
        sleep(2)

    def tearDown(self):
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()
