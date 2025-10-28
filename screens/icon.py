from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

class IconButton(Button):
    def __init__(self, icon_path, label_text, on_press_callback, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (1, 1, 1, 1)

        layout = BoxLayout(orientation='vertical', spacing=5, padding=5)
        img = Image(source=icon_path, size_hint=(1, 0.8))
        label = Label(text=label_text, size_hint=(1, 0.2), color=(0, 0, 0, 1), font_size=12)

        layout.add_widget(img)
        layout.add_widget(label)
        self.add_widget(layout)
        self.bind(on_press=on_press_callback)
