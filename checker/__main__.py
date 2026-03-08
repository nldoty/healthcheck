import threading
from checker.checker import site_status

sites = [
    ('Earthdata Search', 'https://search.earthdata.nasa.gov'),
    ('Earthdata Login', 'https://urs.earthdata.nasa.gov'),
    ('Earthdata API', 'https://cmr.earthdata.nasa.gov/search/collections.json'),
    ('NASA Earthdata', 'https://www.earthdata.nasa.gov')
]

print("Start program")

for site in sites:
   t = threading.Thread(target=site_status, args=[site])
   t.start()

