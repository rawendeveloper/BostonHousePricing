import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))

# Load the scaler (if applicable)
scalar = pickle.load(open('scaling.pkl', 'rb'))  # Ensure scaler.pkl exists if required

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    input_data = np.array(list(data.values())).reshape(1, -1)
    transformed_data = scalar.transform(input_data)
    output = regmodel.predict(transformed_data)
    print(output[0])
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)
