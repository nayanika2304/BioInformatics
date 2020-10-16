genetic_code = {}
with open('RNA_codon_table_1.txt','r') as f:
    for item in f.readlines():
        genetic_code[item.split(" ")[0]] = item.split(" ")[1].strip("\n")

def reverse_complement(text):
    dna = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    swap_text = ''
    for t in text:
        swap_text += dna[t]
    return swap_text[::-1]

def transcribe(text):
    result = text.replace('T','U')
    return result

def reverse_transcribe_rna(rna):
    result = rna.replace('U', 'T')
    return result

def protien_translation(rna):
    protien = ''
    for i in range(0,int(len(rna)/3)):
        pos = i*3
        kmer = rna[pos:pos+3]
        protien += genetic_code[kmer]
    return protien

def peptide_encoding(dna,peptide):
    dna_rc = reverse_complement(dna)
    rna = transcribe(dna)
    rna_rc = transcribe(dna_rc)
    rna_length = len(peptide) * 3
    results = []
    for i in range(len(rna) - rna_length + 1):
        rna_snip = rna[i:i+rna_length]
        if protien_translation(rna_snip) == peptide:
            results.append(reverse_transcribe_rna(rna_snip))
    for i in range(len(rna_rc) - rna_length + 1):
        rna_snip = rna_rc[i:i + rna_length]
        if protien_translation(rna_snip) == peptide:
            results.append(reverse_complement(reverse_transcribe_rna(rna_snip)))
    return results

with open('dataset_96_7.txt','r') as f:
    data = f.readlines()
    input_dna = data[0].strip("\n")
    peptide = data[1].strip("\n")

result = peptide_encoding(input_dna,peptide)
for r in result:
    print(r)

