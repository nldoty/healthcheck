import requests
import yaml
import threading
from site_management.site import Site
from datetime import datetime

interval = 60.0
site_data = []
last_checked_time = None


def update_time(): 
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S %Z")
    return formatted_time


def load_sites(sites): 
    sites_dict = None
    with open(sites, 'r') as file:
        sites_dict = yaml.safe_load(file) 

    return sites_dict['sites']

def build_list(sites_list):
    for item in sites_list:
        site_name = item['name']
        url = item['url']
        expected_status = item['expected_status']
        site = Site(site_name, url, expected_status)
        site_data.append(site)


def site_status(site, timeout=1):
    try:
        # Use HEAD request for efficiency, only downloads headers
        response = requests.head(site.url)

        return response.status_code == site.expected_status
    
    except requests.exceptions.ConnectionError:
        print("Connection Error (Invalid hostname or no internet)")
        return False
    except requests.exceptions.Timeout:
        print("Timeout Error")
        return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False


def update_sites():
    last_checked_time = update_time()
    for site in site_data:
        site.current_status = site_status(site)
    
    t = threading.Timer(interval, site_status, args=[site])
    t.start()