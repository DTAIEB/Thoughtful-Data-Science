[[StockExplorer]]
@route(explore="*")
@templateArgs
def stock_explore_screen(self):
   tabs = [("Explore","StockExploreSubApp"), ("Moving Average", "MovingAverageSubApp"),
                ("ACF and PACF", "AutoCorrelationSubApp"), ("Forecast with ARIMA", "ForecastArimaSubApp")] 
   …
