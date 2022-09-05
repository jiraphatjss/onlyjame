from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_chrome_with_metamask(context):
    extension_path = '/home/jame/.config/google-chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.12.4_0.crx'
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_extension(extension_path)
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    context.driver = driver
    context.driver.get('https://www.google.com/')
    print("kuy")

def switch_window_handle(context):
    original_window = context.driver.current_window_handle
    wait = WebDriverWait((context.driver), 10)
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in context.driver.window_handles:
        if window_handle != original_window:
            context.driver.switch_to.window(window_handle)
            break
            
def import_wallet_first_time(context):
    wait = WebDriverWait((context.driver), 10)
    wait.until(EC.title_is("MetaMask"))
    context.driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/button").click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button"))).click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]"))).click()
    wait.until(EC.visibility_of_all_elements_located)
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-0"))).send_keys("organ")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-1"))).send_keys("enter")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-2"))).send_keys("friend")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-3"))).send_keys("canal")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-4"))).send_keys("clump")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-5"))).send_keys("fix")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-6"))).send_keys("juice")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-7"))).send_keys("fat")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-8"))).send_keys("carry")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-9"))).send_keys("luggage")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-10"))).send_keys("bullet")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "import-srp__srp-word-11"))).send_keys("return")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "password"))).send_keys("094800678")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "confirm-password"))).send_keys("094800678")
    wait.until(EC.visibility_of_element_located(
        (By.ID, "create-new-vault__terms-checkbox"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/button"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/button"))).click()

def import_and_switch_to_test_wallet(context):
    wait = WebDriverWait((context.driver), 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/section/div[1]")))
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "identicon"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[3]/div[7]"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "private-key-box"))).send_keys(
        "0xa2fe8606b81463fb377f4c2cf5388bf400066f3974e1c12e24345a8dc8ca65d6")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]"))).click()
    # context.driver.close()
    

    # Monet_RPauction = "https://auction.staging.monet.market/?auction_address=0x415880766290B9F5Cdf45E70fF483DFE87af74e2"
    # context.driver.get(Monet_RPauction)
    # context.driver.switch_to.window(original_window)
    # context.driver.switch_to.new_window('tab')
    # context.driver.get(
    #     'chrome-extension://{}/home.html'.format("nkbihfbeogaeaoehlefnkodbefgpgknn"))
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.CLASS_NAME, "identicon"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "/html/body/div[1]/div/div[3]/div[7]"))).click()
    # wait.until(EC.element_to_be_clickable((By.ID, "private-key-box"))).send_keys(
    #     "0xa2fe8606b81463fb377f4c2cf5388bf400066f3974e1c12e24345a8dc8ca65d6")
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]"))).click()
    # context.driver.close()
    # context.driver.switch_to.window(original_window)


    # context.driver.get(Monet_RPauction)
    # if context.driver.current_url == Monet_RPauction:
    #     pass
    # else:
    #     raise Exception('incorrect url')
    # wait.until(EC.element_to_be_clickable(
    #     (By.CSS_SELECTOR, ("[data-test-element=btn-connect-wallet]")))).click()
    # wait.until(EC.number_of_windows_to_be(2))
    # for window_handle in context.driver.window_handles:
    #     if window_handle != original_window:
    #         context.driver.switch_to.window(window_handle)
    #         break
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]"))).click()
    # wait.until(EC.element_to_be_clickable(
    #     (By.CSS_SELECTOR, ("[data-testid=page-container-footer-next]")))).click()
    # wait.until(EC.number_of_windows_to_be(2))
    # for window_handle in driver.window_handles:
    #     if window_handle != original_window:
    #         driver.switch_to.window(window_handle)
    #         break
    #     else:
    #         driver.switch_to.window(original_window)
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/button[2]"))).click()
    # for window_handle in context.driver.window_handles:
    #     if window_handle != original_window:
    #         context.driver.switch_to.window(window_handle)
    #         break
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/button[2]"))).click()
    # for window_handle in context.driver.window_handles:
    #     if window_handle != original_window:
    #         context.driver.switch_to.window(window_handle)
    #         break
    # wait.until(EC.number_of_windows_to_be(1))
    # context.driver.switch_to.window(original_window)
    # wait.until(EC.visibility_of_element_located(
    #     (By.XPATH, "/html/body/div[1]/div[2]/div/div"))).is_displayed()
    # wait.until_not(EC.presence_of_element_located(
    #     (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[6]/footer/button[2]")))


# from fake_headers import Headers

# header = Headers(
#     browser="chrome",  # Generate only Chrome UA
#     os="win",  # Generate only Windows platform
#     headers=False # generate misc headers
# )
# customUserAgent = header.generate()['User-Agent']
# extension_path = '/home/jame/.config/google-chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.12.4_0.crx'

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument(f"user-agent={customUserAgent}")
# chrome_options.add_extension(extension_path)
# chrome_options.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--allow-running-insecure-content')

# context = webdriver.Chrome(options=chrome_options)
# wait = WebDriverWait(context, 10)
# original_window = context.current_window_handle
