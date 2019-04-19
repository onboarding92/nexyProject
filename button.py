import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
 # You would need futhermore this
class Launch(BoxLayout):
    def __init__(self, **kwargs):
        super(Launch, self).__init__(**kwargs)
        mybutton = Button(
                            text = 'Click me',
                            size = (80,80),
                            size_hint = (None,None)
                          )
        mybutton.bind(on_press = self.say_hello) # Note: here say_hello doesn't have brackets.
        Launch.add_widget(self, mybutton)

    def say_hello(self, mybutton):
        print ("hello")

class App(App):
    def build(self):
        return Launch()


if __name__ == '__main__':
    App().run()


