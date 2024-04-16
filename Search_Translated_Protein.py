from Bio.Seq import Seq
from Bio import SeqIO

def translate_dna_to_protein(dna_sequence):
    dna_seq = Seq(dna_sequence)
    protein_seq = dna_seq.translate(to_stop=True)
    return protein_seq

def translate_fasta_file_to_protein(fasta_file, output_file):
    with open(output_file, 'w') as output_handle:
        for record in SeqIO.parse(fasta_file, "fasta"):
            protein_sequence = translate_dna_to_protein(record.seq)
            output_handle.write(f">{record.id}\n{protein_sequence}\n")

def search_protein_in_output_file(output_file, protein_to_search):
    matching_ids = []
    for record in SeqIO.parse(output_file, "fasta"):
        if protein_to_search in record.seq:
            matching_ids.append(record.id)
    return matching_ids


input_fasta_file = 'Q118NP1inp.fasta' # Replace 'input.fasta' with the path to your input FASTA file
output_protein_file = 'output_proteins.fasta' # Replace 'output_proteins.fasta' with the desired output file path

# Translate DNA sequences to protein and write to output file
translate_fasta_file_to_protein(input_fasta_file, output_protein_file)

# Replace 'GKIPHIILHSPSPGTGKTTVAKALCHDVNADM' with the protein sequence you are searching for
protein_to_search = 'GKIPHIILHSPSPGTGKTTVAKALCHDVNADM'

# Search for the given protein sequence in the output file
matching_sequence_ids = search_protein_in_output_file(output_protein_file, protein_to_search)

# Print the IDs of sequences that contain the given protein sequence
print("Matching sequence IDs:")
for seq_id in matching_sequence_ids:
    print(seq_id)