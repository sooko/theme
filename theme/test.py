from __init__ import NavBar
from kivy.app import App


class MyApp(App):
    def build(self):
        return NavBar()

if __name__=="__main__":
    MyApp().run()