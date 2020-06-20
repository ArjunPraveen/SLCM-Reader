from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import SessionNotCreatedException
from selenium import webdriver
import pandas as pd

#put in your slcm details here
def data():
    loginUrl = 'https://slcm.manipal.edu/'
    Username = '180911230'
    Password = '#########'  
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

def menu():
    while True:
        try:
            print("---------------------------------------")
            choice = int(input("Enter 1 to view attendance\nEnter 2 to view internal marks\n"))
            if 2 % choice == 0:
                return choice
            else:
                print("Enter a valid choice")
        except ValueError:
            print("Enter a valid choice")

def tableize(df):
    if not isinstance(df, pd.DataFrame):
        return
    df_columns = df.columns.tolist() 
    max_len_in_lst = lambda lst: len(sorted(lst, reverse=True, key=len)[0])
    align_center = lambda st, sz: "{0}{1}{0}".format(" "*(1+(sz-len(st))//2), st)[:sz] if len(st) < sz else st
    align_right = lambda st, sz: "{0}{1} ".format(" "*(sz-len(st)-1), st) if len(st) < sz else st
    max_col_len = max_len_in_lst(df_columns)
    max_val_len_for_col = dict([(col, max_len_in_lst(df.iloc[:,idx].astype('str'))) for idx, col in enumerate(df_columns)])
    col_sizes = dict([(col, 2 + max(max_val_len_for_col.get(col, 0), max_col_len)) for col in df_columns])
    build_hline = lambda row: '+'.join(['-' * col_sizes[col] for col in row]).join(['+', '+'])
    build_data = lambda row, align: "|".join([align(str(val), col_sizes[df_columns[idx]]) for idx, val in enumerate(row)]).join(['|', '|'])
    hline = build_hline(df_columns)
    out = [hline, build_data(df_columns, align_center), hline]
    for _, row in df.iterrows():
        out.append(build_data(row.tolist(), align_right))
    out.append(hline)
    return "\n".join(out)

    
def login_scrape():
    try:
        driver = configure()
        url, username, userpassword= data()
        driver.get(url)
        driver.implicitly_wait(5)
        name = driver.find_element_by_name('txtUserid')
        name.send_keys(username)
        password = driver.find_element_by_name('txtpassword')
        password.send_keys(userpassword)
        driver.find_element_by_name('btnLogin').click()
        print("Succesfully logged in")
        print("Loading ...")
        academicsPage = EC.presence_of_element_located((By.ID, 'rtpchkMenu_lnkbtn2_1'))
        delay = 15
        myElem = WebDriverWait(driver, delay).until(academicsPage)
        myElem.click()
        choice = menu()
        print("---------------------------------------")
        if  choice == 1:
            df = pd.DataFrame(columns = ['Subject','Total','Absent','Percentage-Present','Comments'])
            driver.find_element_by_xpath('//a[contains(@href,"#3")]').click()
            
            EC.presence_of_all_elements_located((By.XPATH, '//td[@class="text-center"]'))
            cells = driver.find_elements_by_xpath('//table[@id="tblAttendancePercentage"]/tbody/tr/td[@class="text-center"]')
            # for i in cells:
            #     print(i.get_attribute('textContent'))
            for index, value in enumerate(cells):   
                if index % 8 == 2:
                    subject= (value.get_attribute('textContent'))
                elif index % 8 == 4:
                    total= int(value.get_attribute('textContent'))
                elif index % 8 == 6:
                    absent= int(value.get_attribute('textContent'))
                elif index % 8 == 7:
                    percentage = int(value.get_attribute('textContent').split('.')[0])
                    if percentage <=75:
                        comment = "WARNING"
                    else:
                        comment = "SAFE"
                if index !=0 and index % 8 ==0:
                    df.loc[len(df)] = [subject, total, absent, percentage, comment]
            print (tableize(df))
        elif choice == 2:
            pass
        else:
            menu()
        

    except TimeoutException:
            print("Loading took too much time!")
    except SessionNotCreatedException:
            print("Driver forcefully shut!")   
            

    finally:
        c = input("Do you want to try again: (Y/N)\n")
        if c == 'Y' or c == 'y':
            login_scrape()
        else:
            print("\nBye")


            



#----------------main function------------------------------

print("Welcome!")
print("Open the terminal in full screen")
login_scrape()
print('----------x----------')


