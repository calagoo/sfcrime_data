import osmnx as ox

# Define the location (San Francisco)
place_name = "San Francisco, California, USA"

# Download the street network
graph = ox.graph_from_place(place_name, network_type="drive")

# Plot the street network
ox.plot_graph(ox.project_graph(graph))