for col_name in ["DEGREE", "PAGE_RANK", "CLOSENESS", "BETWEENNESS"]:
    print("{} : {}".format(
        col_name, 
        airports_centrality.nlargest(10, col_name)["IATA_CODE"].values)
    )
