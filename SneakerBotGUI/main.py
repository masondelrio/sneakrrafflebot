from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

userList = []

class HomeScreen(Screen):
    pass
class SettingsScreen(Screen):
    email = ObjectProperty(None)
    def btn(self):
        userList.append(self.email.text)
        self.email.text = ""
        print(userList)
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI
    def change_screen(self, screen_name):
        #get screen manager from kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

MainApp().run()
