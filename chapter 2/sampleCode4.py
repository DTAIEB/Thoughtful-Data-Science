import pixiedust
data_url = "https://data.cityofnewyork.us/api/views/e98g-f8hy/rows.csv?accessType=DOWNLOAD"
building_dataframe = pixiedust.sampleData(data_url, forcePandas=True)
