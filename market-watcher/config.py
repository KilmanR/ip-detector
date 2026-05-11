BITCOIN_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
EXCHANGE_URL = "https://www.cbr-xml-daily.ru/daily_json.js"
REQUEST_TIMEOUT = 10
BTC_ALERT_THRESHOLD = 1000
USD_ALERT_THRESHOLD = 0.5
TARGET_CURRENCY = "RUB"
btc_baseline = 80000
def get_config():
    return {
        "bitcoin_url": BITCOIN_URL,
        "exchange_url": EXCHANGE_URL,
        "btc_alert" : BTC_ALERT_THRESHOLD,
        "usd_alert" : USD_ALERT_THRESHOLD,
        "target_currency" : TARGET_CURRENCY,
        "btc_baseline": btc_baseline,
        "timeout": REQUEST_TIMEOUT
    }