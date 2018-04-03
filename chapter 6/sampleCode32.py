@route(score_url="*")
@templateArgs
def do_score_url(self, score_url):
   scores_dict = score_image(self.graph, self.model, score_url)
   return """
{%for model, results in scores_dict.items()%}
<div style="font-weight:bold">{{model}}</div>
<ul style="text-align:left">
{%for label, confidence in results%}
<li><b>{{label}}</b>: {{confidence}}</li>
{%endfor%}
</ul>
{%endfor%}
   """
