import threading
import site
from checker.checker import update_sites, load_sites, build_list

print("__Main__ run")
parsed_sites = load_sites("/Users/ndoty/dev/healthcheck/flask-app/checker/sites.yaml")
sites = build_list(parsed_sites)

t = threading.Thread(target=update_sites)
t.start()