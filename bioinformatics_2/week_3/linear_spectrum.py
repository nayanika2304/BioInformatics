def _get_peptide_mass(amino_acid_mass_table, peptide):
    mass = 0
    for pos in range(len(peptide)):
        mass += amino_acid_mass_table[peptide[pos]]
    return mass


def _get_amino_acid_mass_table():
    with open('integer_mass_table.txt') as datafile:
        lines = [line.strip().split(' ') for line in datafile.readlines()]
    aas, masses = zip(*lines)
    masses = [int(mass) for mass in masses]
    return dict(zip(aas, masses))

def linear_spectrum(peptide):
    amino_acid_mass_table = _get_amino_acid_mass_table()
    sub_peptides = [['',0]]
    for l in range(len(peptide))[1:]:
        for pos in range(len(peptide)):
            if pos + l <= len(peptide):
                sub_peptide = peptide[pos:pos+l]
                sub_peptides.append([sub_peptide,0])
    if (peptide):
        sub_peptides.append([peptide,0])
    for entry in sub_peptides:
        entry[1] = _get_peptide_mass(amino_acid_mass_table, entry[0])
    sub_peptides = [sub[1] for sub in sub_peptides]
    return sorted(sub_peptides)


with open('dataset_98_4.txt','r') as f:
    peptide = f.readlines()[0].strip("\n")

result = linear_spectrum(peptide)
print(str(result).lstrip("[").rstrip("]").replace(","," "))
