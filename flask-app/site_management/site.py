import requests

class Site: 
    def __init__(self, name, url, expected_status, current_status=None):
        self._name = name
        self._url = url
        self._expected_status = expected_status
        self._current_status = current_status

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Site name cannot be empty.")
        self._name = value

    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, value):
        if not value:
            raise ValueError("Site URL cannot be empty.")
        self._url = value

    @property
    def expected_status(self):
            return self._name
        
    @expected_status.setter
    def expected_status(self, value):
        if not value:
            raise ValueError("Site name cannot be empty.")
        self._expected_status = value

    @property
    def current_status(self):
        return self._current_status 
    
    @current_status.setter
    def current_status(self, value):
        # This value CAN be empty, when status has not been set.
        self._current_status = value

    def site_status(self):
        try:
            # Use HEAD request for efficiency, only downloads headers
            response = requests.head(self._url)

            print("Expected status: " + str(self._expected_status))
            return response.status_code == self._expected_status
        
        except requests.exceptions.ConnectionError:
            print("Connection Error (Invalid hostname or no internet)")
            return False
        except requests.exceptions.Timeout:
            print("Timeout Error")
            return False
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return False
