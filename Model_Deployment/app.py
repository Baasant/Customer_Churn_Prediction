# 1. Library imports
import uvicorn
from fastapi import FastAPI
from req_body import request_body
import pickle

# 2. Create the app object
app = FastAPI()
pickle_in = open("random_forest_classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8080
@app.get('/')
def index():
    return {'message': 'Hello'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8080
@app.get('/{name}')
def get_name(name: str):
    return {'check whether your client will churn or not?!': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def chrun(data:request_body):
    test_data = [[
        data.col_0,
        data.col_1,
        data.col_2,
        data.col_3,
        data.col_4,
        data.col_5,
        data.col_6,
        data.col_7,
        data.account_length,
        data.international_plan,
        data.voice_mail_plan,
        data.number_vmail_messages,
        data.total_day_minutes,
        data.total_day_calls,
        data.total_day_charge,
        data.total_eve_minutes,
        data.total_eve_calls,
        data.total_eve_charge,
        data.total_night_minutes,
        data.total_night_calls,
        data.total_night_charge,
        data.total_intl_minutes,
        data.total_intl_calls,
        data.total_intl_charge,
        data.number_customer_service_calls,
        data.area_code_408,
        data.area_code_415,
        data.area_code_510,
    ]]


    prediction = classifier.predict(test_data)[0]
    if(prediction==0):
        prediction="The client Will stay don't worry"
    else:
        prediction="will churn give him/her some offers"
    return {
        'prediction': prediction
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
