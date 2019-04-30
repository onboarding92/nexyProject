import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
import webbrowser
from kivy.uix.pagelayout import PageLayout
 # You would need futhermore this
class Launch(PageLayout):
	def __init__(self, **kwargs):
		super(Launch, self).__init__(**kwargs)
		mybutton = Button(
			text = 'Click me',
			size = (80,80),
			size_hint = (None,None)
			)
		mybutton.bind(on_press = self.say_hello) # Note: here say_hello doesn't have brackets.
		Launch.add_widget(self, mybutton)

	def say_hello(self):
		url = "https://dishcovery.menu/?gclid=EAIaIQobChMIyomKnIH44QIVxYTVCh3tuAdDEAAYASAAEgLMCvD_BwE"
		webbrowser.open_new(url)
		print ("hello")

class App(App):
	def build(self):
		self.root = Builder.load_file("test.kv")
		return Launch()


if __name__ == '__main__':
	App().run()


