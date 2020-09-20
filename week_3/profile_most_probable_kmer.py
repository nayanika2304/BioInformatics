
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
