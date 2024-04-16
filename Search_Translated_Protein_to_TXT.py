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

def search_protein_in_output_file(output_file, protein_to_search, result_file):
    with open(result_file, 'w') as result_handle:
        for record in SeqIO.parse(output_file, "fasta"):
            if protein_to_search in record.seq:
                result_handle.write(f"{record.id}\n")


input_fasta_file = 'Q118NP1inp.fasta' # Replace 'input.fasta' with the path to your input FASTA file
output_protein_file = 'output_proteins.fasta' # Replace 'output_proteins.fasta' with the desired output file path

translate_fasta_file_to_protein(input_fasta_file, output_protein_file) # Translate DNA sequences to protein and write to output file

protein_to_search = 'IPHIILHSPSPGTGKTTVAKALC' # Replace 'IPHIILHSPSPGTGKTTVAKALC' with the protein sequence you are searching for

result_file = 'matching_ids.txt' # Replace 'matching_ids.txt' with the desired text file to write the matching sequence IDs

search_protein_in_output_file(output_protein_file, protein_to_search, result_file) # Search for the given protein sequence in the output file and write matching IDs to the result file

print(f"Matching sequence IDs have been written to {result_file}")