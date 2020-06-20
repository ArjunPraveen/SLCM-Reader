from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

login_url = 'https://slcm.manipal.edu/'

Username = '180911230'
Password = '#####'

options = webdriver.ChromeOptions()

options.add_argument('--log-level=3')
#options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("C:/Users/arjun/Downloads/chromedriver_win32/chromedriver.exe", options=options)
delay = 15

try:
    driver.get(login_url)
    driver.implicitly_wait(5)
    name = driver.find_element_by_name('txtUserid')
    name.send_keys(Username)
    password = driver.find_element_by_name('txtpassword')
    password.send_keys(Password)
    driver.find_element_by_name('btnLogin').click()
    print("Succesfully logged in")
    academicsPage = EC.presence_of_element_located((By.ID, 'rtpchkMenu_lnkbtn2_1'))
    
    myElem = WebDriverWait(driver, delay).until(academicsPage)
    myElem.click()
    
    



except Exception as e:
    if(e == TimeoutException):
        print("Loading took too much time!")
    else:
        print(e)




