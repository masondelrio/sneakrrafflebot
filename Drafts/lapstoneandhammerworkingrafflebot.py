import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import zipfile,os

###Potential for proxy problem, not implemented properly yet. Ignore.
def proxy_chrome(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS):
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
                                host: "%(host)s",
                                port: parseInt(%(port)d)
                              },
                              bypassList: ["foobar.com"]
                            }
                          };
                    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
                    function callbackFn(details) {
                        return {
                            authCredentials: {
                                username: "%(user)s",
                                password: "%(pass)s"
                            }
                        };
                    }
                    chrome.webRequest.onAuthRequired.addListener(
                                callbackFn,
                                {urls: ["<all_urls>"]},
                                ['blocking']
                    );
                        """ % {
                    "host": PROXY_HOST,
                    "port": PROXY_PORT,
                    "user": PROXY_USER,
                    "pass": PROXY_PASS,
                }

                pluginfile = 'extension/proxy_auth_plugin.zip'

                with zipfile.ZipFile(pluginfile, 'w') as zp:
                    zp.writestr("manifest.json", manifest_json)
                    zp.writestr("background.js", background_js)

                co = Options()
                # extension support is not possible in incognito mode for now
                # co.add_argument('--incognito')
                co.add_argument('--disable-gpu')
                # disable infobars
                co.add_argument('--disable-infobars')
                co.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                # location of chromedriver, please change it according to your project.
                chromedriver = os.getcwd() + '/Chromedriver/chromedriver'
                co.add_extension(pluginfile)
                driver = webdriver.Chrome(chromedriver, chrome_options=co)
                # return the driver with added proxy configuration.
                return driver






#Code works for Lapstone and Hammer website as of
def enterRaffle(email):



            driver = webdriver.Chrome(executable_path='/Users/masondelrio/Desktop/chromedriver')
            time.sleep(1)
            driver.get(str("https://www.lapstoneandhammer.com/collections/releases/products/dunk-low-sp-university-red"))
            time.sleep(1)


            driver.find_element_by_xpath('//input[@aria-label="Enter your email address"]').send_keys("poopman@gmail.com")


            driver.find_element_by_xpath('//button[@class="needsclick Button__FormStyledButton-p2mbjt-0 dvMZen kl-private-reset-css-Xuajs1"]').click()


            driver.find_element_by_xpath('//input[@id="mce-EMAIL"]').send_keys(email)

            driver.find_element_by_xpath('//input[@id = "mce-FNAME"]').send_keys('Vanessa')


            driver.find_element_by_xpath('//input[@id = "mce-LNAME"]').send_keys('Antonel')
            time.sleep(1)


            driver.find_element_by_xpath('//select[@id="mce-MMERGE3"]').click()

            driver.find_element_by_xpath('//option[@value="9"]').click()



            driver.find_element_by_xpath('//input[@id = "mc-embedded-subscribe"]').click()
            time.sleep(1)
            print("All Done!")


userList = []


print("Enter a list of emails separated by new lines (Enter 'q' to quit)\n")
while True:
    input_email = input()
    if input_email == 'q':
        break
    userList.append(input_email)
print("Emails successfully collected.")

print("Entering Multiple Raffles... ")
print(userList)
for emails in userList:
    enterRaffle(emails)
