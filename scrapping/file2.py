from selenium import webdriver

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

driver1.get('https://facebook.com')
driver2.get('https://youtube.com')
driver3.get('https://stackoverflow.com')
