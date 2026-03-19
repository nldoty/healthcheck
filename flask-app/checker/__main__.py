import threading
import site
from checker.checker import site_status, load_sites, build_list

print("__Main__ run")
parsed_sites = load_sites("/Users/ndoty/dev/healthcheck/flask-app/checker/sites.yaml")
sites = build_list(parsed_sites)

for site in sites:
   t = threading.Thread(target=site_status, args=[site])
   t.start()

