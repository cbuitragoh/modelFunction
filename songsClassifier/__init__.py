import logging
import azure.functions as func
from songsClassifier.helper_funtions import load_data, make_predictions, create_response

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Making inference at the endpoint of the songs-classifier model')
    
    input = req.get_json()
    
    if (isinstance(input, dict)) and ("columns" in input.keys()):
        try:
            # Load data
            df = load_data(input)
        except:
            response = "Error loading data"
            return func.HttpResponse(response, status_code=500)
        try:
            # Make predictions
            predictions = make_predictions("songsClassifier/model.pkl", df)
        except:
            response = "Error making predictions"
            return func.HttpResponse(response, status_code=500)
        try:
            # Response
            response = create_response(predictions)
            return func.HttpResponse(response, status_code=200)
        except:
            response = "Error creating response"
            return func.HttpResponse(response, status_code=500)
    else:
        return func.HttpResponse(body="No input or bad format data provided, \
                                        only json format is accepted", 
                                        status_code=400)