from http.client import HTTPConnection
from urllib.parse import urlparse

def site_status(url, timeout=1):
    