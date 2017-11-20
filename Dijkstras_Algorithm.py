#Dijkstra's (pronounced deyek-stra) algorithm is for finding the shortest possible
#path in weighted directed acyclic graphs. NOTE Dijkstra's algorithm does not work
#on graphs with negative weighted edges. See the Bellman-ford algorithm

class Dijkstra(object):
    def __init__(self, graph):
        """Initialise Dijkstra search.
        Params:
            Graph: should be a nested dictionary detailing nodes, neighbours
            and weights for edges connecting nodes and neighbours"""
        if istype(graph) is dict:
            self.graph = graph
        else:
            print("Graph of invalid datatype")
            break
        self.infinity = float("inf")

    def init_costs(self, start_node):
        #We only know the costs for the neighbours of the starting node
        #Set all other nodes to infinity
        costs = {}
        for node in self.graph:
            if node == start_node:
                for k, v in node.items():
                    costs[k] = v
            else:
                for k, v in node:
                    costs[k] = self.infinity
        return costs

    def init_parents(self, start_node):
        #Set the parent of neighbours to start node
        parents = {}
        for k, v in self.graph[start_node].items():
            parents[k] = "start"
        return parents

    def find_lowest_cost_node(self, costs, processed_nodes):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost_node and node not in processed_nodes:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def find_shortest_path(self, start_node):
        costs = self.init_costs(start_node)
        parents = self.parents(start_node)
        processed = []
        node = self.find_lowest_cost_node(costs, processed)

        while node is not None:
            cost = costs[node]
            neighbours = self.graph[node]
            for n in neighbours.keys():
                new_cost = cost + neighbours[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = node
            processed.append(node)
            node = find_lowest_cost_node(costs, processed)
        return parents, costs
