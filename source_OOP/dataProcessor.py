#!/usr/bin/python3.8
"""
#
# dataProcessor.py: class for convert copora to words frequency matrix
#
#   Author: C. Lu
#   Date: July. 28, 2021
#
"""
import os
import string
import pandas as pd
import numpy as np
import nltk
from numpy.linalg import svd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import pairwise_distances

from utilities import Utilities

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class DataProcessor:

  def __init__(self, corpora, docs_list):

    self.corpora = corpora
    self.docs_list = docs_list

  # create word frequency matrix from corpora 
  def corpora_to_words_freq(self):

    # set up lemmatizer for changing the word form back to its lemma, such as,  change "am, are, is" to "be"
    lemmatizer = WordNetLemmatizer()

    # sw contains the stopwords, such as "a", "an", etc. that are commonly used but carry very little useful information
    sw = stopwords.words('english')

    # convert corpora to a words string, remove all punctuations, and change all words in lower case

    ut = Utilities()

    words_string = ut.lists_to_string(self.corpora)
    words_string = ut.remove_punctuations(words_string).lower()
    words_list = words_string.split()

    #create words set with lemmatizer
    words_set ={lemmatizer.lemmatize(word) for word in words_list if not word in sw}

    # create words frequency from corpora
    col_name = "document"
    df = pd.DataFrame(data=self.corpora, columns=[col_name])
    words_vector = CountVectorizer(vocabulary=words_set, min_df=0)
    words_frequency = words_vector.fit_transform(df[col_name].values)

    self.words_vector = words_vector
    self.words_frequency = words_frequency

  def create_words_freq_matrix(self):

    # create words frequency matrix from corpora
    words_freq_matrix = pd.DataFrame(data=self.words_frequency.toarray(), index=self.docs_list, columns=self.words_vector.get_feature_names())

    print("words_freq_matrix=", words_freq_matrix)

    # remove words which appear in less than 2 documents
    words_freq_matrix.drop([col for col, val in words_freq_matrix.sum().iteritems() if val < 2], axis=1, inplace=True)

    #create words list which will be analysed 
    words = words_freq_matrix.columns.values.tolist()
    self.words = words

    (row, col) = words_freq_matrix.shape
    return (words_freq_matrix, row, col)


  def create_tf_idf_matrix(self):

    wf = self.words_frequency
    print("wf=", wf)

    transformer = TfidfTransformer()
    tf_idf_frequency = transformer.fit_transform(self.words_frequency)
    print("tf_idf_frequency=", tf_idf_frequency)

    tf_idf_freq_matrix = pd.DataFrame(data=tf_idf_frequency.toarray(), index=self.docs_list, columns=self.words_vector.get_feature_names())
    print("tf_idf_freq_matrix=", tf_idf_freq_matrix)

    # remove words which appear in less than 2 documents
    tf_idf_freq_matrix = tf_idf_freq_matrix[[c for c
        in list(tf_idf_freq_matrix)
        if len(tf_idf_freq_matrix[c].unique()) > 2]]

    return tf_idf_freq_matrix

  
  def convert_full_matrix_to_tril(self, matrix, name):

    #convert full matrix to lower half matrix and comine with index and column information
    matrix_lower_tri  = pd.DataFrame(data=np.tril(matrix, k=0), index=name, columns=name)

    self.matrix_lower_tri = matrix_lower_tri
