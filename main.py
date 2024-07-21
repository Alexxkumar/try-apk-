from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar

class PhonePeInspiredApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return HomeScreen()

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create main layout
        layout = MDBoxLayout(orientation='vertical')
        
        # Add top app bar
        toolbar = MDTopAppBar(title="PhonePe Inspired")
        layout.add_widget(toolbar)
        
        # Add main content area
        content = MDBoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Add some buttons to simulate PhonePe features
        buttons = [
            "Send Money",
            "Recharge",
            "Pay Bills",
            "Book Tickets",
            "Investments"
        ]
        
        for button_text in buttons:
            button = MDRaisedButton(
                text=button_text,
                size_hint=(1, None),
                height="48dp"
            )
            content.add_widget(button)
        
        layout.add_widget(content)
        self.add_widget(layout)

if __name__ == '__main__':
    PhonePeInspiredApp().run()


