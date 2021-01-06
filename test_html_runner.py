import unittest
import login_elements
import login_logout
import add_project
import os

# Import the HTMLTestRunner Module
import HtmlTestRunner

# Get the Present Working Directory since that is the place where the report
# would be stored

current_directory = os.getcwd()

class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_Paramount_demo(self):

        # Create a TestSuite with several test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(login_elements.LoginElementsTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_logout.LoginPageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(add_project.AddProjectTest)
        ])

        output_file = open(current_directory + "\HTML_Test_Runner_ReportTest.txt", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='Test Report for Paramount test application',
            descriptions='Demo for Testing Login and Add project functionality'
        )

        html_runner.run(consolidated_test)

if __name__ == '__main__':
    unittest.main()