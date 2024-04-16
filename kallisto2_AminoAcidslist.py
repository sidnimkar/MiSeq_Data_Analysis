import numpy as np

# Sequenc to be modified
target_seq = ('ATTACTGTAAATGAAAAAGAACACATTCTTGAACAGAAATATCGTCCATCTACTATCGATGAATGTATTCTTCCCGCCTTTGATAAAGAAACCTTTAAATCTATTACAAGTAAAGGTAAGATTCCACATATTATTCTTCATTCTCCTTCTCCAGGAACAGGTAAAACAACTGTAGCAAAAGCATTATGTCATGATGTAAATGCTGATATGATGTTTGTGAATGGGTCAGATTGTAAAATTGATTTCGTTCGTGGTCCTTTGACTAATTTTGCCAGCGCCGCTTCATTTGATGGTCGTCAAAAAGTAATCGTTATTGATGAATTTGACCGTTCAGGGTTAGCAGAGTCTAACCGACATCTTCGTTCCTTTATG')

# Codon to single-letter amino acid mapping
codon_to_aa = {
    'AAG': 'K', 'CGC': 'R', 'CGG': 'R', 'AGG': 'R',
    'GAG': 'E', 'GAC': 'D', 'AAC': 'N', 'CAG': 'Q',
    'CAC': 'H', 'ACC': 'T', 'ACG': 'T', 'AGC': 'S',
    'TCC': 'S', 'TCG': 'S', 'TGC': 'C', 'GCC': 'A',
    'GCG': 'A', 'GTC': 'V', 'GTG': 'V', 'CTC': 'L',
    'CTG': 'L', 'TTG': 'L', 'ATC': 'I', 'ATG': 'M',
    'TTC': 'F', 'TAC': 'Y', 'TGG': 'W', 'GGC': 'G',
    'GGG': 'G', 'CCC': 'P', 'CCG': 'P', 'TAG': '*'
}

# List of codons to be used for replacements
cod = list(codon_to_aa.keys())

# Write to file
with open('NNSAminoAcids.txt', 'w') as fid:
    serial_number = 1  # Initialize serial number
    for i in range(0, len(target_seq), 3):
        tmp = list(target_seq)
        for j in range(32):
            original_codon = target_seq[i:i+3]  # Get the original codon
            tmp[i:i+3] = list(cod[j])
            aa = codon_to_aa[cod[j]]  # Get the single-letter amino acid code
            # Write the header with serial number and amino acid code, and the modified sequence
            fid.write(aa+ '\n') 
            serial_number += 1  # Increment the serial number
        print(i)