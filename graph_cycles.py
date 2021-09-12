from timeit import default_timer as timer
import networkx as nx

'''
Notes:
After testing with several sample graphs, the networkX example is reatively faster than
the native implementation. The native implementation uses recurssion and this slows it down
Since the loop breaks upon the detection of a cycle, the best case scenario is if the cycle occurs
at the beginning of the graph dictionary.

In the event the graph is very large and a cycle exists at the very beginning, the native implementation would be faster since the loops breaks as soon as there is a cycle detected

The networkx implementation returns all cycles found meaning it traverses the whole graph. A better alternative if one wants to know what the cycles are.


'''
# networkx Implementation


def networkx_implementation():
    edges = [("A", "B"), ("B", "C"), ("C", "E"), ("E", "D"), ("E", "F")]
    G = nx.DiGraph(edges)
    if len(list(nx.simple_cycles(G))) > 0:
        return True
    else:
        return False


# native implementation
def native_implementation():
    graph = {"A": ["B"], "B": ["C"], "C": ["E"], "D": ["B"], "E": ["F", "D"], "F": []}

    traversal_path = []

    def visit(vertex):
        traversal_path.append(vertex)  # start traversal
        for neighbour in graph.get(vertex, ()):  # traverse neighbours
            if neighbour in traversal_path or visit(
                neighbour
            ):  # recursion- traverse neighbours of neighbours
                return True  # cycle found
        traversal_path.remove(vertex)
        return False  # have checked everything, no cycles

    return any(visit(v) for v in graph)  # as long as there is a cycle


# timing
start = timer()
networkx_implementation()
end = timer()
print(f" Network x implementation {end - start} seconds")

start = timer()
native_implementation()
end = timer()
print(f" Native implementation {end - start} seconds")

