# Machine learning and statistics project
# John Dunne G00273895
# flask server to be run in a virtual environment or on local machine
# Adapted from lecture series example - https://github.com/ianmcloughlin/random-app/blob/master/rando.py
# To run on windows machine:
# set FLASK_APP=server.py
# python -m flask run
# when server is running access on web browser at - http://127.0.0.1:5000/

# import flask for web app.
#import flask as fl - alternative way to import flask
from flask import Flask

# import keras and load the saved model
# tensorflow documentation on saving and loading a model - https://www.tensorflow.org/guide/keras/save_and_serialize
from tensorflow import keras
model = keras.models.load_model("model.h5")

# Create a new web app.
#app = fl.Flask(__name__)  - alternative way to create a new app
app = Flask(__name__, static_url_path='', static_folder='static')

# Add root route.
# This will serve out the index.html page at the root
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add route to return power value for wind speed entered by user with a GET method
# tested and returning power output successfully at app route with response 200 - http://127.0.0.1:5000/predict/10
# tested with curl call below
# curl "http://127.0.0.1:5000/predict/20
# object of type ndarray is not JSON serializable error was returned at first, I added new return statement with prediction returned as a string
# from stack overflow - https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
@app.route('/predict/<int:x>', methods=['GET'])
def predict(x):
  prediction = model.predict([x])
  #return {"predicted power output": str(prediction[0][0])}
  return str(prediction[0][0])


# debug mode turned on for testing purposes, commented out in final production version
#if __name__ == '__main__' :
  #app.run(debug= True)
