import requests
import json
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import zipfile, os

PROXY_HOST = 'us-dynamic.pureproxies.io'  # rotating proxy or host
PROXY_PORT = 13976  # port
PROXY_USER = '136007+US+136007'  # username
PROXY_PASS = 'w7lhlnehf8'  # password

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(
        os.path.join("/Users/masondelrio/Desktop/chromedriver"),
        chrome_options=chrome_options)
    return driver


def main(email, profile):
    xPath_Email = '//input[@id="contactFormEmail"]'

    xPath_FullName = '//input[@id= "contactFormName"]'

    xPath_Phone = '//input[@id= "contactFormTelephone"]'

    xPath_Street = '//input[@id= "contactFormStreet"]'
    xPath_State = '//input[@id= "contactFormState"]'
    xPath_Zip = '//input[@id= "contactFormZipcode"]'
    xPath_Size = '//input[@id= "contactFormSize"]'
    xPath_Submit = '//input[@id= "contactFormSubmit"]'
    xPath_NewsletterExit = '//svg[@viewBox= "0 0 384 512"]'
    driver = get_chromedriver(use_proxy=True)

    driver.get(str("https://laceupnyc.com/products/fz1267-raffle-only-adidas-yeezy-boost-350-v2-zyon-mens-shoes"))

    driver.find_element_by_xpath(xPath_Email).send_keys(email)
    time.sleep(5)
    driver.find_element_by_xpath(xPath_Phone).send_keys(profile.Phone)
    time.sleep(5)
    driver.find_element_by_xpath(xPath_FullName).send_keys(profile.Fullname)
    time.sleep(5)
    driver.find_element_by_xpath(xPath_Street).send_keys(profile.Street)
    time.sleep(5)
    driver.find_element_by_xpath(xPath_State).send_keys(profile.State)
    time.sleep(5)
    driver.find_element_by_xpath(xPath_Zip).send_keys(profile.Zip)
    time.sleep(5)
    driver.find_element_by_xpath(xPath_Size).send_keys(profile.Size)
    time.sleep(5)
    try:
        driver.find_element_by_xpath(xPath_NewsletterExit).click()
    except NoSuchElementException:
        print("No annoying pop-up")
    time.sleep(5)
    driver.find_element_by_xpath(xPath_Submit).click()
    print("All Done with " + str(email) + "!")
    time.sleep(3)


# <svg viewBox="0 0 384 512" style="display: block; height: 18px; width: 18px;"><path d="M217.5 256l137.2-137.2c4.7-4.7 4.7-12.3 0-17l-8.5-8.5c-4.7-4.7-12.3-4.7-17 0L192 230.5 54.8 93.4c-4.7-4.7-12.3-4.7-17 0l-8.5 8.5c-4.7 4.7-4.7 12.3 0 17L166.5 256 29.4 393.2c-4.7 4.7-4.7 12.3 0 17l8.5 8.5c4.7 4.7 12.3 4.7 17 0L192 281.5l137.2 137.2c4.7 4.7 12.3 4.7 17 0l8.5-8.5c4.7-4.7 4.7-12.3 0-17L217.5 256z"></path></svg>#
userList = []
print("Enter a list of emails separated by new lines (Enter 'q' to quit)\n")

while True:
    input_email = input()
    if input_email == 'q':
        break
    userList.append(input_email)

print("Emails successfully collected.")

print("Entering multiple raffles with..." + str(userList))


class Profile:
    def __init__(self, Fullname, Street, State, Zip, Phone, Size):
        self.Fullname = Fullname
        self.Street = Street
        self.State = State
        self.Zip = Zip
        self.Phone = Phone
        self.Size = Size

    ...


your_Profile = Profile(input("Enter your full name: "),
                       input("Enter your street address: "),
                       input("Enter your state, not abbreviated: "),
                       input("Enter your zip code: "),
                       input("Enter your Phone Number: "),
                       input("Enter your Size: "))

for emails in userList:
    main(emails, your_Profile)
