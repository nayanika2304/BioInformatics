from collections import defaultdict
from functools import reduce
from itertools import combinations, product

def kmer_mismatches(kmer, d):
    """Returns all k-mers that are within d mismatches of the given k-mer."""
    mismatches = [kmer]  # Initialize mismatches with the k-mer itself (i.e. d=0).
    alt_bases = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
    for dist in range(1, d+1):
        for change_indices in combinations(range(len(kmer)), dist):
            for substitutions in product(*[alt_bases[kmer[i]] for i in change_indices]):
                new_mistmatch = list(kmer)
                for idx, sub in zip(change_indices, substitutions):
                    new_mistmatch[idx] = sub
                mismatches.append(''.join(new_mistmatch))
    return mismatches

def motif_enumeration(k, d, dna_list):
    '''Returns all (k, d)-motifs that are shared by all sequences in dna_list.'''

    # Generate sets of (k,d)-motifs for each dna sequence in the list.
    motif_sets = [{kmer for i in range(0,len(dna)-k+1) for kmer in kmer_mismatches(dna[i:i+k], d)} for dna in dna_list]

    # Intersect all sets to get the common elements.  The answers are displayed as sorted, so we'll sort too.
    return sorted(list(reduce(lambda a,b: a & b, motif_sets)))


dna = [
    'ATTTGGC',
    'TGCCTTA',
    'CGGTATC',
    'GAAAATT']
k = 3
d = 1

print(motif_enumeration(k, d,dna))

