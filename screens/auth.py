import math
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from kivy.core.window import Window
from firebase_config import auth 

class AuthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        layout.add_widget(Label(text='Sign In / Sign Up', font_size=24))

        self.email_input = TextInput(hint_text='Email', multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.email_input)

        self.password_input = TextInput(hint_text='Password', multiline=False, password=True, size_hint_y=None, height=40)
        layout.add_widget(self.password_input)

        signin_btn = Button(text='Sign In', size_hint=(1, None), height=40)
        signin_btn.bind(on_press=self.sign_in)
        layout.add_widget(signin_btn)

        signup_btn = Button(text='Sign Up', size_hint=(1, None), height=40)
        signup_btn.bind(on_press=self.sign_up)
        layout.add_widget(signup_btn)

        self.message_label = Label(text='', font_size=16)
        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def sign_in(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        try:
            auth.sign_in_with_email_and_password(email, password)
            self.message_label.text = f"Welcome back, {email}"
            self.manager.current = 'dashboard'
        except Exception:
            self.message_label.text = "Invalid credentials or network error."

    def sign_up(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        try:
            auth.create_user_with_email_and_password(email, password)
            self.message_label.text = f"Account created for {email}"
            self.manager.current = 'dashboard'
        except Exception:
            self.message_label.text = "Error creating account. Try again."

