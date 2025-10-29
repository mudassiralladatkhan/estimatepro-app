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
from firebase_config import auth  # Make sure this file exists

class IconButton(ButtonBehavior, BoxLayout):
    def __init__(self, icon_path, label_text, on_press_callback, **kwargs):
        super().__init__(orientation='vertical', spacing=4, padding=4, **kwargs)
        self.size_hint = (1, None)
        self.height = 300
        self.image = Image(source=icon_path, size_hint=(1, 0.85), allow_stretch=True, keep_ratio=True)
        self.label = Label(text=label_text, font_size=16, size_hint=(1, 0.15), halign='center', valign='middle')
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.image)
        self.add_widget(self.label)
        self.bind(on_press=lambda instance: on_press_callback(label_text))

# -----------------------------------------------
# Dashboard Screen
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='vertical', padding=10, spacing=5)
        root.add_widget(Label(text='Dashboard', font_size=20, size_hint=(1, 0.1)))

        scroll = ScrollView(size_hint=(1, 0.8))
        grid = GridLayout(cols=2, spacing=6, padding=6, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        self.categories = {
            "Concrete": "concrete.jpg",
            "Steel": "steel.jpg",
            "Bricks": "brick.jpg",
            "Plaster": "plaster.jpg",
            "Paint": "paint.jpg",
            "Tiles": "tile.jpg",
            "Excavation": "excavation.jpg",
            "Blocks": "block.jpg",
            "AntiTermite": "antitermite.jpg",
            "SlopeFilling": "slopefilling.jpg",
            "WaterTank": "watertank.jpg"
        }

        for name, icon in self.categories.items():
            btn = IconButton(icon_path=icon, label_text=name, on_press_callback=self.open_estimator)
            grid.add_widget(btn)

        scroll.add_widget(grid)
        root.add_widget(scroll)

        back_btn = Button(text='Back to Home', size_hint=(1, 0.1), font_size=16)
        back_btn.bind(on_press=lambda instance: setattr(self.manager, 'current', 'home'))
        root.add_widget(back_btn)

        self.add_widget(root)

    def open_estimator(self, category_name):
        # Map category names to actual screen names
        screen_map = {
            "Concrete": "concrete",
            "Steel": "steel",
            "Bricks": "bricks",
            "Plaster": "plaster",
            "Paint": "paint",
            "Tiles": "tiles",
            "Excavation": "excavation",
            "Blocks": "blocks",
            "AntiTermite": "antitermite",
            "SlopeFilling": "slopefilling",
            "WaterTank": "watertank"
        }
        screen_name = screen_map.get(category_name, category_name.lower())
        if self.manager.has_screen(screen_name):
            self.manager.current = screen_name
        else:
            print(f"Screen '{screen_name}' not found!")



