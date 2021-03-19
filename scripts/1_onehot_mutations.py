'''
1. Analyze SNP Occurence
Read alignments.fasta and analyze the number of occurences for each SNP.

2. Save to file
Add mutation information to data in sequences.csv (csv file containg sequence metadata),
and save file as mutations.csv
'''

from Bio import AlignIO
from Bio import SeqIO
import pandas as pd

### open files
ref_file = open("data/before_preprocessing/refseq.fasta", "r", encoding='utf-8')
align_file = open("data/before_preprocessing/alignments.fasta", "r", encoding='utf-8') 

refseq = SeqIO.read(ref_file, "fasta").seq
alignments = AlignIO.read(align_file, "fasta")

### find mutations
snp2seq = {}   # a dictionary containing {SNP: Seuqence number containing the SNP}

# repeating for every residue in every sequence
for seq_num, record in enumerate(alignments):
    for idx in range(len(refseq)):

        # if snp is detected
        if record[idx] != refseq[idx]:
            mutation_name = f"{refseq[idx]}{idx+1}{record[idx]}"  # example: 'D614G'
            
            # add mutation name and sequence number to snp2seq
            if mutation_name in snp2seq.keys():
                snp2seq[mutation_name].append(seq_num)
            else:
                snp2seq[mutation_name] = []

### count number of occurences for each SNP
min_count = 20
snp2count = {snp: len(list) for snp, list in snp2seq.items() if snp[-1] != 'X'} # exclude deletions
frequent_snp = [i for i in snp2count if snp2count[i] > min_count]  # select SNPs occuring over min_count

### add mutation data to sequences.csv
df = pd.read_csv("data/before_preprocessing/sequences.csv")

for snp in frequent_snp:
    selected_accessions = [alignments[i].id[:8] for i in snp2seq[snp]]
    df[snp] = pd.Series(df["Accession"].isin(selected_accessions))    # adds a true-or-false array into the dataframe

df.to_csv('data/after_preprocessing/mutations.csv')

### close files
ref_file.close()
align_file.close()