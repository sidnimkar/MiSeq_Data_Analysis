from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd

# prompt the user to enter a protein sequence
protein_seq = input("Enter a protein sequence: ")

# create a SeqRecord object to hold the sequence
protein_seq_record = SeqRecord(Seq(protein_seq))

# create a list of all possible amino acids
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# create a list of all possible sequential mutations
mutations = []
for i in range(len(protein_seq_record.seq)):
    for aa in amino_acids:
        mut_seq = []
        if aa == (protein_seq_record.seq):
            continue
        else:
            # make a copy of the original sequence
            mut_seq = protein_seq_record.seq.tomutable()
            # mutate the i-th amino acid in the sequence
            mut_seq[i] = aa
            # add the mutated sequence to the list of mutations
            mutations.append(SeqRecord(mut_seq))
        
# create a dataframe from the mutated sequences
df = pd.DataFrame({"Sequence": [str(mutation.seq) for mutation in mutations]})

# write the dataframe to an Excel file
df.to_excel("mutated_sequences14.xlsx")
