'''
Input: A string Text and an integer k.
Output: All most frequent k-mers in Text.
'''

text="TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
k = 3


def frequency_map(text, k):
    freq = {}

    n = len(text)

    for i in range(n - k + 1):

        pattern = text[i:i + k]

        if pattern in freq:

            freq[pattern] += 1

        else:

            freq[pattern] = 1

    return freq


print(frequency_map(text, k))


def frequent_kmers(text, k):
    kmers = []

    freq = frequency_map(text, k)

    m = max(freq.values())

    for most_frequent_kmer in freq:

        if freq[most_frequent_kmer] == m:
            kmers.append(most_frequent_kmer)

    return kmers


print("most frequent 3-mer is")

print(frequent_kmers(text, k))

