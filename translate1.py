# Define the input and output file paths
input_file = 'Pool4_6_index.txt'  # Replace with your input text file
output_file = 'Pool4_6_output.fasta'  # Replace with your desired output text file

# Function to translate a DNA sequence to protein
def translate_dna_to_protein(dna_sequence):
    # Create a translation table
    translation_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    # Ensure the input sequence length is a multiple of 3
    if len(dna_sequence) % 3 != 0:
        raise ValueError("Input DNA sequence length must be a multiple of 3")

    # Translate the DNA sequence
    protein_sequence = ''.join([translation_table[dna_sequence[i:i+3]] for i in range(0, len(dna_sequence), 3)])
    
    return protein_sequence

# Read DNA sequences from the input file and translate them
with open(input_file, 'r') as f:
    dna_sequences = [line.strip() for line in f]

protein_sequences = [translate_dna_to_protein(seq) for seq in dna_sequences]

# Write the translated protein sequences to the output file
with open(output_file, 'w') as f:
    for protein_seq in protein_sequences:
        f.write(protein_seq + '\n')

print('Translation completed. Protein sequences saved to', output_file)
