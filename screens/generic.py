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
# -----------------------------------------------
class EstimatorScreen(Screen):
    def __init__(self, category_name, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        layout.add_widget(Label(text=f"{category_name} Estimator", font_size=24))

        self.input_field = TextInput(hint_text='Enter quantity', multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.input_field)

        calc_btn = Button(text='Calculate Cost', size_hint=(1, None), height=40)
        calc_btn.bind(on_press=self.calculate)
        layout.add_widget(calc_btn)

        self.result_label = Label(text='', font_size=16)
        layout.add_widget(self.result_label)

        back_btn = Button(text='Back to Dashboard', size_hint=(1, None), height=40)
        back_btn.bind(on_press=lambda instance: setattr(self.manager, 'current', 'dashboard'))
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def calculate(self, instance):
        value = self.input_field.text
        self.result_label.text = f"Estimated cost for '{value}' units"

