import numpy as np

# Initialize variables
fwd_anchor = ''
rev_anchor = ''
target_seq = ('CTAAAACTTGAATGAGGAAATTATGATTACTGTAAATGAAAAAGAACACATTCTTGAACAGAAATATCGTCCATCTACTATCGATGAATGTATTCTTCCCGCCTTTGATAAAGAAACCTTTAAATCTATTACAAGTAAAGGTAAGATTCCACATATTATTCTTCATTCTCCTTCTCCAGGAACAGGTAAAACAACTGTAGCAAAAGCATTATGTCATGATGTAAATGCTGATATGATGTTTGTGAATGGGTCAGATTGTAAAATTGATTTCGTTCGTGGTCCTTTGACTAATTTTGCCAGCGCCGCTTCATTTGATGGTCGTCAAAAAGTAATCGTTATTGATGAATTTGACCGTTCAGGGTTAGCAGAGTCTAATCGACATCTTCGTTCCTTTATGGAAGCTTATAGTTCAAACTGTAG')
counts = np.zeros((32, len(target_seq) // 3), dtype=int)
cod = ['AAG', 'CGC', 'CGG', 'AGG', 'GAG', 'GAC', 'AAC', 'CAG', 'CAC', 'ACC', 'ACG', 'AGC', 'TCC', 'TCG', 'TGC', 'GCC', 'GCG', 'GTC', 'GTG', 'CTC', 'CTG', 'TTG', 'ATC', 'ATG', 'TTC', 'TAC', 'TGG', 'GGC', 'GGG', 'CCC', 'CCG', 'TAG']

# Open the file for writing
with open('C:\\Users\\sidni\\Documents\\Pool1inp1.sh', 'w') as fid:
    for i in range(0, len(target_seq), 3):
        for j in range(len(cod)):
            # Create a temporary list of characters from the target sequence
            tmp = list(target_seq)
            # Replace the codon at the current position
            tmp[i:i+3] = cod[j]
            # Convert the list back to a string and write to the file
            fid.write(f"grep -c {fwd_anchor + ''.join(tmp)} P1inp1.fastq >> Pool1inptestcounts1.txt\n")
        # Print the current index to the console
        print(i)