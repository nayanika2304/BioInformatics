import itertools
import time
from collections import defaultdict

text = "CCATACGCGCTCCGCGCGCTATATATACATCCCCGCTACGCTCCACCCCCGCTCCATCCCCGCATATACCCGCTGCCCGCTGCGCGCTCCGCATCCACGCTACCCGCTACACATCCGCACACATATCCGCGCACGCTGCACGCACATCCGCACATACGCTACACCCATGCTATACACGCTGCTATCCATATACACGCTATGCGC"
k = 5
d = 3

dna = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}


def reverse_complement(text):
    swap_text = ''
    for t in text:
        swap_text += dna[t]
    return swap_text[::-1]


def FrequentWordsWithMismatches(Genome, k, d):
    start = time.process_time()
    aprox_frq_words = []
    frequencies = defaultdict(lambda: 0)

    # all existent kmers with d mismatches of current kmer in genome


    for index in range(len(Genome) - k + 1):
        curr_kmer_and_neighbors = PermuteMotifDistanceTimes(Genome[index: index + k], d)
        for kmer in curr_kmer_and_neighbors:
            frequencies[kmer] += 1

    for kmer in frequencies:
        if frequencies[kmer] >= max((frequencies.values())):
            aprox_frq_words.append(kmer)
    end = time.process_time()
    print("Time:", end - start)
    return frequencies


def PermuteMotifOnce(motif, alphabet={"A", "C", "G", "T"}):
    """
    Gets all strings within hamming distance 1 of motif and returns it as a
    list.
    """

    return list(set(itertools.chain.from_iterable([[
        motif[:pos] + nucleotide + motif[pos + 1:] for
        nucleotide in alphabet] for
        pos in range(len(motif))])))


def PermuteMotifDistanceTimes(motif, d):
    workingSet = {motif}
    for _ in range(d):
        workingSet = set(itertools.chain.from_iterable(map(PermuteMotifOnce, workingSet)))
    return list(workingSet)


def reverse_complement(text):
    swap_text = ''
    for t in text:
        swap_text += dna[t]
    return swap_text[::-1]

def PrintFreqArrayWithReverseComplement(frequencies):
    total = {}
    result = []
    for kmer in frequencies:
        reverse = reverse_complement(kmer)
        if reverse in frequencies:
            total[kmer] = frequencies[kmer] + frequencies[reverse]

    for kmer in total:
        if total[kmer] >= max(total.values()):
            result.append(kmer)
    return str(result).lstrip("[").rstrip("]").replace(",","")

frequencies = FrequentWordsWithMismatches(text,k,d)
print(PrintFreqArrayWithReverseComplement(frequencies))
