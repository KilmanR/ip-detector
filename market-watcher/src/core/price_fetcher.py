import requests

class PriceFetcher:
    def __init__(self, config):        
        self.config = config
    def get_price(self):        
        response = requests.get(self.config["bitcoin_url"], timeout=self.config['timeout'])                
        response.raise_for_status()        
        return float(response.json()['price'])
    def get_usd_rub(self):
        response = requests.get(self.config["exchange_url"], timeout=self.config['timeout'])                
        response.raise_for_status()        
        return response.json()['Valute']['USD']['Value']