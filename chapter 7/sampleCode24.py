@PixieApp
class StreamingQueriesApp():
    @route()
    def main_screen(self):
        return """
<div class="no_loading_msg" pd_refresh_rate="5000" pd_options="show_progress=true">
</div>
        """
