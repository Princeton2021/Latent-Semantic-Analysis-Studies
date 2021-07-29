#!/usr/bin/python3.8
"""
#
# createPlots.py: plot the correlation results for data visualization 
#
# input: 
#    cvs files
# 
#   Author: C. Lu
#   Date: July 28, 2021
#
"""
import sys
import pandas as pd
from dataVisualization import DataVisualization

# inputs from the command line arguments
source_code_name = sys.argv[0]

f1 = sys.argv[1]
dim1 = sys.argv[2]

f2 = sys.argv[3]
dim2 = sys.argv[4]

f3 = sys.argv[5]
dim3 = sys.argv[6]

f4 = sys.argv[7]
dim4 = sys.argv[8]

out_dir = "../output/plots"

df1 = pd.read_csv(f1)
df2 = pd.read_csv(f2)
df3 = pd.read_csv(f3)
df4 = pd.read_csv(f4)

#display correlation matrix
data_visual = DataVisualization()
data_visual.bars_plot_4(df1, dim1, df2, dim2, df3, dim3, df4, dim4, out_dir)