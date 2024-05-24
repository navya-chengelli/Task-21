import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

driver_path = r"D:\sql\chrome-win64.zip"

# Set ChromeDriver path in the environment variable
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

# Create a ChromeOptions object
chrome_options = Options()

# Add experimental option
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)
#set ChromeDriver path in the environment variable
time.sleep(2)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
#maximize window
driver.maximize_window()
#define a username
username=driver.find_element(By. ID, "user-name")
username.click()
#sleep
time.sleep(1)
#sending the keys
username.send_keys("standard_user")
#define a password
password=driver.find_element(By. ID,"password")
password.click()
time.sleep(1)
#sending the keys
password.send_keys("secret_sauce")
#created cookies before the login the webpage
mycookies=driver.get_cookies()
print("cookies created before login:",len(mycookies))
print("cookies created before login", mycookies)
login=driver.find_element(By. ID,"login-button")
#click on button
login.click()
#created cookies after login the webpage
mycookies=driver.get_cookies()
print("cookies created after login:",len(mycookies))
print("cookies created after login", mycookies)
button=driver.find_element(By.ID,"react-burger-menu-btn")
#click on button
button.click()
time.sleep(2)
#define a logout button
logout_button =driver.find_element(By.XPATH,'//*[@id="logout_sidebar_link"]')
#click on logout button
logout_button.click()
time.sleep(2)
#quit the webpage
driver.quit()