from sklearn.metrics import mean_squared_error
def compute_mean_squared_error(test_series, forecast_series):
    return mean_squared_error(test_series, forecast_series)

print('Mean Squared Error: {}'.format( 
compute_mean_squared_error( test_set['Adj. Close'], results.forecast)) 
)
