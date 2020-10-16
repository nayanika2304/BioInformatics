

def protien_translation(rna, genetic_code):
    protien = ''
    for i in range(0,int(len(rna)/3)):
        pos = i*3
        kmer = rna[pos:pos+3]
        protien += genetic_code[kmer]
    return protien

genetic_code = {}
with open('RNA_codon_table_1.txt','r') as f:
    for item in f.readlines():
        genetic_code[item.split(" ")[0]] = item.split(" ")[1].strip("\n")
with open('dataset_96_4.txt','r') as f:
    rna = f.readlines()[0].strip("\n")

result = protien_translation(rna,genetic_code)
print(result)
