[[LabelsApp]]
@PixieApp
class LabelsApp():
    def setup(self):
        self.labels = self.parent_pixieapp.load_labels(
            self.parent_pixieapp.model, as_json=True
        )
    
    @route()
    def main_screen(self):
        return """
<div pd_render_onload pd_entity="labels">
    <pd_options>
    {
        "table_noschema": "true",
        "handlerId": "tableView",
        "rowCount": "10000"
    }
    </pd_options>
</div>
        """
