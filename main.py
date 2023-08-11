from typing import Any


class Node:
    """Contains the given value, references to connected nodes, as well as the respective weights of connections"""
    def __init__(self, value):
        """Create a node with a given value"""
        self._value = value
        # (node, weight)
        self._connections = []
    
    def connect(self, node: "Node", weight: int):
        """Make a connection between this node and another"""
        self._connections.append((node, weight))

    @property
    def connections(self) -> list[tuple["Node", int]]:
        """Return the list of connections"""
        return self._connections

    @property
    def value(self) -> Any:
        """Return the stored value of the node"""
        return self._value


def connect_nodes(node1: Node, node2: Node, weight: int):
    """Register connection with both nodes"""
    node1.connect(node2, weight)
    node2.connect(node1, weight)


# CREATE GRAPH
# Kept in dictionary with letters for ease of creating the graph
nodes = {}
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for l in letters:
    nodes[l] = Node(l)
# First graph
connections1 = [("A", "B", 50),
                ("A", "C", 25),
                ("B", "D", 25),
                ("B", "I", 80),
                ("C", "E", 45),
                ("C", "F", 50),
                ("D", "I", 70),
                ("D", "F", 10),
                ("E", "H", 35),
                ("E", "G", 30),
                ("F", "H", 25),
                ("G", "J", 80),
                ("I", "J", 30)]
# Second graph
connections2 = [("A", "B", 75),
                ("A", "C", 10),
                ("B", "D", 5),
                ("C", "E", 55),
                ("C", "F", 30),
                ("D", "I", 10),
                ("D", "F", 45),
                ("D", "G", 45),
                ("E", "J", 30),
                ("F", "G", 40),
                ("G", "H", 35),
                ("H", "J", 15),
                ("I", "J", 65)]
# Third graph
connections3 = [("A", "B", 100),
                ("A", "C", 40),
                ("B", "D", 35),
                ("C", "E", 55),
                ("C", "F", 30),
                ("D", "I", 45),
                ("D", "F", 30),
                ("D", "G", 10),
                ("E", "H", 20),
                ("G", "J", 15),
                ("H", "J", 65),
                ("I", "J", 12)]
connections = connections3
for c in connections:
    a, b, w = c
    n1 = nodes[a]
    n2 = nodes[b]
    connect_nodes(n1, n2, w)

'''
#CHECK GRAPH
def show_connected_nodes(letter : str):
    global nodes
    print(f"{letter} connected to:")
    connected_nodes = list(nodes[letter].get_connections())
    for n in connected_nodes:
        print(n.get_value())
show_connected_nodes("F")
print()
show_connected_nodes("J")
print()
show_connected_nodes("C")'''


# Only need the nodes now (letters are contained within the nodes anyway)
def get_shortest_path(start: Node, end: Node):
    current = start
               # node:(distance from start, previous node, visited?)
    distances = {start: (0, start, False)}
    while current != end:
        cur_cons = current.connections
        # Current best distance from start to current node
        cur_dist = distances[current][0]
        for con in cur_cons:
            n, w = con
            # What would be the new distance if going through this node?
            new_dist = cur_dist + w
            if n not in distances.keys():
                # Node not been visited
                distances[n] = (new_dist, current, False)
                continue
            # Current best distance from start to target node
            tar_dist = distances[n][0]
            if tar_dist > new_dist:
                distances[n] = (new_dist, current, False)
        # Mark current node as visited
        temp = distances[current]
        distances[current] = (temp[0], temp[1], True)
        # Find the next closest unvisited node to start node
        current = None
        for n in distances.keys():
            # If the node has been visited, move on to the next
            if distances[n][2] == True:
                continue
            # Check if the node is closer to start than current node
            if current is None or distances[n][0] < distances[current][0]:
                current = n
    
    # FIND SHORTEST PATH
    dist = distances[end][0]
    path = []
    cur = end
    while cur != start:
        path.append(cur.value)
        cur = distances[cur][1]
    path.append(start.value)
    path.reverse()
    print("Path:\t", " -> ".join(path))
    print("Distance:\t", dist)


# Only need list of nodes
nodes = list(nodes.values())
get_shortest_path(nodes[0], nodes[-1])
