[[StockExplorer]]
def select_tickers(self, tickers):
        self.tickers = {ticker.strip():{} for ticker in tickers}
        self.set_active_ticker(tickers[0].strip())
        
def set_active_ticker(self, ticker):
    self.active_ticker = ticker
    if 'df' not in self.tickers[ticker]:
        self.tickers[ticker]['df'] = quandl.get('WIKI/{}'.format(ticker))
        self.tickers[ticker]['df']['daily_spread'] = self.tickers[ticker]['df']['Adj. Close'] - self.tickers[ticker]['df']['Adj. Open']
        self.tickers[ticker]['df'] = self.tickers[ticker]['df'].reset_index()
