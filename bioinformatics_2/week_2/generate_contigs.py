def generate_contigs(kmers):
    # generate dictionary, {begin_node, [begin_node_occurrence, [end_node_1, contig_1], ...]}
    graph_dict = {}
    k = len(kmers[0])
    for kmer in kmers:
        source = kmer[:-1]
        target = kmer[1:]
        if source in graph_dict:
            graph_dict[source].append([target, kmer])
        else:
            graph_dict[source] = [0, [target, kmer]]
        if target in graph_dict:
            graph_dict[target][0] += 1
        else:
            graph_dict[target] = [1]

    # generate contigs
    terminate = False
    while not terminate:
        terminate = True
        for key, values in graph_dict.items():
            for i, value in enumerate(values[1:]):
                if value[0] not in graph_dict:
                    continue
                target = graph_dict[value[0]]
                occurrence = target[0]
                if occurrence == 0:
                    continue
                if occurrence == 1 and len(target)==2: # non-branching condition
                    # merge
                    values.pop(i+1)
                    for j, target_value in enumerate(target[1:]):
                        values.append([target_value[0], value[1]+target_value[1][k-1:]])
                        target.pop(1)
                    terminate = False
                    break
            if not terminate:
                break

    # return contigs
    contigs = []
    for key in graph_dict.keys():
        values = graph_dict[key][1:]
        for value in values:
            contigs.append(value[1])
    contigs.sort()
    return contigs

kmers = []
with open('dataset_205_5.txt','r') as f:
    for item in f.readlines():
        kmers.append(item.strip('\n'))
result = generate_contigs(kmers)
print(str(result).lstrip('[').rstrip(']').replace("'","").replace(",",""))
