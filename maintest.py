            # # # #                                                             WORKING code**************@*
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import time
import getpass
import pyautogui
import random                                                               
import json
import pandas as pd
import os

li,lis,ml,bug_list,mpl=[],[],[],[],[]
import gspread
gc = gspread.service_account(filename = "D:\\ref\\templates\\Python Codes\\Selenium\\selitestcerd.json")
sh = gc.open_by_key("1og5kORoM3-82yg_uV34e39gh6EYht7lZxmHqG6QLApQ")
worksheet = sh.sheet1
global coun

with open(os.path.join("seleniumroughdata.json")) as json_file:
    f = json.load(json_file)

with open(os.path.join("dataa.json")) as json_file:
    data = json.load(json_file)

Path = "D:\Download(D)\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(Path)


driver.get("http://172.105.33.88/interactive")
driver.find_element_by_name("password").send_keys("Venkat_bot")
time.sleep(1)
pyautogui.press("enter")
time.sleep(0.5)
driver.maximize_window()


time.sleep(3)

# pyautogui.moveTo(30,200,duration=1)
# pyautogui.click()
pyautogui.moveTo(400,500,duration=1)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/aside/ul/div[1]/div[1]/span/div/li").click()


time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/button[1]').click()
time.sleep(3)

class functions():
    def wrksheet():
        global bug_list,lis
        lis,bug_list=[],[]
        worksheet.append_row(ml)
        worksheet.append_row(mpl)
        worksheet.append_row(kk)
        worksheet.append_row(["NEXT"])
        res = worksheet.get_all_values()
        print("result",res)
        print("bug list : ",bug_list)
        bug_list =[]
        lis =[]
        # ml=[]
        functions.re()

    def re():
        global ml,mpl,kk
        mpl,kk,ml=[],[],[]
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/textarea').click()
        time.sleep(1)
        pyautogui.write("/restart")
        pyautogui.press("enter")
        pyautogui.scroll(-140)
        # print("restart")
        time.sleep(2)
        # pyautogui.moveTo(1100,750,duration=2)
        # pyautogui.doubleClick()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/ul/div[1]/div[2]/div[2]/button[2]").click()
        time.sleep(2)
        # pyautogui.moveTo(900,800,duration=2)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/textarea').click()
        v = data[random.randint(0,len(data)-1)]["Intent training phrase {}".format(random.choice([1,2]))]
        pyautogui.write(v)
        pyautogui.press("enter")
        pyautogui.scroll(-140)
        time.sleep(4)
        pyautogui.moveTo(400,500,duration=1)
        
    def ex():
        coun = 0
        # print("text")
        # pyautogui.moveTo(900,800)
        # pyautogui.doubleClick()
        pyautogui.scroll(-140)

        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/textarea').click()
        # pyautogui.write("abc")
        ml.append(driver.find_elements_by_class_name("css-1di2tiy")[-1].text)
        for i in driver.find_elements_by_class_name("css-1di2tiy")[-1].text.split(" "):
            if i.lower().strip() in f:
                pyautogui.write(random.choice(f[i.lower()]))
                coun=1
        if coun == 0:
            pyautogui.write("abc")
        pyautogui.press("enter")
        print("flow")
        pyautogui.scroll(-140)
        time.sleep(3)
        # pyautogui.doubleClick()

    v = data[random.randint(0,len(data)-1)]["Intent training phrase {}".format(random.choice([1,2]))]

    # v="need a repair"
    # print(v)
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/textarea').send_keys(v)
    ml.append(v)####################
    pyautogui.press("enter")
    time.sleep(3)



                

while True:
    try:
        if driver.find_elements_by_class_name("css-1wvkf5u"):
            kk =[i.text for i in driver.find_elements_by_class_name("css-1wvkf5u")]
            # print("kkk  :   - ",kk)
            print(driver.find_elements_by_class_name("css-1wvkf5u")[-1].text)
            mpl.append(driver.find_elements_by_class_name("css-1wvkf5u")[-1].text)

        if driver.find_element_by_class_name("css-1di2tiy"):
            # print("TEXT : ",driver.find_elements_by_class_name("css-1di2tiy")[-1].text)
            if driver.find_elements_by_class_name("css-1di2tiy")[-1].text not in (bug_list) :
                bug_list=[]
                bug_list.append(driver.find_elements_by_class_name("css-1di2tiy")[-1].text)
                # print("\n\n\n\nif\n\n\n\n")
                # print("bug list : ",bug_list)
            elif driver.find_elements_by_class_name("css-d6yrmz"):
                # print("\n\n\n\nelif\n\n\n\n")
                for i in driver.find_elements_by_class_name("css-d6yrmz"):
                    # print("text ",i.text)
                    lis.append(i.text)
                # print("lis : ",lis)
                # print("bug list : ",bug_list)
                if lis not in (bug_list):
                    bug_list.append(lis)
                else:
                    # print("\nelse\n\n\n\n\n\n\n")
                    functions.wrksheet()

            else:
                print("\nelse++\n\n\n\n\n\n\n")
                functions.wrksheet()
            print("bug list : ",bug_list)

        time.sleep(2)
        if driver.find_elements_by_class_name("css-d6yrmz"):
            # print("button found")
            time.sleep(1)
            b= random.choice(driver.find_elements_by_class_name("css-d6yrmz"))
            # print("random button")
            ml.append(b.text)
            b.click()
            pyautogui.scroll(-180)
            time.sleep(3)

        else:
            pyautogui.scroll(-140)

            try:
                if driver.find_elements_by_class_name("css-1di2tiy")[-2].text:
                    if "The details of your action" in driver.find_elements_by_class_name("css-1di2tiy")[-2].text or "You can check your auction status" in driver.find_elements_by_class_name("css-1di2tiy")[-2].text or "Please click here to follow up on your requirement" in driver.find_elements_by_class_name("css-1di2tiy")[-2].text:
                        functions.re()
                        continue
                        # pass
            except:
                if driver.find_elements_by_class_name("css-1di2tiy").text:
                    if driver.find_elements_by_class_name("css-1di2tiy")[-1].text:
                    # print("try EX")
                        functions.ex()
            else:    
                # print("EX FUNCTION")
                functions.ex()

    except Exception as eee:
            # print("eee ",eee)
            functions.ex()

