@PixieApp
class Test():
    @route()
    def main_screen(self):
        return """
        <button type="submit" 
pd_script="call_me()" 
pd_target="target{{prefix}}">
            <pd_script>
self.name="some value"
print("This is a multi-line pd_script")
            </pd_script>
            Click me
        </button>
        
        <div id="target{{prefix}}"></div>
        """
Test().run()
