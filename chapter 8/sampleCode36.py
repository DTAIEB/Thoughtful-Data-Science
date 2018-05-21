def toggle_differencing(self):
   if self.differencing:
       self.entity_dataframe = self.parent_pixieapp.get_active_df().copy()
       self.differencing = False
   else:
       log_df = np.log(self.entity_dataframe['Adj. Close'])
       log_df.index = self.entity_dataframe['Date']
       self.entity_dataframe = pd.DataFrame(log_df - log_df.shift()).reset_index()
       self.entity_dataframe.dropna(inplace=True)
       self.differencing = True
