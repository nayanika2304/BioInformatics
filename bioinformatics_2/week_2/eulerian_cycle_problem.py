class Link:
    "A link in a linked list."
    def __init__(self, node):
        self.node = node
        self.next = None #changed this from self

    #Simple method for debugging
    def __str__(self):
        cur = self
        string = "Link : "
        while True:
            string += str(cur.node) + " > "
            cur = cur.next
            if cur == None:
                break
        return string + "..."

    def insert(self, link):
        "Insert link after self in the linked list and return link."
        link.next = self.next
        self.next = link
        return link

def eulerian_cycle_2(graph):
    """Return an Eulerian cycle in graph, if there is one, as a list of
    nodes. If there are no Eulerian cycles, raise ValueError.

    """
    # # Take a copy of the graph so that we can modify it.
    graph = {k:v[:] for k, v in graph.items()}
    # # Start at any node in the graph that has an edge.
    node = next(node for node, neighbours in graph.items() if neighbours)
    choices = graph[node]
    cur = Link(node)
    begin = cur #new

    # Map from node we've visited (that still has edges) to a link for
    # that node in the linked list.
    visited = {}
    while True:
        # Extend current cycle until no more edges can be followed.
        start = node
        while choices:
            visited[node] = cur
            node = choices.pop()
            choices = graph[node]
            cur = cur.insert(Link(node))

        if node != start:
            raise ValueError("graph has no Eulerian cycle")

        # Find a visited node which still has edges, if any.
        while visited:
            node, cur = visited.popitem()
            choices = graph[node]
            if choices:
                break
        else:
            break

    if any(graph.values()):
        raise ValueError("graph has no Eulerian cycle")

    # Reconstruct cycle by following linked list.
    cycle = []
    cur = begin #new
    while True:
        cycle.append(cur.node)
        cur = cur.next
        if cur == None: #changed from cur == start
            break
    return cycle

with open('dataset_203_2.txt', 'r') as file:
    graph = dict((line.strip().split(' -> ') for line in file))
    for key in graph:
        graph[key] = graph[key].split(',')

cycle = eulerian_cycle_2(graph)
result = '->'.join(cycle)
print(result)

