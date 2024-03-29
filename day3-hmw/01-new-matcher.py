#!/usr/bin/env python
"""
practice, Alternative kmer matcher
Input: xxx.py target.fa query.fa k
Output: target_seq_name  target_start  query_start kmer_seq
"""
import sys
import fasta_fixed

###
target = open(sys.argv[1]) 
query = open(sys.argv[2])
k_len = int(sys.argv[3])
#stringg = str(sys.argv[4])

### Make dictionary of kmer_seq and query start 

query_start = {}
for ident, sequence in fasta_fixed.FASTAReader(query):
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k_len):
        kmer = sequence[i: i+k_len]
        #if kmer not in query_start:
        #print kmer
        if not query_start.get(kmer,0):
            query_start[kmer] = i

# print sequence[0:4]
#print (query_start[stringg])

#print query_start
#print kmer, query_start[kmer]

#parse line in target
#find kmer within sequence
#p# rint ident (target_name) with kmer
#
for ident, sequence in fasta_fixed.FASTAReader(target):
    sequence = sequence.upper()
    for i in range(0, len(sequence)-k_len):
        kmer = sequence[i : i+k_len]
        target_start = str(i)
        if kmer in query_start:
            print ident, target_start, query_start[kmer], kmer

        #matches.sort(reverse=True, key=query_start[kmer])
        #print matches






