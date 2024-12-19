from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class PageObject:
    
    def __init__(self, setting):
        self.driver, self.wait = setting

    def navigate_to_website(self):
        self.driver.get('https://www.cathaybk.com.tw/cathaybk/')
        self.driver.delete_all_cookies() 
        self.driver.set_window_size(430,932)
        self.driver.implicitly_wait(5)
    
    def screen_shot(self):
        self.driver.get_screenshot_as_file("test_one.png")

    def click_header_burger(self):
        # click_burger = self.driver.find_element(By.CLASS_NAME,'cubre-o-header__burger')
        click_burger = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"cubre-o-header__burger")))
        click_burger.click()

    def click_menu_sort_btn_product_introduce(self):
        click_menu_sort_btn = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='產品介紹']")))
        click_menu_sort_btn.click()

    def click_menu_sort_btn_credit_card(self):
        click_menu_sort_btn = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='cubre-a-menuSortBtn' and text()='信用卡']")))
        click_menu_sort_btn.click()

    def calculate_menu_link(self):
        self.driver.get_screenshot_as_file("test_two.png")
        att_parents = self.driver.find_elements(By.XPATH,"//div[@class='cubre-o-menuLinkList__content']")
        att_child = att_parents[1].find_elements(By.XPATH,"//a[@id='lnk_Link' and @class='cubre-a-menuLink']")
        total = 0
        for i in att_child[0:9]:
           print(i.get_attribute('href'))
           total+=1
        return total
    
    def click_credit_card_introduction(self):
        click_menu_credit_card_introduction = self.wait.until(EC.presence_of_element_located((By.XPATH,"//a[@id='lnk_Link' and text()='卡片介紹']")))
        click_menu_credit_card_introduction.click()

    def scroll_to_suspend_credit_card(self):
        # scroll_to_suspend_credit_card = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(.,'停發卡')]")))
        # ActionChains(self.driver) \
        # .scroll_to_element(scroll_to_suspend_credit_card)\
        # .perform()
        self.driver.execute_script("window.scrollTo(0, 3300)")
        parents_swiper = self.driver.find_elements(By.XPATH,"//div[@class='cubre-o-slide__page swiper-pagination-clickable swiper-pagination-bullets']")
        child_swiper = parents_swiper[-1].find_elements(By.XPATH, "span[@aria-label]")
        credit = 0
        for i in child_swiper:
            time.sleep(2)
            self.driver.get_screenshot_as_file(f"test_{credit}.png")
            i.click()
            credit+=1
            
    def calculate_suspend_credit_card(self):
        att_suspend_credit_card = self.driver.find_elements(By.XPATH,"//div[@class='cubre-m-compareCard__pic']//img")
        total = 0
        for i in att_suspend_credit_card[20:30]:
            print(i.get_attribute('id'))
            total+=1
        return total
    
    def driver_close(self):
        self.driver.close()

        



        


    
