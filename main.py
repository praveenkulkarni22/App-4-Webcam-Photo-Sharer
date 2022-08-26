
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# The main.py file and frontend.kv file do not communicate.
# You need to let the main.py file know about frontend.kv configurations.
# You can do that using Builder class.

from kivy.lang import Builder
import wikipedia as wp
import requests as rq

Builder.load_file('frontend.kv')


# how many screen classes are required? We need as many screens are available.
class FirstScreen(Screen):
    # The first screen is going to have methods depending on what are you doing to do with the screen
    def search_image(self):

        # self refers to the instance of FirstScreen
        # manager is an attribute of screen object.
        # current_screen is an attribute of manager as so on.
        # The ids attribute gives the list of ids in the current screen object.
        # --------------------------------------------------------------------
        # self.manager.current_screen.ids.img.source = 'files/Thimmi.jpg'
        # --------------------------------------------------------------------
        # Therefore, the above line of cde is same as setting the source property in frontend.kv
        # file for source id under Image attribute.

        # First the Image Search functionality should grab the text from the text field.
        query = self.manager.current_screen.ids.user_query.text

        # Now lets search the same in wikipedia and get the page and the images in it.
        wiki_page = wp.page(query)
        image_links = wiki_page.images[0]
        req = rq.get(image_links)
        img_path = 'files/image.jpg'
        with open(img_path, 'wb') as f:
            f.write(req.content)
        self.manager.current_screen.ids.img.source = img_path


# The App is the main class. However, the App has a screen manager.

class RootWidget(ScreenManager):
    pass


# kivy is a library and it has many classes. One of the class is App which initializes the app.
# We inherit the App class in our MainApp

class MainApp(App):
    # The App class has a default build method. We need to overwrite the default build class.
    def build(self):
        # The Build method has to return another class - the screen manager.
        # In other words, The App class returns the RootWidget.
        return RootWidget()


MainApp().run()
