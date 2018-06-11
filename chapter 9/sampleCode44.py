from pixiedust.apps.template import TemplateTabbedApp

@PixieApp
class RouteAnalysisApp(TemplateTabbedApp):
    def setup(self):
        self.apps = [
            {"title": "Search Shortest Route", "app_class": "SearchShortestRouteApp"},
            {"title": "Explore Airlines", "app_class": "AirlinesApp"},
            {"title": "Flight Delay Prediction", "app_class": "PredictDelayApp"}
        ]
