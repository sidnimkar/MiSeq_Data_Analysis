# generate shell script to count codon variants of given sequence
fwd_anchor = ''
rev_anchor = ''
target_seq = 'ATTACTGTAAATGAAAAAGAACACATTCTTGAACAGAAATATCGTCCATCTACTATCGATGAATGTATTCTTCCCGCTTTTGATAAAGAAACCTTTAAATCTATTACAAGTAAAGGTAAGATTCCACATATTATTCTTCATTCTCCTTCTCCAGGAACAGGTAAAACAACTGTAGCAAAAGCATTATGTCATGATGTAAATGCTGATATGATGTTTGTGAATGGGTCAGATTGTAAAATTGATTTCGTTCGTGGTCCTTTGACTAATTTTGCCAGCGCCGCTTCATTTGATGGTCGTCAAAAAGTAATCGTTATTGATGAATTTGACCGTTCAGGGTTAGCAGAGTCTCAGCGACATCTTCGTTCCTTT'
counts = [[0 for _ in range(len(target_seq) // 3)] for _ in range(32)]
cod = ['AAG', 'CGC', 'CGG', 'AGG', 'GAG', 'GAC', 'AAC', 'CAG', 'CAC', 'ACC', 'ACG', 'AGC', 'TCC', 'TCG', 'TGC', 'GCC', 'GCG', 'GTC', 'GTG', 'CTC', 'CTG', 'TTG', 'ATC', 'ATG', 'TTC', 'TAC', 'TGG', 'GGC', 'GGG', 'CCC', 'CCG', 'TAG']

with open('/Users/siddharthnimkar/Dropbox (VU Basic Sciences)/MiSeq/test.sh', 'w') as fid:
    for i in range(0, len(target_seq), 3):
        tmp = list(target_seq)
        for j in range(32):
            tmp[i:i+3] = list(cod[j])
            fid.write(f"grep -c {''.join(fwd_anchor + ''.join(tmp))} P1inp.fastq >> P1inp.txt\n")
        print(i)