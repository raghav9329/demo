import unittest
from selenium import webdriver
class test(unittest.TestCase):
    
    def test(self):
    	self.driver=webdriver.Chrome()
    	self.driver.get("http://econpy.pythonanywhere.com/ex/001.html")
    	buyers=self.driver.find_elements_by_xpath("/html[1]/body[1]/div/div")
    	prices=self.driver.find_elements_by_xpath("/html[1]/body[1]/div/span")
    	num_items=len(buyers)
	for i in range(num_items):
	    print(buyers[i].text + ": "+ prices[i].text)
	self.driver.close
if __name__ == '__main__':
    unittest.main()
