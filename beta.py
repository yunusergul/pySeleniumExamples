from selenium import webdriver
from win10toast import ToastNotifier
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.keys import Keys
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
driver.get("https://www.dukkan-senin.com/")#The url of the site to scan
time.sleep(10)
username= driver.find_element_by_name("tbLoginTC")
password= driver.find_element_by_name("tbLoginPassword")
username.send_keys("userName")#user name
password.send_keys("password")#password
loginN = driver.find_element_by_xpath("//*[@id='app']/div[3]/div/div[1]/form/div[3]/input")#xpath
loginN.click()
time.sleep(5)
game = driver.find_element_by_xpath("//*[@id='app']/aside/div[5]/a[3]")
game.click()
time.sleep(5)
point = driver.find_element_by_xpath("//*[@id='app']/div[3]/div[1]/div[2]/div/div/b")
point_text = point.text
time.sleep(5)
driver.close()
toaster = ToastNotifier()
toaster.show_toast("Successful Login "," Successfully Connected Today!! ")#Windows 10 Push Notification
toaster.show_toast("Today's Token Total",format(point_text))#Windows 10 Push Notification



