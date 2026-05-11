from config import get_config
from src.core.price_fetcher import PriceFetcher
from src.core.analyzer import Analyzer

def main():
    config = get_config()
    fetcher = PriceFetcher(config)
    btc_price = fetcher.get_price()
    usd_rub = fetcher.get_usd_rub()
    analyzer = Analyzer(config)
    status = analyzer.get_price_difference(btc_price)
    print(f"BTC: {btc_price}")
    print(f"USD/RUB: {usd_rub}")
    print(f"Status: {status}")
    # print(fetcher.get_price())
    # print(fetcher.get_usd_rub())
if __name__ == "__main__":
    main()
