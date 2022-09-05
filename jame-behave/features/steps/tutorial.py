import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from environment import *

Monet_RPauction = "https://auction.staging.monet.market/?auction_address=0x415880766290B9F5Cdf45E70fF483DFE87af74e2"

@given("test")
def test(context):
    context.driver.get('https://www.google.com/')
    wait = WebDriverWait((context.driver),10)
    wait.until(EC.number_of_windows_to_be(2))
    original_window = context.driver.current_window_handle
    for window_handle in context.driver.window_handles:
        if window_handle != original_window:
            context.driver.switch_to.window(window_handle)
            break
    wait.until(EC.title_is("MetaMask"))
    wait.until(EC.title_is("MetaMask"))
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/button").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]"))).click() 
    wait.until(EC.visibility_of_all_elements_located)
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-0"))).send_keys("organ")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-1"))).send_keys("enter")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-2"))).send_keys("friend")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-3"))).send_keys("canal")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-4"))).send_keys("clump")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-5"))).send_keys("fix")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-6"))).send_keys("juice")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-7"))).send_keys("fat")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-8"))).send_keys("carry")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-9"))).send_keys("luggage")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-10"))).send_keys("bullet")
    wait.until(EC.visibility_of_element_located((By.ID, "import-srp__srp-word-11"))).send_keys("return")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("094800678")
    wait.until(EC.visibility_of_element_located((By.ID, "confirm-password"))).send_keys("094800678")
    wait.until(EC.visibility_of_element_located((By.ID, "create-new-vault__terms-checkbox"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/button"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/button"))).click()
    context.driver.close()
    context.driver.switch_to.window(original_window)
    context.driver.switch_to.new_window('tab')
    context.driver.get('chrome-extension://{}/home.html'.format("nkbihfbeogaeaoehlefnkodbefgpgknn"))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ("[data-testid=popover-close]")))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "identicon"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[7]"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "private-key-box"))).send_keys("0xa2fe8606b81463fb377f4c2cf5388bf400066f3974e1c12e24345a8dc8ca65d6")
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]"))).click()
