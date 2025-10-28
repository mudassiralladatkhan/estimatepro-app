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
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        layout.add_widget(Image(source='logo.jpg', size_hint=(1, 0.4)))
        layout.add_widget(Label(text='EstimatePro', font_size=32, size_hint=(1, 0.1)))
        layout.add_widget(Label(text='Smart Construction Cost Estimator', font_size=24, size_hint=(1, 0.1)))
        btn = Button(text='Get Started', size_hint=(1, 0.2), font_size=20)
        btn.bind(on_press=self.go_to_auth)
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_to_auth(self, instance):
        self.manager.current = 'auth'

