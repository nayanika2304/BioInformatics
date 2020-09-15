text = "CCAGATC"

# if A then T or vice versa
# if C then G or vice versa
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

print(reverse_complement(text))
