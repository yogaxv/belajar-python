from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r'C:\Src\chromedriver_win32\chromedriver.exe') # to open the chromebrowse

driver.get('https://demoikpismart.ikpi.or.id/admin/')
driver.find_element_by_name('email').send_keys('admin@ikpi.com')
driver.find_element_by_name('password').send_keys('123123')
driver.find_element_by_xpath('/html/body/form/div/div/div/input').click()

# tag = driver.find_elements_by_tag_name('h6')
# print(tag)

tag = driver.find_elements_by_tag_name('a')
print(tag[0])

# driver.quit()