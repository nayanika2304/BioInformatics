import numpy as np


def entropy(prop):
    return np.sum([-x * np.log2(x) for x in prop if x > 0])


def motif_entropy(motifs, dna=True):
    n = len(motifs[0])
    result = 0
    for i in range(n):
        nucleotides = "ATGC"
        freq = {k: 0 for k in nucleotides}
        for motif in motifs:
            freq[motif[i]] += 1
        tot = sum(list(freq.values()))
        result += entropy([v / tot for v in freq.values()])
    return result


Motifs = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC"
]
print(motif_entropy(Motifs))
