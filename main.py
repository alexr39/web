#import depencies
from flask import Flask

#Create instance of flask app
app = Flask(__name__)

#Define route to index and content
@app.route('/')
def home():
    return ('Home Page')

#create page with information about us
@app.route('/about')
def about():
    return('Some information about me')


#run and control script
if (__name__ == '__main__'):
    app.run(debug=True)
