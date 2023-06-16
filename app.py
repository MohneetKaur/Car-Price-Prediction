# Flask Application Code

import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained pipeline
with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# Load the categorical columns
with open('encoded_columns.pkl', 'rb') as file:
    categorical_columns = pickle.load(file)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the feature values from the form
    symboling = int(request.form['symboling'])
    fueltype = request.form['fueltype']
    aspiration = request.form['aspiration']
    doornumber = request.form['doornumber']
    carbody = request.form['carbody']
    drivewheel = request.form['drivewheel']
    enginelocation = request.form['enginelocation']
    wheelbase = float(request.form['wheelbase'])
    carlength = float(request.form['carlength'])
    carwidth = float(request.form['carwidth'])
    carheight = float(request.form['carheight'])
    curbweight = float(request.form['curbweight'])
    enginetype = request.form['enginetype']
    cylindernumber = request.form['cylindernumber']
    enginesize = int(request.form['enginesize'])
    fuelsystem = request.form['fuelsystem']
    boreratio = float(request.form['boreratio'])
    stroke = float(request.form['stroke'])
    compressionratio = float(request.form['compressionratio'])
    horsepower = int(request.form['horsepower'])
    peakrpm = int(request.form['peakrpm'])
    citympg = int(request.form['citympg'])
    highwaympg = int(request.form['highwaympg'])

    # Create a DataFrame for prediction
    data = pd.DataFrame([[symboling, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation,
                          wheelbase, carlength, carwidth, carheight, curbweight, enginetype, cylindernumber,
                          enginesize, fuelsystem, boreratio, stroke, compressionratio, horsepower, peakrpm,
                          citympg, highwaympg]], columns=['symboling', 'fueltype', 'aspiration', 'doornumber',
                                                         'carbody', 'drivewheel', 'enginelocation', 'wheelbase',
                                                         'carlength', 'carwidth', 'carheight', 'curbweight',
                                                         'enginetype', 'cylindernumber', 'enginesize', 'fuelsystem',
                                                         'boreratio', 'stroke', 'compressionratio', 'horsepower',
                                                         'peakrpm', 'citympg', 'highwaympg'])

    # Make the prediction
    price = pipeline.predict(data)[0]

    # Render the template with the prediction result
    return render_template('index.html', prediction=f"The predicted price is: {price:.2f}")

if __name__ == '__main__':
    app.run(debug=True)

