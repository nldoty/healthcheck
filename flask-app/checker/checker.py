import requests
from site_management.site import Site
from datetime import datetime

interval = 10.0
last_checked_time = 3456

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

