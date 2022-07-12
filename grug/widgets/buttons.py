from pathlib import Path

from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.behaviors import ToggleButtonBehavior

class LoginButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SignupButton(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
