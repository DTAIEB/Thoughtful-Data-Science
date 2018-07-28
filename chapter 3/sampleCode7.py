[[GitHubTracking]]
@route(page="*")
@templateArgs
def do_retrieve_page(self, page):
    url = getattr(self, page)
    if url is None:
        return "<div>No more rows</div>"
    response = requests.get(url)
    self.prev_url = response.links.get('prev', {}).get('url', None)
    self.next_url = response.links.get('next', {}).get('url', None)
    items = response.json()['items']
    return """
{%for row in items%}
<tr>
    <td>{{row['name']}}</td>
    <td>{{row.get('owner',{}).get('login', 'N/A')}}</td>
    <td><a href="{{row['html_url']}}" target="_blank">{{row['html_url']}}</a></td>
    <td>{{row['stargazers_count']}}</td>
</tr>
{%endfor%}
        """
