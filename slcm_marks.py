from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import SessionNotCreatedException
from selenium import webdriver

def data():
    loginUrl = 'https://slcm.manipal.edu/'
    Username = '180911230'
    Password = '########'
    return loginUrl,Username,Password

def configure():    
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        #options.add_argument('headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome("C:/Users/arjun/Downloads/chromedriver_win32/chromedriver.exe", options=options)
        return driver
    except SessionNotCreatedException:
        print("Driver forcefully shut!")  
    
def login():
    try:
        driver = configure()
        url, username, password = data()
        driver.get(url)
        driver.implicitly_wait(5)
        name = driver.find_element_by_name('txtUserid')
        name.send_keys(username)
        password = driver.find_element_by_name('txtpassword')
        password.send_keys(password)
        driver.find_element_by_name('btnLogin').click()
        print("Succesfully logged in")
        academicsPage = EC.presence_of_element_located((By.ID, 'rtpchkMenu_lnkbtn2_1'))
        delay = 15
        myElem = WebDriverWait(driver, delay).until(academicsPage)
        myElem.click()
        print("For attendance click")
        



    except TimeoutException:
            print("Loading took too much time!")
    except SessionNotCreatedException:
            print("Driver forcefully shut!")   
            

    finally:
        c = input("Do you want to try again: (Y/N)")
        if c == 'Y':
            login()
        else:
            print("Bye")
            



#----------------main function------------------------------


login()



