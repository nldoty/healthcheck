from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.secret_key = 'yG*+24FNR.37gP,A'
CORS(app, support_credentials=True)

@app.route('/status, methods=['GET'])
@cross_origin(supports_credentials=True)
def get_app_status():
    if request.method == 'GET':
        #getter for the data from the checker
        #make it JSON-y
        #return the body and stuff
        
        })
