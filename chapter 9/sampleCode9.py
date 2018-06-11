import matplotlib.cm as cm
fig = plt.figure(figsize = (12,12))
nx.draw(flight_graph, arrows=True, with_labels=True, width = 0.5,style="dotted",
        node_color=range(len(flight_graph)), cmap=cm.get_cmap(name="cool"),
        edge_color=range(len(flight_graph.edges)), edge_cmap=cm.get_cmap(name="spring")
       )
plt.show()
