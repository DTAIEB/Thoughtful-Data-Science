@route(do_training="*")
   @captureOutput
def do_training_screen(self):
       self.classifier, self.eval_results = \
      do_training(
self.train_x, self.train_y, self.test_x, self.test_y, self.num_classes
      )
        return """
<h2>Training completed successfully</h2>
<table>
    <thead>
        <th>Metric</th>
        <th>Value</th>
    </thead>
    <tbody>
{%for key,value in this.eval_results.items()%}
<tr>
    <td>{{key}}</td>
    <td>{{value}}</td>
</tr>
{%endfor%}
    </tbody>
</table>
        """ 
