[[LabelsApp]]
@PixieApp
class LabelsApp():
    def setup(self):
        …
    
    @route()
    def main_screen(self):
        return """
{%if this.custom_labels%}
<div style="margin-top:10px" pd_refresh>
    <pd_script>
self.current_labels = self.custom_labels if self.current_labels is not self.custom_labels else self.labels
    </pd_script>
    <span style="font-weight:bold">Select a model to display:</span>
    <select>
        <option {%if this.current_labels!=this.labels%}selected{%endif%} value="main">MobileNet</option>
        <option {%if this.current_labels==this.custom_labels%}selected{%endif%} value="custom">Custom</options>
    </select>
{%endif%}
<div pd_render_onload pd_entity="current_labels">
    <pd_options>
    {
        "table_noschema": "true",
        "handlerId": "tableView",
        "rowCount": "10000",
        "noChartCache": "true"
        
    }
    </pd_options>
</div>
        """
