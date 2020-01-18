from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
class WPBot:
    def__init__ = (self, username, pw):
    sleep(2)
webdriver.find_element_by_xpath(''//input[@name=\''username\'']'')\
.send_keys(name)
webdriver.find_element_by_xpath(''//input[@name=\''password\'']'')\
.send_keys(password)
webdriver.find_element_by_xpath(''//button[@type=\''submit\'']'')\
.click()
sleep(4)

   WPBot('name', 'password')

