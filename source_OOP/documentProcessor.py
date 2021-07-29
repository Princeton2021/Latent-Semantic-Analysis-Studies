#!/usr/bin/python3.8
"""
#
# DocumentProcessopr class: process documents 
#
# author: C. Lu
#
# date: July 28, 2021
#
"""
import os
import sys
import pandas as pd
import numpy as np

class DocumentProcessor():

    def __init__(self, name, indir, outfile):

        self.name = name
        self.indir = indir
        self.outfile = outfile

        # get all documents in input directopry
        docs = sorted(os.listdir(indir))
        self.docs = docs
        
        # set the float point format and the matrix display option
        pd.options.display.float_format = '{:,.1f}'.format
        pd.set_option("display.max_rows", None, "display.max_columns", None)

    # create corpora from all documents
    def docs_to_corpora(self):

        corpora = []
        for doc in self.docs:
            doc_file = os.path.join(self.indir, doc)

            with open(doc_file) as infile:
                all_lines = infile.readlines()

            all_lines = [line.strip() for line in all_lines]
            corpus = [" ".join(all_lines)]
            corpora.append(corpus)

        self.corpora = corpora


    def open_outfile(self):
        lsa_output = open(self.outfile, "w")
        lsa_output.write(self.name + " output:\n\n")
        self.lsa_output = lsa_output
        
    def close_outfile(self):
        self.lsa_output.close()

    # write documents to output file
    def write_documents_to_file(self):

        for i in range(len(self.docs)):
            self.lsa_output.write(self.docs[i])
            self.lsa_output.write(": ")
            self.lsa_output.write(" ".join(self.corpora[i]))
            self.lsa_output.write("\n")
        
    # write matrix to output file
    def write_matrix_to_file(self, matrix, title):
        
        self.lsa_output.write("\n\n"+title+"\n\n")
        self.lsa_output.write(matrix.to_string(header=True, index=True))
        self.lsa_output.write("\n")
    
