'''
Just checking whether the data is correct. 
The data should have 40939 aligned sequences, respectively lengthed 1273 amino acids.
'''

from Bio import SeqIO
from Bio import AlignIO
from Bio import pairwise2
from Bio.SeqRecord import SeqRecord

# open files
ref_file = open("data/before_preprocessing/refseq.fasta", "r", encoding='utf-8')
align_file = open("data/before_preprocessing/alignments.fasta", "r", encoding='utf-8')

# read files
ref_seq = SeqIO.read(ref_file, "fasta")
alignments = AlignIO.parse(align_file, "fasta")

print("length of each sequence:", len(ref_seq))
print("number of aligned sequences:", len(list(alignments)[0]))

# close files
ref_file.close()
align_file.close()