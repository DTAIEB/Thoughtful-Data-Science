from pixiedust.display.app import *

def call_me():
    print("Hello from call_me")

@PixieApp
class Test():
    @route()
    def main_screen(self):
        return """
        <button type="submit" pd_script="call_me()" pd_target="target{{prefix}}">Click me</button>
        
        <div id="target{{prefix}}"></div>
        """
Test().run()
