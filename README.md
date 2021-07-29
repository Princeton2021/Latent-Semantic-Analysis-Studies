# Latent Semantic Analysis 



  Latent Sementic Analysis (LSA) is one of the most popular Natural Language Processing (NLP) techniques for finding hidden relationships between terms and concepts  mathematically. It is an unsupervised learning. A mathematical technique called "singular value decomposition (SVD)" is used to examinate the unstructured data. More information about the LSA theory and the method can be found in a paper at the location: http://lsa.colorado.edu/papers/dp1.LSAintro.pdf.
  
  
  The Python code implemented in this repository is based on the LSA method. Given a set of text documents, the code can be used to find the correlations between words in these documents and the correlations between the documents in the set.
  
  
  There are 4 subdirectoies in this repository: source, input, output and scripts. Below are the description of each subdirectory:
    
    source_OOP: has the source code in object orientied programing(OOP) style
  
  	input:  has the inputs data for the source code
  
  	output: has the outputs from the source code
  
  	scritps: has shell scripts to run the code
    
    There are 2 subdirectories in output: 
  
      output/correlations: has the correlation results for both words and documents in all SVD reduced dimensions
      output/plots: has the plots for correlation results for both words and documents in several SVD reduced dimensions.
  
  The sample data used for the analysis are from the paper in the above link. Minimum 2 documents are required for analysis.
  
  Before running the code, 3 Python modules panda, sklearn and seaborn are required. The installation can be done by doing the following:
  
  	pip install pandas
    pip install sklearn
    pip install seaborn
  
  Repl.it IDE (www.repl.it) has been used for code implementation and execution.
  
  
  To learn how to run the code, see script "runLSA.sh" or "runLSA_OOP.sh in scripts subdirectory.
  

  
  
  
  
  


  
 
