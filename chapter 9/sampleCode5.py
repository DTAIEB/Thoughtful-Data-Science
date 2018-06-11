edges = flights.groupby(["ORIGIN_AIRPORT","DESTINATION_AIRPORT"]) [["ELAPSED_TIME"]].mean()
edges
