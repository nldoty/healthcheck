import yaml
import os
from datetime import datetime
from site_management.site import Site
import threading

yaml_loc = "site_management/sites.yaml"
interval = 15.0

class SiteList: 
    def __init__(self):
        current_time = datetime.now()
        self._checked_time = current_time.strftime("%H:%M:%S %Z")

        parsed_sites = self._load_sites()
        self._site_list = self._build_list(parsed_sites)

    @property
    def checked_time(self):
        return self._checked_time

    def update_time(self):
        current_time = datetime.now()
        self._checked_time = current_time.strftime("%H:%M:%S %Z")

    @property
    def site_list(self):
        return self._site_list
    
    @site_list.setter
    def site_list(self, site_list):
        if not site_list:
            raise ValueError("Site list cannot be empty.")
        self._site_list = site_list
        
    def _load_sites(self): 
        sites_dict = None
        with open(yaml_loc, 'r') as file:
            sites_dict = yaml.safe_load(file) 

        return sites_dict['sites']
    
    def _build_list(self, sites_list):
        site_data = []
        for item in sites_list:
            site_name = item['name']
            url = item['url']
            expected_status = item['expected_status']
            site = Site(site_name, url, expected_status)
            site_data.append(site)
        
        print(site_data)
        return site_data

    def update_sites(self):
        self.update_time()
        for site in self._site_list:
            site.current_status = site.site_status()
        
        t = threading.Timer(interval, self.update_sites)
        t.start()
