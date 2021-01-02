# Machine learning and statistics project
# John Dunne G00273895
# flask server to be run in a virtual environment 
# Adapted from lecture series example - https://github.com/ianmcloughlin/random-app/blob/master/rando.py

# flask for web app.
import flask as fl
#from flask import Flask

import numpy as np

# import keras and load the saved model
# tensorflow documentation on saving and loading a model - https://www.tensorflow.org/guide/keras/save_and_serialize
from tensorflow import keras
model = keras.models.load_model("model.h5")

# test the model is returning a prediction 
print(model.predict([25]))

# Create a new web app.
app = fl.Flask(__name__)
#app = Flask(__name__, static_url_path='', static_folder='static')

# Add root route.
# This will serve out the index.html page at the root
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add root to return power value for wind speed entered by user
# object of type ndarray is not JSON serializable error was returned at first, I added new return statement with prediction returned as a string
@app.route('/predict')
def predict():
  p = model.predict([25])
  return {"predicted power output": str(p[0][0])}


# from stack overflow - https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
 # prediction = model.predict(np.array(25).tolist()).tolist()
 # return jsonify({'prediction': prediction})

# run the app when script is run from command line
# debug mode is on, the server will reload if any changes made to the file 
#if __name__ == '__main__' :
   #app.run(debug= True)
