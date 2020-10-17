'''
et me show you an insanely easy approach [Prerquisites - Implement LinearSpectrum(Peptide)]:

Let's suppose the given peptide is ABCD
It's Circular_Spectrum will consist of mass of these substrings - [0, A, B, C, D, AB, BC, CD, DA, ABC, BCD, CDA, DAB, ABCD]. This is essentially what we need to calculate.
Do this to calculate Circular_Spectrum(Peptide).

Calculate Linear Spectrum for the Prefix of Peptide i.e. ABC which returns the mass of these substrings [0, A, B, C, AB, BC, ABC]
Find the Total_Mass of original peptide i.e. ABCD. You can use LinearSpectrum(Peptide) and return the last element of the spectrum which is equal to Total_Mass.
Now, for each element of LinearSpectrum of ABC, calculate the difference between mass of ABCD (Total_Mass) and each element. This results in mass of these substrings [ABCD , BCD , CDA, DAB, CD, DA, D].
Combine both the PrefixSpectrum and the difference one. Sort it. What you get is  [0, A, B, C, D, AB, BC, CD, DA, ABC, BCD, CDA, DAB, ABCD] which is what you require.

'''
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

peptide = 'NQEL'
total_mass_original_peptide = linear_spectrum(peptide)[-1]

def cyclic_spectrum(peptide):
    total_mass_original_peptide = linear_spectrum(peptide)[-1]
    spectrum = linear_spectrum(peptide[:-1])
    result = []
    for each in spectrum:
        result.append(total_mass_original_peptide-each)
    return sorted(spectrum+result)

with open('dataset_98_4.txt','r') as f:
    peptide = f.readlines()[0].strip("\n")

result = cyclic_spectrum(peptide)
print(str(result).lstrip("[").rstrip("]").replace(","," "))
