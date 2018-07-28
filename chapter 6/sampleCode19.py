[[ScoreImageApp]]
@route(score_url="*")
@templateArgs
def do_score_url(self, score_url):
   results = score_image(self.graph, self.model, score_url)
   return """
<ul style="text-align:left">
{%for label, confidence in results%}
<li><b>{{label}}</b>: {{confidence}}</li>
{%endfor%}
</ul>
"""
