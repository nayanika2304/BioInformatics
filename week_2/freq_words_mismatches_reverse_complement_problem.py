import itertools
import time
from collections import defaultdict


with open("Salmonella_enterica.txt",'r') as f:
    text = f.read()

k = 9
d = 1

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

frequencies = FrequentWordsWithMismatches(text[3818639:],k,d)
print(PrintFreqArrayWithReverseComplement(frequencies))

'''
    def frequent_words_with_missmatches_by_sorting(text, k, d):
    frequent_patterns = set()
    neighborhoods = [neighbors(text[i:i+k], d) for i in range(len(text) - k + 1)]
    neighborhood_array = [strings for neighborhood in neighborhoods for strings in neighborhood]
    index = [pattern_to_number(neighborhood_array[i]) for i in range(len(neighborhood_array))]
    count = [1] * len(index)
    sorted_index = sorted(index)
    for i in range(len(neighborhood_array) - 1):
        if sorted_index[i] == sorted_index[i + 1]:
            count[i + 1] = count[i] + 1
    max_count = max(count)
    for i in range(len(neighborhood_array)):
        if count[i] == max_count:
            pattern = number_to_pattern(sorted_index[i], k)
            frequent_patterns.add(pattern)
    return frequent_patterns
'''
