import requests

class GeoFetcher:
    def __init__(self, config):
        self.config = config
        self.token = config['ipinfo_token']

    def get_geo(self, ip):
        url = self.config['ipinfo_url_template'].format(ip=ip, token=self.token)
        response = requests.get(url, timeout=self.config['timeout'])
        response.raise_for_status()
        return response.json()