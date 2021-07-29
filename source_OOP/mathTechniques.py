#!/usr/bin/python3.8
"""
#
# mathProcessor.py: class of math techniques
#
#   Author: C. Lu
#   Date: July 28, 2021
#
"""
import pandas as pd
import numpy as np
from numpy.linalg import svd
from sklearn.metrics.pairwise import pairwise_distances

class MathTechniques:

  def __init__(self, matrix):

    self.matrix = matrix

  # create matrix from SVD dimension reduction 
  def SVD_decomposition(self):

    #matrix transposed
    matrix_transposed = self.matrix.T

    # define the matrix as a 2 dimentional numpy array
    A = matrix_transposed.to_numpy()

    # apply SVD  on  matrix A 
    U, S, VT = svd(A)

    self.U = U
    self.S = S
    self.VT = VT

    print("U = ", U)
    print("S = ", S)
    print("VT = ", VT)
  
  def SVD_dim_reduction(self, dimension):

    # SVD dimensions reduction. 
    UD = self.U[:, :dimension]
    SD = np.diag(self.S[:dimension])

    VTD = self.VT[:, :dimension]

    # reconstruct frequency matrix from the matrix with dimension reduction 
    matrix_svd_reduction = UD @ SD @ VTD.T

    return matrix_svd_reduction

  # correlation calculation
  def correlations(self, data, col_name):

    # calculate the correclation
    df = pd.DataFrame(data, columns=col_name)
    corr_mat = df.corr()

    return corr_mat

  # cosine similarity calculation - pairwise from sklearn.metrics
  def cosine_similarity(self, data, col_name):
    # calculate the cosine correclation
    df = pd.DataFrame(data, columns=col_name)
    cosine_sim = pairwise_distances(data, metric="cosine")

    return cosine_sim
