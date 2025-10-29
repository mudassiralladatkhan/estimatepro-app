"""
Minimal test version - NO Firebase, NO complex screens
This will help identify if the issue is Firebase, dependencies, or Kivy itself
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.logger import Logger

class MinimalApp(App):
    def build(self):
        Logger.info("MinimalApp: Starting build")
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(
            text='EstimatePro Test\nIf you see this, Kivy works!',
            font_size=24
        ))
        
        btn = Button(
            text='Click Me',
            size_hint=(1, 0.3),
            font_size=20
        )
        btn.bind(on_press=self.on_button_click)
        layout.add_widget(btn)
        
        self.status = Label(text='Status: Ready', font_size=18)
        layout.add_widget(self.status)
        
        Logger.info("MinimalApp: Build complete")
        return layout
    
    def on_button_click(self, instance):
        self.status.text = 'Status: Button clicked! App is working!'
        Logger.info("MinimalApp: Button clicked")

if __name__ == '__main__':
    MinimalApp().run()
