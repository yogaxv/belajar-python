from selenium import webdriver

url = 'https://www.tokopedia.com/'
browser = webdriver.Chrome()

browser.get(url)
browser.find_element_by_xpath('//*[@id="header-main-wrapper"]/div[2]/div[5]/button[2]').click()