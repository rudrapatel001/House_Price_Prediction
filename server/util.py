import json
import pickle

__location = None
__data_columns = None
__model = None



def get_location_names():
    return __location


def load_saved_artifacts():
    print('Loading the saved artifacts')
    global __data_columns
    global __location
    
    with open("server/artifacts/columns.json",'r') as f:
       __data_columns = json.load(f)['data_columns']
       __location = __data_columns[3:]
       
    with open("server/artifacts/Home_price_prediciton.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...Done")
        
        
        
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())