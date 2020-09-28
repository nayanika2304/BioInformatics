from random import randint

def hamming_distance(p, q):
    """
    Finds the number of mismatches between 2 DNA segments of equal lengths

    p: first DNA segment (str)

    q: second DNA segment (str)

    Returns: number of mismatches (int)
    """
    return sum(s1 != s2 for s1, s2 in zip(p, q))


def find_consensus(motifs):
    """
    Finds a consensus sequence for given list of motifs

    motifs: a list of motif sequences (list)

    Returns: consensus sequence of motifs (str)
    """
    consensus = ""
    for i in range(len(motifs[0])):
        countA, countC, countG, countT = 0,0,0,0 # without psuedocount 0,0,0,0
        for motif in motifs:
            if motif[i] == "A":
                countA += 1
            elif motif[i] == "C":
                countC += 1
            elif motif[i] == "G":
                countG += 1
            elif motif[i] == "T":
                countT += 1
        if countA >= max(countC, countG, countT):
            consensus += "A"
        elif countC >= max(countA, countG, countT):
            consensus += "C"
        elif countG >= max(countC, countA, countT):
            consensus += "G"
        elif countT >= max(countC, countG, countA):
            consensus += "T"
    return consensus

def score(motifs):
    """
    Finds score of motifs relative to the consensus sequence

    motifs: a list of given motifs (list)

    Returns: score of given motifs (int)
    """
    consensus = find_consensus(motifs)
    score = 0.0000
    for motif in motifs:
        score += hamming_distance(consensus, motif)
    return round(score, 4)


def profile_laplace(motifs):
    """
    Finds the profile matrix for given list of motifs

    motifs: list of motif sequences (list)

    Returns: the profile matrix for motifs (list)
    """
    Profile = {}
    A, C, G, T = [], [], [], []
    for j in range(len(motifs[0])):
        countA, countC, countG, countT = 1,1,1,1
        for motif in motifs:
            if motif[j] == "A":
                countA += 1
            elif motif[j] == "C":
                countC += 1
            elif motif[j] == "G":
                countG += 1
            elif motif[j] == "T":
                countT += 1
        A.append(countA)
        C.append(countC)
        G.append(countG)
        T.append(countT)
    Profile["A"] = A
    Profile["C"] = C
    Profile["G"] = G
    Profile["T"] = T
    return Profile


def get_profile_string_most_probable_k_mer(dna, k, profile):
    """
    Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
    (https://stepik.org/lesson/Greedy-Motif-Search-159/step/3?course=Stepic-Interactive-Text-for-Week-3&unit=8217)
    :param dna: a DNA string
    :param profile: a 4 × k matrix Profile
    :return: A Profile-most probable k-mer in Text.
    """
    max_probability = -1
    max_k_mer = None
    for index in range(len(dna) - k + 1):
        k_mer = dna[index: index + k]
        probability = 1
        for pos, base in enumerate(k_mer):
            probability *= profile[base][pos]
        if probability > max_probability:
            max_probability = probability
            max_k_mer = k_mer
    return max_k_mer


def randomized_motif_search_cycle(dna_list, k, t):
    rand_ints = [randint(0, len(dna_list[0]) - k) for i in range(t)]
    motifs = [dna_list[i][r:r + k] for i, r in enumerate(rand_ints)]
    best_motifs = motifs
    best_motifs_score = score(best_motifs)
    while True:
        p = profile_laplace(motifs)
        motifs = [get_profile_string_most_probable_k_mer(dna, k, p) for dna in dna_list]
        print(motifs)
        motifs_score = score(motifs)
        if motifs_score < best_motifs_score:
            best_motifs = motifs
            best_motifs_score = motifs_score
        else:
            return best_motifs_score, best_motifs

def randomized_motif_search(dna_list, k, t):
    best_motifs_score = k*t
    best_motifs = None
    for repeat in range(1000):
        bms, bm = randomized_motif_search_cycle(dna_list, k, t)
        if bms < best_motifs_score:
            best_motifs = bm
            best_motifs_score = bms

    return best_motifs

with open('randomized_motif_finding.txt', "r") as dataset:
    data = []
    for line in dataset:
        data.append(line.strip())
    k = int(data[0].split(" ")[0])
    t = int(data[0].split(" ")[1])
    dna_list = data[1:]
result = randomized_motif_search(dna_list, k, t)
for r in result:
    print(r)
