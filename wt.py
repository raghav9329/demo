from selenium import webdriver
import unittest
import os


"""
Python unittest class which demonstrates creating a webdriver instance using environment variables
populated by the Sauce CI plugins.
"""

class testSauceWrappers(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        command_executor='http://172.17.0.2:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME(chrome_options=options))
        self.driver = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor=command_executor)


    def test_amazon(self):
        driver = self.driver
        driver.get("http://amazon.com")
        print "\rSauceOnDemandSessionID=%s job-name=%s" % (self.driver.session_id, "test_amazon")
        assert "Amazon.com" in driver.title
        driver.quit()


if __name__ == "__main__":
    unittest.main()
