
# Start on Demand
# Continuous Monitoring (needs while loop and need to check API)
# Buy the Product Automatically when Available(Selenium)

# something is available

import requests

import json
from selenium import webdriver
import time
###def availabilitycheck():
  #  r = requests.get('https://feature.com/products.json')
  #  products = json.loads((r.text))['products']

   # for product in products:
  #      productname = product['title']
#
  #      if productname == 'Brain Dead Global Works Snap Mock Neck Pullover - Natural':
#
   #         producturl =  'https://feature.com/products/' + product['handle']
   #         return producturl
  #  return False







#def userurl():
  #  link = requests.get('http://www.awolraffles.com/raffles/nike-dunk-low-sp-university-red')
    #return link



def buyProduct(email):

        for emails in email:

                driver = webdriver.Chrome(executable_path='/Users/masondelrio/Desktop/chromedriver')
                time.sleep(1)
                driver.get(str("http://www.awolraffles.com/raffles/nike-dunk-low-sp-university-red"))




                time.sleep(1)
                driver.find_element_by_xpath('//input[@id= "edit-submitted-name"]').send_keys('Mason Del Rio')
                time.sleep(1)
                driver.find_element_by_xpath('//input[@id="edit-submitted-e-mail-mailchimp-email-address"]').send_keys(email)
                time.sleep(1)
                driver.find_element_by_xpath('//select[@id="edit-submitted-shoe-size"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//option[@value="8.5"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//input[@id="edit-submitted-address"]').send_keys("San Jose, California")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@value = "delivery"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//button[@type = "submit"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//a[@href = "/raffles/nike-dunk-low-sp-university-red"]').click()




userList = []


print("Enter a list of emails separated by new lines (Enter 'q' to quit)\n")
while True:
    input_email = input()
    if input_email == 'q':
        break
    userList.append(input_email)



print(userList)


buyProduct(userList)





#buyProduct(userURL,userList)


#myUrl = availabilitycheck()
#if myUrl != False:
#    buyProduct(myUrl)
#else:
 #   print('no')

#myUrl = availabilitycheck()
#if myUrl != False:
#    buyProduct(link)
#else:
 #   print('no')

#r = requests.get()
#availabilityCheck('productName')

# Buy if Something is available
#buyProduct(url)

#if availabilityCheck('productName') != False:
    #buyProduct(url)

#else:
    #print('Not available')
