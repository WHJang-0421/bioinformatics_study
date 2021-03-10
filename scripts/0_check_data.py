from Bio import SeqIO
from Bio import pairwise2
from Bio.SeqRecord import SeqRecord

ref_seq = ()
sequences = ()

# open files
ref_file = open("bioinformatics_study/data/before_preprocessing/refseq.fasta", "r", encoding='utf-8')
seq_file = open("bioinformatics_study/data/before_preprocessing/sequences.fasta", "r", encoding='utf-8')
align_file = open("bioinformatics_study/data/after_preprocessing/alignments.fas", "w", encoding='utf-8')

# read files
ref_seq = SeqIO.read(ref_file, "fasta")
sequences = SeqIO.parse(seq_file, "fasta")

print(len(ref_seq))
print(len(list(sequences)))

# close files
ref_file.close()
seq_file.close()
align_file.close()