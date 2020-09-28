from random import randint

def score(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count


def profile_laplace(motifs):
    '''Returns the profile of the dna list motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc) + 1) / float(len(col) + 4) for nuc in 'ACGT'] for col in columns]

def profile_most_probable_kmer(dna, k, profile):
    '''Returns the profile most probable k-mer for the given input data.'''
    # A dictionary relating nucleotides to their position within the profile.
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}

    # Initialize the maximum probabily.
    max_probability = -1

    # Compute the probability of the each k-mer, store it if it's currently a maximum.
    for i in range(len(dna)-k+1):
        # Get the current probability.
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]

        # Check for a maximum.
        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable

def _gibbs_sampler_cycle(dna_list, k, t, N):
    dna_length = len(dna_list[0])
    random_integers = [randint(0, dna_length-k) for i in range(t)]
    motifs = [dna_list[i][r:r+k] for i,r in enumerate(random_integers)]
    best_motifs = list(motifs)
    best_motifs_score = score(best_motifs)
    for j in range(N):
        i = randint(0, t-1)
        profile = profile_laplace([motif for index,motif in enumerate(motifs) if index != i])
        motifs[i] = profile_most_probable_kmer(dna_list[i], k, profile)
        motifs_score = score(motifs)
        if motifs_score < best_motifs_score:
            best_motifs_score = motifs_score
            best_motifs = motifs
    return best_motifs_score, best_motifs

def gibbs_sampler(dna_list, k, t, N):
    best_motifs_score = k*t
    best_motifs = None
    for repeat in range(20):
        bms, bm = _gibbs_sampler_cycle(dna_list, k, t, N)
        if bms < best_motifs_score:
            best_motifs = bm
            best_motifs_score = bms

    return best_motifs

# dna_list = ['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA',
#             'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
#             'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
#             'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
#             'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
# k = 8
# t = 5
# N = 100
#
# print(gibbs_sampler(
#     dna_list,k,t,N
# ))

with open('gibbs_sampler.txt', "r") as dataset:
    data = []
    for line in dataset:
        data.append(line.strip())
    k = int(data[0].split(" ")[0])
    t = int(data[0].split(" ")[1])
    N = int(data[0].split(" ")[2])
    dna_list = data[1:]
result = gibbs_sampler(dna_list, k, t,N)
for r in result:
    print(r)
