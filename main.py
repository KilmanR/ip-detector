# Точка входа в приложение IP Detector
import datetime, json, logging, sys
from config import get_config
from src.core.ip_fetcher import IPFetcher
from src.core.geo_fetcher import GeoFetcher
from src.core.yandex_uploader import YandexDiskUploader

# 🔧 Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def main():
    config = get_config()
    logging.info("=" * 50)
    logging.info(" IP Detector - Определение геолокации")
    logging.info("=" * 50)
    logging.info(f"✅ Конфигурация загружена")
    logging.info(f"🔑 Токен ipinfo: {'✓' if config['ipinfo_token'] else '✗'}")
    logging.info(f"🔑 Токен Яндекс.Диск: {'✓' if config['yandex_token'] else '✗'}")
    logging.info("=" * 50)

    current_ip = None
    try:
        ip_fetcher = IPFetcher(config)
        current_ip = ip_fetcher.get_ip()
        logging.info(f"🌍 Твой внешний IP: {current_ip}")
    except Exception as e:
        logging.error(f"❌ Не удалось получить IP: {e}")
        return  # 🔥 Важно: выходим, если нет IP

    try:
        geo_fetcher = GeoFetcher(config)
        geo_data = geo_fetcher.get_geo(current_ip)
        
        logging.info(f"📍 Город: {geo_data.get('city', 'Неизвестно')}")
        logging.info(f"📍 Регион: {geo_data.get('region', 'Неизвестно')}")
        logging.info(f"📍 Координаты: {geo_data.get('loc', 'Неизвестно')}")
        logging.info(f"📍 Провайдер: {geo_data.get('org', 'Неизвестно')}")

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{timestamp}.json"
        
        logging.info(f"💾 Сохраняем отчёт в: {filename}")
        
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
        
        logging.info("📤 Загрузка на Яндекс.Диск...")
        uploader = YandexDiskUploader(config)
        # 🔥 Добавляем папку и overwrite
        uploader.upload_file(filename, f"/{filename}", overwrite=True)
        
        logging.info("✅ Всё готово! Проверь Яндекс.Диск → папка /ip_reports/")
        
    except Exception as e:
        logging.error(f"❌ Ошибка выполнения: {e}", exc_info=True)

if __name__ == "__main__":
    main()