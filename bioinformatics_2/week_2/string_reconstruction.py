from random import sample

def find_cycle(graph, start_node):
    # Find cycle in the graph starting with start_node
    cycle = [start_node]
    node = start_node
    while True:
        sinks = graph[node]
        next_node = sample(sinks, 1)[0]
        if len(sinks) > 1:
            graph[node] = sinks - {next_node}
        else:
            del(graph[node])
        cycle.append(next_node)
        node = next_node
        if node == start_node:
            break

    return cycle, graph

def node_degrees(graph):
    # Calculate indegree and outdegree of all the nodes in the graph
    in_degree = {}
    out_degree = {}

    for source in graph:
        if source not in in_degree:
            in_degree[source] = 0
        out_degree[source] = len(graph[source])
        for sink in graph[source]:
            if sink in in_degree:
                in_degree[sink] += 1
            else:
                in_degree[sink] = 1
            if sink not in out_degree:
                out_degree[sink] = 0
    return in_degree, out_degree

def find_endpoints(graph):
    in_degree, out_degree = node_degrees(graph)
    start_node, end_node = -1, -1

    for node in in_degree:
        ins, outs = in_degree[node], out_degree[node]
        # The start node must be that node which has an outdegree that is one greater than its indegree
        if outs == ins + 1:
            if start_node == -1:
                start_node = node
        # The end node must be that node which has an indegree that is one greater than its outdegree
        elif ins == outs + 1:
            if end_node == -1:
                end_node = node

    return start_node, end_node

def combine_cycles(cycle, index, new_cycle):
    cycle = cycle[:index] + new_cycle + cycle[index + 1:]
    return cycle

def find_eulerian_path(graph):
    start_node, end_node = find_endpoints(graph)
    if end_node in graph:
        graph[end_node].add(start_node)
    else:
        graph[end_node] = {start_node}
    cycle, graph = find_cycle(graph, start_node)
    while graph:
        for i, start_node in enumerate(cycle):
            if start_node in graph:
                new_cycle, graph = find_cycle(graph, start_node)
                cycle = combine_cycles(cycle, i, new_cycle)
                break
    return cycle[:-1]

def construct_debrujin_graph_from_edges(edges):
    graph_dict = {}
    for kmer in edges:
        source = kmer[:-1]
        target = kmer[1:]
        if source in graph_dict:
            graph_dict[source].append(target)
        else:
            graph_dict[source] = [target]
    return graph_dict

def genome_path_problem(patterns):
    return patterns[0] + ''.join([pattern[-1] for pattern in patterns[1:]])

def string_reconstruction(k, kmers):
    graph_dict = construct_debrujin_graph_from_edges(kmers)
    graph = {}
    for source,targets in graph_dict.items():
        graph[source] = set(targets)
    path = find_eulerian_path(graph)
    return genome_path_problem(path)

with open('dataset_203_7.txt','r') as f:
    data = []
    for d in f.readlines():
        data.append(d.strip('\n'))
    k = data[0]
    patterns = data[1:]
result = string_reconstruction(k,patterns)
print(result)
