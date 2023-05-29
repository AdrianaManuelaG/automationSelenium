from selenium import webdriver
import time
from selenium.webdriver.common.by import By


DRIVER_PATH = "C:\\Users\\adria\\Downloads\\chromedriver_win32\\chromedriver.exe"
URL_TO_TEST = "https://www.demo.guru99.com/V4/"
USER = "mngr504576"
PASSWORD = "UrAnegy"




class Login():
    def loginUtilizator(self, utilizator, parola):
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)

        iframe = driver.find_element(By.ID,"gdpr-consent-notice")
        driver.switch_to.frame(iframe)
        time.sleep(10)
        
        acceptAll = driver.find_element(By.ID, "save")
        acceptAll.click()
        time.sleep(20)

        userName = driver.find_element(By.NAME, "uid")
        userName.send_keys(utilizator)
        time.sleep(20)

        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys(parola)

        loginBtn = driver.find_element(By.NAME, "btnLogin")
        time.sleep(5)
        loginBtn.click()
        time.sleep(10)

        test = 0
        try:
            actualTitle = driver.title
        except:
            print("Test Case passed")    
            test = 1
        assert test == 1, "Test failed should not login"    
        
        time.sleep(20)



    def loginTest(self):
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)

        iframe = driver.find_element(By.ID,"gdpr-consent-notice")
        driver.switch_to.frame(iframe)
      
        
        acceptAll = driver.find_element(By.ID, "save")
        acceptAll.click()
        time.sleep(20)

        userName = driver.find_element(By.NAME, "uid")
        userName.send_keys(USER)
        time.sleep(20)

        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys(PASSWORD)

        loginBtn = driver.find_element(By.NAME, "btnLogin")
        loginBtn.click()

        actualTitle = driver.title
         
        assert actualTitle == "Guru99 Bank Manager HomePage", "FAILED actual title" 
        time.sleep(10)

    def loginTestUserNOK(self):
        self.loginUtilizator("notok", PASSWORD)

    def loginTestPasswordNOK(self):
        self.loginUtilizator(USER, "Passnotok")


    def loginTestEmptyuserId(self):
        self.loginUtilizator("", PASSWORD)
        


    def loginTestEmptypassword(self):
    
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(URL_TO_TEST)
        time.sleep(10)

        iframe = driver.find_element(By.ID,"gdpr-consent-notice")
        driver.switch_to.frame(iframe)
        time.sleep(10)
        
        acceptAll = driver.find_element(By.ID, "save")
        acceptAll.click()
        time.sleep(20)

        userName = driver.find_element(By.NAME, "uid")
        userName.send_keys(USER)
        time.sleep(20)

        userPassword = driver.find_element(By.NAME, "password")
        userPassword.send_keys("")

        loginBtn = driver.find_element(By.NAME, "btnLogin")
        loginBtn.click()
        time.sleep(10)
     #id message18
        find = 0
        try:
            driver.find_element(By.ID, "message18")
            find = 1
        except:
            find = 0
        assert find == 1, "Message Password empty not found"   
            
         
 
    def loginTestUserPasswordEmpty(self):
        self.loginUtilizator("", "")
        


logintest = Login()
logintest.loginTest()
logintest.loginTestUserNOK()
logintest.loginTestPasswordNOK()
logintest.loginTestEmptyuserId()
logintest.loginTestEmptypassword()
logintest.loginTestUserPasswordEmpty()