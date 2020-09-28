def genome_path_problem(patterns):
    return patterns[0] + ''.join([pattern[-1] for pattern in patterns[1:]])

with open('dataset_198_3.txt','r') as f:
    data = []
    for d in f.readlines():
        data.append(d.strip('\n'))
print(genome_path_problem(data))
