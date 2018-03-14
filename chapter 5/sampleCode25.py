from pixiedust.display.app import *
@PixieApp
class MyApp():
    @route(key1="value1", key2="*")
    def myroute_screen(self, key1, key2):
        return "<div>fragment: Key1 = {{key1}} - Key2 = {{key2}}"
