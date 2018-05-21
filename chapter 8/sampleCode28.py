def plot_predict(model, dates_series, num_observations):
    fig = plt.figure(figsize = (12,5))
    model.plot_predict(
        start = str(dates_series[len(dates_series)-num_observations]), 
        end = str(dates_series[len(dates_series)-1])
    )
    plt.show()
    
plot_predict(arima_model, train_set['Date'], 100)
plot_predict(arima_model, train_set['Date'], 10) 
