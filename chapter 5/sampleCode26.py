from pixiedust.display.app import *
@PixieApp
class MyApp():
    @route(key1="value1", key2="*")
    @templateArgs
    def myroute_screen(self, key1, key2):
        local_var = "some value"
        return "<div>fragment: local_var = {{local_var}}"
