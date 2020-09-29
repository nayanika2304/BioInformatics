def construct_debrujin_graph_from_edges(edges):
    matches = {}
    for edge in edges:
        parent = edge[:-1]
        child = edge[1:]
        if parent in matches:
            matches[parent].insert(0, child)
        else:
            matches[parent] = [child]
    outputs = [key+" -> "+','.join(matches[key]) for key in list(matches.keys())]
    return outputs

with open('dataset_200_8.txt','r') as f:
    data = []
    for d in f.readlines():
        data.append(d.strip('\n'))

output = construct_debrujin_graph_from_edges(data)
for out in output:
    print(out)
