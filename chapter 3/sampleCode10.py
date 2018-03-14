from pixiedust.display.app import *
@PixieApp
class TestEntity():
    @route()
    def main_screen(self):
        return """
        <h1><center>Simple PixieApp with dynamically computed dataframe</center></h1>
        <div pd_entity="compute_pdf('prefix')" pd_options="handlerId=dataframe" pd_render_onload></div>
        """
test = TestEntity()
test.run()
