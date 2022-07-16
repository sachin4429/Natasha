from flask import Flask,request,jsonify
import requests
import json
 
app = Flask(__name__)

@app.route('/',methods=['POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
