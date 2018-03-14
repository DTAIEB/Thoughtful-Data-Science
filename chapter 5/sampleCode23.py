from pixiedust.display.app import *
from pixiedust.utils import Logger

@PixieApp
@Logger()
class AppWithLogger():
    @route()
    def main_screen(self):
        self.info("Calling default route")
        return "<div>hello world</div>"
    
app = AppWithLogger()
app.run()
