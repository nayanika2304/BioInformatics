pattern = "CGC"
genome = "ATGACTTCGCTGTTACGCGC"

def pattern_matching(pattern, genome):
    n = len(genome)
    k = len(pattern)
    result = []
    for i in range(n-k+1):
        test = genome[i:i+k]
        if test == pattern:
            result.append(i)
    print(result)

pattern_matching(pattern, genome)
