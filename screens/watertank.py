from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class WaterTankScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation='vertical')
        with root.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=root.size, pos=root.pos)
        root.bind(size=self._update_bg, pos=self._update_bg)

        scroll = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        content.add_widget(Label(
            text='Water Tank Estimator',
            font_size=22,
            size_hint=(1, None),
            height=40,
            color=(0.1, 0.1, 0.1, 1),
            bold=True
        ))

        def styled_input(hint):
            return TextInput(
                hint_text=hint,
                multiline=False,
                input_filter='float',
                size_hint=(1, None),
                height=50,
                background_color=(0.95, 0.95, 0.95, 1),
                foreground_color=(0, 0, 0, 1),
                padding=(10, 10)
            )

        self.length_input = styled_input('Tank Length (m)')
        self.width_input = styled_input('Tank Width (m)')
        self.height_input = styled_input('Tank Height (m)')
        self.cost_input = styled_input('Cost per m² (₹)')

        content.add_widget(self.length_input)
        content.add_widget(self.width_input)
        content.add_widget(self.height_input)
        content.add_widget(self.cost_input)

        btn_layout = BoxLayout(size_hint=(1, None), height=40, spacing=10)
        calc_btn = Button(text='Calculate', background_color=(0.2, 0.6, 0.2, 1), font_size=14, size_hint=(0.5, 1))
        clear_btn = Button(text='Clear', background_color=(0.8, 0.2, 0.2, 1), font_size=14, size_hint=(0.5, 1))
        calc_btn.bind(on_press=self.calculate)
        clear_btn.bind(on_press=self.clear)
        btn_layout.add_widget(calc_btn)
        btn_layout.add_widget(clear_btn)
        content.add_widget(btn_layout)

        self.result_label = Label(text='', font_size=16, size_hint=(1, None), height=30, color=(0, 0.5, 0, 1))
        content.add_widget(self.result_label)

        back_btn = Button(text='← Back', size_hint=(None, None), size=(100, 35), font_size=12,
                          background_color=(0.7, 0.7, 0.7, 1), color=(0, 0, 0, 1))
        back_btn.bind(on_press=lambda instance: setattr(self.manager, 'current', 'dashboard'))
        content.add_widget(back_btn)

        scroll.add_widget(content)
        root.add_widget(scroll)
        self.add_widget(root)

    def _update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def calculate(self, instance):
        try:
            length = float(self.length_input.text)
            width = float(self.width_input.text)
            height = float(self.height_input.text)
            cost_per_m2 = float(self.cost_input.text)

            surface_area = 2 * (length * height + width * height) + (length * width)
            total_cost = surface_area * cost_per_m2

            self.result_label.text = f"Surface Area: {surface_area:.2f} m² | Estimated Cost: ₹{total_cost:,.2f}"
        except ValueError:
            self.result_label.text = "Please enter valid numbers."

    def clear(self, instance):
        self.length_input.text = ''
        self.width_input.text = ''
        self.height_input.text = ''
        self.cost_input.text = ''
        self.result_label.text = ''
