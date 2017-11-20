#Breadth-first search algorithms are used for finding if a path exists, and the shortest
#possible path in an unweighted graph. The function below is an implementation
#of breadth-first search in python
import collections

def search(start_point, query_function, graph):
    """Params:
        start_point: starting node, must be an existing key in graph
        query_function: function to pass search queries, must return boolean value
        graph: graph to search. Expects hash table datatype"""
    queue = collections.deque()
    queue += graph[start_point]
    searched = []

    while queue:
        query = queue.popleft()
        if not query in searched:
            if query_function(query):
                print("Matching node found!")
                return {"query_node": query, "path": searched}
        else:
            queue += graph[query]
            searched.append(query)
    return False
