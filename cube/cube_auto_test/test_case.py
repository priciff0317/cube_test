from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
import time 
import subprocess 
from page_object import PageObject
from selenium.webdriver.support.ui import WebDriverWait

# webdriver 配置
def setup():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager' #設定載入頁面時會先只下載dom資源
    options.add_experimental_option("detach", True)
    # service = webdriver.ChromeService(ChromeDriverManager().install(),service_args=['--log-level=DEBUG'],log_output=subprocess.STDOUT) # 直接打印log到terminal
    service = webdriver.ChromeService(ChromeDriverManager().install()) 
    driver = webdriver.Chrome(options=options, service=service)
    wait = WebDriverWait(driver,10,1)
    return driver, wait

# Tsestcase action step

# test1
test = PageObject(setting = setup())
test.navigate_to_website()
time.sleep(2)
test.screen_shot()

# test2
test.click_header_burger()
test.click_menu_sort_btn_product_introduce()
test.click_menu_sort_btn_credit_card()
time.sleep(2)
print(test.calculate_menu_link())

# test3
test.click_credit_card_introduction()
test.scroll_to_suspend_credit_card()
print(test.calculate_suspend_credit_card())

test.driver_close()


