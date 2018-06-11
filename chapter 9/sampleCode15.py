import matplotlib.cm as cm
def visualize_neighbors(parent_node):
    fig = plt.figure(figsize = (12,12))
    # Create a subgraph and add an edge from the parent node to all its neighbors
    graph = nx.DiGraph()
    for neighbor in flight_graph.neighbors(parent_node):
        graph.add_edge(parent_node, neighbor)
    # draw the subgraph
    nx.draw(graph, arrows=True, with_labels=True, width = 0.5,style="dotted",
            node_color=range(len(graph)), cmap=cm.get_cmap(name="cool"),
            edge_color=range(len(graph.edges)), edge_cmap=cm.get_cmap(name="spring"),
           )
    plt.show()
