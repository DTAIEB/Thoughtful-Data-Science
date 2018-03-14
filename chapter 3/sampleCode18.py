from pixiedust.display.app import *

@PixieApp
class WidgetApp():
    @route(widget="my_widget")
    def widget_main_screen(self):
        return "<div>Hello World Widget</div>"
    
@PixieApp
class ConsummerApp(WidgetApp):
    @route()
    def main_screen(self):
        return """<div pd_widget="my_widget"></div>"""
    
ConsummerApp().run()
