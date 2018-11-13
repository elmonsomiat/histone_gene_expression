import pandas as pd
import numpy as np
import os
from keras.models import model_from_json


class GeneExpressionPredictor(object):
    
    """docstring for GeneExpressionPredictor"""
    def __init__(self, model='LSTM'):
        self.model = model
        if self.model=='LSTM':
            self.json_file='trained_models/histone_LSTM.json'
            self.weights_file='trained_models/histone_LSTM.hdf5'
        elif self.model=='CNN':
            self.json_file='trained_models/histone_CNN.json'
            self.weights_file='trained_models/histone_CNN.hdf5'
        else:
            raise NameError
        self.loaded_model = self.model_loader()


    def model_loader(self):
        json_file = open(self.json_file, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(self.weights_file)
        return loaded_model


    def model_predictor(self, X_pred):
        return self.loaded_model.predict(X_pred)



def predict_expression(model, X):
    predictor = GeneExpressionPredictor(model)
    result = predictor.model_predictor(X)
    return result

def clean_data(data_df):
    grp = data_df.groupby('GeneId')
    X_ser = grp.apply(lambda x: np.array(x[[ 'H3K4me3', 'H3K4me1', 'H3K36me3', 'H3K9me3', 'H3K27me3']]))
    X = np.stack(np.array(X_ser))
    return X

def write_predictions_to_file(model, input_file, output_file):
    data_df = pd.read_csv(input_file)
    X = clean_data(data_df)
    result = predict_expression(model, X)
    result_df = pd.DataFrame(result, columns=['result'])
    if not os.path.exists('output/'):
        os.makedirs('output/')
    result_df.to_csv('output/'+output_file, index=False)
    pass
