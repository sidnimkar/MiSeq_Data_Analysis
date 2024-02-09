from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import pandas as pd

# create a protein sequence using the IUPAC alphabet
protein_seq = Seq("MYSERTYGINS", IUPAC.protein)

# create a SeqRecord object to hold the sequence
protein_seq_record = SeqRecord(protein_seq)

# create a list of all possible sequential mutations
mutations = []
for i in range(len(protein_seq_record.seq)):
    # create a mutable version of the sequence
    seq = protein_seq_record.seq.tomutable()

    # mutate each amino acid in turn
    for j in range(len(seq)):
        if i == j:
            # if this is the current position, mutate the amino acid
            seq[j] = "X"
        else:
            # otherwise, set the amino acid to the original value
            seq[j] = protein_seq_record.seq[j]

    # add the mutated sequence to the list
    mutations.append(SeqRecord(seq))

# create a dataframe from the mutated sequences
df = pd.DataFrame({"Sequence": [str(mutation.seq) for mutation in mutations]})

# write the dataframe to an Excel file
df.to_excel("mutated_sequences.xlsx")
