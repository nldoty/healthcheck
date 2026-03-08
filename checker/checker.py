import requests
import threading
interval = 15.0


def site_status(site, timeout=1):
    site_name = site[0]
    url = site[1]
    t = threading.Timer(interval, site_status, args=[site])
    t.start()
    print('Checking status of site {}...'.format(site_name))
    try:
        # Use HEAD request for efficiency, only downloads headers
        response = requests.head(url)
        # Check if status code is exactly 200
        if response.status_code == 200:
            print("Website Available (200 OK)")
            return True
        else:
            print(f"Status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("Connection Error (Invalid hostname or no internet)")
        return False
    except requests.exceptions.Timeout:
        print("Timeout Error")
        return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False
