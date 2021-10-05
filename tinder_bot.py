from selenium import  webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        self.driver.get('https://tinder.com')
        
        sleep(3)
         
        self.driver.find_element_by_xpath('//*[@id="q-600306533"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')   
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="q-600306533"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')   
        login_btn.click()
        
        fb_btn = self.driver.find_element_by_xpath('//*[@id="q1654454959"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
        #switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        
        
        #switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('email@gmail.com')