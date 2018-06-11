def compute_delay_airline_df(airline, org_airport=None):
	# create a mask for selecting the data
   mask = (flights["AIRLINE"] == airline)
   if org_airport is not None:
	    # Add the org_airport to the mask
       mask = mask & (flights["ORIGIN_AIRPORT"] == org_airport)
   # Apply the mask to the Pandas dataframe
   df = flights[mask]
   # Convert the YEAR, MONTH and DAY column into a DateTime
   df["DATE"] = pd.to_datetime(flights[['YEAR','MONTH', 'DAY']])
   # Select only the columns that we need
   return df[["DATE", "ARRIVAL_DELAY"]]
