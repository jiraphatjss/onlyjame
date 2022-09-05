from environment import *

wait = WebDriverWait(driver, 10)


# display.start()
driver.get('https://www.google.com/')
wait.until(EC.number_of_windows_to_be(2))

original_window = driver.current_window_handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
     
wait.until(EC.title_is("MetaMask"))

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/button")

driver.get_screenshot_as_file("screenshot.png")

# display.stop()
