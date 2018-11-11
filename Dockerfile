FROM tensorflow/tensorflow:latest-py3
RUN mkdir /histone_gene_expression_results
WORKDIR /histone_gene_expression_results
COPY . /histone_gene_expression_results
RUN pip install -r requirements.txt
CMD ["python", "/histone_gene_expression_results/run_predictor.py", "--debug"]