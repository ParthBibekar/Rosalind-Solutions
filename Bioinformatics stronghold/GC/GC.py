#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:15:39 2021

@author: parth
"""
from Bio import SeqIO
from Bio.SeqUtils import GC

for seq_record in SeqIO.parse("rosalind_gc.fasta", "fasta"):
    print(seq_record.id)
    #print(repr(seq_record.seq))
    #print(len(seq_record))
    print((seq_record.seq.count("G")+seq_record.seq.count("C"))/len(seq_record)*100)
   
    
