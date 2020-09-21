

from itertools import product

def hamming_problem(pattern1, pattern2):
    count = 0
    for i, j in zip(pattern1, pattern2):
        if i != j:
            count += 1
    return count

def median_string(k, dna_list):
    # Initialize the best pattern score as one greater than the maximum possible score.
    best_score = k*len(dna_list) + 1

    # Check the scores of all k-mers.
    for pattern in product('ACGT', repeat=k):
        current_score = sum([motif_score(''.join(pattern), dna) for dna in dna_list])
        if current_score < best_score:
            best_score = current_score
            best_pattern = ''.join(pattern)

    return best_pattern


def motif_score(pattern, motif):
    '''Returns the score of d(pattern, motif).'''
    return min([hamming_problem(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])

k = 3
dnas = ['AAATTGACGCAT',
        'GACGACCACGTT',
        'CGTCAGCGCCTG',
        'GCTGAGCACCGG',
        'AGTTCGGGACAG'
        ]
print(median_string(k,dnas))

