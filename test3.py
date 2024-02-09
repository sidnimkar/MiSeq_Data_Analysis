# Import necessary modules
from itertools import product
import xlsxwriter

# Define the amino acid alphabet
AMINO_ACID_ALPHABET = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

def generate_mutations(protein_sequence):
  # Create a list of tuples, where each tuple represents a possible mutation
  # at a given position in the protein sequence
  mutations = [mutation for mutation in product(AMINO_ACID_ALPHABET, repeat=len(protein_sequence))]
  
  # Filter out the original sequence from the list of mutations
  mutations = [mutation for mutation in mutations if mutation != tuple(protein_sequence)]
  
  return mutations

# Define a protein sequence to mutate
protein_sequence = "VVEIILSHL"

# Generate the mutations
mutations = generate_mutations(protein_sequence)

# Create an Excel workbook and worksheet
workbook = xlsxwriter.Workbook('mutations.xlsx')
worksheet = workbook.add_worksheet()

# Write the mutations to the Excel worksheet
row = 0
for mutation in mutations:
  worksheet.write_row(row, 0, mutation)
  row += 1

# Close the Excel workbook
workbook.close()
