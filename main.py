#import depencies
from flask import Flask

#Create instance of flask app
app = Flask(__name__)

#Define route to index
@app.route('/')

#content
def home():
    return ('Home Page')


#run and control script
if (__name__ == '__main__'):
    app.run(debug=True)
