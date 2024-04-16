import numpy as np

# Initialize variables
fwd_index = ''
rev_index = ''
target_seq = ('ATTACTGTAAATGAAAAAGAACACATTCTTGAACAGAAATATCGTCCATCTACTATCGATGAATGTATTCTTCCCGCTTTTGATAAAGAAACCTTTAAATCTATTACAAGTAAAGGTAAGATTCCACATATTATTCTTCATTCTCCTTCTCCAGGAACAGGTAAAACAACTGTAGCAAAAGCATTATGTCATGATGTAAATGCTGATATGATGTTTGTGAATGGGTCAGATTGTAAAATTGATTTCGTTCGTGGTCCTTTGACTAATTTTGCCAGCGCCGCTTCATTTGATGGTCGTCAAAAAGTAATCGTTATTGATGAATTTGACCGTTCAGGGTTAGCAGAGTCTCAGCGACATCTTCGTTCCTTTATG')
counts = np.zeros((32, len(target_seq) // 3))
cod = ['AAG', 'CGC', 'CGG', 'AGG', 'GAG', 'GAC', 'AAC', 'CAG', 'CAC', 'ACC', 'ACG', 'AGC', 'TCC', 'TCG', 'TGC', 'GCC', 'GCG', 'GTC', 'GTG', 'CTC', 'CTG', 'TTG', 'ATC', 'ATG', 'TTC', 'TAC', 'TGG', 'GGC', 'GGG', 'CCC', 'CCG', 'TAG']

# Write to file
with open('Pool1.fasta', 'w') as fid:
    serial_number = 1  # Initialize serial number
    for i in range(0, len(target_seq), 3):
        tmp = list(target_seq)
        for j in range(32):
            tmp[i:i+3] = list(cod[j])
            # Write the header with serial number and the modified sequence
            fid.write('>{}\n'.format(serial_number) + ''.join(tmp) + '\n')
            serial_number += 1  # Increment the serial number
        print(i)