class Site: 
    def __init__(self, name, url, status=None):
        self.name = name
        self.url = url
        self.status = status

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
    def status(self):
        return self._status 
    
    @status.setter
    def status(self, value):
        if not value:
            raise ValueError("Site status cannot be empty.")
        self._status = value

