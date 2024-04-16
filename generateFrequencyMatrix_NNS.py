#!/usr/local/bin/python

from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Seq import Seq
#from Bio.Alphabet import generic_dna, generic_protein
import numpy
from collections import OrderedDict

# Import data

wtSeq = SeqIO.read("wild-type.fasta", "fasta")
codonList = ["GCT", "GCC","GCA", "GCG", "TGT","TGC","GAT", "GAC","GAA", "GAG","TTC","TTT", "GGT", "GGC","GGA", "GGG","CAT","CAC", "ATT", "ATC", "ATA", "AAA","AAG", "CTT", "CTC", "CTA", "CTG", "TTA","TTG","ATG","AAT","AAC", "CCT","CCC","CCA","CCG", "CAA","CAG","AGA","AGG","CGT", "CGC","CGA", "CGG","AGT","AGC","TCT","TCC","TCA","TCG","ACT","ACC","ACA","ACG","GTT","GTC","GTA","GTG","TGG","TAT","TAC","TAA", "TAG"]
wtSeqStr = str(wtSeq.seq)
wtSeqList = [wtSeqStr[i:i+3] for i in range(0, len(wtSeqStr), 3)]

# Enumerate variants

variants = OrderedDict()
for position, codon in enumerate(wtSeqList):
    for codons in codonList:
        variant = ''.join(wtSeqList[0:position]) + ''.join(codons) + ''.join(wtSeqList[position+1:])
        variants[variant] = 0

# Count variant frequency

for nuc in SeqIO.parse("SM11.trimmed.fastq", "fastq"):
    if str(nuc.seq) in variants:
        variants[str(nuc.seq)] += 1
        
# Generate frequency matrix

frequencyMatrix = numpy.zeros(shape=(len(codonList),len(wtSeqList)))

for i in range(len(wtSeqList)):
    for j in range(len(codonList)):
        frequencyMatrix[j][i] = variants[''.join(wtSeqList[0:i]) + ''.join(codonList[j]) + ''.join(wtSeqList[i+1:])]
                
numpy.savetxt("SM11_counts.txt", frequencyMatrix, fmt = '%i', delimiter='\t')

#Identify wild-type alleles

wtSeqTrans = wtSeq.seq.translate(to_stop=False)

wtFile = open('SM11_wild-type_counts.txt', 'w+')
for k in variants:
    kSeq = Seq(k)
    kTrans = kSeq.translate()
    if kTrans == wtSeqTrans:
       wtFile.write(k + "\t" + str(variants[k]) + "\n")
       #print k, variants[k]
wtFile.close()
