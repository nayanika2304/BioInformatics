import itertools
from functools import reduce

def get_hamming_distance(dna1, dna2):
    """
    Hamming Distance Problem: Compute the Hamming distance between two strings.
        Input: Two strings of equal length.
    :return: The Hamming distance between these strings.
    """
    if len(dna1) != len(dna2):
        raise Exception("The two DNA strings must have equal length.")

    hamming_distance = 0
    for index in range(len(dna1)):
        if dna1[index] != dna2[index]:
            hamming_distance += 1
    return hamming_distance

def get_minimum_hamming_distance(pattern, dna):
    """
    Hamming Distance Problem: Compute the minimum Hamming distance between a pattern and a DNA string.
        Input: a pattern string and a dna string (which is usually longer than pattern)
    :param pattern: a DNA pattern string
    :param dna: A DNA string, usually longer than the pattern
    :return: The minimum Hamming distance.
    """
    k = len(pattern)
    min_distance = k
    for index in range(len(dna) - k + 1):
        sub_dna = dna[index:index + k]
        distance = get_hamming_distance(pattern, sub_dna)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def find_median_string(dnas, k):
    """
    Median String Problem: Find a median string.
    :param dnas: A collection of strings Dna
    :param k: length of k-mer
    :return: All k-mer Patterns that minimizes d(Pattern, Dna).
    """
    ms = []
    min_d = len(dnas) * k
    for l in itertools.product('ACGT', repeat=k):
        k_mer = ''.join(l)
        d = reduce(lambda a, b: a + b, map(lambda dna: get_minimum_hamming_distance(k_mer, dna), dnas))
        if d < min_d:
            min_d = d
            ms = [k_mer]
        elif d == min_d:
            ms.append(k_mer)
    return ms

k = 7
dna_list = [
    'CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',

    'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',

    'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG'
        ]
print(median_string(k,dna_list))

