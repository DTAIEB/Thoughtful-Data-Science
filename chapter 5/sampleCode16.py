class SimpleDisplay(Display):
    def doRender(self, handlerId):
        self._addHTMLTemplateString("""
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
