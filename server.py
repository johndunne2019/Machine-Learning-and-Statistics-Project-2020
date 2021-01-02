# Machine learning and statistics project
# John Dunne G00273895
# flask server to be run in a virtual environment 
# Adapted from lecture series example - https://github.com/ianmcloughlin/random-app/blob/master/rando.py

# flask for web app.
#import flask as fl
from flask import Flask

# Create a new web app.
#app = fl.Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='static')

# Add root route.
# This will serve out the index.html page at the root
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add root to return power value for wind speed entered by user
#@app.route('/api/uniform')
#def uniform():
  #return "test" #{"value": np.random.uniform()}

# run the app when script is run from command line
if __name__ == '__main__' :
    app.run(debug= True)
