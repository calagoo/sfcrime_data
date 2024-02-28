import osmnx as ox
from osmnx import routing
import matplotlib.pyplot as plt


class Node:
    def __init__(self, id, lat, lon):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.nearest_node = None

    def __str__(self):
        return "Node id: " + str(self.id) + " Lat: " + str(self.lat) + " Lon: " + str(self.lon)

    def __repr__(self):
        return str(self)
    
    def find_nearest_node(self, graph):
        self.nearest_node = ox.nearest_nodes(graph, self.lon, self.lat)

def main():

    node1 = Node(1, 37.78338518997091, -122.43956939968092)
    node2 = Node(2, 37.77571129565835, -122.42438491079076)
    # Define the location (San Francisco)
    place_name = "San Francisco, California, USA"

    # Download the street network
    graph = ox.graph_from_place(place_name, network_type="walk")


    # Get the closest node
    node1.find_nearest_node(graph)
    node2.find_nearest_node(graph)

    # Create a route between the nodes using the shortest path algorithm
    route = routing.shortest_path(graph, node1.nearest_node, node2.nearest_node, weight="length")

    # Plot the street network
    if route:
        ox.plot_graph_route(graph, route)
    else:
        print("No route found between the nodes.")

if __name__ == "__main__":
    main()
