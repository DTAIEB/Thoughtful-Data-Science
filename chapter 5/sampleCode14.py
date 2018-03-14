from pixiedust.display.app import *
@PixieApp
class TestEvents():
    @route()
    def main_screen(self):
        return """
<div>
    <button type="submit">
        <pd_event_payload>
        {
            "type":"topicA",
            "message":"Button Clicked"
        }
        </pd_event_payload>
        Send event A
    </button>
    <table onclick="pixiedust.sendEvent({type:'topicB',text:event.srcElement.innerText})">
        <tr><td>Row 1</td></tr>
        <tr><td>Row 2</td></tr>
        <tr><td>Row 3</td></tr>
    </table>
</div>
<div class="container" style="margin-top:30px">
    <div class="row">
        <div class="col-sm-6" id="listenerA{{prefix}}">
            Listening to button event
            <pd_event_handler pd_source="topicA" pd_script="print(eventInfo)" pd_target="listenerA{{prefix}}">
            </pd_event_handler>
        </div>
        <div class="col-sm-6" id="listenerB{{prefix}}">
            Listening to table event
            <pd_event_handler pd_source="topicB" pd_script="print(eventInfo)" pd_target="listenerB{{prefix}}">
            </pd_event_handler>
        </div>
    </div>
</div>
        """ 
app = TestEvents()
app.run()
