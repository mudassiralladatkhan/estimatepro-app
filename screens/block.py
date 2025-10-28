from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class BlockScreen(Screen):
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
            text='Block Estimator',
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

        self.wall_length = styled_input('Wall Length (m)')
        self.wall_height = styled_input('Wall Height (m)')
        self.block_length = styled_input('Block Length (cm)')
        self.block_height = styled_input('Block Height (cm)')
        self.cost_per_block = styled_input('Cost per Block (₹)')

        content.add_widget(self.wall_length)
        content.add_widget(self.wall_height)
        content.add_widget(self.block_length)
        content.add_widget(self.block_height)
        content.add_widget(self.cost_per_block)

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
            wall_length = float(self.wall_length.text)
            wall_height = float(self.wall_height.text)
            block_length = float(self.block_length.text)
            block_height = float(self.block_height.text)
            cost_per_block = float(self.cost_per_block.text)

            wall_area_cm2 = wall_length * wall_height * 10000
            block_area_cm2 = block_length * block_height
            blocks_needed = (wall_area_cm2 / block_area_cm2) * 1.05
            total_cost = blocks_needed * cost_per_block

            self.result_label.text = f"Blocks Needed: {int(blocks_needed)} | Estimated Cost: ₹{total_cost:,.2f}"
        except ValueError:
            self.result_label.text = "Please enter valid numbers."

    def clear(self, instance):
        self.wall_length.text = ''
        self.wall_height.text = ''
        self.block_length.text = ''
        self.block_height.text = ''
        self.cost_per_block.text = ''
        self.result_label.text = ''
