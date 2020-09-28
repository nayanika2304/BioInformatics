with open("dataset_5164_1.txt") as inp:
    input_items = inp.read().strip().splitlines()
    pattern = input_items[0].strip()
    dna_sequences = input_items[1].strip().split()


def hamming_problem(pattern1, pattern2):
    count = 0
    for i, j in zip(pattern1, pattern2):
        if i != j:
            count += 1
    return count


def window(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i + k]


def distance(pattern, dna):
    k = len(pattern)
    distance = 0
    for d in dna:
        hamming_distance = float('inf')
        for i in range(0,len(d)-k +1):
            if hamming_distance > hamming_problem(pattern,d[i:i+k]):
                hamming_distance = hamming_problem(pattern,d[i:i+k])
        distance += hamming_distance
    return distance


print(distance(pattern, dna_sequences))
