def prefix(pattern):
    n = len(pattern) - 1
    return pattern[0:n]

def suffix(pattern):
    n = len(pattern) - 1
    return pattern[-n:]

def overlap_graph(patterns):
    result = {}
    for i,pattern_1 in enumerate(patterns):
        for j,pattern_2 in enumerate(patterns):
            if i != j and suffix(pattern_1) == prefix(pattern_2):
                if pattern_1 not in result:
                    result[pattern_1] = pattern_2
                else:
                    result[pattern_1] = result[pattern_1] +',' +pattern_2
    return result

with open('dataset_198_10.txt','r') as f:
    patterns = []
    for d in f.readlines():
        patterns.append(d.strip('\n'))
r = overlap_graph(patterns)
for key,value in r.items():
    print( key + ' -> '+ value)
