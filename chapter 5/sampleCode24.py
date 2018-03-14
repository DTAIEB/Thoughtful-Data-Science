from pixiedust.display.app import *

@PixieApp
class TestJSDebugger():
    @route()
    def main_screen(self):
        return """
<script>
function FooJS(){
    debugger;
    return "value"
}
</script>
<button type="submit" pd_options="state=$val(FooJS)">Call route</button>
        """
    
    @route(state="*")
    def my_route(self, state):
        return "<div>Route called with state <b>{{state}}</b></div>"
    
app = TestJSDebugger()
app.run()
