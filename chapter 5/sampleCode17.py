from pixiedust.display.chart.renderers import PixiedustRenderer
from pixiedust.display.chart.renderers.baseChartDisplay import BaseChartDisplay

@PixiedustRenderer(rendererId="simpletable", id="tableView")
class SimpleDisplayWithRenderer(BaseChartDisplay):
    def get_options_dialog_pixieapp(self):
        return None #No options needed
    
    def doRenderChart(self):
        return self.renderTemplateString("""
<table class="table table-striped">
   <thead>
       {%for column in entity.columns.tolist()%}
       <th>{{column}}</th>
       {%endfor%}
   </thead>
   <tbody>
       {%for _, row in entity.iterrows()%}
       <tr>
           {%for value in row.tolist()%}
           <td>{{value}}</td>
           {%endfor%}
       </tr>
       {%endfor%}
   </tbody>
</table>
        """)
