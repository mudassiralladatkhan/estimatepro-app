from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class ConcreteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Root layout with white background
        root = BoxLayout(orientation='vertical')
        with root.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=root.size, pos=root.pos)
        root.bind(size=self._update_bg, pos=self._update_bg)

        # Scrollable content
        scroll = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        # Title
        content.add_widget(Label(
            text='Concrete Volume Estimator',
            font_size=22,
            size_hint=(1, None),
            height=40,
            color=(0.1, 0.1, 0.1, 1),
            bold=True
        ))

        # Input styling
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

        self.length_input = styled_input('Length (m)')
        self.width_input = styled_input('Width (m)')
        self.depth_input = styled_input('Depth (m)')
        self.price_input = styled_input('Price per m³ (₹)')

        for field in [self.length_input, self.width_input, self.depth_input, self.price_input]:
            content.add_widget(field)

        # Buttons (compact and modern)
        btn_layout = BoxLayout(size_hint=(1, None), height=40, spacing=10)
        calc_btn = Button(
            text='Calculate',
            background_color=(0.2, 0.6, 0.2, 1),
            font_size=14,
            size_hint=(0.5, 1)
        )
        clear_btn = Button(
            text='Clear',
            background_color=(0.8, 0.2, 0.2, 1),
            font_size=14,
            size_hint=(0.5, 1)
        )
        calc_btn.bind(on_press=self.calculate_cost)
        clear_btn.bind(on_press=self.clear_inputs)
        btn_layout.add_widget(calc_btn)
        btn_layout.add_widget(clear_btn)
        content.add_widget(btn_layout)

        # Result label
        self.result_label = Label(
            text='',
            font_size=16,
            size_hint=(1, None),
            height=30,
            color=(0, 0.5, 0, 1)
        )
        content.add_widget(self.result_label)

        # Back button (small and clean)
        back_btn = Button(
            text='← Back',
            size_hint=(None, None),
            size=(100, 35),
            font_size=12,
            background_color=(0.7, 0.7, 0.7, 1),
            color=(0, 0, 0, 1)
        )
        back_btn.bind(on_press=lambda instance: setattr(self.manager, 'current', 'dashboard'))
        content.add_widget(back_btn)

        scroll.add_widget(content)
        root.add_widget(scroll)
        self.add_widget(root)

    def _update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def calculate_cost(self, instance):
        try:
            length = float(self.length_input.text)
            width = float(self.width_input.text)
            depth = float(self.depth_input.text)
            price = float(self.price_input.text)

            volume = length * width * depth
            cost = volume * price

            self.result_label.text = f"Estimated Cost: ₹{cost:,.2f}"
        except ValueError:
            self.result_label.text = "Please enter valid numbers."

    def clear_inputs(self, instance):
        self.length_input.text = ''
        self.width_input.text = ''
        self.depth_input.text = ''
        self.price_input.text = ''
        self.result_label.text = ''
