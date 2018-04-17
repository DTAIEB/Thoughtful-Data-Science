from pixiedust.display.app import *
from pixiedust.apps.template import TemplateTabbedApp

@PixieApp
class TwitterSentimentApp(TemplateTabbedApp):
    def setup(self):
        self.apps = [
            {"title": "Tweets Insights", "app_class": "TweetInsightApp"},
            {"title": "Streaming Queries", "app_class": "StreamingQueriesApp"}
        ]
        
app = TwitterSentimentApp()
app.run()
