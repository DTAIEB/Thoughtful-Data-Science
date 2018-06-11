flight_graph = nx.from_pandas_edgelist(
    flights, "ORIGIN_AIRPORT","DESTINATION_AIRPORT", "ELAPSED_TIME", 
    create_using = nx.DiGraph() )
