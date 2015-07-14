from kivy.app import App
from kivy.uix.button import Button

class Hello(App):
    def build(self):
        btn = Button(text='Hello World!')
        return btn

Hello().run()
