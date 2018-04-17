@route(show_progress="true")
    def do_show_progress(self):
        return """
{%for query in this.spark.streams.active%}
    <div>
    <div class="page-header"> 
        <h1>Progress Report for Spark Stream: {{query.id}}</h1>
    <div>
    <table>
        <thead>
          <tr>
             <th>metric</th>
             <th>value</th>
          </tr>
        </thead>
        <tbody>
            {%for key, value in query.lastProgress.items()%}
            <tr>
                <td>{{key}}</td>
                <td>{{value}}</td>
            </tr>
            {%endfor%}
        </tbody>        
    </table>
{%endfor%}
        """
