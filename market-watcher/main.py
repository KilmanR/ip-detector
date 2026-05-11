from config import get_config
from src.core.price_fetcher import PriceFetcher
from src.core.analyzer import Analyzer
from src.core.reporter import Reporter

def main():
    config = get_config()
    fetcher = PriceFetcher(config)
    btc_price = fetcher.get_price()
    usd_rub = fetcher.get_usd_rub()
    analyzer = Analyzer(config)    
    status = analyzer.get_price_difference(btc_price)
    reporter = Reporter(config)
    message = reporter.save_report(btc_price, usd_rub, status)
    print(message)
    print(f"BTC: {btc_price}")
    print(f"USD/RUB: {usd_rub}")
    print(f"Status: {status}")
    # print(fetcher.get_price())
    # print(fetcher.get_usd_rub())
if __name__ == "__main__":
    main()
