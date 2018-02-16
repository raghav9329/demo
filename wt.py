from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")
buyers=driver.find_elements_by_xpath("/html[1]/body[1]/div/div")
prices=driver.find_elements_by_xpath("/html[1]/body[1]/div/span")
num_items=len(buyers)
for i in range(num_items):
    print(buyers[i].text + ": "+ prices[i].text)
driver.close
