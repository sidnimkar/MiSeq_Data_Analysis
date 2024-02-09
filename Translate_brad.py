import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Data import CodonTable

def dna_to_protein(dna_sequence):
  """Translates a DNA sequence to a protein sequence.

  Args:
    dna_sequence: The DNA sequence to be translated.

  Returns:
    The translated protein sequence.
  """

  codon_table = CodonTable.unambiguous_dna_by_id[1]
  protein_sequence = Seq(dna_sequence).translate(codon_table)

  return protein_sequence

def fasta_to_excel(Pool2_3_index, excel_file):
  """Reads DNA sequences from a FASTA file, translates them to protein sequences, and writes them to an Excel file.

  Args:
    fasta_file: The path to the FASTA file.
    excel_file: The path to the Excel file.
  """

  df = pd.DataFrame(columns=["DNA Sequence", "Protein Sequence"])
  for record in SeqIO.parse(Pool2_3_index, "fasta"):
    dna_sequence = record.seq
    protein_sequence = dna_to_protein(dna_sequence)
    df = df.append({"DNA Sequence": dna_sequence, "Protein Sequence": protein_sequence}, ignore_index=True)

  df.to_excel(excel_file, index=False)

if __name__ == "__main__":
  fasta_file = "dna_sequences.fasta"
  excel_file = "dna_to_protein.xlsx"
  fasta_to_excel(fasta_file, excel_file)
