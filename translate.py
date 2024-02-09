from Bio import SeqIO

# Define the input and output file paths
input_fasta_file = 'Pool2_3_index.fasta'  # Replace with your input .fasta file path
output_text_file = 'output.txt'   # Replace with your desired output text file path

# Open the output text file for writing
with open(output_text_file, 'w') as output_file:
    # Iterate over the DNA sequences in the FASTA file
    for record in SeqIO.parse(input_fasta_file, 'fasta'):
        sequence_id = record.id
        dna_sequence = record.seq
        protein_sequence = dna_sequence.translate(to_stop=True)  # Translate DNA to protein

        # Write the translated protein sequence to the output text file
        output_file.write(f">{sequence_id}\n")
        output_file.write(f"{protein_sequence}\n")

print('Translation and writing to text file completed.')
