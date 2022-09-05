import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from environment import *

Monet_RPauction = "https://auction.staging.monet.market/?auction_address=0x415880766290B9F5Cdf45E70fF483DFE87af74e2"

@step("User have MetaMask wallet")
def step_impl(context):
    pass

@step("User access to website")
def step_impl(context):
    context.driver.get(Monet_RPauction)
    if context.driver.current_url == Monet_RPauction:
        pass
    else:
        raise Exception('incorrect url')

@step("User connect wallet")
def step_impl(context):
    pass

@step('Users can see their wallet address')
def step_impl(context):
    pass

@step("User approve MONT")
def stepl_impl(context):
    pass

@step("Users see approve button disappear")
def step_impl(context):
    pass





