from scipy.sparse import csr_matrix
from joblib import load
import numpy as np

# converts data to sparse format
def to_sparse(data):

    data = np.array(data, dtype=float)
    return csr_matrix(data)


def to_dense(data):
    return csr_matrix.todense(data)


def load_location_encoder():
    data_encoder = load('location_encoder.joblib')
    return data_encoder
    
def load_listing_encoder():
    data_encoder = load('listing_type_encoder.joblib')
    return data_encoder
    
    
def encode_to_numerical_listing_type(listing_col):
    
    data_encoder = load_listing_encoder()
    
    feature_list = listing_col.reshape(-1, 1)
    encoded_feature = data_encoder.transform(feature_list)
    
    return encoded_feature

def encode_to_numerical_location(listing_col):
    
    data_encoder = load_location_encoder()
    
    feature_list = listing_col.reshape(-1, 1)
    encoded_feature = data_encoder.transform(feature_list)
    
    return encoded_feature
