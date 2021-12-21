from selenium import webdriver
chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
pop = driver.find_element_by_css_selector("#articlecount a")
print(pop.text)

driver.quit()