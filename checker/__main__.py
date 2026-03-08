import threading
from checker.checker import site_status

interval = 15.0

print("Start program")

t = threading.Timer(interval, site_status, args=('https://search.earthdata.nasa.gov',))
t.start()