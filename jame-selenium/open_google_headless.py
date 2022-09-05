from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")
driver.find_element(By.NAME, "btnK")
driver.title
if driver.title == "Google":
    print("pass")
else:
    print("failed")


