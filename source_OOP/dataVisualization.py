#!/usr/bin/python3.8
"""
#
# dataVisualization.py: class for getting visual representation of data
#
#   Author: C. Lu
#   Date: July. 28, 2021
#
"""
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

class DataVisualization:

  def pairs_plot(self, data, filename):
    df = pd.DataFrame(data)
    sn.pairplot(df)
    plt.savefig(filename)

  def bars_plot_4(self, data1, d1, data2, d2, data3, d3, data4, d4, out_dir):

    rows, cols = data1.shape
  
    #header of the correlation data
    header = data1.iloc[0].index.tolist()
    header.pop(0)
    index = [header[i] for i in range(2)]

    for i in range(rows):

      value1 = data1.iloc[i].values.tolist()
      name1 = value1.pop(0)

      value2 = data2.iloc[i].values.tolist()
      name2 = value2.pop(0)

      value3 = data3.iloc[i].values.tolist()
      name3 = value3.pop(0)

      value4 = data4.iloc[i].values.tolist()
      name4 = value4.pop(0)

      df = pd.DataFrame({'SVD dimension = '+str(d1): value1, 'SVD dimension = '+str(d2): value2, 'SVD dimension = '+str(d3): value3, 'SVD dimension = '+str(d3): value3, 'SVD dimension = '+str(d4): value4}, index=header)

      ax = df.plot.bar(rot=1) 
      ax.set_title("correlations of \""+name1+"\" with others")
      ax.set_ylabel("correlation")

      plt.xticks(rotation = 30)
      #plt.xticks(range(len(header)), header, rotation='vertical')

      name1=name1.strip(".txt")

      plt.savefig(out_dir+"/"+name1)
      

  def bars_plot_style_T(self, data, filename):

    rows, cols = data.shape
  
    #header of the correlation data
    header = data.iloc[0].index.tolist()
    header.pop(0)

    for i in range(rows):

      value = data.iloc[i].values.tolist()
      word = value.pop(0)

      df = pd.DataFrame({'SVD': value}, index=header)

      ax = df.T.plot.bar(rot=0)  
      plt.savefig(word)

  def heatmap_view(self, data, filename):

    mask = np.zeros_like(data, dtype=np.bool)
  
    ax = sn.heatmap(data, mask=mask, center=0, vmin=-1, vmax=1, linewidths=.5, square=True, annot=True, cmap="Greens")
    plt.savefig(filename)