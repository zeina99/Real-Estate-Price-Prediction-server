import joblib
from flask import Flask, request

import scipy as sp
# from joblib import load

app = Flask(__name__)

model = joblib.load('model_file.joblib')


# def to_sparse(data):
#     return sp.sparse.csr_matrix(data)


# def to_dense(data):
#     return sp.sparse.csr_matrix.todense(data)


# to_dense = FunctionTransformer(to_dense)
# to_sparse_transformer = FunctionTransformer(to_sparse)


@app.route("/", methods=['POST'])
def index():
    req_data = request.get_json()
    num_of_bedrooms = req_data['bedrooms']
    num_of_bathrooms = req_data['bathrooms']
    area = req_data['area']
    location = req_data['location']
    listing_type = req_data['listing_type']
    description = req_data['description']

    predicted_price = model.predict(
       [ [num_of_bathrooms, num_of_bedrooms, area, location, listing_type, description]])
    return {
        "price": predicted_price
    }
