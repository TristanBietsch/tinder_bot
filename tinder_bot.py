from selenium import  webdriver
from time import sleep

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        self.driver.get('https://tinder.com')
        
        sleep(3)
         
        self.driver.find_element_by_xpath('//*[@id="q-600306533"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')   
        
        sleep(2)
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="q-600306533"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')   
        login_btn.click()
        
        sleep(2)
        
        fb_btn = self.driver.find_element_by_xpath('//*[@id="q1654454959"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
        sleep(2)
        
        #switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        
        sleep(2)
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0_Z3"]')
        login_btn.click()
        
        
bot = TinderBot()
bot.login()