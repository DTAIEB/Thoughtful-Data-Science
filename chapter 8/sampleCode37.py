@route(show_acf='*')
@captureOutput
def show_acf_screen(self):
    smt.graphics.plot_acf(self.entity_dataframe['Adj. Close'], lags=50)

@route(show_pacf='*')
@captureOutput
def show_pacf_screen(self):
    smt.graphics.plot_pacf(self.entity_dataframe['Adj. Close'], lags=50)
