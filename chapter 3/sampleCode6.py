[[GitHubTracking]]
@route(query="*")
@templateArgs
def do_search(self, query):
    self.first_url = "https://api.github.com/search/repositories?q={}".format(query)
    self.prev_url = None
    self.next_url = None
    self.last_url = None
    
    response = requests.get(self.first_url)
    if not response.ok:
        return "<div>An Error occurred: {{response.text}}</div>"

    total_count = response.json()['total_count']
    self.next_url = response.links.get('next', {}).get('url', None)
    self.last_url = response.links.get('last', {}).get('url', None)
    return """
<h1><center>{{total_count}} repositories were found</center></h1>
<ul class="pagination">
  <li><a href="#" pd_options="page=first_url" pd_target="body{{prefix}}">First</a></li>
  <li><a href="#" pd_options="page=prev_url" pd_target="body{{prefix}}">Prev</a></li>
  <li><a href="#" pd_options="page=next_url" pd_target="body{{prefix}}">Next</a></li>
  <li><a href="#" pd_options="page=last_url" pd_target="body{{prefix}}">Last</a></li>
</ul>
<table class="table">
    <thead>
        <tr>
            <th>Repo Name</th>
            <th>Lastname</th>
            <th>URL</th>
            <th>Stars</th>
        </tr>
    </thead>
    <tbody id="body{{prefix}}">
        {{this.invoke_route(this.do_retrieve_page, page='first_url')}}
    </tbody>
</table>
"""
