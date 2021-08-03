from flask import Flask, request
import joblib
# from joblib import load

app = Flask(__name__)

model = joblib.load('model_file.joblib')



@app.route("/", methods=['POST'])
def index():
    req_data = request.get_json()
    num_of_bedrooms = req_data['bedrooms']
    num_of_bathrooms = req_data['bathrooms']
    area = req_data['area']
    location = req_data['location']
    listing_type = req_data['listing_type']
    description = req_data['description']

    # make sure input to predict is in this order 
    # listing_type	bedrooms	bathrooms	area	location	description
    predicted_price = model.predict(
       [ [listing_type, num_of_bedrooms, num_of_bathrooms, area, location, description]])

    predicted_price = predicted_price[0]

    return {
        "price": predicted_price
    }
