import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
driver = webdriver.Chrome()
driver.get('https://www.clover.com/dashboard/login')
driver.implicitly_wait(random.randrange(1, 8))
driver.maximize_window()  # Time to enter credentials
driver.find_element_by_id("email-input").click()
driver.find_element_by_id("email-input").clear()
driver.implicitly_wait(random.randrange(3, 6))
element=driver.find_element_by_id("email-input")
for char in "silvio@pentadatainc.com":
    element.send_keys(char)
    time.sleep(random.randrange(3, 6))
driver.find_element_by_id("password-input").click()
driver.find_element_by_id("password-input").clear()
driver.implicitly_wait(random.randrange(1, 3))
element1=driver.find_element_by_id("password-input")
for char in "Seattle123!":
    element1.send_keys(char)
    time.sleep(random.randrange(3, 6))
driver.implicitly_wait(random.randrange(3, 6))
driver.find_element_by_id("log-in").click()
#driver.implicitly_wait(random.randrange(3, 6))