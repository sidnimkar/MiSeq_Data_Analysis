from Bio.Seq import Seq

# Correct BsaI site (GGTCTC) and complementary overhang to AAGC
bsaI_site_with_complementary_overhang = 'GCTTAgAGACC'
# NNS codon for random mutation
nns_codon = 'NNS'

def calculate_tm(seq):
    """Calculate the melting temperature using the Wallace rule."""
    return (2 * (seq.count('A') + seq.count('T')) + 4 * (seq.count('C') + seq.count('G'))) - 20

def generate_reverse_primer_with_bsaI_site_and_desired_tm(dna_sequence, amino_acid_position):
    protein_sequence = Seq(dna_sequence).translate()
    if amino_acid_position < 1 or amino_acid_position > len(protein_sequence):
        raise ValueError("Amino acid position is out of range.")
    codon_start_index = (amino_acid_position - 1) * 3
    
    # Initialize the primer with the BsaI site with complementary overhang
    primer = bsaI_site_with_complementary_overhang
    primer_extension = ''
    
    # Extend the primer until the desired Tm is reached for the extension part
    i = 0
    while calculate_tm(primer_extension) < 58 and codon_start_index - i > 0:
        primer_extension += dna_sequence[codon_start_index - i - 1]
        i += 1
        if calculate_tm(primer_extension) > 61:
            # Remove the last added base and stop
            primer_extension = primer_extension[:-1]
            break
    
    if calculate_tm(primer_extension) < 58:
        raise ValueError("Cannot achieve desired Tm with given sequence constraints.")
    
    # Reverse complement the entire primer to make it a proper reverse primer
    primer = str(Seq(primer_extension + primer).reverse_complement())
        
    return primer

def print_fasta_with_bsaI_site_and_desired_tm_for_range_reverse(dna_sequence, start_position, end_position):
    for amino_acid_position in range(start_position, end_position + 1):
        try:
            primer_reverse = generate_reverse_primer_with_bsaI_site_and_desired_tm(dna_sequence, amino_acid_position)
            # Calculate Tm for the extension only
            tm = calculate_tm(primer_reverse[len(bsaI_site_with_complementary_overhang):])
            print(">Reverse_Primer_for_AA_Pos_{} (Tm: {}C)".format(amino_acid_position, tm))
            print(primer_reverse)
        except ValueError as e:
            print("Error for amino acid position {}: {}".format(amino_acid_position, e))

# Example usage:
dna_seq = "ATGATTACTGTAAATGAAAAAGAACACATTCTTGAACAGAAATATCGTCCATCTACTATCGATGAATGTATTCTTCCCGCCTA"
start_amino_acid_position = 12
end_amino_acid_position = 14
print_fasta_with_bsaI_site_and_desired_tm_for_range_reverse(dna_seq, start_amino_acid_position, end_amino_acid_position)