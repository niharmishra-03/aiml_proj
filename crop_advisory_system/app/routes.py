from flask import Blueprint, render_template, request
from .models import predict_crop
from .utils import recommend_fertilizer
import os
import csv
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    crop_result = None
    fertilizer_result = None

    if request.method == 'POST':
        user_input = {
            'N': float(request.form['N']),
            'P': float(request.form['P']),
            'K': float(request.form['K']),
            'pH': float(request.form['pH']),
            'temperature': float(request.form['temperature']),
            'humidity': float(request.form['humidity']),
            'rainfall': float(request.form['rainfall']),
        }

        # Get crop and fertilizer results
        crop_result = predict_crop(user_input)
        fertilizer_result = recommend_fertilizer(user_input)

        # Path to log CSV
        log_path = os.path.join('data', 'predictions_log.csv')
        file_exists = os.path.isfile(log_path)

        # Log prediction data
        with open(log_path, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow([
                    'Timestamp', 'N', 'P', 'K', 'pH', 'Temperature', 'Humidity', 'Rainfall',
                    'Predicted Crop', 'Fertilizer Recommendation'
                ])
            writer.writerow([
                datetime.now(),
                user_input['N'], user_input['P'], user_input['K'],
                user_input['pH'], user_input['temperature'],
                user_input['humidity'], user_input['rainfall'],
                crop_result, fertilizer_result
            ])

    return render_template('index.html', crop=crop_result, fertilizer=fertilizer_result)
