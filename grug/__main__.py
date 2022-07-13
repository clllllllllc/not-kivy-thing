from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp

import pandas as pd

import json

from .widgets import SignupButton, LoginButton


class MenuScreen(Screen):
    pass


class LoginScreen(Screen):
    temp_pass = StringProperty("Password")
    temp_user = StringProperty("Username")

    def check_login(self):
        users_url = r"grug/saves/users.json"
        with open(users_url) as json_file:
            users_dict = json.loads(json_file.read())
            print(users_dict)
        login = False
        print(users_dict)
        # Add code
        for i in users_dict["users"]:
            username = self.ids.username.text
            password = self.ids.password.text
            print(username, password)
            print(i["username"], i["password"])
            if i["username"] == username and i["password"] == password:
                login = True
                self.login_id = i["user_id"]

        if login:
            print("ur mom")
            self.manager.current = "user"


class SignupScreen(Screen):
    temp_pass = StringProperty("Password")
    temp_user = StringProperty("Username")
    temp_email = StringProperty("Email")
    temp_code = StringProperty("Code")

    def check_signup(self):
        users_url = r"grug/saves/users.json"
        with open(users_url) as json_file:
            users_dict = json.loads(json_file.read())
            print(users_dict)
        newacc = True
        # Add code
        for i in users_dict["users"]:
            username = self.ids.username.text
            password = self.ids.password.text
            email = self.ids.email.text
            code = self.ids.code.text

            if i["username"] == username or i["email"] == email:
                newacc = False

        if newacc:
            new_user = {
                "user_id": 1,
                "username": username,
                "password": password,
                "email": email,
                "rank": "none",
                "servers": [],
                "settings": {
                    "button_font": "Default",
                    "button_color": "Default",
                    "button_bgcolor": "Default",
                    "label_font": "Default",
                    "label_color": "Default",
                    "font_size": "Default",
                    "bg_image": "Default",
                    "window_size": "Default"
                }
            }
            users_dict["users"].append(new_user)
            json_object = json.dumps(users_dict, indent = 4)
            with open(users_url, "w") as json_file:
                json_file.write(json_object)
            self.manager.current = "menu"


class UserScreen(Screen):

    def add_server(self):
        pass
    
    def on_click_server(self):
        pass
    def on_click_thing(self):
        pass
    
    def on_click_settings(self):
        pass


class SettingsScreen(Screen):
    pass


class GrugApp(MDApp, App):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignupScreen(name="signup"))
        sm.add_widget(UserScreen(name="user"))
        sm.add_widget(SettingsScreen(name="settings"))
        return sm

    pass


if __name__ == "__main__":
    GrugApp().run()
