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

class ImageButton(ButtonBehavior, Image):
    pass

KV = ''
class ContentNavigationDrawer(BoxLayout):
    userList =[]
    email = ObjectProperty(None)
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

        for email in userList:
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