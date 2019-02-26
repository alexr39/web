#import depencies
from flask import Flask, render_template

#Create instance of flask app
app = Flask(__name__)

#Define route to index and content
@app.route('/')
def home():
    return render_template('Home.html')

#create page with information about us
@app.route('/blog')
def about():
    return render_template('blog.html')


#run and control script
if (__name__ == '__main__'):
    app.run(debug=True)
