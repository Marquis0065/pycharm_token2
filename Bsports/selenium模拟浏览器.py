
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
from selenium.webdriver.common.by import By

url = 'https://fanyi.baidu.com/'
browser = webdriver.Chrome()

browser.get(url)
input = browser.find_element(By.ID,'baidu_translate_input')
input.send_keys('blacktea')
print(browser.requests)
browser.quit()
# url = 'http://www.baidu.com'
# s = Service(r'C:\Users\fzh00\PycharmProjects\pythonProject1\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
# driver.get(url)
# print(driver.get_cookies())
# dic = {}
# for cookie in driver.get_cookies():
#     dic[cookie['name']]=cookie['value']
# print(dic)
#
# import time
# time.sleep(5)
# driver.quit()