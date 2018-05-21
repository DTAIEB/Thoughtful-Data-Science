import statsmodels.tsa.api as smt
smt.graphics.plot_acf(logmsft_diff, lags=100)
plt.show()
