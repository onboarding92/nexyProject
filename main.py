'''
Widget animation
================

This example demonstrates creating and applying a multi-part animation to
a button widget. You should see a button labelled 'plop' that will move with
an animation when clicked.
'''

from kivy.app import App
from kivy.uix.pagelayout import PageLayout


class PageLayoutDemo(PageLayout):
    pass


class TestApp(App):
    title = "Kivy PageLayout Demo"

    def build(self):
        return PageLayoutDemo()


if __name__ == "__main__":
    TestApp().run()
