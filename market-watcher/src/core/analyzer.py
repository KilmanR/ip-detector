class Analyzer:
    def __init__(self, config):        
        self.config = config
    def get_price_difference(self, current_price):
        if current_price - self.config['btc_baseline'] > self.config['btc_alert']:
            return 'SPIKE'
        elif current_price - self.config['btc_baseline'] < - self.config['btc_alert']:
            return 'DROP'
        else:
            return 'STABLE'