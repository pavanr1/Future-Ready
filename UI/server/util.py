import json 
import pickle

__locations = None
__data_columns = None
__model = None 

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    
    print("Hello")
    with open("C:\Users\Pruthvik Kashyap S\OneDrive\Desktop\Machine Learning\Examples\Ex21 Data Cleaning (Real Estate Price Prediction Project)\UI\server\artifacts\columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        
    with open("artifacts/bengaluru_home_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())