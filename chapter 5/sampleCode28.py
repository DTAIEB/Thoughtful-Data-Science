from pixiedust.display.app import *
from pixiedust.utils import Logger
@PixieApp
@Logger()
class MyApp():
    @route()
    def main_screen(self):
        self.debug("In main_screen")
        return "<div>Hello World</div>"
