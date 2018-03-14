from datetime import datetime
import requests
import pandas
def load_commit_activity(owner, repo_name):
    response = requests.get(
        "https://api.github.com/repos/{}/{}/stats/commit_activity".format(owner, repo_name),
        auth=(github_user, github_token)
    ).json()
    pdf = pandas.DataFrame([
        {"total": item["total"], "week":datetime.fromtimestamp(item["week"])} for item in response
    ])
    
    return {
        "pdf":pdf,
        "chart_options": {
          "handlerId": "lineChart",
          "keyFields": "week",
          "valueFields": "total",
          "aggregation": "SUM",
          "rendererId": "bokeh"
        }
    }
