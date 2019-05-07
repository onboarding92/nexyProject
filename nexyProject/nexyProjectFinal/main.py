import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
import webbrowser
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os

from connected import Connected

class Redirect(Screen):
	def redirect(self):
		url = "https://dishcovery.menu/?gclid=EAIaIQobChMIyomKnIH44QIVxYTVCh3tuAdDEAAYASAAEgLMCvD_BwE"
		webbrowser.open_new(url)
		print ("hello")
	def next(self):
		print("next")
		self.manager.transition = SlideTransition(direction="right")
		self.manager.current = 'login'

class Login(Screen):
	def do_login(self, loginText, passwordText, telefonoText, cittaText, viaText, mailText):
		app = App.get_running_app()

		app.username = loginText
		app.password = passwordText
		app.telefono = telefonoText
		app.città = cittaText
		app.via = viaText
		app.mail = mailText

		self.manager.transition = SlideTransition(direction="left")
		self.manager.current = 'connected'

		print(app.username, app.password, app.telefono, app.città, app.via, app.mail)

		app.config.read(app.get_application_config())
		app.config.write()

	def resetForm(self):
		self.ids['login'].text = ""
		self.ids['password'].text = ""
		self.ids['telefono'].text = ""
		self.ids['citta'].text = ""
		self.ids['via'].text = ""
		self.ids['mail'].text = ""


class App(App):
		
	username = StringProperty(None)
	password = StringProperty(None)
	telefono = StringProperty(None)
	citta = StringProperty(None)
	via = StringProperty(None)
	mail = StringProperty(None)


	def build(self):
		self.root = Builder.load_file("test.kv")
		manager = ScreenManager()
		manager.add_widget(Redirect(name="redirect"))
		manager.add_widget(Login(name='login'))
		manager.add_widget(Connected(name='connected'))
		
		return manager
	
	def get_application_config(self):
		if(not self.username):
			return super(App, self).get_application_config()

		conf_directory = self.user_data_dir + '/' + self.username

		if(not os.path.exists(conf_directory)):
			os.makedirs(conf_directory)

		return super(App, self).get_application_config(
		'%s/config.cfg' % (conf_directory)
		)
	

if __name__ == '__main__':
	App().run()


