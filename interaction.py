from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# wiki_articles = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(wiki_articles.text)
driver.get("https://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.NAME,value="fName")
f_name.send_keys("shresta")
time.sleep(1)
l_name = driver.find_element(By.NAME,value="lName")
l_name.send_keys("Mallina")
time.sleep(1)
email = driver.find_element(By.NAME,value="email")
email.send_keys("sreshtamallina.1234@gmail.com")
time.sleep(1)
press_sign_up = driver.find_element(By.XPATH,value='/html/body/form/button')
press_sign_up.click()

