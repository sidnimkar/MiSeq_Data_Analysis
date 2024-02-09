from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd

# prompt the user to enter a protein sequence
protein_seq = input("Enter a protein sequence: ")

# create a SeqRecord object to hold the sequence
protein_seq_record = SeqRecord(Seq(protein_seq))

# create a list of all possible sequential mutations
mutations = [SeqRecord(protein_seq_record.seq[:i] + "X" + protein_seq_record.seq[i+1:]) for i in range(len(protein_seq_record.seq))]

# create a dataframe from the mutated sequences
df = pd.DataFrame({"Sequence": [str(mutation.seq) for mutation in mutations]})

# write the dataframe to an Excel file
df.to_excel("mutated_sequences.xlsx")
