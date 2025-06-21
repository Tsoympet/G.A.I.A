from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class GAIAAppMobile(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Welcome to GAIA Mobile Interface')
        self.btn1 = Button(text='Speak')
        self.btn2 = Button(text='Dream')
        self.btn1.bind(on_press=self.on_speak)
        self.btn2.bind(on_press=self.on_dream)
        self.add_widget(self.label)
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)

    def on_speak(self, instance):
        self.label.text = 'GAIA speaking...'

    def on_dream(self, instance):
        self.label.text = 'Generating a dream...'

class GAIAApp(App):
    def build(self):
        return GAIAAppMobile()

if __name__ == '__main__':
    GAIAApp().run()
