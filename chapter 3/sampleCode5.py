import requests
import pandas
[[GitHubTracking]]
@route(query="*")
@templateArgs
def do_search(self, query):
    response = requests.get( "https://api.github.com/search/repositories?q={}".format(query))
    frames = [pandas.DataFrame(response.json()['items'])]
    while response.ok and "next" in response.links:
        response = requests.get(response.links['next']['url'])
        frames.append(pandas.DataFrame(response.json()['items']))

    pdf = pandas.concat(frames)
    response = requests.get( "https://api.github.com/search/repositories?q={}".format(query))
    if not response.ok:
        return "<div>An Error occurred: {{response.text}}</div>"
    return """<h1><center>{{pdf|length}} repositories were found</center></h1>"""
