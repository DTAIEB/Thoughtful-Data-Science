[[PredictDelayApp]] 
@route(flight_segment="*", airline="*")
    @captureOutput
    def predict_screen(self, flight_segment, airline):
        if flight_segment is None or flight_segment == "":
            return "<div>Please select a flight segment</div>"
        airport = flight_segment.split(":")[1]
        mask = (flights["DESTINATION_AIRPORT"] == airport)
        if airline is not None and airline != "":
            mask = mask & (flights["AIRLINE"] == airline)
        df = flights[mask]
        df.index = df["DEPARTURE_TIME"]
        df = df.tail(50000)
        df = df[~df.index.duplicated(keep='first')]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            arima_model_class = ARIMA(df["ARRIVAL_DELAY"], dates=df['DEPARTURE_TIME'], order=(1,1,1))
            arima_model = arima_model_class.fit(disp=0)
            fig, ax = plt.subplots(figsize = (12,8))
            num_observations = 100  
            date_series = df["DEPARTURE_TIME"]
            arima_model.plot_predict(
                start = str(date_series[len(date_series)-num_observations]), 
                end = str(date_series[len(date_series)-1]),
                ax = ax
            )
            plt.show()
