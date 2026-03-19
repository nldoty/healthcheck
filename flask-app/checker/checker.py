import requests
import yaml
import threading
from site_management.site import Site
from datetime import datetime
interval = 10.0


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
    sites_to_status = []
    for item in sites_list:
        site_name = item['name']
        url = item['url']
        expected_status = item['expected_status']
        site = Site(site_name, url, expected_status)
        sites_to_status.append(site)

    return sites_to_status


def site_status(site, timeout=1):

    print(site)
    url = site.url
    expected_status = site.expected_status

    t = threading.Timer(interval, site_status, args=[site])
    t.start()
    try:
        # Use HEAD request for efficiency, only downloads headers
        response = requests.head(url)
        
        return response.status_code == expected_status
    
    except requests.exceptions.ConnectionError:
        print("Connection Error (Invalid hostname or no internet)")
        return False
    except requests.exceptions.Timeout:
        print("Timeout Error")
        return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False
