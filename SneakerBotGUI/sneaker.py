from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.nytimes.com")
headlines = driver.find_elements_by_class_name("story-heading")
for headline in headlines:
    print(headline.text.strip())
## Start on Demand
## Continuous Monitoring (needs while loop and need to check API)
## Buy the Product Automatically when Available(Selenium)
#
## something is available
#
## import requests
##
## import json
## from selenium import webdriver
## import time
##
##
##
##
## def buyProduct(email):
##
##         for emails in email:
##
##                 driver = webdriver.Chrome(executable_path='/Users/masondelrio/Desktop/chromedriver')
##                 time.sleep(1)
##                 driver.get(str("http://www.awolraffles.com/raffles/nike-dunk-low-sp-university-red"))
##
##
##
##
##                 time.sleep(1)
##                 driver.find_element_by_xpath('//input[@id= "edit-submitted-name"]').send_keys('Mason Del Rio')
##                 time.sleep(1)
##                 driver.find_element_by_xpath('//input[@id="edit-submitted-e-mail-mailchimp-email-address"]').send_keys(email)
##                 time.sleep(1)
##                 driver.find_element_by_xpath('//select[@id="edit-submitted-shoe-size"]').click()
##                 time.sleep(1)
##                 driver.find_element_by_xpath('//option[@value="8.5"]').click()
##                 time.sleep(1)
##                 driver.find_element_by_xpath('//input[@id="edit-submitted-address"]').send_keys("San Jose, California")
##                 time.sleep(1)
##                 driver.find_element_by_xpath('//input[@value = "delivery"]').click()
##                 time.sleep(1)
##                 driver.find_element_by_xpath('//button[@type = "submit"]').click()
##                 time.sleep(1)
##                 driver.find_element_by_xpath('//a[@href = "/raffles/nike-dunk-low-sp-university-red"]').click()
##
##
#
#
#userList = []
#
#print("Enter a list of emails separated by new lines (Enter 'q' to quit)\n")
#while True:
#    input_email = input()
#    if input_email == 'q':
#        break
#    userList.append(input_email)
#
#
#
#print(userList)
#
## buyProduct(userList)
