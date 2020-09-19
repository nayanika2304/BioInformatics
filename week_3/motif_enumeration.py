def hamming_problem(pattern1, pattern2):
    count = 0
    for i, j in zip(pattern1, pattern2):
        if i != j:
            count += 1
    return count


def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    elif len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffix_pattern = pattern[1:]
    first_symbol_pattern = pattern[0]

    suffix_neighbors = neighbors(suffix_pattern, d)
    for text in suffix_neighbors:
        if hamming_problem(suffix_pattern, text) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighborhood.append(nucleotide + text)
        else:
            neighborhood.append(first_symbol_pattern + text)
    return neighborhood


# Write your MotifEnumeration() function here along with any subroutines you need.
# This function should return a list of strings.
def motif_enumeration(dnas, k, d):
    patterns = []
    result = ""
    for dna in dnas:
        for i in range(0, len(dna) - k + 1):
            compute_neighbors = neighbors(dna[i:i + k], d)
            for j in compute_neighbors:
                count = 0
                for l in dnas:
                    print(l)
                    for i in range(0, len(l) - k + 1):
                        if hamming_problem(j, l[i:i + k]) <= d:
                            count += 1
                            break
                if count == len(dnas):
                    patterns.append(j)
    [patterns.append(x) for x in patterns if x not in patterns]
    print(set(patterns))
    for item in set(patterns):
        result = result + " " + str(item)
    return result


dna = [
    'TGCGGCGGGAACGGCGAGACTTGGC',
    'GAATAGTTAACTGGTTTCGGGCGCC',
    'TACGGGGGCCCCATCGGTTCTAAAG',
    'ACTATTTGATAAGATGATCGTACGG',
    'GCTAGTCCGGTTGACCGTACGCGGC',
    'CCCTAAAGCTTCAAATTCGGCGTAC']
k = 5
d = 1

print(motif_enumeration(dna, k, d))

