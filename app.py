import flask
from  flask import  request

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    arg = request.arges['arg1']
    return  'Hello worlddd!'

