import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import zipfile,os

def enterRaffle(email):

            driver = webdriver.Chrome(executable_path='/Users/masondelrio/Desktop/chromedriver')
            time.sleep(1)
            driver.get(str("https://docs.google.com/forms/d/e/1FAIpQLSeHfR7uI1tREQR_b2Hc-aNAb2_e377kgsqZXBcTYPfr4l_Z9w/viewform?embedded=true"))
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Email).send_keys(email)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Fname).send_keys(input_Fname)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Lname).send_keys(input_Lname)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Street).send_keys(input_Street)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_City).send_keys(input_City)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_State).send_keys(input_State)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Zip).send_keys(input_Zip)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Size).click()
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Submit).click()
            time.sleep(30)
            print("All Done with " +str(email)+ "!")



userList = []
xPath_Email = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input'
xPath_Fname = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
xPath_Lname = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
xPath_Street = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
xPath_City = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
xPath_State = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'
xPath_Zip = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'
xPath_Size = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[8]/label/div/div[1]/div'
xPath_Submit = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div[3]/div[1]/div'

print("Enter a list of emails separated by new lines (Enter 'q' to quit)\n")

while True:
    input_email = input()
    if input_email == 'q':
        break
    userList.append(input_email)

print("Emails successfully collected.")

print("Entering multiple raffles with..." +str(userList))


print("Enter First Name: ")
input_Fname = input()
print("Enter Last Name: ")
input_Lname = input()
print("Enter Street Address: ")
input_Street = input()
print("Enter City: ")
input_City = input()

print("Enter State: ")
input_State= input()
print("Enter Zip Code: ")
input_Zip = input()

for emails in userList:
    enterRaffle(emails)













