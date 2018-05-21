import requests
databases = []
page = 1
while(page is not None):
    payload = requests.get("https://www.quandl.com/api/v3/databases?api_key={}&page={}"\
                    .format(quandl.ApiConfig.api_key, page)).json()
    databases += payload['databases']
    page = payload['meta']['next_page']
