[[TensorGraphApp]]
return """
{%if this.custom_graph%}
<div style="margin-top:10px" pd_refresh>
    <pd_script>
self.graph = self.custom_graph if self.graph is not self.custom_graph else self.parent_pixieapp.graph
    </pd_script>
    <span style="font-weight:bold">Select a model to display:</span>
    <select>
        <option {%if this.graph!=this.custom_graph%}selected{%endif%} value="main">MobileNet</option>
        <option {%if this.graph==this.custom_graph%}selected{%endif%} value="custom">Custom</options>
    </select>
{%endif%}
<iframe seamless style="width:1200px;height:620px;border:0" srcdoc="{{code}}"></iframe>
"""
