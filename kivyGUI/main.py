from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemableBehavior
from kivy.core.audio import SoundLoader
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.utils import get_color_from_hex
from kivymd.theming import colors
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import zipfile,os
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
import zipfile


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import os, sys
import time
from bs4 import BeautifulSoup

class ImageButton(ButtonBehavior, Image):
    pass

KV = ''
class ContentNavigationDrawer(BoxLayout):
    userList =[]
    email = ObjectProperty(None)
    input_Fname =ObjectProperty(None)
    input_Lname=ObjectProperty(None)
    input_Street=ObjectProperty(None)
    input_City=ObjectProperty(None)
    input_State=ObjectProperty(None)
    input_Zip=ObjectProperty(None)
    pHost=ObjectProperty(None)
    pPort=ObjectProperty(None)
    pUser=ObjectProperty(None)
    pPass=ObjectProperty(None)
    def save_info(self):
        Fname = self.input_Fname.text
        Lname = self.input_Lname.text
        Street = self.input_Street.text
        City = self.input_City.text
        State = self.input_State.text
        Zip = self.input_Zip.text
        self.input_Fname.text = ""
        self.input_Lname.text = ""
        self.input_Street.text= ""
        self.input_City.text= ""
        self.input_State.text= ""
        self.input_Zip.text= ""
        print(Fname,Lname,Street,City,State,Zip)



    def btn(self):
        text = self.email.text
        userList=text.split()
        self.email.text = ""
        print(userList)
        xPath_Email = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input'
        xPath_Fname = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        xPath_Lname = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        xPath_Street = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
        xPath_City = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
        xPath_State = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'
        xPath_Zip = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'
        xPath_Size = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[8]/label/div/div[1]/div'
        xPath_Submit = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div[3]/div[1]/div'


        for email in userList:
            driver = webdriver.Chrome(executable_path='/Users/manuelpartida/Desktop/chromedriver')
            time.sleep(1)
            driver.get(str("https://docs.google.com/forms/d/e/1FAIpQLSeHfR7uI1tREQR_b2Hc-aNAb2_e377kgsqZXBcTYPfr4l_Z9w/viewform?embedded=true"))
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Email).send_keys(email)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Fname).send_keys(Fname)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Lname).send_keys(Lname)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Street).send_keys(Street)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_City).send_keys(City)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_State).send_keys(State)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Zip).send_keys(Zip)
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Size).click()
            time.sleep(3)
            driver.find_element_by_xpath(xPath_Submit).click()
            time.sleep(30)
            print("All Done with " +str(email)+ "!")
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
            os.path.join("/Users/manuelpartida/Desktop/chromedriver"),
            chrome_options=chrome_options)
        return driver

    def main():
        driver = get_chromedriver(use_proxy=True)
        driver.get('https://www.google.com/search?q=my+ip+address')
        time.sleep(30)


    def audioToText(mp3Path):
        driver = get_chromedriver(use_proxy=True)
        driver.execute_script('''window.open("","_blank");''')
        driver.switch_to.window(driver.window_handles[1])

        driver.get(googleIBMLink)

        # Upload file
        time.sleep(1)
        root = driver.find_element_by_id('root').find_elements_by_class_name('dropzone _container _container_large')
        btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
        btn.send_keys(mp3Path)

        # Audio to text is processing
        time.sleep(audioToTextDelay)

        text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div/dialog').find_elements_by_tag_name('dd')
        result = " ".join([each.text for each in text])

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        return result


    def saveFile(content, filename):
        with open(filename, "wb") as handle:
            for data in content.iter_content():
                handle.write(data)
    def testproxy(self):
        delayTime = 2
        audioToTextDelay = 10
        filename = 'test.mp3'
        byPassUrl = 'https://www.google.com/recaptcha/api2/demo'
        googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'

        option = webdriver.ChromeOptions()
        option.add_argument('--disable-notifications')
        option.add_argument("--mute-audio")
        # option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        option.add_argument(
            "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

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
        """ % (self.pHost.text, self.pPort.text, self.pUser.text, self.pPass.text)
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        driver.get(byPassUrl)

        googleClass = driver.find_elements_by_class_name('g-recaptcha')[0]
        outeriframe = googleClass.find_element_by_tag_name('iframe')
        outeriframe.click()

        allIframesLen = driver.find_elements_by_tag_name('iframe')
        audioBtnFound = False
        audioBtnIndex = -1

        for index in range(len(allIframesLen)):
            driver.switch_to_default_content()
            iframe = driver.find_elements_by_tag_name('iframe')[index]
            driver.switch_to.frame(iframe)
            driver.implicitly_wait(delayTime)
            try:
                audioBtn = driver.find_element_by_id('recaptcha-audio-button') or driver.find_element_by_id('recaptcha-anchor')
                audioBtn.click()
                audioBtnFound = True
                audioBtnIndex = index
                break
            except Exception as e:
                pass

        if audioBtnFound:
            try:
                while True:
                    href = driver.find_element_by_id('audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    saveFile(response, filename)
                    response = audioToText(os.getcwd() + '/' + filename)
                    print(response)

                    driver.switch_to_default_content()
                    iframe = driver.find_elements_by_tag_name('iframe')[audioBtnIndex]
                    driver.switch_to.frame(iframe)

                    inputbtn = driver.find_element_by_id('audio-response')
                    inputbtn.send_keys(response)
                    inputbtn.send_keys(Keys.ENTER)

                    time.sleep(2)
                    errorMsg = driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
                    audioToText(response)# maybe goes here
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("Success")
                        break

            except Exception as e:
                print(e)
                print('Caught. Need to change proxy now')
        else:
            print('Button not found. This should not happen.')
        #
        # if __name__ == '__main__':
        #     audioToText()


        #self.submit(userList)
    pass
class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'LightGreen'
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def play_sound(self):
        self.sound = SoundLoader.load('Fallout V.A.T.S. sound effect.wav')
        self.sound.play()





MainApp().run()
