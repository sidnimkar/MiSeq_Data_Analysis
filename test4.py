from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import pandas as pd

# create a protein sequence using the IUPAC alphabet
protein_seq = Seq("VVEIILSHL", IUPAC.protein)

# create a SeqRecord object to hold the sequence
protein_seq_record = SeqRecord(protein_seq)

# create a list of all possible single amino acid mutations
mutations = [SeqRecord(protein_seq_record.seq.tomutable().reverse_complement()) for i in range(len(protein_seq_record.seq))]

# print the mutated sequences
for mutation in mutations:
    print(mutation.seq)



# create a dataframe from the mutated sequences
df = pd.DataFrame({"Sequence": [str(mutation.seq) for mutation in mutations]})

# write the dataframe to an Excel file
df.to_excel("mutated_sequences.xlsx")
