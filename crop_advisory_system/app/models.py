import pickle
import os
import numpy as np

model_path = os.path.join('models', 'crop_recommendation.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def predict_crop(data):
    input_features = np.array([[
        data['N'], data['P'], data['K'],
        data['temperature'], data['humidity'],
        data['pH'], data['rainfall']
    ]])
    prediction = model.predict(input_features)
    return prediction[0]
