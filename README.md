This repository contains the trained models (both CNN and LSTM) to predict the gene expression given 5 histones modification marks:

https://www.kaggle.com/c/gene-expression-prediction


To run using to Docker:
`docker build -t histone_predictor .`


`docker run  -e model="LSTM" -e input="path_to_data/input_data_name.csv" -e output "output_data_name.csv" -v /path/to/local/result/location:/histone_gene_expression_results histone_predictor`


e.g.:
`docker run -e model="CNN" -e input_file="data/x_train.csv" -e output_file="output.csv" -v /home/ana/kaggle/histone_gene_expression:/histone_gene_expression_results histone_predictor`

