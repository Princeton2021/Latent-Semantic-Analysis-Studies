#!/usr/bin/python3.8
"""
#
# LSA.py: Latent semantic analysis application for finding correlation among words and documents
#
# input: 
#    text documents
#
# output:  
#   words frequency matrix
#   correlation among the words 
#   correlation among the documents 
#   
#   Author: C. Lu
#   Date: July 28, 2021
#
"""

import sys

from documentProcessor import DocumentProcessor
from dataProcessor import DataProcessor
from mathTechniques import MathTechniques
from dataVisualization import DataVisualization

def main():

    print("Start running ...")

    # inputs from the command line arguments
    source_code_name = sys.argv[0]
    input_dir = sys.argv[1]
    output_file = sys.argv[2]
    corr_dir = sys.argv[3]

    # generate copora from documents
    docs_process = DocumentProcessor(source_code_name, input_dir, output_file)
    docs_process.docs_to_corpora()

    # create words frequency from corpora
    data_process = DataProcessor(docs_process.corpora, docs_process.docs)
    data_process.corpora_to_words_freq()
    (words_freq_matrix, row, col) = data_process.create_words_freq_matrix()
    
    # SVD method to create dimension reduced words frequency matrix 
    math_techniques = MathTechniques(words_freq_matrix)
    math_techniques.SVD_decomposition()
    
    # calculate the corrlations for all dimension of SVD 
    for dimension in range(1,row+1):

      SVD_matrix = math_techniques.SVD_dim_reduction(dimension)

      # calculate correlations for documents
      docs_corr_mat = math_techniques.correlations(SVD_matrix, docs_process.docs)

      # calculate correlations for words
      words_corr_mat = math_techniques.correlations(SVD_matrix.T, data_process.words)

      #create file names for outputs
      docs_corr_file = corr_dir+"/docs_corr_SVD_dim"+str(dimension)+".csv"
      words_corr_file = corr_dir+"/words_corr_SVD_dim"+str(dimension)+".csv"

      print("doc_corr_file=", docs_corr_file)

      #save correlation to csv file for further analysis
      docs_corr_mat.to_csv(docs_corr_file)
      words_corr_mat.to_csv(words_corr_file)


    # open output_file for outputs
    docs_process.open_outfile()
    
    # write all input documents to output file
    docs_process.write_documents_to_file()
    
    # write words frequency matrix to output file
    docs_process.write_matrix_to_file(words_freq_matrix, "words frequency matrix:")

    #close output file
    docs_process.close_outfile()

    
if __name__== "__main__":
    main()

print("Done successfully !")
    
    
