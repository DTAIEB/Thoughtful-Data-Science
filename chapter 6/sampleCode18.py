[[ScoreImageApp]]
@route(image_url="*")
@templateArgs
def do_process_url(self, image_url):
   image_urls = get_image_urls(image_url)
   return """
<div>
{%for url in image_urls%}
<div style="float: left; font-size: 9pt; text-align: center; width: 30%; margin-right: 1%; margin-bottom: 0.5em;">
<img src="{{url}}" style="width: 100%">
  <div style="display:inline-block" pd_render_onload pd_options="score_url={{url}}">
  </div>
</div>
{%endfor%}
<p style="clear: both;">
</div>
        """
