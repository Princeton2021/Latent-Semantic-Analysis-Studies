#This script uses the source code in source_OOP location

#input_dir:  the location of the input data to be processed. 
#output_file: an output file containing the processed results from the code

input_dir=../input
output_dir=../output
corr_dir=$output_dir/correlations
output_file=$output_dir/LSA_OOP.output
source_code=../source_OOP/LSA.py

PYTHON=/usr/bin/python3.8

# check the existence of input directory
[ ! -d $input_dir ] && echo "Error: $input_dir does not exists. Please create it" && exit 1

# check the existence of output directory
[ ! -d $output_dir ] && echo "Error: $output_dir does not exists. Please create it" && exit 1

# check the existence of output directory
[ ! -d $corr_dir ] && echo "Error: $corr_dir does not exists. Please create it" && exit 1

# count the number of files in the input directopry. Minimum 2 files are required for analysis
[ $(ls $input_dir | wc -l) -le 2 ] && echo "Info: There are no enough files in $input_dir diretory for LSA analysis. Minimum 2 files are required" && exit 1

$PYTHON  $source_code $input_dir $output_file $corr_dir

