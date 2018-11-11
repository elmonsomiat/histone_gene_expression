import os
from predictor.gene_expression_predictor import write_predictions_to_file


model = os.environ.get('model', 'LSTM')
input_file = os.environ.get('input_file')
output_file = os.environ.get('output_file')

write_predictions_to_file(model, input_file, output_file)

print('The predictions are available in', output_file)