# Ways of building a graph
# Edge list
# In the list we have the way edges are linked
# graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent list
# Similar way is with adjacent list, but the only difference is that the edges are indexes and the values are edges neighbours
# graph = [[2], [2,3], [0, 1, 3], [1, 2]]

# Adjacent matrix
# ex: index of 0, has connection 2, index of 1 with 2 and 3, index of 2 with 0, 1, 2
# graph = [
# [0, 0, 1, 0],                 ex: 0 <-> 2
# [0, 0, 1, 1],                 ex: 1 <-> 2, 1 <-> 3
# [1, 1, 0, 1],                 ex: 2 <-> 0, 2 <-> 1, 2 <-> 3
# [0, 1, 1, 0],                 ex: 3 <-> 1, 3 <-> 2
# ]

# * can be used as an object (or in python case dict)

# graph = {
# 0: [0, 0, 1, 0],
# 1: [0, 0, 1, 1],
# 2: [1, 1, 0, 1],
# 3: [0, 1, 1, 0],
# }

# now for an actual code example:
class Graph:
    def __init__(self):
        self.num_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.num_of_nodes += 1

    def add_edge(self, node1, node2):
        # undirected graph
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show(self):
        for node in self.adjacent_list:
            connections = " ".join(self.adjacent_list[node])
            print(f"{node} --> {connections}")


if __name__ == '__main__':
    myGraph = Graph()
    myGraph.add_vertex('0')
    myGraph.add_vertex('1')
    myGraph.add_vertex('2')
    myGraph.add_vertex('3')
    myGraph.add_vertex('4')
    myGraph.add_vertex('5')
    myGraph.add_vertex('6')

    myGraph.add_edge('3', '1')
    myGraph.add_edge('3', '4')
    myGraph.add_edge('4', '2')
    myGraph.add_edge('4', '5')
    myGraph.add_edge('1', '2')
    myGraph.add_edge('1', '0')
    myGraph.add_edge('0', '2')
    myGraph.add_edge('6', '5')

    myGraph.show()
