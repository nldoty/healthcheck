import json
from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
from site_management.siteList import SiteList

app = Flask(__name__)
app.secret_key = 'yG*+24FNR.37gP,A'
earthdata_list = None

CORS(app, support_credentials=True)
@app.route('/status', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_app_status():
    data = []
    if request.method == 'GET':
        checked_sites = []
        for site in earthdata_list.site_list:
            obj = {
                "name": site.name,
                "url": site.url,
                "status": site.current_status
            }
            checked_sites.append(obj)

        data = {
            "updated_time": earthdata_list.checked_time,
            "site_data": checked_sites
        }
    
    return jsonify(data), 200

with app.app_context(): 
    earthdata_list = SiteList()
    earthdata_list.update_sites()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)