import requests

class IPFetcher:
    def __init__(self, config):
        self.config = config

    def get_ip(self):
        response = requests.get(self.config['ipify_url'], timeout=self.config['timeout'])
        response.raise_for_status()
        return response.json()['ip']