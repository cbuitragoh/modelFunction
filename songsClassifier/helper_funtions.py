import pickle
import json
import pandas as pd

def make_predictions(model_name, data):
    # Load model
    model = pickle.load(open(model_name, 'rb'))
    # Make predictions
    predictions = model.predict(data)
    return predictions


def load_data(input):
    #load file
    file = input
    #extract columns label
    columns = file['columns']
    #extract data vaules
    data = list(file['data'])
    #create dataframe
    df = pd.DataFrame(data, columns=columns)
    #remove target column
    df.drop(columns=["in_spotify_playlists"], inplace=True)
    #rename released_year column
    df.rename(columns={"released_year": "age_of_song"}, inplace=True)
    #transform value age_of_song column
    df["age_of_song"] = df["age_of_song"].apply(lambda x: 2023-x)
    
    return df


def create_response(predictions):
    #create response
    predictions = predictions.tolist()
    response = {"predictions": predictions}
    response = json.dumps(response) 
   
    return response
  