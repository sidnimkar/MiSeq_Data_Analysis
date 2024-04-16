#!/usr/local/bin/python

from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import numpy

# Import data

wtSeq = SeqIO.read(open("wild-type.fasta"), "fasta")
aaList = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y","*"]
wtSeqList = list(wtSeq.seq)

# Enumerate variants

variants = {str(wtSeq.seq):0}
for position, residue in enumerate(wtSeqList):
    remaining = list(set(aaList) - set(residue))
    for aa in remaining:
        variant = ''.join(wtSeqList[0:position]) + ''.join(aa) + ''.join(wtSeqList[position+1:])
        variants[variant] = 0

# Translate nucleotide sequence and count variant frequency

for nuc in SeqIO.parse("1.fastq", "fastq"):
    protein = SeqRecord(seq = nuc.seq.translate(to_stop=False), id = "trans_" + nuc.id, description = "translation of variant")
    if str(protein.seq) in variants:
        variants[str(protein.seq)] += 1
        
# Generate frequency matrix

frequencyMatrix = numpy.zeros(shape=(len(aaList),len(wtSeqList)))
pairs = enumerate("ACDEFGHIKLMNPQRSTVWY*")
revPairs = [(v,k) for k,v in pairs]
revMapping = dict(pairs)
mapping = dict(revPairs)

for i in range(len(wtSeqList)):
    variantList = [x for x in variants if x[i] != wtSeqList[i]]
    for j in range(len(variantList)):
        frequencyMatrix[mapping[variantList[j][i]]][i] = variants[variantList[j]]
        frequencyMatrix[mapping[wtSeqList[i]]][i] = variants[str(wtSeq.seq)]
        
                
numpy.savetxt("1.txt", frequencyMatrix, fmt = '%i', delimiter='\t')
