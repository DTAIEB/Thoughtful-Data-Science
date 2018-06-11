[[USFlightsAnalysis]]
def compute_toggle_centrality_layer(self, org_airport, dest_airport, centrality):
    cache.clear()
    cities = nx.dijkstra_path(flight_graph, org_airport, dest_airport, weight=compute_weight(centrality))
    layer_index = self.get_layer_index(centrality, {
        "name": centrality,
        "geojson": {
            "type": "FeatureCollection",
            "features":[
                {"type":"Feature",
                 "properties":{"route":"{} to {}".format(cities[i], cities[i+1])},
                 "geometry":{
                     "type":"LineString",
                     "coordinates":[
                         self.get_airport_location(cities[i]),
                         self.get_airport_location(cities[i+1])
                     ]
                 }
                } for i in range(len(cities) - 1)
            ]
        },
        "paint":{
            "line-width": 8,
            "line-color": self.centrality_indices[centrality]
        }
    })
    self.toggleLayer(layer_index)
