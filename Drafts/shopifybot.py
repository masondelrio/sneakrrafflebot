
# Start on Demand
# Continuous Monitoring (needs while loop and need to check API)
# Buy the Product Automatically when Available(Selenium)

# something is available

import requests

import json
from selenium import webdriver
import time
def availabilitycheck():
    r = requests.get('https://feature.com/products.json')
    products = json.loads((r.text))['products']

    for product in products:
        productname = product['title']

        if productname == 'Brain Dead Global Works Snap Mock Neck Pullover - Natural':

            producturl =  'https://feature.com/products/' + product['handle']
            return producturl
    return False
def buyProduct(url):

    driver = webdriver.Chrome(executable_path='/Users/masondelrio/Desktop/chromedriver')
    time.sleep(1)
    driver.get(str(url))
    time.sleep(1)
    driver.find_element_by_xpath('//div[@data-value="MD"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@class="primary-btn add-to-cart"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//a[@href="/checkout"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder = "Email"]').send_keys('mason@gmail.com')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder = "First name"]').send_keys('John')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder = "Last name"]').send_keys('Smith')
    driver.find_element_by_xpath('//input[@placeholder = "Address"]').send_keys('1234 Streetname Drive')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder = "Apartment, suite, etc. (optional)"]').send_keys('Apt# 1')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder = "City"]').send_keys('San Jose')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder = "ZIP code"]').send_keys('95132')
    time.sleep(1)

    driver.find_element_by_xpath('//input[@data-backup = "phone"]').send_keys('2087619999' + u'\ue007')
    time.sleep(5)
    driver.find_element_by_xpath('//button[@type = "submit"]').click()
    time.sleep(1)



myUrl = availabilitycheck()
if myUrl != False:
    buyProduct(myUrl)
else:
    print('no')


#r = requests.get()
#availabilityCheck('productName')

# Buy if Something is available
#buyProduct(url)

#if availabilityCheck('productName') != False:
    #buyProduct(url)

#else:
    #print('Not available')
#poop