from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
import time

username = input("hesabınızın ismi nedir?\n")                                                            #Giriş yapmak için hesap bilgilerini istiyor.
pw = input("şifreniz nedir?\n")                                                                          #Giriş yapmak için hesap bilgilerini istiyor.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://instagram.com")
time.sleep(5)
driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
time.sleep(1)
driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
time.sleep(1)
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span").click()    #xpath kodu ile tıklaması gereken yerleri buluyor
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(40)


takipciler = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")                          #Css kodundan username ile ilgili kod ile takipçileri buluyor.

f= open("takipciler1.txt","w+")                                                                          #takipciler1.txt isimli bir not defteri klasörü oluşturuyor.

for takipci in takipciler:
    f.write(takipci.text + "\n")                                                                         #Sayfada yüklenen tüm takipçileri takipciler1.txt dosyasına listeliyor.

f.close() 

time.sleep(4)
