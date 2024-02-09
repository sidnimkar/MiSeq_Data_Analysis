fwd_anchor = ""
rev_anchor = ""
target_seq = "CTAAAACTTGAATGAGGAAATTATGATTACTGTAAATGAAAAAGAACACATTCTTGAACAGAAATATCGTCCATCTACTATCGATGAATGTATTCTTCCCGCCTTTGATAAAGAAACCTTTAAATCTATTACAAGTAAAGGTAAGATTCCACATATTATTCTTCATTCTCCTTCTCCAGGAACAGGTAAAACAACTGTAGCAAAAGCATTATGTCATGATGTAAATGCTGATATGATGTTTGTGAATGGGTCAGATTGTAAAATTGATTTCGTTCGTGGTCCTTTGACTAATTTTGCCAGCGCCGCTTCATTTGATGGTCGTCAAAAAGTAATCGTTATTGATGAATTTGACCGTTCAGGGTTAGCAGAGTCTAATCGACATCTTCGTTCCTTTATGGAAGCTTATAGTTCAAACTGTAG"

counts = [0] * (32 * len(target_seq) // 3)  # Convert numel to len and use integer division

cod = ["AAG", "CGC", "CGG", "AGG", "GAG", "GAC", "AAC", "CAG", "CAC", "ACC", "ACG", "AGC",
       "TCC", "TCG", "TGC", "GCC", "GCG", "GTC", "GTG", "CTC", "CTG", "TTG", "ATC", "ATG",
       "TTC", "TAC", "TGG", "GGC", "GGG", "CCC", "CCG", "TAG"]

# Open the output file in write mode
with open("C:/Users/sidni/Documents/Pool1inp.sh", "w") as fid:

    for i in range(0, len(target_seq), 3):
        tmp = target_seq

        for j in range(32):
            tmp = tmp[:i] + cod[j] + tmp[i+3:]
            command = f"grep -c {fwd_anchor + tmp} P1inp.fastq >> Pool1inptestcounts1.txt"
            fid.write(command + "\n")

        print(i)

# Close the file
fid.close()
