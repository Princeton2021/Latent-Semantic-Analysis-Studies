#This script uses the source code in source_OOP location

#input_dir:  the location of the input data to be processed. 
input_dir=../output/correlations
output_dir=../output/plots
source_code=../source_OOP/createPlots.py

PYTHON=/usr/bin/python3.8

#words and documents correlations data file prefix
wcorr=$input_dir/words_corr_SVD_dim
dcorr=$input_dir/docs_corr_SVD_dim

#for corr in $wcorr $dcorr
for corr in $dcorr
do 

  data1=$corr\2.csv
  dim1=2

  data2=$corr\4.csv
  dim2=4

  data3=$corr\6.csv
  dim3=6

  data4=$corr\8.csv
  dim4=8

  echo $data1,  $data2, data3, data4

  $PYTHON  $source_code $data1 $dim1 $data2 $dim2 $data3 $dim3 $data4 $dim4 $out_dir

echo "Done"
done

