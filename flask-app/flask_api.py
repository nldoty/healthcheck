import json
import logging
from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
from checker import checker
from site_management.siteList import SiteList

app = Flask(__name__)
app.secret_key = 'yG*+24FNR.37gP,A'
earthdata_list = None

CORS(app, support_credentials=True)
@app.route('/status', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_app_status():
    json_string = []
    if request.method == 'GET':
        for site in earthdata_list.site_list:
            json_string.append(json.dumps(site.__dict__))
            print(json_string)
    
    return jsonify(json_string), 200

with app.app_context(): 
    earthdata_list = SiteList()
    earthdata_list.update_sites()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)