from flask import Flask, render_template
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello Tamati first flask app'

if __name__ == '__main__':
    app.run(debug=True)
