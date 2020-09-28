
filename = 'dataset_159_3.txt'
with open(filename, "r") as dataset:
    data = []
    for line in dataset:
        data.append(line.strip())
    text = data[0]
    k = int(data[1])
    raw_profile = data[2:]
    bases = ['A', 'C', 'G', 'T']
    prof = [list(map(float, raw_profile[i].split())) for i in range(len(raw_profile))]
    prof_dict = dict(zip(bases, prof))


def compute_probability(kmer,profile_mat):
    prob=1
    for i in range(0,len(kmer)):
        if kmer[i]=='A':
            prob=prob*profile_mat['A'][i]
        if kmer[i]=='C':
            prob=prob*profile_mat['C'][i]
        if kmer[i]=='G':
            prob=prob*profile_mat['G'][i]
        if kmer[i]=='T':
            prob=prob*profile_mat['T'][i]
    return prob

def profile(dna_seq,k,profile_matrix):
    max_probab=0
    for i in range(len(dna_seq)-k+1):
        kmer=dna_seq[i:i+k]
        pro=compute_probability(kmer,profile_matrix)
        if pro>max_probab:
            max_probab=pro
            sol=kmer
    return sol

print(profile(text,k,prof_dict))
'''
def profile_most_probable_kmer(dna, k, profile):
    Returns the profile most probable k-mer for the given input data.

    # A dictionary relating nucleotides to their position within the profile.
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}

    # Initialize the maximum probabily.
    max_probability = -1
    most_probable = ''
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
'''
