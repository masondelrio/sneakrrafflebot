from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
userList = []

KV = ''
class ContentNavigationDrawer(BoxLayout):
    email = ObjectProperty(None)
    def btn(self):
        text = self.email.text
        userList.append(text.split())
        self.email.text = ""
        print(userList)
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
        return Builder.load_string(KV)

    def on_start(self):
        icons_item = {
            "folder": "My Raffles",
            "account-multiple": "Shared with me",
            "star": "Starred Raffles",
            "history": "Recent Raffles ",
            "checkbox-marked": "Raffles won",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


MainApp().run()
