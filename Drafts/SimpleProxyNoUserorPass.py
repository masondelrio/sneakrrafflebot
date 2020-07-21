import time

from selenium import webdriver

def changeHostChrome(proxy):
    chrome_options = webdriver.ChromeOptions()
    print(proxy)
    chrome_options.add_argument('--proxy-server=http://%s' % proxy )
    chrome_options.add_argument("--incognito")
    chrome = webdriver.Chrome(executable_path='/Users/masondelrio/Desktop/chromedriver' , options=chrome_options)
    chrome.get("https://www.google.com/search?q=what+is+my+ip&oq=what+is+m&aqs=chrome.0.69i59j69i57j0l3j69i60l3.3328j1j7&sourceid=chrome&ie=UTF-8")
    time.sleep(30)
    # chrome.get("http://www.google.com")
    # search = chrome.find_element_by_name('q')
    # search.send_keys("my ip")
    # search.send_keys(Keys.RETURN)
    print(chrome.get_log('driver'))


Proxy ="us-dynamic-1.resdleafproxies.com:16936"
changeHostChrome(Proxy)
