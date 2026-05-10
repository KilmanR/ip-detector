import datetime
import json
from config import get_config
from src.core.ip_fetcher import IPFetcher
from src.core.geo_fetcher import GeoFetcher
from src.core.yandex_uploader import YandexDiskUploader

def main():
    config = get_config()
    ip_fetcher = IPFetcher(config)
    
    try:
        current_ip = ip_fetcher.get_ip()
    except Exception:
        pass
        
    try:
        geo_fetcher = GeoFetcher(config)
        geo_data = geo_fetcher.get_geo(current_ip)
        
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{timestamp}.json"
        
        report_data = {
            "ip": current_ip,
            "city": geo_data.get('city'),
            "region": geo_data.get('region'),
            "country": geo_data.get('country'),
            "loc": geo_data.get('loc'),
            "org": geo_data.get('org'),
            "timezone": geo_data.get('timezone')
        }
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)
            
        uploader = YandexDiskUploader(config)
        uploader.upload_file(filename, f'/{filename}')
    except Exception:
        pass

if __name__ == "__main__":
    main()