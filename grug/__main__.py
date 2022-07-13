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
        user_dict = dict()
        with open(users_url) as json_file:
            users_dict = json.loads(json_file.read())
            print(users_dict)
        login = False
        # Add code
        for i in users_dict["users"]:
            print(i["username"])
            print(i["password"])
            print(self.temp_pass)
            print(self.temp_user)
            if i["username"] == self.temp_user and i["password"] == self.temp_pass:
                self.login = True
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
        users_dict = json.loads(users_url)
        newacc = True
        # Add code
        for i in users_dict:
            if i["username"] == self.temp_user or i["email"] == self.temp_email:
                newacc = False

        if newacc:
            self.manager.current = "menu"


class UserScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class GrugApp(App):
    def build(self):
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
