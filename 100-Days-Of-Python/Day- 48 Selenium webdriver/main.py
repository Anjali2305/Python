
from selenium import webdriver
chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://github.com/Anjali2305/Python")
driver.quit()