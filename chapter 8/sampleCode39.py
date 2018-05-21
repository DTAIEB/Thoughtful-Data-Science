    @route(plot_predict="true")
    @captureOutput
    def plot_predict(self):
        plot_predict(self.arima_model, self.train_set['Date'], 100)
